---
interest: medium
link: https://arxiv.org/abs/2605.18956
next_step: skim
priority: medium
slack_ts: '1779337383.815139'
source: cs.CV - Computer Vision
status: unread
title: 'MotionMERGE: A Multi-granular Framework for Human Motion Editing, Reasoning,
  Generation, and Explanation'
---
# MotionMERGE: A Multi-granular Framework for Human Motion Editing, Reasoning, Generation, and Explanation
> 原文: [https://arxiv.org/abs/2605.18956](https://arxiv.org/abs/2605.18956)

arXiv:2605.18956v1 Announce Type: new
Abstract: Recent motion-language models unify tasks like comprehension and generation but operate at a coarse granularity, lacking fine-grained understanding and nuanced control over body parts needed for animation or interaction. This stems from fundamental issues in both the model and the data, in which the model can't focus on motion's localized pattern, and the training data lacks fine-grained supervision. To tackle this, we propose MotionMERGE, a unified framework that bridges the granularity gap. First, we pioneer the study of fine-grained languageguided motion control, including detailed understanding and localized editing, by explicitly modeling motion at part and temporal levels within a single LLM, thereby endowing the model with robust priors for precise control. Second, we design ReasoningAware Granularity-Synergy pre-training, a novel strategy that employs joint supervision for cross-granularity alignment, temporal grounding, localized alignment, motion coherency, and motion-grounded chain-of-thought (CoT) reasoning. This equips the model with fine-grained motion-language alignment, crossgranularity synergy, and explicit reasoning ability. Third, we curate MotionFineEdit, a large-scale dataset (837K atomic + 144K complex triplets) with the first fine-grained spatio-temporal corrective instructions and motion-grounded CoT annotations, establishing a new benchmark for fine-grained text-driven motion editing and motion-grounded reasoning. Extensive experiments demonstrate the capability of MotionMERGE for more precise motion generation, understanding, and editing, and compelling zero-shot generalization to other complex motion tasks. This work represents a significant step toward models that interact with motion in finer granularity and human-like reasoning.
