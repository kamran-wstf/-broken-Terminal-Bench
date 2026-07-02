You are given an Apache-style access log file at `/app/access.log`.

Read the log and produce a JSON report at `/app/report.json` containing exactly
the following keys:

- `total_requests`: integer — the number of non-empty lines counted as requests.
- `unique_ips`: integer — the number of distinct client IP addresses seen (the first token on each log line).
- `top_path`: string or null — the most frequently requested path extracted from the request line (the path following the HTTP method, e.g. `"GET /index.html HTTP/1.1"`). If no paths are found, set `top_path` to null.

Behavioral details:
- Skip empty lines and malformed lines that do not contain at least one token.
- Count only lines that appear to contain an HTTP method followed by a path when determining `top_path`.
- The report file must be valid JSON, be non-empty, and conform to the key names and types above.

Place the report at `/app/report.json`. The verifier will validate presence, JSON structure, and types for these keys.
