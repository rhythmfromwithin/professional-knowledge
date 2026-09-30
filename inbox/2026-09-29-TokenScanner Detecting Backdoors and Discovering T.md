---
interest: medium
link: https://arxiv.org/abs/2609.31878
next_step: skim
priority: low
slack_ts: '1790745137.060179'
source: cs.CR - Cryptography and Security
status: unread
title: 'TokenScanner: Detecting Backdoors and Discovering Triggers in Text-to-Image
  LoRAs via Full Vocabulary Scanning'
---
# TokenScanner: Detecting Backdoors and Discovering Triggers in Text-to-Image LoRAs via Full Vocabulary Scanning
> 原文: [https://arxiv.org/abs/2609.31878](https://arxiv.org/abs/2609.31878)

arXiv:2609.31878v1 Announce Type: new
Abstract: LoRAs are widely studied for adapting base text-to-image diffusion models. However, a backdoored LoRA can hide a backdoor: it behaves normally in most cases, but produces attacker-specified content (the backdoor target) when a hidden backdoor trigger appears in the input prompt. Detecting such backdoors before using an untrusted LoRA is important for the safety of LoRA adaptation. We present TokenScanner, a model-level vocabulary scanner for backdoor detection within a LoRA fine-tuned text-to-image diffusion model, aiming to discover the malicious trigger for trustworthy LoRA adaptation. The key observation is that backdoor trigger tokens that appear in a larger proportion of training prompts tend to induce more prominent token-specific LoRA responses than those induced by unrelated tokens. TokenScanner therefore scans the tokenizer vocabulary and measures token-wise LoRA responses in the U-Net and the text encoder. It uses these responses to detect backdoored LoRAs and rank candidate trigger tokens for subsequent testing of backdoor activation. Experiments on seven backdoor settings, comprising 840 backdoored LoRAs and 840 real-world benign test LoRAs, show that TokenScanner achieves 95.96% AUC and 96.55% TPR at an FPR of 10.95%. It also achieves 89.40% Hit@1 and 99.40% Hit@5 for trigger discovery across all seven settings.
