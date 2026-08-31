---
interest: medium
link: https://arxiv.org/abs/2608.27504
next_step: skim
priority: low
slack_ts: '1788152843.346929'
source: cs.CR - Cryptography and Security
status: unread
title: 'Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability
  Study'
---
# Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study
> 原文: [https://arxiv.org/abs/2608.27504](https://arxiv.org/abs/2608.27504)

arXiv:2608.27504v1 Announce Type: new
Abstract: Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by which LLMs process adversarial prompts remain poorly understood. We present a mechanistic analysis of the jailbreaking behavior in a large-scale, safety-aligned LLM, focusing on LLaMA-2-7B-chat-hf. Leveraging edge attribution patching and subnetwork probing, we systematically identify computational circuits responsible for generating affirmative responses to jailbreak prompts. Ablating these circuits during the first token prediction can reduce attack success rates by up to 80\%, demonstrating its critical role in safety bypass. Our analysis uncovers key attention heads and MLP pathways that mediate adversarial prompt exploitation, revealing how important tokens propagate through these components to override safety constraints. These findings advance the understanding of adversarial vulnerabilities in aligned LLMs and pave the way for targeted, interpretable defense mechanisms based on mechanistic interpretability.
