---
title: "IceCube Takes Flight with Pelican - A First Experience"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.31851
priority: medium
status: unread
interest: medium
next_step: skim
---
# IceCube Takes Flight with Pelican - A First Experience
> 原文: [https://arxiv.org/abs/2609.31851](https://arxiv.org/abs/2609.31851)

arXiv:2609.31851v1 Announce Type: new
Abstract: The IceCube Neutrino Observatory has removed GridFTP and x.509 certificate authentication for data transfers, migrating to the Pelican Platform, the Open Science Data Federation, and WLGC tokens. While this is a common solution on the computing infrastructure we use, we required several customizations to work with our existing data storage structure and make it easier for scientists to use. We wrote a custom WLCG token issuer to support our POSIX filesystem with custom user and group permissions across the entire filesystem. We also made several modifications to HTCondor to ease job submission using tokens, including a custom credmon. After an initially bumpy transition due to several now-resolved Pelican issues, the Pelican-based system has already proven superior to GridFTP in several ways.
