---
title: "Wide-Area GNSS Spoofing and Jamming Detection Using AIS-Derived Spatiotemporal Integrity Monitoring"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.11055
priority: low
status: unread
interest: medium
next_step: skim
---
# Wide-Area GNSS Spoofing and Jamming Detection Using AIS-Derived Spatiotemporal Integrity Monitoring
> 原文: [https://arxiv.org/abs/2603.11055](https://arxiv.org/abs/2603.11055)

arXiv:2603.11055v1 Announce Type: new
Abstract: Global Navigation Satellite System (GNSS) spoofing and jamming threaten maritime navigation by corrupting positions from Automatic Identification System (AIS) transponders. Crucially, raw AIS messages contain communication-layer defects (duplicated MMSIs, timestamp errors, stale retransmissions, and multi-station rebroadcast delays) that can mimic spoofing or jamming. Thus, AIS positions are unreliable without pre-filtering. We propose a three-stage AIS-based framework that (1) uses rule-based diagnostics to discard communication faults, (2) applies an interacting multiple model filter and transmission-interval analysis to extract kinematic-consistency and continuity anomalies, and (3) applies spatiotemporal DBSCAN to group anomalies by multi-vessel coherence and temporal persistence and classify them as sensor faults, spoofing, or jamming. Tested on approximately 966 million AIS messages from Korean coastal waters, the framework detected 17 spoofing and 343 jamming clusters and reduced false alarms by 98.6% relative to naive clustering. These results show that, after rigorous pre-filtering, AIS data can enable wide-area GNSS interference detection without dedicated sensors.
