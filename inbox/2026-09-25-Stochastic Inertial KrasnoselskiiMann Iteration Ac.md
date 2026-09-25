---
title: "Stochastic Inertial Krasnosel'skii-Mann Iteration Achieves Near-Optimal Sample Complexity"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.28543
priority: medium
status: unread
interest: medium
next_step: skim
---
# Stochastic Inertial Krasnosel'skii-Mann Iteration Achieves Near-Optimal Sample Complexity
> 原文: [https://arxiv.org/abs/2609.28543](https://arxiv.org/abs/2609.28543)

arXiv:2609.28543v1 Announce Type: new
Abstract: We analyze a simple stochastic inertial Krasnosel'skii--Mann (iKM) method for finding a fixed point of a nonexpansive operator in a real Hilbert space. Our method is obtained simply by adding two inertial extrapolations to stochastic KM [Bravo and Cominetti, 2024], and it retains one call to a possibly biased stochastic oracle per update and achieves sharp rates in both the stochastic and deterministic regimes. Specifically, with our proposed parameter schedule, we prove the following last-iterate fixed-point residual bound: \[
{O}\!\left(\frac{1}{K} +\frac{\sigma\log K}{\sqrt K} +\frac{B\_K\log K}{K}\right), \] where $K$ is the horizon, $\sigma$ is the noise level and $B\_K$ is the accumulated root-mean-square bias. When $B\_K=O(\sqrt K)$, this yields $\widetilde O(\epsilon^{-2})$ sample complexity that matches, up to a logarithmic factor, the stochastic-oracle lower bound given under the unbiased subclass of our model [Foster et al., 2019, Theorem 2]. It also improves the best-known $O(\epsilon^{-4})$ random-iterate guarantee for stochastic KM [Bravo and Cominetti, 2024, Corollary 5.4]. To our knowledge, this is the first single-loop method for general nonexpansive fixed-point problems to attain this near-optimal sample complexity without variance reduction or batching. When the oracle is exact, the same method attains the worst-case-optimal $O(K^{-1})$ last-iterate residual rate [Park and Ryu, 2022, Theorem 4.6], improving the $O(K^{-1/2})$ rate of classical KM [Cominetti et al., 2014; Bravo and Cominetti, 2018].
