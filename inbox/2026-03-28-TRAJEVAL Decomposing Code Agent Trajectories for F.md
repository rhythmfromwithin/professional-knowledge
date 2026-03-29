---
interest: medium
link: https://arxiv.org/abs/2603.24631
next_step: skim
priority: low
slack_ts: '1774754614.576429'
source: cs.SE - Software Engineering
status: unread
title: 'TRAJEVAL: Decomposing Code Agent Trajectories for Fine-Grained Diagnosis'
---
# TRAJEVAL: Decomposing Code Agent Trajectories for Fine-Grained Diagnosis
> 原文: [https://arxiv.org/abs/2603.24631](https://arxiv.org/abs/2603.24631)

arXiv:2603.24631v1 Announce Type: new
Abstract: Code agents can autonomously resolve GitHub issues, yet when they fail, current evaluation provides no visibility into where or why. Metrics such as Pass@1 collapse an entire execution into a single binary outcome, making it difficult to identify where and why the agent went wrong. To address this limitation, we introduce TRAJEVAL, a diagnostic framework that decomposes agent trajectories into three interpretable stages: search (file localization), read (function comprehension), and edit (modification targeting). For each stage, we compute precision and recall by comparing against reference patches. Analyzing 16,758 trajectories across three agent architectures and seven models, we find universal inefficiencies (all agents examine approximately 22x more functions than necessary) yet distinct failure modes: GPT-5 locates relevant code but targets edits incorrectly, while Qwen-32B fails at file discovery entirely. We validate that these diagnostics are predictive, achieving model-level Pass@1 prediction within 0.87-2.1% MAE, and actionable: real-time feedback based on trajectory signals improves two state-of-the-art models by 2.2-4.6 percentage points while reducing costs by 20-31%. These results demonstrate that our framework not only provides a more fine-grained analysis of agent behavior, but also translates diagnostic signals into tangible performance gains. More broadly, TRAJEVAL transforms agent evaluation beyond outcome-based benchmarking toward mechanism-driven diagnosis of agent success and failure.
