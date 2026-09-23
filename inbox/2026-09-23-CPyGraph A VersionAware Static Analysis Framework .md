---
interest: medium
link: https://arxiv.org/abs/2609.25083
next_step: skim
priority: low
slack_ts: '1790137551.062129'
source: cs.CR - Cryptography and Security
status: unread
title: 'CPyGraph: A Version-Aware Static Analysis Framework for Native CPython Bytecode'
---
# CPyGraph: A Version-Aware Static Analysis Framework for Native CPython Bytecode
> 原文: [https://arxiv.org/abs/2609.25083](https://arxiv.org/abs/2609.25083)

arXiv:2609.25083v1 Announce Type: new
Abstract: Static analysis of Python packages must recover both program structure and object flow across first-class functions, dynamic dispatch, implicit protocol calls, exceptions, closures, and module execution. Native CPython bytecode provides the executable lowering of these behaviors, but its instruction, call, stack, and exception representations change across releases. This creates a need for a version-aware analysis foundation whose graph products share the same bytecode identities and semantics. We present CPyGraph, a C++ framework for package-level analysis of native CPython bytecode. Version- specific adapters expose stack, control, call, lexical, protocol, and exception semantics through a shared interface while preserving code-object identities and native bytecode offsets. An operand-stack-aware Andersen points- to analysis and call graph grow together to a fixed point. Their shared state supports exception-aware CFGs, block-level CDGs, and interprocedural DDGs, with optional function-level flow, context, and bounded path sensitivity. The framework also records unresolved dynamic behavior through typed coverage summaries. We evaluate CPyGraph with PYGBench, 201 package-level programs and 1,733 fixed candidates. On CPython 3.10, the default analysis reaches 91.40% candidate precision and 100% recall; complete sensitivity reaches 94.97% precision with the same recall. Across CPython 3.10-3.14, 1,328 of 1,334 version-invariant queries agree, and CPyGraph matches PyCG on its 112-program call-graph benchmark.
