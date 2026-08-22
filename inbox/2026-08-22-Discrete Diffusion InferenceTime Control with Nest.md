---
title: "Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.20123
priority: medium
status: unread
interest: medium
next_step: skim
---
# Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo
> 原文: [https://arxiv.org/abs/2608.20123](https://arxiv.org/abs/2608.20123)

arXiv:2608.20123v1 Announce Type: new
Abstract: We study inference-time control for text generation in discrete diffusion language models, where the goal is to steer sampling toward sequence-level rewards without retraining. Prior work in this domain has focused on particle-based methods such as best-of-$n$ sampling and bootstrap sequential Monte Carlo, which may suffer from overoptimism and weight degeneracy, respectively. We address these limitations using \emph{nested} sequential Monte Carlo methods. We formulate nested SMC (NSMC) and fully-adapted nested SMC (FA-NSMC) for Feynman--Kac steering, identifying and correcting errors in prior formulations that lead to biased final estimates. We evaluate these methods on toxicity and fluency steering tasks, showing that NSMC and FA-NSMC consistently outperform best-of-$n$ and bootstrap SMC.
