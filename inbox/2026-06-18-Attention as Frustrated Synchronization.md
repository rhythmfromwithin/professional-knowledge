---
interest: medium
link: https://arxiv.org/abs/2606.18694
next_step: skim
priority: low
slack_ts: '1781759639.497079'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Attention as Frustrated Synchronization
---
# Attention as Frustrated Synchronization
> 原文: [https://arxiv.org/abs/2606.18694](https://arxiv.org/abs/2606.18694)

arXiv:2606.18694v1 Announce Type: cross
Abstract: A network of oscillators that synchronizes perfectly computes nothing further, so an attention architecture built from synchronization must locate its computation in structured departures from agreement. We introduce the Frustrated Synchronization Network (FSN), whose token states are phases on a torus and whose entire value pathway is one learned complex coupling kernel over harmonics and a one-step delay. Each component of the kernel is a frustration in the sense of the synchronization literature. The complex phases are static Kuramoto-Sakaguchi frustration angles, the signed harmonics are repulsive Daido components, and the delay term, which couples each token to the successors of the tokens it attends to, is algebraically identical to Kuramoto-Sakaguchi coupling whose frustration angle is the data's own transition, so next-token prediction is implemented as synchronization frustrated by the data. At matched one-million-parameter and training budgets on character-level text and code, the FSN's validation loss is below a tuned RoPE-SwiGLU transformer's at every epoch measured, and the comparison survives training the baseline to convergence: every thirty-epoch enwik8 seed finishes below the transformer's converged fifty-epoch loss of 1.611, and the FSN's completed fifty-epoch runs converge to 1.5953 +/- 0.0014. A variant with every feed-forward block replaced by mean-field coupling to learned collective modes, leaving no multilayer perceptron in the stack, tracks the transformer. On natural text the unfrustrated base layer falls behind the converged transformer at every copy depth, worst on long-range copy events; the kernel reverses the deficit at every depth of four and beyond. Headline comparisons are at the one-million-parameter scale; a scale ladder is complete through four million parameters with the advantage persisting, and remaining arms are marked as in progress.
