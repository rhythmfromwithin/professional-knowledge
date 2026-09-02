---
interest: medium
link: https://arxiv.org/abs/2608.28656
next_step: skim
priority: medium
slack_ts: '1788321939.541339'
source: cs.RO - Robotics
status: unread
title: 'RedLight-VLA: Models for traffic-rule grounding and behavioral emphasis in
  driving policies'
---
# RedLight-VLA: Models for traffic-rule grounding and behavioral emphasis in driving policies
> 原文: [https://arxiv.org/abs/2608.28656](https://arxiv.org/abs/2608.28656)

arXiv:2608.28656v1 Announce Type: new
Abstract: Behavior-cloned Vision-Language-Action (VLA) driving policies struggle with rare rule-governed maneuvers at signalized intersections. Braking and launching examples contribute little to averaged trajectory loss, while fused representations lack explicit supervision for the governing traffic-light and stop-line state. We present RedLight-VLA, a training objective that uses expert futures and automatically generated perception targets without additional manual rule annotation. First, trajectory-derived behavioral reweighting (BR) emphasizes rare deceleration and acceleration using rotation-invariant longitudinal dynamics and a scale-preserving reduction that exactly recovers the baseline when disabled. Second, parallel auxiliary (AUX) heads ground traffic-light and stop-line state in continuous post-fusion rule tokens, without autoregressive language generation or changes to the trajectory decoder. We evaluate on a curated set of 20 s sequences with a 5 s prediction horizon. Controlled variants share the same backbone, training data, decoder, and evaluation population. Against an otherwise identical VLA baseline, RedLight-VLA reduces red-light stop-line overshoot from 7.3% to6.8%, reduces stop-line velocity error by 12.7%, and improves 3 s trafficlight-sliced ADE/FDE from 0.274/0.964 m to 0.247/0.897 m. Green-light false stops increase from 3.2% to 3.9%; however, combining BR with AUX supervision mitigates the larger increase observed for AUX alone (4.0%). The combined model also improves non-traffic-light ADE/FDE from 0.268/0.956 m to 0.241/0.876 m and outperforms either mechanism alone on all four sliced displacement measures.
