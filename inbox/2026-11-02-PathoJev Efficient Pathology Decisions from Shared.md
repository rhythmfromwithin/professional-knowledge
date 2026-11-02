---
interest: medium
link: https://arxiv.org/abs/2610.40752
next_step: skim
priority: medium
slack_ts: '1793597891.069029'
source: cs.CV - Computer Vision
status: unread
title: 'PathoJev: Efficient Pathology Decisions from Shared Visual Context'
---
# PathoJev: Efficient Pathology Decisions from Shared Visual Context
> 原文: [https://arxiv.org/abs/2610.40752](https://arxiv.org/abs/2610.40752)

arXiv:2610.40752v1 Announce Type: new
Abstract: Pathology workflows require multiple visual judgments about the same slide, from identifying tumor type to assessing grade and invasion. Generating and parsing a separate textual response for each structured question adds latency between visual evidence and usable decisions. Building on the System One paradigm, we introduce PathoJev, a pathology model that directly predicts answer probabilities for whole-slide and region-level assessment. PathoJev encodes each slide once and evaluates independent question suffixes in batches over the shared visual context. Reusing the hybrid backbone's recurrent states further limits the computation that grows with slide-context length for each additional question. Across three whole-slide benchmarks, the 9B and 27B models achieve mean accuracies of 77.2% and 78.1%, exceeding SlideChat by 5.4 and 6.3 percentage points. Both scales also maintain competitive accuracy on five ROI benchmarks. On WSI-Bench, the 9B model runs 9.1x faster than SlideChat. Shared context accelerates eight-question workloads by 6.9x and 5.9x over separate prefix encoding, rising to 11.2x and 8.9x for 64 questions. These results provide a reusable probabilistic interface for combining multiple visual judgments in whole-slide and local tissue assessment. Code: https://github.com/ChyaZhang/PathoJev.
