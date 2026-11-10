---
interest: medium
link: https://arxiv.org/abs/2611.08745
next_step: skim
priority: low
slack_ts: '1794293798.009809'
source: cs.CR - Cryptography and Security
status: unread
title: 'I Don''t Care How You Hide It, I Care What You Do: Runtime Detection of Malicious
  ML Models'
---
# I Don't Care How You Hide It, I Care What You Do: Runtime Detection of Malicious ML Models
> 原文: [https://arxiv.org/abs/2611.08745](https://arxiv.org/abs/2611.08745)

arXiv:2611.08745v1 Announce Type: new
Abstract: Pre-trained machine learning (ML) models shared through public platforms can be weaponized to execute malicious payloads during loading or inference. Existing scanners prove inadequate for detecting malicious models as they rely on static analysis and function denylists, support limited serialization formats, and miss attacks that replace denylisted functions with equivalent alternatives, exploit unsupported loading paths, or abuse legitimate framework APIs. To address this problem, we present ModelShield, the first runtime behavioral detection system for malicious ML models that attributes observed system-level behavior to specific model operations. It combines application-level instrumentation of ML framework APIs with eBPF-based syscall tracing, tracking model behavior across spawned threads and processes to separate model-triggered activity from environment noise. Attributed syscall sequences are classified using 195 detection patterns mapped to MITRE ATT&CK techniques. We implemented ModelShield to support 17 ML frameworks and 36 formats. On an independent dataset, it is the only evaluated tool to achieve zero false positives, with false negatives limited to payloads that produce no malicious runtime behavior. It detected all 29 published evasion variants spanning function substitution, loading-path obfuscation, and TensorFlow API abuse, where no existing scanner achieved complete coverage. Across 145,000 models scanned from public platforms, it captured 41 malicious models on Hugging Face, including a reverse-shell payload and a payload that performed host reconnaissance and outbound exfiltration. Among these, ModelScan, PickleScan, Fickling, and ModelAudit detected only 29%, 56%, 80%, and 93%, respectively. Despite runtime overhead, ModelShield has a median analysis time of 12.3 seconds, with 90% of scans completing within 35.5 seconds, making it practical for hub-scale screening.
