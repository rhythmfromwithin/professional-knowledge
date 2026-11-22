---
interest: medium
link: https://arxiv.org/abs/2611.25218
next_step: skim
priority: low
slack_ts: '1795328175.983499'
source: cs.DB - Databases
status: unread
title: 'The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription
  with Manual Data Entry at Scale'
---
# The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription with Manual Data Entry at Scale
> 原文: [https://arxiv.org/abs/2611.25218](https://arxiv.org/abs/2611.25218)

arXiv:2611.25218v1 Announce Type: new
Abstract: How closely does machine transcription agree with manual double-entry data? We digitize the 1912 and 1921 editions of the American Medical Directory, a national register of US physicians with roughly 140,000 and 150,000 entries in the two volumes, and compare five machine-extraction workflows with a full-count double-entered manual transcription. Like many historical directories, the AMD is semi-structured rather than tabular, so errors arise from misreading the layout as well as the text. A script that parses commercial OCR text using rules written by coding agents recovers about 97 percent of manually transcribed records with similar precision, more than a multimodal language model workflow (gemini-2.0.flash) that reads the page images and the OCR text. When the two methods fail, they fail on partly overlapping sets of records, so reconciling their outputs raises both recall and precision to about 98 percent. An open-weight LLM pipeline run on a local GPU server falls between the parser and the multimodal workflow in recall, and replacing the commercial OCR model with an open-source alternative lowers its recall by only about 2 percentage points. As the manual transcription's own error rate is unknown, these rates measure agreement rather than accuracy. Direct processing charges for the commercial OCR and multimodal workflow were about 0.03 euro per page, compared with 14.70 euro per page for manual transcription.
