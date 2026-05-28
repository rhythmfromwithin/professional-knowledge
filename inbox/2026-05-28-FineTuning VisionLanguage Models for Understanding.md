---
title: "Fine-Tuning Vision-Language Models for Understanding Current Damage and Scoring Priority with Quality Guard Agent"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.27452
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fine-Tuning Vision-Language Models for Understanding Current Damage and Scoring Priority with Quality Guard Agent
> 原文: [https://arxiv.org/abs/2605.27452](https://arxiv.org/abs/2605.27452)

arXiv:2605.27452v1 Announce Type: new
Abstract: Bridge inspection in Japan requires mandatory visual assessments every five years, yet qualitative damage ratings (levels a-e) assigned by different engineers exhibit significant inter-rater variability -- a critical barrier to consistent infrastructure management. The aging of skilled engineers further threatens inspection capacity. This paper presents a methodology for automating bridge damage understanding and repair priority scoring using fine-tuned Vision-Language Models (VLMs).
We fine-tune LLaVA-1.5-7B with QLoRA on up to 4,000 paired bridge damage images and inspection text records, then evaluate on a fixed test set of 800 images. The model outputs natural language descriptions identifying structural members and damage patterns, from which a rule-based scoring engine calculates a five-level repair priority index. A progressive training study (1k/2k/3k/4k samples) reveals that 2k training samples achieve near-optimal validation loss in only 2.9 hours of training; beyond 2k, validation loss improves by no more than 0.2% per doubling of training samples, exhibiting clear diminishing returns. Furthermore, semantic similarity on the held-out test set peaks at 3k (0.6909) and degrades at 4k (0.6739), indicating that quality-curated mid-scale data outperforms larger but noisier corpora. Inference optimization combining torch.compile() and batch processing (batch\_size=8) achieves 10.06 seconds per image -- a 70.2% reduction over the unoptimized baseline.
Our approach contributes to data governance in bridge inspection, reduces inter-rater variability, and provides AI-assisted triage to augment expert engineers in inspection workflows. Furthermore, we introduce a two-stage Quality Guard using a fine-tuned Swallow-8B SLM to reject low-quality VLM outputs before priority scoring, preventing spurious scores from damaged or unrecognised images.
