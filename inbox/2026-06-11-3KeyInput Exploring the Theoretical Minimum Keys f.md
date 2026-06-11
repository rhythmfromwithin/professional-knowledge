---
interest: medium
link: https://arxiv.org/abs/2606.11642
next_step: skim
priority: low
slack_ts: '1781153108.958689'
source: cs.HC - Human-Computer Interaction
status: unread
title: '3-Key-Input: Exploring the Theoretical Minimum Keys for Text Entry'
---
# 3-Key-Input: Exploring the Theoretical Minimum Keys for Text Entry
> 原文: [https://arxiv.org/abs/2606.11642](https://arxiv.org/abs/2606.11642)

arXiv:2606.11642v1 Announce Type: new
Abstract: How far can we reduce the number of physical keys if we endow an ambiguous keyboard with modern language models? Fewer keys increase hardware design freedom in constrained settings such as assistive devices and mobile form factors. This paper systematically evaluates text entry systems using 2-5 physical keys combined with language-model-based disambiguation. On a 300-sentence English corpus (100 sentences each for Business / Conversational / Technical), we compare key counts (2-5), letter-to-key mappings (layout-based / frequency-based / intentionally worst-case), and decoders (Trie-only, GPT-2 beam search, GPT-4o selection). We find that 3 keys + GPT-4o achieves character error rate (CER) 9.46% and word error rate (WER) 12.20%, reducing CER by 59% relative to 2 keys (CER 23.3%). At 3 keys, the key-stream entropy is 1.54 bits/char; while increasing to 5 keys improves accuracy (CER 5.4%), the marginal gains diminish. Mapping choice has a small impact under standard designs ({\Delta}CER < 0.5 pp), and even an intentionally worst mapping degrades CER by only +0.5 pp, whereas Technical sentences yield roughly twice the error rate of Business. These results suggest that, in our evaluated offline setting under a strong LM prior, 3 keys are a practical minimum for general English.
