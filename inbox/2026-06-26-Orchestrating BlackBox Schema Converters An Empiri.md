---
interest: medium
link: https://arxiv.org/abs/2606.26180
next_step: skim
priority: low
slack_ts: '1782447551.610549'
source: cs.SE - Software Engineering
status: unread
title: 'Orchestrating Black-Box Schema Converters: An Empirical Study of Automated,
  Quality-Ranked Conversion Across Heterogeneous Schema Languages'
---
# Orchestrating Black-Box Schema Converters: An Empirical Study of Automated, Quality-Ranked Conversion Across Heterogeneous Schema Languages
> 原文: [https://arxiv.org/abs/2606.26180](https://arxiv.org/abs/2606.26180)

arXiv:2606.26180v1 Announce Type: new
Abstract: Modern software systems routinely need the same data model in several schema languages: a model may exist as JSON Schema for a web API, as XSD for data exchange, and as SHACL for a knowledge graph. Keeping these representations consistent as the model evolves is a recurring construction and maintenance burden, because converters between schema languages are hard to find, scattered across ecosystems, of uneven quality, and frequently lossy. We study, empirically, to what extent such imperfect, heterogeneous converters can be orchestrated into automated, reproducible, and quality-ranked conversions, and where the current converter landscape reaches its limits. Our approach models schema languages as nodes and converters, treated as black boxes, as directed edges, so that conversions become paths that are discovered, executed, ranked, and reported with full per-step provenance, with failures handled by trying alternatives. We realize it as the open-source Schema Conversion Orchestrator, integrate it into MetaConfigurator, and evaluate it on 60 conversion tasks built from real-world schemas across five schema languages, using agent-assisted, human-reviewed quality annotations. Orchestration surfaces a usable result for 43 of 60 tasks; the remaining failures localize concrete gaps in the converter landscape. We discuss implications for tool builders and for measuring conversion quality.
