---
title: "DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.05241
priority: medium
status: unread
interest: medium
next_step: skim
---
# DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation
> 原文: [https://arxiv.org/abs/2605.05241](https://arxiv.org/abs/2605.05241)

arXiv:2605.05241v1 Announce Type: new
Abstract: Sim-to-real transfer remains a critical bottleneck for deploying dexterous manipulation policies learned in simulation to real-world robots. Existing approaches rely on manually designed domain randomization or task-specific adaptation, limiting their generalizability across diverse manipulation scenarios. We present DexSim2Real, an integrated framework that leverages vision-language foundation models to bridge the sim-to-real gap for dexterous manipulation. Our system combines three components: (1) Foundation Model-Guided Domain Randomization (FM-DR), which uses a vision-language model as a visual realism critic to optimize simulation parameters via closed-loop CMA-ES, complementing text-based approaches like DrEureka with direct visual feedback; (2) a Tactile-Visual Cross-Attention Policy (TVCAP) that adapts cross-attention visuo-tactile fusion to zero-shot sim-to-real RL; and (3) a Progressive Skill Curriculum (PSC) that builds on LLM-based task decomposition with a difficulty scheduler tailored to contact-rich dexterous tasks. Extensive experiments on six challenging manipulation tasks with blinded evaluation demonstrate that DexSim2Real achieves a 78.2% average real-world success rate, outperforming DrEureka and DeXtreme while reducing the sim-to-real performance gap to only 8.3%.
