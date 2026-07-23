---
title: "Hazard or Anomaly? Evaluating VLMs for Understanding Dangers and Discrepancies"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.18325
priority: medium
status: unread
interest: medium
next_step: skim
---
# Hazard or Anomaly? Evaluating VLMs for Understanding Dangers and Discrepancies
> 原文: [https://arxiv.org/abs/2607.18325](https://arxiv.org/abs/2607.18325)

arXiv:2607.18325v1 Announce Type: new
Abstract: Modern safety-critical systems increasingly rely on human-robot interaction to reduce disaster risk and support decision-making during emergencies. Vision-Language Models (VLMs) are promising for these settings because they can interpret complex scenes and communicate safety-relevant information, but they still require careful evaluation to ensure reliable safety reasoning. In particular, current evaluations often frame danger recognition as a binary decision (Safe/Unsafe), making it unclear whether a model is identifying true physical hazards or merely reacting to unusual scene elements. We address this limitation by introducing an explicit distinction between hazard and anomaly, and by separately recognizing hazardous and anomalous states. We evaluate several state-of-the-art VLMs across two datasets and multiple prompting strategies to test whether this distinction changes model behavior. Our results show that VLMs frequently misinterpret anomalousness as hazardousness, revealing an over-reliance on contextual irregularity as a proxy for danger. We further show that explicitly separating anomaly from hazard provides a more informative evaluation of VLM safety reasoning and exposes failure modes that binary safety judgments can obscure. Our public dataset is available on Roboflow https://app.roboflow.com/vlm-in-context-anomaly-and-hazard-detection/camera-ready-roman-ds.
