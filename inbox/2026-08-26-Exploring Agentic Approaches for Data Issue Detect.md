---
interest: medium
link: https://arxiv.org/abs/2608.21602
next_step: skim
priority: low
slack_ts: '1787820599.620149'
source: cs.HC - Human-Computer Interaction
status: unread
title: Exploring Agentic Approaches for Data Issue Detection and Repair in AI-Assisted
  Visualization
---
# Exploring Agentic Approaches for Data Issue Detection and Repair in AI-Assisted Visualization
> 原文: [https://arxiv.org/abs/2608.21602](https://arxiv.org/abs/2608.21602)

arXiv:2608.21602v1 Announce Type: new
Abstract: AI is increasingly lowering the barrier to data analysis and creating visualization scripts. However, a key obstacle in AI-assisted visualization is that certain data issues can lead to visualizations that are plausible, but misrepresent the underlying data. These \textit{visualization defects} are elusive and difficult to fix, particularly for non-experts who may not know what data issues cause them or how to guide AI systems to resolve them. We present findings of a preliminary empirical investigation of how commercial LLMs identify and repair defect-inducing data issues. Using a curated subset of the 911 emergency-call dataset with five injected data issues, we evaluated GPT-5, GPT-4o, GPT-4, and Claude Sonnet 4.6 under a three-stage prompting protocol, including zero-shot, guided issue-identification, and guided issue-repair. We executed this protocol under two conditions: single-agent and a multi-agent orchestration that separates data issue detection, review, repair planning, data repair, and repair quality assurance. We observed that across both conditions, LLMs identified and repaired single-field issues (e.g., missing values) but struggled to identify and repair temporal, geographic, and semantic issues. Based on these observations, we discuss design implications for agentic visualization systems, including explicit representation of data assumptions, selective human intervention for ambiguous decisions, and evidence-based repair.
