# Coding and engineering

- Map the normal entry point and the files it calls. Inspect project instructions, state, dependencies, and related tests. Reproduce a reported bug with authorized, ordinary inputs when possible. For a review, prioritize verified issues by impact and cite exact file paths and lines.
- Make a small fix at the source. Consider supported inputs, earlier data versions, concurrency, permissions, partial failures, and retries where relevant. Reuse existing interfaces and avoid unrelated rewrites.
- Run the applicable format, lint, type, test, and build checks. Add a targeted regression test when existing coverage misses the failure. For Java exercises, respect the exact stdin/stdout format and entry-point requirements. For web APIs, check error handling and permissions with test data.
- Trace a change through the product before shipping. For a UI feature, exercise it through the browser. For database changes, review the migration, rollback or recovery route, and access policies. For security work, focus on defensive diagnosis and remediation.
- Deliver the implementation, test evidence, and any limitation. Create commits, PRs, or deployments when authorized for the task.
