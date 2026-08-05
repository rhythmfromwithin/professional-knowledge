---
title: "AutoFOAM: The Self-Refining Autonomous OpenFOAM Agent"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2608.00003
priority: high
status: unread
interest: medium
next_step: skim
---
# AutoFOAM: The Self-Refining Autonomous OpenFOAM Agent
> 原文: [https://arxiv.org/abs/2608.00003](https://arxiv.org/abs/2608.00003)

arXiv:2608.00003v1 Announce Type: new
Abstract: Computational Fluid Dynamics (CFD) plays an important role in modern engineering, but using open-source solvers such as OpenFOAM requires considerable knowledge and skills, as well as time-consuming configuration file setup. To reduce this burden, we propose AutoFOAM - a self-evolving large language model (LLM) agent that creates, evaluates, runs, and evolves its own OpenFOAM simulations based solely on natural-language instructions. Our model is pre-trained on the Qwen-coder 2.5-14B, which is then fine-tuned on 252 text prompts targeting 7 OpenFOAM solvers, 13 parametrized mesh templates, and a y plus-aware numerical policy. The crucial element of the algorithm is a sophisticated evolution loop composed of 7 stages. To prevent model degeneration under repeated self-training, the agent employs three complementary anti-collapse streams: RAG-augmented retry context, surgical dictionary-level patching, and prompt-diversity paraphrasing. By bridging generative artificial intelligence with rigorous fluid simulations, AutoFOAM accelerates rapid prototyping and democratizes advanced CFD workflows.
