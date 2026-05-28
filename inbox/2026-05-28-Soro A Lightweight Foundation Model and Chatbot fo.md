---
title: "Soro: A Lightweight Foundation Model and Chatbot for Tajik"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.27379
priority: high
status: unread
interest: medium
next_step: skim
---
# Soro: A Lightweight Foundation Model and Chatbot for Tajik
> 原文: [https://arxiv.org/abs/2605.27379](https://arxiv.org/abs/2605.27379)

arXiv:2605.27379v1 Announce Type: new
Abstract: We present Soro, a family of Tajik-specialized conversational large language models (LLMs) designed for real-world deployment under tight compute and connectivity constraints in Tajikistan. Starting from open-weight Gemma 3 checkpoints, we perform Tajik-only continual pretraining on a curated 1.9-billion-token corpus spanning filtered web text, PDF documents, and curriculum-aligned educational materials, followed by supervised instruction tuning on 40K Tajik teacher-style examples. To enable rigorous evaluation despite the limited coverage of Tajik in standard benchmarks, we introduce a suite of Tajik benchmarks covering general knowledge, linguistic competence, and school- and university entrance-exam domains, and we open-source them on Hugging Face. Across these Tajik benchmarks, Soro substantially outperforms same-size Gemma 3 baselines while retaining strong English performance on standard datasets. We further show that FP8 and INT4 quantization of Soro preserves most Tajik-language gains while reducing memory requirements for edge deployment, supporting an ongoing education-sector pilot and planned scale-out across schools in Tajikistan.
