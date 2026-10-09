---
title: "SLVR: Structured Latent Visual Reasoning via Human-like Reasoning Flows"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.10563
priority: medium
status: unread
interest: medium
next_step: skim
---
# SLVR: Structured Latent Visual Reasoning via Human-like Reasoning Flows
> 原文: [https://arxiv.org/abs/2610.10563](https://arxiv.org/abs/2610.10563)

arXiv:2610.10563v1 Announce Type: new
Abstract: Multimodal large language models (MLLMs) often answer visual reasoning questions by relying on linguistic priors rather than task-relevant visual evidence. Textual chain-of-thought reasoning can partially mitigate this issue by encouraging models to decompose visual questions into intermediate evidence-seeking steps, but generating these steps autoregressively increases inference cost. Latent reasoning avoids explicit rationale generation, but existing approaches provide limited control over what intermediate states encode, making it difficult to impose separate supervision for planning, grounding, and evidence selection. We propose Structured Latent Visual Reasoning (SLVR), a training framework that bridges explicit chain-of-thought and latent reasoning by organizing multimodal reasoning into typed latent stages for planning, grounding, evidence selection, and reasoning integration.
SLVR first trains the model to rely on the image by masking answer-revealing text and contrasting the correct answer with visually plausible distractors. It then organizes reasoning into latent stages for planning, grounding, evidence selection, and integration, supervising each stage with the corresponding signal: plans, boxes, visual evidence, and final rationales. This gives latent reasoning an explicit functional structure while avoiding generated textual chains at inference time.
Built on Qwen2.5-VL-7B, SLVR improves consistently across multimodal reasoning benchmarks, with absolute gains of +9.4 on MMVP and +14.2 on BLINK Relation, as well as improvements on V\*, MathVista, and ChartQA. These results suggest that structured latent supervision can improve fine-grained visual reasoning without the decoding overhead of textual CoT. Project page is available \href{https://bogao-code.github.io/SLVR/}{here}.
