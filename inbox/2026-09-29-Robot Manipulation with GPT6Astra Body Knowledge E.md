---
interest: medium
link: https://arxiv.org/abs/2609.31770
next_step: skim
priority: medium
slack_ts: '1790659465.882109'
source: cs.RO - Robotics
status: unread
title: 'Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent
  Skills, and Sim2Real Transfer'
---
# Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer
> 原文: [https://arxiv.org/abs/2609.31770](https://arxiv.org/abs/2609.31770)

arXiv:2609.31770v1 Announce Type: new
Abstract: General-purpose multimodal agents can write robot-control programs, but repeated exploration and model-mediated action selection can make execution slow. We study how external body knowledge, successful experience, and executable skills improve an XLeRobot controlled by GPT-6-Astra in a simulated and a physical elevator-button task. In 30 fixed-start simulation trials, complete robot geometry and camera information reduce mean completion time by 57.4% relative to a baseline with only the common control interface and no prior experience; images with synchronized action and state records reduce it by 68.6% without additional body assets. In nine paired comparisons (18 trials) at starts displaced by 10-100 cm, experience recorded at the original start reduces mean time by 58-63% relative to no experience, demonstrating generalization to the tested new starting positions. During experience experiments, GPT-6-Astra spontaneously generates a short visual-feedback program. Researcher-refactored versions reduce mean local-task time by 29-31% in 27 simulation trials. Finally, 12 real-robot trials using operator-confirmed button contact demonstrate sim2real reuse: at a shared nominal start, simulation XML assets and simulation experience reduce mean time by 53.0% and 49.9%, respectively; real experience also transfers to two new starts. These results suggest a practical way to build general-purpose manipulation experiments around GPT-6-Astra: supply machine-readable body descriptions and synchronized demonstrations, and turn useful agent-generated feedback routines into reusable skills, while the agent adapts actions from current images. We release all task prompts, trial-level experimental data, and acquired skill implementations at https://github.com/hesd10/astra-robot-sim2real.
