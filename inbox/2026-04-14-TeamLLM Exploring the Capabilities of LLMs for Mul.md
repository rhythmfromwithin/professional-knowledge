---
interest: medium
link: https://arxiv.org/abs/2604.08771
next_step: skim
priority: low
slack_ts: '1776223654.230689'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'TeamLLM: Exploring the Capabilities of LLMs for Multimodal Group Interaction
  Prediction'
---
# TeamLLM: Exploring the Capabilities of LLMs for Multimodal Group Interaction Prediction
> 原文: [https://arxiv.org/abs/2604.08771](https://arxiv.org/abs/2604.08771)

arXiv:2604.08771v1 Announce Type: new
Abstract: Predicting group behavior, how individuals coordinate, communicate, and interact during collaborative tasks, is essential for designing systems that can support team performance through real-time prediction and realistic simulation of collaborative scenarios. Large Language Models (LLMs) have shown promise for processing sensor data for human-activity recognition (HAR), yet their capabilities for team dynamics or group-level multimodal sensing remain unexplored. This paper investigates whether LLMs can predict group coordination patterns from multimodal sensor data in collaborative Mixed Reality (MR) environments. We encode hierarchical context -- individual behavioral profiles, group structural properties, and temporal activity context -- as natural language and evaluate three LLM adaptation paradigms (zero-shot, few-shot, and supervised fine-tuning) against statistical baselines. Our evaluation on 16 groups (64 participants, $\sim$25 hours of sensor data) reveals that LLMs achieve 3.2$\times$ improvement over LSTM baselines for linguistically-grounded behaviors, with fine-tuning reaching 96\% accuracy for conversation prediction while maintaining sub-35ms latency. Beyond performance gains, we characterize the boundaries of text-based LLMs for multimodal sensing conversation prediction succeeds because turn-taking maps to linguistic patterns, while shared or joint attention may require spatial and visual reasoning that text only LLMs cannot capture. We further identify simulation mode brittleness (83\% degradation from cascading context errors) and minimal few-shot sensitivity to example selection strategy. These findings establish guidelines when LLMs are appropriate for CPS/IoT sensing for team dynamics and inform the design of future multimodal foundation models.
