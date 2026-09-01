---
interest: medium
link: https://arxiv.org/abs/2608.27462
next_step: skim
priority: high
slack_ts: '1788237859.406139'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Sledgehammer or Scalpel? A Fine-grained Adaptive Framework for Implicit Hate
  Speech
---
# Sledgehammer or Scalpel? A Fine-grained Adaptive Framework for Implicit Hate Speech
> 原文: [https://arxiv.org/abs/2608.27462](https://arxiv.org/abs/2608.27462)

arXiv:2608.27462v1 Announce Type: new
Abstract: Unlike explicit attacks with obvious profanity, implicit hate speech hides malice within seemingly compliant expressions through metaphors and contextual hints, making its detection in online content review challenging. While existing PLM- or LLM-based methods perform well, they typically apply a single reasoning process to all samples. This overlooks fine-grained linguistic nuances and causes unnecessary computation for simpler cases. We observe that online hate speech is not monolithic but manifests in varied forms. We therefore define three fine-grained categories: Shallow, Targeted, and Context-Dependent. Accordingly, we propose Fine-grained Adaptive Implicit Hate speech Detection (FAID), a novel framework that first performs fine-grained classification and then adapts to specific categories. Specifically, for Shallow samples with surface-identifiable intents, the framework adopts lightweight prompt-tuning for rapid classification; for Targeted comments that bind malicious intent to concealed targets, we design knowledge augmentation to iteratively refine the model and reveal hidden targets; for Context-Dependent comments lacking background information, we utilize an agentic framework that automatically generates prompts to evolve context, infer missing background information and identify ambiguous malicious intents. This adaptive architecture focuses computational resources on complex implicit samples while avoiding redundant reasoning for shallow samples. Experiments on four benchmark datasets demonstrate that FAID significantly outperforms SOTA baselines.
