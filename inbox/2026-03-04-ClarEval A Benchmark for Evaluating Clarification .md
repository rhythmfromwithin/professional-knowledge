---
title: "ClarEval: A Benchmark for Evaluating Clarification Skills of Code Agents under Ambiguous Instructions"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.00187
priority: low
status: unread
---
# ClarEval: A Benchmark for Evaluating Clarification Skills of Code Agents under Ambiguous Instructions
> 原文: [https://arxiv.org/abs/2603.00187](https://arxiv.org/abs/2603.00187)

arXiv:2603.00187v1 Announce Type: new
Abstract: To integrate seamlessly into real-world software engineering, Code Agents must evolve from passive instruction followers into proactive collaborative partners. However, current evaluation paradigms predominantly reward "guessing" user intent under ideal conditions, neglecting the agent's ability to align with users through dialogue--a critical trait for collaborative intelligence. In this work, we propose a paradigm shift in evaluation to drive this transition. We introduce ClarEval, a framework designed to assess an agent's "Collaborative Quotient" by simulating the inherent ambiguity of human communication. By systematically injecting three types of realistic ambiguity (missing goals, premises, and ambiguous terminology) into standard tasks, we force agents to step out of their "generator" role and engage in requirement elicitation. To quantify this capability, we propose a metric suite led by Average Turns to Clarify (ATC) and Key Question Coverage (KQC), which measure not just the correctness of the generated code, but the efficiency and precision of the collaboration. Our experiments on eleven state-of-the-art agents reveal a stark reality: while models like GPT-5-Coder excel at coding, they often lack the strategic communication skills required for efficient partnership. ClarEval thus serves as a crucial roadmap for bridging the gap between strong coders and capable collaborators.The code is available at https://github.com/JialinLi13/ClarEval
