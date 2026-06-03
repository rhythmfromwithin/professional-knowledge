---
interest: medium
link: https://arxiv.org/abs/2605.30512
next_step: skim
priority: high
slack_ts: '1780462691.802329'
source: cs.AI - Artificial Intelligence
status: unread
title: 'PhyDrawGen: Physically Grounded Diagram Generation from Natural Language'
---
# PhyDrawGen: Physically Grounded Diagram Generation from Natural Language
> 原文: [https://arxiv.org/abs/2605.30512](https://arxiv.org/abs/2605.30512)

arXiv:2605.30512v1 Announce Type: new
Abstract: Generating physics diagrams from text requires strict adherence to physical laws. While current generative models produce visually plausible outputs, they systematically hallucinate force vectors, ignore conservation laws, and violate geometric constraints. We present PhyDrawGen, a neuro-symbolic pipeline that decouples semantic scene understanding from physical constraint satisfaction. First, a large language model extracts a typed scene graph from the problem text. A deterministic solver then converts this graph into a Planar Straight-Line Graph (PSLG), encoding force balance, optical paths, and field topologies as exact geometric primitives. Finally, a fine-tuned Qwen-VL model implements a visually grounded propose-verify loop to iteratively correct any constraint violations. Evaluated on a benchmark of 1,449 problems spanning mechanics, optics, and electromagnetism, PhyDrawGen significantly outperforms GPT-5-image, Gemini 2.5 Flash, and Gemini 3 Pro, demonstrating robust physical accuracy even on unusual-object problems.
