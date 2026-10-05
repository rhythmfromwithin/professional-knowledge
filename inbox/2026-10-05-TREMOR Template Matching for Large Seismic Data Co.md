---
title: "TREMOR: Template Matching for Large Seismic Data Collections"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.02534
priority: low
status: unread
interest: medium
next_step: skim
---
# TREMOR: Template Matching for Large Seismic Data Collections
> 原文: [https://arxiv.org/abs/2610.02534](https://arxiv.org/abs/2610.02534)

arXiv:2610.02534v1 Announce Type: new
Abstract: Seismic station networks continuously record the ground velocity at several locations on earth in the form of waveform data series, which seismologists analyze to detect various kinds of geophysical events, including earthquakes. Some of these events are of particular interest: they are called templates and are used to search the seismic data collections for matching, similar events. This is known as template matching, and is a fundamental task in seismology, serving as the backbone for various seismic analyses. However, template matching requires extensive processing times, especially for seismic collections that exceed the memory capacity of a single machine. This poses a significant challenge to seismologists and is becoming worse as the seismological datasets continue to grow in size. In this paper, we introduce TREMOR, a distributed data series processing framework for template matching, designed to efficiently handle large waveform collections. We apply TREMOR to two representative real-world seismic use cases for template matching and, through an extensive experimental evaluation, we demonstrate its efficiency, with TREMOR being up to 12x faster than the best competing method, while returning the same, exact results.
