---
title: "Reasoning-Guided Grounding: Elevating Video Anomaly Detection through Multimodal Large Language Models"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.02912
priority: medium
status: unread
interest: medium
next_step: skim
---
# Reasoning-Guided Grounding: Elevating Video Anomaly Detection through Multimodal Large Language Models
> 原文: [https://arxiv.org/abs/2605.02912](https://arxiv.org/abs/2605.02912)

arXiv:2605.02912v1 Announce Type: new
Abstract: Video Anomaly Detection (VAD) has traditionally been framed as binary classification or outlier detection, providing neither interpretable reasoning nor precise spatial localization of anomalous events. While Vision-Language Models (VLMs) offer rich scene understanding, they struggle with reliable spatial grounding - often producing hallucinated or geometrically invalid bounding boxes when asked to localize objects. We propose VANGUARD (Video Anomaly Understanding through Reasoning and Grounding), a framework that unifies anomaly classification, spatial grounding, and chain-of-thought reasoning within a single VLM. VANGUARD introduces a three-stage curriculum that progressively layers training objectives: (1) classifier warmup on frozen backbone features, (2) LoRA-adapted spatial grounding, and (3) chain-of-thought generation. To overcome the sparse annotation typical of VAD benchmarks, we employ a teacher-student annotation pipeline in which a VLM (Qwen3-VL-4B) generates structured per-subclip reasoning trajectories based on manual annotations available from the UCA Dataset. Further, GroundingDINO provides bounding box supervision. On UCF-Crime, VANGUARD achieves 94% ROC-AUC with 84% F1 while simultaneously producing interpretable chain-of-thought explanations and spatial grounding of anomalous objects - capabilities absent from prior VAD methods. Ablations confirm that staged training outperforms monolithic optimization, and that structured reasoning acts as an implicit regularizer yielding more balanced predictions than classification-only fine-tuning. Zero-shot transfer to XD-Violence and ShanghaiTech demonstrates cross-domain generalization without target-domain adaptation.
