---
title: "Lost in Translation: How Language Re-Aligns Vision for Cross-Species Pathology"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.04405
priority: medium
status: unread
---
# Lost in Translation: How Language Re-Aligns Vision for Cross-Species Pathology
> 原文: [https://arxiv.org/abs/2603.04405](https://arxiv.org/abs/2603.04405)

arXiv:2603.04405v1 Announce Type: new
Abstract: Foundation models are increasingly applied to computational pathology, yet their behavior under cross-cancer and cross-species transfer remains unspecified. This study investigated how fine-tuning CPath-CLIP affects cancer detection under same-cancer, cross-cancer, and cross-species conditions using whole-slide image patches from canine and human histopathology. Performance was measured using area under the receiver operating characteristic curve (AUC). Few-shot fine-tuning improved same-cancer (64.9% to 72.6% AUC) and cross-cancer performance (56.84% to 66.31% AUC). Cross-species evaluation revealed that while tissue matching enables meaningful transfer, performance remains below state-of-the-art benchmarks (H-optimus-0: 84.97% AUC), indicating that standard vision-language alignment is suboptimal for cross-species generalization. Embedding space analysis revealed extremely high cosine similarity (greater than 0.99) between tumor and normal prototypes. Grad-CAM shows prototype-based models remain domain-locked, while language-guided models attend to conserved tumor morphology. To address this, we introduce Semantic Anchoring, which uses language to provide a stable coordinate system for visual features. Ablation studies reveal that benefits stem from the text-alignment mechanism itself, regardless of text encoder complexity. Benchmarking against H-optimus-0 shows that CPath-CLIP's failure stems from intrinsic embedding collapse, which text alignment effectively circumvents. Additional gains were observed in same-cancer (8.52%) and cross-cancer classification (5.67%). We identified a previously uncharacterized failure mode: semantic collapse driven by species-dominated alignment rather than missing visual information. These results demonstrate that language acts as a control mechanism, enabling semantic re-interpretation without retraining.
