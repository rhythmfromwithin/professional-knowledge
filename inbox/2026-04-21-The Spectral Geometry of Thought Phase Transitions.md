---
interest: medium
link: https://arxiv.org/abs/2604.15350
next_step: skim
priority: high
slack_ts: '1776742311.060489'
source: cs.LG - Machine Learning
status: unread
title: 'The Spectral Geometry of Thought: Phase Transitions, Instruction Reversal,
  Token-Level Dynamics, and Perfect Correctness Prediction in How Transformers Reason'
---
# The Spectral Geometry of Thought: Phase Transitions, Instruction Reversal, Token-Level Dynamics, and Perfect Correctness Prediction in How Transformers Reason
> 原文: [https://arxiv.org/abs/2604.15350](https://arxiv.org/abs/2604.15350)

arXiv:2604.15350v1 Announce Type: new
Abstract: We discover that large language models exhibit \emph{spectral phase transitions} in their hidden activation spaces when engaging in reasoning versus factual recall. Through systematic spectral analysis across \textbf{11 models} spanning \textbf{5 architecture families} (Qwen, Pythia, Phi, Llama, DeepSeek-R1), we identify \textbf{seven} core phenomena: (1)~\textbf{Reasoning Spectral Compression} -- 9/11 models show significantly lower $\alpha$ for reasoning ($p < 0.05$), with larger effects in stronger models; (2)~\textbf{Instruction Tuning Spectral Reversal} -- base models show reasoning $\alpha < $ factual $\alpha$, while instruction-tuned models reverse this relationship; (3)~\textbf{Architecture-Dependent Generation Taxonomy} -- prompt-to-response shifts partition into expansion, compression, and equilibrium regimes; (4)~\textbf{Spectral Scaling Law} -- $\alpha\_\text{reasoning} \propto -0.074 \ln N$ across 4 Qwen base models ($R^2 = 0.46$); (5)~\textbf{Token-Level Spectral Cascade} -- per-token alpha tracking reveals local synchronization that decays exponentially with layer distance, and is weaker for reasoning than factual tasks; (6)~\textbf{Reasoning Step Spectral Punctuation} -- phase-transition signatures align with reasoning step boundaries; and (7)~\textbf{Spectral Correctness Prediction} -- spectral $\alpha$ alone achieves AUC $= 1.000$ (Qwen2.5-7B, late layers) and mean AUC $= 0.893$ across 6 models in predicting correctness \emph{before} the final answer is generated. Together, these findings establish a comprehensive \emph{spectral theory of reasoning} in transformers, revealing that the geometry of thought is universal in direction, architecture-specific in dynamics, and predictive of outcome.
