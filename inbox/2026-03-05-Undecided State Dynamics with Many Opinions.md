---
interest: medium
link: https://arxiv.org/abs/2603.02636
next_step: skim
priority: medium
slack_ts: '1773456092.214809'
source: cs.DC - Distributed Computing
status: unread
title: Undecided State Dynamics with Many Opinions
---
# Undecided State Dynamics with Many Opinions
> 原文: [https://arxiv.org/abs/2603.02636](https://arxiv.org/abs/2603.02636)

arXiv:2603.02636v1 Announce Type: new
Abstract: We study the Undecided-State Dynamics (USD), a fundamental consensus process in which each vertex holds one of $k$ decided opinions or the undecided state. We consider both the gossip model and the population protocol model. Prior work established tight bounds on the consensus time of this process only for the regime $k = O(\sqrt{n}/(\log n)^2)$ (for the population protocol model) and $k = O((n/\log n)^{1/3})$ (for the gossip model), often under restrictive assumptions on the initial configuration.
In this paper, we obtain the first consensus-time guarantees for USD that hold for \emph{arbitrary} $2\le k\le n$ and for \emph{arbitrary} initial configurations in both the gossip model and the population protocol model. In the gossip model, USD reaches consensus within $\widetilde O(\min\{k,\sqrt n\})$ synchronous rounds with probability $1-p\_{\bot}-n^{-c}$, where $p\_{\bot}$ is the gossip-specific probability of collapsing to the all-undecided state in the first round. In the population protocol model, USD reaches consensus within $\widetilde O(\min\{kn,n^{3/2}\})$ asynchronous interactions with high probability. We also present lower bounds that match the upper bounds up to polylogarithmic factors for a specific initial configuration and show that our upper bounds are essentially optimal.
