> Historical inventory from the original account. Setup commands and service listings are recorded as references.

# Skills and Plugins Inventory

Source: scroll through the Claude plugin directory. Repo names were read from small
on-screen text, so a few may be slightly off. The installation status below records verified sources and identifies unresolved items.

---

## How to install

### Option A: Claude Code
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install <plugin-name>@claude-plugins-official
```
Community marketplace: `/plugin marketplace add anthropics/claude-plugins-community`

### Option B: Other agents that use the SKILL.md format (Codex, Cursor, Copilot, Gemini CLI, etc.)
Many skill repos can be installed with the `skills` CLI:
```
npx skills add <owner>/<repo> -g
```
Or manually: clone the repo and copy the skill folder (the one containing `SKILL.md`) into your agent's skills directory.
```
git clone https://github.com/<owner>/<repo>.git
```
Note: Claude-specific parts (connectors, hooks, slash commands, MCP servers) may not work outside Claude.
Plain `SKILL.md` skills transfer best.

---

## Anthropic

| Name | Source |
|---|---|
| Bio Research, Brand Voice, Customer Support, Data, Design, Engineering, Enterprise Search, Finance, Human Resources, Legal, Marketing, Operations, Product Management, Sales, Small Business | https://github.com/anthropics/knowledge-work-plugins |
| frontend-design, mcp-server-dev, skill-creator | https://github.com/anthropics/claude-plugins-official |
| market-researcher | https://github.com/anthropics/financial-services |
| Figma | https://github.com/figma/mcp-server-guide |

Partner connectors (install from Browse plugins in the Claude app): Zoom, PDF Viewer, Modern Web Guidance (Google Chrome), Postiz, Bright Data, Product Tracking (Accoil), SearchFit SEO.

---

## Community skills

| Name | Source |
|---|---|
| animation-studio | https://github.com/I-afaqrashid/claude-animation-studio |
| AnimatedWebs | https://github.com/iboss21/animatedwebs-claude |
| B2B Sales Enablement | https://github.com/shashwatgtm/b2b-sales-enablement |
| Bigdata.com | https://github.com/bigdata-com/bigdata-plugins-marketplace |
| Crypto Spot Futures Analyzer | https://github.com/keycustodian09-spec/crypto-spot-futures-analyzer |
| Cryptowisser News | https://github.com/cryptowisser-com/cryptowisser-news-plugin |
| design-superpowers | https://github.com/lsdimi/design-superpowers |
| icon-creator | https://github.com/ultrathinker/icon-creator |
| image-generation | https://github.com/ahmedraza28/image-generation-skill |
| Instagram channel | https://github.com/riasistemas/claude-channel-instagram |
| liquid-glass-skills | https://github.com/yordilorenzo/liquid-glass-skills |
| Motion Reel | https://github.com/aries-spring/motion-reel |
| roblox-dev | https://github.com/ivar-anon/roblox-dev |
| S&P Global | https://github.com/kensho-technologies/spglobal-agent-skills |
| Senior Engineering Partner | https://github.com/bjgreenberg/senior-engineering-partner |
| stock-portfolio-valuation | https://github.com/apack1001/stock-portfolio-valuation |
| stockinsights.ai (India) | https://github.com/stockinsights-ai/plugins |
| Supabase | https://github.com/supabase-community/supabase-plugin |
| token-usage | https://github.com/wizzouk2/token-usage |
| UI Design Review, Website Design | https://github.com/uxkin/agent |
| UI/UX Behaves | https://github.com/lohbrandt/ui-ux-behaves |
| UX Agent Skills | https://github.com/carlsz/ux-agent-skills |
| video-to-code-skill | https://github.com/piotrlason/video-to-code-skill |
| watch-video (confirmed) | https://github.com/MarcinSufa/claude-watch-video |
| writing-quality | https://github.com/israelmusondaayliffe/plugins |
| YouTube Transcriber | https://github.com/msapps-mobile/claude-plugins |

---

## Quick install commands (copy and run)

```
npx skills add anthropics/knowledge-work-plugins -g
npx skills add anthropics/claude-plugins-official -g
npx skills add anthropics/financial-services -g
npx skills add I-afaqrashid/claude-animation-studio -g
npx skills add iboss21/animatedwebs-claude -g
npx skills add shashwatgtm/b2b-sales-enablement -g
npx skills add bigdata-com/bigdata-plugins-marketplace -g
npx skills add keycustodian09-spec/crypto-spot-futures-analyzer -g
npx skills add cryptowisser-com/cryptowisser-news-plugin -g
npx skills add lsdimi/design-superpowers -g
npx skills add ultrathinker/icon-creator -g
npx skills add ahmedraza28/image-generation-skill -g
npx skills add riasistemas/claude-channel-instagram -g
npx skills add yordilorenzo/liquid-glass-skills -g
npx skills add aries-spring/motion-reel -g
npx skills add ivar-anon/roblox-dev -g
npx skills add kensho-technologies/spglobal-agent-skills -g
npx skills add bjgreenberg/senior-engineering-partner -g
npx skills add apack1001/stock-portfolio-valuation -g
npx skills add stockinsights-ai/plugins -g
npx skills add supabase-community/supabase-plugin -g
npx skills add wizzouk2/token-usage -g
npx skills add uxkin/agent -g
npx skills add lohbrandt/ui-ux-behaves -g
npx skills add carlsz/ux-agent-skills -g
npx skills add piotrlason/video-to-code-skill -g
npx skills add MarcinSufa/claude-watch-video -g
npx skills add israelmusondaayliffe/plugins -g
npx skills add msapps-mobile/claude-plugins -g
```

---

## Not matched

- `amd/skills`, `design-skills`, Finance Tutor, and the crypto-research marketplace: on-screen text was too blurry to read the owner or repo name.
- Entries marked "By you" in the video (Cartoon 3d short, Inkbeat shorts, Kaz map animation, seedance-2.5, Lightwhinh) are the uploader's own skills with no public source.

---

## ChatGPT Work Mode installation status

**Verified GitHub imports** — 21 standalone skills and 306 workflows in 3 installed collections.

Open **Plugins**, then **Skills**, to find the standalone skills and collections. Invoke a collection by name and specify the workflow you want. Collections include the upstream workflow instructions and source links. Some workflows require a connector, supporting script, or local runtime.

| Plugin or connection | Status |
|---|---|
| Figma | Connected previously with 17 bundled skills. |
| Zoom | Declined. |
| Supabase | The ChatGPT connector is connected and verified. It includes the Supabase and Supabase Postgres Best Practices skills. |
| PDF Viewer, Bright Data, Accoil Product Tracking, Postiz, SearchFit SEO, Modern Web Guidance | Exact ChatGPT plugin matches were unavailable in account search. |
| Claude plugins and local MCP servers | No Claude plugin or standalone MCP server was added. |

### Verified GitHub skill imports

| Source | Count | Skills available |
|---|---:|---|
| [ahmedraza28/image-generation-skill](https://github.com/ahmedraza28/image-generation-skill) | 1 | `image-generation` |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 4 | `frontend-design`, `mcp-server-dev-build-mcp-app`, `mcp-server-dev-build-mcp-server`, `mcp-server-dev-build-mcpb` |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | 5 | `competitive-analysis`, `comps-analysis`, `idea-generation`, `pptx-author`, `sector-overview` |
| [aries-spring/motion-reel](https://github.com/aries-spring/motion-reel) | 1 | `motion-reel` |
| [bigdata-com/bigdata-plugins-marketplace](https://github.com/bigdata-com/bigdata-plugins-marketplace) | 8 | `bigdata-capital-allocation`, `bigdata-catalysts`, `bigdata-company-brief`, `bigdata-comps`, `bigdata-country-analysis`, `bigdata-credit`, `bigdata-deal-analysis`, `bigdata-deep-dive` |
| [I-afaqrashid/claude-animation-studio](https://github.com/I-afaqrashid/claude-animation-studio) | 1 | `animation-studio` |
| [MarcinSufa/claude-watch-video](https://github.com/MarcinSufa/claude-watch-video) | 1 | `watch-video` |

### `github-business-skills` (177 workflows)

| Source | Count | Included workflows |
|---|---:|---|
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 177 | `accessibility-review`, `account-context`, `account-plan`, `account-research`, `account-tiering`, `ad-manager`, `analyze`, `ap-processor`, `architecture`, `audit-support`, `brand-review`, `brand-style`, `brand-voice-enforcement`, `brief`, `build-agent`, `build-connector`, `build-dashboard`, `business-pulse`, `call-list`, `call-prep`, `call-summary`, `campaign-plan`, `canva-creator`, `capacity-plan`, `cash-flow-snapshot`, `change-request`, `close-management`, `close-month`, `close-plan`, `code-review`, `comp-analysis`, `competitive-brief`, `competitive-brief`, `competitive-intelligence`, `compliance-check`, `compliance-tracking`, `content-creation`, `content-strategy`, `contract-review`, `create-an-asset`, `create-viz`, `crm-autopilot`, `crm-hygiene-check`, `customer-escalation`, `customer-health`, `customer-research`, `customer-voice`, `daily-briefing`, `data-context-extractor`, `data-visualization`, `deal-advance-gap`, `deal-review`, `deal-signals`, `deal-slip-scenario`, `debug`, `deploy-checklist`, `design-critique`, `design-handoff`, `design-system`, `digest`, `discover-brand`, `documentation`, `draft-content`, `draft-offer`, `draft-outreach`, `draft-response`, `email-sequence`, `end-of-day`, `expansion-whitespace`, `explore-data`, `financial-statements`, `forecast`, `grant-rfp-writer`, `grow-pipeline`, `growth-pulse`, `guideline-generation`, `handle-objection`, `hiring-screener`, `inbox-manager`, `inbox-sweep`, `incident-response`, `instrument-data-to-allotrope`, `interview-prep`, `inventory-planner`, `invoice-chase`, `job-post-builder`, `journal-entry`, `journal-entry-prep`, `kb-article`, `knowledge-synthesis`, `lead-finder`, `lead-triage`, `lead-triage`, `legal-response`, `legal-risk-assessment`, `log-activity`, `marketing-monday`, `meeting-briefing`, `metrics-review`, `monday-brief`, `month-end-prep`, `onboarding`, `org-planning`, `outreach-composer`, `pay-the-bills`, `payroll-prep`, `people-report`, `performance-report`, `performance-review`, `pipeline-review`, `plan-payroll`, `policy-lookup`, `process-doc`, `process-optimization`, `product-brainstorming`, `proposal-builder`, `reactivate`, `reconciliation`, `recruiting-pipeline`, `renewal-radar`, `rep-context`, `report-builder`, `report-pack`, `research-synthesis`, `restock`, `review-contract`, `review-reputation`, `risk-assessment`, `roadmap-update`, `route-lead`, `runbook`, `schedule-meeting`, `scientific-problem-selection`, `scvi-tools`, `search`, `search-strategy`, `seo-ai-visibility`, `seo-audit`, `setup`, `signature-request`, `single-cell-rna-qc`, `smb-onboard`, `smb-router`, `social-content-engine`, `source-management`, `sox-testing`, `speed-to-lead`, `sprint-planning`, `sql-queries`, `stakeholder-map`, `stakeholder-update`, `standup`, `start`, `statistical-analysis`, `status-report`, `synthesize-research`, `system-design`, `tax-prep`, `tax-season-organizer`, `team-pipeline`, `tech-debt`, `testing-strategy`, `ticket-deflector`, `ticket-triage`, `triage-nda`, `update-opportunity`, `user-research`, `ux-copy`, `validate-data`, `variance-analysis`, `vendor-check`, `vendor-review`, `view-pdf`, `weekly-wrap`, `win-loss-review`, `write-query`, `write-spec` |

### `github-design-and-media-skills` (59 workflows)

| Source | Count | Included workflows |
|---|---:|---|
| [carlsz/ux-agent-skills](https://github.com/carlsz/ux-agent-skills) | 5 | `audit-cuj`, `render-report`, `spec-cuj`, `usability-audit`, `ux-audit` |
| [cuellarfr/design-skills](https://github.com/cuellarfr/design-skills) | 10 | `accessibility-audit`, `design-critique`, `design-elevation`, `design-ops`, `design-systems`, `interaction-design`, `journey-mapping`, `ux-research`, `ux-strategy`, `ux-writing` |
| [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | 2 | `generate-project-plan`, `video-interaction-mapper` |
| [iboss21/animatedwebs-claude](https://github.com/iboss21/animatedwebs-claude) | 7 | `animatedwebs-backgrounds`, `animatedwebs-components`, `animatedwebs-design`, `animatedwebs-gradients`, `animatedwebs-hero`, `animatedwebs-site`, `animatedwebs-style` |
| [israelmusondaayliffe/plugins](https://github.com/israelmusondaayliffe/plugins) | 4 | `business-writing-intent-enforcer`, `claim-boundary-checker`, `writing-enforcer`, `writing-quality-router` |
| [lohbrandt/ui-ux-behaves](https://github.com/lohbrandt/ui-ux-behaves) | 9 | `ui-ux`, `ui-ux-active`, `ui-ux-chart`, `ui-ux-date`, `ui-ux-dialog`, `ui-ux-form`, `ui-ux-passive`, `ui-ux-table`, `ui-ux-tabs` |
| [lsdimi/design-superpowers](https://github.com/lsdimi/design-superpowers) | 9 | `creative`, `design`, `design-review`, `ds-consumer`, `ds-make`, `ds-manage`, `ds-producer`, `figma-setup`, `map-design` |
| [piotrlason/video-to-code-skill](https://github.com/piotrlason/video-to-code-skill) | 3 | `run-video-to-code-skill`, `setup-video-to-code-skill`, `show-help-video-to-code-skill` |
| [ultrathinker/icon-creator](https://github.com/ultrathinker/icon-creator) | 1 | `icon-creator` |
| [uxkin/agent](https://github.com/uxkin/agent) | 7 | `build-ui`, `design-md`, `ios-screens`, `no-ui-slop`, `ui-from-screenshot`, `ui-states`, `uxkin-research` |
| [yordilorenzo/liquid-glass-skills](https://github.com/yordilorenzo/liquid-glass-skills) | 2 | `apple-motion-feel`, `liquid-glass-motion` |

### `github-research-and-development-skills` (70 workflows)

| Source | Count | Included workflows |
|---|---:|---|
| [amd/skills](https://github.com/amd/skills) | 26 | `apu-memory-tuner`, `eaiapps-guided-install`, `flydsl-kernel-authoring`, `flydsl-kernel-trace-analysis`, `hyperloom-workload-optimizer`, `lemonade-router-builder`, `local-ai-app-integration`, `local-ai-use`, `magpie-kernel-evaluator`, `moat-cuda-to-rocm`, `quark-install`, `quark-torch-llm-ptq`, `rocm-doctor`, `rocprof-compute-kernel-bottleneck`, `rocprof-compute-memory`, `rocprof-compute-pc-sampling`, `rocprof-compute-roofline`, `rocprof-compute-speed-of-light`, `rocprof-compute-torch-trace`, `rocprofiler-pc-sampling`, `rocprofiler-systems-choosing-a-profiling-preset`, `rocprofiler-systems-discovering-profiling-options`, `rocprofiler-systems-instrumenting-binaries`, `serving-llms-on-epyc`, `serving-llms-on-instinct`, `tracelens-analysis-orchestrator` |
| [bigdata-com/bigdata-plugins-marketplace](https://github.com/bigdata-com/bigdata-plugins-marketplace) | 16 | `bigdata`, `bigdata-earnings-preview`, `bigdata-earnings-quality`, `bigdata-earnings-recap`, `bigdata-investment-thesis`, `bigdata-markets-today`, `bigdata-moat`, `bigdata-quick-take`, `bigdata-risk`, `bigdata-screen`, `bigdata-sector`, `bigdata-special-situations`, `bigdata-stock-move`, `bigdata-theme`, `bigdata-valuation`, `bigdata-watchlist` |
| [bjgreenberg/senior-engineering-partner](https://github.com/bjgreenberg/senior-engineering-partner) | 1 | `senior-engineering-partner` |
| [cryptowisser-com/cryptowisser-news-plugin](https://github.com/cryptowisser-com/cryptowisser-news-plugin) | 1 | `crypto-news` |
| [ivar-anon/roblox-dev](https://github.com/ivar-anon/roblox-dev) | 10 | `luau-strict-typing`, `new-system`, `review`, `roblox-architecture`, `roblox-datastores`, `roblox-performance`, `roblox-security`, `roblox-testing`, `roblox-ui`, `setup` |
| [kensho-technologies/spglobal-agent-skills](https://github.com/kensho-technologies/spglobal-agent-skills) | 3 | `earnings-preview-single`, `funding-digest`, `tear-sheet` |
| [keycustodian09-spec/crypto-research-market-insights](https://github.com/keycustodian09-spec/crypto-research-market-insights) | 1 | `crypto-research` |
| [keycustodian09-spec/crypto-spot-futures-analyzer](https://github.com/keycustodian09-spec/crypto-spot-futures-analyzer) | 1 | `crypto-spot-futures-analysis` |
| [mechamis/mechami-plugins](https://github.com/mechamis/mechami-plugins) | 1 | `finance-tutor` |
| [msapps-mobile/claude-plugins](https://github.com/msapps-mobile/claude-plugins) | 1 | `youtube-transcriber` |
| [shashwatgtm/b2b-sales-enablement](https://github.com/shashwatgtm/b2b-sales-enablement) | 3 | `competitive-intelligence`, `meeting-prep-debrief`, `sales-proposal-builder` |
| [stockinsights-ai/plugins](https://github.com/stockinsights-ai/plugins) | 2 | `get-started`, `stock-research` |
| [supabase-community/supabase-plugin](https://github.com/supabase-community/supabase-plugin) | 2 | `supabase`, `supabase-postgres-best-practices` |
| [wizzouk2/token-usage](https://github.com/wizzouk2/token-usage) | 1 | `report` |
| [yordilorenzo/liquid-glass-skills](https://github.com/yordilorenzo/liquid-glass-skills) | 1 | `liquid-glass` |

### Source corrections and pending items

- Also found [AMD Skills](https://github.com/amd/skills), [design-skills](https://github.com/cuellarfr/design-skills), [Finance Tutor](https://github.com/mechamis/mechami-plugins/tree/main/plugins/finance-tutor), and [Crypto & Bitcoin Analyst](https://github.com/keycustodian09-spec/crypto-research-market-insights).
- The listed stock-portfolio-valuation repository returned 404. The five personal skills require their original files.
- The Instagram channel skills depend on the Claude channel integration. Work Mode did not acquire an Instagram connection.
- ChatGPT’s safety check declined the original Business collection. The documentation-only version omits executable resources and the Nextflow development workflow.
- Names or display metadata were adjusted where needed for Work Mode. Skills with connector, local runtime, or external service dependencies may require setup when used.
