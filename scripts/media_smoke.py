"""Generate or verify the six-second editing fixture."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory


ASSETS = Path(__file__).resolve().parents[1] / "assets"
VIDEO = ASSETS / "sample-video.mp4"
COVER = ASSETS / "sample-cover.png"


def run(executable, *args):
    program = shutil.which(executable)
    if program is None:
        raise SystemExit(f"{executable} is required for this media command.")
    return subprocess.run([program, *args], text=True, check=True, capture_output=True).stdout


def generate():
    with TemporaryDirectory(dir=ASSETS) as tmp:
        video = Path(tmp) / VIDEO.name
        cover = Path(tmp) / COVER.name
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error",
            "-f", "lavfi", "-i", "testsrc2=size=640x360:rate=30:duration=6",
            "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000:duration=6",
            "-vf", "drawbox=x=0:y=328:w=640:h=32:color=blue:t=fill:enable='between(t,2,4)'",
            "-af", "volume=0.18",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
            "-movflags", "+faststart", str(video),
        )
        run("ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
            "-frames:v", "1", "-threads", "1", "-update", "1", str(cover))
        video.replace(VIDEO)
        cover.replace(COVER)


def probe(path):
    return json.loads(run("ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)))


def verify():
    data = probe(VIDEO)
    video = next((stream for stream in data["streams"] if stream["codec_type"] == "video"), {})
    audio = next((stream for stream in data["streams"] if stream["codec_type"] == "audio"), {})
    cover = probe(COVER)["streams"][0]
    duration = float(data["format"]["duration"])
    if (video.get("width"), video.get("height"), video.get("r_frame_rate")) != (640, 360, "30/1"):
        raise SystemExit("Unexpected video dimensions or frame rate.")
    if video.get("codec_name") != "h264" or audio.get("codec_name") != "aac" or abs(duration - 6) > 0.05:
        raise SystemExit("Unexpected media codecs or duration.")
    if (cover.get("codec_name"), cover.get("width"), cover.get("height")) != ("png", 640, 360):
        raise SystemExit("Unexpected cover image format or size.")
    run("ffmpeg", "-v", "error", "-xerror", "-i", str(VIDEO), "-f", "null", "-")
    print("Verified and decoded 6-second 640x360, 30 fps H.264/AAC fixture and PNG cover.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate", action="store_true", help="Rebuild the example MP4 and PNG before checking.")
    if parser.parse_args().regenerate:
        generate()
    verify()
