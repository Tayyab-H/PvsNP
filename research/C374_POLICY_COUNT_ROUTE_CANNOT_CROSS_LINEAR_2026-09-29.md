# C-374 - Pure policy-region counting cannot cross the linear barrier

Date: 29 September 2026  
Route: close the count-only branch exposed by C-372/C-373 and isolate what a useful next theorem must charge.  
Classification: **EXACT ROUTE CAP; POLICY GEOMETRY REMAINS OPEN.**

## 1. A universal upper bound on the number of regions needed

Fix any valid C-319 cover Q. For each low table w in SIZE(s1), choose one positional winning policy and its sound CNF region R_w from C-334. The chosen regions cover SIZE(s1), because w belongs to its own selected region. After duplicate regions are removed, this is a cover using at most

M1 = |SIZE(s1)|

distinct regions.

Circuit counting gives

log2(M1) = O(s1 log(s1+n)) = N^(beta+o(1)) = o(N).

This bound is independent of Q and of the particular low-anchor subfamily.

## 2. Ceiling for region-count arguments

A C-319 region is determined by the subset of the 2q fixed seed clauses used at policy stops, so the graph can have at most 2^(2q) distinct regions. A proof that uses only the number R of regions must therefore pass through

2^(2q) >= R,
q >= (1/2) log2(R).

But the minimum number of regions needed to cover all low tables is at most M1. Hence any lower bound on q derived only from the cardinality of a region cover is capped by

q >= at most (1/2) log2(M1) = N^(beta+o(1)) = o(N).

This cannot establish the already known q>=N-o(N), let alone a superlinear bound. C-373's lower bound of 2^(Omega(sqrt(D))) regions is valid structural information, but its conversion through a generic region count is strictly sublinear here.

## 3. What is retired and what remains live

Retire region-count-only arguments, including stronger choices of the low code family, as a route to the project target. C-372/C-373 still provide useful facts about how large or pseudorandom anchors behave inside one sound cone.

The live question is geometric and transition-sensitive: how do the context and continuation supports at a shared state combine across different selected policies? C-281 says every compatible context/proof pair is accepted, so its entire completion cylinder must be low. The next theorem must show that a fixed graph cannot arrange these cross-policy products cheaply, or construct a sound compact arrangement. It must account for overlapping high exclusions (C-130), filtered children (C-132), and the broad high activation regions in C-145. Merely counting anchors, policies, clauses, or regions is exhausted.

## 4. Checkpoint

- The policy-region count route has a strict o(N) ceiling from |SIZE(s1)|: proved.
- No arbitrary-cover cross-policy compatibility theorem has been established.
- The best native lower bound remains q>=N-o(N).
- No full-promise near-linear cover or P-vs-NP proof follows.

The next open obligation is recorded as O-222 in research/OPEN_OBLIGATIONS.md.
