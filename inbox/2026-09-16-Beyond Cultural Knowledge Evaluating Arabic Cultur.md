---
interest: medium
link: https://arxiv.org/abs/2609.16006
next_step: skim
priority: medium
slack_ts: '1789532927.492839'
source: cs.CY - Computers and Society
status: unread
title: 'Beyond Cultural Knowledge: Evaluating Arabic Cultural Appropriateness of Large
  Language Models'
---
# Beyond Cultural Knowledge: Evaluating Arabic Cultural Appropriateness of Large Language Models
> 原文: [https://arxiv.org/abs/2609.16006](https://arxiv.org/abs/2609.16006)

arXiv:2609.16006v1 Announce Type: new
Abstract: Large language models (LLMs) increasingly serve users whose expectations are shaped by their cultural context, yet most cultural evaluations test what a model knows rather than how it behaves when giving open-ended recommendations, opinions, and guidance. We introduce AraBehave: 1,623 culturally grounded, open-ended Arabic prompts with 29,214 cultural-appropriateness judgments from native speakers across several Arab regions, plus a scoring model whose predictions correlate strongly with human judgments on unseen systems (Pearson r=0.74). Evaluating three Arabic-centric and three frontier LLMs, we find that cultural appropriateness is not a single capability but decomposes into two largely independent components: normative stance and grounded cultural accuracy. The best general-purpose and best Arabic-centric models score identically (3.84 vs. 3.83 of 5) yet almost never fail for the same reason: general-purpose models exhibit strong factual grounding but a culturally inappropriate normative stance, being penalized for secular framing and false balance on culturally settled matters (28--33% of their low-score rationales), while the best Arabic-centric model adopts the expected stance but is penalized for fabricated hadith and misquoted verses (29%). Stance is cheap and fragile: one sentence of cultural instruction lifts Gemini to 4.57, above every Arabic-specialized model. Conversely, a generic ``answer clearly and objectively'' prompt costs Allam-7B 0.68 points, while asking the same questions in English lowers scores for every model but one. Grounding instead tracks scale and Arabic alignment data, and disappears when culturally aware instruction tuning is replaced by a culture-neutral corpus. General safety benchmarks see none of this: they saturate above 89 while cultural scores span 2.71-3.84. We will release the benchmark, annotations, and the scoring model.
