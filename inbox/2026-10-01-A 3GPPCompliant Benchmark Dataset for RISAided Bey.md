---
interest: medium
link: https://arxiv.org/abs/2609.39058
next_step: skim
priority: low
slack_ts: '1790918087.778639'
source: cs.DB - Databases
status: unread
title: A 3GPP-Compliant Benchmark Dataset for RIS-Aided Beyond 5G Networks
---
# A 3GPP-Compliant Benchmark Dataset for RIS-Aided Beyond 5G Networks
> 原文: [https://arxiv.org/abs/2609.39058](https://arxiv.org/abs/2609.39058)

arXiv:2609.39058v1 Announce Type: new
Abstract: Reconfigurable Intelligent Surfaces (RIS) are emerging as a key technology for programmable wireless environments in the beyond the fifth generation (B5G) networks. However, data-driven RIS research remains bottleneck by the lack of standardized, high-fidelity and open-source datasets. In this paper, we introduce a large-scale 3GPP TR 38.901-compliant dataset for RIS-aided millimeter wave (mmWave) networks, that considers severe path loss, blockage sensitivity, and spatial channel sparsity make the RIS assistance more impactful. The dataset spans various canonical 3GPP deployment scenarios across 20 controlled variants, capturing diverse user densities, fading conditions, and blockage regimes. Uniquely, every sample includes oracle RIS phase configurations obtained via a globally optimal brute-force codebook search, providing gold-standard supervision labels that are absent from any existing public dataset. Rich multi-task annotations comprising full channel state information (CSI), per-link channel decomposition, optimal phase matrices, and channel quality index (CQI) labels support a broad range of machine learning paradigms and downstream tasks, including phase optimization, channel estimation, and interference management. As the primary benchmark task, we introduce a novel CSI-to-CQI mapping that frames RIS-aided link-quality prediction as a scalable scalar classification problem, thereby avoiding the exponential output complexity of the direct phase vector prediction. We have evaluated this mapping against state-of-the-art architectures under in-distribution, out-of-distribution, and real-world hardware measurement conditions. Our dataset provides a reproducible, extensible, and community-ready foundation to accelerate data-driven research in RIS-aided B5G networks.
