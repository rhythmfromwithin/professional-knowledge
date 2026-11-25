---
title: "EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.31341
priority: medium
status: unread
interest: medium
next_step: skim
---
# EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot
> 原文: [https://arxiv.org/abs/2611.31341](https://arxiv.org/abs/2611.31341)

arXiv:2611.31341v1 Announce Type: new
Abstract: Social robots face diverse and changing tasks in companionship and education. LLM-based methods can generate task programs, but they still rely on manually developed control interfaces and predefined capabilities. They also lack a general mechanism to optimize completed tasks based on user-specified metrics and reuse performance improvements across tasks.We present EvoMisty, a plugin-based framework that enables coding agents to build and continually improve robot capabilities. EvoMisty builds a control program from official documentation and verifies candidate capabilities on a physical robot. Verified capabilities are stored in an atomic capability library and combined with existing skills to solve tasks. After task completion, EvoMisty can collect execution data, measure user-specified metrics, and iteratively improve task programs. It then distills reusable skills from final solutions into a skill library for future tasks.We evaluate EvoMisty on a physical Misty II robot using Claude Code and Codex. The two agents construct 109 and 107 verified atomic capabilities, respectively. Both complete all 28 AutoMisty benchmark tasks and seven additional tasks beyond AutoMisty's capabilities. Optimization improves all seven evaluated metrics across five tasks. For example, dialogue response latency decreases by 52% and 71%, respectively. Reusing skills from one optimized dialogue task reduces latency by 33% to 72% in three other dialogue tasks without further optimization. All code and experimental videos will be publicly released through the webpage: https://wangxiaoshawn.github.io/projects/evomisty/index.html
