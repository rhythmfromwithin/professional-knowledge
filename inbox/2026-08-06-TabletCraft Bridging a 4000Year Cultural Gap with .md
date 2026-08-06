---
title: "TabletCraft: Bridging a 4,000-Year Cultural Gap with Bidirectional Akkadian NMT and Cuneiform Rendering"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.02609
priority: high
status: unread
interest: medium
next_step: skim
---
# TabletCraft: Bridging a 4,000-Year Cultural Gap with Bidirectional Akkadian NMT and Cuneiform Rendering
> 原文: [https://arxiv.org/abs/2608.02609](https://arxiv.org/abs/2608.02609)

arXiv:2608.02609v1 Announce Type: new
Abstract: Half a million cuneiform clay tablets survive in museums worldwide, yet modern users can neither read nor write in the world's oldest writing system, leaving a 4,000-year cultural barrier that existing NLP tools have only partially addressed.
Prior work enables one-way, scholar-oriented translation from Akkadian to English, but offers no path in the reverse direction: non-specialist users cannot compose new content in cuneiform, and therefore remain passive consumers of ancient culture rather than active participants.
We present TabletCraft, the first open-source system that enables bidirectional interaction with Mesopotamian writing. Users can read ancient tablets (Akkadian to English) and compose new messages as cuneiform clay tablets (English to Akkadian to cuneiform to rendered tablet).
The system integrates a ByT5-based translation model trained on 116K bidirectional samples, a cuneiform sign converter with 14,240 mappings (95.3% coverage), and a visual tablet renderer, packaged as a pip-installable toolkit with CLI and web demo.
On the held-out Akkademia validation split (2,812 samples), we report 49.1 BLEU for Akkadian-to-English and 48.5 BLEU for English-to-Akkadian, the first published quantitative result in the reverse direction.
