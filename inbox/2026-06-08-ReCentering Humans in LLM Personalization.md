---
interest: medium
link: https://arxiv.org/abs/2606.06614
next_step: skim
priority: high
slack_ts: '1780894169.645799'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Re-Centering Humans in LLM Personalization
---
# Re-Centering Humans in LLM Personalization
> 原文: [https://arxiv.org/abs/2606.06614](https://arxiv.org/abs/2606.06614)

arXiv:2606.06614v1 Announce Type: new
Abstract: Despite growing interest, most evaluations of large language models' (LLMs') personalization abilities have relied on synthetic data. It remains unclear how well current personalization systems work for real users. In this paper, we study the gap in LLM personalization performance when using synthetic versus human data. We collect human conversations (550 conversations) and judgments across three stages of personalization: extracting user attributes from conversations (5,949 judgments), pairing relevant attributes with new prompts (11,919), and incorporating relevant attributes into a personalized response (1,101). Incorporating human data reveals system limitations at each stage. Models struggle to extract attributes from human conversations, disagree with human judgments on relevant attributes, and generate personalized responses that humans judge no better than generic responses (though that LLM judges widely rate as better). We introduce two lightweight training-based interventions that shift automated personalization evaluation closer to human data in our first two stages. However, in our third stage we find that learned reward models achieve only modest correlation with human ratings, suggesting that human-aligned personalization quality judgments are difficult to model directly. Our collected data provides a foundation for studying how models should extract, select, and incorporate user information in ways that humans find useful.
