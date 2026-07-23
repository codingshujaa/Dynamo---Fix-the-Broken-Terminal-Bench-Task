You are in `/app` with an Apache-style access log at `/app/access.log`. Produce a JSON report at `/app/report.json`.

Success criteria:

1. `/app/report.json` exists and is a JSON object with exactly these keys and value types: `total_requests` as an integer, `unique_ips` as an integer and `top_path` as a string.
2. `total_requests` is the number of non-empty access-log entries.
3. `unique_ips` is the number of distinct client IP addresses, using the first whitespace-delimited field on each log line.
4. `top_path` is the request path that appears most often inside the quoted HTTP request. For example, from `"GET /index.html HTTP/1.1"`, the path is `/index.html`.

Use JSON values directly.
