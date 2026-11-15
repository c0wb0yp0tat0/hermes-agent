# SERENA-HARNESS-PLAN-20261115

## THE LEG'S DESIGN

### Overview
The MCP-executor leg integrates a local MCP client (Python SDK `mcp>=1.27,<2`) into the harness to route write-class calls through Serena's tools. The leg is optional, controlled by a flag (`--executor mcp` or environment variable `HARNESS_EXECUTOR=mcp-serena`), and defaults to the standard writer if disabled.

### Configurations
1. **Flag Activation**:
   - Command-line flag: `--executor mcp`
   - Environment variable: `HARNESS_EXECUTOR=mcp-serena`
   - Default: Standard writer (no flag or `HARNESS_EXECUTOR=default`).

2. **Executor Process**:
   - **Preferred Route**: StdIO Launch
     - The harness spawns a subprocess for the MCP client and launches Serena via `serena.exe start-mcp-server --transport streamable-http` (stdio-bound).
     - The tunnel is established locally between the harness and the MCP client.
   - **Fallback Route**: HTTP Transport
     - If the host is configured with the `--transport streamable-http` flag, the harness connects to Serena via HTTP over the SSH tunnel.

3. **Write-Call Routing**:
   - **Symbol-Level Tools**: Write calls targeting symbol-level operations (e.g., `rename_symbol`, `replace_symbol_body`) are routed to Serena's LSP tools.
   - **Pattern-Based Tools**: Write calls targeting content replacement (e.g., `replace_content`, `write_file`) are routed to Serena's pattern-based tools.
   - **Default Writer**: Non-write calls or calls not fitting the above criteria default to the standard writer.

4. **Call-Result Pairing**:
   - Each write call is paired with a result from Serena's tools via the MCP session protocol.
   - Results are truncated to the harness's result budget (e.g., file content limited to 1MB).

5. **Bounded Results**:
   - Tool outputs are constrained to the harness's result budgets (e.g., file content, shell command output).
   - Exceeding the budget triggers a fallback to the standard writer.


## THE RECEIPT FLOOR

### Postcondition Check
After Serena's write tool returns, the executor performs a re-read byte-check of the artifact to verify correctness. This ensures the receipt is based on actual file content, not Serena's tool output.

- **Verification Process**:
  - Re-read the artifact post-write.
  - Compare the hash or content of the artifact against the intended bytes.
  - If the re-read fails, the result is marked as a failure, and the harness reverts to the standard writer.

- **Fold-Step Unchanged**: The fold-step's verification logic remains unchanged; only the write surface is modified.


## THE TWO-WAY DOOR, EXACT

### Config Delta
- **Flag**: `--executor mcp` or `HARNESS_EXECUTOR=mcp-serena`.
- **Executor Process**: The subprocess for the MCP client and Serena.
- **Tunnel**: SSH tunnel or HTTP connection to Serena.

### Rollback Plan
- **Remove the Flag**: Disable the flag or unset the environment variable.
- **Drop the Tunnel**: Terminate the SSH tunnel or HTTP connection.
- **Writer Return**: The harness reverts to the standard writer.

### Success Criterion
- **N Compose-Lane Landings**: Achieve zero write-class failures in **N=3** compose-lane landings through Serena's tools.

### Exit Criterion
- **Failure Threshold**: Two consecutive write-class failures trigger the rollback and return to the standard writer.


## THE TEST PLAN

### Minimal Live Probe
1. **Setup**:
   - Launch the harness with the `--executor mcp` flag.
   - Ensure the SSH tunnel or HTTP connection to Serena is active.

2. **Test Brief**:
   - Create a small artifact (e.g., a 1KB text file) for a write-only compose brief.
   - Execute the brief through the MCP-executor leg.

3. **Verification**:
   - Re-read the artifact post-write.
   - Confirm the artifact matches the intended bytes (hash/cmp).
   - Record meters (e.g., latency, success/failure counts).

4. **Expected Outcome**:
   - The artifact lands correctly with the re-read receipt.
   - Meters reflect successful execution through the leg.


## THE HONEST MARKERS

### Unverified Items
- **Serena's Tool List**: Unread. The LSP backend's language coverage and tool inventory are unverified.
- **StdIO Launch on Windows**: Unverified. The process-lifetime and stability of the stdio-launch route on Windows are untested.
- **SDK Availability**: Unverified. The availability and compatibility of the MCP SDK (`mcp>=1.27,<2`) on the rig-side are unconfirmed.

### Assumptions
- The SSH tunnel and HTTP transport are stable and accessible.
- Serena's tools are deterministic for write-class operations.
- The harness's result budgets are respected by Serena's tools.

---