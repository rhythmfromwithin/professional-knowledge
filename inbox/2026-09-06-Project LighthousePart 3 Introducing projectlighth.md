---
link: https://medium.com/airbnb-engineering/project-lighthouse-part-3-introducing-project-lighthouse-anonymize-74f8b26653fb?source=rss
slack_ts: '1788667893.514239'
source: Airbnb Engineering
title: 'Project Lighthouse — Part 3: Introducing project-lighthouse-anonymize'
----53c7c27702d5---4
priority: medium
status: unread
interest: medium
next_step: skim
---
# Project Lighthouse — Part 3: Introducing project-lighthouse-anonymize
> 原文: [https://medium.com/airbnb-engineering/project-lighthouse-part-3-introducing-project-lighthouse-anonymize-74f8b26653fb?source=rss----53c7c27702d5---4](https://medium.com/airbnb-engineering/project-lighthouse-part-3-introducing-project-lighthouse-anonymize-74f8b26653fb?source=rss----53c7c27702d5---4)

### Project Lighthouse **—**Part 3: Introducing project-lighthouse-anonymize

#### *The data in Project Lighthouse is powered by privacy-preserving anonymization code. We’ve put this code into open source, and published two new technical papers detailing the scalable algorithms and data quality frameworks behind it.*

![A red and white lighthouse standing on a grassy coastal bluff beside a white cottage with a red roof, overlooking a rocky shoreline and calm blue ocean at golden hour.](https://cdn-images-1.medium.com/max/1024/1*Z2EMY7FElWHf-TY6r69IOA.png)

**By:** [Adam Bloomston](https://www.linkedin.com/in/adam-bloomston/)

### Introduction

In 2020, we launched Project Lighthouse, which we developed in partnership with leading civil rights and privacy organizations. As our 2020 [announcement](https://news.airbnb.com/measuring-discrimination-on-the-airbnb-platform/) details, Project Lighthouse enables us to measure potential disparities in user experiences. This work uses perceived race data that is never linked to individual accounts; we only use this data for measuring potential disparities, and users who want to opt-out can do so by turning off the data use settings in their account’s Privacy page. [Our results](https://news.airbnb.com/2024-project-lighthouse-update/), shared in 2024, demonstrate how we use these analyses to measure our progress in mitigating those disparities.

Earlier this year, we open-sourced [project-lighthouse-anonymize](https://github.com/airbnb/project-lighthouse-anonymize), the Python library that powers Project Lighthouse’s anonymization process. To provide the full technical foundation for this work, we also published two new papers on arXiv alongside the code release. Together with our original 2020 paper, these three papers form a complete story: the foundational methodology, the scalable implementation, and the quality validation framework.

### The foundational methodology (2020)

[Our original 2020 paper](https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf) established the privacy-by-design approach for Project Lighthouse and provides the rationale for choosing k-anonymity as the technical privacy model to prevent sensitive attribute disclosure at scale. For an introduction to this paper, see our [first blog post](https://medium.com/airbnb-engineering/project-lighthouse-part-1-p-sensitive-k-anonymity-c6ee7d79c4f9) on p-sensitive k-anonymity and our [second blog post](https://medium.com/airbnb-engineering/project-lighthouse-part-2-measurement-with-anonymized-data-69fb01eac88) on measurement with anonymized data.

### Core Mondrian: Scalable partition-based anonymization (2025)

The first of our new papers, [Core Mondrian: Basic Mondrian beyond k-anonymity](https://arxiv.org/abs/2510.09661), presents the k-anonymity algorithm at the heart of the open source library. Core Mondrian extends the [classic Mondrian algorithm](https://ieeexplore.ieee.org/document/1617393) with:

* **Extensible architecture**, using the Strategy Pattern to support k-anonymity and future privacy model extensions
* **Parallel processing**, with a hybrid recursive-queue execution model (combining immediate recursive processing for small partitions with queue-based parallel processing for large partitions)
* **Other enhancements**, including NaN-pattern pre-partitioning (accommodating missing values) and dynamic suppression budget management

This algorithm enables scalable anonymization of large datasets while preserving the ability to use the underlying data for statistical analyses.

### Measuring Data Quality for Project Lighthouse (2025)

The second of the new papers, [Measuring Data Quality for Project Lighthouse](https://arxiv.org/abs/2510.06121), addresses a critical question: how do you know if your anonymized data are “good enough” for your analysis?

The paper introduces a comprehensive framework for measuring data quality under anonymization, including:

**Three primary metrics**:

* Pearson correlation (preserving linear relationships between original and anonymized values)
* Revised Information Loss Metric or RILM (measuring how well the “shape” or geometric size of data is preserved — higher scores mean less distortion)
* Normalized Mutual Information v1 or NMIv1 (measuring entropy preservation, essentially how much information content is retained)

**Empirical validation methodology**: We reframe data quality assessment as a machine learning classification problem, using synthetic datasets to validate that our metrics and thresholds successfully predict when anonymized data will produce statistically valid results

**Default thresholds**: The paper and library include the specific threshold values we use for Project Lighthouse, which may serve as useful starting points for others implementing similar systems

This framework enables analysts without deep anonymization expertise to confidently assess whether their anonymized data supports valid statistical conclusions.

### Getting started

The library is available on PyPI and GitHub at [github.com/airbnb/project-lighthouse-anonymize](https://github.com/airbnb/project-lighthouse-anonymize). With this library, you can successively enforce both technical privacy models from [our 2020 paper](https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf):

```
p, k = 2, 5  
# First technical privacy model: k-anonymity  
anon_df, dq_metrics, disclosure_metrics = k_anonymize(logger, input_df, qids, k, {}, "row_id")  
# Second technical privacy model: p-sensitive k-anonymity via perturbation  
sensitized_df, _, _ = p_sensitize(logger, anon_df, qids, "race", p, k, sens_attr_value_to_prob)
```

The algorithm for enforcing k-anonymity is described in [Core Mondrian: Basic Mondrian beyond k-anonymity](https://arxiv.org/abs/2510.09661). And the data quality metrics and thresholds for k-anonymity are described in [Measuring Data Quality for Project Lighthouse](https://arxiv.org/abs/2510.06121):

```
minimum_dq_met, minimum_dq_met_reasons = check_dq_meets_minimum_thresholds(dq_metrics)  
assert minimum_dq_met, str(minimum_dq_met_reasons)
```

The [getting started guide](https://github.com/airbnb/project-lighthouse-anonymize/blob/main/docs/getting_started.md) builds on the code snippets above and provides a complete, runnable example using the [UCI Adult dataset](https://archive.ics.uci.edu/dataset/2/adult).

### Conclusion

We continue to invest in trying to combat potential discrimination and bias users may face when using Airbnb, and in taking steps to enable everyone in our global community to use and enjoy Airbnb. We believe that doing so requires transparency in our methodologies, both to build trust with our users and to encourage other companies to do the same.

If this type of work interests you, check out some of our [related positions](https://careers.airbnb.com/)!

### Acknowledgements

The Airbnb Anti-discrimination & Equity team is Adam Bloomston, Elizabeth Burke, Megan Cacace, Anne Diaz, Wren Dougherty, Matthew Gonzalez, Remington A. Gregg, Yeliz Güngör, Eeway Hsu, Heesoo Kim, Sara Kwasnick, Joanne Lacsina, Demma Rosa Rodriguez, Adam Schiller, Jessica Simon, Maggie Tang, Skyler Wharton, Marilyn Wilcken. I also want to thank Natalija Fijacko, Lauren Mackevich, Laura Rillos, Jessica Simon, Floyd Smith, and Lei Wei for their role in refining and improving this blog post.

*The author acknowledges the use of Large Language Models (LLMs) for assistance with literature review, technical writing, and editing.*

*All product names, logos, and brands are property of their respective owners. All company, product, and service names used in this website are for identification purposes only. Use of these names, logos, and brands does not imply endorsement.*

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=74f8b26653fb)

---

[Project Lighthouse — Part 3: Introducing project-lighthouse-anonymize](https://medium.com/airbnb-engineering/project-lighthouse-part-3-introducing-project-lighthouse-anonymize-74f8b26653fb) was originally published in [The Airbnb Tech Blog](https://medium.com/airbnb-engineering) on Medium, where people are continuing the conversation by highlighting and responding to this story.
