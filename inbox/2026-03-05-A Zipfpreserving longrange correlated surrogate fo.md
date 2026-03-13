---
interest: medium
link: https://arxiv.org/abs/2603.02213
next_step: skim
priority: high
slack_ts: '1773369792.334639'
source: cs.CL - Computation and Language (NLP)
status: unread
title: A Zipf-preserving, long-range correlated surrogate for written language and
  other symbolic sequences
---
# A Zipf-preserving, long-range correlated surrogate for written language and other symbolic sequences
> 原文: [https://arxiv.org/abs/2603.02213](https://arxiv.org/abs/2603.02213)

arXiv:2603.02213v1 Announce Type: new
Abstract: Symbolic sequences such as written language and genomic DNA display characteristic frequency distributions and long-range correlations extending over many symbols. In language, this takes the form of Zipf's law for word frequencies together with persistent correlations spanning hundreds or thousands of tokens, while in DNA it is reflected in nucleotide composition and long-memory walks under purine-pyrimidine mappings. Existing surrogate models usually preserve either the frequency distribution or the correlation properties, but not both simultaneously.
We introduce a surrogate model that retains both constraints: it preserves the empirical symbol frequencies of the original sequence and reproduces its long-range correlation structure, quantified by the detrended fluctuation analysis (DFA) exponent. Our method generates surrogates of symbolic sequences by mapping fractional Gaussian noise (FGN) onto the empirical histogram through a frequency-preserving assignment. The resulting surrogates match the original in first-order statistics and long-range scaling while randomising short-range dependencies.
We validate the model on representative texts in English and Latin, and illustrate its broader applicability with genomic DNA, showing that base composition and DFA scaling are reproduced. This approach provides a principled tool for disentangling structural features of symbolic systems and for testing hypotheses on the origin of scaling laws and memory effects across language, DNA, and other symbolic domains.
