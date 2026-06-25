---
interest: medium
link: https://arxiv.org/abs/2606.25170
next_step: skim
priority: medium
slack_ts: '1782360765.156219'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Minimax PAC Bounds for Learning in Exogenous Contextual MDPs
---
# Minimax PAC Bounds for Learning in Exogenous Contextual MDPs
> 原文: [https://arxiv.org/abs/2606.25170](https://arxiv.org/abs/2606.25170)

arXiv:2606.25170v1 Announce Type: new
Abstract: We study PAC learning in tabular discounted Markov decision processes with exogenous i.i.d. contexts, with discount factor $\gamma$, finite state space $\mathcal X$, action space $\mathcal A$, and context space $\mathcal Z$. At each time step, a context is drawn independently from an unknown distribution $\mu$ and revealed before the agent acts. This context may affect both rewards and transitions, while remaining uncontrolled by the agent. Depending on the regime, the learner has access either to a sampling oracle for $\mu$, to a sampling oracle for the transition kernel conditioned on state-context-action tuples, or to both. Oracles can be accessed before and during policy execution. The sample complexity is measured by a couple $(n,m)$, where $n$ is the number of calls to the sampling oracles before execution and $m$ is the number of calls to the sampling oracles during execution. When rewards and transitions are known and only the context distribution $\mu$ is sampled, we give a variance-reduced algorithm that solves policy evaluation (PE), best-value estimation (BVE), and best-policy extraction (BPE) with $\left(\widetilde O\left(1/((1-\gamma)^3\varepsilon^2)\right), 0 \right) $ sample complexity. The rate is independent of $|\mathcal Z|$ and minimax optimal up to logarithmic factors. As a corollary, we also obtain tight rates in the case of one-step perfect look-ahead, improving upon the existing guarantees. In the fully unknown regime, where both $\mu$ and P must be learned, we show that PE remains $|\mathcal Z|$-free, with matching upper and lower bounds $\bigl(\widetilde O(|\mathcal X|/((1-\gamma)^3\varepsilon^2)),\, \widetilde O(1/((1-\gamma)^2\varepsilon^2))\bigr)$.
