---
interest: medium
link: https://medium.com/airbnb-engineering/safeguarding-dynamic-configuration-changes-at-scale-5aca5222ed68?source=rss
next_step: skim
slack_ts: '1773196766.572269'
source: Airbnb Engineering
title: Safeguarding Dynamic Configuration Changes at Scale
----53c7c27702d5---4
priority: medium
status: unread
---
# Safeguarding Dynamic Configuration Changes at Scale
> 原文: [https://medium.com/airbnb-engineering/safeguarding-dynamic-configuration-changes-at-scale-5aca5222ed68?source=rss----53c7c27702d5---4](https://medium.com/airbnb-engineering/safeguarding-dynamic-configuration-changes-at-scale-5aca5222ed68?source=rss----53c7c27702d5---4)

#### **How Airbnb ships dynamic config changes safely and reliably**

![](https://cdn-images-1.medium.com/max/1024/1*v2VDklQn1NHAx-MiR8DYMQ.png)

By [Cosmo Qiu](https://www.linkedin.com/in/cosmo-qiu/), [Bo Teng](https://www.linkedin.com/in/bo-t-b04912238/), [Siyuan Zhou](https://www.linkedin.com/in/siyuan-zhou-85ba8057/), [Ankur Soni](https://www.linkedin.com/in/ankursoni/), [Willis Harvey](https://www.linkedin.com/in/willish/)

Dynamic configuration is a core infrastructure capability in modern systems. It allows developers to change runtime behavior without restarting or redeploying services, even as the number of services and requests grows. In practice, that might mean rolling out a new address form for a region launch, tightening an authorization rule, or adjusting timeouts when a dependency is slow.

Like any powerful tool, dynamic configuration is a double-edged sword. While it enables fast iteration and rapid incident response, a bad change can cause regressions or even outages. This is a common challenge across the industry: balancing developer flexibility with system reliability.

In this post, we will outline the expectations of a modern dynamic configuration platform, then walk through the high-level architecture of Airbnb’s dynamic config platform and how its core components work together to enable safe, flexible config changes.

### Modern config platform essentials

As Airbnb’s business grows, our expectations for the dynamic config platform have evolved over time through our own learnings as well as industry best practices. These shape our view of what a good dynamic config platform should provide, including:

* **A coherent experience for config management**: The platform provides a streamlined, end-to-end experience for defining, reviewing, testing, and rolling out config changes. It covers the most common needs out of the box with rich built-in features, while still offering escape hatches for edge cases.
* **Strong reliability, availability and safety guarantees**: All config changes are validated, reviewed, and rolled out progressively, with clear ownership and well-defined access control. Treating config as code is a key focus: config changes are versioned, reviewed, and auditable like service code, but remain dynamic at runtime. The platform itself must be highly available so that services can reliably fetch and apply configs. Changes should be observable, with support for fast rollbacks when needed.
* **Safe testing in isolated environments**: Developers can validate config changes in isolated local or canary environments before they reach production.
* **Flexible multi-tenant support**: In a multi-tenant platform, different tenants have different risk profiles. The platform should allow config owners to customize how their configs behave per tenant, including deployment triggers, guardrails, and rollout strategy (for example, AWS zone or Kubernetes pod percentage-based rollouts).
* **Fast and controlled incident response**: During an incident, responders can ship emergency configs as needed with clear auditability. The platform also provides observability for config changes, so incident responders can tell what changed, who was affected, when the change was made, and who made the change. This enables them to effectively identify the culprit and take action.

### High-level architecture

At Airbnb, Sitar is the internal name for our dynamic config platform. It provides a common way for teams to manage runtime behavior safely. At a high level, Sitar has four main parts: a developer-facing layer, a control plane, a data plane, and the clients and agents that run alongside application code.

![](https://cdn-images-1.medium.com/max/1024/1*Bv62zjTLRJRCKNdcTgiazA.jpeg)

The developer-facing layer is where config changes are created and reviewed. By default, configs are managed through a Git-based workflow, while a few exceptions are managed in the web interface (sitar-portal), which is also used for admin operations such as emergency deployments.

The control plane is responsible for orchestrating config changes. It enforces schema validation, ownership, and access control, and decides how each change should be rolled out: for example, which environments or AWS zone to target, what percentage of Kubernetes pods to start with, and how to progress the rollout over time. The control plane also specifies how to roll back the changes when needed, and supports routing in-flight configs to specific environments or slices of subscribers for fast testing.

The data plane provides scalable storage and efficient distribution of configs. It acts as the source of truth for config values and versions, and propagates updates to services reliably, consistently, and quickly.

On the product services side, an agent sidecar running alongside each service fetches the subscribed configs from the data plane and maintains a local cache. Client libraries inside the service then read from this cache and expose configs to application logic with fast, in-process access and optional fallbacks.

Putting these together, a typical change starts from a Git flow, proceeds through control-plane validation and rollout decisions, into the data plane for distribution, and finally to agents and client libraries that apply the config updates to application logic.

### Key design choices

In this section, we highlight a few key design choices that shape how the platform looks and is operated.

#### **Configs as code with a Git-based workflow**

Config changes are by default managed by a Git-centric workflow. We use GitHub as the primary interface for managing configs, because we have an established and responsive internal team to manage GitHub Enterprise. GitHub integrates naturally with our existing CI/CD tooling, so we can reuse rich validation and deployment pipelines without re-inventing the wheel. This approach gives developers a consistent experience to make code changes: open a pull request, get reviews, merge, and deploy. GitHub also brings additional benefits such as mandatory reviewers, review and approval flows, and a change history. Configs under the same theme are grouped into tenants, with clear owners, customizable tests, and a dedicated CD pipeline.

While the Git-based flow is the default, we keep a UI portal for teams that prefer a portal-based experience and as a shortcut for specific operational needs, such as fast emergency config updates that can bypass the normal CI/CD pipeline.

#### **Staged rollouts and fast rollbacks**

When a change is proposed, schema validation (checking that the config matches the expected structure and types) and other automated checks run in CI. The change is always reviewed and approved before rollout.

Once merged in the main branch, the control plane performs a staged rollout where the change is first deployed to a limited scope, then gradually expanded to a larger scope if things look good. At each stage of this rollout, the change is evaluated, the author and the stakeholders are notified if regressions are detected, and a fast rollback can be triggered if needed. Staged rollouts can greatly reduce the blast radius of bad changes and improve the overall reliability of the platform.

#### **Separated control and data planes**

We separate the “decide” and “deliver” responsibilities. The control plane focuses on validation, authorization, and rollout decisions, while the data plane focuses on storing configs and distributing them reliably at scale. This separation allows us to evolve rollout strategies and policies without disrupting the underlying storage and delivery mechanisms, and vice versa.

#### **Local caching and resilient clients**

On the product services side, we introduced a local caching layer between the agent sidecar and the client library to improve resilience and availability. The agent sidecar runs alongside the main service container, regardless of which language the service is written in, and periodically fetches subscribed configs from the backend and persists them locally. The client libraries then read from this local cache. Even if the backend is temporarily unavailable or degraded, services can continue operating on the last known good configs from the local cache.

### Impact on product teams

It is essential for the Sitar system to make life easier for product teams. In practice, its architecture changes how teams ship and operate in a few ways:

* **Rollouts become safer and more predictable.** New behaviors, such as refined authorization rules, can be introduced gradually, verified on a small slice of traffic or in a specific environment, and rolled back quickly if needed. Teams spend less time worrying about “big bang” releases and more time iterating on behavior.
* **Teams get more flexibility in how their configs are managed and rolled out.** Each team can tailor a config flow to its own risk profile and release schedules. For example, teams can choose between automatic, manual, or cron rollouts, select the rollout strategy, and add extra checks. This lets teams keep their existing ways of working while still benefiting from a common platform and shared guardrails.
* **Incident mitigation becomes faster and more controlled.** When something goes wrong in production, incident responders can use observability tools that integrate config events to quickly locate the culprit change, then take quick action using the portal’s emergency flow. These emergency updates are fully auditable for future review.

Besides these examples, the platform includes other improvements in usability, safety, and observability that we will not cover in detail here. Together, they contribute to a smoother day-to-day experience for teams that rely on dynamic configuration.

### Conclusions and next steps

Dynamic configuration is a foundational capability of modern infrastructure. It enables fast iteration and rapid incident response, but only when it is equipped with strong safety features and provides a good developer experience. In this post, we shared how we think about a modern dynamic config platform at Airbnb, and how we developed Sitar’s architecture to meet those expectations.

The work is ongoing. As Airbnb’s business grows, we are continuing to refine rollout strategies, improve config testing, invest in observability and smart incident response tooling, and evolve other platform components.

In future posts, we plan to dive deeper into specific areas of the platform, such as how we optimize the Kubernetes sidecar that delivers config updates and how we design the developer experience around config management.

If this type of work interests you check out our [open roles](https://careers.airbnb.com/).

### Acknowledgments

Our progress with Sitar would not have been possible without the support and contributions of many people. We’d like to thank Craig Sosin, Nikolaj Nielsen, Daniel Fagnan, Alex Edwards, Xian Gao, Nick Morgan, Carolina Calderon, Hanfei Lin, Joyce Li, Yunong Liu, Alex Berghage, Brian Wolfe, Yann Ramin, Denis Sheahan, Richa Khandelwal, Swetha Vaidy, Abhishek Parmar, Adam Kocoloski, Adam Miskiewicz, and all the other engineers and teams at Airbnb who joined design reviews and offered valuable feedback, as this work would not have been possible without them.

*All product names, logos, and brands are property of their respective owners. All company, product and service names used in this website are for identification purposes only. Use of these names, logos, and brands does not imply endorsement.*

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=5aca5222ed68)

---

[Safeguarding Dynamic Configuration Changes at Scale](https://medium.com/airbnb-engineering/safeguarding-dynamic-configuration-changes-at-scale-5aca5222ed68) was originally published in [The Airbnb Tech Blog](https://medium.com/airbnb-engineering) on Medium, where people are continuing the conversation by highlighting and responding to this story.
