---
interest: medium
link: https://arxiv.org/abs/2606.18310
next_step: skim
priority: low
slack_ts: '1781759640.545119'
source: cs.CR - Cryptography and Security
status: unread
title: Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based
  RAG Systems
---
# Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems
> 原文: [https://arxiv.org/abs/2606.18310](https://arxiv.org/abs/2606.18310)

arXiv:2606.18310v1 Announce Type: new
Abstract: Injecting malicious knowledge into retrieval-augmented generation (RAG) systems can manipulate retrieved evidence and mislead downstream generation, posing a serious security threat for AI applications. Existing RAG injection attacks mainly rely on manipulating external knowledge bases, such as crafting malicious corpus. However, the synthetic text crafted by such data-centric methods could be detectable, leading to the failure of attacks. Beyond corpus manipulation, open-source retrievers are increasingly exposing RAG systems to model-centric attacks. In this paper, we propose conflict-aware retriever editing, i.e., CAREATTACK, a model-centric retriever attack framework for malicious knowledge injection in RAG. Specifically, CAREATTACK consists two stages of conflict-aware retriever editing and attack-preserving anchor repair. Conflict-aware retriever editing adapts efficient closed-form parameter editing to the dense retrieval model, promoting malicious knowledge above benign competing passages and resolving potential parameter conflicts through graph-based conflict detection and parameter editing projection. Then, attack-preserving anchor repair performs lightweight calibration on the edited retriever to further eliminate the impact on non-target prompts while preserving the attack effectiveness for target prompts. We instantiate CAREATTACK on Qwen3-Embedding-0.6B and BGE-M3, and conduct evaluation on three benchmark datasets. Experimental results demonstrate our method substantially promote malicious passages into the retrieved knowledge of RAG systems and can perform attacks for batches of target prompts and passages, given the access of retrieval model parameters. Since most RAG systems are built upon open-source retrieval models, this work reveals a practical attack surface in RAG systems. Codes are public accessible at https://anonymous.4open.science/r/CareAttack-3F1C.
