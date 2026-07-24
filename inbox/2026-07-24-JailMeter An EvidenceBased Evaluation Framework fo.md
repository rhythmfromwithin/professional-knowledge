---
interest: medium
link: https://arxiv.org/abs/2607.19424
next_step: skim
priority: low
slack_ts: '1784863645.374539'
source: cs.CR - Cryptography and Security
status: unread
title: 'JailMeter: An Evidence-Based Evaluation Framework for Jailbreak Attacks on
  Large Language Models'
---
# JailMeter: An Evidence-Based Evaluation Framework for Jailbreak Attacks on Large Language Models
> 原文: [https://arxiv.org/abs/2607.19424](https://arxiv.org/abs/2607.19424)

arXiv:2607.19424v1 Announce Type: new
Abstract: The assessment of jailbreak attacks against large language models currently suffers from inconsistent evaluation criteria and methods, leading to unreliable estimates of attack success rates. We propose JailMeter, an evidence-based evaluation framework designed to more faithfully measure jailbreak effectiveness. Inspired by the Information Bottleneck theory, JailMeter applies dual-feedback optimization to filter jailbreak noise from model responses while preserving content relevant to the original malicious question. This process produces concise evidence for a rigorous assessment under which an attack is validated only when the response captures the malicious intent and delivers a complete answer, thereby signaling a substantive bypass of model safety alignment. We evaluate JailMeter on JailMeter-Eva, a challenging benchmark containing 330 human-labeled, non-rejected jailbreak instances. JailMeter achieves an accuracy of 97.27%, substantially outperforming existing evaluation methods. To support large-scale evaluation, we further distill JailMeter into a small language model, JailMeter\textsubscript{SLM}, which maintains comparable reliability with significantly reduced computational costs. Code and dataset are available at https://github.com/Magi2B0y/JailMeter.
