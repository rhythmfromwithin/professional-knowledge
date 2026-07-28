---
title: "FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2607.21596
priority: high
status: unread
interest: medium
next_step: skim
---
# FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills
> 原文: [https://arxiv.org/abs/2607.21596](https://arxiv.org/abs/2607.21596)

arXiv:2607.21596v1 Announce Type: new
Abstract: Large language model agents increasingly solve complex tasks by constructing inference-time workflows that combine reasoning, tool use, and code execution. While such workflows enable flexible problem solving, the useful procedures discovered during execution are often transient: they help solve the current task but are not retained in a form that can systematically benefit future tasks. We present FlowEvo, a training-free framework that compiles successful traces into reusable skill records. Each record pairs a callable artifact with auxiliary structured guidance, and admission applies interface, replay, and safety checks where feasible. These skill records persist in a skill bank at inference time. FlowEvo is organized around three coupled mechanisms: (1)~workflow-to-skill compilation, which extracts reusable executable artifacts from successful traces; (2)~skill-to-workflow feedback, which retrieves accumulated skills to support future problem solving through either direct execution or structured context injection; and (3)~skill curation, which monitors downstream utility and suppresses skills that cause negative transfer. Through this workflow--skill--workflow feedback loop, FlowEvo enables agents to accumulate and refine task-solving capability over time without updating model parameters. Experiments on benchmarks spanning interactive environments (ALFWorld) and code/math generation (HumanEval, GSM8K) show that FlowEvo achieves the best accuracy-cost tradeoff among the evaluated baselines under our implementation settings. On ALFWorld, FlowEvo achieves an 82.8\% success rate, 23.6 percentage points above the strongest baseline, while its average token usage per episode is less than half that of the most efficient baseline. Controlled ablations confirm that each mechanism contributes to the overall result. The code is public at https://github.com/DEFENSE-SEU/FlowEvo.
