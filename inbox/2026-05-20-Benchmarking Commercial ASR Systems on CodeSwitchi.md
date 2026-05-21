---
interest: medium
link: https://arxiv.org/abs/2605.19069
next_step: skim
priority: high
slack_ts: '1779337380.827689'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Benchmarking Commercial ASR Systems on Code-Switching Speech: Arabic, Persian,
  and German'
---
# Benchmarking Commercial ASR Systems on Code-Switching Speech: Arabic, Persian, and German
> 原文: [https://arxiv.org/abs/2605.19069](https://arxiv.org/abs/2605.19069)

arXiv:2605.19069v1 Announce Type: new
Abstract: Code-switching -- the natural alternation between two languages within a single utterance -- represents one of the most challenging and under-studied conditions for automatic speech recognition (ASR). Existing commercial ASR benchmarks predominantly evaluate clean, monolingual audio and report a single Word Error Rate (WER) figure that tells practitioners little about real-world multilingual performance. We present a benchmark evaluating five commercial ASR providers across four language pairs: Egyptian Arabic--English, Saudi Arabic (Najdi/Hijazi)--English, Persian (Farsi)--English, and German--English. Each dataset comprises 300 samples selected by a two-stage pipeline: a heuristic filter scoring transcripts on five structural code-switching signals, followed by a GPT-4o and Gemini 1.5 Pro ensemble scoring candidates across six linguistic dimensions. This pipeline reduces LLM scoring costs by approximately 91\% relative to exhaustive scoring. We evaluate the systems on both WER and BERTScore, arguing that BERTScore is a more reliable metric for Arabic and Persian pairs where transliteration variance causes WER to penalise semantically correct transcriptions. ElevenLabs Scribe v2 achieves the lowest WER across all four language pairs (13.2% overall; 13.1% on Egyptian Arabic) and leads on BERTScore (0.936 overall). We further demonstrate that difficulty-stratified analysis reveals performance gaps masked by aggregate averages, and that BERT embedding projections confirm semantic proximity between reference and hypothesis despite surface-level script differences. The benchmarking dataset is publicly available at https://huggingface.co/datasets/Perle-ai/ASR\_Code\_Switch.
