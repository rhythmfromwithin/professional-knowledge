---
title: "ToxiShield: Promoting Inclusive Developer Communication through Real-Time Toxicity Filtering"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.14408
priority: low
status: unread
interest: medium
next_step: skim
---
# ToxiShield: Promoting Inclusive Developer Communication through Real-Time Toxicity Filtering
> 原文: [https://arxiv.org/abs/2604.14408](https://arxiv.org/abs/2604.14408)

arXiv:2604.14408v1 Announce Type: new
Abstract: Toxic interactions during code reviews can undermine teamwork and hinder productivity in software engineering (SE) teams. While prior studies explore toxicity detection and empirical investigation, they lack real-time detoxification tools to support the SE community. To address this gap, we present ToxiShield, a browser extension for GitHub pull requests that is built using three modules: i) Toxicity Filter -- to identify whether a text is toxic, ii) Communication coach -- to facilitate just-in-time fine-grained toxicity categorization with explanations, and iii) The Reframer -- that generates a revised, constructive alternative of a toxic text. For each module, we trained and evaluated multiple deep learning and Large Language Models (LLMs) to identify the best choice. A BERT-based binary detection model, trained on 38,761 code review samples, achieves 98% accuracy and an F1-score of 97% and is the selected one for the Toxicity Filter module. For the Communication Coach, prompt-tuned Claude 3.5 Sonnet achieved the best performance with 39% MCC and 42% F1 in multiclass toxicity classification with detailed reasoning. For Reframer, we evaluated five LLMs using a fine-tuning strategy on a dataset of 10,120 code review comments. The fine-tuned Llama 3.2 model achieves 95.27% style transfer accuracy, 97.03% fluency, 67.07% content preservation, and an 84% J-score. We further validated ToxiShield through a human evaluation using the Technology Acceptance Model with 10 participants, confirming its perceived usefulness and ease of adoption. ToxiShield sets a benchmark for advancing constructive communication in software engineering, driving inclusivity and healthier collaboration in open-source communities.
