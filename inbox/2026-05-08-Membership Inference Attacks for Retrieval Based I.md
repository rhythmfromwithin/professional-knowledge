---
interest: medium
link: https://arxiv.org/abs/2605.04116
next_step: skim
priority: low
slack_ts: '1778385535.087819'
source: cs.CR - Cryptography and Security
status: unread
title: Membership Inference Attacks for Retrieval Based In-Context Learning for Document
  Question Answering
---
# Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering
> 原文: [https://arxiv.org/abs/2605.04116](https://arxiv.org/abs/2605.04116)

arXiv:2605.04116v1 Announce Type: new
Abstract: We show that remotely hosted applications employing in-context learning when augmented with a retrieval function to select in-context examples can be vulnerable to membership-inference attacks even when the service provider and users are separate parties. We propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs. The first attack uses a reference model to estimate an otherwise unavailable loss metric. The second attack improves upon it by eliminating the reference model and instead computing a membership statistic through a simple but novel weighted-averaging scheme. Our comprehensive empirical evaluations consider a stricter case in which the adversary has a paraphrased version of the text in the queries and show that our attacks can exhibit stronger resilience to paraphrasing and outperform three prior attacks in many cases with small number of prefixes. We also adapt an existing ensemble prompting defense to our setting, demonstrating that it substantially mitigates the privacy leakage caused by our second attack.
