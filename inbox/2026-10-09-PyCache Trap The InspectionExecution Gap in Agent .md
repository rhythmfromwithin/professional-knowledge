---
title: "PyCache Trap: The Inspection-Execution Gap in Agent Skill Scanners"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.10612
priority: low
status: unread
interest: medium
next_step: skim
---
# PyCache Trap: The Inspection-Execution Gap in Agent Skill Scanners
> 原文: [https://arxiv.org/abs/2610.10612](https://arxiv.org/abs/2610.10612)

arXiv:2610.10612v1 Announce Type: new
Abstract: Agent skills combine instructions with executable resources, giving third-party packages access to an agent's runtime. Existing skill scanners inspect documentation and visible source, but Python may execute a bundled bytecode cache with different behavior. We study this gap between inspection and execution through PyCache Trap, which pairs benign source with a substituted cache accepted by the loader and connects it to a task-relevant invocation. Scanner-guided rewriting changes the invocation wording while preserving the cache body, separating package admission from recognition of the concealed behavior. Across 100 skills and seven scanners, PyCache Trap achieves 94-100% attack success, with no semantic recognition of the cache-resident behavior. We propose execution-aware validation (EAV) to connect inspected instructions, scripts, imports, and runtime artifacts in a typed execution graph. EAV combines grounded behavioral analysis with trusted reproduction of compiled artifacts. It detects all 100 evaluated source-present cache substitutions and reaches 92.8% Recall at 10.0% FPR across five attack families and 200 benign skills. The results support checking the executable artifacts a runtime can select as part of skill admission, within the supported loaders and code-object normalization. The code is released at https://github.com/leo0481/PyCacheTrap.
