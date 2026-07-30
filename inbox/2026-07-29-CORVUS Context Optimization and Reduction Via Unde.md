---
interest: medium
link: https://arxiv.org/abs/2607.22711
next_step: skim
priority: high
slack_ts: '1785380033.140759'
source: cs.LG - Machine Learning
status: unread
title: 'CORVUS: Context Optimization and Reduction Via Underlying Synchronization
  for LLM Coding Agents'
---
# CORVUS: Context Optimization and Reduction Via Underlying Synchronization for LLM Coding Agents
> 原文: [https://arxiv.org/abs/2607.22711](https://arxiv.org/abs/2607.22711)

arXiv:2607.22711v1 Announce Type: new
Abstract: LLM coding agents operate by constructing trajectories that accumulate reasoning, tool calls, and results to enable multi-step decision-making. However, the conventional append-only trajectory architecture found in practice tightly couples file-read actions with their observations, capturing snapshots that become permanently fixed in the chronological history. As files change through agent edits or concurrent human modifications, these snapshots become stale, causing reasoning errors and causing agents to redundantly re-read files, with each re-read appending yet another copy to the trajectory. To mitigate this, we propose CORVUS, a novel trajectory architecture that decouples file-read actions from their observations by maintaining a synchronized registry of relevant files and injecting only their current contents at each reasoning cycle. This structural change produces significantly lighter-weight trajectories that remain synchronized with the actual codebase state by construction, eliminating redundant file copies and stale snapshots that bloat conventional trajectories. We evaluated CORVUS on SWE- POLYBENCH\_VERIFIED and SWE-BENCH PRO across four LLMs, achieving 9-50% reduction in average input tokens per task, 15-32% shorter final prompts, and up to 37% fewer reasoning cycles while maintaining comparable pass rates.
