---
interest: medium
link: https://arxiv.org/abs/2608.07541
next_step: skim
priority: medium
slack_ts: '1786501804.666329'
source: cs.CV - Computer Vision
status: unread
title: 'NeuroPilot: An Agent-Driven Smart Pipeline for Processing, Quality Control,
  and Managing Neuroimages'
---
# NeuroPilot: An Agent-Driven Smart Pipeline for Processing, Quality Control, and Managing Neuroimages
> 原文: [https://arxiv.org/abs/2608.07541](https://arxiv.org/abs/2608.07541)

arXiv:2608.07541v1 Announce Type: new
Abstract: Transforming raw neuroimage archives into analysis-ready derivatives relies on three brittle stages: data standardization, modality-specific preprocessing, and quality control (QC). While individual neuroimaging tools are well developed, their orchestration requires project-specific scripts, environment-adaptive tuning, and labor-intensive manual QC. To address this, we introduce NeuroPilot, a multi-agent system that digitalizes the expertise of neuroimage processing, QC, and data management into three LLM-invocable skills: dcm2bids-skill, neuroimage-pre-skill, and qc-agent-skill. The LLM-driven agent autonomously orchestrates workflows, generalizing various infrastructure settings into a single configuration to achieve the highest scalability. Demonstrating the system's generalizability, we deployed NeuroPilot across 17 cohorts (>123,000 subjects) spanning infant to aging populations and multiple MRI modalities (structural, diffusion, functional). In practice, after standardizing data via the dcm2bids-skill, the agent dynamically routes datasets to the optimal neuroimage-pre-skill based on available modalities and cohort traits (e.g., dispatching T1w and fMRI data to fMRIPrep, or selecting specialized pipelines for infant cohorts). The qc-agent-skill then drives an evidence-based, semi-automated QC via a 3-D browser dashboard, utilizing a multi-tiered verification system to optimize failed cases and escalate complex issues for supervisor inspection. Quantitatively, our QC agent screened 558 production subjects, validating its automated flags against FreeSurfer's topology-defect metrics. The infant processing pipeline achieved a 100% (201/201) completion rate on QC-validated inputs. Importantly, NeuroPilot compresses the traditional 2--3 month timeline for training staff and processing complete datasets into a single week. NeuroPilot is deployed in https://wanda-cyberbench.com/.
