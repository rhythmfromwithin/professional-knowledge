---
interest: medium
link: https://arxiv.org/abs/2611.17770
next_step: skim
priority: low
slack_ts: '1794808695.949089'
source: cs.DB - Databases
status: unread
title: 'Bridge: Database-Grounded Interactive Disambiguation for Text-to-SQL'
---
# Bridge: Database-Grounded Interactive Disambiguation for Text-to-SQL
> 原文: [https://arxiv.org/abs/2611.17770](https://arxiv.org/abs/2611.17770)

arXiv:2611.17770v1 Announce Type: new
Abstract: Ambiguity remains a persistent challenge in text-to-SQL, where an underspecified natural-language question may admit multiple plausible SQL interpretations. Recent work attempts to recover the user's intended interpretation through iterative clarification, but typically relies heavily on LLM parametric knowledge for ad hoc reasoning, leading to limited ambiguity-resolution effectiveness and high LLM cost. We further observe that many ambiguity errors stem from ambiguous column grounding, which remains poorly handled. Therefore, we propose Bridge, a database-grounded disambiguation framework built on an existing iterative protocol. Bridge supplies the LLM's ambiguity detection with offline-distilled knowledge about potential ambiguity relations among columns in the target database. Offline, Bridge constructs a Column Ambiguity Graph by first identifying potentially ambiguous column pairs using complementary database-grounded signals, followed by LLM-based verification. Online, columns and values mentioned in a previous incorrect SQL prediction are used as anchors to retrieve alternatives from the Column Ambiguity Graph and an offline-constructed value similarity index, respectively. The results are integrated for further pruning and consolidated for subsequent ambiguity detection. Extensive experiments on BIRD-dev without the benchmark-provided evidence show that, at comparable LLM cost, Bridge outperforms the strongest baseline by 11.60% in execution accuracy and improves the recall and precision of column usage in the final SQL by 5.25% and 12.37%, respectively.
