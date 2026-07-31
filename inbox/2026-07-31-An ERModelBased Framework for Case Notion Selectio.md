---
title: "An ER-Model-Based Framework for Case Notion Selection in Object-Centric Processes"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2607.26384
priority: low
status: unread
interest: medium
next_step: skim
---
# An ER-Model-Based Framework for Case Notion Selection in Object-Centric Processes
> 原文: [https://arxiv.org/abs/2607.26384](https://arxiv.org/abs/2607.26384)

arXiv:2607.26384v1 Announce Type: new
Abstract: Object-centric process mining operates on event logs where each event references multiple objects of different types. A fundamental challenge is defining a case notion - the grouping of events into coherent process execution instances -without which process discovery and conformance checking cannot proceed. Existing approaches either flatten the log to a single object type (losing inter-object coordination) or use the connected component of the object graph (creating overly complex cases due to resource-like objects). We propose an Entity-Relationship-schema-guided framework that identifies the primary entity (PE) type anchoring each process execution, classifies other entity types as secondary coordination entities or resources, and defines cases as connected components of the primary and secondary entity object relationship graph. The resulting case notion is shown to produce strict partitions with automatic transitive closure. The framework is illustrated with an order management process and validated on a 1,000-event OCEL log producing 40 structurally coherent cases.
