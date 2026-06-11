---
interest: medium
link: https://arxiv.org/abs/2606.11476
next_step: skim
priority: low
slack_ts: '1781153122.397259'
source: cs.SE - Software Engineering
status: unread
title: 'SentTrack: Sentiment-Driven Bottleneck Detection in GitHub Issue Repositories'
---
# SentTrack: Sentiment-Driven Bottleneck Detection in GitHub Issue Repositories
> 原文: [https://arxiv.org/abs/2606.11476](https://arxiv.org/abs/2606.11476)

arXiv:2606.11476v1 Announce Type: new
Abstract: Software engineering teams increasingly depend on GitHub issue threads to coordinate work, report bugs, and negotiate technical decisions, yet most repository health tools focus on code metrics and ignore the conversational dynamics that drive or stall development. This paper presents SentTrack, a dual-lens framework for detecting socio-technical bottlenecks from GitHub issue discussions. Applied to the AvaloniaUI open-source repository across approximately 9,000 issue threads, the framework addresses three questions: how to automate workflow-inefficiency detection from real-time conversational data, whether sentiment signals can surface risk earlier than traditional label-based methods, and how to isolate human narrative from machine-generated noise in mixed-media issue text. SentTrack combines two complementary pipelines. A horizontal pipeline translates raw issue reports into clean summaries using a large language model, extracts mid-level concern phrases, and clusters them through UMAP and HDBSCAN, producing 613 semantic clusters from the first 3,608 issues processed. A vertical pipeline applies the ABCDE collaborative interaction framework to classify each comment and infer thread-level outcomes. Across the full corpus, 49\% of threads ended in stagnation and only 13\% reached resolution, with the resolution gap identified as the dominant bottleneck signal. A weighted scoring engine that combines negativity, stagnation, resolution gap, and thread length gives maintainers an interpretable prioritization tool for high-friction discussions before they stall development.
