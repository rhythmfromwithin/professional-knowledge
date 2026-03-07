---
title: "Deterministic Preprocessing and Interpretable Fuzzy Banding for Cost-per-Student Reporting from Extracted Records"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.04905
priority: low
status: unread
---
# Deterministic Preprocessing and Interpretable Fuzzy Banding for Cost-per-Student Reporting from Extracted Records
> 原文: [https://arxiv.org/abs/2603.04905](https://arxiv.org/abs/2603.04905)

arXiv:2603.04905v1 Announce Type: new
Abstract: Administrative extracts are often exchanged as spreadsheets and may be read as reports in their own right during budgeting, workload review, and governance discussions. When an exported workbook becomes the reference snapshot for such decisions, the transformation can be checked by recomputation against a clearly identified input.
A deterministic, rule-governed, file-based workflow is implemented in cad\_processor.py. The script ingests a Casual Academic Database (CAD) export workbook and aggregates inclusive on-costs and student counts into subject-year and school-year totals, from which it derives cost-per-student ratios. It writes a processed workbook with four sheets: Processing Summary (run record and counters), Trend Analysis (schoolyear cost-per-student matrix), Report (wide subject-level table), and Fuzzy Bands (per-year anchors, membership weights, and band labels). The run record includes a SHA-256 hash of the input workbook bytes to support snapshot-matched recomputation.
For within-year interpretation, the workflow adds a simple fuzzy banding layer that labels finite, positive school-year cost-per-student values as Low, Medium, or High. The per-year anchors are the minimum, median, and maximum of the finite, positive ratios. Membership weights are computed using left-shoulder, triangular, and right-shoulder functions, with deterministic tie-breaking in a fixed priority order (Medium, then Low, then High). These weights are treated as decision-support signals rather than probabilities.
A worked example provides a reproducible calculation of a band assignment from the reported anchors and ratios. Supplementary material includes a claim-to-evidence matrix, a reproducibility note, and a short glossary that links selected statements to code and workbook artefacts.
