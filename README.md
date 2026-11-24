# Master Workflow Skill Pack

A portable Agent Skills repository for software engineering, websites, design, video, Roblox, and business work. Start with [SKILL.md](SKILL.md), then open the relevant playbook.

## Use this pack

1. Extract the ZIP. Keep the folder structure intact so the skill can open its references and assets.
2. Use the [setup guide](references/setup.md) for your assistant. If uploading only one file to a chat, attach the [self-contained Markdown edition](references/standalone-master.md).
3. Try: “Use Master Workflow to plan a 30-second Roblox coding short. Include the proof shot, edit timeline, and verification checklist.”

## Repository contents

| Path | Contents |
|---|---|
| [SKILL.md](SKILL.md) | Entry point and task router |
| [references](references) | Domain playbooks, setup, dependency matrix, original inventory, and standalone edition |
| [templates](templates) | Coding, design, video, shot list, edit list, and release checklists |
| [examples](examples) | Worked Roblox tutorial and website handoff examples |
| [assets](assets/README.md) | Original test video, captions, and cover frame |
| [scripts](scripts) | Python validators, media inspection, and fixture regeneration |
| [agents](agents/openai.yaml) | Optional OpenAI skill display metadata |
| [.github/workflows](.github/workflows) | GitHub Actions validation for future use |

## Validate or start version control

Run the following from this directory. Use `py -3` in place of `python` on Windows if needed.

```sh
python scripts/validate_pack.py
python scripts/media_smoke.py
git init
git add .
git commit -m "Add master workflow skill pack"
```

Validation uses Python 3.10 or newer. Media inspection and regeneration use FFmpeg and FFprobe. The sample video is synthetic practice media and the source footage for the Roblox tutorial remains a project input. Git, a provider account, or a paid API is required only for workflows that call for it.

The ZIP is a Git-ready source snapshot. It includes Git configuration and CI files, with no Git history or remote configured. The [dependency matrix](references/dependencies.md) explains what ships with the pack and what each external workflow requires.
