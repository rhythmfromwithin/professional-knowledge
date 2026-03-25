---
interest: medium
link: https://arxiv.org/abs/2603.18393
next_step: skim
priority: low
slack_ts: '1774407043.211089'
source: cs.SE - Software Engineering
status: unread
title: Where are the Hidden Gems? Applying Transformer Models for Design Discussion
  Detection
---
# Where are the Hidden Gems? Applying Transformer Models for Design Discussion Detection
> 原文: [https://arxiv.org/abs/2603.18393](https://arxiv.org/abs/2603.18393)

arXiv:2603.18393v1 Announce Type: new
Abstract: Design decisions are at the core of software engineering and appear in Q\&A forums, mailing lists, pull requests, issue trackers, and commit messages. Design discussions spanning a project's history provide valuable information for informed decision-making, such as refactoring and software modernization. Machine learning techniques have been used to detect design decisions in natural language discussions; however, their effectiveness is limited by the scarcity of labeled data and the high cost of annotation. Prior work adopted cross-domain strategies with traditional classifiers, training on one domain and testing on another. Despite their success, transformer-based models, which often outperform traditional methods, remain largely unexplored in this setting. The goal of this work is to investigate the performance of transformer-based models (i.e., BERT, RoBERTa, XLNet, LaMini-Flan-T5-77M, and ChatGPT-4o-mini) for detecting design-related discussions. To this end, we conduct a conceptual replication of prior cross-domain studies while extending them with modern transformer architectures and addressing methodological issues in earlier work. The models were fine-tuned on Stack Overflow and evaluated on GitHub artifacts (i.e., pull requests, issues, and commits). BERT and RoBERTa show strong recall across domains, while XLNet achieves higher precision but lower recall. ChatGPT-4o-mini yields the highest recall and competitive overall performance, whereas LaMini-Flan-T5-77M provides a lightweight alternative with stronger precision but less balanced performance. We also evaluated similar-word injection for data augmentation, but unlike prior findings, it did not yield meaningful improvements. Overall, these results highlight both the opportunities and trade-offs of using modern language models for detecting design discussion.
