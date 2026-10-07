---
title: "DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.06898
priority: low
status: unread
interest: medium
next_step: skim
---
# DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections
> 原文: [https://arxiv.org/abs/2610.06898](https://arxiv.org/abs/2610.06898)

arXiv:2610.06898v1 Announce Type: new
Abstract: As GUI-based mobile agents rapidly progress, rigorous safety evaluation of their autonomous decision-making in realistic app interfaces becomes increasingly critical. Existing benchmarks mainly focus on execution-level anomalies using task success or hijack rates, but fail to capture the in-task goal deviation risk in multi-candidate selection tasks, where the decision may be steered toward an attacker-specified target, even in violation of instruction-implied constraints (e.g., cheapest/highest-rated), without any overt execution anomalies. We present DIBench, a decision integrity benchmark for measuring this risk in mobile agents. DIBench covers 7 commercial and 3 simulated apps with 5 task types. Under a threat model restricted to non-privileged UI content, we construct 8 deceptive injection probe instantiations that can steer critical selections without overt anomalies. The benchmark includes 1,000 clean and 36,672 injected instances, with a unified protocol and integrity metrics for comparison. Experiments spanning 4 agent frameworks and 7 base models show that completion-based evaluation can overestimate agent trustworthiness and miss decision-integrity risks: deceptive injections steer selections and shift early action policies, inflating completion rates and creating a misleading illusion of safety. Common defenses, including detection, image preprocessing, and prompt reminders, yield inconsistent integrity gains. Overall, DIBench provides a unified, reproducible benchmark to quantify the risk of in-task goal deviation in mobile agents and enable comparable evaluations of safety defenses.
