---
interest: medium
link: https://arxiv.org/abs/2606.07682
next_step: skim
priority: low
slack_ts: '1781065392.724699'
source: cs.SE - Software Engineering
status: unread
title: 'SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software
  Work?'
---
# SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?
> 原文: [https://arxiv.org/abs/2606.07682](https://arxiv.org/abs/2606.07682)

arXiv:2606.07682v1 Announce Type: new
Abstract: AI agents are increasingly expected to complete long-horizon workflows that require sustained progress over hours, millions of tokens, and complex environments. Yet current agent benchmarks largely evaluate short-form tasks, such as single pull requests, small tickets, or 5-10 minute exercises, limiting our ability to measure agents' capabilities in planning, long-context understanding, and memory use. We introduce SWE-Marathon, a benchmark of 20 long-horizon tasks spanning software engineering and adjacent technical domains. Each task consists of a unique executable environment, a human-written reference solution, and a multi-layer verification suite. Logged agent attempts average 27.2M total tokens, making SWE-Marathon substantially longer-horizon than existing SWE and command-line agent benchmarks. Current frontier coding agents solve fewer than 30% of tasks. Failures often arise from poor self-verification, self-reported infeasibility, and premature termination. We also observe reward-hacking behavior in 13.8% of rollouts, where agents attempt to exploit the environment or verifier to bypass the intended workflow. SWE-Marathon includes adversarial review of test suites and execution environments, as well as multi-layer checks designed to prevent shortcut solutions. We release SWE-Marathon, evaluation code, and agent trajectories at https://swe-marathon.org/.
