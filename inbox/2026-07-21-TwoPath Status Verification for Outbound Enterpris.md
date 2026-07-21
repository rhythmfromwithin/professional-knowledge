---
title: "Two-Path Status Verification for Outbound Enterprise Messaging Pipelines: Webhook and Scheduled Polling Fallback Architecture"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2607.15529
priority: low
status: unread
interest: medium
next_step: skim
---
# Two-Path Status Verification for Outbound Enterprise Messaging Pipelines: Webhook and Scheduled Polling Fallback Architecture
> 原文: [https://arxiv.org/abs/2607.15529](https://arxiv.org/abs/2607.15529)

arXiv:2607.15529v1 Announce Type: new
Abstract: Outbound enterprise messaging pipelines face a fundamental reliability challenge: delivery status callbacks (webhooks) from messaging providers are subject to network failures, endpoint unavailability, and provider-side retry exhaustion, resulting in stale status records in the CRM system of record. A naive single-path architecture that relies exclusively on webhooks leaves a population of messages permanently in an intermediate state when callbacks fail. This paper presents a two-path status verification architecture, generalized from patterns observed in production CRM-native messaging systems built on multi-tenant platform-as-a-service infrastructure. The primary path uses a real-time webhook received by a REST endpoint, which publishes an internal event for asynchronous record update. The fallback path uses a configurable scheduled polling job that detects records still in transitional status after a configurable interval and queries the provider's status API directly to reconcile state. We describe the event-driven primary path, the scheduler-based fallback, deduplication via idempotent upsert, the sync failure detection mechanism, and the platform resource-limit considerations that shape each design decision.
