---
interest: medium
link: https://arxiv.org/abs/2609.26920
next_step: skim
priority: medium
slack_ts: '1790310818.283159'
source: cs.CV - Computer Vision
status: unread
title: Cross-Modal Contrastive Learning from Histopathology and CT for Automated Renal
  Cell Carcinoma Grading
---
# Cross-Modal Contrastive Learning from Histopathology and CT for Automated Renal Cell Carcinoma Grading
> 原文: [https://arxiv.org/abs/2609.26920](https://arxiv.org/abs/2609.26920)

arXiv:2609.26920v1 Announce Type: new
Abstract: Background: Clear cell renal cell carcinoma (ccRCC) exhibits substantial clinical heterogeneity, and accurate grade assessment is essential for risk stratification and treatment planning. However, conventional grading requires invasive tissue sampling. We developed RCC-Align, a cross-modal contrastive learning framework that leverages paired histopathology and computed tomography (CT) data during training to improve noninvasive CT-based ccRCC grade prediction. Methods: RCC-Align aligns paired whole-slide histopathology images (WSIs) and CT scans through contrastive cross-modal objectives, transferring grade-discriminative information from microscopic tissue morphology to macroscopic radiologic representations. The framework was trained and evaluated on paired TCGA and CPTAC cohorts using patient-level five-fold cross-validation. Performance for low- versus high-grade ccRCC classification was compared against CT-only baselines (DINOv2-Base and DINOv2-Finetuned) and a WSI-based reference model (GigaPath-Finetuned). Cross-modal alignment was assessed using cosine similarity analysis. Results: RCC-Align achieved an AUC of 0.601 (95% CI, 0.524-0.673) and AUPRC of 0.599 (95% CI, 0.541-0.676), outperforming DINOv2-Finetuned (AUC 0.545; AUPRC 0.543) with significantly improved low-grade prediction (p = 0.004). RCC-Align also demonstrated stronger paired WSI-CT embedding alignment compared with baselines. The WSI-based GigaPath reference achieved an AUC of 0.719. Conclusion: Pathology-guided contrastive learning improves CT-based ccRCC grading while requiring only CT at inference. This approach may complement tissue diagnosis when biopsy is unsafe, infeasible, or limited by intratumoral heterogeneity. Validation in larger, multi-institutional cohorts with external testing is needed before clinical translation.
