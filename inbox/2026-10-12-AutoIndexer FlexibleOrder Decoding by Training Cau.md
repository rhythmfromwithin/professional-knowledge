---
interest: medium
link: https://arxiv.org/abs/2610.12545
next_step: skim
priority: high
slack_ts: '1791783316.644139'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'AutoIndexer: Flexible-Order Decoding by Training Causal Models on Chains of
  Edits'
---
# AutoIndexer: Flexible-Order Decoding by Training Causal Models on Chains of Edits
> 原文: [https://arxiv.org/abs/2610.12545](https://arxiv.org/abs/2610.12545)

arXiv:2610.12545v1 Announce Type: new
Abstract: Autoregressive decoding is less suited to non-causally ordered data, e.g., cross-references or future dependencies, since their outputs cannot be revised post hoc, unlike iterative human reasoning. Diffusion LLMs partially mitigate this limitation but still cannot flexibly insert or remove arbitrary numbers of tokens from a pre-generated context. We design AutoIndexer as a generative model with a novel training and decoding mechanism that simulates a Chain of Edits, allowing the model to flexibly modify its prior outputs in hindsight via token insertions, substitutions, and deletions. The model learns to predict marker tokens for opening and closing edits, simultaneously moving a cursor to positions in the existing token sequence, analogous to a text editor. Training sequences are obtained by perturbing ground-truth labels with inverse chained edit operations, and the model learns to edit by undoing those inverses. The perturbation training allows AutoIndexer to be robust to erroneous context and adaptable to editing tasks such as code correction. We demonstrate that our method exhibits post-generation context-editing capabilities that most autoregressive and diffusion models lack without compromising performance on standard LLM benchmarks. The code is available at https://github.com/AutodeskAILab/autoindexer.
