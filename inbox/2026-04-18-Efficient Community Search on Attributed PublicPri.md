---
interest: medium
link: https://arxiv.org/abs/2604.14988
next_step: skim
priority: low
slack_ts: '1776569843.476989'
source: cs.DB - Databases
status: unread
title: Efficient Community Search on Attributed Public-Private Graphs
---
# Efficient Community Search on Attributed Public-Private Graphs
> 原文: [https://arxiv.org/abs/2604.14988](https://arxiv.org/abs/2604.14988)

arXiv:2604.14988v1 Announce Type: new
Abstract: Public-private graph, where a public network is visible to everyone and every user is also associated with its own small private graph accessed by itself only, widely exists in real-world applications of social networks and financial networks. Most existing work on community search, finding a query-dependent community containing a given query, only studies on a public graph, neglecting the privacy issues in public-private networks. However, considering both the public and private attributes of users enables community search to be more accurate, comprehensive, and personalized to discover hidden patterns. In this paper, we study a novel problem of attributed community search in public-private graphs (ACS-PP), aiming to find a connected k-core community that shares the most keywords with the query node. This problem uncovers structurally cohesive communities, such as interest-based user groups or core teams in collaborative networks. To optimize search efficiency, we propose an integrated scheme of constructing a public global graph index and a private personalized graph index. For the private index, we developed a compact structure of the PP-FP-tree index. The PP-FP-tree is constructed based on the public and private neighbors of the query node in the public-private graph, serving as an efficient index to mine frequent node sets that share the most common attributes with the query node. Extensive experiments on real public-private graph datasets validate both the efficiency and quality of our proposed PP-FP search algorithm against existing competitors. The case study on public-private collaboration networks provides insights into the discovery of public-private communities.
