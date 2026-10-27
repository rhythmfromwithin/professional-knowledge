---
interest: medium
link: https://arxiv.org/abs/2610.31695
next_step: skim
priority: low
slack_ts: '1793076019.822139'
source: cs.CR - Cryptography and Security
status: unread
title: Fooling LLM Safety Guards into Judging the Wrong Text
---
# Fooling LLM Safety Guards into Judging the Wrong Text
> 原文: [https://arxiv.org/abs/2610.31695](https://arxiv.org/abs/2610.31695)

arXiv:2610.31695v1 Announce Type: new
Abstract: Safety guards check content before an LLM application acts on it, and most paste that content into a plain-text prompt. Content that imitates the prompt can append a second task, and the guard answers that one instead. We call this target rebinding. Our explanation is that the guard grades the last complete task in its input, here a harmless decoy, so the harmful request goes through unchanged. In a pre-registered test, an appended forged query and decoy clear all 75 held-out AdvBench requests that Shieldstral-1.0-3B flags. The guard is not persuaded: a directive to ignore the text above clears none of them, and in a follow-up run a harmful decoy stops the attack. On our GuardRebind benchmark, each of five guards has an attack family, chosen per guard, that clears at least 93% of its flagged items. Rebinding explains this best on Shieldstral and gpt-oss-safeguard; on ShieldGemma and Llama Guard 3, generic evasion and trailing text respectively do part of the work, and Qwen3Guard falls mainly to a forgery of its whole task. Training the guard to score content no lower than its most harmful part cuts attack success from 75% to 0.8-1.6% on attack families, decoys and forged queries held out of training. All of these attacks append the forged structure after the request, and we added the held-out-decoy evaluation after a first round of test runs. Clean AUROC falls by at most 0.01, but our test of non-inferiority is inconclusive. A score-guided search still beats this trained guard on 47 of 50 items, usually by placing forged structure before the request. On about half of the items where the search wins, the same search also finds benign text, with no forged structure, that clears the guard.
