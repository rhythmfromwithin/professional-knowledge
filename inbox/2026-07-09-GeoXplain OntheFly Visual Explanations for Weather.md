---
title: "GeoXplain: On-the-Fly Visual Explanations for Weather Foundation Models"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2607.05655
priority: low
status: unread
interest: medium
next_step: skim
---
# GeoXplain: On-the-Fly Visual Explanations for Weather Foundation Models
> 原文: [https://arxiv.org/abs/2607.05655](https://arxiv.org/abs/2607.05655)

arXiv:2607.05655v1 Announce Type: new
Abstract: Weather and climate foundation models produce high-dimensional forecasts whose learned relationships are difficult to inspect with static plots alone. GeoXplain is an interactive Python-based visualization toolkit for exploring geospatial attribution maps across climate variables, atmospheric pressure levels, and forecast time. The toolkit accepts attribution bundles containing attribution grids together with corresponding metadata and renders them in a notebook widget or browser with map and globe modes, linked timelines, pressure-level controls, target annotations, and optional physical-field overlays. We frame GeoXplain as a model-agnostic earth-system visualization toolkit and present the GeoXplain Aurora Adapter as its first computation backend. The adapter computes explanations for the Aurora foundation model, either in a local GPU process, through a GPU listener, or through a SLURM-backed listener, while preserving the same Python call site for analysts. It currently supports gradient saliency, Integrated Gradients, RISE, ViT-CX, multi-frame saliency and Integrated Gradients rollouts, and retrieval of ERA5 overlays. GeoXplain can be installed as a PyPI package with pip install geoxplain. The code is open-source and available at https://github.com/clemenskoprolin/geoxplain.
