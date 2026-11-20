"""Commit a prepared summary, physical target, generation and receipt atomically."""
import os
import uuid
from hermes_state_mutation_prepared import validate_prepared


def compress_in_transaction(db, conn, session_id, payload, prepared):
    snapshot = validate_prepared(db, conn, session_id, prepared)
    policy = snapshot['receipt']['policy']
    target = snapshot['target']
    from hermes_state_worker_compression import archive_on_connection, publish_on_connection
    # No worker/turn/compactor can be active: validate_prepared checks those
    # obligations on this exact connection. No separate legacy transaction runs.
    if prepared['in_place']:
        child = target
        # F2 shadow wiring (M3 Probe A + studies/.../probes/release_point_gate.py): cite-or-hold
        # before the archive release. INERT unless GOVERNED_COMPACTION_RELEASE_RULE=ON — the
        # two-way door: shadow -> enforce, the flag flip is the rollback, bytes intact.
        if os.environ.get("GOVERNED_COMPACTION_RELEASE_RULE", "").lower() in ("on", "1", "true"):
            rel = (snapshot.get("release_event_id") if isinstance(snapshot, dict) else None)
            if not (isinstance(rel, str) and len(rel) >= 16):
                raise ValueError(
                    "F2-HOLD: no citable release_event_id in the snapshot receipt; the block is "
                    "held (archive deferred) — release a block only when the teacher can cite "
                    "the event that ended its use")
        archive_on_connection(db, conn, target, prepared['messages'])
        affected = {session_id, target}
    else:
        child = uuid.uuid4().hex
        publish_on_connection(db, conn, parent_session_id=target, child_session_id=child,
            source=policy['source'], model=policy['model'], messages=prepared['messages'],
            model_config={'_compressed_from': target}, cwd=policy['cwd'], require_compression_lease=False)
        affected = set()  # Rotation publication already advances the logical revision.
    conn.execute('UPDATE sessions SET runtime_generation=runtime_generation+1 WHERE id=?', (session_id,))
    generation = conn.execute('SELECT runtime_generation FROM sessions WHERE id=?', (session_id,)).fetchone()[0]
    return affected, {'target_session_id': child, 'previous_target_session_id': target,
                   'execution_generation': generation, 'message_count': len(prepared['messages']),
                   'summary': prepared.get('summary')}
