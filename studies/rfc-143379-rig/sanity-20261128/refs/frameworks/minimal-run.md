# Minimal Run Workflow

## Inputs

- one low-risk task;
- one target artifact;
- the Schema envelope;
- a workspace with a writable `runs/` directory.

## Steps

1. **Deconstruct:** write the task, desired outcome, constraints, and unknowns.
2. **Sense:** classify the task domain.
3. **Choose:** select one mechanism and explain why alternatives are deferred.
4. **Calibrate:** record confidence, base-rate assumption, and counter-evidence.
5. **Probe:** perform the smallest useful reversible action.
6. **Review:** compare the result with the declared success criterion.
7. **Record:** save the artifact and a run record.
8. **Compose-check:** mark each required mechanism as fired or absent.

## No shared-state rule

Workers may write:

```text
runs/<run-id>/workers/<worker-id>/artifact.md
runs/<run-id>/workers/<worker-id>/summary.md
```

Only the parent or designated fold step may update a shared index.
