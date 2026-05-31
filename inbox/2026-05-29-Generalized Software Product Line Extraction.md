---
interest: medium
link: https://arxiv.org/abs/2605.28989
next_step: skim
priority: low
slack_ts: '1780202384.915589'
source: cs.SE - Software Engineering
status: unread
title: Generalized Software Product Line Extraction
---
# Generalized Software Product Line Extraction
> 原文: [https://arxiv.org/abs/2605.28989](https://arxiv.org/abs/2605.28989)

arXiv:2605.28989v1 Announce Type: new
Abstract: Software product line (SPL) engineering has been successfully applied to software development by obtaining software systems as compositions of modular features. Existing approaches to SPL engineering, however, are typically bound to a specific technological space (such as, a programming language and a composer) and integrated development environment (IDE), and rely on extraction mechanisms that make strong assumptions on the underlying technological space. This tight coupling hinders reuse, evolution, and adoption of heterogeneous development environments. We propose a general, workbench-agnostic protocol for extracting feature models from existing software artifacts and for configuring and deriving software products. The protocol follows a bottom-up approach based on lightweight dependency units called "atoms", and organizes the extraction and configuration process around an SPL server (workbench-independent) and an SPL client with a workbench-specific backend and a generic frontend. The protocol makes few assumptions on the underlying software artifacts and is therefore applicable to varied SPLs. The applicability of this approach is presented through a prototypical implementation of the architecture in which several subsystems interact and can be swapped freely without affecting the others. In particular, we focus on the application of such a protocol in the context of language product lines (LPLs), demonstrating its applicability to concrete scenarios while preserving workbench-agnosticism. From bottom to top, the implementation comprises: Neverlang language artifacts, a Java SPL client backend, an agnostic and reusable SPL server written in Go and Prolog, and a JavaScript SPL client frontend.
