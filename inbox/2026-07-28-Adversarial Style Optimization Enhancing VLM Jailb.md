---
interest: medium
link: https://arxiv.org/abs/2607.21619
next_step: skim
priority: high
slack_ts: '1785208711.430879'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic
  Triggers Optimization'
---
# Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization
> 原文: [https://arxiv.org/abs/2607.21619](https://arxiv.org/abs/2607.21619)

arXiv:2607.21619v1 Announce Type: new
Abstract: Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-content-based vulnerabilities. Unlike previous research, we empirically find that MLLMs exhibit a Stylistic Inconsistency between their comprehension ability and safety ability: MLLMs can robustly understand content regardless of visual style, yet their defense mechanisms can be easily bypassed by specific stylistic triggers. Based on this finding, we propose Adversarial Style Optimization (ASO), a plug-and-play enhancement module to amplify existing visual jailbreaks. ASO fine-tunes an image-editing model to superimpose an optimized stylistic modification onto a given adversarial image, using a Group Relative Policy Optimization (GRPO) agent guided by a Structurally-Tiered Reward Function that combines a logit-based signal for detecting explicit refusals with a high-fidelity semantic evaluation from a powerful judge model. Extensive experiments show that ASO significantly enhances the ASR of SOTA attacks, demonstrating that stylistic biases are a scalable vector for red-teaming MLLMs. Our code is available at https://github.com/bingjunluo/ASO.
