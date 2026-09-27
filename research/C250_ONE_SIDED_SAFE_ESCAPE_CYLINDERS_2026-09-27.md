# C-250 — One-sided safe escape cylinders at seedful roots

Date: 27 September 2026  
Route: O-153, use C-249's normalized root and C-240's seed selector to constrain the first predecessor.  
Status: proved conditional width lemma; its certificate-count amplification fails at the existing C-246 ceiling.

## 1. Statement

Let \(U=\{0,1\}^N\setminus\mathrm{SIZE}(s_2)\), with \(|\mathrm{SIZE}(s_2)|<2^{N-2}\), so U two-wise shatters coordinates. Consider an empty-carrier root i with disjoint endpoints \(E_i,H_i\subseteq U\). For side S, let

\[
\mathcal S_i^S=\{(k,b): U\cap\{z:z_k=b\}\subseteq U_i^S\}
\]

be its direct seed vocabulary, where \(U_i^E=E_i\) and \(U_i^H=H_i\). Suppose \(\mathcal S_i^S\ne\varnothing\), choose \((k,b)\in\mathcal S_i^S\), and take a low table \(w\) with \(w_k=b\) on which i activates.

**Theorem.** Every opposite-side predecessor \(j\) used as a witness for this root activation, and every proof support C rooted at j with \(C\subseteq\ell(w)\), satisfies

\[
|\mathrm{free}(C)|\le \left\lceil\log_2|\mathrm{SIZE}(s_2)|\right\rceil+1.
\]

The opposite side must use a predecessor: if its direct seed vocabulary is empty this is immediate; if both sides have direct seeds, C-240 says the opposite vocabulary is exactly the complementary literal \((k,1-b)\), which does not match w.

## 2. Proof

Because \((k,b)\in\mathcal S_i^S\), the high-side half-cube

\[
L_{k,b}=U\cap\{z:z_k=b\}
\]

lies inside endpoint \(U_i^S\). The opposite endpoint is disjoint, so

\[
U_i^{\bar S}\cap L_{k,b}=\varnothing.
\]

For a predecessor \(j\) on side \(\bar S\), carrier containment gives \(T_j\subseteq U_i^{\bar S}\). The C-243 carrier lemma gives

\[
U\cap\mathrm{Cyl}(C)\subseteq T_j.
\]

Consequently no high table in \(U\cap\mathrm{Cyl}(C)\) can have bit b at coordinate k. Every Boolean table extending C and having bit b at k must therefore lie in \(\mathrm{SIZE}(s_2)\).

Let f be the number of free coordinates of C. Since C matches w, if k is fixed then it is fixed to b and all \(2^f\) completions are in SIZE(s2). If k is free, exactly \(2^{f-1}\) completions have bit b and are all in SIZE(s2). In either case \(f\le\lceil\log_2|\mathrm{SIZE}(s_2)|\rceil+1\). \(\square\)

The bound is one-sided: the half of the support cylinder on which coordinate k equals b is entirely low. The other half may contain high tables. If C itself fixes k=b, then the whole cylinder is low and the stronger \(f\le\lceil\log_2|\mathrm{SIZE}(s_2)|\rceil\) holds.

## 3. Root interpretation

For every normalized output root with a nonempty direct seed vocabulary, each low anchor matching one of those seed literals has a mandatory opposite-side predecessor whose proof supports are half-safe cylinders. If both direct seed vocabularies are nonempty, C-240 reduces the root to one complementary selector coordinate; each of its two branches has the corresponding opposite-side predecessor family. If one side is seedless, that side's predecessor family is mandatory.

Roots with no direct seed literals on either side are not covered by this lemma: their accepted proofs require predecessors on both sides, and safety comes only from the two-sided union support already analyzed in C-242/C-247.

## 4. Repeated-block test and exact failure

On the subfamily of C-234 diagonal anchors \(w_g(p,u)=g(u)\) routed through seedful roots, each associated escape support C has at most \(\kappa+1\) free table coordinates. With r repeated copies of each suffix coordinate, one such cylinder matches at most

\[
2^{(\kappa+1)/r}
\]

anchors: a suffix value can vary only if all r copies are free. Thus seedful-root escape supports have the same exponential anchor-capacity ceiling as C-246's safe output certificates. If every diagonal anchor uses this branch, exponentially many supports are required; if some anchors use roots with no direct seed literals, C-250 gives no capacity bound on that subfamily, which must be handled by the two-sided C-242/C-247 analysis.

The number of ranked proof-DAG support descriptions rooted at any of the q states is still at most

\[
q\,2^q(2N+q)^{2q}.
\]

Even under the strongest case in which all \(2^{\Theta(m)}\) anchors use seedful roots, for \(m=\Theta(s_2)=N^\beta\) the resulting certificate-count inequality is only

\[
\Theta(m)-\frac{\kappa+1}{r}
\le \log q+q+2q\log(2N+q),
\]

which is weaker than the existing q\(\ge N-o(N)\) floor at q\(=\Theta(N)\). The new half-safe lemma sharpens *which* predecessor supports are safe, but their raw count remains too large to charge q.

## 5. Learning and next obligation

The seedful root branch converts a direct endpoint literal into a half-safe predecessor cylinder. The first failed implication remains certificate count \(\Rightarrow\) state count. The needed next step is to show that half-safe predecessor supports from different roots cannot be organized independently: their common state reuse must either create a high cross-join or pay superlinear q. The seedless-root branch separately requires a two-sided context/proof join, and C-250 does not bound how many anchors it serves.

No superlinear fusion bound, near-linear full-promise cover, or P-vs-NP proof follows from C-250.

**Follow-up.** C-251 closes the local seedless/missed-seed support gap: if no direct root seed matches, the two predecessor supports have a consistent union whose whole cylinder is low. This does not change C-250's failure to charge cross-root reuse or state count. See `research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md`.
