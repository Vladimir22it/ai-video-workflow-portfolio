# Product Opportunity: Business Video Workflow Automation

**Status:** Idea and validation roadmap. There is currently **no launched app, commercial SaaS, paying customer, verified market demand, or proven ROI**.

## Transferable capability

The personal music-video project demonstrated an organized workflow: accept requirements and source constraints, plan the sequence with AI assistance, run deterministic FFmpeg jobs, use restartable checkpoints, review output with a human, and deliver the file.

The reusable value is **workflow design and orchestration** — not ownership of music or Royal Caribbean footage.

## Working proposal: VideoFlow AI

A narrow automation service for small businesses that need recurring short videos from *their own* photos, clips and approved business data.

Potential clients: window-treatment installers, local training schools, and retail store networks.

### MVP V0.1 — capabilities

1. Upload client-owned or correctly licensed photos/videos and brand assets with usage information.
2. Enter the business goal, product/service facts, desired format (9:16 or 16:9) and allowed claims.
3. Let an LLM propose a storyboard and copy; **require human approval**.
4. Render a 15–60-second video with template-based Python/FFmpeg.
5. Provide MP4 download and basic QA/processing logs.
6. Track runtime, revision count, manual effort, compute cost and user acceptance.

Suggested tools: Streamlit + Python + FFmpeg + JSON/Google Sheets + optional approved LLM API. CPU processing is sufficient for a simple template-first prototype. **This stack is proposed, not implemented here.**

### Roadmap

- Days 1–5: rights-clean local MVP and three sample videos; test operating assumptions.
- Week 2: supervised pilot with one business and owner-approved media.
- Week 3: interviews with at least five potential buyers, plus measurement of real costs and rework.
- Week 4: offer a limited paid pilot if there is interest and all permissions are in place.
- Only after repeatable demand: consider a hosted subscription or integrations with CRM, catalogs and n8n.

### Monetization hypotheses

Done-for-you video batches, client-specific workflow installation, ongoing maintenance and eventually SaaS. Prices and revenue projections require actual customer validation.

### Key risks

Crowded video-editing market, uncertain demand, weak input assets, copyrights, personal image consent, hallucinated prices and product claims, render cost, reliability, and customer support. The differentiator should be **integration with a specific business process**, not merely claiming “AI creates videos.”

[Main overview](../README.md) · [Case study](CASE_STUDY.md)
