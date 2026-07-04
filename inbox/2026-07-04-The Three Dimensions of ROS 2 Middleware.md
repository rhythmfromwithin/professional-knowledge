---
interest: medium
link: https://arxiv.org/abs/2607.01304
next_step: skim
priority: medium
slack_ts: '1783136978.250079'
source: cs.RO - Robotics
status: unread
title: The Three Dimensions of ROS 2 Middleware
---
# The Three Dimensions of ROS 2 Middleware
> 原文: [https://arxiv.org/abs/2607.01304](https://arxiv.org/abs/2607.01304)

arXiv:2607.01304v1 Announce Type: new
Abstract: ROS 2 (Robot Operating System 2) has emerged as the de facto standard for modern robot software development, with middleware implementations such as the Data Distribution Service (DDS) and Zenoh forming the core infrastructure for distributed robotic communication. Despite their architectural flexibility, these middleware systems exhibit structural limitations, particularly under dynamic and resource-constrained wireless environments. This paper presents a systematic survey of ROS 2 middleware and introduces a conceptual framework to examine its architectural limits through three structural dimensions required by distributed robotic systems, namely Space, Time, and State. We first provide a structured analysis of middleware architecture and operational dynamics, including discovery, data exchange, and state management mechanisms. Building on this foundation, we formalize Time as temporal predictability for control loops, Space as spatial abstraction from physical topology to enable modular deployment, and State as contextual continuity despite dynamic node participation and intermittent connectivity. Through a comprehensive review of existing implementations and prior studies, we organize middleware research according to the structural trade-offs that arise among these dimensions. Under constrained wireless conditions, spatial abstraction can obscure network variability and weaken temporal guarantees, while mechanisms that preserve state continuity introduce computational and network overhead that competes with time-critical communication. These interactions reveal structural trade-offs that characterize the practical limits of contemporary robot middleware. By synthesizing architectural patterns and identifying gaps in current modeling and analysis approaches, this survey outlines a principled research roadmap for robust and scalable robotic middleware architectures.
