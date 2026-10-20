---
title: "Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.24052
priority: low
status: unread
interest: medium
next_step: skim
---
# Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks
> 原文: [https://arxiv.org/abs/2610.24052](https://arxiv.org/abs/2610.24052)

arXiv:2610.24052v1 Announce Type: new
Abstract: AI agents are growing more capable and persistent, and are being deployed in ever larger numbers. As more start collaborating, AI control measures must remain effective when they covertly collude on a harmful objective. We introduce MiniLab, a synthetic series of live services and codebases (5 interconnected services, 249 benign tasks, 8 attack objectives), adapted from internal AI deployment infrastructure. We demonstrate distributed attacks, in which different agents carry out separate attack fragments, and how their covertness evades frontier monitors when reading their trajectories individually. We show how distributed attacks spread across diverse contexts and harmful objectives through 16 human-optimized attacks (weight exfiltration, unmonitored rogue deployment, permission elevation, and more). A frontier monitor, GPT-5.6 Sol, reading each agent separately flags only 7% of successful distributed attacks, compared with 87% when a single agent carries out the same side task. Individual attacks can also be composed into longer attack sequences toward a greater loss-of-control outcome, without any individual agent being flagged. Finally, we tested whether models can plan these covert attacks: even with execution and monitor feedback, the best model-planned attacks succeed covertly against a single-trajectory GPT-5.6 Sol monitor in at most 25% of executions, compared with 80% for human-crafted plans, though this may scale with model capabilities. By turning worst-case coordinated attacks into reproducible red-team cases, our work provides a foundation for preventing locally benign agent actions from accumulating into system-level loss of control.
