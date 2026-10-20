# Results and Evidence Ledger

**October 2026 project — independent personal fan video**

These distinctions prevent inflated or misleading resume statements.

| Measure | Fact / evidence | Interpretation |
| --- | --- | --- |
| Video completed | Owner explicitly confirmed successful V5 render | Owner-attested completion |
| User acceptance | Owner said video looks good and motion is smooth | Human qualitative QA, not a benchmark |
| Timeline duration | **157.368 s** from documented edit plan | Planned value; no independent final file `ffprobe` captured here |
| Resolution | **1920×1080** configured for final export | Production specification |
| FPS | **50** output configured | Does not establish 50 native captured source frames/sec |
| Segments | **22** planned/render scene positions | Design scope |
| Approved windows | **15** across three source videos | Source-selection scope |
| Compressed video size | **~140 MB** | Owner estimate |
| Distribution | Google Drive video preview and download reported working | Owner report |
| External outreach | Email/video link sent to Royal Caribbean | Not official endorsement or approval |
| External reaction | Unknown | Cannot claim |
| Rights/licensing | Original soundtrack arrangement, backing track and footage rights not established | Public demo uses synthetic media |
| Manual time, cost, money saved | Not systematically tracked | Cannot claim ROI or time-savings percentage |
| Commercial deployment | None | Future concept only |

## How to strengthen evidence

Run `ffprobe` on the downloaded **original** final MP4 (not the Drive stream):

```bash
ffprobe -v error -show_entries format=duration,size,bit_rate -show_entries stream=index,codec_name,width,height,r_frame_rate,avg_frame_rate -of json final_video.mp4
```

Record actual resulting data only after running it. This validates basic metadata, not subjective motion quality or legal permissions.

For a future commercial pilot also measure actual wall-clock duration, human intervention minutes, success rate, corrections per approved clip, total cost per accepted result and sales/lead effects.

**Rights and brand note:** Source availability and noncommercial fan intent do not by themselves grant the rights to republish music or footage. No private recordings or videos appear in this public repository.

[Case study](CASE_STUDY.md) · [Architecture](ARCHITECTURE.md)
