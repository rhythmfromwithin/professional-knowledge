---
interest: medium
link: https://arxiv.org/abs/2610.20656
next_step: skim
priority: low
slack_ts: '1792296500.568179'
source: cs.CR - Cryptography and Security
status: unread
title: 'Unmasking the Secret Code: Using Canaries to Show How Masked Context Controls
  Memorization in SFT'
---
# Unmasking the Secret Code: Using Canaries to Show How Masked Context Controls Memorization in SFT
> 原文: [https://arxiv.org/abs/2610.20656](https://arxiv.org/abs/2610.20656)

arXiv:2610.20656v1 Announce Type: new
Abstract: Canaries, or synthetic training records containing known secrets, are widely used to assess whether language models reveal information from their training data. But how much do these measurements depend on the canaries themselves? We study this question through controlled fine-tuning experiments with language and vision-language models, spanning synthetic tasks and tasks where training improves useful performance. Whether a secret is provided in the training input strongly changes what the model learns; for example, models can reproduce a secret in the input yet fail to recall it when it is removed, even after extensive repetition during training. When training instead requires predicting the secret from the surrounding context, later recall can become reliable. Repetition alone is therefore insufficient to characterize memorization. We also find that changing when a canary appears, or which other canaries accompany it, can substantially change measured memorization without increasing that canary's repetition count. These results show that canary measurements depend on how secrets are presented during training and tested afterward. Audits should test whether their conclusions hold across these choices before extending them to other training records.
