---
title: "The Tethys Dataset: Seven Years of Hourly Smart Water Metering and a Pipeline for Making It Usable"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.22358
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Tethys Dataset: Seven Years of Hourly Smart Water Metering and a Pipeline for Making It Usable
> 原文: [https://arxiv.org/abs/2609.22358](https://arxiv.org/abs/2609.22358)

arXiv:2609.22358v1 Announce Type: new
Abstract: Methods for water demand forecasting and leak detection are based on public datasets, and for water those are scarce, short, or released only after an undocumented cleaning process, hiding defects of the deployment they came from. We present Tethys: 91 months of hourly water consumption data from 24 buildings of a municipal water network, published with a quantitative account of its quality, rather than in place of one. Raw availability is 59.4%, while loss is not random: 4 fleet-wide outages totalling 595 days interrupt the entire estate at once. We show that the aggregation producing the released files silently introduced 205,200 impossible decreases in a cumulative index, and that correcting it is a one-line change. Because the meters are cumulative, the readings bracketing a short gap fix the volume that passed through it, so 75.9% of hours rest on a measurement, while 24.1% are reported as unknown. We release the dataset, its per-hour provenance, and the pipeline that produces it.
