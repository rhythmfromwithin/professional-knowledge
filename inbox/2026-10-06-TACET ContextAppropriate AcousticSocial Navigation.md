---
interest: medium
link: https://arxiv.org/abs/2610.03828
next_step: skim
priority: medium
slack_ts: '1791266370.950139'
source: cs.RO - Robotics
status: unread
title: 'TACET: Context-Appropriate Acoustic-Social Navigation for Quadrupeds'
---
# TACET: Context-Appropriate Acoustic-Social Navigation for Quadrupeds
> 原文: [https://arxiv.org/abs/2610.03828](https://arxiv.org/abs/2610.03828)

arXiv:2610.03828v1 Announce Type: new
Abstract: Quadruped robots entering hospitals, care homes, and quiet offices must be context-appropriate not only in where they move but in how loudly they move: a legged robot's locomotion noise, dominated by foot-ground impacts, is itself a social variable. Prior social navigation respects human space but treats the robot as acoustically uniform, while quiet-locomotion methods reduce noise to an operator-specified, context-blind level. We present TACET, a context-appropriate acoustic-social navigation method that infers social context from the robot's egocentric view and decides both where it walks and how loudly, coupling a slow fine-tuned vision-language reasoner to a fast reactive controller through a single compact behavior token, . The same token conditions both a social costmap (where to go) and a quiet locomotion policy (how loudly to move), while a structured out-of-view memory keeps recently seen people in the reasoner's context after they leave the camera view. On a real quadruped, context-conditioned locomotion lowers locomotion noise by up to 9.3 dBA at matched speed, and across our scenarios the full method keeps personal-space compliance at 100% with low acoustic intrusion (<=2.9 dBA), jointly improving spatial and acoustic performance in the evaluated scenarios. The project page is available at https://rcilab.khu.ac.kr/tacet/.
