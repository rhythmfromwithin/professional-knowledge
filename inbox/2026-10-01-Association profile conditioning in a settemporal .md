---
title: "Association profile conditioning in a set-temporal transformer for cross-session intracortical motor decoding"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2609.39080
priority: low
status: unread
interest: medium
next_step: skim
---
# Association profile conditioning in a set-temporal transformer for cross-session intracortical motor decoding
> 原文: [https://arxiv.org/abs/2609.39080](https://arxiv.org/abs/2609.39080)

arXiv:2609.39080v1 Announce Type: new
Abstract: Intracortical motor decoders degrade across sessions because the set of recorded units changes and persisting units can alter how their firing relates to behavior. Most existing methods update network weights on each new session or rely on unlabeled activity, which does not directly reveal such changes. We present APST, an Association Profile-conditioned Set-Temporal transformer that adapts to new sessions with all network weights frozen. From a few labeled calibration trials, APST summarizes how each unit's firing relates to behavior in a four-dimensional association profile computed in closed form. The profiles condition a set-attention encoder that accepts any number and order of units, followed by a causal transformer for streaming decoding. On held-out DANDI688 sessions from two monkeys, APST reaches velocity $R^2$ of $0.78$ and $0.81$, versus $0.40$ and $0.58$ for a variant that uses neural activity alone, and matches or exceeds an RNN fine-tuned on the same trials. On FALCON private held-out evaluation, it attains $R^2$ of $0.65$, $0.42$, and $0.44$ on M1, M2, and H1.
