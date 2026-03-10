---
title: "Review Beats Planning: Dual-Model Interaction Patterns for Code Synthesis"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.03406
priority: low
status: unread
interest: medium
next_step: skim
---
# Review Beats Planning: Dual-Model Interaction Patterns for Code Synthesis
> 原文: [https://arxiv.org/abs/2603.03406](https://arxiv.org/abs/2603.03406)

arXiv:2603.03406v1 Announce Type: new
Abstract: How should two language models interact to produce better code than either can alone? The conventional approach -- a reasoning model plans, a code specialist implements -- seems natural but fails: on HumanEval+, plan-then-code degrades performance by 2.4 percentage points versus the code specialist alone. We show that reversing the interaction changes everything. When the code specialist generates freely and the reasoning model reviews instead of plans, the same two models on the same hardware achieve 90.2% pass@1 -- exceeding GPT-4o (87.2%) and O1 Preview (89.0%) -- on ~$2/hr of commodity GPU. Cross-benchmark validation across 542 problems (HumanEval+ and MBPP+) reveals a moderating variable: review effectiveness scales with specification richness, yielding 4x more improvement on richly-specified problems (+9.8pp) than on lean ones (+2.3pp), while remaining net-positive in both cases. The practical implication is twofold: compose models by their cognitive strengths (reviewers review, coders code), and invest in specification quality to amplify the returns.
