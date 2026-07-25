---
title: "AuthProbe: Specification-Driven, Multi-Identity Detection of Broken Object-Level Authorization in Recruitment API"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.20574
priority: low
status: unread
interest: medium
next_step: skim
---
# AuthProbe: Specification-Driven, Multi-Identity Detection of Broken Object-Level Authorization in Recruitment API
> 原文: [https://arxiv.org/abs/2607.20574](https://arxiv.org/abs/2607.20574)

arXiv:2607.20574v1 Announce Type: new
Abstract: Broken Object-Level Authorization (BOLA), also known as Insecure Direct Object Reference (IDOR), has topped the OWASP API Security ranking since 2019 and is the root cause of some of the largest exposures of applicant data in recruitment technology. The defining feature of this flaw class is that a malicious request is byte-for-byte indistinguishable from a legitimate one, which is precisely why web application firewalls and single identity scanners fail to catch it. We present AuthProbe, an open-source, black-box scanner that detects BOLA and IDOR in HTTP APIs by driving its tests from an OpenAPI specification and by acting under two or more identities that the operator controls. AuthProbe discovers, for each identity, the objects that identity legitimately owns, then attempts to read one identity's objects while authenticated as another and confirms a leak by comparing the response against a ground-truth fetch by the true owner. It also walks predictable identifiers to expose enumeration and reports missing authentication and existence oracles. The tool returns a severity-thresholded exit code and machine-readable reports so that it can gate a continuous integration build. On a synthetic recruitment API in which the McHire failure class is reproduced, AuthProbe detects every planted cross-identity read with no false positives on a hardened counterpart, and its running time grows linearly with the number of objects under test. AuthProbe is released under the Apache 2.0 license with an authorized-use guardrail.
