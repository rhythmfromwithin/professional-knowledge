---
title: "Refining LLM-based Directed Test Input Generation via Runtime Value Feedback"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.07926
priority: low
status: unread
interest: medium
next_step: skim
---
# Refining LLM-based Directed Test Input Generation via Runtime Value Feedback
> 原文: [https://arxiv.org/abs/2608.07926](https://arxiv.org/abs/2608.07926)

arXiv:2608.07926v1 Announce Type: new
Abstract: LLM-based directed input generation techniques have shown promising effectiveness at producing target-reaching test inputs. However, due to the constraint of available code information and inherent unpredictability of LLM inference, reliable directed input generation requires mechanisms to ground the process in observed runtime behavior. We propose ReDig, a runtime feedback-guided refinement framework which adds a control loop around an LLM-based directed test input generation technique to refine the directed input generation with runtime values observed in prior target-missing test executions. In the case studies with Poppler and Libsndfile, we found that ReDig effectively derive runtime value feedback to diagnose why the previous test script failed to reach the target lines, and also effectively leverage given runtime value feedback to refine the test scripts in subsequent steps.
