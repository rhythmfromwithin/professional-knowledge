---
interest: medium
link: https://arxiv.org/abs/2609.31820
next_step: skim
priority: low
slack_ts: '1790745130.285979'
source: cs.SE - Software Engineering
status: unread
title: 'Hypothesis-awkward: Property-Based Testing Strategies for Awkward Array'
---
# Hypothesis-awkward: Property-Based Testing Strategies for Awkward Array
> 原文: [https://arxiv.org/abs/2609.31820](https://arxiv.org/abs/2609.31820)

arXiv:2609.31820v1 Announce Type: new
Abstract: Hypothesis-awkward is a collection of Hypothesis strategies for Awkward Array. Awkward Array can represent a wide variety of nested, variable-length, mixed-type data. Many tools that process Awkward Arrays are widely used and actively developed. The unit test cases of many of these tools list predefined input samples. In practice, such samples can cover only a small portion of the vast combinatorial space of Awkward Array instances. Hypothesis, a Python property-based testing library, generates test data that can make test cases fail and automatically explores edge cases. The main strategy of Hypothesis-awkward generates nearly all possible Awkward Arrays, with options to control the layout, data types, missing values, masks, and other array attributes. Property-based tests written with these strategies have begun to run in the continuous integration of Awkward Array; to date, they cover a small part of Awkward Array and have found 37 bugs in it, as well as one in Hypothesis itself. These strategies make the tests of Awkward Array and of the tools that use it more reliable.
