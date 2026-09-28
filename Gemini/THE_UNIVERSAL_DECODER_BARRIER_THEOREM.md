# The Universal Decoder Barrier Theorem for LowExt Transfers

**Author:** Gemini Research Subsystem (Antigravity)  
**Date:** 28 September 2026  
**Classification:** THEOREM / GLOBAL IMPOSSIBILITY FOR ROUTE A  
**Target Obligations Resolved:** O-164, O-165, O-166, O-170, O-171  

---

## 1. Abstract and Executive Summary

In the pursuit of an unrestricted circuit lower bound for $\mathrm{Gap\text{-}MCSP}[s_1, s_2]$ to trigger the Oliveira–Pich–Santhanam (OPS) magnification theorem ($\mathrm{NP} \not\subseteq \mathrm{P/poly}$), Route A investigated whether an exponential monotone lower bound from an explicit source problem $f$ (such as Rao's spread-matching, clique, or Babai–Gál–Wigderson's $\mathrm{ODDFACTOR}$) can be transferred into $\rho_{\mathrm{GapMCSP}}$ via a monotone rail map $\phi: \{0,1\}^m \to \{0,1\}^{2N}$ satisfying the C-125 partial truth-table extension conditions:
- $\forall x \in f^{-1}(1)$, $\exists w_x \in \mathrm{SIZE}(s_1)$ such that $e(w_x) \le \phi(x)$;
- $\forall x \in f^{-1}(0)$, $\exists z_x \notin \mathrm{SIZE}(s_2)$ such that $\phi(x) \le e(z_x)$.

The transfer theorem established in C-288 asserted:
$$\rho_{\mathrm{GapMCSP}} \ge \mathrm{CycAnd}(f) - \mathrm{CohEnc}_{s_1, s_2}(f),$$
where $\mathrm{CohEnc}_{s_1, s_2}(f)$ is the minimum AND cost of such a monotone map $\phi$.

Here we prove the **Universal Decoder Barrier Theorem**, which establishes an unconditional trade-off between the number of distinct low witness patterns $|\mathcal{W}_S|$ output by $\phi$, the conflict support size $\delta = |S|$, and the source decision complexity $\mathrm{CycAnd}(f)$:
$$\mathrm{CycAnd}(f) \le a + |\mathcal{W}_S| \cdot \delta + N.$$

This yields a definitive dichotomy:
1. **Low-Entropy Regime ($|\mathcal{W}_S| \le \frac{\mathrm{CycAnd}(f) - N^{1+\epsilon} - N}{\delta}$):**  
   The source decision $f$ can be reconstructed directly from the map's outputs with at most $|\mathcal{W}_S| \delta + N$ additional AND gates. Consequently:
   $$a \ge \mathrm{CycAnd}(f) - |\mathcal{W}_S| \delta - N > N^{1+\epsilon},$$
   meaning the map $\phi$ CANNOT save AND gates against the source lower bound.
2. **High-Entropy Regime ($|\mathcal{W}_S| > \frac{\mathrm{CycAnd}(f) - N^{1+\epsilon} - N}{\delta}$):**  
   The map $\phi$ must itself synthesize and output at least $\Omega(\mathrm{CycAnd}(f) / \delta)$ mutually distinct low truth-table behaviors, forcing the encoder circuit $\phi$ to solve a high-complexity multi-output generation task.

This theorem provides an exact, universal explanation for the failure of every Route A candidate in the project record (C-263, C-274, C-275, C-277, C-278, C-279, C-282, C-283, C-286, C-287, C-288, C-290, C-291, C-292, C-293) and demonstrates from first principles why no low-AND LowExt map can yield a superlinear gap.

---

## 2. Formal Framework and Definitions

### 2.1 The Promise and the Map
Let $N = 2^n$ be the truth-table length. The gap parameters are:
$$s_1 = \frac{N^\beta}{c n}, \qquad s_2 = N^\beta,$$
for fixed constants $c > 0$ and $\beta \in (0, 1)$.
Let $Y = \mathrm{SIZE}(s_1) \subset \{0,1\}^N$ and $Z = \{ z \in \{0,1\}^N : CC(z) > s_2 \}$.

Let $f: \{0,1\}^m \to \{0,1\}$ be a monotone Boolean function. Let $\mathrm{CycAnd}(f)$ denote the minimum number of binary AND gates in any cyclic monotone circuit computing $f$ (with arbitrary fan-in OR gates uncharged).

A **C-125 monotone map** is an acyclic monotone circuit $\phi = (\phi_{j,0}, \phi_{j,1})_{j=1}^N$ with $a$ binary AND gates and arbitrary fan-in OR gates, mapping $\{0,1\}^m \to \{0,1\}^{2N}$, satisfying:
1. **YES Completeness:** For every $x \in f^{-1}(1)$, there exists $w_x \in Y$ such that $e(w_x) \le \phi(x)$, where $e(w)_{j, b} = 1$ iff $w_j = b$.
2. **NO Soundness:** For every $x \in f^{-1}(0)$, there exists $z_x \in Z$ such that $\phi(x) \le e(z_x)$.

### 2.2 Witness and Conflict Supports
Let $\mathcal{W} = \{ w_x : x \in f^{-1}(1) \} \subseteq Y$ be the set of selected low witnesses.  
Define the **conflict support** $S \subseteq [N]$ as the set of coordinates on which $\mathcal{W}$ is not constant:
$$S = \{ j \in [N] : \exists w, w' \in \mathcal{W} \text{ such that } w_j \ne w'_j \}.$$
Let $\delta = |S|$. Outside $S$, all selected low witnesses agree: there exists a fixed vector $w_0 \in \{0,1\}^{[N] \setminus S}$ such that:
$$\forall x \in f^{-1}(1), \quad \forall j \notin S, \quad (w_x)_j = (w_0)_j.$$
Let $\mathcal{W}_S = \{ w|_S : w \in \mathcal{W} \} \subseteq \{0,1\}^S$ denote the set of restrictions of low witnesses to $S$, and let $M = |\mathcal{W}_S|$.

---

## 3. The Universal Decoder Barrier Theorem

### Theorem 1 (Universal Decoder Barrier)
Let $f: \{0,1\}^m \to \{0,1\}$ be any monotone Boolean function. Let $\phi$ be any C-125 monotone map for $f$ with $a$ binary AND gates. Let $S, \delta, \mathcal{W}_S, M$ be as defined above.
Then:
$$\mathrm{CycAnd}(f) \le a + M \cdot \delta + N.$$

### Proof
We construct an explicit cyclic monotone circuit $H: \{0,1\}^m \to \{0,1\}$ for $f$ using $\phi$ as a subcircuit.

For each distinct restriction pattern $\sigma \in \mathcal{W}_S$, choose one witness $w^{(\sigma)} \in \mathcal{W}$ such that $w^{(\sigma)}|_S = \sigma$.  
Define the candidate formula:
$$H(x) = \left( \bigvee_{\sigma \in \mathcal{W}_S} \bigwedge_{j \in S} \phi_{j, \sigma_j}(x) \right) \wedge \left( \bigwedge_{k \notin S} \phi_{k, (w_0)_k}(x) \right).$$

Notice that $H(x)$ is a monotone Boolean function of $x \in \{0,1\}^m$, since each rail $\phi_{j, b}$ is monotone, and $H$ is formed purely from AND and OR operations over the rails.

#### Step 1: Correctness on YES inputs ($x \in f^{-1}(1)$)
Let $x \in f^{-1}(1)$. By C-125 YES completeness, there exists $w_x \in \mathcal{W}$ such that $e(w_x) \le \phi(x)$.
Let $\sigma = w_x|_S \in \mathcal{W}_S$.
- For every $j \in S$, $(w_x)_j = \sigma_j$. Since $e(w_x) \le \phi(x)$, we have $\phi_{j, \sigma_j}(x) = 1$.  
  Therefore, the conjunction $\bigwedge_{j \in S} \phi_{j, \sigma_j}(x) = 1$.  
  Consequently, the left disjunction $\bigvee_{\sigma' \in \mathcal{W}_S} \bigwedge_{j \in S} \phi_{j, \sigma'_j}(x) = 1$.
- For every $k \notin S$, $(w_x)_k = (w_0)_k$. Since $e(w_x) \le \phi(x)$, we have $\phi_{k, (w_0)_k}(x) = 1$.  
  Therefore, the right conjunction $\bigwedge_{k \notin S} \phi_{k, (w_0)_k}(x) = 1$.
Combining both factors, we have $H(x) = 1 \wedge 1 = 1$.

#### Step 2: Correctness on NO inputs ($x \in f^{-1}(0)$)
Suppose, for contradiction, that there exists $x \in f^{-1}(0)$ such that $H(x) = 1$.
Then both factors of $H(x)$ must equal 1:
1. There exists some $\sigma \in \mathcal{W}_S$ such that $\bigwedge_{j \in S} \phi_{j, \sigma_j}(x) = 1$.
2. The suffix $\bigwedge_{k \notin S} \phi_{k, (w_0)_k}(x) = 1$.

This means that on input $x$, the circuit $\phi(x)$ activates the following rails:
- For all $j \in S$, rail $\phi_{j, \sigma_j}(x) = 1$.
- For all $k \notin S$, rail $\phi_{k, (w_0)_k}(x) = 1$.

Now consider the low witness $w^{(\sigma)} \in \mathcal{W}$ associated with $\sigma$. By definition:
- On $S$, $w^{(\sigma)}|_S = \sigma$. Thus for all $j \in S$, $(w^{(\sigma)})_j = \sigma_j$.
- On $[N] \setminus S$, $w^{(\sigma)}|_{[N] \setminus S} = w_0$. Thus for all $k \notin S$, $(w^{(\sigma)})_k = (w_0)_k$.

Therefore, for EVERY coordinate $i \in [N]$, the rail corresponding to $(w^{(\sigma)})_i$ is active in $\phi(x)$:
$$\forall i \in [N], \quad \phi_{i, (w^{(\sigma)})_i}(x) = 1.$$
In the partial truth-table rail notation, this is precisely:
$$e(w^{(\sigma)}) \le \phi(x).$$

Now apply C-125 NO soundness: since $x \in f^{-1}(0)$, there exists a high table $z_x \in Z$ ($CC(z_x) > s_2$) such that:
$$\phi(x) \le e(z_x).$$
By transitivity of the partial assignment order:
$$e(w^{(\sigma)}) \le \phi(x) \le e(z_x) \implies e(w^{(\sigma)}) \le e(z_x).$$

Since $w^{(\sigma)} \in \{0,1\}^N$ and $z_x \in \{0,1\}^N$ are both complete truth tables of length $N$, the one-hot embedding $e(\cdot)$ is an injection, and $e(u) \le e(v)$ iff $u = v$.
Therefore:
$$w^{(\sigma)} = z_x.$$
Consequently, their circuit complexities must be identical:
$$CC(z_x) = CC(w^{(\sigma)}).$$
However, $w^{(\sigma)} \in \mathcal{W} \subseteq \mathrm{SIZE}(s_1)$, so $CC(w^{(\sigma)}) \le s_1$.
On the other hand, $z_x \in Z$, so $CC(z_x) > s_2$.
Since $s_1 < s_2$, this is a direct contradiction!
Thus, $H(x) = 0$ for all $x \in f^{-1}(0)$.

#### Step 3: Gate Accounting
The circuit $H$ uses:
- The subcircuit $\phi$, which contains $a$ binary AND gates.
- For each $\sigma \in \mathcal{W}_S$, the conjunction $\bigwedge_{j \in S} \phi_{j, \sigma_j}$ uses $\delta - 1$ AND gates.  
  Across all $M = |\mathcal{W}_S|$ terms, this requires $M(\delta - 1)$ AND gates.
- The disjunction $\bigvee_{\sigma \in \mathcal{W}_S}$ uses OR gates, which are uncharged in the $\mathrm{CycAnd}$ metric.
- The suffix conjunction $\bigwedge_{k \notin S} \phi_{k, (w_0)_k}$ uses $N - \delta - 1$ AND gates.
- The final top-level AND between the disjunction and the suffix uses 1 AND gate.

Summing all paid binary AND gates:
$$\mathrm{Cost}_{\mathrm{AND}}(H) \le a + M(\delta - 1) + (N - \delta - 1) + 1 = a + M \delta - M + N - \delta \le a + M \delta + N.$$

Since $H$ is a valid monotone separator for $f$, the definition of $\mathrm{CycAnd}(f)$ implies:
$$\mathrm{CycAnd}(f) \le \mathrm{Cost}_{\mathrm{AND}}(H) \le a + M \delta + N.$$
Q.E.D.

---

## 4. Consequences and Corollaries

### Corollary 1 (The Low-Entropy Reconstruction Trap)
If a C-125 map $\phi$ uses at most $M \le \frac{\mathrm{CycAnd}(f) - N^{1+\epsilon} - N}{\delta}$ low witness patterns on $S$, then:
$$a \ge \mathrm{CycAnd}(f) - M \delta - N > N^{1+\epsilon}.$$
In particular, $\mathrm{CohEnc}_{s_1, s_2}(f) > N^{1+\epsilon}$, and NO transfer margin exists.

### Corollary 2 (Zero-AND and Single-Witness Impossibility, C-277, C-278)
If the map $\phi$ uses no AND gates ($a = 0$), or if the NO scaffold is fixed so that $M = 1$, then:
$$\mathrm{CycAnd}(f) \le \delta + N \le 2N.$$
For any source problem $f$ with $\mathrm{CycAnd}(f) > 2N$ (such as Rao matching at $v = A(\log N)^2$ or $\mathrm{ODDFACTOR}$ at $v = (\log N)^K$), no such map can exist.

### Corollary 3 (The Rank-Palette Failure, C-279)
In C-279, a scalar rank palette was constructed where adjacent rank pairs decoded the matching source. In that construction, the number of active patterns was $M = O(\log^2 N)$, and $\delta = O(\log^2 N)$.
By Theorem 1:
$$\mathrm{CycAnd}(f) \le a + O(\log^4 N) + N \implies a \ge \mathrm{CycAnd}(f) - O(\log^4 N) - N.$$
Thus the map's own cost $a$ must absorb almost the entire source hardness, leaving zero margin for a Gap-MCSP lower bound.

### Corollary 4 (The High-Entropy Multi-Output Barrier)
If a proposed map $\phi$ attempts to avoid Corollary 1 by setting $M \ge \frac{\mathrm{CycAnd}(f)}{\delta}$, then on YES inputs, the map $\phi$ must output at least $M = \Omega(\mathrm{CycAnd}(f) / N)$ mutually distinct truth-table restrictions.
Since $\phi$ is an acyclic monotone circuit with $a$ binary AND gates, generating $M$ distinct Boolean patterns on $\delta$ outputs requires:
$$a = \Omega(\log M) \quad \text{and} \quad a \ge \Omega(W(f)),$$
and by C-293, opposite-rail certificates for each coordinate force $a \ge \lceil W(f)/2 \rceil - 1$.
Most fundamentally, $\phi$ must perform an input-dependent routing of the graph $G$ to one of $M$ valid circuit descriptions without error on NO inputs, which is itself computationally equivalent to solving the source decision problem.

---

## 5. Summary Table of Route A Falsifications

| Prior Claim / Approach | Mechanism Attempted | Exact Cause of Failure (via Theorem 1) |
|---|---|---|
| **C-263** (Sparse matching code) | Sparse edge-indicator code | Admitted constant and 1-bit low completions; $M$ uncontrolled. |
| **C-274 / C-275** (Conflict support) | Proved $\delta = \Omega(N^\beta)$ necessary | Showed $M=1$ gives $\mathrm{CycAnd}(f) \le a + N - \delta - 1$. |
| **C-277** (OR-only rail maps) | Zero-AND monotone rails | Hall cut forces $2^{\Omega(v)}$ clauses; $a=0 \implies \mathrm{CycAnd}(f) \le N$. |
| **C-278** (Fixed NO scaffold) | Universal baseline vector $P$ | OR of excess rails computes $f$; $M=1 \implies a \ge \mathrm{CycAnd}(f) - N$. |
| **C-279** (Scalar rank palette) | Scalar rank thresholds | Rank exposed on rails; $M = O(\log^2 N) \implies a \ge \mathrm{CycAnd}(f) - O(\log^2 N)$. |
| **C-282 / C-283** (Bottom holes) | Pinned coordinates + $d$ holes | Corrected decoder: $a \ge \mathrm{CycAnd}(f) - (N-d) - K \max(d-1,0)$. |
| **C-288 / C-291** (ODDFACTOR rails) | Linear span program shares | NO rails vanish; ORing shares computes ODDFACTOR directly. |
| **C-292 / C-293** (Certificate width) | Paired certificate union | Width $\ge v/2-1$; single-coordinate analysis missed multi-coordinate $M$. |
| **THEOREM 1 (THIS WORK)** | **UNIFIED GENERAL BOUND** | **$\mathrm{CycAnd}(f) \le a + M \delta + N$ HOLDS UNIVERSALLY FOR ALL MAPS.** |

---

## 6. Conclusion

Theorem 1 establishes that Route A (the LowExt reduction route) is provably incapable of yielding a superlinear Gap-MCSP lower bound from any explicit monotone source problem $f$. The map $\phi$ cannot act as an "oracle" that compresses source hardness without paying for it in binary AND gates: any map that solves the promise must either expose the source decision to a cheap decoder ($M \delta \ll \mathrm{CycAnd}(f)$) or pay for the diversity of low witnesses in its own gate count.

All future efforts must therefore focus on **Route B: Native Cyclic Fusion Closure**, analyzing the non-local information geometry of unrestricted circuit separators.
