---
interest: medium
link: https://arxiv.org/abs/2605.16517
next_step: skim
priority: low
slack_ts: '1779164085.721449'
source: cs.SE - Software Engineering
status: unread
title: Customizing an LLM for Enterprise Software Engineering
---
# Customizing an LLM for Enterprise Software Engineering
> 原文: [https://arxiv.org/abs/2605.16517](https://arxiv.org/abs/2605.16517)

arXiv:2605.16517v1 Announce Type: new
Abstract: Enterprise software development is a continuous evolutionary process, characterized by incremental additions, architectural revisions, production deployments and rigorous maintenance. These activities generate valuable data that modern LLMs could be finetuned on, to unlock additional tool possibilities for enterprise software engineering. While frontier LLMs are already very capable, this form of customization offers a compelling path for enterprise-specific optimization.
We introduce Gemini for Google (GfG)}, an adaptation of Gemini specialized for Google's internal software engineering ecosystem. This paper details the model's end-to-end development, from curating a trillion-token proprietary dataset to implementing a mid-training strategy that mitigates catastrophic forgetting. In a large-scale blind A/B study across 29,000 developers, Gemini for Google significantly outperformed baselines: reducing the mean number of iterations per turn by 23\%, and increasing code survival rates by about 17%. Beyond metrics, we provide a comprehensive blueprint for enterprise model adaptation, covering: (1)The extraction of high-value signals from software engineering data, (2)Data preparation strategies, (3)Full-stack model tuning (continued pre-training and post-training), and (4)The deployment of downstream applications. We believe this methodology offers a replicable path for other organizations to unlock the full potential of their internal engineering data.
