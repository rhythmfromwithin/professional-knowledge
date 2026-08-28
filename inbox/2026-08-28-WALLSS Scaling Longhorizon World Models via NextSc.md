---
title: "WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.26239
priority: medium
status: unread
interest: medium
next_step: skim
---
# WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression
> 原文: [https://arxiv.org/abs/2608.26239](https://arxiv.org/abs/2608.26239)

arXiv:2608.26239v1 Announce Type: new
Abstract: Generative world models provide robots with predictive models of how the world evolves under interaction, with growing potential for simulation, planning, policy evaluation, and robot learning. Beyond clip-level future prediction, a unified generative formulation should relate actions to consequences, support flexible horizons and continuous interaction, and enable reward-driven optimization. We introduce WALL-SS, a world model that generates visual futures through Scale-wise autoregressive Scaling, enabling action-controllable and long-horizon robotic simulation. WALL-SS represents embodied trajectories as causal sequences of temporally interleaved observations and actions, making action-dependent state transitions explicit while naturally supporting variable-length generation, streaming extension through reusable causal states, and direct optimization through sequence probabilities. To make this formulation effective over long horizons, we generate each future observation in a coarse-to-fine manner and develop three complementary components within the same hierarchy. Action-conditioned next-scale prediction injects scale-aligned action representations to improve action-future coupling and model both successful and failed behaviors. Scale-compressed long-horizon memory retains recent interactions at fine resolution while compressing distant observations and actions, with scale-wise dream forcing enhancing robustness to self-generated context. Finally, on-policy alignment optimizes autoregressive visual dynamics with action-following and long-term consistency rewards while preserving the pretrained visual distribution. Experiments show that WALL-SS improves action following and trajectory accuracy, supports coherent minute-long streaming rollout under bounded memory, and consistently benefits from on-policy alignment in reducing action drift and long-horizon inconsistency.
