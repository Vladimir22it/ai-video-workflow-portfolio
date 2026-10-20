# Synthetic Video Rendering Demo

This is **new, rights-clean sample code** to illustrate FFmpeg orchestration. It is not the private *Legend of the Seas* notebook and does not reproduce that video.

## Requirements

- Python 3.10+ (standard library only).
- `ffmpeg` and `ffprobe` installed on your system and on `PATH`.
- FFmpeg build includes `libx264` and the `drawtext` video filter.

## Run

From the repository root:

```bash
python demo/render_demo.py --project data/sample_project.json --out output/demo.mp4
```

The project manifest contains three synthetic title cards with invented text. Change their text, colors and durations in `data/sample_project.json`. All generated media is created locally; no external images, music, company logo, credentials or cloud service are required.

Expected output: **1280×720**, **30 FPS**, about **6 seconds**, silent H.264 MP4.

Inspect results with:

```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,avg_frame_rate -of json output/demo.mp4
```

The script prints a short metadata report after rendering. Media created by this mini-demo is unrelated to the Beatles song and official Royal Caribbean footage. For commercial use of FFmpeg components or codecs, verify their applicable licenses separately.
