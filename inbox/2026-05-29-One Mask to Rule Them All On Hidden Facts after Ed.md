---
interest: medium
link: https://arxiv.org/abs/2605.28839
next_step: skim
priority: high
slack_ts: '1780290087.806229'
source: cs.LG - Machine Learning
status: unread
title: 'One Mask to Rule Them All: On Hidden Facts after Editing and How to Find Them'
---
# One Mask to Rule Them All: On Hidden Facts after Editing and How to Find Them
> 原文: [https://arxiv.org/abs/2605.28839](https://arxiv.org/abs/2605.28839)

arXiv:2605.28839v1 Announce Type: new
Abstract: Knowledge editing methods such as ROME and MEMIT update factual associations in transformer models by modifying MLP weights. While evaluated mainly by output behavior, their internal mechanism remains underexplored. We investigate whether edits rely on a common mechanism, regardless of which fact is modified. Despite fact-specific weight changes, we argue that ROME and MEMIT target the same subset of weights critical for maintaining edits. To isolate this subset, we train a compact binary mask over the edited weights. The mask reverses 80% of edits on the training set and over 70% on the test set, confirming that diverse edits share a common functional structure. Our analysis reveals that the mask reverses edits by eliminating overattention in later layers. Additionally, we show that injecting the mask during editing drops editing success from 98% to 38%, demonstrating that this mechanism is necessary for edits to succeed. Our finding that edits suppress rather than overwrite knowledge explains why ROME and MEMIT fail to propagate changes to related facts. The identified common functional subspace informs detection and defense against unwanted edits.
