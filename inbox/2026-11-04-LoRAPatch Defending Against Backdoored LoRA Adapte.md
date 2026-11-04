---
title: "LoRA-Patch: Defending Against Backdoored LoRA Adapters via Directional Steering"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2611.03752
priority: low
status: unread
interest: medium
next_step: skim
---
# LoRA-Patch: Defending Against Backdoored LoRA Adapters via Directional Steering
> 原文: [https://arxiv.org/abs/2611.03752](https://arxiv.org/abs/2611.03752)

arXiv:2611.03752v1 Announce Type: new
Abstract: Third-party LoRA adapters introduce serious backdoor risks: malicious adapters can maintain normal task performance while embedding hidden, trigger-activated behaviors, making them difficult to detect through standard utility evaluations. Existing removal-based defenses typically sanitize backdoored models by updating, pruning, distilling, or mixing model parameters. However, these approaches are misaligned with adapter-based deployment, where the trusted base model is expected to remain frozen. In this work, we propose LoRA-Patch, a lightweight backdoor defense tailored to LoRA adapters. Our key insight is that backdoor injection distorts the directional geometry of a poisoned adapter relative to its trusted base model. Building on this insight, LoRA-Patch suppresses trigger-activated behaviors by realigning adapter directions through layer-wise steering, without modifying the base model weights. Extensive experiments across five backdoor attacks and three models show that LoRA-Patch effectively mitigates trigger-activated backdoors, outperforming existing baselines while preserving benign task performance. Moreover, LoRA-Patch is computationally efficient, constructing patches within 20 seconds across all evaluated models and adapters. Our code is publicly available at https://github.com/FOXVEDA/LoRA-Patch.
