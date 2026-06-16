---
interest: medium
link: https://arxiv.org/abs/2606.14713
next_step: skim
priority: low
slack_ts: '1781586974.403129'
source: cs.DB - Databases
status: unread
title: 'Recurring Public Transit Schedules: Stable Identification from GTFS and Similarity
  Analysis'
---
# Recurring Public Transit Schedules: Stable Identification from GTFS and Similarity Analysis
> 原文: [https://arxiv.org/abs/2606.14713](https://arxiv.org/abs/2606.14713)

arXiv:2606.14713v1 Announce Type: new
Abstract: Public transit schedules contain recurring service structures: many dates share the same passenger-facing timetable, while others differ because of weekends, holidays, seasons, or special events. GTFS does not encode these recurring schedules directly, so downstream scheduling, assignment, and mismatch models lack an explicit recurrent supply object. This paper formalizes recurring schedules as DayTypes, defined by the complete set of Route Pattern trips operating on a date, and develops a stable GTFS-based extraction method using H3 route-pattern keys. We then define a schedule-comparison framework with exact, time-tolerant, and structural-comparability metrics that distinguish strict timetable differences from small timing shifts and larger service changes. Validation on Japanese and Canadian GTFS feeds shows substantial schedule compression, a median of four nonempty DayTypes per agency in the pairwise-analysis sample, hierarchical nesting between service classes, and country-level differences in the persistence of exact disjointness. The resulting DayTypes provide compact Route-Pattern-time schedule sets for timetable synchronization, vehicle scheduling, demand assignment, and schedule-consolidation analysis.
