---
title: "What is Good? Extracting and Testing Implicit Theories of Literary Quality from LLM Reasoning Traces"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.20425
priority: high
status: unread
interest: medium
next_step: skim
---
# What is Good? Extracting and Testing Implicit Theories of Literary Quality from LLM Reasoning Traces
> 原文: [https://arxiv.org/abs/2607.20425](https://arxiv.org/abs/2607.20425)

arXiv:2607.20425v1 Announce Type: new
Abstract: What makes writing "good" remains a persistent question in literary studies and computational linguistics. We present a two-study investigation of how reasoning-enabled LLMs evaluate literary quality.
In Study 1, we construct a benchmark of 30 real texts spanning six quality tiers, from canonical literature to anonymous forum posts, and extract the model's implicit theory of quality from its reasoning traces. Across five DeepSeek replications, the model achieves 79.3% mean tier-classification accuracy. The traces reveal a consistent stated theory: the model values intentionality over correctness, prioritizing craft, depth, and distinctive voice. A familiarity experiment with style-matched but unrecognizable passages suggests that source recognition may inflate scores, although this is confounded by genuine quality differences between canonical originals and researcher-written pastiches.
In Study 2, we probe this theory through systematic degradation of five canonical prose passages. We apply six manipulations - vocabulary simplification, rhythm flattening, imagery removal, voice genericization, structure simplification, and combined degradation - and reevaluate each version. Vocabulary simplification causes the smallest quality loss (0.41 +/- 0.46 points), far below structure (2.78) or voice (2.34) loss. Combined degradation is devastating (-5.64) but subadditive. An exploratory comparison with Qwen QwQ shows the same broad qualitative pattern.
Together, these studies suggest that LLM judgments of writing quality are holistic, author-specific, and more sensitive to structural than lexical features, with implications for automated writing feedback and computational aesthetics.
