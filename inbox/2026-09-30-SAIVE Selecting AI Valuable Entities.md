---
title: "SAIVE: Selecting AI Valuable Entities"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.36512
priority: low
status: unread
interest: medium
next_step: skim
---
# SAIVE: Selecting AI Valuable Entities
> 原文: [https://arxiv.org/abs/2609.36512](https://arxiv.org/abs/2609.36512)

arXiv:2609.36512v1 Announce Type: new
Abstract: Data lakes store large amounts of telemetry, with logs from network sensors, hosts, and applications containing possibly hundreds of fields for every event. Large enterprises are then left with data lakes that cannot be analyzed efficiently with AI. Aggregate analysis looks at persistent shifts in behavior over time. Many of the fields and columns in data lakes are not useful as they do not contain information that is sufficiently diverse or concentrated to support AI analysis. SAIVE is a simple method for examining a few rows in a large table and applies a histogram of histograms filtering criterion to select the fields that for AI analysis is more likely to yield useful results. This paper provides a principled foundation for the SAIVE heuristics by assuming of a Zipf-Mandelbrot power-law distribution of the underlying data. Constraining the Zipf-Mandelbrot exponent alpha to a reasonable range provides a a practical, cheap, expert-free filter for selecting AI valuable entities in large data sets.
