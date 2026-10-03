---
interest: medium
link: https://arxiv.org/abs/2609.38216
next_step: skim
priority: medium
slack_ts: '1791003461.466599'
source: cs.RO - Robotics
status: unread
title: 'Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb
  Replacement'
---
# Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement
> 原文: [https://arxiv.org/abs/2609.38216](https://arxiv.org/abs/2609.38216)

arXiv:2609.38216v1 Announce Type: new
Abstract: Existing benchmarks evaluate tabletop manipulation, flat-floor household activity, or humanoid locomotion and manipulation as separate task groups; none scores vertical mobility and dexterous work on a fragile payload in one long-horizon episode. We present Fiatlux, a light-bulb replacement benchmark built on NVIDIA Isaac Lab. In one episode, a Unitree G1 humanoid positions a step ladder under a ceiling or wall fixture, climbs it, exchanges a spent bulb in a socket for a fresh one, and leaves the spent one in a disposal crate. We decompose the episode into twelve subtask environments scored on difficulty-weighted gates. The goal is a successful replacement, with the fresh bulb seated, the spent one disposed of, neither dropped, and a fragility bound not crossed. Runs that fall short can earn partial credit. Observations are split into a standard mode (signals a physical robot could sense or estimate) and a privileged mode (exact simulator state). We specify the evaluation protocol and provide reference baseline implementations spanning RSL-RL PPO, zero-shot NVIDIA GR00T N1.7 Vision-Language-Action (VLA) models, and whole-body controllers. Additionally, we provide the teleoperated recordings used to specify and check the success gates. The benchmark code and the teleoperated recordings are available at fiatlux-bench.github.io.
