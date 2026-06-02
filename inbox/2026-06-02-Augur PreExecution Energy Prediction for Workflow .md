---
title: "Augur: Pre-Execution Energy Prediction for Workflow Tasks in Heterogeneous Clusters"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.00348
priority: medium
status: unread
interest: medium
next_step: skim
---
# Augur: Pre-Execution Energy Prediction for Workflow Tasks in Heterogeneous Clusters
> 原文: [https://arxiv.org/abs/2606.00348](https://arxiv.org/abs/2606.00348)

arXiv:2606.00348v1 Announce Type: new
Abstract: Scientific workflows are widely used to process large quantities of data, leading to significant energy consumption and carbon emissions. To reduce this environmental impact, energy and carbon-aware scheduling approaches could be employed. However, such methods require runtime and energy predictions, which are typically only available for workflows that have been executed previously. Meanwhile, scientists may execute new or modified workflows, use workflows with different input data, or run them on alternative infrastructure. To address this critical gap, we propose Augur, a novel method to predict the energy consumption of scientific workflow tasks prior to execution. By efficiently profiling both the available cluster infrastructure and the workflow at hand, Augur is capable of predicting the overall energy consumption of the workflow with a median prediction error of $16.3\pm15.3\%$ compared to Ichnos, an energy estimation method that uses fitted power models, and $18.2\pm14.7\%$ compared to Intel RAPL, as observed in our experimental evaluation on public and private cloud infrastructure. Relying on only minimal historical execution data, Augur outperforms two state-of-the-art methods in predicting both task runtime and total workflow energy, providing a robust foundation for energy-efficient and carbon-aware scientific data analysis.
