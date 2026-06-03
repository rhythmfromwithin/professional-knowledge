---
title: "AURA: Action-Gated Memory for Robot Policies at Constant VRAM"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2606.02775
priority: high
status: unread
interest: medium
next_step: skim
---
# AURA: Action-Gated Memory for Robot Policies at Constant VRAM
> 原文: [https://arxiv.org/abs/2606.02775](https://arxiv.org/abs/2606.02775)

arXiv:2606.02775v1 Announce Type: new
Abstract: The KV-cache is the right memory for datacenters but the wrong memory for robots. Datacenter inference batches many short requests and resets them, amortizing an attention cache across a crowd. Embodied agents instead run one long, non-resetting episode on bandwidth-limited edge hardware, where high-bandwidth memory and flash are scarce, flash has finite write endurance, and memory writes rather than compute can become the binding constraint.
AURA-Mem (Action-Utility Recurrent Adaptive Memory) targets this regime. It wraps a frozen vision-language-action backbone with a constant-size recurrent memory and a learned gate that writes only when the current observation would change the next action: memory that knows when to stay silent. Unlike reconstruction-based memory, the gate is trained directly against a closed-loop action-error signal. Its inference state is fixed at 4,224 bytes regardless of horizon, while a KV-cache grows to 6,061 times larger at 100,000 steps.
On a controlled synthetic benchmark, AURA-Mem matches the best O(1) baseline in accuracy while using 5.19-6.13 times fewer writes, and up to 9.19 times fewer writes on easier configurations. Budget-matched random and periodic schedules do not recover this gain, isolating the benefit to the action-surprise signal. On a trained closed-loop OpenVLA-OFT 7B panel on LIBERO-Long (n=60 episodes per arm), the gate does not hurt success: AURA-Mem matches the ungated base policy (0.233) and slightly exceeds an always-write KV arm (0.217), while using 7.0 times fewer writes and constant memory. We also instantiate an approximate-information-state value-loss bound as a methodology demonstration; at this scale, the bound is vacuous rather than a guarantee.
