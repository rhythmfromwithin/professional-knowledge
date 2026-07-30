---
interest: medium
link: https://arxiv.org/abs/2607.21633
next_step: skim
priority: high
slack_ts: '1785380029.951649'
source: cs.LG - Machine Learning
status: unread
title: On the Depth Scalability of Logic Gate Networks
---
# On the Depth Scalability of Logic Gate Networks
> 原文: [https://arxiv.org/abs/2607.21633](https://arxiv.org/abs/2607.21633)

arXiv:2607.21633v1 Announce Type: new
Abstract: Logic Gate Networks (LGNs) implement computation through compositions of Boolean operations, yet unlike classical Boolean circuits, existing LGNs do not reliably benefit from increased depth. We identify two distinct causes: optimization collapse in deep relaxed LGNs and a topology-induced limitation that persists even when skip-biased initialization and straight-through estimation stabilize training. Thus, trainability alone is insufficient; deeper layers must also receive information that supports useful computation.
We introduce Input-Anchored Logic Gate Networks (IALGNs), in which each gate combines an evolving hidden feature with a direct input anchor. This topology preserves a computational spine while conditioning every layer on the original input. We show that a depth-D path can depend on up to D+1 input bits and establish a strict path-wise depth hierarchy. Random-k anchor relaxation further improves anchor selection without relaxing the spine.
Across MNIST, CIFAR-10, and CIFAR-100, IALGNs achieve consistent fixed-width depth--accuracy improvements beyond 100 layers, whereas alternative LGN topologies saturate or degrade. Layer-wise probes, topology ablations, and effective-depth analysis show that input anchoring produces progressively more informative representations and preserves longer computational paths. These results demonstrate that scalable depth in LGNs requires both stable optimization and an information-access pattern that supports input-conditioned refinement.
