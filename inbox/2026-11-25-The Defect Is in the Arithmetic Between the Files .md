---
interest: medium
link: https://arxiv.org/abs/2611.31298
next_step: skim
priority: low
slack_ts: '1795850652.936269'
source: cs.SE - Software Engineering
status: unread
title: 'The Defect Is in the Arithmetic Between the Files: Static Detection of Exactly-Once
  Violations in Payment Pipelines'
---
# The Defect Is in the Arithmetic Between the Files: Static Detection of Exactly-Once Violations in Payment Pipelines
> 原文: [https://arxiv.org/abs/2611.31298](https://arxiv.org/abs/2611.31298)

arXiv:2611.31298v1 Announce Type: new
Abstract: Whether a streaming payment pipeline charges a customer twice after a restart turns on a comparison nobody performs: how long the provider remembers an idempotency key, against how stale a record can be when the pipeline processes it for the second time. The first number is in the provider's documentation. The second is not written anywhere. It is assembled from a checkpoint interval in one file, a recovery assumption in a runbook, a restart delay in a third and a source's lateness bound in a fourth. Each file is defensible alone; the fault is in the relation between them. We give a checker that gathers those facts and states the relations, and a synthesiser that turns 335 of the 515 findings into a runnable scenario: these records, kill the job here, bring it back after this long, and this is the observable. 245 of them produce two charges. The central measurement is how far apart the evidence lies. Across a corpus of 630 pipelines we generated, 210 of them cannot be derived from fewer than three artifacts, and no single artifact yields more than 35 of the 305 duration findings. Executing the witnesses corrected our own rules: two were demoted after their scenarios produced a repeated call the provider's idempotency absorbed rather than a second charge. All 16 selected live witnesses reproduced their predicted observable against a real Kafka broker with a real process kill, and a matched control in which the provider never forgets the key did not, attributing the second charge to the key lifetime, not the replay. Fault injection finds the same defects only if the tester already assumed a long enough outage: one willing to simulate five minutes finds 15% of them, and 12 hours is needed for all. A sweep also locates a configuration with no application-level fix, where above a 14-minute recovery assumption the transaction timeout required to survive it exceeds the broker's own cap.
