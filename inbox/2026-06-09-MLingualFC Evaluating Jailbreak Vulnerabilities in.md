---
interest: medium
link: https://arxiv.org/abs/2606.07706
next_step: skim
priority: low
slack_ts: '1780978311.394469'
source: cs.CR - Cryptography and Security
status: unread
title: 'MLingualFC: Evaluating Jailbreak Vulnerabilities in Multilingual Vision-Language
  Models'
---
# MLingualFC: Evaluating Jailbreak Vulnerabilities in Multilingual Vision-Language Models
> 原文: [https://arxiv.org/abs/2606.07706](https://arxiv.org/abs/2606.07706)

arXiv:2606.07706v1 Announce Type: new
Abstract: Vision-Language Models (VLMs) have demonstrated strong performance across multimodal tasks, yet their safety robustness remains an open challenge. While prior work has shown that structured visual prompts such as flowcharts can effectively jailbreak VLMs, existing studies are largely limited to English-centric settings. In this paper, we introduce MLingualFC, a multilingual multimodal benchmark designed to evaluate jailbreak vulnerabilities of VLMs across diverse languages using structured flowchart representations. MLingualFC encodes harmful instructions into flowchart images across five languages (Hindi, Punjabi, Spanish, Romanian, and German). We evaluate state-of-the-art multilingual VLMs, including Qwen2.5-VL, Gemma-4, and Pangea, under a black-box threat model. Our results reveal significant multilingual safety gaps. Flowchart-based attacks achieve high attack success rates (ASR) in case of Latin script languages, demonstrating that visual encoding of harmful content effectively bypasses safety alignment across languages. In contrast, non-Latin script languages such as Punjabi exhibit substantially lower ASR, suggesting potential limitations in visual text recognition rather than stronger safety alignment. These findings highlight that current VLM safety mechanisms fail to generalize across languages and modalities. Resources are available at https://github.com/Rishabhpm23/MLingualFC
