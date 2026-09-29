# C-346 — Explicit small-gap full-support encoding at the OPS constants

Date: 29 September 2026  
Route: close the constant-slack audit left in C-345 by using separate minimax and sampling margins at the concrete OPS parameter c=10.  
Classification: **EXPLICIT POINTWISE PROMISE-PRESERVING ENCODING; EFFICIENT SAMPLE SELECTION STILL OPEN; NO P-VS-NP RESULT.**

## 1. Parameters

The proof of OPS Theorem 1.4 explicitly establishes its circuit upper bound for

    N = 2^n,
    s1 = N^beta/(10*n),
    s2 = N^beta = 10*n*s1.

See the proof's choice s=2^(beta*n)/(10*n) and Theorem 1.4. [OPS, Theorem 1.4 and its proof](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

Let S(m)=m^d be the fixed polynomial YES threshold of the Total-Learn theorem. Choose the padded domain dimension m so that, for all sufficiently large source instances,

    s1 <= S(m) <= 1.01*s1.

This is possible by taking m to be the least integer with m^d>=s1; consecutive values differ by a relative o(1). Set the predictor threshold

    T = ceil(3*S(m)/2) <= ceil(1.515*s1),

the minimax advantage parameter a=6/25=0.24, the empirical-sampling error eta=1/1000, the full-support mixture weight delta=2^(-10), and the Total-Learn accuracy parameter epsilon_L=1/4.

## 2. Hard-core distribution for every high table

Fix f with CC(f)>s2. Consider the finite zero-sum game with addresses x as rows, size-T circuits C as columns, and payoff 1[C(x) != f(x)]. If the value were below 1/2-a, minimax would give a distribution over size-T circuits whose expected error is below 1/2-a at every address.

Draw

    k = ceil((ln N + 1)/(2*a^2))

circuits independently from this mixture and take their majority. For each x, Hoeffding bounds the majority's error by exp(-2*a^2*k) <= 1/(e*N). A union bound over all N addresses gives positive probability that this majority computes f exactly. A direct threshold-counting dynamic program implements majority with O(k^2) fan-in-two gates, so the circuit size is at most k*T+O(k^2).

The leading size ratio, using T<=1.515*s1, is

    k*T/s2 <= (1.01*125*ln(2)/96) + o(1)
            < 0.912 + o(1).

Thus k*T+O(k^2)<s2 for all sufficiently large n: the leading ratio is below 0.912, and O(k^2)=O(n^2)=o(s2) for each fixed beta>0. This contradicts CC(f)>s2. Therefore there is an address distribution mu for which every size-T circuit has error at least 1/2-a=0.26.

This fixes the constant issue in C-345: at c=10 there is room for a predictor class 1.5 times the low threshold. No unspecified “sufficiently large c” is needed.

## 3. A short list with a constant empirical margin

The number of size-T circuits is

    M_T <= 2^(O(T*log(T+n+2))).

Take q=ceil((ln M_T+1)/(2*eta^2)) independent addresses from mu. For each fixed circuit, Hoeffding bounds the probability that its empirical error is less than its mu-error minus eta by exp(-2*eta^2*q). A union bound over all M_T circuits shows that some list Q satisfies

    error_Q(C) >= 0.26 - 0.001 = 0.259

for every circuit C of size at most T. Thus each such predictor has accuracy at most 0.741 on the uniform distribution over Q.

For fixed beta>0, log(T+n)=Theta(n), so

    q = O(T*log(T+n)/eta^2) = O(N^beta) = o(N).

The constant hidden by eta=0.001 is large but fixed. Q depends on f and is not yet efficiently selectable.

## 4. Add full support and check both promise sides

Mix the Q distribution with the uniform distribution over all N addresses, using uniform mass delta=1/1024. Every address now has positive probability. For any size-T circuit C,

    Pr[C(x)=f(x)]
      <= (1-delta)*0.741 + delta
      < 0.742
      < 1/2 + epsilon_L = 0.75.

Thus the learning NO condition holds against every circuit of size at most T.

For the YES case, if CC(f)<=s1 then f itself predicts every labeled example. Pad the domain to the chosen m bits and let F(y)=f(y_1...y_n), ignoring the remaining bits. The Q branch uses addresses x concatenated with a zero suffix, while a delta-mass uniform branch on all m-bit y gives full support and labels F(y). Any predictor restricted to the Q branch induces an n-input predictor of no larger circuit size.

The sampler circuit can hardwire the N-bit table f, the q addresses in Q, and their labels. A lookup for f has size O(N*n); selecting an element of Q costs O(q*m). Since m is a fixed positive power of s1 and s1=N^beta/(10*n), both costs are polynomial in m. The mixture probabilities can be exact dyadic probabilities; Q can be padded by repetitions to a power-of-two list size.

Consequently, once Q is supplied, this is a valid pointwise reduction of the explicit low/high Gap-MCSP promise to

    Total-Learn with YES threshold S(m),
    NO predictor threshold ceil(3*S(m)/2),
    accuracy cutoff 3/4,
    and full support.

The cited conditional Total-Learn theorem permits this linear g(S)=ceil(3S/2) and constant inverse accuracy parameter. [TR26-091, Definitions 24 and Theorem 33](https://eccc.weizmann.ac.il/report/2026/091/download/).

## 5. Exact remaining gap

This is not an efficient reduction yet. For high f, the list Q is obtained by minimax and finite-class sampling. A deterministic reduction must select it from the explicit table in time polynomial in N (or by a circuit of the desired near-linear size). Validity is the relation

    forall circuits C of size at most T, exists x in Q: C(x) != f(x).

The proof establishes that each high f has such a short list; it gives no selector computing the list. For low f, any list works, so the missing operation is precisely the high-table anti-checker synthesis problem. C-345's large-gap obstruction remains true: nearby high tables of size O(s2*n) defeat targets whose g(s1) exceeds that patch size. The current construction deliberately uses the small linear gap g(S)=1.5S.

This parameter audit sharpens the next task but yields no unconditional learning hardness transfer, no general Gap-MCSP lower bound, no superlinear fusion bound, and no P-vs-NP proof.
