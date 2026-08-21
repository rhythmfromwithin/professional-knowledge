---
title: "Scheduling and Routing with Degradation-Triggered Job Arrivals: An Application to Forest Firefighting with an Unmanned Aerial Vehicle Fleet"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.18140
priority: medium
status: unread
interest: medium
next_step: skim
---
# Scheduling and Routing with Degradation-Triggered Job Arrivals: An Application to Forest Firefighting with an Unmanned Aerial Vehicle Fleet
> 原文: [https://arxiv.org/abs/2608.18140](https://arxiv.org/abs/2608.18140)

arXiv:2608.18140v1 Announce Type: new
Abstract: We define an intertwined scheduling and routing problem where new jobs appear due to the degradation of the existing jobs. Specifically, once a job arrives at a potential job location, a time window begins during which the demand of the job can be fulfilled. The demand degrades within the time window, and once it surpasses a particular threshold, it triggers the arrival of new jobs. Each job location inherently possesses an initial default reward, and the presence of an unprocessed job at a location gradually reduces this default value. The overall objective is to maximize the total remaining reward. The underlying motivation of this problem aligns with the proverb ``a stitch in time saves nine," and the problem itself carries practical implications. We focus on the problem in the context of aerial forest firefighting. Each ignited area has a designated action window; delaying intervention causes the fire to grow, diminishing the area's value and causing it to spread to adjacent areas. We develop a mixed-integer programming model that maximizes value retention in wildfire-threatened regions, and a hybrid model based on dynamic constraint generation to enhance the scalability of the model. We evaluate the performance and practicality of our models through computational experiments and a case study. Additionally, we ensure the study's reproducibility and encourage further research by providing open access to the codebase of our model.
