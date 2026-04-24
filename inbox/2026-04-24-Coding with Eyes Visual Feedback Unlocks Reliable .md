---
title: "Coding with Eyes: Visual Feedback Unlocks Reliable GUI Code Generating and Debugging"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.19750
priority: low
status: unread
interest: medium
next_step: skim
---
# Coding with Eyes: Visual Feedback Unlocks Reliable GUI Code Generating and Debugging
> 原文: [https://arxiv.org/abs/2604.19750](https://arxiv.org/abs/2604.19750)

arXiv:2604.19750v1 Announce Type: new
Abstract: Recent advances in Large Language Model (LLM)-based agents have shown remarkable progress in code generation. However, current agent methods mainly rely on text-output-based feedback (e.g. command-line outputs) for multi-round debugging and struggle in graphical user interface (GUI) that involve visual information. This is mainly due to two limitations: 1) GUI programs are event-driven, yet existing methods cannot simulate user interactions to trigger GUI element logic 2) GUI programs possess visual attributes, making it difficult for text-based approaches to assess whether the rendered interface meets user needs. To systematically address these challenges, we first introduce InteractGUI Bench, a novel benchmark comprising 984 commonly used real-world desktop GUI application tasks designed for fine-grained evaluation of both interaction logic and visual structure. Furthermore, we propose VF-Coder, a vision-feedback-based multi-agent system for debugging GUI code. By perceiving visual information and directly interacting with program interfaces, VF-Coder can identify potential logic and layout issues in a human-like manner. On InteractGUI Bench, our VF-Coder approach increases the success rate of Gemini-3-Flash from 21.68% to 28.29% and raises the visual score from 0.4284 to 0.5584, indicating the effectiveness of visual feedback in GUI debugging.
