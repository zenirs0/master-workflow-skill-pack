# Roblox video production skills for Claude and ChatGPT

Researched 24 November 2026. This reference covers Roblox video production. Installation history is recorded in the [previous inventory](prior-inventory.md).

## Start with the deliverable

Ask for the Roblox place or repository, target audience, video format and duration, and the available footage and tools. Infer routine defaults when possible. For a short, use 1080 × 1920 and 30 fps as starting export settings. For a coding tutorial, use 1920 × 1080 and 30 fps. Match a 60 fps delivery when the capture and target warrant it.

| Goal | Production workflow | Deliverables |
|---|---|---|
| Roblox gameplay trailer | Studio playtest → OBS capture → edit in Kdenlive or Remotion → FFmpeg export check | Shot list, source clips, trailer master |
| Luau coding tutorial | Verify the code in Studio → record the editor and gameplay → build code callouts in Remotion → add captions | Tested snippet, script, edited MP4, SRT |
| Roblox cinematic short | Set keyframed or scripted cameras in Studio → capture the scene → generate optional reference-led B-roll → edit vertical | Shot plan, capture notes, generated-shot log, vertical master |
| Scripted devlog | Read the project changes → capture a before/after pair → build a Remotion timeline with narration and diffs | Video source, render, captions, change list |
| Improve an existing edit | Inspect clips with FFprobe → build a timestamped cut list → repair pacing, framing, audio, and captions → check the export | Edit decision list, MP4, SRT, QA notes |

## Skill instructions

### 1. Code the mechanic and prove it in Studio

1. Inspect the repository or place before changing it. Name the file and its Studio location, such as a LocalScript in StarterPlayerScripts. Match the project's Rojo mapping if it uses one.
2. Identify client-only visuals and UI separately from server-owned gameplay state. For a gameplay feature that depends on replication, use Studio’s client/server or multi-client testing controls and check the relevant Output logs.
3. Define the visual proof before recording. State the input, expected state change, and one failure case. For a coin mechanic, record pickup, score increment, and the coin becoming unavailable after collection. For a tutorial, show the final behavior briefly before the code walkthrough.
4. Keep the filmed snippet small. Show real line numbers or the actual diff. Use local formatting and analysis tools if configured. Record Studio test results explicitly. If Studio is unavailable, label the code **awaiting Studio verification**.

### 2. Capture a real Roblox cinematic

1. Make a shot list with duration, camera movement, action, capture method, and intended crop. Use a dedicated capture place or a saved place version for camera experiments.
2. Use the Animation Editor for avatar movement. For repeatable camera travel, use the local player's CurrentCamera with Scriptable camera mode, explicit CFrame or keyframes, and TweenService where interpolation fits. Keep Camera.Focus current during scripted movement. Restore player camera control after the shot and test the transition.
3. Record separate gameplay, editor, and cinematic clips. Capture a short test to check framing, dropped frames, and game versus narration audio. Hide irrelevant chat, usernames, credentials, and notifications from the recording area. Keep originals for future crops.
4. Leave room around the subject for a vertical cut. Capture the HUD deliberately when it proves a feature. Record a clean angle for titles and transitions.

### 3. Generate optional Roblox-style video shots

1. Start from a screenshot or reference you can use. Record the avatar’s silhouette, outfit colors, map landmarks, lighting, and framing. Ask for one movement and one camera direction per shot.
2. Use Veo, Runway, or a configured fal endpoint for atmosphere, transitions, illustrative scenes, or concept shots. Verify supported duration, aspect ratio, reference inputs, and usage cost for the selected model before a paid generation run. Keep important UI, text, real gameplay, and exact code in captured or rendered layers.
3. Save each returned file with its shot ID, provider, model, prompt, aspect ratio, and reference filename. Review every cut for avatar drift, changed geometry, unreadable typography, and abrupt motion. Identify generated inserts in the shot list and label them in the video when they could be mistaken for gameplay.

**Example image-to-video prompt**

> Use the attached screenshot of my original Roblox floating-island obby as the opening reference. Preserve the teal hoodie, square avatar silhouette, amber checkpoint ring, and the three islands in the same positions. Frame vertically with the avatar centered and the checkpoint in the upper middle. The camera slowly pushes forward as the avatar takes two steps toward the checkpoint. Keep movement steady and the scene free of added text, HUD, or extra characters. Use this as a short concept insert in a trailer.

### 4. Edit for the target format

1. Inspect source resolution, frame rate, duration, and audio streams with FFprobe. Transcribe speech with Whisper or whisper.cpp when needed, then correct Luau API spelling, identifiers, and timings by hand.
2. Build the first cut from a timestamped edit decision list. Use Remotion for reusable code panels, line highlights, step cards, animated overlays, and repeatable formats. Use Kdenlive for manual trims, reframing, audio mixing, and subtitle work. Use FFmpeg for exact trims, batch export, and media checks. Preserve source files and render to a separate output.
3. Let narration finish before each instructional cut. Keep on-screen code readable on a phone. Where a vertical crop would cut code or controls, make a stacked composition with cropped code above gameplay. Add captions with enough contrast and clear space from platform overlays.
4. Check the exported file on a phone and desktop. Verify dimensions, duration, caption sync, quiet and loud sections, and legibility of code. Deliver the MP4, SRT when relevant, and editing or render source when requested.

**Example 30-second Luau short**

| Time | Visual | Audio or caption |
|---|---|---|
| 0–3 s | Real footage of a coin pickup and score increment | “Make a coin add to your score in Roblox.” |
| 3–9 s | Show Studio hierarchy with the coin and server script highlighted | “Put the pickup logic on the server.” |
| 9–19 s | Show the actual Luau snippet with one highlighted change | Explain the touch handler and the one-pickup check. |
| 19–26 s | Replay the Studio test and show the second-touch result | State the result observed in Studio. |
| 26–30 s | Show the final mechanic and script location | End on the tested outcome. |

**Shot sheet fields** — ID, edit in/out, source file and timecode, capture or generation method, on-screen action, camera or crop, narration, caption, verification status.

### 5. Improve the skill from examples

Save three representative requests with their inputs, expected outputs, and verification results. Run them in Claude and ChatGPT/Codex under comparable tool access. Score each dimension from 0 to 2. Use 0 for missing or wrong, 1 for incomplete, and 2 for fully verified.

| Test case | Check |
|---|---|
| 30-second coin pickup short | Correct Luau context, real behavior shown, code readable on mobile, SRT aligned |
| 45-second trailer with generated B-roll | Gameplay and generated inserts identifiable, avatar continuity, coherent pacing, valid export |
| Two-minute coding devlog from a diff | Exact file paths and snippets, real playtest evidence, repeatable timeline, usable narration |

Score **Roblox accuracy**, **visual continuity**, **editing and captions**, **reproducibility**, and **honest tool reporting**. Require evidence for Studio, generation, and render claims. Compare results, add a short rule for repeated failures, and rerun the same examples. Skill instructions and examples guide the assistant’s workflow without changing model weights.

## Verified skills, plugins, and tools

| Name | Type and use | Requirements and status |
|---|---|---|
| [Roblox Studio agent plugin](https://github.com/Roblox/roblox-studio-agent-plugin) | Official Roblox plugin for live Studio inspection, Luau editing, screenshot capture, and playtesting | Roblox Studio on Windows or macOS. Upstream supports Claude Code/Cowork and ChatGPT desktop/Codex. ChatGPT account search did not surface it in this session. |
| [Roblox development skill](https://github.com/MSayib/roblox-dev-skill) | Community Agent Skill with Luau architecture, UI, testing, and Studio workflows | Its Markdown is portable. Studio operations require the live Studio connection. |
| [Roblox Dev](https://github.com/ivar-anon/roblox-dev) | Community Claude Code plugin with strict typing, architecture, UI, performance, and testing references | Port individual Markdown instructions to ChatGPT where needed. Claude plugin commands are client-specific. Also listed in Appendix A. |
| [Roblox Luau](https://create.roblox.com/docs/luau) and [Rojo v7](https://rojo.space/docs/v7/) | Language docs and file-based project sync | Use the current project map. Rojo is optional for Studio-only projects. |
| [Roblox camera](https://create.roblox.com/docs/workspace/camera), [Animation Editor](https://create.roblox.com/docs/tutorials/curriculums/animator/work-with-the-animation-editor), and [Studio testing modes](https://create.roblox.com/docs/studio/testing-modes) | Official references for cinematics and gameplay validation | Studio required for execution. |
| [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) | Upstream Agent Skills for React-based video, code overlays, timed titles, and renders | Node.js and a Remotion project for rendering. The upstream catalog documents Claude Code and Codex support. |
| [fal.ai Agent Skills](https://github.com/fal-ai-community/skills) | Includes cinematography, storytelling, prompting, and storyboard-to-short-film | Read the source’s runtime instructions. Endpoint execution requires a configured account. ChatGPT lists the fal app as available for installation. |
| [Google Veo](https://ai.google.dev/gemini-api/docs/video) and [Runway](https://dev.runwayml.com/endpoints/image_to_video) | Image-to-video providers for inserts and concept visuals | Generation needs provider access. ChatGPT lists Runway as available for installation. |
| [OBS Studio](https://obsproject.com/kb/quick-start-guide) | Local screen and game capture for Studio and editor footage | Desktop recording application. Test sources, audio tracks, and resolution before filming. |
| [FFmpeg and FFprobe](https://www.ffmpeg.org/documentation.html), [Kdenlive](https://docs.kdenlive.org/en/effects_and_filters/subtitles.html), and [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Media inspection and export, timeline and subtitle editing, local transcription | Install your selected desktop or command-line tools to execute those steps. |
| [Video Editing Skill](https://github.com/social-media-skills/video-editing-skill) | Community agent skill for FFmpeg editing | Review the source and run it only where FFmpeg and the source footage are accessible. |
| [Watch Video](https://github.com/MarcinSufa/claude-watch-video) | Existing skill for timestamped frames and transcripts from a recording | Already in the imported inventory. Actual processing depends on its local tools and source access. |
| Figma and Supabase | Figma for storyboards and diagram assets. Supabase for permitted project data when a video needs it. | Both are verified connected in the prior inventory. |
| Adobe and Descript | Optional editing integrations to evaluate against your exact clip export needs | ChatGPT lists both as available for installation. |

Use the source links above for current setup, feature limits, and licensing. The tool permissions and execution environment determine which steps an assistant can perform.

## Use the same Markdown in Claude and ChatGPT

- **Claude Code** — Use the repository entry point when installing Master Workflow. For a Roblox-only skill, place the original Roblox skill file at `.claude/skills/roblox-video-production/SKILL.md` in your project. Call the skill by name. [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- **Claude web or desktop** — Package the skill folder as a ZIP and upload it through Claude’s custom skills controls when available. [Claude custom skills guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- **ChatGPT Work** — In **Plugins → Skills**, use **Create → Upload from your computer** if your account exposes skill upload. You can also attach this Markdown to a project or chat and ask ChatGPT to follow the first section through the usage examples. [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- **Codex** — Put the skill in your project’s `.agents/skills/roblox-video-production/SKILL.md` directory. A local Windows or macOS Studio session is needed for the Roblox MCP workflow. [Codex skill documentation](https://developers.openai.com/codex/skills) · [Studio MCP documentation](https://create.roblox.com/docs/studio/mcp)
- **Android or web** — Use the skill for planning, code drafting, prompts, caption review, and uploaded-file analysis when supported. Capture or playtest in a desktop Studio session, then provide the footage and logs. [Roblox plugin compatibility](https://github.com/Roblox/roblox-studio-agent-plugin#works-with)

For the desktop Studio connection, follow Roblox’s instructions for your client. Enable the Studio MCP server inside Studio and verify by asking the assistant to list open Studio windows. Check the place name before allowing edits or running a playtest.

**Starter request**

> Use Roblox Video Production to make a 30-second vertical short for my Roblox obby. Start with gameplay footage, show the tested Luau checkpoint behavior, and use Remotion or an edit decision list for code overlays and captions. Mark generated inserts separately. Record what you verified and label any Studio or render steps that still need execution.
