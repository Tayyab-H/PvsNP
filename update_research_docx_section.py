"""Insert the 23 September research follow-up into the synthesis DOCX."""

from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("P_vs_NP_Research_Synthesis_2026-09-23.docx")
CANDIDATE = Path("P_vs_NP_Research_Synthesis_2026-09-23_candidate.docx")
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
W = "{" + NS["w"] + "}"


def paragraph_text(paragraph):
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def styled_paragraph(template, text):
    result = deepcopy(template)
    ppr = result.find(W + "pPr")
    for child in list(result):
        if child is not ppr:
            result.remove(child)
    template_run = template.find(W + "r")
    run = etree.Element(W + "r")
    if template_run is not None:
        rpr = template_run.find(W + "rPr")
        if rpr is not None:
            run.append(deepcopy(rpr))
    value = etree.SubElement(run, W + "t")
    if text[:1].isspace() or text[-1:].isspace():
        value.set("{" + "http://www.w3.org/XML/1998/namespace" + "}space", "preserve")
    value.text = text
    result.append(run)
    return result


with ZipFile(DOCX, "r") as source:
    document = etree.fromstring(source.read("word/document.xml"))
    body = document.find(".//" + W + "body")
    stale_prefixes = (
        "Proposition 21.4 - global anchor-support form",
        "Let A be a finite anchor set",
        "The proof is induction on closure stages:",
        "Fractional minimax stress test -",
        "On the four-point and five-point threshold toys",
        "Transfer test for recent local decision trees -",
        "Golovnev and Gurumukhani's ECCC TR26-195 local-decision-tree model",
        "Proposition 21.5 - firing-rule circuits compile covers",
        "Let Lambda={(E_j,H_j): j in [m]}",
        "For bit-literal generators, b_X(a) is an OR of at most 2N input literals",
        "Proposition 21.6 - exact two-pair cover at the sparse-shell boundary",
        "Let n=2r+1 with r>=1",
        "For the upper bound, partition coordinates into I,J",
        "For the lower bound, any one universal pair must be disjoint",
        "For the lower bound, any universal single pair must be disjoint",
        "The six-point experiment",
        "Proposition 21.7 - proof-DAG leaves give a near-linear Gap-MCSP cover lower bound",
        "Let a universal list Lambda have m pair rules",
        "Let Lambda contain m pair rules",
        "All leaves are matching bit-literal generators",
        "Every leaf is a matching bit-literal generator",
        "For s2=N^beta with fixed beta<1",
        "An accessible local ChatGPT-project mirror contains a separate line",
        "Proposition 22.1 - projected affine controls",
        "Represent a circuit with XOR, NOT, and binary AND gates",
        "This does not assume an efficient method to find the best control set",
        "Proposition 22.2 - minimum projected control rank",
        "Given a simple graph G=(V,E) with at least one edge",
        "Choosing one input of each AND gate selects one endpoint",
        "The independent finite check in experiment_branch_rank_vertex_cover.py",
        "The independent experiment experiment_branch_rank_vertex_cover.py",
        "A read-only import of the project's affine-plus-AND solver was also checked",
        "The direction connects to established SAT work",
        "This direction connects to established SAT research on backdoor sets",
        "The open algorithmic question is whether structured instances",
        "For a supplied control choice, r is computable by linear algebra",
        "Choosing one input of each AND gate selects one endpoint of every edge",
        "Proposition 22.3 - control selection is Rank Vertex Cover",
        "Write the affine solution set as x0+L",
        "First replace each AND gate with identical inputs",
        "At each search node, maintain a basis",
        "With rank budget q, this search has depth",
        "Rank Vertex Cover is established parameterized-complexity work",
        "A read-only import of the project's rank-control solver",
        "The rank-cover check in experiment_affine_control_rank_fpt.py",
        "The remaining issue is the value of r*",
        "The affine-plus-AND branch-collapse line also gives",
        "The concrete remaining question is whether SAT instances",
        "Haoxing Lin, ECCC TR26-139",
        "Proposition 23.1 - Reed-Muller feature-span filters have a one-pair cover",
        "Let Omega={0,1}^N, let A=Omega minus U",
        "Every required literal generator G_{i,a_i}",
        "The feature image has affine dimension r=D-1",
        "The affine experiment experiment_affine_span_filter_failure.py",
        "This rules out the affine and, more broadly, all d=o(N)",
        "This rules out affine and Reed-Muller feature-span filters",
        "Ben Daniel's ECCC TR26-201 studies witness isolation",
        "Proposition 24.1 - affine-orbit interpolation gives a one-pair cover below half degree",
        "Let Omega={0,1}^N, let A=Omega minus U have size M, and let 0<=d<N/2",
        "The set B0={x: |x|<=d} has D points",
        "Choose T uniformly from the invertible affine maps",
        "The condition 2MD<2^N also implies M<2^(N-1-d)",
        "The experiment experiment_affine_orbit_unisolvent_pair.py checked",
        "This strengthens the Reed-Muller feature-span exclusion",
        "Proposition 25.1 - transitive unisolvent orbits cover q-ary feature-span filters",
        "Let Omega be a finite set of size Q, let V be a D-dimensional function space",
        "For uniform g in G and fixed a in A, transitivity makes g^{-1}a uniform",
        "For q-ary generalized Reed-Muller features, take Omega=F_q^N",
        "For any anchor set Y subset of A, define the q-ary feature-span family",
        "For fixed q and degree fraction d/(N(q-1)) tending to alpha<1/2",
        "The experiment experiment_qary_affine_orbit_pair.py checks 387 finite-field cases",
        "This q-ary extension still does not produce an uncovered semi-filter",
    )
    for paragraph in list(body.findall(W + "p")):
        if paragraph_text(paragraph).startswith(stale_prefixes):
            body.remove(paragraph)
    paragraphs = body.findall(W + "p")
    heading_template = next(
        p for p in paragraphs
        if p.xpath("./w:pPr/w:pStyle[@w:val='Heading2']", namespaces=NS)
    )
    normal_template = next(
        p for p in paragraphs
        if p.xpath("./w:pPr/w:pStyle[@w:val='NormalWeb']", namespaces=NS)
    )
    status_paragraph = next(
        p for p in reversed(paragraphs)
        if paragraph_text(p).startswith("The Clay Mathematics Institute still lists P vs NP as unsolved")
    )
    updated_status = (
        "The Clay Mathematics Institute still lists P vs NP as unsolved "
        "(https://www.claymath.org/millennium/p-vs-np/). No positive "
        "P-versus-NP result has been obtained here. The strongest new outputs are "
        "exact closure characterizations, a firing-rule circuit compilation, a sparse-shell boundary theorem, and a near-linear "
        "all-semi-filter cover lower bound for Gap-MCSP; the superlinear lower bound needed by the magnification route remains open."
        " The affine-plus-AND line yields an exact SAT algorithm in 2^O(r*) poly(N), where r* is the minimum projected affine control rank. Finding optimal controls is classically NP-hard, but it is exactly Rank Vertex Cover and is FPT in r*, so controls can be found within the same parameterized bound. Exhaustive and randomized checks passed; no small-rank bound holds for all circuits, and this is not a P-versus-NP proof. The affine-orbit cover result now extends from binary Reed-Muller features to q-ary generalized Reed-Muller spaces below half degree; this still rules out a candidate family rather than proving a circuit lower bound."
    )
    body.replace(status_paragraph, styled_paragraph(normal_template, updated_status))
    insertion_target = next(
        p for p in paragraphs
        if paragraph_text(p).startswith((
            "Relevant literature published 19-23 September 2026",
            "Relevant literature updates, 4-23 September 2026",
        ))
    )
    insertion = body.index(insertion_target)

    additions = [
        (heading_template,
         "Proposition 21.4 - global anchor-support form of preservation closure"),
        (normal_template,
         "Let A be a finite anchor set, let each anchor a have required nonempty generators G_a in a finite universe U, and let Lambda be a list of pairs (E,H). Define A_S^t as the anchors whose preservation closure contains S at stage t. Then A_S^0={a: some G in G_a is a subset of S}, and A_S^(t+1)=A_S^t union the union over (E,H) in Lambda with E intersection H a subset of S of (A_E^t intersection A_H^t). For every stage and set S, this gives exactly the same membership as running the preservation closure separately for each anchor. It is enough to store S in {empty set} union {E,H,E intersection H: (E,H) in Lambda}, with at most 3|Lambda|+1 sets. Thus Lambda covers every semi-filter above every anchor in A exactly when A is contained in A_empty^infinity."),
        (normal_template,
         "The proof is induction on closure stages: S is already present, or a listed rule has both endpoints present and its intersection is contained in S. Passing to anchor sets turns the endpoint condition into A_E intersection A_H. This is an exact joint checker that avoids enumerating all 2^|U| subsets or semi-filters. The experiment experiment_anchor_support_closure.py compares this recurrence with direct closure for every one- and two-rule list in the four-point model (32,896 lists), and for 2,048 seeded multi-rule lists plus all single rules in the five-point model (3,072 total); all tested memberships agree. The anchor-support sets may remain exponentially large for the low-circuit anchor family, so this sharpens the representation of the obstruction without proving a lower bound."),
        (heading_template,
         "Fractional minimax stress test - no scalable witness found"),
        (normal_template,
         "On the four-point and five-point threshold toys, a numerical linear program searched for an anchor-balanced distribution on anchored semi-filters minimizing the largest mass captured by any ordered pair. The solver returned 3/4 and 9/11, respectively. In each case its selected support has one equally weighted filter per anchor; exhaustive enumeration of all ordered pairs gives exact maxima of 3 of 4 and 9 of 11 filters on those supports. The LP values have no separately supplied exact dual certificate, and these finite examples imply no asymptotic trend. They do not give the vanishing single-pair influence needed for a fractional-cover proof at magnification scale. See experiment_toy_semfilter_minimax.py."),
        (heading_template,
         "Transfer test for recent local decision trees - only the baseline depth"),
        (normal_template,
         "Golovnev and Gurumukhani's ECCC TR26-195 local-decision-tree model looked relevant because sufficiently strong adaptive lower bounds imply circuit lower bounds. For Gap-MCSP, a direct counting argument gives only the baseline. Fix an accepting low-circuit table y on a correct depth-d ℓ-local decision tree. At most dℓ input positions are queried along its path, and every completion agreeing with y on those positions follows the same path. There are at most 2^{O(s2 log(n+s2))} truth tables with circuits below s2, so the completion subcube must be no larger than that count; otherwise it contains a high-circuit table, contradicting correctness. The path therefore touches at least N-O(s2 log(n+s2)) positions, giving dℓ >= N-O(s2 log(n+s2)). With s2=N^β for β<1, this is (1-o(1))N/ℓ, essentially the trivial N/ℓ bound. It gives no superconstant depth overhead and does not activate the paper's circuit-lower-bound implication. See https://eccc.weizmann.ac.il/report/2026/195/."),
        (heading_template,
         "Proposition 21.5 - firing-rule circuits compile covers into promise separators"),
        (normal_template,
         "Let Lambda={(E_j,H_j): j in [m]}, K_j=E_j intersection H_j, and b_X(a) indicate that at least one required generator for anchor a is contained in X. Set F_j^0(a)=0 and define A_X^t(a)=b_X(a) OR the OR of F_j^t(a) over j with K_j subset X, for every endpoint X and X=empty. Then F_j^(t+1)(a)=F_j^t(a) OR (A_Ej^t(a) AND A_Hj^t(a)). A_empty^m(a)=1 exactly when closure derives empty: each fired rule adds only its fixed intersection, and at most m rule flags can newly fire, so m rounds suffice."),
        (normal_template,
         "For bit-literal generators, b_X(a) is an OR of at most 2N input literals, with a_i=b included when the high-table slice B_i,b is contained in X. Hardwiring these flags costs O(Nm) gates over at most 2m endpoint sets. Unrolling m rounds costs O(m^3) additional gates. Thus a size-m universal cover yields a nonuniform De Morgan circuit separator of size O(Nm+m^3): it accepts low-circuit anchors, while every high-circuit anchor z has the principal semi-filter {S subset U: z in S}, which preserves every pair. The firing recurrence matched direct closure on 32,896 four-point and 3,072 five-point rule-list instances in experiment_anchor_support_circuit.py. The cubic overhead and hardwired slice containments do not yield the required magnification-scale lower bound."),
        (heading_template,
         "Proposition 21.6 - exact two-pair cover at the sparse-shell boundary"),
        (normal_template,
         "Let n=2r+1 with r>=1, let u_i=1^n-e_i be the n strings with exactly one zero, add v=1^n, and take anchors of weight at most r. For anchor a, its matching coordinate generator is {u_i} if a_i=0, and U minus {u_i} if a_i=1. The minimum universal cover list over all semi-filters has exactly two pairs."),
        (normal_template,
         "For the upper bound, partition coordinates into I,J with |I|=r+1 and |J|=r. The disjoint pair E={u_i:i in I}, H={u_j:j in J} covers every anchor except the one whose zero set is exactly I: every anchor has at least r+1 zeros, so its zero set intersects I, and it intersects J unless it equals I. A second disjoint pair ({u_p},{u_q}) for any distinct p,q in I covers that exceptional anchor."),
        (normal_template,
         "For the lower bound, any universal single pair must be disjoint and each side must contain a matching generator for every anchor. For a fixed anchor, two matching generators can be disjoint only when they are zero-slices {u_i},{u_j} at distinct zero coordinates: two one-slices intersect at v, and a one-slice intersects every different zero-slice. The singleton indices in each side must therefore hit every (r+1)-subset of [n], requiring at least r+1 indices per side. Since the sides are disjoint this needs 2r+2 coordinates, but n=2r+1. Thus one pair cannot suffice."),
        (normal_template,
         "The six-point experiment experiment_toy_all_semfilters_6point.py (n=5,r=2) exhaustively finds that one pair covers at most 15 of 16 anchors and verifies the explicit two-pair cover. This theorem concerns a sparse promise with singleton zero-slices. It does not transfer to Gap-MCSP, where every two-coordinate literal cylinder contains exponentially many high-circuit tables."),
        (heading_template,
         "Proposition 21.7 - proof-DAG leaves give a near-linear Gap-MCSP cover lower bound"),
        (normal_template,
         "Let Lambda contain m pair rules, and fix a low-circuit anchor a. If its preservation closure derives the empty set, choose the first rule application q whose fixed intersection K_q=E_q intersection H_q is empty. Trace each endpoint's first derivation. An endpoint is witnessed either by one initial matching literal generator contained in it, or by a rule j that fired earlier and whose fixed intersection K_j is contained in it. Memoizing each earlier rule gives an acyclic AND-DAG with at most m rule nodes, each with two antecedents. The DAG is connected to q, so it has at most m+1 generator leaves: with k rule nodes and L leaves, it has at most 2k edges and connectedness requires at least k+L-1, so L<=k+1<=m+1. Induction up the DAG shows that the intersection of all leaf generators is contained in K_q, hence is empty in U."),
        (normal_template,
         "Every leaf is a matching bit-literal generator for the same anchor, so the leaves fix a consistent set Q of at most m+1 truth-table coordinates. Their intersection is exactly the high-circuit promise restricted to the subcube that agrees with a on Q. Let M2 be the number of truth tables computed by circuits of size below s2. If 2^(N-|Q|)>M2, that subcube contains a high-circuit table, contradicting the empty intersection. Therefore rho_GapMCSP(n,beta) >= N-log2(M2)-1 = N-O(s2 log(n+s2))-1, using the standard circuit-counting bound M2 <= 2^(O(s2 log(n+s2)))."),
        (normal_template,
         "For s2=N^beta with fixed beta<1, the error is o(N), so this gives rho >= (1-o(1))N for the all-semi-filter cover measure. This is the first size-dependent lower bound in the audit, but it remains linear and falls short of the N^(1+epsilon) magnification threshold. The proof-DAG leaf argument cannot exceed N because there are only N truth-table coordinates; a stronger result must exploit structure beyond the number of literal leaves. The experiment experiment_proof_dag_leaf_bound.py traces all 263,168 anchor/rule-list cases for all one- and two-rule lists in the four-point toy; all 45,606 empty derivations have empty leaf intersection and at most k+1 leaves for k proof rules. This finite check validates the trace implementation, not the asymptotic theorem. This does not prove P != NP."),
        (heading_template,
         "Proposition 22.1 - projected affine controls give a 2^r poly(N) SAT algorithm"),
        (normal_template,
         "Represent a circuit with XOR, NOT, and binary AND gates using one variable per wire. Put the XOR/NOT equations and output=1 into an affine GF(2) system A, leaving out the AND equations. Choose one input wire from each AND gate; let B be the set of distinct chosen wires and r=dim pi_B(Sol(A)). If A is inconsistent, reject. Otherwise enumerate the 2^r patterns in this affine projection and fix the chosen wires. Each AND equation z=x AND y becomes affine: z=0 when its chosen input is 0, and z equals the other input when the chosen input is 1. Gaussian elimination decides each resulting system, giving a 2^r poly(N)-time algorithm. Since r<=|B|<=k for k AND gates, this also gives the standard 2^k poly(N) bound."),
        (normal_template,
         "For a supplied control choice, r is computable by linear algebra. If the minimum projected rank is O(log N), the combined solver is polynomial time. Section 22.3 gives an FPT method to find optimal controls, but it assumes native XOR/AND structure and does not recover affine constraints from arbitrary CNF."),
        (heading_template,
         "Proposition 22.2 - minimum projected control rank is NP-hard to find"),
        (normal_template,
         "Given a simple graph G=(V,E) with at least one edge, create input bits x_v and an AND gate y_uv=x_u AND x_v for every edge, then XOR all y_uv and require output=1. The affine relaxation A constrains only the AND-output variables through the XOR accumulator and output requirement; it leaves all primary inputs free. Therefore every chosen control set B of primary input wires has projection pi_B(Sol(A)) equal to the full Boolean cube and rank |B|."),
        (normal_template,
         "Choosing one input of each AND gate selects one endpoint of every edge, so the selected wire set is a vertex cover. Conversely, any vertex cover can select one endpoint for each edge. Thus the minimum projected rank is exactly the minimum vertex-cover size. This is an acyclic circuit with every AND gate in the output cone, so exact optimization of r is NP-hard in classical complexity. A matching of k disjoint edges gives r*=k for an O(k)-gate circuit, so there is no universal logarithmic rank bound. This does not preclude fixed-parameter tractability in r; the next result identifies the general problem and gives the corresponding branch search."),
        (normal_template,
         "The independent experiment experiment_branch_rank_vertex_cover.py enumerates all 1,098 simple graphs on 2-5 vertices and 59,808 control selections; the minimum rank always equals brute-force vertex-cover size. The general result follows from the reduction, not the finite check."),
        (heading_template,
         "Proposition 22.3 - control selection is Rank Vertex Cover and is FPT in r"),
        (normal_template,
         "First replace each AND gate with identical inputs, z=x AND x, by its affine equation z=x and include it in A. Assume the resulting affine system is consistent, with solution set x0+L and L=ker(A). Choose a basis v1,...,vd for L and associate to each wire w the vector c_w=((v1)_w,...,(vd)_w). For every wire set B, dim pi_B(Sol(A)) equals the linear rank of {c_w:w in B}. Make a graph with circuit wires as vertices and one edge between the distinct input wires of every remaining AND gate; merge duplicate edges. A valid control set is exactly a vertex cover, and its rank is exactly the projected affine rank."),
        (normal_template,
         "At each search node, maintain a basis for the span of selected control vectors. If some AND edge has both endpoint vectors outside the span, branch on either endpoint; each branch raises rank by one. If no such edge remains, every AND has an endpoint in the span, and those endpoints form a cover of rank at most the current budget. For completeness, a rank-q cover always contains an endpoint of every uncovered edge, so following that endpoint keeps the current span inside the cover's span and reaches a successful node within q branches."),
        (normal_template,
         "With rank budget q, this search has depth at most q and at most 2^(q+1)-1 nodes. Iterative deepening finds a minimum-rank control cover r* in 2^O(r*) poly(N) time. Enumerating its 2^r* affine projection patterns and solving each slice by Gaussian elimination takes the same asymptotic time. Thus full control discovery plus SAT decision is 2^O(r*) poly(N), with an exponential worst case when r* is large."),
        (normal_template,
         "The rank-cover check in experiment_affine_control_rank_fpt.py matched exhaustive minima on all 1,098 identity-matroid graphs through five vertices, all 16,384 simple four-vertex graphs paired with binary vector representations, and 1,000 random represented-matroid instances. The integrated affine-control SAT solver in experiment_affine_control_rank_sat.py matched exhaustive SAT on 2,500 random small systems, with 1,039 SAT and 1,461 UNSAT. It also solved shared-control instances with 8, 64, and 256 AND gates at rank one, using three search nodes each. These checks validate the implementation only."),
        (normal_template,
         "Rank Vertex Cover is established parameterized-complexity work. Meesum, Panolan, Saurabh, and Zehavi use it for algebraic compression (https://arxiv.org/abs/1705.02822); a 2024 ESA paper notes that Rank Vertex Cover is folklore FPT parameterized by rank (https://drops.dagstuhl.de/storage/00lipics/lipics-vol308-esa2024/LIPIcs.ESA.2024.17/LIPIcs.ESA.2024.17.pdf). The project contribution here is recognizing that the affine projection rank is exactly this known objective and composing control search with affine-slice SAT; the FPT branching principle itself is not claimed as new."),
        (normal_template,
         "The remaining issue is the value of r* on unrestricted circuits and whether useful affine structure can be recovered from arbitrary SAT encodings. No universal small-rank theorem, polynomial-time all-SAT algorithm, or P-versus-NP consequence emerged. This is an exact parameterized algorithm for a structured slice of SAT, not a breakthrough resolving the open problem."),
    ]
    additions.extend([
        (normal_template,
         "Ben Daniel's ECCC TR26-201 studies witness isolation from circuit descriptions. Under indistinguishability obfuscation, a randomized polynomial-size pruning procedure that isolates every nonempty affine-subspace input with probability at least a/log L would imply NP subseteq P/poly; iO together with nonuniformly secure one-way functions rules out such an isolator. In a membership-query-only model, subexponential query budgets still allow only Theta(1/n) worst-case isolation probability on affine targets. This is a conditional barrier to generic witness-picking routines, not an unconditional P-versus-NP result, and it does not apply to the exact 2^O(r*) poly(N) decision algorithm above. See https://eccc.weizmann.ac.il/report/2026/201/."),
        (heading_template,
         "Proposition 23.1 - Reed-Muller feature-span filters have a one-pair cover"),
        (normal_template,
         "Let Omega={0,1}^N, let A=Omega minus U be all tables below the high-complexity threshold s2, with |A|<=M=2^(O(s2 log(n+s2)))=2^o(N) for s2=N^beta and fixed beta<1. The low-circuit anchors Y are a subset of A. Let d<N and map each x to phi_d(x), the vector of all squarefree monomials of degree at most d evaluated at x; its dimension is D=sum_{j<=d} binomial(N,j). The proof applies when M<2^(N-1-d) and D+1<2^(N-d)-M. These inequalities hold for every d=o(N); for fixed d/N tending to alpha<1/2, the second holds when H_2(alpha)<1-alpha, where H_2 is binary entropy. The equality occurs at alpha*=about 0.22709. For each low-circuit anchor a in Y define F_{a,d}={S subset U: phi_d(a) lies in the affine F_2-span of phi_d(S)}, taking the affine hull of the empty set to be empty. These families are upward closed and exclude the empty set, so they are semi-filters."),
        (normal_template,
         "Every required literal generator G_{i,a_i}=U intersect {x:x_i=a_i} belongs to F_{a,d}. If not, affine separation gives a nonzero degree-d Boolean polynomial that is 1 at a and vanishes on all high-circuit points in that coordinate slice. Its restriction is a nonzero Reed-Muller codeword RM(d,N-1), with weight at least 2^(N-1-d), but its support would lie among at most M low tables, contradiction. Likewise phi_d(U) spans phi_d(Omega), since a nonzero degree-d polynomial has weight at least 2^(N-d)>M. The Reed-Muller minimum-distance formula is classical; see Delsarte, Goethals, and MacWilliams (1970), https://doi.org/10.1016/S0019-9958(70)90214-7."),
        (normal_template,
         "The feature image has affine dimension r=D-1, with at most 2^(r+1)=2^D affine hyperplanes. Each proper hyperplane misses at least delta=2^(N-d)-M points of U. Color U independently with two colors. For one specified color and one hyperplane, the probability that all outside points receive that color is at most 2^(-delta); a union bound over both colors and all hyperplanes gives failure probability at most 2^(D+1-delta)<1, since D=2^o(N) and delta=2^(N-o(N)). Thus there is a disjoint partition U=E union H with both parts spanning the full feature space. Every low anchor feature lies in both spans, so E,H belong to every F_{a,d} for a in Y, while E intersect H is empty and is excluded. One pair covers the entire low-degree feature-span family."),
        (normal_template,
         "The affine experiment experiment_affine_span_filter_failure.py checks all 696 excluded sets of sizes one through three in a four-bit cube. The Reed-Muller experiment experiment_low_degree_span_filter.py uses degree-two features on an eight-bit cube (37 monomials), checking all 256 single-anchor exclusions and 512 seeded exclusions of sizes two or three. All literal-slice membership and full-span partition checks passed. The finite checks validate the code only; the asymptotic conclusion follows from Reed-Muller distance and the probabilistic union bound."),
        (normal_template,
         "This rules out affine and Reed-Muller feature-span filters satisfying the distance-versus-dimension conditions as sources of a cover lower bound. In particular it covers every d=o(N) and every fixed degree fraction below alpha* about 0.22709. This entropy cutoff is where this union-bound proof stops, not a demonstrated boundary for the filter family. It does not upper-bound the full cover complexity or prove P unequal NP: arbitrary semi-filters need not arise from feature-space span, and an uncovered filter against every short pair list remains to be constructed."),
        (heading_template,
         "Proposition 24.1 - affine-orbit interpolation gives a one-pair cover below half degree"),
        (normal_template,
         "Let Omega={0,1}^N, let A=Omega minus U have size M, and let 0<=d<N/2. Put D=sum_{j<=d} binomial(N,j), and use phi_d for the degree-d monomial evaluation map. If 2MD<2^N, then the degree-d feature-span filters for any anchor set Y subset of A have a disjoint pair E,H that belongs to every filter, provided the coordinate-literal generators from Section 23 are included."),
        (normal_template,
         "The set B0={x: |x|<=d} has D points. Its evaluation matrix, with rows and columns indexed by subsets S,T of size at most d, has entry 1[T subseteq S]; ordering by inclusion makes it triangular with diagonal one. Thus B0 is unisolvent. Its complement image B1={x: |x|>=N-d}, obtained by x->x+1^N, is also unisolvent because affine substitution preserves the degree-d polynomial space. Since 2d<N, B0 and B1 are disjoint. Every invertible affine map T preserves these facts."),
        (normal_template,
         "Choose T uniformly from the invertible affine maps. For each fixed a in A, T^{-1}(a) is uniform on Omega, so the probability that a lies in T(B0) union T(B1) is 2D/2^N. A union bound over A gives failure probability at most 2MD/2^N<1. Hence some T avoids A on both sets; set E=T(B0), H=T(B1). Each feature set spans the full linear feature space. The constant feature is one, so every linear representation of phi_d(a) has coefficient sum one and is also an affine representation. Thus E,H belong to every filter and are disjoint."),
        (normal_template,
         "The condition 2MD<2^N also implies M<2^(N-1-d), since D>=2^d. The literal-generator proof from Section 23 therefore applies: any affine separator restricts to a nonzero degree-d polynomial on an (N-1)-dimensional slice, with Reed-Muller weight at least 2^(N-1-d)>M. If M=2^o(N), then 2MD<2^N whenever d=o(N), and for every fixed d/N tending to alpha<1/2 because D=2^(H_2(alpha)N+o(N)) with H_2(alpha)<1."),
        (normal_template,
         "The experiment experiment_affine_orbit_unisolvent_pair.py checked 208 seeded excluded-set instances for N=4 through 7 and degrees one or two. It found disjoint transformed interpolation sets avoiding A, verified both feature matrices have full rank, checked every anchor lies in both affine hulls, and tested all matching coordinate-literal generators. The finite checks validate the implementation; the proof is the interpolation and affine-group argument above."),
        (normal_template,
         "This strengthens the Reed-Muller feature-span exclusion from the earlier random-coloring cutoff alpha* about 0.22709 to every fixed alpha<1/2. The ingredients are classical interpolation and Reed-Muller distance with an affine-orbit averaging argument. It rules out this candidate family as a source of a cover lower bound; it does not bound full cover complexity or resolve P versus NP. Constructing an uncovered semi-filter outside this feature-span family remains open."),
        (heading_template,
         "Proposition 25.1 - transitive unisolvent orbits cover q-ary feature-span filters"),
        (normal_template,
         "Let Omega be a finite set of size Q, let V be a D-dimensional function space over F containing the constant-one function, and let a transitive group G act on Omega while preserving V. Suppose V has two disjoint information sets B0 and B1, each of size D. If A subset Omega has size M, U=Omega minus A, and 2MD<Q, then some g in G maps both information sets into U. With phi the evaluation map of a basis of V, the sets E=g(B0) and H=g(B1) are disjoint and each feature image spans F^D."),
        (normal_template,
         "For uniform g in G and fixed a in A, transitivity makes g^{-1}a uniform on Omega. The probability it lands in B0 union B1 is 2D/Q. A union bound over A is less than one, so a map avoiding A exists. Since phi includes the constant feature, every linear representation of phi(a) has coefficient sum one and is therefore an affine representation. Thus E and H belong to every anchored feature-span filter. If every coordinate-slice restriction of a nonzero function in V has support greater than M, affine separation also proves that the required coordinate-value generators belong to the filters."),
        (normal_template,
         "For q-ary generalized Reed-Muller features, take Omega=F_q^N and V spanned by reduced monomials x^e with 0<=e_i<q and sum(e_i)<=d. Let D be their number. Choose alphabet levels lambda_0,...,lambda_(q-1) reversed by an affine involution tau(x)=c-x, and define B0 by index vectors k with sum(k_i)<=d; let B1=tau^N(B0). Newton polynomials product_i product_(j<e_i)(x_i-lambda_j) give a basis whose evaluation matrix on B0 is triangular with nonzero diagonal. Thus both sets are information sets, and they are disjoint whenever 2d<N(q-1). The affine group preserves V and acts transitively on Omega."),
        (normal_template,
         "For any anchor set Y subset of A, define the q-ary feature-span family by S in F_(a,d) exactly when phi_d(a) lies in the affine F_q-span of phi_d(S). If M<delta_q(d,N-1), where delta_q is the minimum distance on an (N-1)-coordinate slice, every matching coordinate-value generator belongs to each family: otherwise separation gives a nonzero restricted codeword supported inside A. Writing d=a(q-1)+b with 0<=b<q-1, the classical distance is delta_q(d,m)=(q-b)q^(m-a-1). See Kasami, Lin, Peterson (1968) and Delsarte, Goethals, MacWilliams (1970), https://doi.org/10.1016/S0019-9958(70)90214-7."),
        (normal_template,
         "For fixed q and degree fraction d/(N(q-1)) tending to alpha<1/2, both 2MD<q^N and M<delta_q hold when M=2^o(N). The dimension ratio D/q^N is a lower-tail probability for the sum of N uniform digits in {0,...,q-1}, exponentially small below half the mean; the slice distance is also exponential in N. The experiment experiment_qary_affine_orbit_pair.py checks 387 finite-field cases over F_3 and F_5, verifying pair disjointness, full feature rank, anchor affine-span membership, and coordinate-slice membership."),
        (normal_template,
         "This q-ary extension still does not produce an uncovered semi-filter or a superlinear all-semi-filter cover lower bound. It extends the project-level obstruction to a broader family of equivariant algebraic feature constructions and identifies a property a successful feature design must evade: two small disjoint information sets in a transitive feature space."),
    ])
    for offset, (template, text) in enumerate(additions):
        body.insert(insertion + offset, styled_paragraph(template, text))

    literature_heading = next(
        p for p in body.findall(W + "p")
        if paragraph_text(p).startswith((
            "Relevant literature published 19-23 September 2026",
            "Relevant literature updates, 4-23 September 2026",
        ))
    )
    updated_literature_heading = styled_paragraph(
        literature_heading, "Relevant literature updates, 4-23 September 2026"
    )
    body.replace(literature_heading, updated_literature_heading)
    literature_note = (
        "Haoxing Lin, ECCC TR26-139, revision 2 (4 September 2026), proves unconditional fine-grained AC0 size lower bounds for k-OV, k-XOR, and k-SUM through depth-zero projections from colored subgraph isomorphism. At fixed depth the bounds scale as n^(Omega(k)) for the stated parameter ranges, with additional growing-k bounds for selected gate orientations. These results concern bounded-depth circuits and fine-grained targets; they supply no transfer to general Boolean circuits or Gap-MCSP, so they do not provide the superlinear cover lower bound needed by the magnification route. See https://eccc.weizmann.ac.il/report/2026/139/."
    )
    body.insert(
        body.index(updated_literature_heading) + 1,
        styled_paragraph(normal_template, literature_note),
    )
    updated_xml = etree.tostring(document, xml_declaration=True, encoding="UTF-8", standalone=True)
    with ZipFile(CANDIDATE, "w", compression=ZIP_DEFLATED) as target:
        for entry in source.infolist():
            contents = updated_xml if entry.filename == "word/document.xml" else source.read(entry.filename)
            target.writestr(entry, contents)

print(f"Wrote {CANDIDATE}")
