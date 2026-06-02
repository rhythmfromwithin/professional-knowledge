---
title: "An Empirical Study on Logging Evolution On Stack Overflow: Trends, Topics, and Challenges"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2606.00118
priority: low
status: unread
interest: medium
next_step: skim
---
# An Empirical Study on Logging Evolution On Stack Overflow: Trends, Topics, and Challenges
> 原文: [https://arxiv.org/abs/2606.00118](https://arxiv.org/abs/2606.00118)

arXiv:2606.00118v1 Announce Type: new
Abstract: Context: Logging is a crucial practice in software engineering, aiding developers in debugging applications when errors occur. While existing research has explored logging challenges from an academic perspective through literature reviews and source code analysis, a comprehensive study from the practitioners' perspective remains lacking.
Objective: This paper aims to bridge this knowledge gap by presenting an in-depth analysis of trends, topics, and challenges in logging based on a dataset of 216,094 posts from Stack Overflow (SO), a popular Q\&A platform for developers.
Method: We analyzed longitudinal trends by examining metadata related to users, questions, and tags associated with logging discussions. To identify prevalent discussion topics, we employed a Large Language Model (LLM)--based classification approach, based on a manually validated ground-truth sample. Topic popularity was assessed through average scores and views, while difficulty was measured using three community-driven metrics: the proportion of questions without accepted answers, the proportion of unanswered questions, and the median time to receive an accepted answer.
Results: Our analysis identifies 11 distinct topics, with the top three (General Logging Practices, Error Handling and Debugging, and Logging Levels and Output) accounting for over 70\% of all logging-related discussions. Notably, Logging in Containerized Environments emerged as the most difficult topic: 64.9\% of its questions lack an accepted answer, and its median resolution time is among the highest. These findings highlight enduring practitioner struggles with logging in Docker or other containerized environments and the integration of logging pipelines into orchestrators such as Kubernetes and cloud environments.
Conclusion: This study sheds light on the practical challenges of logging and provides actionable insights for developers, framework vendors, researchers, and educators.
