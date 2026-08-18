---
title: "Adjacency-Based Spectral Proxy Control of Mobile Communication Agents"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.13616
priority: medium
status: unread
interest: medium
next_step: skim
---
# Adjacency-Based Spectral Proxy Control of Mobile Communication Agents
> 原文: [https://arxiv.org/abs/2608.13616](https://arxiv.org/abs/2608.13616)

arXiv:2608.13616v1 Announce Type: new
Abstract: We consider a heterogeneous mobile-agent network composed of uncontrolled task agents and controllable communication agents. The objective is to reposition communication agents online as task agents move. Since throughput-based objectives are generally unsuitable for real-time control, spectral graph metrics such as algebraic connectivity are commonly adopted as surrogate objectives. However, controlling algebraic connectivity relies on the eigenvector corresponding to the second-smallest eigenvalue of a graph's Laplacian matrix (i.e., the Fiedler vector), whose distributed estimation requires an unbounded number of communication rounds to converge.
In this work, we identify a structural decomposition of this Fiedler-gradient controller into a local interaction rule and a graph embedding component, suggesting the use of alternative embeddings that are easier to estimate distributively than the Fiedler vector. As a particular instance, we propose A-Fiedler, which replaces the Fiedler embedding with the dominant eigenvector of the adjacency matrix, commonly used as a graph embedding of nodes into a latent geometry. This representation is more naturally suited for distributed implementation under local communication constraints.
We evaluate A-Fiedler against the classical Fiedler-gradient controller. Results show comparable network performance in the absence of communication constraints and improved robustness under distributed estimation. For instance, under the same number of communication rounds, the Fielder-gradient may even converge to disconnected configurations whereas our proposition maintains performance. We believe our contribution provides a simpler path toward distributed network control.
