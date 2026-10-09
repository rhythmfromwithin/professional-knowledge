---
interest: medium
link: https://arxiv.org/abs/2610.06930
next_step: skim
priority: medium
slack_ts: '1791524733.931519'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Low-Rank and Structured Sparse Tensor Decomposition for Anomaly Detection in
  Multivariate Functional Data
---
# Low-Rank and Structured Sparse Tensor Decomposition for Anomaly Detection in Multivariate Functional Data
> 原文: [https://arxiv.org/abs/2610.06930](https://arxiv.org/abs/2610.06930)

arXiv:2610.06930v1 Announce Type: new
Abstract: Multivariate functional data arise in many modern manufacturing systems, where multiple sensors record densely sampled process trajectories. Monitoring such data is challenging because nominal variation is strongly correlated across samples, sensors, and time, while faults may appear either as isolated deviations or as structured departures concentrated within a limited number of sensor-specific temporal trajectories. We propose two unsupervised sparse tensor decomposition methods that preserve this multimode structure. Entrywise Sparse CP Decomposition (ES-CP) uses an entrywise \(\ell\_1\) penalty to identify localized anomalies, whereas Fiberwise Sparse-Group Lasso CP Decomposition (FG-Lasso) combines entrywise and fiberwise penalties to detect both localized deviations and anomalies concentrated within temporal fibers. Both methods represent nominal process behavior through a low-rank CP decomposition and are estimated using alternating optimization with closed-form sparse-component updates. Two simulation studies evaluate performance under different fault structures, signal severities, noise levels, and missing observations. FG-Lasso attains or ties the highest macro F$\_1$ score in almost all settings in the first study and achieves the highest macro F$\_1$ score. In a multichannel forging-process case study, FG-Lasso and ES-CP obtain macro F$\_1$ scores of 0.85 and 0.82, respectively, compared with 0.69 or lower for TRPCA and PCA-based anomaly detectors. The results demonstrate that explicitly matching the sparse penalty to the anticipated fault structure improves both anomaly detection and fault localization in high-dimensional functional processes.
