---
title: "Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2611.06418
priority: low
status: unread
interest: medium
next_step: skim
---
# Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness
> 原文: [https://arxiv.org/abs/2611.06418](https://arxiv.org/abs/2611.06418)

arXiv:2611.06418v1 Announce Type: new
Abstract: Brains and large language models need not be considered equivalent systems to reveal an interpretable commonality: both exhibit high-dimensional, nonlinear dynamics whose behavior can only be modeled imperfectly. This creates a shared challenge whenever we seek to intervene in their dynamics. A controller may either rely on a model identified around a particular operating regime and risk failure as the system moves away from that regime, or explicitly account for uncertainty and a changing internal state. Neurostimulation has confronted an analogous problem for decades. The limitations of fixed, open-loop stimulation have motivated closed-loop and state-dependent approaches that condition intervention on the ongoing state of the neural system. Inspired by this principle, we formulate LLM steering as a feedback-control problem in which the network's internal state, rather than a fixed intervention alone, determines how the system is perturbed. We further account for the mismatch between tractable dynamical models and the nonlinear transformer they approximate through robust control. As one principled realization of this framework, we develop an $H\_\infty$-based steering controller that limits sensitivity to disturbances and linearization mismatches. Across multiple steering benchmarks, the controller improves performance over existing baselines, with particularly pronounced gains under out-of-distribution conditions and varying length complexities. Beyond controller performance, we introduce robust steerability, $S\_{\mathrm{rob}}$, a pre-deployment measure of tolerance to dynamics mismatch; across model-task pairs, it exhibits task-specific structure and varies systematically with model scale. Beyond robust LLM steering, our measure asks not merely whether control is possible, but how much uncertainty it can survive; a principle that may span artificial and biological neural systems.
