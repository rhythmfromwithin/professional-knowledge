---
title: "Certifying Repeatable Entry-Replay Witnesses for COBOL-to-Java Migration"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.27272
priority: low
status: unread
interest: medium
next_step: skim
---
# Certifying Repeatable Entry-Replay Witnesses for COBOL-to-Java Migration
> 原文: [https://arxiv.org/abs/2610.27272](https://arxiv.org/abs/2610.27272)

arXiv:2610.27272v1 Announce Type: new
Abstract: Producing synthetic data for comparison testing a migrated COBOL application is a major challenge that agentic migrations face today. Our prior paper, the Agentic Method for Deterministic Validation of Legacy Code Migration, presents a deterministic oracle to facilitate such migrations, the Locksmith Loop. We now propose a novel method for achieving high branch and paragraph coverage through generated synthetic end-to-end test cases, by means of entry-replay test-case certification by observing the code execution trace on a surrogate COBOL program that mocks external interactions via a chronological external-operation tape. We applied our method to a very large COBOL program with 33,429 lines of code to generate 849 synthetic end-to-end test cases covering 2,973/3,806 source branches (78.1%) and 989/1,033 main-AST paragraphs (95.7%). Using the Locksmith Loop's projected-agreement validation, the generated Java code matched the COBOL surrogate on the specified observations across all 849 certified synthetic end-to-end test cases. During the campaign we detected 61 defects and fixed the Java generator accordingly. To test whether the coding agent could silently introduce business logic bugs, we seeded 450 defects into the Java code, such as deleted writes, deleted paragraph calls, and altered rounding, to verify how many of these would be detected by the gating methodology. The gate detected 47.6%, including all deleted writes and paragraph calls in executed code, but was unable to detect the rounding and precision defects.
