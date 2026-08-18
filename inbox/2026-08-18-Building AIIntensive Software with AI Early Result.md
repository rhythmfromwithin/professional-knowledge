---
title: "Building AI-Intensive Software with AI: Early Results and a Cautionary Tale on Measuring Development Cost"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.13730
priority: low
status: unread
interest: medium
next_step: skim
---
# Building AI-Intensive Software with AI: Early Results and a Cautionary Tale on Measuring Development Cost
> 原文: [https://arxiv.org/abs/2608.13730](https://arxiv.org/abs/2608.13730)

arXiv:2608.13730v1 Announce Type: new
Abstract: Empirical reports on the true cost of AI-intensive software development remain scarce, and the few that exist are easy to get wrong in ways that never surface in the final number. We report early results from an ongoing case study: a six-person student team built a full conversational onboarding assistant -- RAG-based code chat, guided tours, dependency graphs, technical-debt analysis -- over one academic term using pervasive AI assistance. We instrumented development with a three-layer cost model (real AI spend, self-reported human effort, human counterfactual) and initially reported a 19.4x cost ratio. A follow-up pass revealed two independent errors -- inferring per-token cost under a flat-rate subscription, and pricing the counterfactual with the wrong regional labor rates -- that together had inflated the ratio by roughly 2x; the corrected figure is ~9.9x. We present this correction as an early, generalizable finding in its own right: both errors are easy to make, invisible in the final number, and plausibly common in similar reports. We outline next steps toward a more robust, replicable costing methodology for AI-intensive development.
