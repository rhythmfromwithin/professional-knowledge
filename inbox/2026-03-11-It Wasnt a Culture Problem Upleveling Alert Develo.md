---
link: https://medium.com/airbnb-engineering/it-wasnt-a-culture-problem-upleveling-alert-development-at-airbnb-01e2290eb0f5?source=rss
slack_ts: '1773196804.567739'
source: Airbnb Engineering
title: 'It Wasn’t a Culture Problem: Upleveling Alert Development at Airbnb'
----53c7c27702d5---4
priority: medium
status: unread
interest: medium
next_step: skim
---
# It Wasn’t a Culture Problem: Upleveling Alert Development at Airbnb
> 原文: [https://medium.com/airbnb-engineering/it-wasnt-a-culture-problem-upleveling-alert-development-at-airbnb-01e2290eb0f5?source=rss----53c7c27702d5---4](https://medium.com/airbnb-engineering/it-wasnt-a-culture-problem-upleveling-alert-development-at-airbnb-01e2290eb0f5?source=rss----53c7c27702d5---4)

![](https://cdn-images-1.medium.com/max/1024/1*Cy9Y4YIsQLRhjl15rMGqkQ.jpeg)

#### How we changed our Observability as Code alert review process and cut development cycles from weeks to minutes.

Observability as Code (OaC) — defining alerts, dashboards, and SLOs via code rather than UI — is table stakes for large engineering organizations. With OaC, observability adopts software development’s version control, code review, and testing processes, achieving the same level of discipline as a result. At Airbnb’s scale (thousands of engineers and services), this is the foundation that lets teams ship confidently while maintaining the reliability our guests and hosts depend on.

Yet there’s a critical gap in most OaC workflows. While we bring rigor to alert definitions through code review and version control, the actual behavior of those alerts often can’t be validated until they’re live. Production becomes the proving ground. Problems surface either as noise that erodes trust or silence that hides real incidents.

This tolerance of high alert noise might appear to be a culture problem, but we realized it was actually a gap in the developer workflow. We solved it by building accessible, fast feedback loops to preview, validate, and surface actionable insights on alert behavior before PR submission. With these changes, development cycles collapsed from weeks to minutes, and we successfully migrated 300,000 alerts from a vendor to Prometheus, a feat that wouldn’t have been possible otherwise.

### Airbnb’s OaC North Star

Our Observability as Code North Star is for product teams to receive out-of-the-box, best-practice monitoring from platform teams. When a product engineer adopts Kubernetes, a service framework, or a database, they should inherit battle-tested alerts, dashboards, and SLOs. The best monitoring gives product engineers the benefit of all of Airbnb’s infra and platform domain expertise immediately. We call this “zero touch.”

We began our OaC journey more than 10 years ago when we [built Interferon](https://medium.com/airbnb-engineering/alerting-framework-at-airbnb-35ba48df894f), starting with 1,000 alerts. Today, we manage 300,000. By any measure, Interferon was a success, scaling our monitoring practices towards our North Star.

However, this success introduced new operational challenges. With so many alerts in production, validating any OaC changes became costly, and it became harder to iterate. Engineers faced a difficult tradeoff: tuning an alert template might reduce noise, but it also risked losing an important signal. Without a way to preview alert behavior, the safer choice was often to leave things as-is.

### The problem: Traditional code review can’t validate alert behavior

The problem wasn’t Interferon itself, but rather a development workflow gap. Our North Star requires platform teams to define and maintain monitoring patterns at scale, but we lacked the necessary tooling to effectively validate those patterns against reality.

Traditional code review can validate syntax and logic, and unit tests can verify outputs. But neither can answer the questions that matter most: “How will these alerts behave in production? What noise might they generate? Will they needlessly wake up on-call engineers at 3 AM?”

That’s why you have to validate alerts against real-world data. If your assumptions about the data are wrong, your alert is wrong.

However, off-the-shelf query visualization tools are insufficient for the job. They don’t account for alert-specific parameters, and most notably, they show downsampled data that masks actual alert behavior — step sizes don’t match evaluation intervals. Also, the further you move from static configs, the harder validation becomes. With templating, reviewers must manually copy-paste queries and fill in variables. For a single alert, this is tedious and error-prone; for changes affecting hundreds of services, it’s impossible.

So in practice, developers often had to resort to a weeks-long process of deploying a new alert side-by-side with the existing one, waiting for real-world data to come in, validating, and then iterating.

### The solution: Making alert behavior visible

What if an infrastructure engineer could validate a Kubernetes alert template, one that fans out to thousands of services, in 30 seconds instead of 30 days?

That question among others prompted us to rethink and rebuild our OaC platform from the ground up. Building on top of Prometheus’ open source foundations, we could develop the exact UX our engineers needed, particularly local diffs and pre-deployment validation.

The core of this workflow is local-first development: The same code and inputs run in production must run identically on a developer’s laptop and in CI. In addition, we built **Change Reports** that show how alerts will be modified and **bulk backtesting** that simulates alerts against historical data.

We rolled out this platform incrementally, with each milestone providing compounding value.

#### Phase 1: Text-based diffs everywhere

![](https://cdn-images-1.medium.com/max/1024/1*NEVDYuTGZJ6XwAsCUqetHA.png)

An example alert diff in markdown format

We first generated markdown alert diffs with field-level granularity and query links — the “terraform plan” of OaC. We met developers where they work, in terminal via CLI and in PRs via CI. This solved the basic visibility problem: engineers could finally review the OaC generated alerts without error-prone copy-pasting.

#### Phase 2: Dedicated Change Report UI

![](https://cdn-images-1.medium.com/max/1024/1*Z2FoWr95uknzOPb3tYJwwg.png)![](https://cdn-images-1.medium.com/max/1024/1*AQerk_Q3E1h3zOveLijmRg.png)

The left image lists all alert modifications resulting from a code change. The right image dives into a specific alert.

We then built a Change Report UI showing side-by-side alert diffs exactly as they will appear in production, removing the guesswork and mental mapping between config and UI. However, the user was still responsible for mentally simulating alert behavior, which is challenging even for Prometheus experts to get right.

#### Phase 3: Historical simulation via bulk backtesting

![](https://cdn-images-1.medium.com/max/1024/1*R4Gk9LyATkdH5hHHVros9g.png)![](https://cdn-images-1.medium.com/max/1024/1*BA_Fv1oVTPymUQUwene7HQ.png)

The backtesting integration into the change list (left) and individual alert (right) views

Finally, we built a backtesting system that runs proposed alerts against historical data, hooking directly into [Prometheus’s rule manager](https://github.com/prometheus/prometheus/blob/c7bc56cf6c8f9c92e98beddca26ed9b47f8a5ac9/rules/manager.go#L97). Backtesting allows users to understand which alerts would have fired, when, and why, as if they had existed the entire time. Displaying this simulated state inline in the Change Report UI answered the question that matters most: “How would this alert behave in production?”

We backtest in bulk for the entire diff — hundreds or thousands of related alerts — and surface quality signals to help reviewers focus their attention. We compute a “noisiness” metric and show alert firing timelines in the table view, letting users sort by potential problems and focus their effort.

#### Putting it all together

On the new platform, when a user makes an OaC change, they will now generate a Change Report via CLI or CI. We post a Change Report on all PRs.

![](https://cdn-images-1.medium.com/max/1024/1*ibWolnBsOQD4yJCDk9zdag.png)

The user reviews their changes via the UI. In this example, a one week backtest was conducted, and the changes are sorted by noisiness, seen in the “Tuning” column, to help direct users’ attention.

![](https://cdn-images-1.medium.com/max/1024/1*U6n6RvF4-fTi3MBVeQsjtA.png)

The user can dive into individual alerts to learn more. This one looks to be problematic, firing once per day.

![](https://cdn-images-1.medium.com/max/1024/1*OU3knDx3DNoQGhVQHZPILA.png)

The user can set overrides. Given the graph, 1.14 looks like a better trigger threshold.

![](https://cdn-images-1.medium.com/max/1024/1*hSNS3BDZ2sdJdHakuEb-1A.png)

They can then see the impact of their changes. No more alert firings. This looks good and is ready to ship.

![](https://cdn-images-1.medium.com/max/1024/1*Vw2paibsDpqT2Cqe4MSK6A.png)

### Our learnings

#### Compatibility over novelty

A key architectural decision was compatibility over novelty**.** Rule groups are Prometheus’ standardized format. By taking that as input, we hooked directly into Prometheus’s rule evaluation engine rather than reimplementing it. We wrote results as Prometheus time series blocks, exposing the data via [the standard query API](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries). This meant building analysis tools once. This standardization made our system portable, allowing us to reach all developers in their existing workflows.

#### Guardrails aren’t optional

Simulating thousands of alerts over 30 days quickly and without service degradations required careful design. Each backtest runs in its own Kubernetes pod with autoscaling to prevent resource contention. Concurrency limits, error thresholds, and multiple circuit breakers prevent cascading failures. A backtesting system that can destabilize production is worse than no system at all.

#### Perfect is the enemy of shipped

Our simulator doesn’t account for recording rule dependencies. We could have built a more sophisticated dependency resolver, but users can separate this into two distinct tasks — modify the recording rule first, then backtest alerts that depend on it — assuming they know they should. The Change Report UI helps, because when modified dependencies are detected, it highlights them and prompts resolution. This turns a technical limitation into a guided workflow. We shipped the 80% solution that immediately delivers value, leveraging the UI to close gaps.

#### Own the full surface area

Monitoring is often an afterthought — engineers have limited time under tight deadlines. Our job is to make that time as effective as possible. Prometheus is powerful but exposes a low-level API that requires expertise most engineers don’t have. To achieve our North Star, we introduced abstractions like anomaly detection, burn rate alerts, and change detection. But abstractions only simplify things when you own all the touchpoints: the input language engineers write, the generation process, the UI that displays results, and the validation tools that provide feedback. Partial ownership creates leaky abstractions. Full ownership lets us ruthlessly optimize for developer experience.

### The impact

#### Successful migration from a vendor to Prometheus

We migrated 300,000 alerts from a vendor to Prometheus. Rewriting every alert would have been impossible with our old workflow, but we achieved it thanks to our Change Report UI, bulk backtesting, and an additional vendor-specific integration. By codifying our domain knowledge in the UX, what originally promised to be a multi-year slog of manual effort became a structured, confident migration.

#### Collapsed development cycles

The typical developer workaround for making alert changes — deploy side-by-side, wait, then iterate — became obsolete. Engineers now make and validate alert changes all within a single PR. Platform teams confidently deploy template changes affecting thousands of services. What once took a month of iteration now takes an afternoon.

#### Culture transformation

Even though we realized we had a workflow problem, not a culture problem, solving this problem still ended up transforming our culture. We reduced companywide alert noise by 90%, and engineers stopped tolerating noisy alerts and started competing to improve them. Platform teams resumed iterating on shared patterns. Alert hygiene became a point of pride, not a chore to avoid.

> Turnkey alert testing is the biggest positive improvement to alerts management in Airbnb’s history.

> I’ve seen people spend hours debating the merits of changing an alert only to do nothing because of fear, uncertainty, and doubt. This new alert testing capability completely evaporates the stop energy and allows us to monitor with confidence.

> - Gregory Szorc, Senior Staff Software Engineer

### Conclusion

Local-first development, Change Reports, and bulk backtesting give us the necessary tools to incrementally reach our North Star. Platform teams can now confidently iterate on monitoring for their domains. Zero touch is becoming how we operate, one cycle at a time.

Now that we’ve introduced pre-deployment visibility and validation to the alert lifecycle, our next step is to introduce that same rigor to on-call analysis.

If this type of work interests you, check out some of our [open roles](https://careers.airbnb.com/).

#### Acknowledgements

Thank you to the Reliability Experience team — Kevin Goodier, Harry Shoff, Rich Unger, and Vlad Vassiliouk — and our partners across the company who helped make this a reality.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=01e2290eb0f5)

---

[It Wasn’t a Culture Problem: Upleveling Alert Development at Airbnb](https://medium.com/airbnb-engineering/it-wasnt-a-culture-problem-upleveling-alert-development-at-airbnb-01e2290eb0f5) was originally published in [The Airbnb Tech Blog](https://medium.com/airbnb-engineering) on Medium, where people are continuing the conversation by highlighting and responding to this story.
