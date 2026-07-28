---
interest: medium
link: https://arxiv.org/abs/2607.21958
next_step: skim
priority: medium
slack_ts: '1785208715.464919'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Efficient Online LLM Watermark Detection via Rao-Blackwellized E-Processes
---
# Efficient Online LLM Watermark Detection via Rao-Blackwellized E-Processes
> 原文: [https://arxiv.org/abs/2607.21958](https://arxiv.org/abs/2607.21958)

arXiv:2607.21958v1 Announce Type: new
Abstract: As large language models (LLMs) are increasingly deployed, reliable and efficient mechanisms for distinguishing AI-generated text from human-written content have become essential. Statistical watermarking has emerged as a promising solution, yet most existing methods are typically fixed-horizon procedures, precluding valid early stopping in streaming generation. In this paper, we develop an efficient online watermark detection framework with anytime-valid inference based on Rao-Blackwellized e-processes, enabling recursive token-level evidence updates without storing the full history. In particular, we instantiate the framework for the Gumbel-max watermark and reduce the original token-level dependence testing problem to a pivot-induced sequential testing problem with an explicit null distribution. Theoretically, we prove anytime-valid Type I error control under arbitrary optional stopping and establish positive asymptotic log-growth under watermarking, implying consistency of the proposed stopping rules. Simulations and experiments on real LLM-generated text demonstrate efficient online detection with rigorous anytime-valid guarantees.
