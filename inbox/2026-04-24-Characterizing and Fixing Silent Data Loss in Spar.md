---
title: "Characterizing and Fixing Silent Data Loss in Spark-on-AWS-Lambda with Open Table Formats"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.20081
priority: medium
status: unread
interest: medium
next_step: skim
---
# Characterizing and Fixing Silent Data Loss in Spark-on-AWS-Lambda with Open Table Formats
> 原文: [https://arxiv.org/abs/2604.20081](https://arxiv.org/abs/2604.20081)

arXiv:2604.20081v1 Announce Type: new
Abstract: AWS Lambda terminates containers with an uncatchable SIGKILL signal when a function exceeds its configured timeout. When a Spark-on-AWS-Lambda (SoAL) job is killed between Phase 1 (data upload) and Phase 2 (metadata commit) of a write, the result is silent data loss: orphaned Parquet files accumulate on S3 while the table's committed state remains unchanged and standard monitoring raises no alert. We characterize this vulnerability across Delta Lake and Apache Iceberg through 860 controlled kill-injection experiments at three dataset sizes. A SIGKILL landing in the inter-phase gap produced silent data loss in 100% of trials for both formats. We then present SafeWriter, a language-level wrapper that arms a watchdog thread 30 seconds before the Lambda timeout, triggers a format-native rollback via SQL, and records a checkpoint document on S3. SafeWriter converted every tested kill scenario into a clean, detectable rollback with under 100 ms added to normal write paths.
