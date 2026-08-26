---
interest: medium
link: https://arxiv.org/abs/2608.20512
next_step: skim
priority: medium
slack_ts: '1787708789.693369'
source: cs.CY - Computers and Society
status: unread
title: 'From Urban Mobility to Epidemic Dynamics: A Mixture-of-Experts Framework with
  Preference Alignment for Policy Scenario Simulation'
---
# From Urban Mobility to Epidemic Dynamics: A Mixture-of-Experts Framework with Preference Alignment for Policy Scenario Simulation
> 原文: [https://arxiv.org/abs/2608.20512](https://arxiv.org/abs/2608.20512)

arXiv:2608.20512v1 Announce Type: new
Abstract: Non-pharmaceutical interventions (NPIs) alter epidemic risk through behavioral reallocations, not simply aggregate mobility reductions. Scenario-based NPI analysis therefore requires a behavioral layer that translates alternative policy calendars into plausible activity and mobility trajectories before downstream outcomes are simulated. We introduce UrbanShare-MoE-PA, a data-driven agent-level framework that maps factual and alternative NPI calendars to daily time-allocation trajectories and propagates them through a calibrated behavior-driven SEIR simulator. The behavioral engine decomposes each agent-day into travel share, POI-category allocation conditional on staying, and travel-mode allocation conditional on traveling. It combines a structured UrbanShare baseline, mixture-of-experts heads for heterogeneous POI and mode responses, and phase-aware preference alignment for calendar-conditioned rollouts. Using data from 911 agents in Singapore observed from March to August 2020, we evaluate factual reconstruction, four alternative lockdown calendars, and epidemic-activity trade-offs. UrbanShare-MoE improves POI reconstruction over the baseline, while UrbanShare-MoE-PA achieves the lowest travel-mode errors and the clearest alternative-calendar trajectories. In the calibrated SEIR simulation, early lockdown lowers infectious burden, late lockdown increases it, and short lockdown preserves the highest weighted activity with only a modest increase in epidemic burden relative to the original policy. These results show that epidemic-activity conclusions depend on how policy calendars are translated into behavior, and that agent-level mobility-share modeling provides an interpretable bridge between policy timing, behavior, and downstream simulation.
