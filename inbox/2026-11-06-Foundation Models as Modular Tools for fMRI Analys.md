---
interest: medium
link: https://arxiv.org/abs/2611.06926
next_step: skim
priority: low
slack_ts: '1794116476.638039'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Foundation Models as Modular Tools for fMRI Analysis
---
# Foundation Models as Modular Tools for fMRI Analysis
> 原文: [https://arxiv.org/abs/2611.06926](https://arxiv.org/abs/2611.06926)

arXiv:2611.06926v1 Announce Type: new
Abstract: Foundation models (FMs) for the brain are rapidly growing in number and each captures a different aspect of the same data. A single scientific question often needs several of them at once, alongside classical analysis and the literature, but no established method combines them, because each model defines its own inputs, outputs, and spatial conventions. Representation alignment, the usual route from an FM into a language model, binds one FM to one LLM and requires retraining for every model added. We take a modular route: each FM becomes an independent tool server that a fixed language agent calls next to classical and literature tools, with no retraining. We start with fMRI, where public FMs already disagree on how to name a brain location and open task data give a classical baseline, and serve two FMs at opposite ends of that spectrum, BrainLM (atlas parcels) and Omni-fMRI (atlas-free voxels). A 76-question benchmark, a 2 by 2 tool ablation, and an independent LLM judge yield 3,040 judged traces. In this first study, modular FM access raises holistic answer quality by $+0.70$ on a 1 to 5 rubric (95% CI $[+0.44, +0.97]$, $n=34$). The gain lands in how the agent selects, parameterizes, and grounds tool calls, and peaks where the agent must cross FM vocabularies. The two FMs win on different questions, yet mounting both matches the better one, and the voxel interface fails 7.8 times more often by context overflow. Modular connection works. Orchestrating what it connects, across EEG and MRI models, is the work ahead.
