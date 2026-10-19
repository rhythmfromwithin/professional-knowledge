---
title: "Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.22461
priority: medium
status: unread
interest: medium
next_step: skim
---
# Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses
> 原文: [https://arxiv.org/abs/2610.22461](https://arxiv.org/abs/2610.22461)

arXiv:2610.22461v1 Announce Type: new
Abstract: Refuse collection in pedestrian campuses, parks and mixed-use districts remains manual because compaction trucks cannot reach bins located on walkways, courtyards and building service doors. This paper presents Mothership, a two-tier autonomous refuse collection system in which an electric compaction truck (the mothership) carries two low-speed sidewalk robots (RoboCarts) that fetch standard two-wheel bins, deliver them to the truck, return the empty bins to their original positions and re-dock on the truck for charging. The architecture separates responsibilities by scale: the truck performs road driving, compaction, lifting and energy supply, while the carts perform only sidewalk transport and bin grasping. This split removes the lift-and-tip mechanism from the sidewalk vehicle, keeping it light and low, and relaxes cart-to-truck docking tolerance to the +/-100 mm capture window of a standard automated lifter. We describe the system architecture, the bin-handling and docking interfaces, and a mission-planning formulation that decomposes a route into truck stop points and cart tasks. A discrete-event simulation over synthetic campus layouts with 2-16 bins/ha quantifies throughput as a function of bin density, cart count and stop-point radius. A two-cart configuration serves 20-29 bins/h. Throughput is governed by an interaction between cart count and stop-point radius: a single cart performs best with many close stops, whereas three or four carts need wide stops (80 m) to stay busy, reaching 35-49 bins/h at moderate-to-high densities. The best stop radius therefore has to be chosen together with the fleet size, not fixed in advance.
