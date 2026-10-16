---
title: "BD-HazardVLM: Probing Vision-Language Models for Latent Defensive-Driving Hazards in Bangladesh Road Scenes"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.20627
priority: medium
status: unread
interest: medium
next_step: skim
---
# BD-HazardVLM: Probing Vision-Language Models for Latent Defensive-Driving Hazards in Bangladesh Road Scenes
> 原文: [https://arxiv.org/abs/2610.20627](https://arxiv.org/abs/2610.20627)

arXiv:2610.20627v1 Announce Type: new
Abstract: Vision-language models are increasingly used for driving-scene understanding, yet their defensive reasoning under weakly structured Global South traffic remains unclear. We introduce BD-HazardVLM, a diagnostic benchmark of 500 Bangladesh road-scene images, comprising 375 from RSUD20K and 125 from TFP-BD, annotated for hazard presence, primary hazard category, risk timing, severity, defensive actions, visible evidence, and hallucination- and Western-road-bias traps. We evaluate Qwen2.5-VL-7B, InternVL3-8B, and MiniCPM-V-4.6 using a shared zero-shot task definition and structured output schema. Binary hazard-presence accuracy ranges from 88.0 percent to 89.2 percent, essentially matching the 89.0 percent majority-class baseline. Fine-grained reasoning is substantially weaker: category accuracy remains below 40 percent, risk-timing accuracy ranges from 1.6 percent to 12.4 percent, and exact defensive-action matching remains below 2 percent. Although InternVL3-8B achieves the highest severity accuracy at 61.2 percent, it has zero recall on the 58 high-severity cases. Qwen exhibits severe category mode collapse, while all models show weak latent-hazard anticipation and near-zero self-reported trap recognition. For the evaluated models, these findings show that coarse hazard recognition does not imply reliable fine-grained defensive-driving reasoning and motivate geographically diverse safety evaluation.
