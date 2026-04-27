---
interest: medium
link: https://arxiv.org/abs/2604.20911
next_step: skim
priority: low
slack_ts: '1777261687.746909'
source: cs.CR - Cryptography and Security
status: unread
title: Omission Constraints Decay While Commission Constraints Persist in Long-Context
  LLM Agents
---
# Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents
> 原文: [https://arxiv.org/abs/2604.20911](https://arxiv.org/abs/2604.20911)

arXiv:2604.20911v1 Announce Type: new
Abstract: LLM agents deployed in production operate under operator-defined behavioral policies (system-prompt instructions such as prohibitions on credential disclosure, data exfiltration, and unauthorized output) that safety evaluations assume hold throughout a conversation. Prohibition-type constraints decay under context pressure while requirement-type constraints persist; we term this asymmetry Security-Recall Divergence (SRD). In a 4,416-trial three-arm causal study across 12 models and 8 providers at six conversation depths, omission compliance falls from 73% at turn 5 to 33% at turn 16 while commission compliance holds at 100% (Mistral Large 3, $p < 10^{-33}$). In the two models with token-matched padding controls, schema semantic content accounts for 62-100% of the dilution effect. Re-injecting constraints before the per-model Safe Turn Depth (STD) restores compliance without retraining. Production security policies consist of prohibitions such as never revealing credentials, never executing untrusted code, and never forwarding user data. Commission-type audit signals remain healthy while omission constraints have already failed, leaving the failure invisible to standard monitoring.
