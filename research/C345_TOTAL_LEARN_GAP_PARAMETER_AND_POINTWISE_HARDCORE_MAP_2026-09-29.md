# C-345 — Total-Learn gap parameters and the pointwise hard-core map

Date: 29 September 2026  
Route: re-audit C-344 against the formal Total-Learn quantifiers in ECCC TR26-091, then derive the strongest pointwise transfer justified by the explicit Gap-MCSP gap.  
Classification: **POINTWISE FULL-SUPPORT HARD-CORE EXISTENCE; SELECTOR/SYNTHESIS STILL OPEN; NO P-VS-NP RESULT.**

## 1. Formal learning promise and the scope correction

ECCC TR26-091 defines Total-Learn at domain dimension m by a sampler circuit of size poly(m). Its YES threshold is a circuit bound s(m); its NO condition excludes predictors up to g(s(m)) that achieve accuracy at least 1/2+epsilon. Theorem 33 states conditional NP-hardness for every subexponential g and inverse accuracy parameter. In the paper's formal convention, subexponential functions include polynomial functions, so a target choice such as g(s)=2s is allowed. [Definitions 24 and Theorem 33](https://eccc.weizmann.ac.il/report/2026/091/download/).

C-344 correctly refutes the uniform-address sampler: a high table can be within K*s2 entries of a low table and so be predicted almost perfectly under uniform addresses. Its statement that a repaired sampler would need to defeat an unspecified “subexp(s1)-size” predictor was too broad. The target gap function g is a parameter. For large choices such as g(s1) much greater than s2*n, a nearby high table has an exact predictor within the allowed size, so no distribution can make that table a NO instance. But the cited theorem also permits small polynomial choices such as g(s)=2s; the C-344 patch circuit is then too large to refute a table-conditioned hard-core distribution. Thus C-344 closes the uniform lift and large-gap settings only; it does not close the small-gap, f-dependent route.

## 2. Quantitative pointwise hard-core lemma

Let the explicit truth-table domain have N=2^n points. Let T be a circuit-size threshold and let f be any Boolean table satisfying

    CC(f) > C0 * T * (ln N + 1) / epsilon^2,

where 0<epsilon<1/2 is fixed and C0 is an absolute constant for the chosen circuit basis.

Then there is a distribution mu on addresses such that every circuit C of size at most T has error at least 1/2-epsilon under mu. To see this, consider the finite zero-sum game whose row player chooses an address x, whose column player chooses a size-T circuit C, and whose payoff is 1[C(x) != f(x)]. If no address distribution has minimum expected error at least 1/2-epsilon, minimax gives a distribution over size-T circuits whose expected error is below 1/2-epsilon at every x. Draw

    k = ceil((ln N + 1)/(2 epsilon^2))

circuits independently from that mixture and take their majority. Hoeffding's inequality and a union bound over all N addresses give positive probability that the majority equals f at every address. That majority has size O(kT), contradicting the displayed circuit-complexity assumption. Therefore mu exists.

The circuit class of size T has at most M_T=2^{O(T log(T+n))} members. Draw

    q = O((log M_T + log(1/delta))/epsilon^2)
      = O(T log(T+n)/epsilon^2)

addresses independently from mu. A second Hoeffding bound and a union bound show that some list Q of q addresses has empirical error at least 1/2-2epsilon for every size-T circuit. This is the standard finite-class sampling step. Q depends on f; no efficient selector has been obtained.

## 3. OPS-scale consequence

For the OPS thresholds

    s1 = N^beta/(c*n),   s2 = N^beta = c*n*s1,

take T=lambda*s1 for a fixed constant lambda. The minimax condition holds whenever the constants satisfy

    c > C0*lambda*ln(2)/epsilon^2,

The empirical anti-checker list then has q=O(s1*n)=O(N^beta), which is o(N) for fixed beta<1. Thus the explicit worst-case promise does give a short, table-dependent sample that defeats a constant-factor enlargement of the low circuit class, provided the fixed gap constants leave the displayed slack.

This does not imply the same for substantially larger predictor thresholds. The C-344 sphere construction gives a promised high table f with CC(f)=O(s2*n)=O(s1*n^2). Hence whenever g(s1) eventually exceeds this bound—for example g(s)=s^(1+eta) for any fixed eta>0, which is allowed by TR26-091's formal subexponential convention—the same f is exactly predictable within the learning NO class under every distribution. That obstruction is compatible with the small-gap pointwise lemma because g(s)=lambda*s is only a constant factor.

## 4. Full-support Total-Learn encoding

Given Q, form the mixture that uses Q's empirical distribution with probability 1-delta and the uniform address distribution with probability delta. Every address then has positive probability. On the Q branch, every size-T predictor has accuracy at most 1/2+2epsilon; on the uniform branch its accuracy is at most 1. Consequently its total accuracy is at most

    (1-delta)(1/2+2epsilon)+delta
      <= 1/2+2epsilon+delta/2.

Choose epsilon and delta so the right side is strictly below the target Total-Learn threshold 1/2+epsilon_L.

To meet the Total-Learn input-size convention, pad the domain to m bits and define F(y)=f(y_1...y_n), ignoring the remaining bits. Put the Q branch on inputs Q concatenated with zero suffixes, and mix in uniform m-bit inputs with mass delta. The Q-branch restriction of any m-input predictor is an n-input predictor of no greater circuit size. The uniform branch gives full support. If the target theorem uses a fixed polynomial threshold s'(m)=Theta(m^d), choose m=Theta(s1^(1/d)) so s'(m)=Theta(s1). Then N and q*m are polynomial in m, and the sampler can hardwire f's truth table and Q while staying within the required poly(m) size. The YES predictor for F uses the original low circuit on the first n bits. This verifies a pointwise, size-polynomial encoding of the distribution once Q is supplied.

The construction is not a reduction from Gap-MCSP: it has not shown how to compute Q from f in polynomial time in the explicit input length N. The predicate that a proposed Q defeats every size-T circuit has quantifier form

    forall C of size at most T, exists x in Q: C(x) != f(x),

so minimax proves witness existence but does not provide the needed selector. This is the exact synthesis bottleneck already identified by C-21/C-40 and Idea 188. Exhaustive optimization over the circuit class is far beyond polynomial time at T=Theta(s1).

## 5. Result and next proof obligation

The corrected picture is:

1. Uniform full-support sampling fails by C-344.
2. For a constant-factor predictor gap and sufficient OPS constant slack, every high table has a short, table-dependent full-support hard-core distribution; the sampler can be represented by a polynomial-size circuit after domain padding.
3. For sufficiently large g(s1), the C-344 nearby-high-table construction rules out a NO instance for some promised high tables, under every distribution.
4. The small-gap pointwise construction does not yield a computable map f -> Q, a lower bound on such maps, or a Gap-MCSP circuit lower bound.

The live mathematical target is now precise: either construct a polynomial-time / near-linear-circuit selector for the small-gap hard-core list from an explicit high table, or prove a lower bound for every such selector strong enough to cross the OPS magnification threshold. This is the same central synthesis problem as O-1/Q201, now with the learning target's gap parameter stated correctly. No superlinear native bound, near-linear full-promise cover, or P-vs-NP proof follows.
## C-346 correction: OPS slack is explicit

OPS's proof uses c=10 in s1=2^(beta*n)/(10*n). C-346 replaces the placeholder constant condition above with an explicit instantiation: minimax margin a=0.24, predictor cutoff T=ceil(1.5*s1), list-sampling loss eta=0.001, uniform mixture delta=1/1024, and Total-Learn accuracy epsilon_L=1/4. The majority circuit ratio is 125*ln(2)/96+o(1)<0.903, so every CC(f)>s2 table has the required pointwise list. The full-support sampler then has predictor accuracy below 0.742 against circuits of size T. The selector remains unconstructed. See research/C346_EXPLICIT_SMALL_GAP_FULL_SUPPORT_ENCODING_AT_OPS_CONSTANTS_2026-09-29.md.
