---
title: "Evaluating Transformer and LSTM Frameworks for Prediction in Ungauged Basins"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2606.02791
priority: high
status: unread
interest: medium
next_step: skim
---
# Evaluating Transformer and LSTM Frameworks for Prediction in Ungauged Basins
> 原文: [https://arxiv.org/abs/2606.02791](https://arxiv.org/abs/2606.02791)

arXiv:2606.02791v1 Announce Type: new
Abstract: Watershed networks exhibit convergent topologies in which multiple tributaries merge into downstream channels,integrating diverse upstream hydrological processes. In ungauged basins, the absence of direct observations increases uncertainty and limits the ability to anticipate extreme events. This study evaluates whether an encoder-only Transformer provides an advantage over an LSTM for upstream streamflow inference under limited hydrologic information, using retrospective simulations from the NOAA National Water Model (NWM). Across both upstream-only and combined configurations, the LSTM showed stronger overall performance than the Transformer model across the two configurations. Incorporating downstream information further boosted performance for all models, increasing median NNSE by more than 60%. Rather than treating this as a leaderboard-style comparison, we interpret the experiments as a test of architectural inductive bias for hydrologic sequence inference. The results indicate that recurrent memory remains better aligned with this upstream reconstruction task than an encoder-only Transformer, while downstream hydrologic context provides a strong auxiliary constraint that substantially improves prediction skill across architectures
