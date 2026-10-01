---
interest: medium
link: https://arxiv.org/abs/2609.38239
next_step: skim
priority: low
slack_ts: '1790832436.775069'
source: cs.CR - Cryptography and Security
status: unread
title: 'Inference-Layer Security: Defending Against Adversarial Inference and Infrastructure
  Abuse'
---
# Inference-Layer Security: Defending Against Adversarial Inference and Infrastructure Abuse
> 原文: [https://arxiv.org/abs/2609.38239](https://arxiv.org/abs/2609.38239)

arXiv:2609.38239v1 Announce Type: new
Abstract: A Technical Report: Operating a large language model (LLM) as a service requires more than inference infrastructure: the provider must also defend against adversarial interactions that seek to exploit the service, including jailbreaking for harmful use, sophisticated denial of service, and distillation attacks. We study this problem at the inference layer, using a hypothetical frontier lab, Five Elements Inc., as a running example. Because no public labelled dataset of adversarial LLM usage exists, we introduce a structural causal model (SCM) that generates a realistically grounded, labelled dataset of user-sessions, with coordinated multi-account campaigns, platform feedback, and three tiers of label observability. On this dataset we train a practical gradient-boosted detector that classifies each user-session as benign or malicious and, if malicious, by attack type. Against oracle labels the detector very nearly solves the binary task (AUPRC $0.993$), yet against the operational labels a real Trust & Safety team would hold, the same model scores an AUPRC of only $0.313$: the detector is more accurate than the labels used to evaluate it. For attack-type attribution, a naive argmax is dominated by the $98\%$ benign prior (macro-F1 $0.295$), whereas a simple thresholded decision engine raises macro-F1 to $0.489$ without sacrificing accuracy. The dataset is publicly released.
