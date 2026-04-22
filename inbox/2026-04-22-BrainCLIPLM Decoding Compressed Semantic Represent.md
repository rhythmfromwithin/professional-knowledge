---
interest: medium
link: https://arxiv.org/abs/2604.16370
next_step: skim
priority: high
slack_ts: '1776828600.153419'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Brain-CLIPLM: Decoding Compressed Semantic Representations in EEG for Language
  Reconstruction'
---
# Brain-CLIPLM: Decoding Compressed Semantic Representations in EEG for Language Reconstruction
> 原文: [https://arxiv.org/abs/2604.16370](https://arxiv.org/abs/2604.16370)

arXiv:2604.16370v1 Announce Type: new
Abstract: Decoding natural language from non-invasive electroencephalography (EEG) remains fundamentally limited by low signal-to-noise ratio and restricted information bandwidth. This raises a fundamental question regarding whether sentence-level linguistic structure can be reliably recovered from such signals. In this work, we suggest that this assumption may not hold under realistic information constraints, and instead propose a semantic compression hypothesis in which EEG signals encode a compressed set of semantic anchors rather than full linguistic structure. Under our new perspective, direct sentence reconstruction becomes an overparameterized objective relative to the intrinsic information capacity of EEG. To address this mismatch, we introduce Brain-CLIPLM, a two-stage framework that decomposes EEG-to-text decoding into semantic anchor extraction via contrastive learning and sentence reconstruction using a retrieval-grounded large language model (LLM) with Chain-of-Thought (CoT) reasoning, following a granularity matching principle that aligns decoding complexity with neural information capacity. Evaluated on the Zurich Cognitive Language Processing Corpus, Brain-CLIPLM achieves 67.55\% top-5 and 85.00\% top-25 sentence retrieval accuracy, significantly outperforming direct decoding baseline, while cross-subject evaluation confirms robust generalization. Control analyses, including permutation testing, further demonstrate that EEG-derived representations carry sentence-specific information beyond language model priors. These results suggest that EEG-to-text decoding is better framed as recovering compressed semantic content rather than reconstructing full sentences, providing a biologically grounded and data-efficient pathway for non-invasive brain-computer interfaces.
