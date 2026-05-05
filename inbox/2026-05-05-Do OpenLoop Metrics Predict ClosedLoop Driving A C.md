---
title: "Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.00066
priority: medium
status: unread
interest: medium
next_step: skim
---
# Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive
> 原文: [https://arxiv.org/abs/2605.00066](https://arxiv.org/abs/2605.00066)

arXiv:2605.00066v1 Announce Type: new
Abstract: Open-loop evaluation offers fast, reproducible assessment of autonomous driving planners, but its ability to predict real closed-loop driving performance remains questionable. Prior work has shown that traditional open-loop metrics such as Average Displacement Error (ADE) and Final Displacement Error (FDE) exhibit no reliable correlation with closed-loop Driving Score. In this paper, we ask whether the more recent, safety-aware open-loop metrics introduced by NAVSIM~v2 can bridge this gap. By systematically cross-referencing published results from 15 state-of-the-art methods across NAVSIM (open-loop) and Bench2Drive (closed-loop), we compile a paired dataset of open-loop sub-metrics and closed-loop performance, yielding 8 methods with complete paired data. Our analysis reveals three key findings: (1) the aggregate NAVSIM PDM Score shows a strong positive but non-monotonic correlation with Bench2Drive Driving Score, with clear ranking inversions; (2) among individual NAVSIM sub-metrics, Ego Progress (EP) is the strongest single predictor of closed-loop success, substantially exceeding the safety-critical collision metric NC; (3) the safety-progress trade-off manifests differently in open-loop and closed-loop: methods that maximize safety at the expense of progress rank highly in NAVSIM but underperform in closed-loop due to timeout and slow-driving penalties. We further demonstrate that a much simpler 3-metric formula matches the predictive power of the full 5-metric PDMS at the same Spearman $\rho{=}0.90$ on our paired sample of $n{=}8$ methods, suggesting that within current state-of-the-art methods -- where TTC and Comfort approach saturation -- these two sub-metrics add little marginal information for closed-loop ranking. Additionally, we identify the snowball effect -- where small open-loop deviations compound into closed-loop failures -- as a candidate mechanism for the residual gap.
