---
interest: medium
link: https://arxiv.org/abs/2610.23858
next_step: skim
priority: medium
slack_ts: '1792556400.697639'
source: cs.CV - Computer Vision
status: unread
title: 'I$^2$-Med: Interpretable Medical Inference through Visual-Guided Dynamic Logits
  Calibration'
---
# I$^2$-Med: Interpretable Medical Inference through Visual-Guided Dynamic Logits Calibration
> 原文: [https://arxiv.org/abs/2610.23858](https://arxiv.org/abs/2610.23858)

arXiv:2610.23858v1 Announce Type: new
Abstract: Medical vision language models have demonstrated strong potential for medical image understanding and reasoning. However, their interpretability and reliability remain limited because medical vision language tasks require precise visual grounding and clinically coherent explanations. This is particularly challenging due to complex imaging patterns and scarce expert annotations. These challenges reduce the effectiveness of conventional reasoning methods and lead to visual hallucination, defined as the generation of text that is not grounded in the given visual input, which further limits their applicability in clinical practice. To mitigate these challenges, we propose an interpretable medical inference (I$^2$-Med) framework that enhances visual faithfulness during inference without additional training to improve reasoning and explanation faithfulness in medical vision language models. During text generation, I$^2$-Med uses a visual guidance module to check whether each candidate word is supported by the medical image and consistent with the current reasoning. Based on this guidance, the model's output scores are adjusted to favor visually grounded words, without changing the model parameters. Extensive experiments on the OmniMedVQA benchmark, covering eight medical imaging modalities and five clinical question types, demonstrate that our proposed I$^2$-Med framework generates more clinically meaningful and visually faithful reasoning chains and reduces visual hallucination under standard medical VQA evaluation metrics. The source code is publicly available at \url{https://github.com/mtanveer1/l2-med}.
