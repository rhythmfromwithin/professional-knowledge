---
interest: medium
link: https://arxiv.org/abs/2606.30680
next_step: skim
priority: medium
slack_ts: '1782880935.308759'
source: cs.RO - Robotics
status: unread
title: Locker-based Truck-Drone Routing with Integrated Considerations of Pickups,
  Deliveries, and No-Fly Zones
---
# Locker-based Truck-Drone Routing with Integrated Considerations of Pickups, Deliveries, and No-Fly Zones
> 原文: [https://arxiv.org/abs/2606.30680](https://arxiv.org/abs/2606.30680)

arXiv:2606.30680v1 Announce Type: new
Abstract: Truck-drone delivery is an emerging last-mile logistics mode combining the long-haul capacity of trucks with the flexible service capability of drones. In locker-based operations, smart lockers serve not only as temporary parcel storage facilities but also as automated drone docking and service nodes. These automated nodes support drone takeoff, landing, parcel handover, and battery replacement, thereby significantly extending the service range and operational flexibility of drone-assisted delivery networks. However, practical locker-based delivery systems face complex real-world challenges, requiring the integrated coordination of not only parcel delivery, return pickup, battery-constrained and load-dependent drone flights, but also necessary detours around restricted airspace. To address this practical and multifaceted challenge, this paper introduces a locker-based truck-drone routing problem with integrated considerations of pickups, deliveries, and no-fly zones (LTDRP-PDNF), with the objective of minimizing the total operational cost of a fleet of drone-equipped trucks. We formulate the route construction process as a Markov Decision Process and develop a two-stage deep reinforcement learning-based neural heuristic. The first stage utilizes an attention-based encoder and a Bidirectional Gated Recurrent Unit decoder to solve the truck-only routing problem, formulated as a capacitated vehicle routing problem. The second stage combines a policy-transfer strategy with a hybrid dispatch assignment heuristic to construct fully coordinated truck and drone routes for LTDRP-PDNF. Experiments on instances of different scales demonstrate that the proposed method outperforms metaheuristic and neural heuristic baselines in most cases while maintaining exceptionally short computation times, offering an effective, scalable solution framework under practical operational constraints.
