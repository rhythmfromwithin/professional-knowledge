---
title: "SecureMCP: A Policy-Enforced LLM Data Access Framework for AIoT Systems via Model Context Protocol"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.05260
priority: low
status: unread
interest: medium
next_step: skim
---
# SecureMCP: A Policy-Enforced LLM Data Access Framework for AIoT Systems via Model Context Protocol
> 原文: [https://arxiv.org/abs/2605.05260](https://arxiv.org/abs/2605.05260)

arXiv:2605.05260v1 Announce Type: new
Abstract: The deployment of Large Language Model (LLM)-generated SQL queries in Artificial Intelligence of Things (AIoT) systems introduces critical security risks, as prompt injection attacks can manipulate LLMs into producing unauthorized queries that expose sensitive data or execute destructive operations. Existing NL2SQL research focuses on query accuracy, while MCP server implementations provide only SQL-level protections without fine-grained role-based access control. This paper proposes SecureMCP, a policy-enforced LLM data access framework integrating Role-Based Access Control (RBAC) with an MCP server to establish multi-layer defense for LLM-generated SQL execution. The framework incorporates five defense modules -- check\_policy for table-and-column-level RBAC, explain\_gate for cost-explosive query blocking, SQL Interceptor for dangerous pattern detection, Risk Level Filter for SQL risk classification, and DB Isolation for cross-database restriction -- operating in a sequential fail-closed pipeline mapped to six prompt injection types grounded in the OWASP Top 10 for LLM Applications. We evaluate SecureMCP on the IoT-SQL dataset (11 tables, 173 columns, 239,398 records) using Qwen3-8B. Experiment A demonstrates that defense modules preserve execution accuracy, with EX-in-ALLOW remaining within 65.1%-76.4% across four RBAC roles, matching the unprotected baseline of 63.8%. Experiment B shows that SecureMCP achieves 82.3% Policy Compliance on 2,400 adversarial queries, with genuine defense failures limited to 3.4%. The defense-in-depth analysis reveals check\_policy accounts for 78.7% of blocks, while secondary modules contribute an additional 17.5 percentage-point improvement. The Injection Incorporation Rate of 72.5% confirms high LLM susceptibility, establishing the necessity of external policy enforcement.
