---
interest: medium
link: https://arxiv.org/abs/2604.15390
next_step: skim
priority: low
slack_ts: '1776742299.819079'
source: cs.SE - Software Engineering
status: unread
title: Analyzing Chain of Thought (CoT) Approaches in Control Flow Code Deobfuscation
  Tasks
---
# Analyzing Chain of Thought (CoT) Approaches in Control Flow Code Deobfuscation Tasks
> 原文: [https://arxiv.org/abs/2604.15390](https://arxiv.org/abs/2604.15390)

arXiv:2604.15390v1 Announce Type: new
Abstract: Code deobfuscation is the task of recovering a readable version of a program while preserving its original behavior. In practice, this often requires days or even months of manual work with complex and expensive analysis tools. In this paper, we explore an alternative approach based on Chain-of-Thought (CoT) prompting, where a large language model is guided through explicit, step-by-step reasoning tailored for code analysis. We focus on control flow obfuscation, including Control Flow Flattening (CFF), Opaque Predicates, and their combination, and we measure both structural recovery of the control flow graph and preservation of program semantics. We evaluate five state-of-the-art large language models and show that CoT prompting significantly improves deobfuscation quality compared with simple prompting. We validate our approach on a diverse set of standard C benchmarks and report results using both structural metrics for control flow graphs and semantic metrics based on output similarity. Among the tested models and by applying CoT, GPT5 achieves the strongest overall performance, with an average gain of about 16% in control-flow graph reconstruction and about 20.5% in semantic preservation across our benchmarks compared to zero-shot prompting. Our results also show that model performance depends not only on the obfuscation level and the chosen obfuscator but also on the intrinsic complexity of the original control flow graph. Collectively, these findings suggest that CoT-guided large language models can serve as effective assistants for code deobfuscation, providing improved code explainability, more faithful control flow graph reconstruction, and better preservation of program behavior while potentially reducing the manual effort needed for reverse engineering.
