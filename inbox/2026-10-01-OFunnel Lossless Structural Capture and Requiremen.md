---
title: "O-Funnel: Lossless Structural Capture and Requirement-Driven Extraction from Drifting, Heterogeneous Documents"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.39209
priority: low
status: unread
interest: medium
next_step: skim
---
# O-Funnel: Lossless Structural Capture and Requirement-Driven Extraction from Drifting, Heterogeneous Documents
> 原文: [https://arxiv.org/abs/2609.39209](https://arxiv.org/abs/2609.39209)

arXiv:2609.39209v1 Announce Type: new
Abstract: Pulling a fixed set of fields out of documents that arrive in many formats and under drifting schemas is usually done with hand-written byte patterns, which break whenever a key is renamed, a value is reformatted, or a lookalike value appears first. We argue the cause is structural: one pattern must both describe the value and locate it among its surroundings. O-Funnel separates the two. It transcribes any XML, JSON, CSV, HTML or key-value text document into one typed tree over five constructors, gated by an oracle that rejects any capture that does not reconstruct its source. Each needed field is declared in the tree's own terms and located by fusing independent evidence (key, path, value shape, synonym, key spelling, record neighborhood, value profile), so the best-supported node wins and a missing field is reported with a reason. Data no requirement claims becomes residue that a funnel traces back to the requirements to learn new key aliases. On 34,989 real PubMed records, O-Funnel matches a hand-written parser (F1 1.00). After a five-element schema rename, the parser's regular expressions fall to 0.20 while O-Funnel stays at 1.00, with every capture verified complete. On constructed suites that isolate regex failure modes it raises F1 from 0.43 to 1.00, and from 0.80 to 0.94 after self-improvement; on held-out schema-matching instances it is competitive with classical matchers without training. O-Funnel is a dependency-free Python library (pip install ofunnel).
