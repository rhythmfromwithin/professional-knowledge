---
interest: medium
link: https://arxiv.org/abs/2607.05465
next_step: skim
priority: medium
slack_ts: '1783569526.341209'
source: cs.CV - Computer Vision
status: unread
title: 'CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration'
---
# CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration
> 原文: [https://arxiv.org/abs/2607.05465](https://arxiv.org/abs/2607.05465)

arXiv:2607.05465v1 Announce Type: new
Abstract: Complex image creation and editing often require more than a single generation or editing model. A user request may involve synthesizing images, localizing objects, segmenting regions, editing selected content, compositing intermediate assets, reading text, and enhancing the final result. Such tasks shift multimodal agents from perception-augmented reasoning to manipulation-centered visual creation, where tools must actively transform visual states rather than merely inspect them. However, existing multimodal tool-use agents are mostly optimized for perception, search, or domain-specific editing, and lack large-scale supervision for executable image-creation trajectories. In this paper, we introduce CanvasCraft, a large-scale multimodal tool-use dataset for complex image creation and editing, and \textbf{CanvasAgent}, a tool-augmented multimodal agent that learns to orchestrate heterogeneous visual tools through multi-turn interaction. CanvasCraft contains 140K fully annotated executable trajectories and 10K
RL task specifications. CanvasAgent is first trained with SFT to learn executable reasoning-action trajectories, and is then optimized with GRPO using a hybrid reward that combines outcome- and process-level signals. During rollout, CanvasAgent inspects intermediate results, tracks visual assets, and adapts tool decisions to the evolving visual state. Experiments evaluate both final image quality and trajectory behavior, demonstrating the effectiveness of CanvasAgent and the proposed dataset for complex multi-tool image creation workflows.
