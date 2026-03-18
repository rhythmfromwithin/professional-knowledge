---
title: "Safety-Guided Flow (SGF): A Unified Framework for Negative Guidance in Safe Generation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.13300
priority: medium
status: unread
interest: medium
next_step: skim
---
# Safety-Guided Flow (SGF): A Unified Framework for Negative Guidance in Safe Generation
> 原文: [https://arxiv.org/abs/2603.13300](https://arxiv.org/abs/2603.13300)

arXiv:2603.13300v1 Announce Type: new
Abstract: Safety mechanisms for diffusion and flow models have recently been developed along two distinct paths. In robot planning, control barrier functions are employed to guide generative trajectories away from obstacles at every denoising step by explicitly imposing geometric constraints. In parallel, recent data-driven, negative guidance approaches have been shown to suppress harmful content and promote diversity in generated samples. However, they rely on heuristics without clearly stating when safety guidance is actually necessary. In this paper, we first introduce a unified probabilistic framework using a Maximum Mean Discrepancy (MMD) potential for image generation tasks that recasts both Shielded Diffusion and Safe Denoiser as instances of our energy-based negative guidance against unsafe data samples. Furthermore, we leverage control-barrier functions analysis to justify the existence of a critical time window in which negative guidance must be strong; outside of this window, the guidance should decay to zero to ensure safe and high-quality generation. We evaluate our unified framework on several realistic safe generation scenarios, confirming that negative guidance should be applied in the early stages of the denoising process for successful safe generation.
