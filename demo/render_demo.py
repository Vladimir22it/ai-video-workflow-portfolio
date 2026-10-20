#!/usr/bin/env python3
"""Render a silent video with FFmpeg from synthetic title cards (no third-party media)."""
import argparse
import json
import re
import subprocess
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default="data/sample_project.json")
    parser.add_argument("--out", default="output/demo.mp4")
    args = parser.parse_args()

    plan = json.loads(Path(args.project).read_text(encoding="utf-8"))
    width, height, fps = (int(plan[key]) for key in ("width", "height", "fps"))
    scenes = plan["scenes"]
    if not (1 <= len(scenes) <= 20 and 320 <= width <= 1920 and 240 <= height <= 1080 and 1 <= fps <= 60 and width % 2 == 0 and height % 2 == 0):
        raise ValueError("Invalid video settings")
    for scene in scenes:
        if not isinstance(scene["text"], str) or not re.fullmatch(r"[A-Za-z0-9 !?.-]{1,60}", scene["text"]):
            raise ValueError("Invalid title; use simple letters and punctuation")
        if not isinstance(scene["color"], str) or not re.fullmatch(r"0x[0-9a-fA-F]{6}", scene["color"]):
            raise ValueError("Invalid hex color")
        if not 0.5 <= float(scene["duration"]) <= 15:
            raise ValueError("Duration must be 0.5 to 15 seconds")
    outputs = Path(args.out)
    outputs.parent.mkdir(parents=True, exist_ok=True)
    # Use generated colors and text; no licensed input assets.
    filter_steps = []
    command = ["ffmpeg", "-y"]
    for scene in scenes:
        command.extend(["-f", "lavfi", "-t", str(float(scene["duration"])), "-i",
                        f"color=c={scene['color']}:s={width}x{height}:r={fps}"])
    for i, scene in enumerate(scenes):
        title = scene["text"].replace(":", "").replace("'", "")
        filter_steps.append(f"[{i}:v]drawtext=text='{title}':fontcolor=white:fontsize=40:x=(w-text_w)/2:y=(h-text_h)/2,format=yuv420p[v{i}]")
    labels = "".join(f"[v{i}]" for i in range(len(scenes)))
    filter_steps.append(f"{labels}concat=n={len(scenes)}:v=1:a=0[out]")
    command.extend(["-filter_complex", ";".join(filter_steps), "-map", "[out]",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", str(outputs)])
    subprocess.run(command, check=True)
    print("Created:", outputs)

if __name__ == "__main__":
    main()
