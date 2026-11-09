---
title: "Compression of Emotion in Language Model Representations"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2611.08683
priority: high
status: unread
interest: medium
next_step: skim
---
# Compression of Emotion in Language Model Representations
> 原文: [https://arxiv.org/abs/2611.08683](https://arxiv.org/abs/2611.08683)

arXiv:2611.08683v1 Announce Type: new
Abstract: Large language models (LLMs) have been evaluated on their ability to identify emotions expressed in text and produce fluent emotional language. However, output predictions alone do not reveal how fine-grained emotion distinctions are organized internally. We study seven LLMs on GoEmotions, an English Reddit dataset annotated with 27 fine-grained emotion categories plus neutral. We compare model predictions and emotion-prompted final-token representations with the 28 GoEmotions categories and with coarser emotion-family and sentiment groupings.
We find a consistent pattern of $\textit{overcompression}$ relative to the fine-grained GoEmotions taxonomy. Under the tested KMeans protocol, when we cluster their hidden representations without using emotion labels, the clearest split is into two groups that largely separate positive from negative emotion. Coarser emotion groupings are also recovered with fewer clusters than the full 28-category taxonomy. Yet linear probes retain substantial fine-grained predictive information. These results suggest that fine-grained emotion information remains accessible even though broader affective structure more strongly organizes the unsupervised geometry.
