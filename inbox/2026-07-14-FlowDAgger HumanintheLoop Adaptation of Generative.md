---
interest: medium
link: https://arxiv.org/abs/2607.08877
next_step: skim
priority: medium
slack_ts: '1784085263.120479'
source: cs.RO - Robotics
status: unread
title: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent
  Space'
---
# FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space
> 原文: [https://arxiv.org/abs/2607.08877](https://arxiv.org/abs/2607.08877)

arXiv:2607.08877v1 Announce Type: new
Abstract: Pretrained generative robot policies based on flow matching and diffusion have achieved impressive results across a wide range of manipulation tasks. Yet real-world deployments routinely expose failure modes outside the pretraining distribution. Closing these gaps typically requires large-scale data collection or online reinforcement learning on physical hardware, which is impractical for rapid and safe adaptation. We present FlowDAgger, a sample- and compute-efficient method for adapting frozen generative robot policies from human interventions in latent space. Our key idea is action inversion: each human expert action is mapped to the noise that would have produced it under the frozen base policy, using reverse-time integration followed by local refinement. The resulting inverted noise provides supervision for a lightweight latent policy that steers the base model at deployment time, enabling rapid skill acquisition while preserving its behavioral priors. We evaluate FlowDAgger in simulation and on real-world bimanual and single-arm manipulation, adapting both action-head VLAs and world-action models from a handful of interventions. FlowDAgger outperforms supervised fine-tuning and latent-space RL baselines and preserves pretrained skills on held-out tasks, offering a practical path for adapting robot foundation models in the real world. Website: https://microsoft.github.io/FlowDAgger
