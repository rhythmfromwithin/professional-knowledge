---
title: "Prediction Is Not Calibration: Item Parameter Recovery and Representation Coupling in Knowledge Tracing"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.30211
priority: high
status: unread
interest: medium
next_step: skim
---
# Prediction Is Not Calibration: Item Parameter Recovery and Representation Coupling in Knowledge Tracing
> 原文: [https://arxiv.org/abs/2610.30211](https://arxiv.org/abs/2610.30211)

arXiv:2610.30211v1 Announce Type: new
Abstract: Knowledge tracing (KT) models can estimate item parameters through an item response decoder trained solely for next-response prediction, yet predictive accuracy does not guarantee parameter recovery. We study 2PL, GPCM, and NRM decoders paired with LSTM, Transformer, and DKVMN encoders. Response-model derivatives show why discrimination and option slope updates depend directly on the scale and spread of estimated ability. Affine logit identities show how item-dependent shifts and rescaling in estimated ability are absorbed into item parameters without changing response probabilities. In simulations, difficulty, mean threshold, and correct-option intercept recovery remain high under shuffled order across representation widths, whereas discrimination and keyed option slope contrast recovery require wider item representations and degrade further under fixed item order. Separating the sequence item representation (width $d\_S$) from the item parameter key (width $d\_M$), and pairing a wide key with a thin sequence representation ($\mathrm{SK}(64,8)$), reduces fixed-order ability distortions and improves recovery and cross-order consistency without sacrificing test accuracy or increasing model size relative to a shared width-64 baseline ($\mathrm{SH}(64)$). On TIMSS and EdNet, widening $d\_M$ consistently improves agreement with an offline IRT reference, while the trade-off from narrowing $d\_S$ depends on the encoder's reliance on sequence width for prediction. These findings show why item parameters, especially discrimination and option slopes, must be evaluated separately from response prediction.
