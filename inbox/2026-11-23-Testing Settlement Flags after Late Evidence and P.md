---
title: "Testing Settlement Flags after Late Evidence and Process Restart"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2611.26665
priority: low
status: unread
interest: medium
next_step: skim
---
# Testing Settlement Flags after Late Evidence and Process Restart
> 原文: [https://arxiv.org/abs/2611.26665](https://arxiv.org/abs/2611.26665)

arXiv:2611.26665v1 Announce Type: new
Abstract: A settlement flag can survive an application restart while the economic effects remain ambiguous. We define a contract linking the fixed plan, source admission at two cutoffs, identity-keyed ledger effects and post-invocation state. We generated 504 synthetic histories, ran each through a file implementation and a separately coded SQLite implementation, and observed 672 controlled process exits. The file implementation missed 54 same-identity payment-date conflicts, including 27 that credited cash early, and a monitor using run flags, artifact presence and purchase counts accepted all 54. The same contract distinguishes a purchase awaiting closure from a correct quote wait for a single writer on a running kernel and filesystem.
