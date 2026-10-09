---
interest: medium
link: https://arxiv.org/abs/2610.06939
next_step: skim
priority: medium
slack_ts: '1791524738.425759'
source: cs.DC - Distributed Computing
status: unread
title: 'When Robots Crash: Optimal Asynchronous Gathering at Weber Meeting Nodes'
---
# When Robots Crash: Optimal Asynchronous Gathering at Weber Meeting Nodes
> 原文: [https://arxiv.org/abs/2610.06939](https://arxiv.org/abs/2610.06939)

arXiv:2610.06939v1 Announce Type: new
Abstract: We study the \textit{optimal gathering} problem over a finite set of designated \textit{meeting nodes} for \textit{asynchronous, anonymous,} and \textit{oblivious} mobile robots on an infinite grid under crash faults. The robots have global visibility and strong multiplicity detection, but share neither a coordinate system nor chirality. The objective is to gather all non-faulty robots at a \textsc{Weber Meeting Node}, minimizing the total Manhattan distance from their initial positions. Up to $n-2$ robots may crash permanently, and such crashes are indistinguishable from arbitrary delays. Existing approaches often rely on a designated robot to break symmetry, whose crash may block the remaining robots indefinitely. Instead, our approach enables every robot to independently select the same target from its snapshot, while target-dependent restricted shortest paths preserve the target as a \textsc{Weber Meeting Node}. We prove that, under strong multiplicity detection, optimal gathering is impossible from certain fully symmetric configurations. For all remaining configurations, our algorithm \textsc{CrashTolerantWeberGathering()} selects a unique common target, preserves its optimality throughout the execution, and allows non-faulty robots to progress without waiting for crashed robots, thereby guaranteeing gathering in finite time.
