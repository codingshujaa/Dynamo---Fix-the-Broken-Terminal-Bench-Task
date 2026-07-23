# Fixed Terminal-Bench Harbor Task

This repo contains the repaired `dynamo/log-report` task.

The task asks an agent to read `/app/access.log` and write a small JSON report to `/app/report.json`. The fixed version now has a clear prompt, a pinned Docker image, no leaked solution file and a verifier that checks the real JSON values.

## What Was Fixed

- `task.toml` now collects `/app/report.json` as a top-level artifact array.
- The Dockerfile uses a pinned approved Python image.
- The leaked `solution_hint.py` file was removed.
- The verifier checks the report schema, value types and exact values.
- `tests/test.sh` writes `/logs/verifier/reward.txt` and `/logs/verifier/ctrf.json`.
- `instruction.md` now says exactly what output is required.

## Verification

I ran the fixed task with Docker Desktop and Harbor.

```text
harbor run -p log-report -a oracle -n 1 --job-name log-report-oracle-fixed
```

Result:

```text
Reward: 1
CTRF summary: 4 tests, 4 passed and 0 failed
Produced report: {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
```

I also ran the no-op agent.

```text
harbor run -p log-report -a nop -n 1 --job-name log-report-nop-fixed
```

Result:

```text
Reward: 0
CTRF summary: 4 tests, 0 passed and 4 failed
Failure reason: missing /app/report.json
```
