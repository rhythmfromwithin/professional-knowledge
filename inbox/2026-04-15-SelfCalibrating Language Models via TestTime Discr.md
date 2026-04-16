---
interest: medium
link: https://arxiv.org/abs/2604.09624
next_step: skim
priority: high
slack_ts: '1776310486.197409'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Self-Calibrating Language Models via Test-Time Discriminative Distillation
---
# Self-Calibrating Language Models via Test-Time Discriminative Distillation
> 原文: [https://arxiv.org/abs/2604.09624](https://arxiv.org/abs/2604.09624)

arXiv:2604.09624v1 Announce Type: new
Abstract: Large language models (LLMs) are systematically overconfident: they routinely express high certainty on questions they often answer incorrectly. Existing calibration methods either require labeled validation data, degrade under distribution shifts, or incur substantial inference costs. Recent work has shown that LLMs already contain a better-calibrated signal than the one they verbalize: the token probability of "True" when the model is asked "Is this answer correct?" ($P(\text{True})$) consistently outperforms their stated confidence, a gap that is theoretically grounded as generative error is lower-bounded by roughly twice the corresponding discriminative error. We introduce $\textbf{SECL}$ ($\textbf{SE}$lf-$\textbf{C}$alibrating $\textbf{L}$anguage Models), a test-time training (TTT) pipeline that exploits this gap as label-free self-supervision, requiring no labeled data or human supervision. SECL adapts only when the input distribution shifts, training on just 6--26% of the question stream at lower cost than the baseline it distills from. Across four small language models from three model families and four diverse domains, SECL reduces Expected Calibration Error (ECE) by 56--78%, outperforming its own supervision signal and matching or outperforming recent inference-time methods. SECL is the first method to apply TTT to calibration; seven ablations covering signal quality, gating strategy, weight accumulation, loss design, domain ordering, hyperparameter sensitivity, and layer selection confirm that each component is crucial and robust across configurations. Code: https://anonymous.4open.science/r/secl-emnlp26-submission-C890
