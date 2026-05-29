---
title: "The Cognitive Categorical Transformer: Category-Theoretic Inductive Biases for Language Modeling"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.28864
priority: high
status: unread
interest: medium
next_step: skim
---
# The Cognitive Categorical Transformer: Category-Theoretic Inductive Biases for Language Modeling
> 原文: [https://arxiv.org/abs/2605.28864](https://arxiv.org/abs/2605.28864)

arXiv:2605.28864v1 Announce Type: new
Abstract: The Cognitive Categorical Transformer (CCT) is a 306M-parameter architecture that augments a pretrained GPT-2 Small backbone with cognitively grounded components derived from category theory and several inspirations from cognitive science. Under a matched-step protocol (215,000 optimizer steps, matched data, matched optimizer and schedule) on WikiText-103, CCT reaches 21.27 validation perplexity, compared with 24.19 for an identically fine-tuned GPT-2 Small baseline. The architecture therefore contributes a 2.92 PPL (12% relative) reduction beyond what in-domain fine-tuning alone provides. A retrain-from-scratch ablation that holds GT-Full simplicial message passing bypassed across the entire seven-phase activation schedule reaches 23.72 PPL, localizing 84% of the architectural improvement (2.45 of 2.92 PPL) to GT-Full. We present the first ablation-validated evidence that simplicial message passing improves language-model perplexity at the 306M-parameter scale on WikiText-103. Published GPT-2 Large reaches 22.05 zero-shot PPL on WikiText-103 with 6.2x more parameters than GPT-2 Small; this paper treats that number as an external published reference, not as the architectural benchmark. Three negative results on consistency-style categorical priors (sheaf smoothing, adjunction round-trip, curvature regularization) and the joint structural-prior result for GT-Full and PrecisionWeightedPP together support an empirical pattern termed the \*structure/consistency distinction\*, in which categorical priors that add new topology improve language modeling and those that enforce a consistency identity do not.
