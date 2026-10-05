---
title: "SOLO: Certified-Recall Metric Similarity Search with Scan-Only Sampled Inverted Lists"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.02387
priority: low
status: unread
interest: medium
next_step: skim
---
# SOLO: Certified-Recall Metric Similarity Search with Scan-Only Sampled Inverted Lists
> 原文: [https://arxiv.org/abs/2610.02387](https://arxiv.org/abs/2610.02387)

arXiv:2610.02387v1 Announce Type: new
Abstract: We present SOLO, an index for approximate nearest-neighbor search in general metric spaces whose serving path contains no ranking heuristic of any kind: a query is routed to the $k\_s$ nearest points of a random sample of the database, and every object in the touched posting lists is evaluated with the true distance. Because nothing must outrank anything, recall equals a coverage probability computable from the stored index: one ground-truth pass over a query sample certifies every operating point at once, without serving any of them -- a recall certificate, and for a navigable graph no analogous object exists at any price. The whole index is one recursive rule -- sample the collection, post each object to its $b$ nearest sample points, split any list that outgrows a bound, always scan the leaves -- and its operating surface obeys an equal-work law, recall $\approx f(b \cdot k\_s)$, whose level is a one-scalar signature of the dataset. The same scan-only structure gives a serving floor no graph architecture reaches once the router is itself indexed by the same rule: Deep-100M served at recall 0.9977 from 1 GB of resident memory (enforced cap, 10.7 bytes per object) and at 0.9964 from 256 MB, Deep-1B at recall 0.9925 from 512 MB (and from 96 MB at depth 3), inserts that are one search, and deletes that are exact. Throughput is competitive where the hardware allows it -- up to $1.8\times$ a tuned HNSW at $10^8$ on a two-socket 32-core server, with operating points to the right of where that graph saturates -- and the tables report it against HNSW, DiskANN, GRAFT, NAPP, misi, and SPANN's assignment rule on the same hardware and ground truth.
