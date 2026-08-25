---
title: "Scalpel3: A High-Performance Data Carving Architecture for Recovery of Fragmented Files"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.20363
priority: medium
status: unread
interest: medium
next_step: skim
---
# Scalpel3: A High-Performance Data Carving Architecture for Recovery of Fragmented Files
> 原文: [https://arxiv.org/abs/2608.20363](https://arxiv.org/abs/2608.20363)

arXiv:2608.20363v1 Announce Type: new
Abstract: File carving recovers files from raw storage media without relying on filesystem metadata, a key capability in digital forensics, data recovery, and digital exploration. Traditional tools such as Foremost, Scalpel v1/2, and PhotoRec handle contiguous files effectively, and some support fragmented recovery for specific formats under simplifying assumptions, but no publicly available tool provides a general-purpose, high-performance framework for developing and deploying fragmented recovery strategies across many file types at scale. This paper presents Scalpel3, the first general-purpose, open source, massively parallel file carving framework designed to support both contiguous and fragmented recovery at scale. Its primary contribution is an extensible, high-performance architecture that enables researchers to develop, test, and deploy new carving strategies without implementing their own multithreaded backends or I/O infrastructure. Adding support for new file types typically requires only development of single-threaded file validation logic and, where useful, block validation or custom reassembly logic -- the Scalpel3 backend manages parallelization, synchronization, and fast I/O automatically. The architecture also integrates the ONNX Runtime, allowing learned classifiers to participate in block validation and reassembly when useful. Beyond raw performance, Scalpel3 introduces practical features for real-world investigations: persistent checkpointing for long-running jobs, human-in-the-loop control allowing operators to monitor progress and redirect effort interactively, and block-level deduplication to shrink the search space. By making this framework publicly available, we aim to lower barriers to experimentation and help translate file carving research into practitioner-ready tools.
