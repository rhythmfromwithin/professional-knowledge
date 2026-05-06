---
title: "LLM-based uncertainty assessment of social media situational signals for crisis reporting"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2605.00829
priority: medium
status: unread
interest: medium
next_step: skim
---
# LLM-based uncertainty assessment of social media situational signals for crisis reporting
> 原文: [https://arxiv.org/abs/2605.00829](https://arxiv.org/abs/2605.00829)

arXiv:2605.00829v1 Announce Type: new
Abstract: Social media has become a critical source of situational awareness during disasters, providing real-time insights into evolving impacts and emerging needs. To support crisis response at scale, recent work has increasingly leveraged large language models (LLMs) to automatically classify and summarize situational information from social media streams. However, existing approaches implicitly assume that extracted situational claims are equally plausible, despite information quality varying substantially as a crisis unfolds. In this work, we propose an uncertainty-aware framework for automated situational awareness reporting that explicitly accounts for the plausibility of social media claims. First, we classify social media posts according to an established situational awareness schema. Second, we introduce an uncertainty assessment layer that evaluates whether individual situational claims plausibly reflect real-world conditions when conditioned on external proxy data, while explicitly eliciting the model's confidence in this judgment. Third, we use these uncertainty assessments to generate crisis reports that communicate not only what is being reported, but how certain those reports are. We apply this framework to over 200,000 earthquake-related Twitter/X posts, using impact summaries from the USGS PAGER as a representative external proxy. We argue that explicitly representing uncertainty supports human crisis communicators in prioritizing information under time pressure, and provides a framework for integrating external proxy data into LLM-based situational awareness pipelines.
