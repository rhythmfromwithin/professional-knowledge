---
interest: medium
link: https://arxiv.org/abs/2603.22355
next_step: skim
priority: medium
slack_ts: '1774493863.796379'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Demystifying Low-Rank Knowledge Distillation in Large Language Models: Convergence,
  Generalization, and Information-Theoretic Guarantees'
---
# Demystifying Low-Rank Knowledge Distillation in Large Language Models: Convergence, Generalization, and Information-Theoretic Guarantees
> 原文: [https://arxiv.org/abs/2603.22355](https://arxiv.org/abs/2603.22355)

arXiv:2603.22355v1 Announce Type: new
Abstract: Knowledge distillation has emerged as a powerful technique for compressing large language models (LLMs) into efficient, deployable architectures while preserving their advanced capabilities. Recent advances in low-rank knowledge distillation, particularly methods like Low-Rank Clone (LRC), have demonstrated remarkable empirical success, achieving comparable performance to full-parameter distillation with significantly reduced training data and computational overhead. However, the theoretical foundations underlying these methods remain poorly understood. In this paper, we establish a rigorous theoretical framework for low-rank knowledge distillation in language models. We prove that under mild assumptions, low-rank projection preserves the optimization dynamics, yielding explicit convergence rates of $O(1/\sqrt{T})$. We derive generalization bounds that characterize the fundamental trade-off between model compression and generalization capability, showing that the generalization error scales with the rank parameter as $O(r(m+n)/\sqrt{n})$. Furthermore, we provide an information-theoretic analysis of the activation cloning mechanism, revealing its role in maximizing the mutual information between the teacher's and student's intermediate representations. Our theoretical results offer principled guidelines for rank selection, mathematically suggesting an optimal rank $r^\* = O(\sqrt{n})$ where $n$ is the sample size. Experimental validation on standard language modeling benchmarks confirms our theoretical predictions, demonstrating that the empirical convergence, rank scaling, and generalization behaviors align closely with our bounds.
