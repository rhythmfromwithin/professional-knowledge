---
title: "HiFIVE: High-Fidelity Vector-Tile Reduction for Interactive Map Exploration"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.10270
priority: low
status: unread
interest: medium
next_step: skim
---
# HiFIVE: High-Fidelity Vector-Tile Reduction for Interactive Map Exploration
> 原文: [https://arxiv.org/abs/2603.10270](https://arxiv.org/abs/2603.10270)

arXiv:2603.10270v1 Announce Type: new
Abstract: Interactive visualization is a common tool for exploring large open-data repositories, where users quickly explore datasets across diverse domains. When it comes to large-scale spatial data, many existing tools rely on server-side rendering to produce small images that can be viewed at the client-side. However, most users prefer client-side rendering that allows quick styling of the data for better visualization experience. This paper presents HiFIVE, a data-management framework for scalable, high-fidelity client-side geospatial visualization. We formalize the visualization-aware tile reduction problem, which captures the trade-off between tile-size and visualization distortion, and prove its NP-hardness. HiFIVE introduces a two-stage solution combining triage and sparsification to selectively prune records, attributes, and values based on information-theoretic and spatial criteria. Experiments demonstrate substantial tile-size reductions while preserving visual fidelity and interactive performance at terabyte scale.
