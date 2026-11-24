# Websites and deployment

1. Write down the page goal, audience, primary action, and required states. Turn references into principles such as composition, hierarchy, and motion, and make an original interface.
2. Use the existing framework when the project has one. Build responsive layout and a working primary flow first. Make forms, navigation, download links, and calls to action functional. Include metadata and useful fallback states.
3. Check mobile and desktop layouts, keyboard navigation, contrast, reduced motion, loading and error states, and console errors. Use browser screenshots or Playwright traces for visual and interaction issues.
4. Choose hosting from the workload, existing account, budget, and deployment target. Use Vercel for a compatible frontend or preview, Hostinger for the hosting setup the project calls for, and AWS for backend or worker workloads when appropriate. Verify current runtime and pricing constraints before recommending production architecture.
5. Verify a preview using real routes and mobile sizing before a production rollout. Check base URLs, callback allowlists, redirect links, build settings, and database access. Keep secrets server-side and use environment-specific values. When a deployment was requested, verify the deployed URL and a critical user path.
