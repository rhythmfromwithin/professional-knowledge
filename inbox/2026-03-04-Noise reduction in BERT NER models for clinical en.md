---
title: "Noise reduction in BERT NER models for clinical entity extraction"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.00022
priority: high
status: unread
interest: medium
next_step: skim
---
# Noise reduction in BERT NER models for clinical entity extraction
> 原文: [https://arxiv.org/abs/2603.00022](https://arxiv.org/abs/2603.00022)

arXiv:2603.00022v1 Announce Type: new
Abstract: Precision is of utmost importance in the realm of clinical entity extraction from clinical notes and reports. Encoder Models fine-tuned for Named Entity Recognition (NER) are an efficient choice for this purpose, as they don't hallucinate. We pre-trained an in-house BERT over clinical data and then fine-tuned it for NER. These models performed well on recall but could not close upon the high precision range, needed for clinical models. To address this challenge, we developed a Noise Removal model that refines the output of NER. The NER model assigns token-level entity tags along with probability scores for each token. Our Noise Removal (NR) model then analyzes these probability sequences and classifies predictions as either weak or strong. A na\"ive approach might involve filtering predictions based on low probability values; however, this method is unreliable. Owing to the characteristics of the SoftMax function, Transformer based architectures often assign disproportionately high confidence scores even to uncertain or weak predictions, making simple thresholding ineffective. To address this issue, we adopted a supervised modeling strategy in which the NR model leverages advanced features such as the Probability Density Map (PDM). The PDM captures the Semantic-Pull effect observed within Transformer embeddings, an effect that manifests in the probability distributions of NER class predictions across token sequences. This approach enables the model to classify predictions as weak or strong with significantly improved accuracy. With these NR models we were able to reduce False Positives across various clinical NER models by 50\% to 90\%.
