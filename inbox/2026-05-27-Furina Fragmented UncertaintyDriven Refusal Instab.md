---
title: "Furina: Fragmented Uncertainty-Driven Refusal Instability Attack"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.26158
priority: low
status: unread
interest: medium
next_step: skim
---
# Furina: Fragmented Uncertainty-Driven Refusal Instability Attack
> 原文: [https://arxiv.org/abs/2605.26158](https://arxiv.org/abs/2605.26158)

arXiv:2605.26158v1 Announce Type: new
Abstract: Safety alignment in large language models (LLMs) and multimodal large language models (MLLMs) is commonly assumed to operate as a near-binary threshold mechanism. We challenge this assumption by revealing that safety behavior is governed by an instability region where small perturbations induce stochastic refusal decisions rather than deterministic outcomes. We develop a multi-metric diagnostic framework combining external and internal signals to characterize this instability. Through systematic experiments, we identify a characteristic diagnostic signature: inputs in unstable regimes exhibit elevated output uncertainty yet decreased internal safety activation, a decoupling phenomenon that explains why detection-based defenses fail against sophisticated attacks. Building on this framework, we introduce Furina, a jailbreak attack that deliberately induces this signature through fragmented, scene-anchored prompts without model-specific optimization. Furina outperforms strong single-turn and multi-turn baselines on HarmBench and achieves competitive results on MM-SafetyBench, demonstrating that uncertainty amplification provides a principled and transferable mechanism for understanding safety vulnerabilities. Code is available at: https://github.com/0xCavaliers/Furina\_Jailbreak.
