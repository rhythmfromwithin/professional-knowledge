---
title: "EditHero: A Benchmark for Long-Horizon Part-Level 3D Editing and Vibe Modeling"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.02298
priority: medium
status: unread
interest: medium
next_step: skim
---
# EditHero: A Benchmark for Long-Horizon Part-Level 3D Editing and Vibe Modeling
> 原文: [https://arxiv.org/abs/2610.02298](https://arxiv.org/abs/2610.02298)

arXiv:2610.02298v1 Announce Type: new
Abstract: 3D editing methods are usually tested on a single edit, yet an asset is built through a long sequence of revisions, each of which must implement the requested change while leaving everything else unchanged. We introduce EditHero, to our knowledge the first benchmark for long-horizon, part-level 3D editing, with natural-language instructions and target images for both geometry and texture. A deterministic assembly engine produces the exact target after every edit, and every sequence is reviewed by hand. We use EditHero to compare 2 opposite approaches to 3D editing. Non-agentic methods operate top down, regenerating the object from a learned 3D representation and inferring what to keep. In contrast, LLM/VLM agents operate bottom up, editing through code that inspects the mesh and rewrites only the parts required by instructions. The non-agentic methods often miss the requested change and disturb regions that should stay fixed. Most LLMs follow instructions more closely, and all of them preserve the unedited parts better, but each of their edits takes minutes. We will release the engine and the edit sequences to support research on reliable iterative 3D editing.
