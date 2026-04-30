---
title: "GCA-BULF: A Bottom-Up Framework for Short-Term Load Forecasting Using Grouped Critical Appliances"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.24766
priority: high
status: unread
interest: medium
next_step: skim
---
# GCA-BULF: A Bottom-Up Framework for Short-Term Load Forecasting Using Grouped Critical Appliances
> 原文: [https://arxiv.org/abs/2604.24766](https://arxiv.org/abs/2604.24766)

arXiv:2604.24766v1 Announce Type: new
Abstract: With the rise of time-of-use and tiered electricity pricing, energy consumers are encouraged to adopt peak-shifting strategies by automatically controlling high-power appliances. These help lower energy costs while enhancing the power grid's stability. To support such energy management with high resilience and responsiveness, reliable short-term load forecasting (STLF) plays a critical role. STLF predicts electricity consumption over time horizons ranging from minutes to days, using historical data, temporal patterns, and contextual factors. Traditional top-down forecasting methods struggle to capture the complex consumption patterns of diverse and mixed appliance loads. Although bottom-up methods improve forecasting accuracy by integrating appliance-level data, monitoring all appliances is costly, and many do not meaningfully impact total load prediction. Therefore, we propose GCA-BULF, a bottom-up short-term load forecasting framework based on grouped critical appliances, supported by three key designs. First, the Critical Appliance Filtering module ranks appliances according to their power consumption, switching frequency, and usage pattern periodicity, and identifies critical ones through iterative load decomposition. Next, the Related Appliance Grouping module clusters these appliances based on spatial and temporal correlations for group-level forecasting. Finally, the Collaborative Load Forecasting module refines the total load prediction by combining multiple group-level forecasts. We evaluate GCA-BULF on residential and office building load forecasting tasks. Experimental results reveal that GCA-BULF improves hourly total load forecasting by 20.85%-57.88% compared to existing top-down methods and by 33.03%-92.48% compared to bottom-up methods.
