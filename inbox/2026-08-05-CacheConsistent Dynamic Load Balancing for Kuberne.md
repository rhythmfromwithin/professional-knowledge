---
title: "Cache-Consistent Dynamic Load Balancing for Kubernetes Controllers"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.00454
priority: medium
status: unread
interest: medium
next_step: skim
---
# Cache-Consistent Dynamic Load Balancing for Kubernetes Controllers
> 原文: [https://arxiv.org/abs/2608.00454](https://arxiv.org/abs/2608.00454)

arXiv:2608.00454v1 Announce Type: new
Abstract: As Kubernetes clusters grow, the scalability of controllers can become a bottleneck for the performance of the system. Distributing the load dynamically across multiple controller instances, however, raises the following two problems, and a controller can therefore be run only as a single instance today. The first problem is the cost of reassignment. A controller retrieves objects on the basis of the Labels attached to them, so in a naive design in which the assigned instance is recorded in a Label on every object, the Labels must be rewritten in proportion to the total number of objects whenever instances are added or removed. The second problem is cache consistency. A controller consults only its own cache when it reads an object and never refers to the actual data, so the cache has to be updated explicitly at the time of a reassignment. Furthermore, a controller manages a cache independently for each kind of object, so cache updates have to be synchronized across the kinds of objects. We propose a method for scaling Kubernetes controllers horizontally that combines lightweight load balancing with cache synchronization. A two-level Hash maps objects to Virtual Nodes, records their identifiers in Labels, and assigns Virtual Nodes to instances by Consistent Hashing. Whenever instances are added or removed, it therefore suffices to update the Label value specified when objects are retrieved, and no Label on an object has to be rewritten. The cache is also locked until the reassignment has completed, which prevents any reference to a stale cache. The version identifier of the data store is used to synchronize the kinds of objects with one another. We implemented the proposed method on Kubernetes and evaluated it: the processing throughput rises with the number of instances, and the time required for reassignment remains within an acceptable range.
