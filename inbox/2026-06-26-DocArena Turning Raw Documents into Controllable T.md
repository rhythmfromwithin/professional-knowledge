---
interest: medium
link: https://arxiv.org/abs/2606.26122
next_step: skim
priority: medium
slack_ts: '1782447546.908249'
source: cs.CV - Computer Vision
status: unread
title: 'DocArena: Turning Raw Documents into Controllable Training Environments for
  Document Search Agents'
---
# DocArena: Turning Raw Documents into Controllable Training Environments for Document Search Agents
> 原文: [https://arxiv.org/abs/2606.26122](https://arxiv.org/abs/2606.26122)

arXiv:2606.26122v1 Announce Type: new
Abstract: Recent methods train search agents via reinforcement learning from (question, answer, evidence) tuples without requiring expert trajectories. The tuples serve as the training environment, and whose properties directly shape what search strategies and generalization abilities the agent can develop. While prior works have made encouraging progress in improving training data quality, existing environments remain predominantly text-based and existing approaches can struggle to construct training environments that are controllable, scalable, and account for multimodal data. Given this, we propose DocArena, a fully automated data curation pipeline building on the practical need for multimodal document search and question-answering. It transforms raw document collections into training environments for search agents without any human annotation. The pipeline first structures and indexes documents through MLLM-based visual perception, then profiles and leverage the cross-page information distribution to construct reasoning-intensive QA pairs, as well as performs cascaded quality assurance operations via MLLM. We introduce DocArena-79K with QA pairs from 8,336 documents spanning 16 domains and 49 languages. We further design a Doc-Search agent infrastructure that decouples visual perception from the policy model, allowing text-based LLMs to serve as the reasoning backbone for multimodal document retrieval and QA. Under a unified evaluation framework where only the policy model differs, experiments on six multimodal document scenarios and seven text-based QA benchmarks show that agents trained on DocArena data achieve the best performance on both retrieval accuracy and QA quality. Further analysis on agent search behaviors confirms the effectiveness and controllability of the constructed training environment.
