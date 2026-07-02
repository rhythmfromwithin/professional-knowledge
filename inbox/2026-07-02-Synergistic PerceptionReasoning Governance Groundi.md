---
interest: medium
link: https://arxiv.org/abs/2607.00060
next_step: skim
priority: medium
slack_ts: '1782965370.109839'
source: cs.CV - Computer Vision
status: unread
title: 'Synergistic Perception-Reasoning Governance: Grounding Medical MLLMs with
  Verifiable Anatomical Evidence'
---
# Synergistic Perception-Reasoning Governance: Grounding Medical MLLMs with Verifiable Anatomical Evidence
> 原文: [https://arxiv.org/abs/2607.00060](https://arxiv.org/abs/2607.00060)

arXiv:2607.00060v1 Announce Type: new
Abstract: Multimodal large language models (MLLMs) show strong promise for clinical VQA and radiology report generation, yet inference-time hallucinations still undermine trustworthy use: models can produce fluent conclusions that conflict with imaging evidence. Existing mitigation strategies typically rely on additional training, external retrieval/knowledge bases, or multi-stage post-hoc verification, which increases cost and pipeline complexity and often generalizes poorly across models and tasks.To address this, we propose a holistic, training-free evidence-injection framework that systematically mitigates hallucinations through dual-side evidence injection. By leveraging ROI priors acquired using MedSAM in our implementation, we recalibrate the visual perception trajectory via ROI-guided activation modulation while anchoring the textual reasoning trajectory by mapping anatomical coordinates into discrete semantic tokens as verifiable external memory. Then we introduce a task-aware dynamic router to select modality-specific interventions based on task semantics, balancing perceptual grounding and linguistic fluency. We conduct systematic evaluations on 2 tasks and 5 datasets using \texttt{LLaVA-1.5-7B}, \texttt{LLaVA-Med-1.5-7B}, \texttt{Qwen3-VL-8B/32B}, and \texttt{InternVL-3.5-8B/38B}. Controlled ablations and visualizations further validate the framework, which consistently outperforms baselines across medical benchmarks, improving close-ended accuracy by up to $\sim\mathbf{6}\%\uparrow$ and reducing open-ended hallucinations by $\sim\mathbf{35}\%\downarrow$. The code has been made available on GitHub: \href{https://github.com/Henry991115/SPRG}{\textcolor{blue}{https://github.com/Henry991115/SPRG}}.
