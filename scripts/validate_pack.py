"""Check the portable skill, local references, and sample editing data."""

import csv
from decimal import Decimal
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CAPTION = re.compile(r"(?P<start>\d{2}:\d{2}:\d{2},\d{3}) --> (?P<end>\d{2}:\d{2}:\d{2},\d{3})")
LINK = re.compile(r"!?(?:\[[^\]\n]+\])\(([^()\s]+)\)")
REQUIRED = (
    "SKILL.md", "README.md", ".gitignore", ".gitattributes", "agents/openai.yaml",
    ".github/workflows/validate.yml", "references/standalone-master.md",
    "references/prior-inventory.md", "assets/sample-video.mp4",
    "assets/sample-cover.png", "assets/sample-captions.srt", "examples/sample-edit.csv",
    "templates/shot-list.csv", "templates/edit-decision-list.csv",
)


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_entry_point():
    for path in (ROOT / "SKILL.md", ROOT / "references/standalone-master.md"):
        source = path.read_text(encoding="utf-8")
        metadata = re.match(r"\A---\nname: (master-workflow)\ndescription: (.{1,1024})\n---\n", source)
        require(metadata, f"Unexpected Agent Skills frontmatter in {path.relative_to(ROOT)}.")


def check_links():
    count = 0
    for path in ROOT.rglob("*.md"):
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            require(resolved.is_relative_to(ROOT) and resolved.exists(),
                    f"Broken local link in {path.relative_to(ROOT)}: {target}")
            count += 1
    return count


def seconds(timestamp):
    hours, minutes, tail = timestamp.split(":")
    return Decimal(hours) * 3600 + Decimal(minutes) * 60 + Decimal(tail.replace(",", "."))


def load_captions():
    captions = (ROOT / "assets/sample-captions.srt").read_text(encoding="utf-8").strip()
    blocks = re.split(r"\n\s*\n", captions)
    cues = []
    for i, block in enumerate(blocks, 1):
        lines = block.splitlines()
        require(len(lines) == 3 and lines[0] == str(i), f"Bad format for SRT cue {i}.")
        match = CAPTION.fullmatch(lines[1])
        require(match, f"Bad timestamps for SRT cue {i}.")
        cues.append((seconds(match["start"]), seconds(match["end"]), lines[2]))
    return cues


def check_edit_data():
    sample = ROOT / "examples/sample-edit.csv"
    with sample.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    with (ROOT / "templates/edit-decision-list.csv").open(newline="", encoding="utf-8") as f:
        template_columns = next(csv.reader(f))
    require(rows and list(rows[0]) == template_columns, "Example edit fields differ from the template.")
    expected = load_captions()
    require(len(expected) == len(rows), "Sample edit and SRT cue counts differ.")
    cursor = Decimal(0)
    for row, cue in zip(rows, expected):
        clip = (sample.parent / row["source_file"]).resolve()
        require(clip == ROOT / "assets/sample-video.mp4", "Example edit must point to the bundled clip.")
        clip_in, clip_out = Decimal(row["source_in_s"]), Decimal(row["source_out_s"])
        start, end = Decimal(row["timeline_in_s"]), Decimal(row["timeline_out_s"])
        require(0 <= clip_in < clip_out <= 6 and start == cursor and end - start == clip_out - clip_in,
                f"Invalid timeline for {row['clip_id']}.")
        require((start, end, row["caption"]) == cue, f"SRT and timeline disagree for {row['clip_id']}.")
        cursor = end
    require(cursor == 6, "Sample edit must span the full six seconds.")
    return len(rows)


def main():
    for relative in REQUIRED:
        path = ROOT / relative
        require(path.is_file() and path.stat().st_size > 0, f"Missing or empty file: {relative}")
    check_entry_point()
    links = check_links()
    cues = check_edit_data()
    print(f"Validated both skill entry points, {links} local links, and {cues} matching edit and caption cues.")


if __name__ == "__main__":
    main()
