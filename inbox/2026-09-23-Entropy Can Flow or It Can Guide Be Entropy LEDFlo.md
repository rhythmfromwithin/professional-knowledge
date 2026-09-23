---
interest: medium
link: https://arxiv.org/abs/2609.25131
next_step: skim
priority: high
slack_ts: '1790137554.083979'
source: cs.LG - Machine Learning
status: unread
title: 'Entropy Can Flow, or It Can Guide. Be Entropy. LEDFlow: Introducing Entropy-guided
  Generation Order into Uniform Discrete Flow'
---
# Entropy Can Flow, or It Can Guide. Be Entropy. LEDFlow: Introducing Entropy-guided Generation Order into Uniform Discrete Flow
> 原文: [https://arxiv.org/abs/2609.25131](https://arxiv.org/abs/2609.25131)

arXiv:2609.25131v1 Announce Type: new
Abstract: Uniform discrete flow permits repeated updates at every generation position. While continued revision supports correction of wrong tokens, it also exposes correct intermediate predictions to later errors. An experiment on Sudoku puzzles shows that 9.4% of generated cells are correct at an intermediate step but incorrect in the final output. We introduce generation order into uniform discrete flow through selective absorption, which fixes chosen predictions while preserving the uniform-flow velocity at active positions. To prevent absorbing incorrect predictions, we propose Low-Entropy Discrete Flow (LEDFlow), a training-free sampler that adaptively orders absorption by local entropy. By decomposing absorption error into joint dependence and conditional prediction terms, we show that selecting the lowest-entropy positions under a fixed absorption budget minimizes an upper bound on the conditional term. We further support the choice of local entropy by showing that the decision-error bound of global lookahead grows with the lookahead window under an imperfect denoiser. Across reasoning benchmarks, LEDFlow attains 0.845 Nikoli Sudoku solve accuracy, with the largest gains on strongly constrained tasks. On text-to-image generation it attains the best overall score, and on multimodal understanding it improves over the native sampler on all six benchmarks, at an inference cost comparable to standard flow sampling.
