---
interest: medium
link: https://arxiv.org/abs/2605.13919
next_step: skim
priority: high
slack_ts: '1778903364.122589'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Merging Methods for Multilingual Knowledge Editing for Large Language Models:
  An Empirical Odyssey'
---
# Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey
> 原文: [https://arxiv.org/abs/2605.13919](https://arxiv.org/abs/2605.13919)

arXiv:2605.13919v1 Announce Type: new
Abstract: Multilingual knowledge editing (MKE) remains challenging because language-specific edits interfere with one another, even when locate-then-edit methods work well in monolingual settings. This paper focuses on three issues: the effectiveness of vector merging methods for MKE, the extent to which Task Singular Vectors for Merging (TSVM) can reduce multilingual interference, and the influence of the weight scaling factor and rank compression ratio on performance. We evaluate six merging variants with two popular backbone large language models, two base knowledge editing methods, and 12 languages on the MzsRE benchmark under a large-scale batch-editing setting. Our results show that vector summation with shared covariance is the most reliable overall strategy, whereas simple summation without shared covariance performs poorly. TSVM improves performance in some settings, but its ability to mitigate multilingual interference is limited. We also find that performance is sensitive to both weight scale and rank ratio, with larger-than-default scaling and relatively low rank often yielding better results. These findings clarify the practical strengths and limits of current vector merging methods for MKE and provide guidance for future multilingual knowledge editing research.
