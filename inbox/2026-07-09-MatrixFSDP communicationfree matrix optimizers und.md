---
interest: medium
link: https://arxiv.org/abs/2607.05895
next_step: skim
priority: medium
slack_ts: '1783655933.974799'
source: cs.DC - Distributed Computing
status: unread
title: 'MatrixFSDP: communication-free matrix optimizers under ZeRO-3 parameter sharding'
---
# MatrixFSDP: communication-free matrix optimizers under ZeRO-3 parameter sharding
> 原文: [https://arxiv.org/abs/2607.05895](https://arxiv.org/abs/2607.05895)

arXiv:2607.05895v1 Announce Type: new
Abstract: Matrix optimizers such as Muon are attractive for large-scale training because they can improve convergence and token efficiency over coordinate-wise optimizers. Muon does this by orthogonalizing momentum-smoothed matrix updates with Newton-Schulz, producing spectrum-balanced updates that require the complete 2D matrix as input. This exposes a systems mismatch: FSDP/ZeRO-3 saves memory by making the optimizer see shards, not whole matrices. Existing systems therefore either reconstruct matrices at every optimizer step, paying weight-sized communication after backward, or make the update local by using ZeRO-1 owner placement with full parameters resident. MatrixFSDP takes a third path: it changes where ZeRO-3 shards live, not the optimizer being computed. For each 2D weight, one data-parallel rank owns the whole matrix and the other ranks hold empty shards; non-matrix tensors are packed into tail owners and stay on AdamW. The ordinary backward reduction then lands the full Muon input on the owner, so Newton-Schulz runs locally with no optimizer-step matrix collective. Forward and backward still materialize and reshard parameters; the runtime challenge is to make that uneven layout efficient and correct. MatrixFSDP does so with MatrixShard metadata, a balance-aware owner planner, deterministic owner-segment P2P collectives, owner-buffer pinning, and owner-shard checkpoint resharding. The resulting update matches full-matrix Muon while preserving ZeRO-3-scale memory: on 64 A100s, MatrixFSDP reduces optimizer-step latency over stock FSDP2-Muon by 4.2x on one node and 54.6x on eight nodes, reaches up to 2.15x end-to-end speedup, and runs model sizes where ZeRO-1 owner placement exceeds an 80 GB GPU.
