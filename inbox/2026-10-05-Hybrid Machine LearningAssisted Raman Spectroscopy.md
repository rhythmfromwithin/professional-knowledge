---
title: "Hybrid Machine Learning-Assisted Raman Spectroscopy with Generative Feature Augmentation for Pharmaceutical Identification"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.02224
priority: high
status: unread
interest: medium
next_step: skim
---
# Hybrid Machine Learning-Assisted Raman Spectroscopy with Generative Feature Augmentation for Pharmaceutical Identification
> 原文: [https://arxiv.org/abs/2610.02224](https://arxiv.org/abs/2610.02224)

arXiv:2610.02224v1 Announce Type: new
Abstract: Rapid and reliable identification of pharmaceutical residues is important for safeguarding public health, ensuring food safety, and enabling practical Raman-based screening. In this study, we propose HyMLRaman, a hybrid Raman spectroscopy framework that combines deep spectral feature extraction, generative models, and classical machine-learning classifiers to identify six pharmaceutical compounds, including amoxicillin, chloramphenicol, ciprofloxacin, tetracycline, ibuprofen, and paracetamol. Raman spectra are converted into spectral images and encoded with several deep neural-network backbones, among which EfficientNet-B3 yields the most effective representation. The resulting 1536-dimensional embeddings are then used to train downstream classifiers, including SVM, KNN, logistic regression, random forest, XGBoost, and ANN, using stratified 10-fold cross-validation. The hybrid EfficientNet-B3--SVM configuration achieves the strongest baseline performance, reaching 96.31% accuracy and a macro-F1 score of 96.36%, outperforming the standalone CNN baseline. To address limited-data conditions, a generative model, a DDPM-based feature augmentation, is introduced in a PCA-reduced EfficientNet-B3 latent space. The low-data ablation results show that DDPM augmentation provides selective benefits, particularly for KNN with reduced training fractions, and that its effect remains classifier-dependent. Finally, an application-level Raman Pharmaceutical Analyzer demonstrates the feasibility of embedding the trained model into an interactive Raman analysis workflow. These results suggest that HyMLRaman provides a practical and interpretable route for rapid Raman-based pharmaceutical screening.
