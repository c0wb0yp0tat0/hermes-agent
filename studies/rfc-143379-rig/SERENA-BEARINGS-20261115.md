# SERENA-BEARINGS-20261115

## THE TRUE SURFACE

### Dashboard and HTTP Service
- **Dashboard Face**: Accessible via `GET http://127.0.0.1:24282/dashboard/`. The dashboard is a Werkzeug-based Python web application (Werkzeug/3.1.7, Python/3.13.15). It redirects to `/dashboard/` upon accessing the root endpoint (`/`).
- **API Routes**: No documented `/api/*` or `/openapi.json` routes were found. The `/docs` endpoint does not provide any API documentation.
- **MCP Route**: No `/mcp`, `/sse`, `/mcp/sse`, `/health`, or `/v1/models` routes were confirmed. These endpoints returned HTTP 404 errors.

### Host-Side Analysis
- **Serena Help**: The `serena.exe --help` command was not executed due to the bounded probe limit. However, the process `serena.exe` is running with the command `serena.exe start-mcp-server --context claude-code --project Downloads`. This suggests that Serena is a local MCP server with a specific context and project.

### MCP Transport
- **MCP Server Status**: The server is running on port `24282` and is accessible via the SSH tunnel. However, no MCP-specific routes or tools were confirmed through the bounded probes.

### Honest Markers
- **MCP Route**: Unconfirmed. No evidence of an MCP route or tools was found through the bounded probes.
- **Tools Inventory**: Unread. No tools were listed or accessible through the dashboard or API routes.
- **Model/API Nature**: Unclear. The server is running as an MCP server, but its specific functionality (e.g., LLM endpoint) is not confirmed.

## THE WIRING OPTIONS

### Option (a): Harness MCP-Executor Leg
- **Design Sketch**: The harness would call Serena's tools over the SSH tunnel as the write surface. This would involve:
  - **Plugging**: Integrating Serena's tools into the harness's tool executor.
  - **Replacement**: Replacing the current write surface with Serena's tools.
  - **Fallback**: If Serena degrades, the harness would revert to the current writer.

- **Failure Classes Addressed**: This option could address read-scatter, write-overwrite, and commit-phase failures by providing a deterministic local write surface.

### Option (b): MCP-Client Connector Route
- **Design Sketch**: The rig's gateway would connect as an MCP client to Serena. This would:
  - **Plugging**: Allow Serena's tools to be callable rig-side.
  - **Replacement**: Integrate Serena's tools into the rig's workflow.
  - **Fallback**: If Serena fails, the rig would revert to its default tools.

- **Failure Classes Addressed**: This option could mitigate failures by leveraging Serena's deterministic nature for write operations.

### Option (c): Host-Side Script Route
- **Design Sketch**: The harness's terminal executor would call Serena via the SSH route. This would:
  - **Plugging**: Use SSH to invoke Serena's tools directly.
  - **Replacement**: Replace the current write operations with SSH-based calls.
  - **Fallback**: If SSH or Serena fails, the harness would revert to the current writer.

- **Failure Classes Addressed**: This option could handle write-overwrite and commit-phase failures by ensuring deterministic execution via SSH.

## THE TWO-WAY-DOOR PLAN

### Config Delta
- **Tunnel**: Establish an SSH tunnel to `127.0.0.1:24282`.
- **Endpoint**: Configure the harness to use Serena's tools via the tunnel.
- **Harness Flag**: Add a flag to the harness configuration to enable Serena integration.

### Rollback Plan
- **Remove the Flag**: Disable the flag in the harness configuration.
- **Drop the Tunnel**: Terminate the SSH tunnel.
- **Writer Return**: The harness reverts to the standard writer.

### Success Criterion
- **Compose-Lane Landings**: Achieve zero write-class failures in N landings through Serena's tools.

### Exit Criterion
- **Failure Threshold**: Two consecutive failures would trigger the rollback and return to the standard writer.

## THE STAGE-2 SEED

### Confirmed Surface Facts
- **Serena Server**: Running on port `24282` with context `claude-code` and project `Downloads`.
- **Transport**: Werkzeug-based web app with no confirmed MCP routes or tools.
- **Tunnel**: SSH tunnel to `127.0.0.1:24282` is live.

### Chosen Option Sketch
- **Option (a)**: Harness MCP-Executor Leg is the primary candidate for integration due to its deterministic nature and potential to address multiple failure classes.

### Harness Integration Points
- **Tool Executor**: The harness's tool executor needs to be updated to call Serena's tools.
- **Fallback Mechanism**: Ensure the harness can revert to the current writer if Serena fails.

## THE HONEST MARKERS
- **MCP Route**: Unconfirmed. No evidence of an MCP route was found.
- **Tools Inventory**: Unread. No tools were accessible or listed.
- **Model/API Nature**: Unclear. The server is an MCP server, but its specific capabilities (e.g., LLM endpoint) are not confirmed.

---