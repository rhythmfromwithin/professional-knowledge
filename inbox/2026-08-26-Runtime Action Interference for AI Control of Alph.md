---
interest: medium
link: https://arxiv.org/abs/2608.21398
next_step: skim
priority: high
slack_ts: '1787708817.738969'
source: cs.LG - Machine Learning
status: unread
title: Runtime Action Interference for AI Control of AlphaStar in StarCraft II
---
# Runtime Action Interference for AI Control of AlphaStar in StarCraft II
> 原文: [https://arxiv.org/abs/2608.21398](https://arxiv.org/abs/2608.21398)

arXiv:2608.21398v1 Announce Type: new
Abstract: A trained reinforcement learning policy does not determine the complete behavior that users encounter: deployment code still schedules, admits, suppresses, or replaces its proposed actions. We contribute \emph{runtime action interference} (RAI), an AI control mechanism that preserves policy parameters while regulating action pacing and filtering configured action patterns after inference. RAI releases a proposed action only when its cooldown condition is satisfied and its content detector does not flag the action; otherwise, it dispatches a no-op. The detector covers specified toxic behaviors, including worker-unit harassment, while the cooldown controls action rate. We implement RAI in a replication of AlphaStar actor.py and make the implementation and reproducibility materials available through an open source code repository. We deployed RAI in a \textit{StarCraft~II} human participant study that compared two presentations of the same opponent with high capability and rate limited actions; we withheld its capability claim in one presentation and disclosed it in the other. On response scales from 1 to 5, we observed pooled fairness, trust, and toxicity means of 3.90, 3.50, and 2.00 under claim withholding, compared with 2.62, 4.31, and 2.85 under disclosure. Disclosure corresponded with lower perceived fairness and higher perceived toxicity across every expertise group, whereas trust increased among novices and experts but decreased among intermediate participants. Our human evaluation therefore shows that perceptions of an opponent controlled through RAI can vary substantially with the capability information presented to users, even when the configured control remains constant. We conclude that human-computer evaluations must separate control within the execution stack from capability disclosure and assess fairness, trust, and toxicity as distinct dimensions of human experience.
