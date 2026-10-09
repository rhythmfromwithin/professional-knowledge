---
title: "Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.10601
priority: medium
status: unread
interest: medium
next_step: skim
---
# Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection
> 原文: [https://arxiv.org/abs/2610.10601](https://arxiv.org/abs/2610.10601)

arXiv:2610.10601v1 Announce Type: new
Abstract: Reinforcement Learning (RL) has enabled legged robots to perform a range of skills in single-task settings. However, applications such as farm robotics or space exploration require diverse skills such as locomotion, digging, or close-range surveying. Training an end-to-end policy to address this problem remains difficult due to challenges such as sample inefficiency and gradient conflict between tasks in multi-task learning. We propose a three-stage method that trains a single policy to perform distinct tasks such as walking, digging, and hopping, and compose them into novel behaviors such as crawling. First, multiple teacher policies are trained using RL on narrowly defined tasks. Then, two additional stages train a student policy with a multi-teacher distillation setup that uses a combined RL and Imitation Learning (IL) objective under an adversarial task selection process that focuses training on the worst-performing task. With this method, we train a student policy that performs 22 tasks using 8 teachers. Evaluations show our method preserves motion quality and tracks commands more accurately than PPO and distill-then-finetune baselines, and in some cases generalizes to new tasks without explicit training. Finally, we demonstrate real-world robustness by deploying the resulting policy on a Unitree B1 quadruped. Video: https://youtu.be/V9yX04EBcFA
