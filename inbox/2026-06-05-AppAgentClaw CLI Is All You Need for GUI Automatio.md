---
title: "AppAgent-Claw: CLI Is All You Need for GUI Automation"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2606.05171
priority: low
status: unread
interest: medium
next_step: skim
---
# AppAgent-Claw: CLI Is All You Need for GUI Automation
> 原文: [https://arxiv.org/abs/2606.05171](https://arxiv.org/abs/2606.05171)

arXiv:2606.05171v1 Announce Type: new
Abstract: The OpenClaw platform provides a practical foundation for automation through its skill-oriented architecture, organizing external capabilities into lightweight, reusable components that can be invoked efficiently through a command-line interface (CLI). However, a significant bottleneck remains: many real-world tasks are confined to graphical user interfaces (GUIs) with no stable API available. While LLM-based GUI agents offer generality, their reliance on repeated live model inference makes them too slow, costly, and inconsistent to serve as efficient OpenClaw skills. In this paper, we present AppAgent-Claw, a demonstration-driven system that converts GUI workflows into reliable, reusable skills without runtime inference. By following a ``record-once, replay-many'' paradigm, the system captures rich contextual metadata to facilitate robust execution. It employs a layered localization strategy to handle visual shifts and a validation-coupled execution model to ensure intended on-screen effects. AppAgent-Claw provides a practical, efficient, and diagnosable solution for integrating GUI-bound tasks into the OpenClaw ecosystem.
