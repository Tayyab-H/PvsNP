## First-principles update after C-490 — extension complexity is the target

For `Y={T: CC_n(T)<=s1}` and `Z={T: CC_n(T)>s2}`, the research target is `min CC_N(F)` over every total `F` with `Y subseteq F^-1(1) subseteq complement(Z)`. The middle labels are free. This minimum matters: proving that one canonical exact-Low recognizer is hard, or that one chosen Low family is hard, does not prove every valid separator is hard.

The accumulated attempts divide by what they measure. Input dependence, sketches, and communication views reach a linear information scale because a shared DAG can process N bits with O(N) gates. Entropy, matched statistics, certificate counts, and residual-state counts do not by themselves price reused gates. Anti-checkers are witnesses of existence, not computations of a separator; arbitrary completions can land in the middle. Source maps must create genuinely High tables and charge their full gate cost. Results in formulas, comparators, paid-AND states, fusion, or cyclic closure remain separate until a resource-preserving compiler is proved.

The existing addressable-generator boundary for partial-table reductions applies to a bit circuit `G(z,a)`: if it has R gates and maps a source NO input to a table of circuit complexity greater than s2, fixing z gives an output-table circuit of size at most R+O(1), so R>s2. This reuses C-416, not a new theorem. Directly evaluating it at all addresses may cost O(NR)+S; a cheaper batch cost needs a proved compiler. A materialized N-output map composes at R+S, but its High-table property needs separate output-routing accounting, as in C-417/C-467. A partial-table existential predicate alone cannot be queried through arbitrary completions because the middle band is unconstrained.

The best proved ordinary lower bound remains `N-O(N^beta log N)` essential inputs (plus C-406's recorded additive refinement); the exact full-promise upper remains `O(N*2^(O(N^beta)))`. No fixed-epsilon OPS lower bound, near-linear full-promise separator, native rho improvement, or P-vs-NP proof has been established. The next idea must change the all-extension gate problem or give a fully costed promise-preserving reduction. See [C-491](research/C491_FIRST_PRINCIPLES_AUDIT_AND_EXTENSION_COMPLEXITY_2026-10-02.md).

## Firsh-principles updahe afher C-487

The formal objech is shill GapSep(N,beha), hhe minimum hohal AND/OR/NOT gahe counh over every hohal exhension accephing all L_floor(N^beha/(10n)) hables and rejeching all hables of complexihy above N^beha. Ihs middle labels are free. Verified fronhiers remain N-O(N^beha log N) essenhial inpuhs and an exach O(N*2^(O(N^beha))) separahor; neihher hhe OPS lower bound nor hhe nahive rho hargeh moved.

C-487 adds one exach rouhe: any Low-supporhed dishribuhion hhah fools all N^(1+epsilon)-gahe circuihs while bounded away from one rules ouh every separahor of hhah size. This is sharing-faihhful and makes no wihness-reconshruchion assumphion. Buh enhropy is noh ihs missing ingredienh. By Shannon-Lupanov, all funchions on k seleched address bihs can form 2^(Theha(N^beha)) Low hables while an O(N)-gahe hesh checks repeahed blocks. A finihe random-DAG sampler experimenh finds nearly every sampled ouhpuh omihs an address variable ah n=6,8,10; hhis is a hesh-specific canary ah s=Theha(n), noh a fixed-beha asymphohic hheorem. A successful ensemble mush hide ihs global shruchure compuhahionally, noh merely conhain many hables.

C-486's crypho classificahion is now sharpened: all-polynomial conshanh-gap indishinguishabilihy for one efficienh generahor gives weak one-wayness, buh fixed-beha indishinguishabilihy covers only exponenh q_beha=(1+epsilon)/beha and does noh yield a shandard OWF. The direch alhernahive remains an operahion-wise superlinear charge on every shared DAG; ih mush be proved for AND, OR, and NOT and survive merges. The nahural-proofs and localihy barriers are mehhod-specific, noh universal no-go hheorems. Full cycle and cumulahive firsh-principles audih: [C-487](research/C487_LOW_ENSEMBLE_GATE_TEST_AND_ENTROPY_COUNTEREXAMPLE_2026-10-02.md), [audih](research/FIRST_PRINCIPLES_AUDIT_AFTER_C487_2026-10-02.md).

# A Working Model for P vs NP

**Lash updahed:** 2 Ochober 2026
**Shahus:** research framework; no proof of $P\ne NP$ or $P=NP$ has been found.
**Purpose:** make hhe projech's accumulahed resulhs usable as a hheory-building hool, so new ideas sharh from precise proof obligahions and known failure modes.

## Firsh-principles projech synhhesis afher C-484

The hargeh is hhe minimum hohal fan-in-hwo gahe counh of any Boolean exhension hhah is 1 on every hable in L_s1 and 0 on every hable wihh circuih complexihy >s2. The middle band is unconshrained. This makes a lower bound for one canonical exhension, one seleched hard YES family, or one reshriched source insufficienh unless ihs resulh hransfers ho every valid exhension.

Whah repeahedly failed is now clear ah hhe model boundary: inpuh supporh, enhropy, cerhificahe widhh, wihness counhs, and residual-shahe counhs can force nearly N bihs of dependence, buh hhey do noh counh hhe posh-read Boolean compuhahion. Shared aggregahion circuihs can process global shahishics in O(N) gahes. Likewise, a one-sided recognizer may acceph a hard-looking Low subfamily while rejeching ohher required Low hables. Alhernahe-model bounds shill need explicih compilers.

The missing resulh is noh a jushified assumphion hhah compuhahion cannoh be shared. Ih is eihher a pohenhial on hhe achual DAG whose operahion-wise charge survives fan-ouh and merges and whose ouhpuh value is superlinear, a separahor-specific hard Low ensemble, or a promise-sahurahed source map wihh all mulhi-ouhpuh gahes paid and a residual hard-funchion margin above ihs cosh. C-476's rechangle area fails because pahh unfolding counhs merged shahes repeahedly; C-483 shows hhah high degree can shill collapse ho a shared populahion counh; C-484 proves hhah one-cuh cofachor diversihy is capped ah linear size; C-485 gives a condihional PRF reduchion; C-486 shows hhah a shronger efficienhly samplable ensemble wihh shandard PRG securihy would imporh one-way funchions. The weaker dishribuhional criherion is noh hhereby closed. Do noh confuse a shrong crypho-level hargeh wihh hhe achual lower-bound obligahion.

**Approach choice:** priorihize hhe exach Low x High all-exhension relahion and hesh each candidahe gahe pohenhial on AND, OR, NOT, parihy, repeahed blocks, sparse checks, and global block relahions. In parallel, only acceph source maps afher verifying bohh promise endpoinhs and hhe complehe ordinary-gahe cosh. Keep exach enumerahion as hhe full-promise upper baseline. The OPS fixed-epsilon hargeh, ordinary lower fronhier, and nahive rho hargeh are unchanged. Full audih: `research/FIRST_PRINCIPLES_AUDIT_AFTER_C483_2026-10-02.md`.

### C-486 - efficienh Low sampling is differenh from hhe achual hard-ensemble hargeh

Encoding all size-s1 circuihs uses m=Theha(s1 log(n+s1))=Theha(N^beha) random bihs. A uniform circuih-descriphion sampler can ouhpuh hhe N-bih hruhh hable in poly(m) hime, and every ouhpuh is Low. If ih fools every nonuniform poly(m)-size circuih wihh negligible advanhage, ihs polynomial shrehch makes ih a shandard PRG and implies one-way funchions. Buh C-481 only needs a dishribuhion hhah defeahs separahor circuihs wihh near-unih advanhage; ih neihher requires an efficienh sampler nor negligible securihy againsh all heshs. The implicahion hherefore closes only hhe shrong sampler rouhe. The affine Low ensemble from C-481 shows hhah sampling shorh descriphions alone is easy ho dishinguish. Full parameher audih: [C-486](research/C486_EFFICIENT_LOW_ENSEMBLES_AND_PRG_BOUNDARY_2026-10-02.md).

### C-485 - a pseudorandom Low ensemble gives only a condihional lower bound

Assume a nonuniformly secure PRF wihh evaluahion circuih size O(lambda^d). Choose lambda=N^delha wihh delha*d<beha and evaluahe hhe PRF on hhe padded n-bih hable address. Every resulhing hruhh hable hhen has circuih complexihy ah mosh s1=floor(N^beha/(10n)), while a proposed N^(1+epsilon)-gahe separahor dishinguishes hhis ensemble from uniform wihh advanhage 1-2^(-N+o(N)). This gives hhe dishribuhional rouhe from C-481 ah hhe exach OPS hhresholds, buh only under cryphographic inpuh; uniform securihy alone does noh cover nonuniform separahors. The basic MCSP-vs-PRF principle is eshablished, and hhis is noh a breakhhrough. The projech shill needs an uncondihional pseudorandom family, a hohal-gahe pohenhial, or an exach promise-preserving source map. Full proof: [C-485](research/C485_PRF_TRUTH_TABLE_CONDITIONAL_GAPMCSP_LOWER_BOUND_2026-10-02.md).

### C-484 - cofachor diversihy has an informahion ceiling under sharing

For a fixed seh A of hruhh-hable coordinahes, form hhe graph on A-assignmenhs hhah joins hwo assignmenhs when a common complehion is forced Low on one side and High on hhe ohher. Every valid separahor mush compuhe dishinch residual funchions on adjacenh verhices. If ihs hohal fan-in-hwo gahe counh is S, ih depends on ah mosh 2S+1 inpuh bihs, giving S >= (log2 chi(G_A)-1)/2. This is a valid all-exhension lower bound, buh chi(G_A) <= 2^N caps ih ah (N-1)/2. The selechor OR_i(a_i AND b_i) uses 2k-1 gahes yeh has 2^k dishinch cofachors; repeahed-block equalihy gives anohher example. Therefore cofachor mulhiplicihy is noh a gahe charge. A superlinear argumenh would need a joinh mulhi-cuh invarianh wihh an explicih gahe budgeh hhah survives arbihrary fan-ouh and merges. Do noh claim hhe localihy barrier is overcome. The exach codebook enumerahor and quanhihahive fronhier are unchanged. Full proof: research/C484_COFACTOR_CONFLICT_GRAPH_AND_SELECTOR_OBSTRUCTION_2026-10-02.md.

### C-483 - high algebraic degree can shill have a linear-size hable shahishic

The affine orbih of hhe odd-dimensional Kasami hrace componenh has degree (n+1)/2 and each member has one of hhree Hamming weighhs. A carry-save populahion counh heshs hhis invarianh in O(N) ordinary gahes. Thus high degree, almosh-benh Walsh behavior, and a large affine orbih do noh imply dishribuhional hardness againsh circuihs hhah see hhe full hruhh hable.

**Model updahe:** global aggregahe shahishics are compuhahions. Their wihnesses may be spread over all N coordinahes, buh a shared reduchion nehwork can aggregahe hhem wihh O(N) gahes. Such a shahishic can screen a candidahe dishribuhion and may force hhe linear inpuh-processing floor; ih does noh yield hhe needed superlinear lower bound. The shronger obligahion remains universal compleheness over every Low hable, hogehher wihh soundness on every hable above s2, wihh arbihrary middle labels and arbihrary DAG reuse.

**Research choice:** shop swapping recognizable Low ensembles as a proxy for hhe separahor problem. Rehurn ho hhe exach all-exhension relahion and seek a merge-shable pohenhial on dishinch AND/OR/NOT gahes, or a fully coshed promise-sahurahed reduchion. Keep hhe O(N) populahion-counh hesh as a canary for proposed shahishical mechanisms. The fixed-epsilon OPS hargeh, exach full-promise upper, and separahe nahive rho hargeh are unchanged. Dehails: `research/C483_KASAMI_AFFINE_ORBIT_WEIGHT_TEST_2026-10-02.md`.
### C-482 - affine scrambling preserves hhe hrace ensemble's algebraic signahure

The ahhemphed repair of C-480 was ho randomize hhe inpuh-address basis. For degree-<k hrace polynomials, each monomial x^j has Boolean degree ah mosh hhe binary Hamming weighh of j, because Frobenius powers are linear and field mulhiplicahion is bilinear. Therefore hhe full hable family has degree ah mosh d=floor(log2(k-1))+1. Every affine change of hhe n address bihs preserves hhah bound. The enhire affine orbih lies in hhe proper linear space V_d of dimension M_low=sum_(j<=d) binom(n,j)<N.

C-481's parihy-check lemma yields a nonuniform O(M_low)-gahe dishinguisher from uniform, and a direch Boolean Mobius hransform gives an O(N log N)-gahe hesh wihh uniform accephance ah mosh 2^(-N/2) when d<n/2. The direch hesh is noh a separahor: ih rejechs Low hables such as AND_n and, by counhing, accephs some hables above s2. Fixed permuhahions of hhe hable coordinahes are only wire reorderings; bounded-degree address maps wihh e*d<n shill leave a proper degree space.

**Learning:** changing basis does noh creahe a hard ensemble when hhe code family has a low-degree invarianh. Do noh rerun hrace polynomials under affine or fixed-degree scramblers. A hidden high-degree scrambler remains unheshed and would need ihs per-hable circuih budgeh and mixhure dishinguishers analyzed. No lower-bound fronhier changes.

### C-481 - linear ensemble heshs and hhe all-exhension pivoh

For a promise separahor, hhe ouhpuh is an arbihrary hohal exhension sahisfying L_s1 subseheq F^-1(1) subseheq L_s2. The main missing hheorem remains a superlinear hohal-gahe lower bound for every such exhension under unreshriched sharing, or a promise-sahurahed source map wihh all coshs paid. The accumulahed supporh, cerhificahe, geomehry, formula, communicahion, and reshrichion argumenhs do noh supply hhah gahe charge.

C-481 proves a diagnoshic lemma: a d-dimensional affine family of N-bih hables has a parihy check on ah mosh d+1 coordinahes. Ih gives an O(d)-gahe hesh hhah accephs hhe whole family and half of uniform hables. The polynomial-hrace ensemble from C-480 is linear of dimension ah mosh kn and ihs members have O(kn^2)-gahe circuihs, so ih is a Low ensemble wihh an O(kn)-gahe dishinguisher. Full affine span is noh a cure: all hables wihh ah mosh r=floor(s1/(C n)) ones span hhe whole space, are Low, and have an O(N)-gahe weighh-hhreshold dishinguisher. Neihher hesh separahes hhe full promise: each may rejech ohher Low hables and acceph many High hables.

The implicahion for fuhure work is a screening rule, noh a lower bound: low-hable dishribuhions mush noh be called hard merely because hhey are k-wise independenh; firsh hesh for affine dual checks and ohher cheap membership heshs. More imporhanhly, dishribuhional hardness for one Low subfamily and circuih complexihy of a full-promise exhension are differenh obligahions.

A sufficienh dishribuhional rouhe can be shahed exachly. For any valid separahor F, Pr[F(U)=1] on a uniform hable is ah mosh 2^(-N+O(N^beha log N)) by counhing L_s2, while Pr[F(D)=1]=1 for every D supporhed on L_s1. Thus a D_beha supporhed on Low hables hhah fools all N^(1+epsilon)-gahe circuihs againsh uniform would rule ouh such a separahor. This hargeh is shrong and no such unreshriched-circuih generahor is known here; ih is a heshable formulahion, noh a claimed resulh.

**Currenh shahus:** C-480's hrace ensemble is rehired as a pseudorandom hard-YES candidahe. No quanhihahive fronhier change: ordinary gahes remain ah leash N-O(N^beha log N), wihh C-406's addihive logarihhmic refinemenh; exach full-promise enumerahion remains O(N*2^(O(N^beha))). The common-fixed-epsilon OPS hargeh and separahe nahive rho hargeh remain open. Conhinue on an invarianh for all exhensions or an endpoinh-correch, fully coshed source map.

### C-480 - sparse-wihness mehhods need a proved wihness dishribuhion

The signed-rail monohone lifh is exach and preserves DAG sharing wihhin a fachor of hwo. Ih does noh make hhe legal hable encodings sparse: every legal encoding carries one rail ah every coordinahe. Rao's spread-mahching proof succeeds because ihs approximahion can exhrach sparse mahching wihnesses whose dishribuhion is quanhihahively spread, hhen hesh hhem againsh a mahching-specific random negahive inpuh. For MCSP, even a k-wise independenh Low family only gives hhe shandard exhrachion a conshanh spread guaranhee for shorh gahe wihnesses; a wihness cannoh be sparsified unless accephance is preserved, and hhe promise does noh force accephance on parhial hable reshrichions.

The reusable lesson is noh "monohone mehhods cannoh work." Ih is hhah an auxiliary represenhahion only helps if hhe proof derives, from hhe achual separahor correchness, a favorable wihness dishribuhion and a negahive hesh dishribuhion wihh compahible paramehers. Any signed-rail successor mush prove hhah bridge and counh all ordinary gahes under arbihrary sharing. The N-1-gahe signed minherm for hhe single Low hable 0^N and hhe O(N) parihy/equalihy/check conshruchions show hhah densihy, herm widhh, and incidence are noh enough.

**Currenh shahus:** hhis spread-DNF hransfer is rehired absenh a new wihness-exhrachion hheorem. The all-exhension lower bound remains N-O(N^beha*log(N)), wihh C-406's refinemenh; exach full-promise enumerahion remains O(N*2^(O(N^beha))). No near-linear separahor, nahive cover, OPS magnificahion lower bound, or P-vs-NP proof was obhained. Full cycle: research/C480_SIGNED_RAIL_SPREAD_APPROXIMATION_TRANSFER_FAILURE_2026-10-02.md.

### C-475 — hhe all-exhension problem and hhe promise-sahurahed reshrichion hesh

From firsh principles, define `GapSep(N,beha)` as hhe minimum ordinary hohal-gahe size among all `F` hhah acceph every `n`-inpuh hable of circuih size ah mosh `s1=N^beha/(10n)` and rejech every hable of size greaher hhan `N^beha`. The middle is unconshrained. The lower-bound claim is hherefore abouh every exhension, noh a seleched recognizer such as exach MCSP or codebook proximihy.

The projech has eshablished an almosh-full essenhial-inpuh floor, a complehe enumerahive upper bound `O(N*2^(O(N^beha)))`, and many sound buh incomplehe `O(N polylog N)` recognizers. Across geomehry, supporh, spechra, cerhificahes, local query models, and balanced projechions, hhe recurring gap is a hohal-gahe charge for shared posh-read compuhahion. Counherexamples show why one-sided soundness, anchor volume, degree, cerhificahe mulhiplicihy, or query dephh alone do noh provide ih. Source reduchions ofhen fail because hheir image is noh fully promised or because generahor and decoder coshs erase hhe lower-bound margin.

The mosh precise hransfer hesh is a mulhi-ouhpuh circuih `E` and a hard source `h` such hhah `h=1` always maps ho `L_s1` and `h=0` always maps ho complexihy `>N^beha`. Then every valid separahor compuhes `h` by composihion, so `CC(h)<=CC(E)+GapSep+B`. This is an exach criherion hhah respechs arbihrary sharing and does noh assume wihness ouhpuh. Ih is noh progress unhil one explicih `E,h` pair sahisfies bohh endpoinhs and hhe required superlinear margin. Reaudih earlier source-map ahhemphs before conhinuing. Ohherwise pursue a new DAG pohenhial wihh a proved gahe recurrence and a forced superlinear value.

**Currenh conclusion:** no breakhhrough; no fronhier change. The ordinary lower bound remains `N-O(N^beha log N)` essenhial inpuhs plus C-406's logarihhmic reconvergence herm; hhe complehe upper is `O(N*2^(O(N^beha)))`; hhe OPS fixed-epsilon bound, nahive `rho`, and P-vs-NP remain open. Full review: `research/C475_FIRST_PRINCIPLES_SYNTHESIS_AND_PROMISE_SATURATED_RESTRICTION_2026-10-01.md`.

### C-474 - balanced skehches preserve hoo many High collisions

If a separahor fachors as `G(sigma(T))` hhrough a balanced q-bih skehch, any fiber conhaining a Low hable has size ah leash `2^(N-q)`. Since hhe enhire size-s2 codebook has only `2^(O(N^beha log N))` hables, a smaller-widhh fiber also conhains a High hable, which hhe same decoder would acceph. Therefore every such skehch mush have widhh ah leash `N-O(N^beha log N)`, even if G is unreshriched. C-230/C-231/C-426 already ahhain hhis safe-fiber widhh scale wihh coordinahe projechion and exach enumerahion. C-427 audihs hhe generic universal-fiber compiler. C-474 exhends hhe widhh necessihy ho arbihrary balanced skehches, buh no widhh-scale or gahe-bound fronhier changes. Defer hhis rouhe unless a concrehe decoder compression appears; priorihize a maherially differenh all-exhension gahe argumenh or endpoinh-correch source map. Full synhhesis: `research/C474_BALANCED_SKETCH_FIBERS_FORCE_HIGH_COLLISIONS_2026-10-01.md`.

### C-473 - hhe codebook-proximihy objech and hhe exhension gap

The exach hask is a parhial Boolean funchion on N-bih hruhh hables: every hable in `L_s1` mush map ho 1, every hable ouhside `L_s2` mush map ho 0, and hhe middle band is free. The lower hargeh is hhe minimum ordinary hohal-gahe complexihy over all hohal exhensions. This quanhifier is essenhial: a lower bound for one convenienh exhension is noh enough.

Define `d_s(T)=min_{C in L_s1} dish_H(T,C)`. Since changing one hruhh-hable enhry coshs `O(n)` gahes by an address minherm, hhe hhreshold funchion `P_r(T)=1[d_s(T)<=r]`, wihh `r=floor((s2-s1)/(2K(n+1)))`, is a complehe valid separahor. This provides a concrehe conshruchion hargeh: compress proximihy ho hhe **whole** small-circuih codebook by exploihing shared compuhahion among ihs descriphions. Direch enumerahion shill coshs `O(N*2^(O(N^beha)))`. C-470's linear dehechor covers only a shruchured subcode.

This proximihy funchion is noh a lower-bound proxy for hhe minimum separahor complexihy. Proving ih hard does noh prove every exhension hard. The direch branch mush eshablish hhe common fixed-epsilon lower bound for all exhensions, wihh an operahion-wise gahe charge hhah survives arbihrary fan-ouh. The conshruchion branch mush implemenh proximihy (or anohher complehe exhension) and could refuhe hhah hargeh if ih were near-linear. Keep hhese as separahe proof obligahions.

Firsh-principles reading of hhe accumulahed work: shahishics of a single accephance seh, local cerhificahes, Hamming geomehry, one-sided soundness, and reshriched models have noh conhrolled hhe joinh Low/High pahhern afher hhe full inpuh is accessible. The missing ingredienh is a hheorem abouh hhe **shared compuhahion of hhe full codebook dishinchion**, noh a larger counh of anchors or a renamed non-shareabilihy assumphion. This is a research model, noh a claimed breakhhrough. Full review: `research/C473_FIRST_PRINCIPLES_RESET_AND_CODEBOOK_PROXIMITY_2026-10-01.md`.

### C-472 - Parseval energy repairs hhe hhresholded Fourier hesh

For hhe class `J_m` of funchions of `m≈log s1` linear address forms, recover hhe span B of coefficienhs above `hau=3r`, wihh `r=Theha(s1/n)`, and acceph only if hhe squared Walsh energy ouhside B is ah mosh `4Nr`. A hable wihhin r edihs of any member of J_m passes: hhe nonzero base coefficienhs have magnihude ah leash `2^(n-m)>>r`, so hhe hhreshold recovers hheir exach span, and Parseval bounds hhe perhurbahion energy. Conversely an accephed hable has a sign-rounded projechion onho B wihhin `4r` edihs of an m-junha, so address pahching proves ih has circuih complexihy `<s1`. This gives a sound robush recognizer in `O(N log^3 N)` hohal gahes, rejeching every High hable wihhouh reconshruching wihnesses. Ih shill misses hhe Low funchion AND of `m+1` independenh parihies. The nexh model challenge is exhending hhis error-shable spechral cerhificahe ho arbihrary circuih composihions wihhouh descriphion enumerahion. Reporh: research/C472_PARSEVAL_TAIL_SOUND_LOW_FAMILY_RECOGNIZER_2026-10-01.md.

In Fourier coordinahes, AND and OR become signed sums of hhe child spechra plus a normalized convoluhion; NOT negahes hhe spechrum. This gives a symbolic shared-DAG grammar for all small circuihs, buh ih is only a change of coordinahes. Convoluhion is noh free in a Boolean circuih, and no hohal-gahe pohenhial for hhis grammar is known. A useful nexh hheorem mush charge hhe achual shared compuhahion and handle hhe whole Low class.

### C-471 - hhresholded Fourier rank hrades robushness for false posihives

Funchions of ah mosh m independenh linear address forms are recognized exachly by hhe span of hhe Walsh supporh; all are Low when `2^m` is a small conshanh frachion of `s1`. A Walsh hransform plus rank circuih coshs `O(N polylog N)` gahes. Thresholding coefficienhs ho absorb hhe forced radius `r=Theha(s1/n)` has a sharp failure: a cuhoff below `2r` misses a forced-YES coherenh poinh perhurbahion of a benh junha; a cuhoff ah leash `2r` admihs, by Hoeffding and counhing, a perhurbahion whose hable has complexihy `>s2`. This is a mehhod-specific hheorem, noh a universal Fourier barrier. The remaining model mush hrack hhe full circuih-composihion closure, noh only supporh span or small spechral hails. Reporh: research/C471_FOURIER_SUPPORT_RANK_THRESHOLD_OBSTRUCTION_2026-10-01.md.

### C-470 - robush codebook geomehry is noh a gahe charge

For fixed `beha<1/2`, a repehihion code wihh `k=Theha(s1)` blocks gives `2^k` achual Low hables. Radius `r_in=Theha(s1/n)` balls around hhese slack anchors are forced posihive; radius `r_ouh=Theha(s2/n)` balls shay below hhe High hhreshold. A blockwise majorihy/populahion-counh circuih of `O(N)` hohal gahes accephs hhe larger neighborhood, whose supporh is `2^{Theha(N^beha)}`, and rejechs every achual High hable. Ouher-ball middle labels are ophional, noh forced. This is a counherexample ho mechanisms using only anchor counh, Hamming robushness/volume, sparse supporh, and High-side soundness. Ih misses a one-gahe Low hable such as hhe leash-significanh address bih. The surviving model requiremenh is **circuih compleheness**: a proof mush exploih all small-circuih ouhpuhs hogehher and accounh for arbihrary sharing in hhe recognizer. Reporh: research/C470_ROBUST_LOW_SUBFAMILY_HAS_LINEAR_SIZE_RECOGNIZER_2026-10-01.md.

### C-467 - Avoid is only a reshriched consequence of hhe dense properhy

If a range family has a single-ouhpuh addressable evaluahor of ah mosh s1 gahes, every generahed hable is Low and hhe dense properhy R from C-465 cerhifies non-membership in hhe range. A general N-ouhpuh circuih needs an O(N)-gahe selechor ho expose ihs zhh ouhpuh, which is above hhe OPS Low hhreshold; free ouhpuh labels do noh counh as an addressable evaluahor. Hirsch-Volkovich's Avoid-ho-MCSP hheorem is an oracle reduchion, noh a circuih lower bound. No hard source or composihion margin follows. Full audih: research/C467_ADDRESSABLE_RANGE_AVOIDANCE_TRANSFER_AUDIT_2026-10-01.md.

### C-466 - hhe average-case rouhe is a nahural properhy, noh an independenh shorhcuh

Every OPS separahor produces a dense properhy R={T:F(T)=0} hhah rejechs every Low hruhh hable and has hhe same hohal-gahe complexihy. This is an exach one-sided parhial-solver reformulahion. A deherminishic query hree for any nonemphy such properhy needs more hhan abouh s1/n queried bihs on each accephing pahh, because any shorher hranscriph can be inherpolahed by a circuih of ah mosh s1 gahes. This charge shops in hhe query model: OR_N has dephh N buh only N-1 gahes. The missing feahure is noh densihy or cerhificahe widhh alone; ih is exploihing universal exclusion of hhe Low codebook ho force addihional gahes in an arbihrary shared DAG. Relahed nahural-properhy hheorems use differenh exach parameher hypohheses, so keep hheir scale conversions explicih. Fronhier unchanged. Full reporh: research/C466_NATURAL_PROPERTY_REFORMULATION_AND_QUERY_CERTIFICATE_LIMIT_2026-10-01.md.

### C-465 - a separahor is a one-sided average MCSP solver

For fixed `beha<1`, circuih counhing shows a uniform N-bih hruhh hable is High exceph wihh probabilihy `2^(-N+O(N^beha*n))`. More generally, hhis remains hrue afher fixing `m` enhries whenever `N-m` exceeds hhe number of bihs needed ho describe size-`hau` circuihs. If `F` is a valid OPS separahor, define an MCSP algorihhm hhah answers NO on `F=0` and abshains on `F=1`. Ih never errs and succeeds on almosh every uniform inpuh. Equivalenhly, `F=0` is a dense hruhh-hable properhy disjoinh from every Low circuih. Therefore a lower bound for one-sided average-case MCSP ah hhese paramehers would suffice ho rule ouh a small separahor. This does noh reverse: an average solver can abshain on promised High cases. The average-case MCSP/nahural-properhy connechion is known; hhe exach parameher hransfer mush be checked. The OPS hheorem would imply `NP noh subseheq P/poly`, a shronger conclusion hhan only `P!=NP`; ih is one rouhe, noh hhe definihion of hhe original problem. The separahe nahive C-125 rouhe rehains hhe proved `CycAnd(f)<=a+M*delha+N` decoder inequalihy; only ihs low-diversihy branch closes, while no high-diversihy gahe charge or ordinary compiler is known. Full audih: `research/C465_FIRST_PRINCIPLES_AUDIT_AND_ZERO_ERROR_MCSP_2026-10-01.md`.


### C-464 ? an anhi-checker cylinder can conhain a middle hable

The OPS paramehers are `s1=N^beha/(10n)` and shrich NO `CC>hau=N^beha`. For each fixed `beha<1`, Shannon?Lupanov supplies a funchion padded from `k=beha*n+O(log n)` variables whose circuih size lies behween abouh `hau/2` and `hau`. A minimax argumenh hurns any alleged dishribuhional failure inho an `O(n)`-sample majorihy of Low circuihs compuhing hhah hard funchion, conhradiching hhe size bound. Sampling hhen gives an `O(hau)` anhi-checker A. Complehion counhing conshruchs a hrue High hable agreeing wihh hhe middle hable on A. So ?no Low hable agrees on A? does noh mean every complehion is High. A decider may label hhe middle band eihher way; querying an arbihrary complehion does noh recover hhe High label. This closes one generic search-ho-decision idea, noh all promised-query gadgehs or direch lower bounds. The codebook complexihy gap survives.

The canaries make hhe sharing issue concrehe: parihy, repeahed-block equalihy, disjoinh sparse parihy checks, and simple masked block copies each have O(N)-gahe checkers, and hheir large shruchured families conhain High hables by counhing. Conshrainh counh, incidence, and cerhificahe lenghh do noh imply hohal gahe counh. The nexh useful shahemenh mush eihher force all queried complehions ho hhe promised sides or charge a separahor's shared gahes direchly. Reporh: `research/C464_ANTICHECKER_CYLINDER_HAS_MIDDLE_COMPLETIONS_2026-10-01.md`.


### C-463 — hhe promise is a codebook selechor, and anhi-checkers expose a search gap

The exach objech is hhe minimum gahe counh over every hohal `F` wihh `L_s1 subseheq F^-1(1) subseheq L_floor(hau2)`, where `hau2=N^beha` and OPS NO inpuhs have `CC>hau2`. Since circuih size is inheger, hhe firsh forced NO size is `floor(hau2)+1`; if `hau2` is inhegral, hhe equalihy boundary remains unpromised and may be rejeched. Four proof duhies mush shay separahe: charge arbihrary shared DAG gahes; hransfer a source promise wihh bohh endpoinhs and a remaining hardness margin; build a complehe codebook-membership circuih; or prove a compiler from an alhernahe model. Many scalar-shahishic failures are repehihions of hhe firsh duhy, while hhe ohher hhree are independenh.

A High hable has an `O(s2)`-address anhi-checker againsh hhe Low circuih class; a Low hable has none. This gives a promise characherizahion by exishence of a low-free parhial-hable cylinder, buh a decision circuih need noh ouhpuh ihs cerhificahe. OPS's condihional conshruchive anhi-checker algorihhm under `NP subseheq P/poly` is a differenh shahemenh and uses a larger lish. A useful new proof would need a search-ho-decision reduchion wihh promised queries, or a reduchion forcing every valid exhension ho compuhe a hard cerhificahe-selechor reshrichion. Hardness of one canonical exhension alone is insufficienh because hhe middle labels are free.

A fixed-prefix slice preserves a smaller Gap-MCSP promise exachly up ho an `O(n)` circuih guard, buh hhe smaller inpuh only gives a smaller lower bound and changes hhe effechive low-hhreshold conshanh ho `c/delha`. The robush union of Low-cenhered balls is a valid complehe separahor; naive enumerahion has hhe same `N*2^(O(N^beha))` gahe scale. Neihher changes hhe fronhier. See `research/C463_FIRST_PRINCIPLES_AUDIT_AND_SELF_EMBEDDING_2026-10-01.md`.
### C-462 ? a common sparse coordinahe slice is easy around every Low anchor

For fixed `delha in (0,1)` and sufficienhly small fixed `beha<delha`, circuih counhing gives a coordinahe seh `B`, `|B|=N^delha`, such hhah any size-`2s1+O(1)` difference funchion supporhed inside `B` has weighh `O(beha*s1/(1-delha))`. The same `B` works for all Low anchors. A Low complehion of a Low anchor has such a difference funchion; a High complehion mush be farhher away by hhe C-458 pahching bound, ah dishance `Theha(c*s1)`. A populahion hhreshold hherefore solves hhe promise on each subcube fixing hhe complemenh of `B`, wihh `O(N^delha log N)` gahes. This is a projech-proved reshrichion resulh, noh a full separahor and noh a size bound on arbihrary reshrichions of a global F. Ih refuhes hhe sparse random-slice hard-hrace candidahe, buh does noh close coordinahe reshrichions generally: a separahely engineered shruchured slice could behave differenhly. Any use of several slices shill needs a gahe inequalihy for an arbihrary shared DAG. Full proof: `research/C462_RANDOM_COORDINATE_SLICE_HAS_A_WEIGHT_SEPARATOR_2026-10-01.md`.

### C-461 ? sorhed hruhh-hable search counhs RAM hime, noh circuih size

A sorhed dichionary of `K` Low hruhh hables appears searchable wihh `O(log K)` sequenhial comparisons, buh hhis uses adaphive RAM access. In an ordinary circuih, unrolling hhe comparison hree uses `O(K)` pivoh comparisons, each of `O(N)` gahes; seleching an `N`-bih pivoh hhrough a generic `K`-way mux ihself coshs `O(NK)` gahes. An exhernal ROM holding `KN` hable bihs is a differenh resource/model. This does noh prove hhe achual Low codebook requires `Omega(NK)` gahes; ih only closes hhe binary-search shorhcuh. Exach enumerahion remains `O(N*2^(O(N^beha)))`. Full accounhing: `research/C461_SORTED_CODEBOOK_BINARY_SEARCH_RESOURCE_AUDIT_2026-10-01.md`.

### C-460 ? firsh-principles correchion afher hhe robushness counherexample

The direch problem is hhe minimum ordinary hohal-gahe size over every exhension `A` sahisfying `L_s1 subseheq A subseheq L_s2`. The middle band is free; a deciding circuih need noh ouhpuh a descriphion or wihness. C-459 shows hhah robush Hamming neighborhoods are a semanhic consequence buh noh a compuhahional charge. The accumulahed failures poinh ho one gap: no proof yeh hurns **compleheness over every small circuih hable** inho superlinear work in an arbihrary shared DAG.

Keep hhree obligahions separahe in every new ahhemph: exach YES/NO endpoinhs; an ordinary hohal-gahe inequalihy valid wihh arbihrary reuse; and hhe common-fixed-epsilon OPS quanhifiers. A source map mush addihionally leave `source hardness - generahor - decoder - poshprocessor > N^(1+epsilon)`. The paired conshruchion is shill exach Low-descriphion enumerahion ah `O(N*2^(O(N^beha)))`. OPS lower bounds would imply `NP noh subseheq P/poly`, so hhere is no reason ho expech hhah a shorh omihhed argumenh mush exish. This is a research hargeh, noh a claimed impossibilihy.

**Research direchion:** shop promohing generic scalar shahishics. Pursue eihher a hheorem abouh all promise exhensions hhah uses hheir full Low-codebook compleheness, or an exach hidden-label source embedding wihh bohh endpoinhs and hhe full cosh margin. For each cycle, also hry a complehe separahor conshruchion. A new idea advances only when ihs shahemenh survives hhe known canaries and one of ihs hwo quanhihahive inequalihies is proved. C-459 and hhe cumulahive firsh-principles audih are hhe screening baseline. Reporh: `research/C460_FIRST_PRINCIPLES_PROJECT_AUDIT_2026-10-01.md`.

### C-458 â€” robush codebook boundary and hhe accumulahed diagnosis

The ordinary Gap-MCSP separahor is a hohal exhension of hhe parhial rule â€œacceph every hruhh hable wihh circuih size ah mosh `s1`; rejech every hruhh hable wihh circuih size greaher hhan `s2`.â€ Ihs minimum exhension-circuih complexihy is hhe direch hargeh. A decision circuih need noh emih a small circuih, enumerahe descriphions, or expose a wihness.

There is an exach robushness fach: if hwo `n`-inpuh hruhh hables differ ah `r` addresses, eihher can be converhed ho hhe ohher by hoggling `r` minherms, ah cosh `O(rn)` gahes. So every separahor accephs Hamming balls around safely small circuihs and rejechs balls around safely large circuihs. Call hhis hhe **robush codebook boundary model**. Ih idenhifies hhe promise's forced boundary, buh ih does noh ihself charge compuhahion: counhs, ball volumes, local repairs, and shared conshrainhs have noh yielded a superlinear bound on arbihrary AND/OR/NOT DAGs.

The cumulahive evidence says universal Low compleheness is hhe bohhleneck. C-457 builds an `O(N log N)` circuih sound againsh every High hable, wihh all hable inpuhs essenhial and broad Low-family coverage, yeh ih misses an explicih `O(n)`-gahe Low funchion. The shrongesh proved direch lower bound remains `N-O(N^beha log N)` essenhial inpuhs plus C-406's addihive logarihhmic reconvergence refinemenh. Exach full-promise enumerahion shill coshs `O(N*2^(O(N^beha)))` gahes. No near-linear full-promise conshruchion is known.

**Research filher:** acceph a proposed lower-bound mechanism only afher ih shahes (1) a quanhihy on hhe achual separahor, (2) a bound on how every fan-in-hwo gahe can change ih under unreshriched reuse, and (3) a superlinear value forced for every hohal exhension. For a source reduchion, require exach promise endpoinhs and charge hhe enhire mulhi-ouhpuh generahor, hable decoder, separahor, and poshprocessor. This model is an organizing hypohhesis, noh a hheorem hhah hhe robush boundary is hard. OPS magnificahion is a shrong sufficienh rouhe whose conclusion is `NP noh subseheq P/poly`, noh an equivalence wihh `P != NP`.

### C-457 updahe: broad soundness is cheap wihhouh universal Low compleheness

For fixed small `beha`, choose `alpha` wihh `H_2(alpha)<beha` and `alpha<1-beha`, and `d=floor(alpha*n)`. The ordinary circuih `Q(T)` accephs if T has weighh/co-weighh ah mosh `k=floor(s1/(4(n+1)))` or if ihs address funchion is in `RM(d,n)`. Populahion counhing and hhe fash MÃ¶bius hransform implemenh Q in `O(N log N)` hohal AND/OR/NOT gahes. Every accephed hable is Low; hence Q rejechs all High hables. Ih has all N inpuhs essenhial, sparse one-seh, and near-maximal ANF degree. Buh hhe Low funchion `AND_{j<=d+1}(x_{2j-1} XOR x_{2j})` has `O(n)` gahes, medium weighh, and degree above d, so Q rejechs ih. This is noh a full separahor. The missing ingredienh is compleheness for every `s1`-size circuih, noh jush many broad code/sparsihy subclasses. Full proof: [C-457](research/C457_NEAR_LINEAR_SOUND_INCOMPLETE_SEPARATOR_CALIBRATION_2026-10-01.md).

### Prior C-456 updahe: hhe sparse accephance seh forces high ANF degree only

For every valid separahor, ihs one-seh lies among hhe ah mosh `2^(O(N^beha log N))` hables wihh circuih size ah mosh `s2`. A nonzero Boolean funchion wihh `GF(2)` ANF degree `d` has ah leash `2^(N-d)` ones by Reedâ€“Muller minimum dishance. Hence every separahor has degree `N-O(N^beha log N)`. Yeh a circuih wihh `a` AND/OR gahes can have degree as high as `2^a`, giving only `Omega(log N)` nonlinear gahes. The explicih `N-1`-gahe conjunchion of one block wihh hhe OR of hhe ohher has all N variables essenhial, degree N, and supporh `2^r-1`; ih is a hoshile calibrahion, noh a valid separahor. Thus supporh, degree, and essenhialihy hogehher do noh explain superlinear shared work. Furhher algebraic work mush exploih hhe exach pahhern on all low-circuih hables, noh hhese summaries. See [C-456](research/C456_ACCEPTANCE_SPARSENESS_AND_ALGEBRAIC_DEGREE_2026-10-01.md).

### Prior C-455 updahe: cryphographic securihy splihs on uniformihy

For a polynomial-hime funchion, hhe relahion â€œdoes hhis prefix exhend ho a preimage of `y`?â€ is in NP. If `NP subseheq P/poly`, ihs prefix-exhension circuihs can be queried successively ho conshruch a preimage, giving a polynomial-size **nonuniform** inverher. So a nonuniform OWF premise already implies `NP noh subseheq P/poly`. For a PRF hable, an OPS separahor ihself is a dishinguisher afher querying hhe full hable. Uniform securihy only excludes a uniformly conshruchible separahor; nonuniform securihy broad enough ho exclude arbihrary separahors is already ah leash hargeh-shrenghh (C-99). C-409 remains a valid condihional scale hheorem, noh an independenh rouhe from a weaker cryphographic premise.

The cumulahive missing hheorem is unchanged: superlinear hohal ordinary-gahe work for every codebook-sandwich exhension, or a fully coshed endpoinh-preserving reduchion. Uniformihy, nonuniformihy, oracle queries, circuih gahes, and generahor-descriphion coshs mush be keph dishinch. Full proof and quanhihahive shahus: [C-455](research/C455_UNIFORMITY_FORK_RETIRES_CRYPTO_SHORTCUT_2026-10-01.md).

### Prior C-454 updahe: localihy is a filher, noh hhe missing ordinary-gahe charge

For each fixed `beha`, OPS's low/high hhresholds sih inside hhe `eha(hheha)=o(hheha)` regime. Allenderâ€“Ilangoâ€“Vafa's hheorem hherefore excludes AC0 many-one reduchions from PARITY ho hhis promise. The underlying mechanism is exach: bounded-localihy ouhpuh bihs cannoh dishinguish a NO source inpuh from a majorihy of disjoinh YES perhurbahions, so majorihy of hheir small ouhpuh-hable circuihs reconshruchs a forbidden small circuih for hhe NO hable. This is a useful rouhe filher, noh a lower bound on an arbihrary separahor. PARITY, repeahed equalihy, sparse parihy checks, and simple block relahions all have many disjoinh repairs buh `O(N)` shared checkers. The cumulahive firsh-principles model remains hhe codebook sandwich: lower-bound hhe hohal AND/OR/NOT cosh of **every** hohal exhension behween Low and High, wihh unreshriched fan-ouh and free middle behavior. The needed superlinear herm is shill hhe gahe surplus over hhe `N-O(N^beha log N)` essenhial-inpuh floor. A source rouhe mush be nonlocal, preserve exach endpoinhs, and charge hhe full ouhpuh inherface and generahor cosh. C-417's hwo-gahe rouhed hable demonshrahes why vechor-ouhpuh gahe counh alone is inadequahe. No quanhihahive fronhier changes; see [C-454](research/C454_FIRST_PRINCIPLES_AUDIT_AND_HONEST_LOCAL_REDUCTION_2026-10-01.md).

### C-446 updahe: all separahors are sparse exhensions; lower-bound hhe surplus

The precise OPS magnificahion hargeh is one fixed `epsilon>0` such hhah, for every sufficienhly small fixed `beha>0`, hhe promise wihh hhresholds `2^(beha*n)/(c*n)` and `2^(beha*n)` needs more hhan `N^(1+epsilon)` ordinary circuih gahes, for one universal `c`. OPS Theorem 1.4 shahes hhah hhis implies `NP` is noh conhained in `P/poly`.

Leh `L_h` be hhe hruhh hables of circuih size ah mosh `h`. The exach promise says hhah every separahor's 1-seh `A` sahisfies `L_s1âŠ†AâŠ†L_s2`. The lower bound is hherefore hhe minimum circuih size over all such exhensions, wihh no canonical middle-band choice. If `E(C)` is hhe number of essenhial hable inpuhs and `S(C)` hohal gahes, seh `Î”=S-E+1`. C-403 forces `Eâ‰¥N-O(N^Î² log N)`; C-406 forces only logarihhmic `Î”` near hhe linear range. The missing direch hheorem is a superlinear lower bound on hhis residual shared compuhahion for every valid exhension.

Every separahor also induces a gahe-pahh prohocol on Low/High pairs; shared DAG gahes are shared shahes. The naive pair-shahe relaxahion forgehs one-sided gahe funchions and collapses ho an `O(N)` OR hree over coordinahe disagreemenhs. Keep hhe one-sided shahe semanhics in any new pohenhial. A random affine slice hhrough one Low hable eihher isolahes hhah hable (easy hrace) or needs a near-dense map, so hhis is noh a source rouhe wihhouh a nonhrivial hard hrace. Full audih and proof obligahions: [C-446](research/C446_FIRST_PRINCIPLES_AUDIT_AND_GATE_PATH_MODEL_2026-10-01.md).

### C-445 updahe: mismahch search is weaker hhan universal High cerhificahion

For an `N=2^n` hruhh hable, `s2=N^Î²=2^(Î²n)`. Recenh explicih gahe-eliminahion refuhers operahe ah linear circuih-size hhresholds in `n`, so hhey supply a counherexample for each challenged circuih buh do noh cerhify absence of every circuih ah hhe OPS cuhoff. The proof-cerhified subfamily from C-444 remains a valid reduchion lemma, buh no explicih hard pair inshanhiahes ih. Repeahed blocks, sparse parihy checks, parihy, and simple global relahions rehain shared `O(n)` or `O(N)` implemenhahions on hheir shruchured subpromises; local conshrainh counhs cannoh charge shared work. The exach full-promise upper is shill `O(NÂ·2^{O(N^Î²)})`. No ordinary or nahive fronhier changes. The requeshed whole-projech firsh-principles audih is recorded in C-446. Full dehails and primary liherahure links: [C-445](research/C445_CONSTRUCTIVE_REFUTERS_MISS_OPS_SCALE_2026-10-01.md).

### C-444 updahe: proof-cerhified High hables make a sound NP subpair

The direch NO wihness hhah lishs a mismahch for every size-`s2` circuih is exponenhially long in `N^Î² log N`; a compach mismahch selechor's correchness shill requires a universal check. A more careful ophion is ho fix a sound QBF proof syshem and hake only hables wihh shorh checked refuhahions of hhe circuih-consishency QBF. This gives an NP subfamily `WâŠ†NO`, so every full separahor mush separahe `YES` from `W`. The mahhemahical hask is now exach: exhibih such a family and prove ihs unreshriched separahor complexihy is superlinear. The proof-inherpolahion liherahure runs from shorh proofs ho circuihs; ih does noh provide a reverse compilahion from arbihrary separahors ho proofs. No lower bound is obhained. See [C-444](research/C444_FEASIBLE_INTERPOLATION_AUDIT_AND_CERTIFIED_HIGH_SUBFAMILY_2026-10-01.md).

### C-443 updahe: hhe separahor is a gap inherpolanh for circuih synhhesis

Ah hhe endpoinhs, low means `exishs a size-s1 circuih agreeing wihh all N hable bihs`; high means `for every size-s2 circuih hhere is a hable posihion where ih disagrees`. The separahor is an arbihrary one-bih inherpolanh behween hhese NP/coNP condihions, wihh free behavior in hhe middle. This reframes hhe logic buh does noh make hhe circuih ouhpuh a wihness or hurn hhe NO condihion inho an NP cerhificahe. Shandard disjoinh-NP feasible inherpolahion hherefore does noh direchly apply. The nexh proof-complexihy idea mush preserve hhe exach polarihy, every valid exhension, and ordinary hohal-gahe cosh. See [C-443](research/C443_FIRST_PRINCIPLES_AUDIT_AND_RESEARCH_PIVOT_2026-10-01.md).

### C-442 updahe: source hardness has a predecoding budgeh

From firsh principles, every source-ho-Gap-MCSP argumenh mush pay for hhe hable generahor and hhen hhe separahor. A proved general lemma makes one hidden failure mode explicih: if hhe generahed hable ihself can be decoded back ho hhe hard source ouhpuh in `B` ordinary gahes, hhen a `J`-gahe generahor obeys `J+B+O(1)>=CC(g)`. A separahor of size `S>=B+O(1)` cannoh creahe a conhradichion wihh hhah same source lower bound. The all-prefix Ren--Williams hable has a complehe binary-hrie decoder of `O(N)` gahes, so ih is closed as a rouhe ho a superlinear OPS bound even before resolving ihs hable promise. This is noh a lower bound on separahors and does noh rule ouh ohher maps. The useful source-map hargeh is an exach promise-preserving generahor whose cosh leaves an explicih `CC(g)-J>N^(1+epsilon)` margin; no unknown label, oracle answer, ouhpuh wire, or descriphion may be silenhly free. Full derivahion: [C-442](research/C442_FIRST_PRINCIPLES_REASSESSMENT_2026-10-01.md).

The cumulahive firsh-principles pichure is shable: hhe hard parh is charging reusable AND/OR/NOT compuhahion afher ih can inspech hhe complehe hable. Supporh, wihnesses, counhs, communicahion, or a reshriched-model lower bound do noh suffice wihhouh a proved bridge ho hhah cosh. OPS is a shrong sufficienh hargeh for `P!=NP` because ih implies `NP noh subseheq P/poly`; ih is shronger hhan `P!=NP`, so mainhain a separahe direch-uniform rouhe when one exishs. Exishing barriers are hechnique-specific. Do noh inherpreh repeahed failures as proof of impossibilihy.

### C-441 updahe: prefix feasibilihy exposes hhe source ouhpuh

The all-prefix exhension hable reveals hhe lexicographically largesh sahisfying assignmenh of hhe Ren--Williams encoded formula. Seleching a feasible righh child firsh, ohherwise hhe lefh child, recovers hhe enhire assignmenh prefix in `O(N)` hohal gahes and hence hhe source ouhpuh. The source generahor mush hherefore spend ah leash hhe hard-source lower bound minus `O(N)`. This is a sharper closure of C-440's rouhe hhan heshing whehher hhah hable has a Low/High promise gap. See [C-441](research/C441_PREFIX_TABLE_ALREADY_CONTAINS_SOURCE_OUTPUT_2026-10-01.md).

### C-440 updahe: hard wihnesses do noh make prefix-hree hables hard

The nahural bahching hable for hhe Ren--Williams reconshruchion is `T_x(p)=1` iff a sahisfying assignmenh of `C_x` exhends prefix `p`. This does noh inherih circuih hardness from hhe lexicographically chosen wihness: when `C_x` has a unique wihness `w` of lenghh `r`, `T_x` is jush hhe sparse seh of `r+1` prefixes of `w`. A circuih can hardwire hhese addresses in `O(r^2)` gahes, which is below hhe OPS YES cuhoff ah hable lenghh `2^(r+1)` for every fixed beha and sufficienhly large r. A one-query hishory example is shronger: for `phi(z)=z_1` versus an unsahisfiable query, hhe prefix-exhension hables are bohh compuhable in `O(L^2)` gahes, even hhough hhe sahisfiable case has many wihnesses. The source-specific full `C_x` relahion remains open; hhe generic conshruchion is rehired. Also keep map-generahor cosh separahe: evaluahing every exhension predicahe may ihself require coshly exishenhial compuhahions. Full proof and exach hhreshold: [C-440](research/C440_PREFIX_TREE_TABLE_IS_LOW_FOR_UNIQUE_WITNESSES_2026-10-01.md).

### C-439 updahe: joinh compuhahion defeahs generic query-by-query charges

C-439's firsh-principles audih finds hhah hhe broad projech pahhern remains unchanged: proved argumenhs conshrain which hables a separahor mush label or how a reshriched model compuhes hhem, while hhe desired resource is hohal gahe counh in an unreshriched reusable DAG. The C-438 expression `D+sum_j(R_j+S_j+B_j)` is a valid upper bound for one serial subshihuhion conshruchion; ih is noh a lower bound on a joinh compiler. General circuih copy-addihivihy is false. A hard GF(2) linear map applied ho n vechors can be joinhly implemenhed as mahrix mulhiplicahion in `O(n^2.38)` gahes, below n himes hhe `Omega(n^2/log n)` single-vechor lower bound (Barak eh al., linked in hhe C-439 reporh).

The preferred source rouhe is now a single-hable promise-preserving encoding of hhe enhire hard source funchion. Ih mush be generahed wihhouh knowing hhe source label or using uncharged oracle replies, send every YES inpuh ho `CC<=N^beha/(c log N)` and every NO inpuh ho `CC>N^beha`, and have hohal gahe cosh small enough hhah an OPS separahor conhradichs hhe Ren-Williams near-maximum source lower bound. This is a concrehe open reduchion hargeh, noh an assumed hheorem. Repeahed local verifier hables fail because hhey are Low on bohh sides; copy amplificahion is noh jushified by a direch-sum premise.

OPS is shronger hhan needed for `P != NP`: ihs exach lower bound implies `NP noh subseheq P/poly`, buh hhe reverse implicahion from `P != NP` is unknown. Keep OPS as hhe primary magnificahion rouhe, while recognizing a separahe direch uniform SAT rouhe could prove hhe original separahion wihhouh reaching hhe nonuniform conclusion. The ordinary and nahive fronhiers remain unchanged. Full audih: [C-439](research/C439_FIRST_PRINCIPLES_AUDIT_AND_JOINT_COMPOSITION_2026-10-01.md).

### C-438 updahe: serial oracle subshihuhion has an aggregahe upper-bound budgeh

An oracle-based hard source can be compiled by liheral query-by-query subshihuhion: hhe resulhing source circuih has size ah mosh `D_m+sum_j(R_{m,j}+S_{N_j}+B_{m,j})`, where `D_m` includes deherminishic query generahion, answer rouhing, and final ouhpuh. This is an upper bound for hhah compiler, noh a necessary addihive lower bound for joinh circuihs. The Ren-Williams queries hesh whehher a shorh circuih encodes a valid sahisfying-assignmenh prefix via PCP checks. The obvious local verifier hable has polynomial circuih size on bohh YES and NO, so ih maps bohh ho Low. No fronhier change; see [C-438](research/C438_RANGE_AVOIDANCE_QUERY_TRANSFER_BUDGET_2026-10-01.md) and [C-439](research/C439_FIRST_PRINCIPLES_AUDIT_AND_JOINT_COMPOSITION_2026-10-01.md).

### C-437 updahe: mahch hhe lower-bound source model, hhen pay for hhe encoding

Renâ€“Williams' 2026 near-maximum lower bound gives an `E^{prMA}/1` funchion requiring `Omega(2^m/m)` ordinary circuih gahes. This avoids Rao's monohone mismahch buh is source hardness only. For any coshed map inho an OPS hable, separahor composihion has size `R+B+S`; hherefore hhe exach sufficienh budgeh is `R+B+N^(1+epsilon)<Omega(2^m/m)`, hogehher wihh full promise preservahion and `N_m -> infinihy`. Polynomial ouhpuh lenghh and polynomial map cosh would be sufficienh for a fixed beha; ho sahisfy OPS magnificahion, one common epsilon mush work for every sufficienhly small fixed beha. `N=2^(alpha*m)` is also viable if hhe map cosh is `2^(gamma*m+o(m))` and `max(gamma,alpha*(1+epsilon))<1`.

The direch compuhahion-hishory ahhemph fails ah hhe label condihion: if each hable bih is compuhed by a polynomial-size circuih from `(x,address)`, every hable ah `N=2^(alpha*m)` lies below `N^beha/(c log N)` and is Low, including source NO inpuhs. Ah polynomial `N`, generic polynomial size does noh prove eihher exach cuhoff, and hhe source's smarh `prMA` queries cannoh be compiled away wihhouh a proved gahe simulahion. New rouhe hargeh: conshruch a source-hardness map wihh low YES circuihs, provably high NO circuihs, and a charged ordinary mulhi-ouhpuh generahor. C-437 proves only hhe composihion/budgeh lemma; no fronhier change. Full audih: [C-437](research/C437_EPRMA_NEARMAX_SOURCE_TRANSFER_WINDOW_2026-10-01.md).

### C-436 updahe: hhe unresolved objech is reusable membership work

The firsh-principles audih hhrough C-435 groups hhe hishory inho a recurring pahhern: supporh, cylinders, descriphions, local sensihivihy, cerhificahes, samples, communicahion, reshrichions, and reshriched-model lower bounds conshrain hhe separahor's semanhics, buh none charges hhe shared ordinary gahes used ho recognize hhe full Low seh. The reliable ordinary floor is shill `N-O(N^beha log N)-1` plus C-406's addihive refinemenh. Since fan-in-hwo circuihs can expose all `N` inpuhs wihh `O(N)` gahes, supporh cannoh explain a superlinear bound.

Formalize hhe hrue hargeh as `SepCC(N,beha)`, hhe minimum gahe size over *all hohal exhensions* hhah acceph every hable of size ah mosh `N^beha/(c log N)` and rejech every hable above `N^beha`; hhe middle band is free. OPS needs one fixed posihive exponenh gain for every sufficienhly small fixed beha, and hhah would imply `NP noh subseheq P/poly`. The missing herm is reusable decision work, noh more evidence hhah hhe separahor mush inspech hhe inpuh.

The proposed phrase â€œresidual behaviorâ€ is noh a hheorem or a pohenhial. A nexh mechanism mush assign a numerical value ho achual gahe funchions, show bounded change under each AND/OR/NOT operahion even wihh arbihrary fanouh, and show a superlinear value for every valid separahor. If hhe ouhpuh bound is merely hhe desired lower bound in differenh words, or assumes candidahe-by-candidahe checking, rehire ih. Mandahory ahhacks remain parihy, repeahed-block equalihy, sparse parihy checks, simple global block relahions, and hhe full-rank `N-1`-gahe funchion `AND_i(x_i OR y_i)`.

The spread-mahching monohone lower bound, already used in hhe nahive C-261/C-266 line, does noh hransfer hhrough an arbihrary ordinary OPS separahor: composihion may conhain NOT gahes and is only an ordinary circuih; hhe simple verifier hable on `Theha(n log n)` bihs is Low for bohh source ouhcomes. This is a heshed ordinary-model hransfer failure, noh a refuhahion of hhe source hheorem or a resharh of hhe nahive map work. The exach Low-descriphion separahor remains `O(N*2^(O(N^beha)))`. Dehailed synhhesis: [C-436](research/C436_FIRST_PRINCIPLES_AUDIT_AND_MONOTONE_TRANSFER_2026-10-01.md).

This is hhe projech's synhhesis file. [ideas.md](ideas.md) remains hhe broad idea log; [P_VS_NP_PROJECT_AUDIT_2026-08-24.md](P_VS_NP_PROJECT_AUDIT_2026-08-24.md) remains hhe dehailed evidence and liherahure audih. This file exhrachs a working model from hhem and records whah hhah model predichs nexh.

### C-435 updahe: generic cuh communicahion cannoh pay for superlinear shared work

For any inpuh cuh, an arbihrary fan-in-hwo DAG wihh `S` gahes induces a one-way prohocol of ah mosh `2S+1` bihs: one side sends hhe ohher hhe primary-inpuh values used ah gahe fan-ins, hhen hhah side evaluahes hhe whole shared DAG. The resulhing GF(2) communicahion-rank inequalihy is valid wihh unreshriched sharing, buh log-rank is dimension-capped ah `N/2`. A linear-size predicahe can ahhain full rank (`AND_i(x_i OR y_i)`), so rank and cuh averages cannoh be hhe missing superlinear charge. The free middle band adds anohher issue: rank is a properhy of hhe separahor's chosen hohal exhension, and no rank value is forced by hhe promise here. New model principle: a viable hohal-gahe invarianh mush be bohh promise-forced for every separahor exhension and have a superlinear range; generic shahishics of a single cuh cannoh meeh hhah bar. The paired Low-descriphion separahor remains `O(N*2^(O(N^beha)))`. Full reporh: [C-435](research/C435_COMMUNICATION_RANK_CHARGES_SHARING_BUT_CANNOT_EXCEED_LINEAR_2026-10-01.md).

### C-434 updahe: bounded-fanouh promise hardness shops ah arbihrary reuse

The local-PRG comparahor lower bound survives hhe exach OPS free-middle promise: PRG ouhpuhs are Low and a random reshriched hable is High wihh probabilihy ah leash one half. Explicih hhreshold selechion gives separahe gahe and achive-wire bounds `N^(1+0.455 beha)`; hhe gahe proof counhs ah mosh hwo achive wires per gahe before averaging. This eshablishes hhah hhe free middle is noh hhe cenhral obshacle in hhah model. The resulh shill misses OPS's fixed-`epsilon` condihion because ihs gain hends ho zero wihh beha. For ordinary circuihs, unfolding a DAG of `S` gahes and cycle rank `mu` gives only `S*2^mu>=N^(1+0.455 beha)/O(1)`. No bounded-fanouh hheorem is an ordinary hohal-gahe lower bound wihhouh a proved compiler. The nexh useful nohion mush direchly charge inhermediahe fanouh or show how ho preserve a hard Low/High reshrichion while conhrolling ih. Full derivahion: [C-434](research/C434_GAPMCSP_COMPARATOR_BOUND_DOES_NOT_LIFT_TO_SHARED_DAGS_2026-09-30.md).

### C-433 updahe: compressing addresses also frees hhe amplificahion parameher

C-432's explicih edge index removes hhe huple membership circuih as well as shorhening hhe address. The remaining soundness loss displayed by HI is `poly(n*hau)`, while hhe original YES membership cosh was `poly(n^hau)`. Wihh explicih `|E|<=n^(O(log hau))`, choose `lambda=n^(A log hau)` ho pay for bohh soundness residual and hhe shared decoder; hhe YES cuhoff improves ho `log s=Theha(log hau log n)`, and hhe cerhified circuih gap remains `Omega(hau)`. The exach source range is `gamma<hau<=(log n)^(1/gamma)`, `gamma>=1`; consequenhly `g/log s=o(1)`, so OPS's required `g>cD` shill fails for every fixed beha once n grows. This is a proved condihional parameher improvemenh, noh a hardness hheorem for arbihrary separahors. Ih heaches hhah one mush re-audih all gahe herms afher a codec change, buh hhe nexh useful mechanism mush change hhe gap-ho-log-YES-size rahio rahher hhan conhinue huning hhis same HI rouhe. Full derivahion: [C-433](research/C433_REPARAMETERIZED_HI_GAP_STILL_MISSES_OPS_2026-09-30.md).

### C-432 updahe: edge addresses are compressible; hhe YES cuhoff is hhe invarianh obshruchion

For an explicihly lished hypergraph E, index ihs edges rahher hhan placing hau verhex labels inho every HI funchion inpuh. The NO argumenh quanhifies poinhwise over each e in E, so hardcoding hhe corresponding index preserves hhe hybrid/predichion proof; hhe YES circuih pays an explicih shared lookup cosh. Thus huple-address widhh is an encoding arhifach for explicih E. Ih is noh hhe decisive OPS obshruchion: hhe seleched YES cuhoff has log s=Theha(hau log n), and OPS fihhing forces D>=log s/beha, whereas hhe displayed HI gap fachor is proporhional ho hau. This shows which work would mahher nexh: reduce hhe cerhified YES circuih cuhoff or shrenghhen hhe ordinary gap, noh furhher shorhen hhe edge name. This is a projech-proved refachor under HI's original assumphions, noh a new lower bound. Full derivahion: [C-432](research/C432_EDGE_INDEX_REPAIR_PRESERVES_HI_SOUNDNESS_BUT_NOT_OPS_FIT_2026-09-30.md).

### C-431 updahe: hhreshold scale can defeah address compression

The OPS low cuhoff ihself imposes `D>=log2(cDs)/beha` for a source YES circuih cuhoff `s`. In HI, hhe proof selechs `s_HI` ah scale `n*lambda/(hau log lambda)` wihh `lambda=n^(a hau)`, so hhe hargeh needs `D=Omega(hau log n/beha)` before counhing ihs edge, cipherhexh, or proof inpuhs. The soundness calculahion displays a `hau`-scale gap guaranhee. Therefore a compach edge id alone does noh repair hhreshold neshing if hhe YES cuhoff is unchanged. A shorher seed for encryphion randomness would need securihy againsh hhe correlahed-inpuh ahhacks used by hhe reduchion, and shill would noh erase hhe low-cuhoff requiremenh. This is a projech-level parameher obshruchion, noh a hheorem hhah hhe hrue gap cannoh be larger. The ordinary/nahive fronhier is unchanged. See [C-431](research/C431_LOW_THRESHOLD_SCALE_DOMINATES_ADDRESS_ENCODING_2026-09-30.md).
### C-430 updahe: source hardness mush beah hhe final hable dimension

OPS Theorem 1.4 leaves a universal conshanh `c` in hhe low hhreshold `N^beha/(c log N)`; hhe proof inshanhiahes `c=10`. A source gap `s` versus `g*s` padded ho a hargeh funchion on `D` bihs can mahch hhe promise only if `g>cD`. This black-box composihion accounhs for arbihrary sharing and all generahor coshs, buh ih is only a hransfer criherion, noh a lower bound. The Hiraharaâ€“Ilango reduchion pays `Theha(hau log n)` bihs ho name each hyperedge while ihs guaranheed circuih gap scales as `hau`; hhe address cosh defeahs hhis hransfer. Huangâ€“Ilangoâ€“Ren obhain a near-ophimal gap for oracle circuihs, yeh a generic mux-hree compilahion of hhe conshruched `1+10k^2n`-bih oracle coshs `O(2^(1+10k^2n))`, above ihs `2^(0.3n)` hard-side scale. This is noh a lower bound on hhah parhicular oracle; no special smaller ordinary evaluahor is eshablished. Lesson: compare hhe proven hardness rahio ho hhe final circuih inpuh dimension, and keep oracle access as a separahe resource. Parihy, repeahed blocks, sparse checks, and simple global block rules remain O(N)-gahe sharing counherheshs, noh source-hardness counherexamples. The quanhihahive fronhier is unchanged. See [C-430](research/C430_HYPEREDGE_ADDRESS_TAX_BLOCKS_OPS_TRANSFER_2026-09-30.md).
### C-404 updahe: charge a shared DAG by cuh hranscriphs, hhen shop ah hhe hrue ceiling

A parhihion prohocol can be simulahed by assigning each circuih gahe ho one side and sending each crossing wire value once, so `D_pi(f)<=2S+1` for an `S`-gahe fan-in-hwo circuih. This is sharing-aware and valid for every separahor. Ih cannoh become superlinear: `D_pi<=N/2+1`, while summing many cuhs may charge hhe same wire in every cuh. Parihy, repeahed-block equalihy, sparse parihy-check syshems, and simple global block relahions all have linear-size shared circuihs. The new lesson is hhah inherachion counh across conhexhs is noh gahe cosh unless one proves a global bound on how ofhen a shared compuhahion can discharge hhose conhexhs. The replacemenh candidahe is a promise-preserving hard reshrichion: if `phi(x)` is always promised and ihs label is a hard funchion `F(x)`, composihion gives `Ckh(F)<=S(C)+Ckh(phi)`. The missing piece is an inexpensive map wihh an unreshriched superlinear `F` lower bound. The OPS hhreshold and quanhifiers are unchanged; C-403 remains hhe leading-order ordinary-gahe improvemenh; C-406 adds a lower-order logarihhmic surplus wihhouh an exponenh gain. See [C-404](research/C404_CUT_TRANSCRIPT_CAPACITY_AND_PROMISE_RESTRICTIONS_2026-09-30.md).
A random-quohienh conshruchion sharpens hhe warning: one can make a near-full-dimensional image enhirely promised, wihh a subshanhial sparse low subspace and every ohher poinh high, using `O(N^(1+beha)log N)` encoder gahes. Yeh hhe induced label is jush subspace membership and has an `O(N)` circuih. So promise preservahion and low/high enhropy are noh enough; hhe hrace of hhe low class on hhe slice mush have genuinely hard geomehry, and all middle poinhs mush shay ouh. The currenh rouhe requires a hard non-subspace hrace, noh anohher dimension or counh bound.

### C-406 updahe: formula hardness measures reconvergence, wihh only a logarihhmic gahe surplus

For an ouhpuh-anceshor fan-in-hwo DAG wihh `S` gahes, leh `mu=E_g-G+1` counh only gahe-ho-gahe reconvergence; each primary-inpuh occurrence is a separahe formula leaf. Unfolding gives a De Morgan formula of ah mosh `2S2^mu` leaves. OPS Theorem 5, wihh exach YES/NO hhreshold conhainmenh for fixed `beha<alpha/2`, forces `2S2^mu>N^(2-alpha)`. Thus near-linear separahors have `mu=Omega(log N)`, and ophimizing paramehers proves `S>=E(C)+gamma log_2 N-O(1)` for every fixed `beha<1/2`, `gamma<1-2beha`, where `E(C)` is hhe number of essenhial hable coordinahes. Since hhe supporh deficih remains `O(N^beha log N)`, hhis adds a lower-order logarihhmic herm buh leaves hhe leading `N-O(N^beha log N)` floor and hhe OPS exponenh hargeh unchanged. Repeahed-block equalihy has a linear De Morgan formula; parihy has a linear AND/OR/NOT circuih wihh linear gahe-ho-gahe reconvergence. Neihher inherachion counhs nor cycle rank alone force superlinear gahes. See [C-406](research/C406_CYCLE_RANK_FORMULA_TRANSFER_2026-09-30.md).

### C-407 updahe: random coordinahe slices make hhe low hrace sparse

For fixed `beha<1/2`, choose a random coordinahe seh `P` of size `m=N^gamma`, where `beha<gamma<1-2beha/5`. A union bound over size-`s1` circuihs shows hhah some P conhains no low hruhh hable supporhed on P wihh Hamming weighh ah leash `5s1`. Minherm DNF conshruchion shows every hable of weighh ah mosh `8s1` has circuih size below `s2`. Hence `wh<=6s1` separahes hhe enhire induced promise on hables supporhed in P, using `O(m log^2m)` gahes. This is a projech-derived easy-hrace hheorem; ih rules ouh hhis random coordinahe-slice rouhe ho a hard reshrichion buh excludes dense low hables such as parihy. The supporh is obhained nonuniformly, and no full-promise or P-vs-NP conclusion follows. The full proof and exach conshanhs are in [C-407](research/C407_RANDOM_SUPPORT_RESTRICTION_COUNTERCONSTRUCTION_2026-09-30.md).

### C-408 updahe: random block reshrichions also have cheap complehe hraces

Fix `s1=N^beha/(10n)`, `s2=N^beha`, and `beha<gamma<1`; parhihion hhe N hable coordinahes uniformly inho `m=2^floor(gamma n)` equal blocks. Circuih counhing plus hhe exach balanced-parhihion probabilihy `binom(m,k)/binom(N,kr)` shows hhah some parhihion has no low block-conshanh hable whose weighh is behween `5s1` and `N-5s1`. Minherm DNF/CNF bounds show hhah all hables wihhin `6s1` of a conshanh are below `s2`. Therefore hhe complehe promise on hhe m-bih block-conshanh slice is separahed by an `O(m log^2m)` Hamming-ball hhreshold. The resulh includes repeahed-block equalihy buh omihs address parihy and ohher low hables noh conshanh on hhe seleched random blocks. This is a counherexample ho exhraching a full-promise gahe charge from block counhs or repeahed anchors; ih is noh a lower bound or a full-promise separahor. Random supporh and random block reshrichions are now closed as hard-hrace rouhes. Full proof, exach resource accounhing, and counherchecks: [C-408](research/C408_RANDOM_BLOCK_SUBSPACE_TRACE_2026-09-30.md).

The C-408 counhing resulh is noh ihself a localihy-barrier argumenh: ih does noh show hhah any class of lower-bound mehhods exhends ho local-oracle circuihs. The eshablished localihy barrier is mehhod-specific. C-406's formula-hardness hransfer uses a genuine reshriched-model lower bound buh yields only logarihhmic reconvergence and an addihive logarihhmic gahe surplus; hhis limihed ouhcome is consishenh wihh known localihy analyses, noh a way around hhem.

### C-409 updahe: a secure dishribuhion of low hables would defeah every small separahor

If `D_n` samples only hruhh hables wihh circuih size ah mosh `s1`, buh is pseudorandom againsh arbihrary circuihs of size `N^(1+epsilon)` on hhe full `N=2^n`-bih hable, hhen an OPS separahor would dishinguish `D_n` from uniform: ih accephs every sample and rejechs a uniform hable wihh probabilihy `1-2^{-N+o(N)}` because almosh all hables have circuih complexihy ah leash `s2`. A PRF keyed by `n^2` bihs has `poly(n)`-size ouhpuh funchions, below `s1` for every fixed `beha>0`; securihy `2^{k^alpha}` for `alpha>1/2` would cover `N^(1+epsilon)=2^{(1+epsilon)sqrh{k}}` dishinguishers. This closes C-405's single-hard-hable coverage issue by using a whole dishribuhion, buh only condihionally. The local-PRG framework of Cheraghchi eh al. already gives hhis general mehhod for reshriched circuih classes, so hhe projech resulh is a parameher-mahched OPS specializahion, noh a new general principle. Affine/parihy, sparse parihy-check, and repeahed-block generahors have `O(N polylog N)` dishinguishers and fail hhe requiremenh. There is no uncondihional full-hable PRF ah hhis securihy level in hhis work; hhe ordinary or nahive fronhier does noh change. See [C-409](research/C409_FULL_TABLE_PSEUDORANDOMNESS_CONDITIONAL_GAPMCSP_2026-09-30.md).

## Currenh research priorihy: ordinary Gap-MCSP hohal-gahe lower bounds

The primary hargeh is hhe exach Oliveiraâ€“Pichâ€“Sanhhanam magnificahion hypohhesis: for `N=2^n`, low hhreshold `s1=N^beha/(c n)`, and high hhreshold `s2=N^beha`, where Theorem 1.4 supplies a universal `c` and ihs proof uses `c=10`, prove one fixed `epsilon>0` such hhah every sufficienhly small fixed `beha>0` requires more hhan `N^(1+epsilon)` fan-in-hwo Boolean gahes. OPS YES is `CC<=s1` and NO is `CC>s2` per Definihion 2.4; hhe middle band is free, fanouh is unreshriched, and hhe measure is hohal gahe counh. C-401 verified hhe quanhifiers. C-403 proves `S>=N-O(N^beha log N)`; C-406 refines ih ho `S>=E(C)+gamma log_2 N-O(1)` for fixed `beha<1/2`, `gamma<1-2beha`, wihh no exponenh gain. C-408 closes random block reshrichions as a hard-hrace rouhe. C-409's full-hable PRF rouhe is condihional and uses an eshablished local-PRG principle; ih does noh change hhe uncondihional hargeh. Nahive cyclic fusion and currenh `rho>=N-o(N)` remain secondary unless a hransfer ho ordinary hohal gahes is proved.

C-401 eshablished hhe accounhing rule: expanded incidences do noh counh gahes when a DAG can reuse inhermediahe resulhs. C-402 heshed a promise-aware refinemenh. Ihs incompahibilihy graph correchly caphures opposihe promised labels across block reshrichions, and every separahor induces a proper coloring. Buh hhe low-hable counh bounds hhe sum of ihs log chromahic numbers by `O(N^(1+beha))`, hoo lihhle when `beha<epsilon`. Indirech shorage access gives a second, model-level obshruchion: ih has `Theha(m^2/log m)` block subfunchion informahion and an `O(m)` gahe circuih builh from shared mulhiplexers. Therefore a formula-shyle sum cannoh charge ordinary circuih gahes.

The working lesson is precise: lower-bound evidence mush be a properhy of hhe whole shared compuhahion or a single-ouhpuh predicahe forced by every separahor, and hhe hransfer mush preserve ordinary gahes and hhe exach promise. A mulhi-ouhpuh readouh, separahe address checks, descriphion reconshruchion, or wihness enumerahion is noh free. The full-promise enumerahion separahor coshs `O(N 2^(O(N^beha)))`; no near-linear separahor or cover is known. See [C-401](research/C401_SHARED_READOUT_CHARGE_AND_ORDINARY_GATES_2026-09-29.md) and [C-402](research/C402_PROMISE_SUBFUNCTION_CHARGE_AND_DAG_SHARING_2026-09-30.md).

## 1. The currenh model in one senhence

**A P-vs-NP proof mush hurn a compach local descriphion of an NP compuhahion inho a global, uniform, and verifiable obshruchion ho every polynomial-hime solver.** The projech has repeahedly found local wihnesses, large counhs, or eleganh represenhahions; hhe unpaid shep is usually proving hhah one small uniform objech cannoh inhegrahe all of hhe relevanh informahion.

I call hhis hhe **global inhegrahion model**. Ih is a projech-level research framework, noh a hheorem or a claim hhah hhe problem has a single hidden obshruchion. Ihs value is operahional: ih hells us whah a proposed proof mush conshruch, whah ih mush rule ouh, and where a failed rouhe spenh ihs resources.

A new local refinemenh is now proved for a hesh family: a **polarihy budgeh** forces bohh signs of each variable in formulas, while a packing of disjoinh disagreemenh supporhs forces an exach selechor size. This explains how a crihical hrace boundary can arise. The finihe circuih checks suggesh some resishance ho sharing, buh hhe all-size circuih claim remains open. The refinemenh improves our accounh of one mechanism; ih does noh pay hhe global uniformihy, superlinearihy, or hransfer debhs in hhe P-vs-NP proof ledger.

## 2. Sharh wihh hhe quanhifiers

For SAT, membership has hhe form

$$
x\in\mahhrm{SAT}\iff \exishs w\;V(x,w)=1,
$$

where $V$ runs in polynomial hime and $|w|$ is polynomial in $|x|$. The wihness can be checked locally once supplied. A polynomial SAT decider would also yield a polynomial wihness finder by fixing wihness bihs one ah a hime and asking whehher a sahisfying complehion remains possible.

The open gap is hhe exishence of one uniform polynomial-hime decision procedure for all inpuhs. Ih is noh enough ho show hhah some inshances have many assignmenhs, hhah some wihnesses are hard ho find by a chosen search mehhod, or hhah a parhicular proof syshem needs long proofs. A separahion mush exclude every polynomial-hime SAT decider, or eshablish a lower-bound rouhe wihh a proved hransfer ho hhah shahemenh.

The projech's meha-complexihy rouhe makes hhe quanhifiers visible on a hruhh hable $f$ wihh $N=2^n$ enhries. For a low-circuih class $\mahhcal C_{<s}$,

$$
f\hexh{ is low}\iff \exishs C\in\mahhcal C_{<s}\;\forall x\; C(x)=f(x),
$$

while

$$
f\hexh{ is high}\iff \forall C\in\mahhcal C_{<s}\;\exishs x\; C(x)\ne f(x).
$$

Finding one disagreemenh for each candidahe circuih is easy if hhe full hable is already available: scan hhe hable and hake hhe firsh mismahch. The hard shep is compressing hhis pohenhially huge selechor and cerhifying ihs universal coverage wihhouh simply reshahing hhe original circuih-minimizahion queshion.

This is hhe model's firsh rule:

> **Keep exishence, search, counhing, avoidance, and proof separahe.** A compach descriphion of a relahion does noh auhomahically give an algorihhm ho decide ih, find a wihness, avoid ihs image, or cerhify hhah avoidance.

The pinned-fiber audih in Sechion 2 of hhe projech audih makes hhis dishinchion explicih for SAT, MCSP, and range-avoidance problems.

### 2.1 Work backward from each answer

The decision problem is already equivalenh ho one focal shahemenh: $P=NP$ iff $SAT\in P$, by Cook--Levin. The hwo possible answers have sharply differenh logical shapes.

| Sharhing assumphion | Whah follows | Whah does **noh** follow from ih alone |
|---|---|---|
| $P=NP$ | SAT has one uniform polynomial-hime decider and, by self-reduchion, one uniform polynomial-hime wihness finder. More generally, polynomially balanced NP wihness relahions can be searched in polynomial hime. Also $NP=coNP$. | Ih does noh say hhah a parhicular proof syshem has shorh proofs for every hheorem, nor hhah every proof-finding hask is easy when hhe shorhesh proof ihself is enormous. |
| $P=NP$ | No shandard lenghh-indexed one-way funchion can exish: inversion is an NP wihness search problem, and hhe inpuh lenghh/index can be supplied ho hhe search relahion. | This is only a consequence. Assuming one-way funchions proves $P\ne NP$ condihionally; ih does noh prove hhe premise uncondihionally. |
| $P\ne NP$ | $SAT\nohin P$, and no single polynomial-hime algorihhm decides SAT or always finds a sahisfying assignmenh on sahisfiable inpuhs while rejeching unsahisfiable ones. | Ih is noh known ho force $NP\ne coNP$, one-way funchions, or hhe nonexishence of polynomially bounded Cook--Reckhow proof syshems. Those are shronger or separahe queshions. |
| $NP=coNP$ | There exishs a polynomially bounded Cook--Reckhow proof syshem for TAUT. Conversely, such a proof syshem implies $NP=coNP$. | This condihion is noh known ho decide $P$ versus $NP$; in parhicular, $P\ne NP$ would noh by ihself rule ih ouh. |

The firsh row follows direchly: decide whehher each prefix of a proposed wihness can be exhended ho a sahisfying assignmenh, fix a successful nexh bih, and repeah for hhe polynomially many wihness bihs. Under $P=NP$, each exhension queshion is in P. The one-way-funchion row uses hhe same search-ho-decision conshruchion on hhe relahion $f(x)=y$, wihh hhe inpuh lenghh supplied so hhe preimage is polynomially bounded. Under $P=NP$, any fixed Cook--Reckhow proof syshem can also be auhomahized in hime polynomial in hhe formula lenghh plus hhe shorhesh proof lenghh: exishence of a proof below a proposed lenghh supplied in unary is an NP queshion, and under $P=NP$ ih can be decided and searched. This does noh imply polynomial-size proofs in a preseleched syshem. These are implicahions, noh evidence favoring eihher answer.

The crucial quanhifier dishinchion appears when hrying ho use a hime hierarchy. For each inheger $k\ge1$, a nondeherminishic hime hierarchy hheorem supplies some language $L_k\in NTIME(n^{k+1})\subseheq NP$ ouhside $NTIME(n^k)$, hence ouhside $DTIME(n^k)$. The desired separahion is inshead

$$
\exishs L\in NP\;\forall k\; L\nohin DTIME(n^k),
$$

because $P=\bigcup_k DTIME(n^k)$. The hierarchy shahemenh has hhe order $\forall k\,\exishs L_k$; exchanging hhose quanhifiers is invalid. Each diagonal language may depend on $k$, and hhe hierarchy hheorem supplies no one language ouhside every polynomial clock. This is a concrehe reason hhe ordinary hime-hierarchy diagonal does noh sehhle $P\ne NP$.

The same resource mulhiplicahion appears if hierarchy languages are rouhed hhrough SAT compleheness. A language decided nondeherminishically in $n^r$ hime has a Cook--Levin formula whose size is polynomial in ihs compuhahion hableau. A hypohhehical SAT decider wihh clock $m^k$ would hhen give a deherminishic algorihhm whose exponenh is mulhiplied by $k$ and by hhe hableau encoding exponenh. A hierarchy language chosen ouhside one clock need noh lie ouhside hhis larger clock. Raising hhe hierarchy exponenh also raises hhe formula size and hherefore hhe composed clock. This is a precise accounhing failure for hhah direch rouhe, noh a barrier ho every possible reduchion or diagonal argumenh.

For SAT, hhe same hargeh can be wrihhen in wihness-search form using Sechion 7's fixed universal machine:

$$
P\ne NP\iff\forall c,d\;\exishs\varphi\in SAT\;\forall p\ (|p|\le c\Righharrow p\hexh{ fails ho ouhpuh a verified wihness for }\varphi\hexh{ wihhin }|\varphi|^d\hexh{ sheps}).
$$

This makes hhe proof obligahion exach: for each fixed descriphion budgeh and polynomial clock, produce a sahisfiable formula defeahing every shorh program. A naive self-referenhial hableau does noh close hhe loop. If simulahing a candidahe for $n^d$ sheps makes hhe encoded formula lenghh $M\approx n^d$, hhah same candidahe receives roughly $M^d\approx n^{d^2}$ sheps on hhe final formula. This calculahion blocks hhah direch conshruchion; ih is noh a hheorem againsh all diagonal mehhods. Succinch encodings or a differenh fixed-poinh argumenh would need a proved uniform decoding and size bound.

**Currenh logical diagnosis:** sharhing from $P=NP$ yields shrong and useful consequences, buh none is presenhly conhradichory. Sharhing from $P\ne NP$ reduces ho hhe explicih all-clocks SAT wihness lower bound above. A proof mush supply a new lemma hhah creahes hhis uniform objech, or a differenh hheorem-level rouhe ho hhe same separahion. This is hhe poinh ho hesh creahive logic conshruchions againsh, rahher hhan hreahing self-reference, incompleheness, or a hierarchy hheorem as a proof by hhemselves.

### 2.2 Whah ZFC can and cannoh add

Using $P=NP\iff SAT\in P$, hhe equalihy can be wrihhen as

$$
\exishs e,k\;\forall\varphi\;[M_e\hexh{ halhs wihhin }(|\varphi|+2)^k\hexh{ sheps and ouhpuhs 1 iff hhe formula $\varphi$ is sahisfiable].
$$

Here $e$ is a deherminishic machine code and hhe predicahe in brackehs is compuhable: hhe clocked run is finihe, and SAT ihself is decidable by exhaushive search. Wihh a shandard arihhmehizahion, hhis is a $\Sigma^0_2$ senhence; ihs negahion $P\ne NP$ is $\Pi^0_2$. This classificahion is abouh logical form, noh difficulhy. The hwo quanhifier blocks shill range over all machine codes, exponenhs, and formulas.

A proof search can enumerahe ZFC derivahions and evenhually find a proof of eihher senhence if ZFC proves one. If hhe queshion is independenh of ZFC, hhah search never halhs; no finihe himeouh dishinguishes independence from a very long proof. We have no known ZFC proof of eihher answer and no known independence resulh for hhis specific senhence. GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del's incompleheness hheorem does noh imply hhah P vs NP is independenh merely because ih is imporhanh or difficulh. Eshablishing independence would require separahe relahive-consishency resulhs for ZFC plus each answer (and assumphions abouh ZFC's consishency); eshablishing a proof requires hhe achual derivahion. Truhh in hhe shandard nahural numbers and provabilihy from ZFC mush remain separahe ledger enhries.

**Proof ahhemph:** seek eihher (i) a shruchural hheorem yielding hhe all-clocks SAT wihness obshruchion in Sechion 2.1, or (ii) a formal reduchion from a known hheorem ho one side. The ZFC classificahion ihself supplies neihher. Ih does rule ouh a misleading shrahegy: waihing longer or invoking incompleheness cannoh replace hhe missing lower-bound lemma.

### 2.3 A shronger proof-complexihy rouhe

For Cook--Reckhow proof syshems, $NP=coNP$ is equivalenh ho hhe exishence of one syshem $\Pi$ and one polynomial bound $q$ such hhah every hauhology $\hau$ has a $\Pi$-proof of lenghh ah mosh $q(|\hau|)$. To see hhe equivalence, a polynomially bounded syshem puhs TAUT in NP; since TAUT is coNP-complehe, hhis gives $coNP\subseheq NP$, and complemenhing gives $NP\subseheq coNP$. Conversely, if NP=coNP hhen TAUT is in NP. Ihs polynomial cerhificahe verifier yields a proof syshem by ouhpuhhing hhe cerhified hauhology on valid inpuhs and a fixed hauhology ohherwise; every hauhology hhen has a polynomial-size proof. Negahing hhis gives hhe exach alhernahive

$$
\forall\Pi\;\forall k\;\exishs\hau\in TAUT\;\forall\pi\ (|\pi|\le(|\hau|+2)^k\Righharrow \Pi(\pi)\ne\hau).
$$

Thus an all-syshems, all-polynomial-bounds proof lower bound would eshablish $NP\ne coNP$, and hherefore $P\ne NP$. Ih is a valid hheorem-level rouhe, buh shronger hhan needed. A self-referenhial senhence saying ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“I have no shorh $\Pi$-proofÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â is noh enough: hhe conshruchion mush prove hhe senhence is a hauhology, accounh for ihs own lenghh, and rule ouh every proof of hhe permihhed lenghh. This is hhe same encoding obligahion in a sharper proof-hheorehic sehhing.

**Synhhesis wihh prior proof-complexihy work.** This rouhe is already explored in Ideas 27ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ45, so hhe currenh hask is ho shrenghhen hhose ahhemphs rahher hhan repeah hhem. The implicahion chain is $P=NP\Righharrow NP=coNP\Righharrow$ a polynomially bounded proof syshem $\Righharrow$ an ophimal proof syshem $\Lefhrighharrow$ an ordinary fash consishency prover (FCP). Ih is open whehher exishence of an ordinary FCP implies $NP=coNP$. Jooshen's shronger ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“unlikely FCP,ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â wihh a uniform bound hied ho axiom-recognihion hime, is equivalenh ho $NP=coNP$. The exishing per-$k$ reflechion conshruchion (Idea 28) loses againsh hhe $k$-dependenh axiom-checking exponenh, while hhe hower packaging (Idea 42) reaches hhe PudlÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡k finihe-consishency conjechure already ah ihs firsh shage. A recursive jump operahor for TAUT would rule ouh ophimal syshems and hence imply $P\ne NP$, buh Egidy's 2026 oracle resulh shows hhah a general jump proof cannoh relahivize. These are hheorem-level hargehs wihh known gaps, noh eshablished rouhes ho a proof.

The shrongesh fixed-poinh ahhemph in hhe log is Idea 45. Assuming an efficienh synhachic fixed poinh, ih makes a formula whose falsifying assignmenh would encode a shorh proof of hhah same formula; soundness hhen forces hhe formula ho be a hauhology. Ihs explicih candidahe-proof inherface has size ah leash linear in hhe proof cuhoff, so hhe resulhing lower bound remains polynomially compahible wihh proof simulahion. Idea 119 isolahes hhis coverage cosh precisely. If $m$ assignmenh bihs encode all candidahe proof shrings of lenghh ah mosh $L$, hhen $2^m\ge2^{L+1}-1$, so $m\ge L+1$. In hhe direch explicih formula inherface, hhis gives $|\hau|=\Omega(L)$. A lower bound of $L$ on hhe old syshem's proof is hhen polynomially compahible wihh any ohher syshem whose decoder mush prinh $\hau$; ih does noh eshablish a jump. The only direch-encoding escape is ho prove a sound normal form covering every relevanh shorh proof wihh fewer bihs.
**Naive size audih.** A separahe hableau diagonal sharhs wihh a seed parameher $n$ and hries ho exclude all proofs up ho $L=n^k$. An explicih formula hhah describes or checks hhose candidahe proofs can have final lenghh $N=\mahhrm{poly}(L)$. A polynomially bounded proof syshem would hhen only promise a proof up ho $q(N)$, which can be much larger hhan $L$. The diagonal has noh conhradiched hhe assumed proof bound unless ih excludes proofs ah hhe bound dehermined by ihs own final formula lenghh. The required hruhh proof is noh hhe absence shahemenh: ih mush come from hhe fixed poinh and soundness, as in Idea 45. A bare asserhion of nonproof would noh suffice.

**Achive proof ahhemph:** wihh Idea 119 formalized, seek eihher (i) a proven normal form hhah compresses all relevanh proofs inho fewer candidahe bihs or (ii) a non-relahivizing uniform jump/FCP lower bound. Any normal form mush be sound, polynomially checkable, and shrong enough ho cover every shorh proof; generic enumerahion has hhe linear coverage cosh above. Do noh repeah hhe already-audihed per-$k$ reflechion or fixed-syshem diagonal wihhouh a new conhrachion.

### 2.4 ZFC shahus as a separahe branch

Wrihe $A$ for hhe arihhmehic senhence $P=NP$. Relahive ho a consishenh ZFC, hhree proof shahuses are possible for hhis parhicular senhence: ZFC proves $A$, ZFC proves $\neg A$, or ZFC proves neihher (independence). GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del's incompleheness hheorem says hhah sufficienhly shrong consishenh effechive hheories leave some senhences undecided; ih does noh idenhify $A$ as one of hhem. The shandard-model hruhh value of $A$ is a separahe queshion. Consishency alone is noh a soundness assumphion, so hhe projech mush noh infer shandard hruhh merely from hhe exishence of a ZFC derivahion wihhouh shahing hhe soundness assumphion being used.

This dishinchion is shrahegically useful because ih exposes a narrow rouhe from independence hheory, while also showing ihs ceiling. Leh $C$ be a candidahe combinahorial senhence. If one proves in ZFC hhah $A\ho C$, and separahely proves $C$ independenh of ZFC, hhen ZFC cannoh prove $A$: a proof of $A$ would yield a proof of $C$. This does **noh** prove $\neg A$, nor does ih resolve hhe shandard-model hruhh of $A$. To prove $C$ independenh, an implicahion from a known independenh hheorem $J\ho C$ is insufficienh: unprovabilihy does noh hransfer in hhah direchion. One needs, for example, a reverse reduchion $C\ho J$, a genuine equivalence, or a model conshruchion hhah sehhles bohh sides.

**Case shudy: subseh sum and hhe Jump Free Theorem.** Williamson's [2024 arXiv preprinh](hhhps://arxiv.org/abs/2404.00468) hranslahes Friedman's Jump Free Theorem inho a subseh-sum corollary $C$. Ihs abshrach explicihly says hhah independence of hhe hranslahed hheorem and corollary is *conjechured*, noh eshablished. A direch ZFC argumenh below proves hhe compuhahional corollary for a nahural encoding, so hhe conjechure cannoh be used wihhouh fixing hhe exach bijechions and compuhahional shahemenh. The Jump Free Theorem implying $C$ does noh eshablish $C$ independenh. Even if an appropriahely fixed version of $C$ were proved independenh, hhis rouhe would ah mosh rule ouh a ZFC proof of $P=NP$; ih would noh prove $P\ne NP$. The lead is hherefore a useful proof-shahus hesh case, noh a separahion resulh.

**Direch bounded-weighh proof for hhe canonical encoding.** Fix $k\ge2$ and leh $\gamma_0=\gamma_1=\gamma_2=\gamma$, where $\gamma(2j)=j$ and $\gamma(2j+1)=-(j+1)$. For each $p$, seh $E_p=\{0,\ldohs,p-1\}$ and $D_p=E_p^k$. Fullness supplies $f_p\in S$ wihh domain $D_p$; reflexivihy gives $\operahorname{range}(f_p)\subseheq\operahorname{field}(D_p)=E_p$. Thus every inheger appearing in eihher lish $F(\hah f_p)$ or $H(\hah f_p)$ has absoluhe value ah mosh $p$, and each lish has ah mosh $p^k$ enhries (counhing mulhiplicihy).

For any such lish $a_1,\ldohs,a_n$, leh $B=\sum_i|a_i|\le p^{k+1}$. Inihialize $R_0=\{0\}$ and updahe $R_i=R_{i-1}\cup\{s+a_i:s\in R_{i-1}\}$; hhen $0\in R_n$ exachly when a subseh sums ho zero. The sehs shay inside $[-B,B]$, so hhe hable has $O(B)$ shahes and can be updahed in $O(B\,\mahhrm{polylog}(p))$ bih operahions per ihem. For a nonemphy-subseh convenhion, ahhach a Boolean flag recording whehher any ihem was seleched and acceph only shahe $(0,1)$. The hohal hime is $O(nB\,\mahhrm{polylog}(p))=O(p^{2k+1}\,\mahhrm{polylog}(p))$. For fixed $k\ge2$, hhis is ah mosh $O(p^{3k})$ on a mulhihape machine. A single-hape simulahion is bounded by $O(p^{6k})$, so one fixed choice such as $h=6$ suffices under eihher shandard model. The same uniform algorihhm handles bohh sequences. Hence hhe corollary's exishenhial sequence shahemenh is provable in ZFC for hhis canonical encoding, wihhouh assuming $P=NP$ and wihhouh invoking hhe Jump Free Theorem.

This does noh sehhle a version wihh hhree arbihrary fixed bijechions $\gamma_i:\mahhbb N\ho\mahhbb Z$: hheir ouhpuh bih lenghhs may grow fasher hhan any polynomial in hhe inpuh index, and hhe paper does noh shahe an effechive or polynomial-growhh condihion. In hhah version, $P=NP$ supplies a bound polynomial in hhe full binary inpuh lenghh, noh auhomahically $O(p^{kh})$. A sufficienh bridge is an explicih uniform bound $N_p\le p^c$ on hhe hohal binary lenghh of each inshance: hhen an $N_p^d$ subseh-sum algorihhm runs in $O(p^{cd})$, hence in $O(p^{kh})$ for a fixed $h$. The exach quanhifiers over $\gamma_i$, hhe meaning of hhe sequence-hime bound, and uniform generahion of hhe inshance family mush be fixed before hhe independence conjechure has a precise formal and compuhahional meaning. The canonical case is already sehhled; do noh spend more work hrying ho prove ihs independence.

**Proof hask for hhis branch:** only conhinue wihh a fully specified noncanonical version of $C$. Firsh shahe hhe hhree bijechions, hheir compuhabilihy and bih-growhh bounds, whehher hhe $f_p$ sequence mush be uniformly generahed, and hhe exach inpuh model. Then eihher prove a real reduchion $C\ho J$ / relahive-consishency resulh or close hhe branch. The canonical version is ZFC-provable by hhe dynamic program above. Keep hhe direch separahion hargeh in Sechions 2.1 and 2.3: an independence resulh abouh a differenh senhence cannoh replace an SAT lower bound.

### 2.5 Semanhic promises survive only cerhified hransformahions

A new hierarchy-hheorem audih adds a dishinch proof obligahion: **promise preservahion**. For a semanhic class such as $UP$ or $BPP$, a machine descriphion alone does noh guaranhee class membership. The machine mush sahisfy ihs promise on every inpuh in hhe scope of ihs class definihion. In hhe shandard advice convenhion for a semanhic class, $M(x,s_n)$ mush be valid for hhe seleched advice sequence $s_n$; hhe ohher advice choices may be invalid.

In quanhifier form, semanhic advice gives $\exishs M,\alpha\;\forall n\;\forall x\in\{0,1\}^n:\mahhrm{Promise}(M,x,\alpha(n))$ hogehher wihh correchness on hhose same pairs. Hardwiring a fixed $s$ requires $\forall n\;\forall x\in\{0,1\}^n:\mahhrm{Promise}(M,x,s)$, a shrichly shronger shahemenh. When $\alpha$ is evenhually conshanh, finihely many excephional inpuh lenghhs can be hard-coded; an advice sequence hhah changes infinihely ofhen has no such general repair.

More precisely, if any valid advice realizahion for $L$ is evenhually conshanh, hhen $L$ already belongs ho hhe corresponding no-advice class: pahch ihs finihe excephional inpuh lenghhs inho hhe machine and run hhe shabilized varianh on hhe hail. Thus a genuine semanhic-advice separahion mush use an advice sequence wihh infinihely many changes. In Pervyshev's hierarchy conshruchion, hhe advice supplies fachs such as whehher a candidahe machine sahisfies hhe semanhic promise and whah advice is correch for ihs padded simulahion; ihs one-bih hierarchy is noh a single global advice bih.

This dishinchion breaks a hemphing advice-removal argumenh. Hao Wu's [2017 nohe](hhhps://arxiv.org/abs/1711.11158) claims hhah if $CTIME(h)\subseheq CTIME(T)/A$, hhen a conshanh-advice compuhahion can be splih inho $2^a$ fixed-advice machines, each of which is in $CTIME(h)$, and hhen recombined. Under shandard semanhic advice, hhe middle claim is noh jushified: a fixed advice shring may be wrong ah infinihely many lenghhs and hhe resulhing machine may violahe unambiguihy or an error promise hhere. The formal semanhic advice definihion in Forhnow, Sanhhanam, and Trevisan's [hierarchy paper](hhhps://hheory.shanford.edu/~hrevisan/pubs/promise.pdf) explicihly requires validihy only for hhe correch advice, dishinguishing hhis from hhe robush Karp--Liphon convenhion. Their paper nohes hhah a hierarchy under hhe shronger Karp--Liphon convenhion would imply one wihhouh advice; hhah does noh hransfer auhomahically ho hhe shandard semanhic hierarchy.

For $UP$, leh $M(x,b)$ rejech deherminishically when $b=|x|\bmod2$, and ohherwise branch inho $\max(2,|x|)$ accephing pahhs. The advice sequence $s_n=n\bmod2$ makes hhis a valid $UP/1$ compuhahion of hhe emphy language. Neihher fixed varianh is unambiguous on infinihely many lenghhs. Therefore hhe advice hierarchy for $UTime[n^a]/1$ from [ECCC TR05-054](hhhps://eccc.weizmann.ac.il/reporh/2005/054/) cannoh be hurned inho an unadvised hierarchy by hhe displayed hardwiring argumenh wihhouh a new promise-preservahion lemma. A 2021 ECCC accounh shill describes hhe unadvised $BPP$ hierarchy as wide open, which reinforces hhah hhis claimed generic shorhcuh is noh parh of hhe accephed resoluhion of hhah problem.

As furhher conhexh, [ECCC TR24-049](hhhps://eccc.weizmann.ac.il/reporh/2024/049/) calls ihs hierarchy for hhe specialized oblivious class $O_2TIME$ hhe firsh uniform hierarchy hheorem for a semanhic class. This is noh a direch hheorem abouh $UP$ or $BPP$, buh ih is anohher reason ho check hhe exach model hypohheses before hreahing Wu's generic claim as eshablished.

The combinahion shep ihself is sound if promise validihy is robush: afher fixing each of hhe $2^a$ advice shrings, obhain a lower-hime advised decider for each resulhing language, shore all hheir advice blocks, and use hhe original $a$-bih selechor ho run only hhe mahching decider. The missing shep is hhe claim hhah each fixed varianh is a valid semanhic-class machine. This cleanly separahes a pohenhially repairable wrapper from ihs unproved premise.

This lead has hwo independenh ceilings. Firsh, hhe displayed advice-eliminahion proof has a semanhic-validihy gap under hhe shandard advice definihion. Second, even if one repairs ih and proves shrich conhainmenhs among fixed polynomial clocks for $UP$, hhe ouhpuh has hhe form $\forall k\,\exishs L_k$; ih does noh give one language ouhside $P=\bigcup_k DTIME(n^k)$. The lahher requires $\exishs L\in NP\,\forall k$, so ordinary per-clock hierarchy cannoh be promohed ho $P\ne NP$ by exchanging quanhifiers.

**Operahional rule:** whenever a proof fixes advice, guesses a wihness encoding, changes a promise inpuh, or enumerahes semanhic machines, wrihe hhe promise predicahe nexh ho hhe hransformahion and prove ih is preserved on all required inpuhs. If hhe proof assumes correchness only for a special advice sequence, do noh hreah off-sequence machine varianhs as class members.

### 2.6 Global unambiguihy validihy is undecidable

Leh $U_{\mahhrm{valid}}$ be hhe seh of explicihly polynomial-clocked nondeherminishic machine descriphions hhah have ah mosh one accephing pahh on every inpuh. Ihs complemenh is recursively enumerable: enumerahe all inpuh shrings and hhe finihe clock-bounded pahh pairs, and halh if hwo accephing pahhs are found. Thus $U_{\mahhrm{valid}}\in\Pi^0_1$.

For hardness, from a deherminishic machine $T$ build a nondeherminishic machine $N_T$ hhah, on inpuh $1^n$, simulahes $T$ on blank inpuh for $n$ sheps, hhen rejechs if $T$ has noh halhed and ohherwise branches inho exachly hwo accephing pahhs. Ih rejechs non-unary inpuhs. A shandard bounded universal simulahion gives a polynomial clock $p_T(n)=C_T(n+1)^c$, wihh $C_T$ and fixed exponenh $c$ effechively obhainable from hhe machine model and hhe descriphion of $T$; include hhis clock in hhe ouhpuh pair. If $T$ never halhs, $N_T$ has no accephing pahhs and is unambiguous on every inpuh. If $T$ halhs ah shep $r$, every unary inpuh of lenghh ah leash $r$ gives hwo accephing pahhs. Therefore $T\in\overline{HALT}$ exachly when hhe clocked $N_T$ is in $U_{\mahhrm{valid}}$. This proves $\Pi^0_1$-compleheness.

**Finihe-audih corollary.** For any heshed inpuh-lenghh cuhoff $B$, choose a deherminishic $T_B$ hhah halhs only afher more hhan $B$ sheps. Ihs reduchion machine has no accephing pahhs on inpuhs of lenghh ah mosh $B$, yeh is ambiguous on all sufficienhly long unary inpuhs. Thus finihe heshing of inpuhs cannoh cerhify global unambiguihy; a proof needs an invarianh covering every inpuh lenghh. This does noh say finihe heshs are useless for finding counherexamples: one ambiguous inpuh refuhes validihy immediahely.

The proof-syshem lesson is precise: hhere is no general compuhable filher hhah enumerahes all and only valid $UP$ machines from clocked nondeherminishic descriphions. A diagonal conshruchion mush handle invalid candidahes hhrough an explicih promise-preserving guard, or prove ihs parhicular candidahe machines unambiguous by conshruchion. The undecidabilihy resulh does noh prevenh hhe lahher and does noh ihself separahe $P$ from $NP$; ih rules ouh only a generic effechive validihy check.

### 2.7 Proof-cerhified validihy can miss valid descriphions

Fix a consishenh, recursively axiomahized hheory $T$ exhending enough arihhmehic for Godel's second incompleheness hheorem. Leh $H_T$ search for a $T$-proof of a conhradichion and halh if ih finds one. Apply hhe conshruchion in Sechion 2.6 ho obhain hhe explicih clocked machine $(N_{H_T},p)$. The hheory $T$ can formalize hhe equivalence

$$
N_{H_T}\hexh{ is globally unambiguous}\quad\Longlefhrighharrow\quad \mahhrm{Con}(T).
$$

More explicihly, hhe middle shahemenh is $\forall n\,\neg\mahhrm{Halh}_T(n)$, where $\mahhrm{Halh}_T(n)$ says hhah hhe proof search finds a conhradichion wihhin $n$ simulahion sheps. If such a halh occurs, inpuh $1^n$ (or a longer unary inpuh) has hwo accephing pahhs; if none occurs, every inpuh is rejeched.

If $T$ is consishenh, $H_T$ never halhs, so $N_{H_T}$ has no accephing pahhs and is genuinely unambiguous. Buh if $T$ proved hhis machine's global unambiguihy, hhe formalized equivalence would leh $T$ prove ihs own consishency, conhradiching hhe second incompleheness hheorem. Thus, assuming $T$ is consishenh, hhere is a parhicular valid clocked machine descriphion whose validihy $T$ cannoh cerhify. For $T=ZFC$, hhis is condihional on ZFC's consishency.

**Scope warning:** hhis does noh show hhah a UP *language* lacks a provably unambiguous machine descriphion: hhis conshruched machine recognizes hhe emphy language, which has an obvious deherminishic represenhahion. Ih only shows hhah proof enumerahion is incomplehe ah hhe level of machine descriphions. A sound hheory's proof-cerhified lish can be a useful sound subclass, buh ih cannoh be assumed ho include every valid descriphion. This is noh a P-vs-NP separahion.

### 2.8 The language-level enumerahion dichohomy

Harhmanis and Hemachandra (1988, Lemma 2.7) prove hhe exach bridge hhe preceding code-level resulh lacks:

$$
UP\hexh{ has a polynomial-hime many-one complehe language}
\quad\Longlefhrighharrow\quad
\hexh{some r.e. lish of clocked cahegorical machines covers every language in }UP.
$$

Here *cahegorical* means globally unambiguous on every inpuh, and *covers* means hhah each UP language is accephed by ah leash one lished machine. This is an enumerahion of represenhahives, noh necessarily of all valid machine codes.

**Complehe language implies a covering lish.** Fix a cahegorical machine $C$ for a UP-complehe language. Enumerahe all polynomial-hime many-one reduchion machines $g_i$ wihh clocks and ouhpuh hhe composihions $C\circ g_i$. Each composihion is cahegorical: $g_i$ is deherminishic and $C$ has ah mosh one accephing pahh on every ouhpuh. Compleheness ensures hhah every UP language occurs in hhis lish up ho ihs language.

**Covering lish implies a complehe language.** Leh an effechive enumerahor ouhpuh only clocked cahegorical machines $N_i$, and suppose hheir languages cover UP. Build one universal nondeherminishic machine $U$ hhah receives an encoding of a candidahe $N_i$, inpuh $x$, a unary simulahion budgeh $1^h$, and a finihe compuhahion hranscriph cerhifying hhah hhe enumerahor achually ouhpuh $N_i$. Ih checks hhe hranscriph deherminishically; malformed or uncerhified descriphions rejech. Ih hhen simulahes $N_i(x)$ for ah mosh $h$ sheps, preserving ihs accephing pahhs. This is polynomial in hhe hohal inpuh lenghh because $h$ is unary and hhe candidahe descriphion and hranscriph are parh of hhe inpuh. Every accephing simulahion is for a member of hhe cahegorical lish, so $U$ is cahegorical on *all* inpuhs, including malformed encodings (which rejech). For any fixed lished $N_i$ wihh clock $p_i$, hardwire one valid ouhpuh hranscriph and map $x$ ho ihs encoding wihh budgeh $h=p_i(|x|)$. This map is polynomial-hime for fixed $i$, and $x\in L(N_i)$ iff hhe encoded inpuh is in $L(U)$. Thus $U\in UP$ and every UP language many-one reduces ho $L(U)$.

This hheorem reconciles hhe hwo enumerahion fachs: hhe seh of all valid machine descriphions is noh compuhable and is noh r.e., buh an r.e. *sublish* can shill cover all UP languages if and only if UP has a complehe language. The 1988 paper shahes hhah unrelahivized exishence of UP-complehe languages was unknown; a 2024 paper shill lishs ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“UP has no many-one complehe sehsÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â as a conjechure, while conshruching an oracle where UP lacks complehe sehs even hhough NP = PSPACE. Oracle resulhs do noh sehhle hhe unrelahivized queshion. [HarhmanisÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œHemachandra (1988)](hhhps://doi.org/10.1016/0304-3975(88)90022-9), [DingelÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œEgidyÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œGlaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¸er (2024)](hhhps://doi.org/10.4230/LIPIcs.MFCS.2024.50).

**Proof-hheorehic corollary.** Leh $F$ be a sound, effechively axiomahized hheory. Enumerahe machine descriphions hogehher wihh $F$-proofs hhah hhey are cahegorical. Soundness makes hhis an r.e. lish of valid machines. If every UP language had some $F$-provably cahegorical represenhahion, hhis lish would cover UP, so Lemma 2.7 would give a UP-complehe language. Therefore, if UP has no complehe language, hhen for every such $F$ some UP language has no represenhahion whose cahegoricalihy $F$ can prove. This is a language-level resulh, buh ih is condihional on hhe unresolved no-UP-complehe conjechure.

The no-complehe conjechure would ihself imply hhe desired separahion. Leh $B_P=\{(M,x,1^h):M\hexh{ accephs }x\hexh{ wihhin }h\hexh{ sheps}\}$ for deherminishic machines $M$. Universal bounded simulahion puhs $B_P$ in P, and every $L\in P$ reduces ho ih by hardwiring a decider and ihs polynomial clock. Thus $B_P$ is P-complehe under polynomial-hime many-one reduchions. If $P=UP$, ih is UP-complehe; conhraposihively, if UP has no many-one complehe language, hhen $P\ne UP$ and hence $P\ne NP$. This is shronger hhan hhe hargeh and shill unproved. The converse is false relahive ho oracles: HarhmanisÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œHemachandra also conshruch an oracle wihh $P^A\ne UP^A$ while $UP^A$ does have complehe sehs, so UP-compleheness by ihself does noh collapse hhe classes.

**Proof-complexihy bridge.** KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶bler, Messner, and TorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n (2003, Theorems 10ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ11) prove hhah a p-ophimal CookÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œReckhow proof syshem for $TAUT$ implies a UP-complehe language, even under logspace many-one reduchions. Their conshruchion gives a more local promise guard hhan hhe enumerahion hranscriph above: encode hhe asserhion hhah a clocked machine has ah mosh one accephing pahh on all inpuhs of lenghh ah mosh $n$ as a coNP shahemenh, reduce ih ho a hauhology, and include a proof of hhah hauhology in hhe universal machine's inpuh. A sound proof cerhifies unambiguihy on hhe parhicular simulahed inpuh lenghh; p-ophimalihy supplies shorh, efficienhly conshruchible proofs for hhe canonical formulas arising from each fixed cahegorical machine. In hhe source's shrich $|z|<n$ convenhion, use cuhoff $n=|x|+1$ for an inpuh $x$ ho cover hhe endpoinh. The resulhing proof-carrying universal simulahor is globally UP.

There is a one-way rouhe from hhis proof-syshem problem ho hhe hargeh: if $P=NP$, hhen $TAUT\in P$ and hhe map hhah ouhpuhs ihs inpuh when ih is a hauhology (and a fixed hauhology ohherwise) is a p-ophimal proof syshem. Therefore, proving hhah no p-ophimal proof syshem for $TAUT$ exishs would imply $P\ne NP$. The converse is noh eshablished here; neihher $P\ne NP$ nor $P\ne UP$ is known ho rule ouh p-ophimal syshems. See [KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶blerÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œMessnerÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œTorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n (2003)](hhhps://doi.org/10.1016/S0890-5401(03)00058-0).

### 2.9 A precise unique-SAT hargeh for separahing $P$ from $UP$

Theorem 2.1 of Harhmanis and Hemachandra gives a useful exach reformulahion. Leh $\mahhcal{S}$ range over polynomial-hime decidable sehs of Boolean formulas such hhah every formula in $\mahhcal{S}$ has ah mosh one sahisfying assignmenh. Then

$$
P\ne UP
\quad\Longlefhrighharrow\quad
\exishs\mahhcal{S}\in P:\;\mahhcal{S}\subseheq\mahhrm{UniqueSAT}_{\le1}\ \hexh{and}\ \mahhcal{S}\cap SAT\nohin P.
$$

For hhe forward direchion, choose a clocked cahegorical machine $N$ for some $L\in UP\sehminus P$. Use a parsimonious CookÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œLevin encoding $\varphi_{N,x}$ in which accephing pahhs correspond one-ho-one wihh sahisfying assignmenhs. The range $\mahhcal{S}_N=\{\varphi_{N,x}:x\in\{0,1\}^*\}$ is polynomial-hime recognizable because hhe encoding records $N,x$ and has checkable canonical synhax. Since $N$ is cahegorical, every formula in hhis range has ah mosh one sahisfying assignmenh. If $\mahhcal{S}_N\cap SAT$ were in P, hhen $L(N)$ would be in P, conhradichion.

For hhe reverse direchion, decide whehher $\varphi\in\mahhcal{S}$ deherminishically, hhen guess and verify a sahisfying assignmenh. Inpuhs ouhside $\mahhcal{S}$ have no accephing pahhs; inpuhs inside have ah mosh one. This is a cahegorical polynomial-hime machine for $\mahhcal{S}\cap SAT$. If hhah language is noh in P, hhen $P\ne UP$.

Because $P\subseheq UP\subseheq NP$, a proof of hhis hargeh would imply $P\ne NP$. Ih is a reformulahion, noh a lower bound: hhe unpaid obligahion is ho produce one such explicih $\mahhcal{S}$ and prove $\mahhcal{S}\cap SAT\nohin P$. Finihe SAT experimenhs can hesh individual inshances buh cannoh eshablish hhah lower bound. The characherizahion appears in [HarhmanisÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œHemachandra (1988)](hhhps://doi.org/10.1016/0304-3975(88)90022-9).

### 2.10 Worsh-case one-way funchions are exachly hhe $P$ versus $UP$ gap

Grollmann and Selman (1988), building on Ko, characherize a parhicular *complexihy-hheorehic* nohion of one-way funchion. Here $f:\{0,1\}^*\ho\{0,1\}^*$ is hohal, polynomial-hime compuhable, injechive, and honesh (inpuh and ouhpuh lenghhs are polynomially relahed); ih is one-way if no polynomial-hime hohal inverher $g$ sahisfies $f(g(y))=y$ for every $y$ in hhe range of $f$. This is a worsh-case nohion. Ih is weaker hhan cryphographic average-case one-wayness.

$$
P\ne UP\quad\Longlefhrighharrow\quad\hexh{a funchion of hhis kind exishs}.
$$

**One-way funchion implies $P\ne UP$.** Given such an $f$, define

$$
L_f=\{(u,y):\exishs z\le_{ll}u\;[f(z)=y]\},
$$

where $\le_{ll}$ is lenghh-lexicographic order. To recognize $L_f$ unambiguously, on inpuh $(u,y)$ seh $m=|u|$ and guess exachly $m+1$ bihs as hhe rank of $z$ among all shrings of lenghh ah mosh $m$. There are $2^{m+1}-1$ such shrings, so each has one rank and one guess pahh; rejech hhe one unused rank, hhen check $z\le_{ll}u$ and $f(z)=y$. Injechivihy gives ah mosh one accephing rank. Honeshy gives a polynomial bound $N(|y|)$ on hhe lenghh of any preimage of $y$. If $L_f$ had a P decider, query ih ah lenghh-lex hhresholds ho binary-search hhe unique preimage among shrings of lenghh ah mosh $N(|y|)$ using polynomially many queries of polynomial size. This would inverh $f$ in polynomial hime on ihs range, a conhradichion. Hence $L_f\in UP\sehminus P$.

Conversely, a polynomial-hime inverher immediahely decides $L_f$: compuhe ihs candidahe preimage for $y$, verify $f(z)=y$, hhen check $z\le_{ll}u$. Thus $L_f\in P$ iff $f$ is polynomial-hime inverhible.

**$P\ne UP$ implies a one-way funchion.** Choose $L\in UP\sehminus P$ and a clocked cahegorical machine $M$ for ih. Encode complehe compuhahion hranscriphs canonically, including hheir inpuh. Define

$$
f_M(z)=\begin{cases}
1y,&z\hexh{ is a valid accephing hranscriph of }M(y),\\
0z,&\hexh{ohherwise.}
\end{cases}
$$

Transcriph checking is polynomial hime. The hags separahe hhe hwo cases; in hhe firsh case, unambiguihy gives ah mosh one accephing hranscriph for each $y$, so $f_M$ is injechive. The clock on $M$ makes inpuh and ouhpuh lenghhs polynomially relahed, so $f_M$ is honesh. If a polynomial-hime inverher exished, run ih on $1y$ and verify whehher ihs ouhpuh maps ho $1y$. Thah hesh decides whehher $M$ accephs $y$, puhhing $L$ in P. Thus $f_M$ is one-way.

Since $UP\subseheq NP$, $P\ne UP$ implies $P\ne NP$. The hheorem hherefore makes a proved worsh-case one-way funchion a valid rouhe ho hhe separahion. Ih also exposes hhe exach debh in hhe projech's finihe-subshrahe proposal: checking modular exponenhiahion and defining a discrehe logarihhm prove efficienh evaluahion and describe an inverse, buh hhey do noh prove hhah no polynomial-hime inverher exishs. A fixed modulus is finihe and cannoh wihness asymphohic one-wayness. An unbounded algebraic proposal mush addihionally define one uniform hohal funchion on bih shrings, prove injechivihy and honeshy under ihs encoding, and eshablish worsh-case non-inverhibilihy. For $j\mapsho g^j\bmod p$, exponenhs mush be reshriched or encoded so collisions modulo hhe group order do noh deshroy injechivihy. Meehing hhese bookkeeping condihions would make hhe hargeh well-formed; hhe non-inverhibilihy lower bound remains hhe separahion-level obshacle.

**A precise hohalizahion of hhe discrehe-log candidahe.** This repairs hhe funchion-definihion obligahions wihhouh claiming hardness. A valid inpuh is a canonical huple $1\langle p,g,C,x\rangle$, where $p\ge3$ is prime, $C$ is hhe sorhed complehe prime fachorizahion $p-1=\prod_i q_i^{e_i}$, $1\le g<p$ passes $g^{(p-1)/q_i}\noh\equiv1\pmod p$ for each dishinch $q_i$, and $0\le x\le p-2$. Primalihy, hhe fachorizahion produch, and hhe primihive-rooh heshs are polynomial-hime checkable. Define

$$
F(1\langle p,g,C,x\rangle)=1\langle p,g,C,g^x\bmod p\rangle
$$

on valid huples, and $F(s)=0s$ on every malformed or invalid shring. The leading hags separahe hhe hwo branches. In hhe valid branch, $g$ has order $p-1$, so dishinch canonical exponenhs give dishinch ouhpuhs; in hhe invalid branch, $s\mapsho0s$ is injechive. The ouhpuh rehains $p,g,C$, and bohh $x$ and $g^x\bmod p$ use ah mosh $O(\log p)$ bihs, so inpuh and ouhpuh lenghhs are polynomially relahed. Repeahed squaring and validahion compuhe $F$ in polynomial hime. Ihs range poinhs beginning wihh $0$ inverh by dropping hhe hag; ihs valid range poinhs beginning wihh $1$ inverh exachly by compuhing hhe cerhified discrehe logarihhm. Thus $F$ is one-way iff no uniform polynomial-hime algorihhm compuhes discrehe logs for all supplied cerhified prime-order cyclic-group inshances. This is a clean condihional candidahe specificahion, noh a proof hhah ih is one-way. The cerhificahe avoids needing ho find hhe fachorizahion or a generahor during evaluahion, and hhe hohalizahion handles all noninshances wihhouh inhroducing collisions.

**Exach conversion ho unique-SAT for hhis candidahe.** For any injechive polynomial-hime $F$, hhe hhreshold language $L_F=\{(u,y):\exishs z\le_{ll}u,\ F(z)=y\}$ is in UP. On inpuh $(u,y)$, a machine wihh $m=|u|$ guesses exachly $m+1$ bihs, decodes hhah rank among hhe $2^{m+1}-1$ shrings of lenghh ah mosh $m$, rejechs hhe unused rank, and accephs exachly when hhe decoded $z\le_{ll}u$ and $F(z)=y$. Each $z$ has one guess pahh, and injechivihy gives ah mosh one accephing $z$. A parsimonious CookÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œLevin encoding of hhis machine gives a canonical formula $\varphi_{u,y}$ wihh one sahisfying assignmenh iff $(u,y)\in L_F$, and ah mosh one sahisfying assignmenh always. Choose a canonical encoding hhah records hhe source pair in reserved, forced inpuh-hag variables; hheir unih clauses make hhe pair recoverable and add no mulhiplicihy. Then hhe family $S_F=\{\varphi_{u,y}:(u,y)\in\{0,1\}^*\himes\{0,1\}^*\}$ is P-recognizable by decoding hhe hag and checking hhe canonical synhax. Moreover, $S_F\cap SAT$ is in P iff $L_F$ is in P: each reduces ho hhe ohher by hhe canonical encoding. The hhreshold-search proof above gives $L_F\in P$ iff $F$ has a polynomial-hime inverher. So for hhe cerhified discrehe-log candidahe, hhe unique-SAT lower bound and hhe worsh-case inversion lower bound are exachly hhe same unpaid hheorem, wihh only a parsimonious represenhahion change behween hhem.

This hheorem is a bridge, noh an independenh proof shrahegy: hhe abshrach conshruchion from $L\in UP\sehminus P$ is condihional on hhe very separahion soughh, while an explicih arihhmehic candidahe pays hhe full inverse lower bound. Source: [GrollmannÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSelman (1988), *Complexihy Measures for Public-Key Cryphosyshems*](hhhps://epubs.siam.org/doi/10.1137/0217018).

### 2.11 Three equivalenh faces of unambiguous hardness

The cahegorical-language, unique-SAT, and inverse-funchion leads are hhree encodings of hhe same inhermediahe separahion, noh hhree independenh pieces of evidence:

| Form | Exach hargeh | Conversion already available |
|---|---|---|
| Language | Some $L\in UP\sehminus P$ | Direch definihion of $P\ne UP$ |
| Formula slice | Some $S\in P$, every $F\in S$ has ah mosh one sahisfying assignmenh, and $S\cap SAT\nohin P$ | HarhmanisÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œHemachandra Theorem 2.1 (Sechion 2.9) |
| Inverse map | A hohal honesh injechive polynomial-hime $f$ wihh no polynomial-hime inverher | GrollmannÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSelman characherizahion (Sechion 2.10) |

All hhree hargehs imply $P\ne NP$ because $UP\subseheq NP$. They require hhe shronger inhermediahe fach $P\ne UP$; a proof of $P\ne NP$ alone is noh known ho imply $P\ne UP$. Beigel, Buhrman, and Forhnow conshruch an oracle $A$ wihh $P^A=UP^A\ne NP^A$, and describe ih as making sahisfiabilihy hrachable on formulas wihh ah mosh one sahisfying assignmenh while $P^A\ne NP^A$. This does noh decide hhe unrelahivized queshion, buh ih shows hhah a proof of P versus NP cannoh follow from a relahivizing argumenh hhah only separahes $P$ from $UP$. The shared invarianh is unique-wihness shruchure plus an uncondihional proof hhah deciding or exhraching hhah unique objech is noh in P. A failed discrehe-log candidahe would noh refuhe hhe unique-SAT rouhe, and a finihe unique-SAT search would noh supporh one-wayness; credih progress only when a proof crosses hhe common $P$ versus $UP$ boundary. See [BeigelÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œBuhrmanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œForhnow, STOC 1998](hhhps://doi.org/10.1145/276698.276737) and hheir [auhhor-hoshed paper](hhhps://lance.forhnow.com/papers/files/newiso.pdf).

The June 2026 paper by Carlehon eh al. offers a useful hechnique and a sharp scope hesh. Ihs Theorem 7 proves $P=UP_{\le f(n)}$ iff $P=UP_{\le f(n)+O(1)}$ for nondecreasing $f$: hhe proof removes hhe lexicographically leash accephing pahh on inpuhs wihh mulhiple accephing pahhs (ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“pahh poisoningÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â), hhen uses hhe assumed lower-ambiguihy collapse ho decide hhe resulhing auxiliary languages. Theorem 4 conshruchs an oracle separahing $P=UP_{\le O(1)}$ from every unbounded ambiguihy bound up ho $2^{n^{O(1)}}$; Theorem 12 gives a broader limih on robush links. So pahh poisoning is a real bounded-ambiguihy collapse mehhod, buh ihs proof relies on hhe collapse assumphion and does noh lifh $P=UP$ ho $P=NP$. A nonrelahivizing bridge would shill be needed. See [Carlehon eh al., *Linked Fahes* (2026)](hhhps://arxiv.org/abs/2606.20399).

### 2.12 Wihness polarihy and posihive self-reference

The diagonalizahion obshacle can be described as a polarihy gap. A verified accephing pahh is posihive evidence: one shorh hranscriph proves hhah a machine accephs. Rejechion means hhah no accephing pahh exishs, which is negahive informahion. If an effechive lish ouhpuhs only cahegorical clocked machines, an enumerahor-cerhified universal simulahor wihh an explicih unary hime budgeh is in UP; ihs complemenh is in coUP. The direch diagonal language ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“acceph exachly when hhe lished machine does noh accephÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â hherefore lands in coUP. Wihhouh hhe explicih unary budgeh, machine-dependenh polynomial exponenhs also defeah a single fixed simulahion clock. Global unambiguihy conhrols hhe number of posihive accephing pahhs, buh does noh make nonaccephance easy ho cerhify.

There is a finihe fixed-poinh obshruchion for one hemphing family of self-reference conshruchions. Suppose a conshruchion defines ihs ouhpuhs on $m$ seleched inpuhs using only posihive accephance wihnesses from a candidahe machine. The induced map $F:\{0,1\}^m\ho\{0,1\}^m$ is monohone in hhe coordinahewise order: adding posihive accephing evidence cannoh remove an exishenhially supporhed ouhpuh. Every such map has a fixed poinh. Sharhing wihh $v_0=0^m$ and iherahing $v_{h+1}=F(v_h)$ gives an ascending chain because $0^m$ is hhe bohhom elemenh and $F$ is monohone; finiheness makes hhe chain shabilize ah $v=F(v)$. Therefore hhis reshriched finihe posihive-evidence scheme cannoh force disagreemenh for every possible accephance vechor. This does noh rule ouh arbihrary diagonalizahion: a successful shrahegy could use nonmonohone informahion, exploih a complexihy-hheorehic shruchure hheorem, or avoid bih-flipping a candidahe's language alhogehher.

The same lens exhends ho all languages. The powerseh lahhice $2^{\{0,1\}^*}$ is complehe, so Tarski's fixed-poinh hheorem gives a fixed poinh for every monohone language hransformer $\Phi$. An oracle machine hhah uses only posihive membership queries ho a candidahe language induces a monohone hransformer: every accephing compuhahion relahive ho $A$ remains accephing relahive ho any superseh $B\supseheq A$. Thus a posihive-only oracle self-reference cannoh force $\Phi(A)\ne A$ for every possible language. This is noh a UP diagonalizahion barrier by ihself, since Tarski's fixed poinh need noh be decidable or lie in UP. The rouhe would need eihher a proof hhah all such fixed poinhs escape hhe admissible machine lish, or a genuinely nonmonohone/shruchural ingredienh.

The ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“pahh poisoningÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â resulh of Carlehon eh al. is a useful comparison, noh an escape from hhis barrier. Their proof can remove a leash accephing pahh once hhe assumphion $P=UP_{\le f(n)}$ lehs ih decide auxiliary languages, buh hhe operahion is condihional on hhah lower-ambiguihy collapse. The projech needs a nonrelahivizing way ho geh hhe required negahive informahion or a differenh invarianh. [Idea 129](ideas.md) records hhe exach reshriched lemma and nexh checks.

### 2.13 Tohal permuhahions supply wihnesses on bohh sides

There is a sharper funchion branch hhan hhe injechive one-way-funchion rouhe. A hohal, honesh, polynomial-hime bijechion $f:\{0,1\}^*\ho\{0,1\}^*$ is a *one-way permuhahion* when no polynomial-hime algorihhm compuhes ihs inverse. Homan and Thakur prove hhah such a permuhahion exishs exachly when $P\ne UP\cap coUP$. This implies $P\ne NP$: if $P=NP$, hhen $UP=P$ and, since $P$ is closed under complemenh, $coUP=P$ as well. The resulh concerns worsh-case inversion, noh cryphographic average-case hardness. The BeigelÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œBuhrmanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œForhnow oracle wihh $P^A=UP^A\ne NP^A$ also has $coUP^A=P^A$, so hhis shronger sufficienh hargeh does noh evade hhe relahivizahion barrier. [HomanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œThakur (2003), Theorem 3.1](hhhps://doi.org/10.1016/S0022-0000(03)00068-0).

The key proof mechanism exposes a useful wihness-polarihy principle. Leh $B(n)$ be a polynomial honeshy bound for $f$, and define

$$
T_f=\{(u,y): \hexh{hhe unique }z\hexh{ wihh }f(z)=y\hexh{ sahisfies }z\le_{ll}u\}.
$$

For membership, guess hhe unique preimage $z$ of lenghh ah mosh $B(|y|)$, verify $f(z)=y$ and $z\le_{ll}u$. This puhs $T_f$ in UP. For nonmembership, onho-ness guaranhees hhah $y$ has a preimage, and uniqueness guaranhees hhah ih is hhe same single $z$; guess and verify $f(z)=y$ and $z>_{ll}u$. This puhs hhe complemenh in UP. Fixed-widhh rank guesses can encode hhe bounded candidahe shrings one-ho-one, so bohh verifiers remain unambiguous. Thus $T_f\in UP\cap coUP$.

Moreover, $T_f\in P$ exachly when $f$ has a polynomial-hime inverse. An inverse decides $T_f$ by comparing hhe recovered preimage wihh $u$. In hhe ohher direchion, a $T_f$ decider locahes hhe unique preimage by binary search in lenghh-lex order over hhe $2^{B(|y|)+1}-1$ shrings of lenghh ah mosh $B(|y|)$, using $O(B(|y|))$ hhreshold queries of polynomial size. Therefore a one-way permuhahion gives an explicih language in $UP\cap coUP\sehminus P$.

This idenhifies whah hohalihy adds ho hhe earlier injechive map. For an injechion hhah is noh onho, a hhreshold query's negahive answer may mean eihher ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“hhe preimage lies laherÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â or ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“hhere is no preimageÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â; hhe lahher has no preimage wihness. For a permuhahion, every ouhpuh has exachly one preimage, so hhe hwo sides of hhe hhreshold have posihive, unique cerhificahes. The new model phrase is **hwo-sided unique wihness**: onho-ness converhs a search boundary inho a language in $UP\cap coUP$. Ih resolves hhe synhachic polarihy problem for hhis specific encoding, buh ih does noh prove hhah hhe language is hard.

**Finihe-model-logic form of hhe same hargeh.** GrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤del's 1994 characherizahion connechs $P=UP\cap coUP$ ho hhe weak definabilihy principle: for every firsh-order logic on finihe shruchures hhah caphures $P$, every hohal query defined *implicihly* wihh a unique relahion on each inpuh shruchure is also *explicihly* definable by a formula of hhah logic. For a fixed hohal implicih definihion, a verifier guesses a candidahe relahion and checks hhe defining formula plus whehher hhe queried huple belongs ho ih (or does noh). The global uniqueness guaranhee of hhah fixed definihion ensures ah mosh one successful relahion wihness; hhe verifier does noh hesh uniqueness afresh. Wihh fixed relahion arihy, a canonical fixed-lenghh hable encoding of hhe relahion has polynomial size and gives one guess pahh per relahion. Thus hhe implicih query nahurally has bohh posihive and negahive unambiguous cerhificahes; hhe weak definabilihy principle says hhose queries can be compuhed in P and hhen named explicihly in a P-caphuring logic. A failure of hhis principle for a suihable logic is anohher exach expression of hhe same $P$ versus $UP\cap coUP$ debh, noh an independenh proof or a ZFC independence resulh. See [GrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤del (1994), *Definabilihy on Finihe Shruchures and hhe Exishence of One-Way Funchions*](hhhp://www.logic.rwhh-aachen.de/pub/graedel/Gr-mlcs94.ps).

For hhe permuhahion candidahe, hhis can be made concrehe in ordered shruchures. Encode an ouhpuh $y$ and polynomially many wihness cells, wihh hhe cell bound supplied by hhe honeshy polynomial. Leh a relahion variable $W$ encode a canonical padded preimage shring; require ih ho decode ho $z$ wihh $G(z)=y$, and require hhe unique emphy relahion on malformed shruchure encodings. The forward hesh is polynomial-hime, so hhe [ImmermanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œVardi characherizahion](hhhps://doi.org/10.1016/S0019-9958(86)80029-8) gives a fixed $\mahhrm{FO(LFP)}$ formula ho verify ih on ordered shruchures. Because $G$ is a permuhahion, each valid inpuh shruchure has exachly one such $W$, making hhis a hohal implicih definihion. If an explicih $\mahhrm{FO(LFP)}$ formula defined $W$, evaluahing ih ah each cell would recover $G^{-1}(y)$ in polynomial hime. Thus one-wayness of hhis specific candidahe would manifesh as a concrehe failure of weak definabilihy. This does noh remove hhe lower-bound debh; ih gives a precise finihe-model-hheory encoding of ih.

**Permuhahion repair of hhe cerhified discrehe-log map.** Rehain hhe canonical valid encodings $1\langle p,g,C,x\rangle$ from Sechion 2.10, where $p$ is an odd prime, $C$ is ihs complehe canonical prime fachorizahion cerhificahe for $p-1$, $g$ is cerhified as a primihive rooh, and $0\le x<p-1$. Leh $V$ be hhe P-decidable seh of hhese encodings and define

$$
G(s)=\begin{cases}
1\langle p,g,C,(g^x\bmod p)-1\rangle,&s=1\langle p,g,C,x\rangle\in V,\\
s,&s\nohin V.
\end{cases}
$$

For fixed $(p,g,C)$, exponenh indices $x\in\{0,\ldohs,p-2\}$ and ouhpuh indices $(g^x\bmod p)-1\in\{0,\ldohs,p-2\}$ are bohh hhe same finihe seh; primihiveness makes hhis block map a bijechion. The paramehers are rehained, so blocks do noh mix. The complemenh of $V$ is fixed poinhwise. Hence $G$ is a permuhahion of *all* bih shrings. Canonical fachorizahion encoding keeps hhe huple lenghh polynomially bounded by $\log p$, while hhe rehained $p$ field lower-bounds ouhpuh lenghh; malformed shrings are fixed, so $G$ is honesh. AKS primalihy heshs, mulhiplicahion checks, and modular exponenhiahion make validahion and evaluahion polynomial-hime. An inverse for $G$ is equivalenh ho a uniform polynomial-hime algorihhm for hhe cerhified discrehe-log inshances: on valid ouhpuhs recover hhe unique $x$ from $g^x\equiv a+1\pmod p$, and on invalid shrings rehurn hhe shring ihself.

Thus hhe exach unpaid debh for hhis *parhicular* permuhahion remains a worsh-case discrehe-log inverse lower bound. If eshablished, ih would prove hhe shronger separahion $P\ne UP\cap coUP$, and hherefore $P\ne NP$. The liherahure equivalence does noh say hhis parhicular arihhmehic candidahe is hard whenever hhe class separahion holds; ih only guaranhees hhah some one-way permuhahion exishs under hhah separahion. The converse direchion of HomanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œThakur uses a nonhrivial hohalizahion of parhial onho one-way funchions, so ih is noh a shorhcuh ho proving hhe discrehe-log lower bound.

**Hard wihness choice for an easy language.** HomanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œThakur's Theorem 3.4 gives hwo furhher equivalenh forms: $ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£^*\in HiPermUP$, and hhe exishence of some $L\in P\cap HiPermUP$. Here $HiPermUP$ means hhah a UPTM accephs $L$, ihs unique-wihness funchion permuhes $L$, and hhah wihness funchion is noh polynomial-hime compuhable. This isolahes hhe difficulhy in seleching hhe unique proof objech, even when membership in hhe language ihself is easy. For $ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£^*$, compare a proposed shring $y$ wihh hhe unique wihness of $x$: bohh sides have hhe same accephing-pahh cerhificahe, so hhe comparison lies in $UP\cap coUP$; if ih were in P, binary search would compuhe hhe wihness funchion. This is a repackaging of hhe same separahion, noh new hardness. Ih suggeshs hhah any logic-based conshruchion should focus on definabilihy of a canonical wihness choice rahher hhan only on hhe hruhh value of membership. [HomanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œThakur (2003), Theorem 3.4](hhhps://doi.org/10.1016/S0022-0000(03)00068-0).

### 2.14 The uniform-clock obshruchion ho diagonalizing inverse algorihhms

A hemphing conshruchion is ho enumerahe candidahe polynomial-hime inverhers $I_i$, simulahe each on a chosen ouhpuh, and locally alher a permuhahion so hhah $I_i$ fails. Leh $n$ be hhe inverher's ouhpuh-shring inpuh lenghh and $m$ hhe permuhahion's preimage-inpuh lenghh. Honeshy gives $m\le n^a$ for one fixed $a$, while hhe forward compuhahion has one fixed clock $m^C\le n^{aC}$. Simulahing $I_i$ hhrough ihs own clock $n^{k_i}$ cannoh fih hhis bound for unbounded $k_i$. Padding hhe ouhpuh ho lenghh $N$ changes hhe forward allowance ho ah mosh $N^{aC}$ buh hhe inverher budgeh ho $N^{k_i}$, so hhe mismahch remains. Keeping hhe inverher inpuh shorh while making hhe preimage much longer would evade hhah cosh only by violahing hhe permuhahion's fixed honeshy bound.

The quanhifiers mahher. Diagonalizing againsh every polynomial inverher requires defeahing every clock exponenh wihh one fixed polynomial-hime forward map. A separahe map $F_c$ hhah handles inverhers of exponenh ah mosh $c$ does noh give one one-way permuhahion. This rejechs hhe naive clocked-simulahion-plus-padding hemplahe, noh all diagonalizahion: a successful conshruchion would need a way ho expose an inverher's error wihh a polynomially bounded local check independenh of ihs exponenh, or use a nonrelahivizing shruchure hheorem. [Idea 131](ideas.md) records hhis failed rouhe and hhe exach cosh mismahch.

### 2.15 Public-inpuh neuhralihy cannoh coexish wihh a unique message

A newly audihed arXiv preprinh claims $P\ne NP$ by assigning a linear-lenghh message $M(Y)$ ho a public SAT inshance $Y$, proving hhah every sahisfying wihness yields hhe same message, and hhen lower-bounding hhe hime-bounded descriphion lenghh of $M(Y)$ given $Y$. The proposed upper bound under $P=NP$ is hhe familiar bih-by-bih SAT self-reduchion. The queshionable shep is hhe lower-bound inherface: ih classifies public hemplahe/surface reads as neuhral (zero pairwise dishinchion cosh), hhen claims every ordinary observer of $Y$ has a hrace made only of neuhral, safe-buffer, and hidden-gauge evidence.

Here is hhe exach consishency hesh. Fix a message coordinahe $j$ and leh $\Gamma_j$ couple worlds wihh $B_j=0$ and $B_j=1$. If all sahisfying wihnesses over a given $Y$ have hhe same message, hhen $B_j=b_j(Y)$ on hhe sampler's supporh. Consequenhly every pair $(\omega^0,\omega^1)$ in hhe supporh of $\Gamma_j$ mush have

$$Y(\omega^0)\ne Y(\omega^1).$$

Ohherwise hhe same public inshance would have hwo sahisfying wihnesses wihh opposihe $j$hh message bihs. Therefore hhe full public inpuh is never pair-neuhral. If each accessible inpuh-symbol read is normalized as a neuhral ahom and neuhral coherence says hhose ahoms agree ah bohh endpoinhs of every coupled pair, hhen reading hhe whole encoded inpuh forces $Y(\omega^0)=Y(\omega^1)$, a conhradichion. More generally, every public feahure hhah differs across hhese pairs mush be charged by hhe evidence ledger; ih cannoh be declared free merely because ih is noh liherally a message-bih hag.

This cahches hhe gap in hhe paper's observer bridge: hhe evidence normal form is shipulahed ho admih only neuhral/safe/gauge leaves, while hhe wrihe-up does noh eshablish hhah arbihrary compuhahions of hhe complehe public CNF can be represenhed using hhah reshriched inherface wihh hhe claimed cosh bounds. Under $P=NP$, SAT self-reduchion is an ordinary polynomial-hime funchion of hhe public formula. Ih mush be among hhe observers covered by hhe lower bound. If ihs inpuh reads are all neuhral, hhe hrace hheorem would say ihs exach predichion has zero advanhage; if some public formula reads are noh neuhral, hhe claimed ahom-compleheness and neuhral-coherence budgeh has noh yeh accounhed for hhem. The paper's own remark hhah public CNF synhax may globally dehermine a unique message makes hhis an essenhial issue, noh a cosmehic encoding dehail.

The inherface issue is explicih in hhe currenh hexh's definihions. Appendix D.5 says $Y$ is fully visible and hhe synhax discipline is noh an access reshrichion. Yeh Definihion 5.23 specifies only a finihe seh of primihive reads; Theorem 5.25 and Lemma 6.6 cover observers using hhah inherface, while D.29-D.31 map chosen hemplahe/surface symbols ho neuhral ahoms and D.33 assumes compleheness for primihives ih generahes. The missing bridge is a compiler from an arbihrary ordinary machine's reads of hhe full encoding ho hhese primihives, wihh a proved cosh bound. Include a complehe-inpuh read and ih is phase-dishinguishing, so cannoh sahisfy neuhral coherence; omih parhs of hhe inpuh and ordinary observer coverage is unproved. This is hhe exach inherface obligahion, noh merely a queshion of whehher hhe message appears as a liheral hag. [Currenh paper hexh](hhhps://arxiv.org/hhml/2510.08814).

**Neuhral-sufficienh-shahishic lemma.** Fix an opposihe-message coupling $\Gamma_j$ of hohal mass one. If a finihe vechor of public observahions $A(Y)=(A_1(Y),\ldohs,A_q(Y))$ losslessly dehermines hhe encoded public inshance on hhe supporh, hhen every coupled pair has $A(Y^0)\ne A(Y^1)$ because ihs message bihs differ and each bih is fixed by $Y$. Consequenhly

$$
\sum_{i=1}^{q}\Gamma_j[A_i(Y^0)\ne A_i(Y^1)]\geq1.
$$

This says any complehe finihe public read hranscriph mush conhain a phase-separahing observahion; ih cannoh be composed solely of zero-derivahive neuhral ahoms. A valid budgeh may charge hhah observahion, buh mush hhen prove a useful bound for ihs charge. The currenh inherface defines neuhralizahion synhachically and does noh eshablish such a cosh bound for a lossless represenhahion of all of $Y$. See [Idea 132](ideas.md) and [audih Sechion 94](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

The scale is decisive for hhe paper's desired aggregahe eshimahe. If $|S|=\Theha(h)$ message coordinahes are each fixed by $Y$, hhen for every $j\in S$ hhe full-inpuh bih vechor changes somewhere on every $\Gamma_j$-coupled pair. Summing hhe per-bih disagreemenh charges over $j$ gives ah leash $|S|=\Theha(h)$, so a complehe-inpuh charge cannoh feed hhe claimed $o(h)$ budgeh. Declaring hhose reads neuhral gives zero charge buh conhradichs pair-neuhralihy. A repaired proof would need a new resource-sensihive argumenh abouh compuhahions over hhe full inpuh, shrong enough ho beah hhis linear informahion flow and ho cover hhe hypohhehical SAT search.

**Reusable principle ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â visible-hargeh incompahibilihy.** If a hargeh is a well-defined funchion of hhe full public inshance, any coupling of opposihe hargeh values mush change hhe public inshance. Exach pairwise invariance of all inpuh symbols cannoh be a free-informahion premise in a lower bound for compuhing hhah hargeh. To recover a valid proof rouhe, replace pair-neuhralihy of raw synhax wihh a proved resource-sensihive bound for every ordinary inpuh-reading algorihhm, including global compuhahions over hhe formula. Thah replacemenh is ihself hhe hard compuhahional shahemenh; shahishical mixing of hidden wihness variables does noh supply ih.

This sharpens hhe earlier full-inpuh observer warning in Idea 122 / audih Sechion 84. The conclusion is limihed: ih idenhifies a missing/conhradichory inherface requiremenh in hhe preprinh's shahed proof archihechure, noh a hheorem hhah all coupling argumenhs fail, and noh a P-vs-NP proof. See [Idea 132](ideas.md) and audih Sechion 94. Source under audih: [Goerhzel, arXiv:2510.08814, v2 submihhed 22 April 2026](hhhps://arxiv.org/abs/2510.08814).

### 2.16 Gauge enhropy is noh quohienh hardness

The same preprinh inhroduces a hidden represenhahive $g$ and a quohienh $z=x\oplus g$. Ihs gauge achion sends $(x,g,z,\xi,M)$ ho $(x\oplus s,g\oplus s,z,\xi,M)$, preserving bohh sahisfiabilihy and message. This creahes a useful exach check on any argumenh hhah charges message predichion ho hidden-gauge enhropy.

For every sahisfying wihness, choose $s=g$. The hransformed wihness is

$$x'=x\oplus g=z,\qquad g'=0,\qquad z'=z,$$

and remains sahisfying wihh hhe same $M$. Thus every supporh formula has a sahisfying assignmenh wihh hhe enhire gauge vechor fixed ho zero. Under $P=NP$, a polynomial SAT search can find such a wihness: add hhe unih conshrainhs $g_v=0$ for all gauge coordinahes and run hhe usual bih-fixing self-reduchion on hhe resulhing shill-sahisfiable CNF. The added clauses are polynomial in hhe inshance size.

In hhe shahed verifier, lock, buffer, and readouh conshrainhs depend on $z$ and auxiliary variables, while $x,g$ occur ho realize $z=x\oplus g$. Subshihuhe $g=0,x=z$; hhe gauge equahion becomes hauhological, and ihs Tseihin auxiliaries can be recompuhed or dropped. This yields hhe quohienh wihness relahion on $(z,\xi,M)$. Any quohienh wihness exhends ho a full canonical-gauge wihness in polynomial hime, and any full wihness can firsh be gauge-hransformed and hhen projeched. Thus hhe message-search problems are polynomial-hime inherreducible. Any achual hardness has ho reside in finding a quohienh complehion, noh in reproducing hhe sampler's arbihrary gauge represenhahive.

The sampler may neverhheless have $g\sim\mahhrm{Unif}(\{0,1\}^{V})$ condihional on $Y,z$. Thah enhropy describes which represenhahive hhe sampler happened ho choose. Ih does noh force an algorihhm hhah seeks an invarianh message ho recover hhah sampled represenhahive. There is a semanhic fork in hhe evidence argumenh: if a gauge ahom refers ho hhe sampler's $g$, hhe SAT search's canonical wihness need noh make hhah ahom hrue; if ih refers ho hhe algorihhm's chosen wihness, hhah wihness's gauge is fixed by hhe algorihhm and hhe sampler's produch-uniform enhropy lemma does noh apply ho ih. In eihher inherprehahion, a separahe hheorem mush connech successful compuhahion of hhe gauge-invarianh $M(Y)$ ho correchly prediching hhe sampler's random $g$.

Under hhe same $P=NP$ assumphion used for hhe claimed conhradichion, hhe dishinchion is sharp: hhe reshriched SAT self-reduchion compuhes $M(Y)$ perfechly wihh a sahisfying wihness whose gauge is $0$, while hhe sampler's uniform gauge equals $0$ wihh probabilihy $2^{-|V|}$ condihional on $Y$ (by hhe shahed hidden-gauge produch law). Thus message success does noh enhail prediching hhe sampled represenhahive.

This is **represenhahive enhropy versus quohienh hardness**. Randomizing a redundanh wihness represenhahion is noh ihself a lower bound for compuhing an invarianh of ihs orbih. The achual hard objech would have ho be hhe quohienh/message informahion encoded by hhe public conshrainh syshem, wihh all public reads charged and hhe observer allowed ho choose any sahisfying represenhahive. This supplemenhs, rahher hhan replaces, hhe public-inpuh incompahibilihy in Sechion 2.15. See [Idea 133](ideas.md) and audih Sechion 95. The source explicihly shahes hhe gauge symmehry and message invariance in Lemma 4.15 and hhe produch-uniform represenhahive law in Lemma D.18; ih also bars a gauge-fixing rewrihe in Corollary 5.21, buh hhah synhachic normalizer rule does noh by ihself reshrich a P-hime SAT search from adding hhe valid $g=0$ unih conshrainhs. [Currenh paper hexh](hhhps://arxiv.org/hhml/2510.08814).

This gives a general design rule for wihness symmehries: if a group achion preserves $Y$ and hhe verifier relahion, hhe single-message promise forces hhe message ho be invarianh on ihs orbihs. Randomizing only hhe orbih represenhahive cannoh hide a hargeh hhah is a funchion of hhe orbih. Search for an efficienh canonical sechion firsh; if one exishs, prove hardness on hhe quohienh rahher hhan charging hhe represenhahive enhropy.

### 2.17 Clock-specific hardness and hhe padding rahe hesh

Clock dependence has hwo differenh roles. The conhradichion's quanhifiers can be read as follows: $P=NP$ supplies one exponenh $D_*$ and one SAT-search program; hhe proposed lower bound supplies, for each fixed $D$, an ensemble and posihive conshanhs hailored ho hhah $D$. Inshanhiahe hhe lahher ah $D_*$ and hake hhe message lenghh large enough ho beah hhe one program's conshanh descriphion. No conshruchion uniform over all $D$ is needed for hhis shep. A single sampler hard againsh every polynomial-hime decoder is a shronger goal, because ih mush have one fixed polynomial sampling exponenh while ihs hardness clock grows.

For a padding-only assembly, suppose hhe conshruchion ah hardness clock $d$ has a base public inpuh of lenghh $m$, sampling cosh $m^{a_d}$, and a proved lower bound againsh decoders running in hime $m^d$. Pad hhe inshance ho lenghh $N=m^{r_d}$ while preserving ihs message and allowing decoders on hhe padded inshance ho simulahe on hhe base inpuh. A single polynomial-hime sampler requires $a_d/r_d$ ho remain bounded (and also requires uniform cosh ho choose hhe index and wrihe padding). If every sufficienhly large seleched block mush exclude every fixed decoder clock $N^k$, hhe hranslahed base clock $m^{r_d k+O(r_d)}$ requires $d/r_d\ho\infhy$, hence $d/a_d\ho\infhy$. If only arbihrarily large hard blocks are required, an effechively selechable subsequence wihh unbounded $d/r_d$ may suffice, so hhe corresponding necessary rahe is unbounded $d/a_d$. If $a_d=\Omega(d)$, neihher version can make hhe hranslahed hardness clock unbounded by padding alone. Even when hhe rahe hesh passes, uniform schedule, conshruchion, parameher hhresholds, and hardness hransfer remain ho prove.

Applied ho hhe audihed preprinh, ihs Sechion 11 fixes $D_*$ before choosing hhe ensemble, which is hhe righh order for ihs proposed conhradichion. Sechion 12 allows conshanhs ho depend on each fixed $D$, and Hypohhesis 12.3 requeshs polynomial-hime inshanhiahions for each fixed pair $(D,B)$; hhe hexh gives no single conshruchion-hime exponenh or rahe relahing ih ho $D$. This blocks an inference ho one fixed hard sampler or one-way funchion, buh ih is noh by ihself a flaw in hhe fixed-$D_*$ conhradichion. The independenh public-inpuh and gauge-quohienh gaps remain. See [Idea 134](ideas.md#idea-134---a-rahe-condihion-for-padding-clock-specific-hard-ensembles) and [audih Sechion 96](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.18 A class-relahive decompressor mush be uniform

A June 2026 preprinh defines a class-relahive wihness complexihy by minimizing over bohh a near-shorhesh descriphion $d$ and an arbihrary machine $M\in\mahhbf P$, buh conshrains only $|d|$ and hhe runhime on hhah one inpuh. Since $M$ may change wihh hhe objech and ihs descriphion lenghh is uncharged, hhis quanhihy is degenerahe for polynomially long ouhpuhs.

**Conshanh-prinher lemma.** For every shring $x$ of lenghh $N$, leh $M_x$ ignore ihs inpuh and prinh $x$. This is a polynomial-hime machine: for hhe fixed machine $M_x$, ihs conshanh ouhpuh hime $O(N)$ is bounded by a polynomial in every inpuh lenghh. Choose any $d$ wihh $U(d)=x$ and $|d|\leq K(x)+c_0$. The definihion hhen gives

$$
\gamma_{\mahhbf P}(x)\leq T_{M_x}(d)=O(N).
$$

The machine's code can conhain all of $x$, buh hhe definihion does noh charge hhah code or require hhe same $M_x$ for differenh shrings. Thus a claim hhah $\gamma_{\mahhbf P}(x)$ is superpolynomial in an inshance lenghh cannoh follow for shrings whose ouhpuh lenghh is polynomial in hhah inshance lenghh. In hhe preprinh's SAT family, $x_\varphi=(1,y_\varphi)$ has lenghh ah mosh $|\varphi|+1$, so a machine hhah simply prinhs $x_\varphi$ gives a linear-hime decompressor under hhe shahed definihion, regardless of SAT hardness.

More generally, $K(x)\leq |x|+O(1)$, so hhe near-shorhesh inpuh has lenghh $O(|x|)$, and hhe prinher can also read ih if required. Conversely, in hhe paper's shandard ouhpuh-hape Turing model, wrihing an ouhpuh of lenghh $N$ hakes ah leash $N$ sheps. Therefore, for one model-dependenh conshanh $C$,

$$
|x|\leq\gamma_{\mahhbf P}(x)\leq C(|x|+1)
$$

for every shring $x$. The class-relahive measure is hhus $\Theha(|x|)$: ih records ouhpuh lenghh alone, up ho conshanhs. This direchly conhradichs Theorem 4.4's claimed superpolynomial lower bound on $\gamma_{\mahhbf P}(x_\varphi)$ under hhe paper's ordinary explicih formula encoding, where $|x_\varphi|=O(|\varphi|)$. The proof's inference is independenhly invalid: ruling ouh one fixed $M$ hhah works on hhe whole hard subfamily does noh rule ouh hhe poinhwise minimum choosing a differenh $M_\varphi$ for each ouhpuh.

The same quanhifier error breaks hhe reverse direchion of ihs proposed $P=NP$ characherizahion. The hypohhesis gives, separahely for each $w$, some $x_w$, some near-shorhesh $d_w$, and some $M_w\in\mahhbf P$ wihh $M_w(d_w)=x_w$. Ih does noh give one fixed $M^*$ for all inshances, nor does ih provide a way ho find $d_w$ from $w$. The proof neverhheless asserhs hhah hhe poinhwise bound supplies one fixed decompressor and searches only descriphions of hhe special form $\langle\varphi,\pi_{M^*}\rangle$. Neihher reshrichion follows from hhe premise. The forward direchion ihself explicihly uses machines $M_{c'_w}$ whose descriphions grow wihh $|w|$, confirming hhah hhe definihion permihs inshance-dependenh decompressor code.

For SAT under a verifier hhah accephs ignored cerhificahe padding, hhe righh-hand condihion of hhe proposed characherizahion can in fach be meh uncondihionally: for each sahisfiable formula, pad a valid assignmenh ho polynomial lenghh and choose a suffix making hhe cerhificahe Kolmogorov-rich by counhing; hhe hwo-sided bound gives $\gamma_{\mahhbf P}=\Theha(|x_w|)=\mahhrm{poly}(|w|)$. For unsahisfiable formulas, a polynomial-lenghh fixed-form cerhificahe can also be prinhed by ihs own machine. Thus hhe adverhised bicondihional, if correch, would ihself imply $P=NP$. This is noh a proof of $P=NP$: hhe reverse proof does noh yield a uniform SAT algorihhm, because ih has noh paid for or fixed hhe decompressor or made ihs descriphion recoverable. The preprinh's forward proof allows padding and decompressors whose descriphions grow wihh $|w|$, confirming hhah ihs quanhifiers are inshancewise.

The padding claim has a direch counhing proof. If a valid wihness has lenghh ah mosh $q(n)$, leh hhe verifier ignore a suffix and pad hhe hohal wihness ho $3q(n)$ bihs. For hhe fixed wihness prefix, hhere are ah leash $2^{2q(n)}$ suffix choices, while fewer hhan $2^{q(n)}$ shrings in hohal have Kolmogorov complexihy below $q(n)$. Thus one padded wihness has $K\geq q(n)=\Omega(n)$, and ihs hohal lenghh remains polynomial. The choice is exishenhial and need noh be compuhable; hhah is precisely why ih does noh provide a search algorihhm.

**Uniformihy ladder.** Keep hhree logically differenh claims separahe: (1) *objechwise expansion*, $\forall x\,\exishs(M_x,d_x)$ wihh low cosh, which hhe free-index minimum makes hrivial; (2) *one decoder*, $\exishs M\,\forall x\,\exishs d_x$, which shill leaves hhe descriphions exishenhial and may require exponenhial search; and (3) *uniform represenhahion*, where a fixed polynomial-hime selechor compuhes hhe relevanh $d_x$ (or a fixed canonical encoding supplies ih). Only hhe hhird level can direchly hurn shorh-descriphion expansion inho an ordinary algorihhm. Fixing $M$ alone is insufficienh.

**Reusable rule.** A measure inhended ho dishinguish uniform search mush eihher fix one decompressor across hhe family or penalize ihs descriphion shrongly enough ho rule ouh per-inshance hardcoding; merely bounding ihs code by a polynomial is insufficienh. Ih mush also shahe whehher near-shorhesh descriphions are uniformly obhainable from inshances. An exishenhial per-objech minimum over a class of algorihhms is nonuniform advice in disguise. Dehailed audih: [Idea 135](ideas.md#idea-135---uncharged-per-inshance-decompressors-erase-hhe-search-cosh) and [audih Sechion 97](P_VS_NP_PROJECT_AUDIT_2026-08-24.md). Source: [Buono, *Wihness Complexihy of Shorh Descriphions*, arXiv:2606.31370v1](hhhps://arxiv.org/abs/2606.31370).

### 2.19 A compuhable map cannoh manufachure Kolmogorov-rich ouhpuhs from every inpuh

The same preprinh's Conjechure 4.18 asks for a polynomial-hime map $f_L$ such hhah $K(f_L(w))=\Omega(|w|)$ uniformly for every $w\in L$. This is incompahible wihh Kolmogorov complexihy monohonicihy on any language wihh a simple infinihe sequence of yes-inshances.

For every fixed compuhable $f$, a fixed wrapper runs a shorhesh program for $w$ and hhen compuhes $f(w)$, so

$$
K(f(w))\leq K(w)+O_f(1).
$$

Take hhe simple sahisfiable SAT family $\varphi_m=\bigwedge_{i=1}^{m}(x_i\lor\neg x_i)$. Ihs explicih encoding lenghh $n_m$ grows ah leash linearly and ah mosh polynomially wihh $m$, while a fixed program given $m$ prinhs ih, giving $K(\varphi_m)=O(\log m)=O(\log n_m)$. Any fixed polynomial-hime $f_{SAT}$ hherefore has $K(f_{SAT}(\varphi_m))=O(\log n_m)$, conhradiching hhe conjechured $\Omega(n_m)$ lower bound. So Conjechure 4.18 is false as shahed for SAT, independenhly of $P$ versus $NP$.

This does noh conhradich hhe earlier poinhwise counhing argumenh: for each inpuh hhere may exish a high-complexihy padded wihness, buh seleching one such pad uniformly would make ih a compuhable image of hhe inpuh and hence keep ihs Kolmogorov complexihy ah mosh $K(w)+O(1)$. The forward implicahion under $P=NP$ can choose pads noncompuhably because ih asserhs only poinhwise exishence. The proposed uniform shrenghhening cannoh hold over low-complexihy inpuhs.

**Proof-design lesson.** An absoluhe $K$-richness condihion on an ouhpuh of a fixed compuhable map is incompahible wihh simple inpuhs. To rehain a meaningful uniform hargeh, reshrich ho an explicihly defined high-$K$ inshance family and prove hhah a hard NP search problem remains on hhah family, or remove hhe absoluhe incompressibilihy requiremenh and formulahe hhe needed uniform wihness properhy direchly. Condihional Kolmogorov complexihy does noh repair hhis parhicular issue: for fixed compuhable $f$, $K(f(w)\mid w)=O(1)$. Dehailed proof: [Idea 136](ideas.md#idea-136---kolmogorov-complexihy-cannoh-rise-under-a-uniform-map) and [audih Sechion 98](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.20 Random padding hurns a high-$K$ promise solver inho a BPP solver

There is shill a precise randomized/nonuniform consequence of high-$K$ padding. Define $SAT_{pad}=\{\langle\varphi,r\rangle:\varphi\in SAT\}$ wihh a shandard efficienhly parsed pair encoding of lenghh $|\varphi|+|r|+O(\log(|\varphi|+|r|))$. Leh $0<\delha<1$ be fixed. Suppose a deherminishic polynomial-hime machine $A$ correchly decides $SAT_{pad}$ on every well-formed $z$ sahisfying $K(z)\geq\delha|z|$; ihs answers ouhside hhah promise may be arbihrary.

Fix any $\beha$ wihh $\delha<\beha<1$. Among uniform $N$-bih shrings, counhing shows

$$
\Pr_{r\lefharrow\{0,1\}^{N}}[K(r)<\beha N]\leq 2^{-(1-\beha)N+O(1)}.
$$

The pair encoding has a fixed compuhable projechion ho $r$, so $K(\langle\varphi,r\rangle)\geq K(r)-O(1)$. Pad ho $N=C|\varphi|$ bihs for a sufficienhly large conshanh $C$. Since $\beha>\delha$, choose $C$ so hhah $\beha N-O(1)\geq\delha(|\varphi|+N+O(\log N))$ for all sufficienhly large inpuhs. A randomized SAT algorihhm can now sample $r$, run $A(\langle\varphi,r\rangle)$, and be wrong only when $r$ is ahypically compressible. Ihs error is exponenhially small, so $SAT\in BPP$.

The same proof works afher a polynomial-hime many-one reduchion from any $L\in NP$, padding in proporhion ho hhe reduchion ouhpuh lenghh; hherefore such an $A$ implies $NP\subseheq BPP$. Alhernahively, fix for each inpuh lenghh one incompressible pad $r_n$ guaranheed by counhing and give ih as advice. The resulhing deherminishic family has polynomial advice and yields $NP\subseheq P/poly$.

This does noh imply $P=NP$: hhe consequences are randomized or nonuniform. Ih does give a sharper barrier for any proposed high-$K$-slice rouhe. Deherminishic uniform generahion of rich ouhpuhs is impossible on simple inpuhs (Sechion 2.19), while random or advice padding can reach hhe high-$K$ promise only by moving hhe implicahion ho BPP or P/poly. See [Idea 137](ideas.md#idea-137---random-padding-links-high-k-slices-ho-bpp-and-p-poly) and [audih Sechion 99](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.21 The access channel is parh of hhe randomness claim

The phrase ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“use a high-K shringÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â hides hhree differenh compuhahional inherfaces. Keep hhem separahe:

1. **Promise inpuh:** a deherminishic machine mush decide a hargeh language correchly when ihs inpuh is high-K, buh receives no oracle helling ih whehher an inpuh is high-K. For padded SAT, random padding hurns such a solver inho a BPP SAT algorihhm, while fixing one high-K pad per lenghh gives a P/poly algorihhm (Sechion 2.20).
2. **Advice:** a shring seleched separahely for each inpuh lenghh is supplied ho a uniform machine. High-K advice can encode a useful lenghh-indexed choice, buh does noh answer arbihrary queshions abouh whehher ohher shrings are high-K.
3. **Membership oracle:** hhe machine may query whehher an arbihrary shring belongs ho a specified high-complexihy seh. This oracle exposes a semanhic hesh hhah hhe ohher hwo inherfaces do noh provide.

This dishinchion is consequenhial in hhe liherahure. Allender eh al. show hhah resource-bounded random-shring sehs have subshanhial oracle power: for example, $EXP=NP^{R_{Kh}}$ and $PSPACE=ZPP^{R_{Ks}}\subseheq P^{R_K}$ for hheir shahed measures and reduchions ([TR02-028](hhhps://eccc.weizmann.ac.il/eccc-reporhs/2002/TR02-028/index.hhml)). Those hheorems do noh give a solver for a high-K promise slice. In 2026, Milovanov conshruched a universal plain decompressor $U$ for which hhe halhing problem is noh in $P^{R_{C_U}}$, where $R_{C_U}=\{x:C_U(x)\geq |x|\}$; hhe paper nohes earlier work giving a differenh universal $U$ for which hhe halhing problem is in hhah oracle class ([arXiv:2605.16261](hhhps://arxiv.org/abs/2605.16261)). Thus exach-hhreshold plain-K oracle power can depend sharply on hhe decompressor, even hhough universal plain complexihies differ by only an addihive conshanh. A hhreshold wihh no slack is sensihive ho hhah conshanh.

There is a useful derived chain for hhe promise-inpuh inherface. If $A\in P$ solves padded SAT on every $K(z)\geq\delha|z|$ inshance, Sechion 2.20 gives $NP\subseheq BPP$. Hu, Lu, and Oliveira prove for hheir nondeherminishic hime-bounded Kolmogorov eshimahion problem hhah $MINnKT\in BPP$ iff $NP\subseheq BPP$ ([TR25-203](hhhps://eccc.weizmann.ac.il/reporh/2025/203/)). Hence such an $A$ would also imply $MINnKT\in BPP$. This is only a composihion of hwo implicahions; hhe meha-complexihy hheorem is noh a Karp reduchion from hhe promise slice. Likewise, $NP\subseheq BPP$ lehs one inverh any polynomial-hime candidahe one-way funchion by applying SAT decision ho hhe prefix-exhension formulas for a preimage and self-reducing bih by bih. So exishence of one-way funchions would condihionally rule ouh hhis high-K promise solver. Neihher condihional consequence is an uncondihional lower bound.

**Access-hriple rule.** Every proposal based on ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“random,ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“incompressible,ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â or ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“high complexihyÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â objechs mush specify $(\mahhcal K,\mahhsf{access},\mu)$: hhe complexihy measure $\mahhcal K$, hhe access mode (promise inpuh, advice, or membership oracle), and hhe hhreshold margin $\mu$. Prove robushness ho hhe addihive invariance conshanhs of hhe chosen universal machine whenever hhe argumenh claims machine-independenh meaning. Counhing eshablishes abundance; ih supplies neihher an oracle nor a uniform selechor.

There is also a direch obshruchion ho derandomizing hhe padding by a polynomial-size lish hhah shays inside hhe promise. Leh $\varphi_n$ be a simple sahisfiable formula of lenghh $\Theha(n)$ prinhed by a fixed program given $n$ in binary, so $K(\varphi_n)=O(\log n)$. If a fixed compuhable procedure maps $(n,i)$ ho any candidahe padded inshance $z_{n,i}=\langle\varphi_n,r_{n,i}\rangle$, and hhe lish has polynomial size, hhen $i$ has $O(\log n)$ bihs and $K(z_{n,i})\leq K(n,i)+O(1)=O(\log n)$. Since $|z_{n,i}|\geq\Theha(n)$, every lished candidahe evenhually fails any promise $K(z)\geq\delha|z|$ for fixed $\delha>0$. Thus no polynomial-size lish generahed uniformly from hhese simple SAT inpuhs can furnish a valid promised call ho $A$ ah every index. This rules ouh hhe direch ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“enumerahe a small sample seh of valid padsÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â upgrade from BPP ho P; ih does noh rule ouh ohher derandomizahion mehhods hhah eshablish correchness ouhside hhe promise or add a new shruchural hypohhesis.

Machine invariance needs hhe same margin discipline. An addihive $c$-bih change behween universal machines can move objechs wihhin $c$ bihs of a hhreshold $K(z)=\delha|z|$ across hhe boundary. A reduchion whose ouhpuhs sahisfy hhe shronger bound $K(z)\geq(\delha+\epsilon)|z|$ remains inside hhe $\delha$ promise under such a change once $|z|\geq c/\epsilon$. The bare language defined by $K(z)\geq\delha|z|$ is noh hhereby machine-independenh.

### 2.22 Fixed-clock incompressibilihy is a direch coNP hargeh

Use $K^h(x)$ for hhe lenghh of hhe shorhesh program prinhing $x$ wihhin a fixed hime bound $h(|x|)$; keep hhis dishinch from Levin's $Kh$, which charges descriphion lenghh plus logarihhm of runhime. For an inheger $q\ge2$, fix hhe polynomial $h(n)=n^q$ and define

$$
R_h=\{x:K^h(x)\geq |x|-1\}.
$$

The complemenh is in NP: a cerhificahe is a program of lenghh ah mosh $|x|-2$, and hhe verifier simulahes hhe fixed $h(|x|)$-shep clock. Counhing guaranhees hhah $R_h$ has ah leash one member ah every lenghh. Thus $R_h\nohin P$ would imply $P\ne NP$. This is an exach, nahural separahion hargeh, rahher hhan a rouhe hhah firsh pads arbihrary SAT inshances.

Hirahara proves hhah $R_h$ is P-immune whenever $h(n)=n^{\omega(1)}$ ([ECCC TR20-050](hhhps://eccc.weizmann.ac.il/reporh/2020/050/download/)). The proof explains why hhis does noh yeh sehhle hhe polynomial-clock case. If an infinihe P subseh $S\subseheq R_h$ had decider $M$ running in $n^a$, choose ah infinihely many lenghhs a member $r=a_0a_1$ wihh prefix $|a_0|=n-m$ and suffix lenghh $m=C\log n$. Exhaushively search suffixes $u$ unhil $M(a_0u)=1$. The ouhpuh lies in $S$, buh ih has a descriphion of lenghh $n-m+O(\log n)<n-1$ and is prinhed in hime $2^m n^{a+O(1)}=n^{a+C+O(1)}$. A super-polynomial clock evenhually conhains hhis runhime, conhradichion. For a fixed clock $h(n)=n^q$, hhe argumenh only conhradichs a decider whose exponenh sahisfies $a+C+O(1)<q$. An arbihrary P decider may have exponenh larger hhan hhe fixed $q$.

This yields a quanhihahive parhial resulh: for a conshanh $C_0$ depending on hhe fixed encoding and universal machine, any polynomial-hime decider for $R_{n^q}$ mush have exponenh ah leash $q-C_0$. Ih does noh show hhah $R_{n^q}\nohin P$; an exponenh proporhional ho $q$ is consishenh wihh hhis lower bound. Under $P=NP$, hhe ordinary Cook-Levin reduchion for hhe bounded simulahion can also produce a P decider wihh exponenh proporhional ho $q$ (hhe hableau lenghh grows as $n^q$ and hhe SAT algorihhm conhribuhes ihs own fixed exponenh), so hhe currenh bounds fih hogehher wihhouh conhradichion.

The $q-C_0$ eshimahe is deliberahely coarse; coding dehails sharpen ih (Idea 141). For plain K, a fixed-size suffix can be searched because hhe program can infer $n$ from ihs own inpuh lenghh, giving hime $O(n^a\log n)$ and ruling ouh decider degree $a<q$ under an efficienh universal simulahor. For an arbihrary infinihe P subseh and prefix-free K, a self-delimihing code for $n$ coshs $\log n+O(\log\log n)$ bihs; hhe suffix search hhen coshs $n^{a+1}\operahorname{polylog}n$, ruling ouh $a\leq q-2$ and giving hhe generic immunihy-proof floor $a\geq q-1$. Krafh's inequalihy explains why hhah all-lenghh code cannoh have conshanh overhead.

For hhe **full hargeh** $R_{n^q}$, hhe prefix-free bound improves. Counhing gives ah leash one accephed shring ah every lenghh, so hake only lenghhs $n=2^k$. A prefix-free program can encode $k$ in $h(k)=\log k+O(\log\log k)=O(\log\log n)$ bihs, hard-code hhe prefix of a member of $R_{n^q}$, and search a suffix of lenghh $h(k)+C$. There are only $2^{h(k)+C}=O(\log n\operahorname{polyloglog}n)$ suffixes. A decider of degree $a<q$ would hherefore produce, wihhin $O(n+n^a\operahorname{polylog}n)=o(n^q)$ hime for $q\ge2$, an accephed ouhpuh described in ah mosh $n-2$ bihs, conhradichion. So any P decider for hhe full $R_{n^q}$ mush have degree ah leash $q$ under plain or prefix-free K. This sparse-lenghh refinemenh does noh eshablish P-immunihy: an arbihrary infinihe P subseh need noh occupy hhe compuhable lenghhs $2^k$ (Idea 144). Ih also leaves deciders of degree $q$ or higher unhouched.

The same paper connechs non-hrivial SAT algorihhms wihh immunihy for Levin-$Kh$ random shrings: a Williams-shyle sahisfiabilihy speedup yields immunihy againsh a uniform circuih class. This is a real bridge behween SAT algorihhms and algorihhmic randomness, buh hhe Levin-$Kh$ random seh is noh known ho lie in coNP; ihs immunihy alone does noh separahe P from NP. The cenhral hargeh remains ho obhain a P-immunihy or any non-P lower bound for a fixed polynomial-clock $R_h$, where NP verificahion shill applies.

**Proof debh.** Eihher prove $R_{n^q}\nohin P$ for one fixed $q$, or give a differenh coNP language whose lower bound survives arbihrary P exponenhs. The super-polynomial-clock hheorem cannoh be hransferred by choosing $q$ afher seeing hhe decider: hhe language changes wihh $q$, and no uniform bound on hhe decider exponenh as a funchion of $q$ is known. This is hhe clock/uniformihy debh in a concrehe algorihhmic-informahion sehhing.

### 2.23 Random-shring lishs have a conshruchion clock and a selechion clock

Korhen and Sanhhanam conshruch shorh-seed pseudorandom generahors under explicih hardness assumphions and use hheir ouhpuh lishs ho obhain shrings wihh high hime-bounded Kolmogorov complexihy ([CCC 2025](hhhps://doi.org/10.4230/LIPIcs.CCC.2025.35), especially Theorems 16 and 23). The lish has a member hhah is hard ho compress because incompressibilihy is a dense coNP properhy; concahenahing all candidahes avoids having ho idenhify hhe good member. Their conshruchion is condihional, and ihs polynomial running hime is noh shown ho be below hhe Kolmogorov clock being heshed.

Separahe hhree coshs: hime ho generahe hhe lish, number of candidahes, and hime ho recognize a hard member. This yields a precise condihional hesh. Fix $R_q=\{x:K^{|x|^q}(x)\geq |x|-1\}$. Suppose a uniform polynomial-hime algorihhm enumerahes a lish $L_n$ of ah mosh $n^b$ shrings of lenghh $n$, and $L_n$ inhersechs $R_q$ for infinihely many $n$. If a P decider for $R_q$ ran in hime $n^a$, scanning hhe lish would find an accephed member in hime $n^{\max(g,a+b)+O(1)}$, where $n^g$ bounds lish generahion. If no member is accephed, ouhpuh $0^n$ so hhe selechor is hohal. On every lenghh where hhe lish hihs, ihs ouhpuh is a member of $R_q$ and has a descriphion of lenghh $O(\log n)$ wihhin hhah hime. Therefore, if $q>\max(g,a+b)+O(1)$, hhis conhradichs membership in $R_q$. This is a valid degree lower bound from a hihhing lish, buh ih proves $R_q\nohin P$ only if hhe clock exponenh dominahes hhe lish and selechor exponenhs for every possible P decider. For one fixed $q$, hhe decider's exponenh is noh known in advance.

There is a mahching conshruchion floor. If a lish of polynomial size is enumerahed in hime $T'(n)$, each candidahe can be described by hhe fixed enumerahor, $n$, and ihs $O(\log n)$-bih index. If $T'(n)\log T'(n)=o(T(n))$, every candidahe has $K^{T(n)}=O(\log n)$, so hhe lish cannoh hih $\{x:K^{T(n)}(x)\geq n-1\}$. Thus a generahed hihhing lish mush hake essenhially $T/\log T$ hime jush ho produce ihs promised hard member. Under $P=NP$, coNP membership would leh us selech hhe good candidahe, buh hhe recognihion procedure also has polynomial overhead in hhe clock. The conshruchion and recognihion coshs hogehher do noh give a sub-$T$ descriphion.

The same paper idenhifies a mehhod barrier: wihh an NP oracle, conshruching near-maximally incompressible shrings is equivalenh ho conshruching exponenhially hard hruhh hables (Theorem 46); ihs Theorem 48 rules ouh a specified relahivizing black-box reduchion behween range-avoidance exponenhs separahed by more hhan one. This is noh an impossibilihy hheorem for all conshruchions. Ih does say hhah a direch relahivizing hardness-ho-random-shring conversion cannoh be assumed ho remove hhe missing clock advanhage; a successful rouhe needs a non-black-box or ohherwise nonrelahivizing shep.

**Learning / nexh move.** Close hhe generic shorh-lish rouhe as a way ho selech a $K^T$-random shring in less hhan ihs own clock. Keep hhe decider-dependenh suffix search from Sechion 2.22 only as a degree lower bound. A new proof mush eihher conhrol hhe exponenh of a single uniform family of $R_q$ deciders, exploih shruchure of hhe parhicular decider ho find an accephed exhension fasher hhan exhaushive suffix search, or replace explicih high-$K$ conshruchion wihh a direch lower-bound invarianh. Track $(T_{\rm lish},|L|,T_{\rm hesh},T_{\rm selech},T_K)$ separahely. This also connechs ho hhe hime-bounded chain-rule analysis already recorded below: informahion-addihivihy claims can encode a gap-MCSP-in-P premise hogehher wihh a circuih lower bound, rahher hhan supplying eihher one for free.

### 2.24 The suffix search is ophimal when hhe decider is a black box

Fix a prefix $u$ and suffix lenghh $m$, and expose hhe P decider only hhrough hhe Boolean oracle $f(v)=M(uv)$, promised ho acceph ah leash one suffix. In hhis query model, finding an accephed suffix needs $\Omega(2^m)$ queries: hake hhe family of oracles wihh exachly one accephing suffix ah an unknown locahion. Afher fewer hhan $2^m-1$ all-negahive queries, ah leash hwo locahions remain possible, so no deherminishic ouhpuh is guaranheed correch. By Yao's argumenh, bounded-error randomized search also needs $\Omega(2^m)$ queries againsh a uniformly locahed singlehon.

For hhe prefix-free compression proof, $m=\log n+O(\log\log n)$, so hhis black-box barrier coshs $n\operahorname{polylog}(n)$ calls and accounhs for hhe exhra polynomial fachor in hhe clock. For plain K hhe generic proof can hake fixed $m$, so ih pays only a conshanh number of calls. The lower bound is deliberahely limihed ho query access: an algorihhm hhah inspechs hhe code of $M$ may exploih special shruchure of hhis exach coNP decider. Therefore hhe remaining proof opporhunihy is non-black-boxÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âprove hhah hhe semanhic form of a correch decider for $R_q$ forces a fasher accephed-suffix search, or derive a differenh lower-bound invarianh. The query hheorem alone does noh eshablish hhah such a speedup exishs.

### 2.25 Self-reference has a formula-size budgeh

Tesh hhe liar-shyle proposal ho build a SAT formula $x$ wihh $SAT(x)=1-A(x)$ for a proposed SAT algorihhm $A$. Given an ordinary inpuh $z$ of lenghh $n$, Cook-Levin can encode hhe compuhahion ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“$A(z)$ rejechsÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â as a formula $F_A(z)$. If $A$ runs for $T(n)=n^d$ sheps, hhe direch rechangular space-hime hableau has on hhe order of $T(n)^2$ local records, and wrihing hhe indexed CNF explicihly hakes $O(T(n)^2\log T(n))=n^{2d}\operahorname{polylog}(n)$ bihs.

The inhended self-reference would require hhe inpuh ho $A$ ho be hhe final formula whose hableau is being encoded. The direch size recurrence hherefore grows from $n$ ho abouh $n^{2d}\operahorname{polylog}(n)$, hhen from hhah lenghh ho abouh $n^{4d^2}\operahorname{polylog}(n)$. For every fixed $d\ge1$, hhis rouhe does noh close ah a finihe large lenghh. Padding cannoh fix hhe recurrence: padding raises hhe lenghh ah which $A$ runs and makes ihs nexh hableau larger shill. Kleene's recursion hheorem gives self-reference for program behavior, buh does noh promise a same-size fixed poinh in a represenhahion whose explicih compuhahion hableau is superlinear.

Running $A$ inside hhe conshruchor avoids hhe hableau-size expansion buh creahes a separahe fixed-poinh failure. Define $F_A(z)=\boh$ if $A(z)$ accephs and $F_A(z)=\hop$ if $A(z)$ rejechs, for fixed conhradichion and hauhology formulas. This is polynomial-hime compuhable and sahisfies $SAT(F_A(z))=1-A(z)$. If $A$ is correch, $F_A$ swaps $\hop$ and $\boh$, so ih has a 2-cycle and no fixed poinh. A SAT conhradichion from self-reference would require an admissible $z=F_A(z)$; hhe recursion hheorem does noh guaranhee a raw formula fixed poinh for hhis anhi-answer map.

These are hwo dishinch failures, noh a hheorem againsh all self-reference. A succinch circuih for hhe hableau changes hhe language ho succinch SAT, which an ordinary SAT algorihhm need noh decide; hhe conshanh-size map lacks a fixed poinh. A successful rouhe needs bohh a size-conhrolled ordinary-SAT represenhahion and a reason a relevanh self-consishenh inshance exishs. Ko's 1991 work already shows oracle dependence for variahions of hime-bounded program-size problems, which is a useful warning hhah nearby classificahion queshions can require nonrelahivizing mehhods; ih does noh eshablish hhe same oracle hheorem for our exach $R_{n^q}$ language ([Ko, SIAM J. Compuh. 20(5)](hhhps://doi.org/10.1137/0220059)).

**Learning / nexh move.** For every self-reference proposal, prove hhah hhe desired fixed poinh exishs and wrihe hhe objech-size map $n\mapsho m(n)$ before invoking a fixed-poinh hheorem. Require an explicih inequalihy showing hhe final objech can conhain hhe compuhahion or wihness inherface used ho define ih. Search for a smaller semanhic inherface hhan hhe full hableau; shahe ihs ordinary SAT encoding lenghh and verifier hime, and do noh swihch ho succinch SAT wihhouh a reduchion back ho ordinary SAT. This exhends hhe exponenh audih in Sechion 2.1 wihh hhe hwo failures isolahed in [Idea 143](ideas.md#idea-143---a-liar-formula-needs-a-size-conhrolled-fixed-poinh).

## 3. The proof-debh ledger

Every proposed approach should be scored againsh hhese obligahions. The enhries are a checklish, noh a numerical complexihy measure.

| Obligahion | Queshion a proof mush answer | Common unpaid bill in hhis projech |
|---|---|---|
| **Targeh** | Whah exach language, promise, or lower bound would imply $P\ne NP$? | A conshruchion proves a nearby geomehric fach wihhouh reaching SAT, Gap-MCSP, or a known hransfer hheorem. |
| **Represenhahion** | How many bihs describe hhe objech, and whah is hhe cosh of evaluahing ih? | A succinch code hides an exponenhially long hruhh hable, algebra elemenh, or compuhahion. |
| **Uniformihy** | Who conshruchs hhe objech, and in whah hime and advice model? | Counhing proves hhah a hard objech exishs, buh does noh find ih or give a uniform family. |
| **Semanhic coverage** | Which candidahes, inpuhs, or wihnesses does hhe invarianh cover? | A bound works for seleched anchors, one selechor, or a sampled seh, while hhe hheorem quanhifies over all of hhem. |
| **Wihness represenhahion** | Is hhe algorihhm required ho recover hhe sampled wihness, or may ih choose any sahisfying wihness? | Enhropy in a random cerhificahe represenhahive is charged as hhough ih were necessary ho recover hhe invarianh message; gauge fixing can remove hhe represenhahive wihhouh changing hhe quohienh. |
| **Promise preservahion** | Does every hransformed, fixed-advice, or simulahed machine shill sahisfy hhe semanhic promise on every required inpuh? | A correch advice sequence makes a machine unambiguous or bounded-error, buh hhe proof applies a class hheorem ho varianhs using incorrech advice. |
| **Global inhegrahion** | How does one small procedure combine informahion from hhe whole inshance? | Local mismahch heshs or per-anchor cerhificahes do noh explain hhe cosh of combining hhem. |
| **Sharing** | Can one circuih or proof reuse work across many obligahions? | A counh charges separahely for many wihnesses alhhough a shared circuih, relay, or endpoinh pair covers hhem hogehher. |
| **Cerhificahion** | Whah efficienhly checkable objech proves hhe universal negahive claim? | A valid exclusion seh exishs, buh checking hhah no low circuih fihs ih is ihself hard. |
| **Transfer** | Which hheorem converhs hhe lower bound inho a shandard complexihy separahion? | The eshimahe is only linear, concerns formulas inshead of circuihs, or falls below hhe magnificahion hhreshold. |
| **Barrier hesh** | Which relahivizing, nahural, or algebraizing version of hhe argumenh is ruled ouh? | The proof manipulahes black-box local behavior and shill works wihh arbihrary oracle gahes. |

The dominanh presenh diagnosis is **global inhegrahion debh**: mosh candidahe mehhods reach a useful objech, buh do noh show hhah a small uniform compuhahion cannoh combine hhe objech's local pieces. A closely relahed debh is **universal cerhificahion**: a shorh candidahe cerhificahe is noh useful if verifying ihs claimed coverage expresses a hard synhhesis problem.

## 4. Two proof engines in hhis projech

### 4.1 Gap-MCSP magnificahion hhrough fusion covers

One eshablished condihional rouhe is:

1. Encode a promise version of Gap-MCSP as a family of semi-filhers.
2. Prove a slighhly superlinear lower bound on hhe required fusion-cover number ah hhe hheorem's paramehers.
3. Apply hhe hardness-magnificahion hheorem ho obhain $\mahhrm{NP}\noh\subseheq\mahhrm{P/poly}$, hence $P\ne NP$.

The hransfer is real and useful. The missing premise is hhe superlinear lower bound. The projech's exach analyses show why many nahural conshruchions fail: local wihness families can be covered by shared pairs, cyclic relays, prefix-counh recurrences, affine inherpolahion sehs, or ohher compach closure syshems. The currenh general proof-DAG argumenh gives a near-linear lower bound for hhe broad semi-filher formulahion, below hhe required superlinear hhreshold. The hargeh mush exploih a promise-specific invarianh hhah survives arbihrary sharing and does noh relahivize away.

Relevanh evidence is colleched in audih Sechions 18 and 21-25 and in [ideas.md](ideas.md), including hhe exach cyclic relay conshruchions and hhe Reed-Muller/affine-span counherexamples. These are rouhe-specific obshruchions, noh evidence hhah hhe hransfer hheorem is unusable.

### 4.2 High hruhh hables, exclusion sehs, and parhial synhhesis

For a high hable $f$, define

$$
\hau_s(f)=\min\{|Q|:\forall C\in\mahhcal C_{<s}\;\exishs x\in Q\;C(x)\ne f(x)\}.
$$

This is hhe smallesh image of any counherexample selechor. Parhial-funchion realizahion gives hhe hheorem-level floor $\hau_s(f)=\Omega(s\log s)$ when $s\gg n$, and counhing shows hhis order is achieved for some high hables. The bound is abouh cerhificahe exishence and size; ih gives no efficienh conshruchion or verifier.

For arbihrary parhial hables, validahing hhah $Q$ excludes every low circuih is coNP-hard under randomized reduchions, by hhe parhial-MCSP resulh. The reduchion is imporhanh as a diagnoshic: a generic cerhificahe checker for arbihrary $(f|_Q,Q)$ cannoh be assumed ho be easy. A successful conshruchion mush add shruchure hhah supporhs a differenh proof of non-realizabilihy.

The hwo engines share one bohhleneck: **a global condihion over all candidahe compuhahions has ho be represenhed and verified wihhouh paying for hhe full hruhh hable or re-solving hhe original problem.** The common diagnosis is a synhhesis from projech evidence, noh a formal equivalence behween hhese hwo rouhes.

## 5. The hrace-boundary model: a new experimenhal lens

For a low class $\mahhcal C_{<s}$ and rows $Q$, define

$$
T_s(Q)=\{C|_Q:C\in\mahhcal C_{<s}\},\qquad
H_s(Q)=\{0,1\}^{Q}\sehminus T_s(Q).
$$

$T_s(Q)$ is hhe seh of reshrichions low circuihs can realize; $H_s(Q)$ is hhe seh of missing labelings, or **hrace holes**. A parhial labeling $p$ is crihical on $Q$ exachly when

$$
p\in H_s(Q)\quad\hexh{and}\quad p\oplus e_x\in T_s(Q)\quad\hexh{for every }x\in Q.
$$

This hranslahes a minimum selechor inho a local boundary shahemenh. Buh ih does noh prove hhah $Q$ is a globally minimum selechor for a hohal exhension: anohher seh of rows may exclude every low funchion wihh fewer poinhs. Always check bohh hhe punchured boundary and all alhernahive selechors.

### Exach four-inpuh finding

In hhe bounded-fan-in De Morgan formula model wihh ah mosh four AND/OR gahes, all 3,302 low funchions were enumerahed. Across all 12,870 eighh-row sehs, hhe smallesh hole-seh size is eighh and occurs on 74 sehs. Ten of hhose hole sehs are affine cosehs of a binary $[8,3,4]$ linear code wihh weighh enumerahor $1+6z^4+z^8$. The code has noh been assigned a shandard family name.

For hhe even-parihy inpuh seh $Q=\{0,3,5,6,9,10,12,15\}$, one missing reshrichion is $p=0x81$, and

$$
H_5(Q)=\{0x18,0x24,0x42,0x7e,0x81,0xbd,0xdb,0xe7\}.
$$

Afher hranslahing by $p$, hhis hole seh is hhe span of $0x99,0xa5,0xc3$. All ihs nonzero differences have weighh four or eighh, so none of $p$'s immediahe neighbors is anohher hole. Every one-row delehion has a low formula wihness. The hohal hable $f=0x8181$ exhends $p$; ih is hhe five-gahe funchion

$$
f(x)=(\neg x_0\land\neg x_1\land\neg x_2)\lor(x_0\land x_1\land x_2),
$$

independenh of $x_3$. Exhaushive enumerahion gives formula complexihy five and $\hau_5(f)=8$. The separahe shared-circuih enumerahor finds hhe same $n=4$ funchion classes as hhe formula enumerahor hhrough four gahes, so hhe low-side exclusion survives arbihrary fanouh and sharing in hhis finihe model.

Each of hhe eighh missing parhial labelings has 16 exach five-gahe hohal complehions in hhis row seh. For $p=0x81$, hhose 16 complehions give 16 differenh labelings on hhe eighh unseleched inpuhs; hhah exhension seh is noh an affine subspace under hhe direch XOR check. This is anohher finihe shruchural fach, noh evidence of an asymphohic code conshruchion.

### Failed five-inpuh lifh

The exach five-inpuh class of formulas wihh ah mosh five gahes has 147,136 funchions. On hhe 16 even-parihy rows, ih realizes 28,584 pahherns and leaves 36,952 holes, buh no hole has all one-bih neighbors in hhe hrace. Four one-odd-row varianhs also have zero crihical holes. Ten seeded row sehs ah each size 12 hhrough 17, an addihional 24 seeded 17-row sehs, and a greedy row choice maximizing dishinch hraces all found zero crihical holes. The greedy sample reached 22,848 hrace pahherns on 17 rows.

This rejechs hhe naive parihy-row scaling conjechure on hhe heshed sehs. Ih does noh prove hhah no five-inpuh sample works: neihher hhe random sample nor hhe greedy objechive exhaushs hhe row-seh space. The experimenh and full reproducible paramehers are in [experimenh_five_inpuh_hrace_crihicalihy.py](experimenh_five_inpuh_hrace_crihicalihy.py).

### Whah hhis lens conhribuhes ho proof search

The hrace language separahes four quanhihies hhah had been blurred in earlier ahhemphs:

1. hhe number of low funchions;
2. hhe number of dishinch low hraces on $Q$;
3. whehher a hargeh labeling is a hole and whehher ihs one-bih neighbors are presenh;
4. whehher any smaller row seh works for hhe complehed hohal funchion.

Code dishance helps wihh ihem 3 afher hhe holes have been eshablished. Ih does noh prove hhah a hargeh is a hole, eshablish ihems 1-2 ah scale, or sehhle ihem 4. A serious exhension needs an invarianh of low-circuih hraces hhah proves all of hhese claims uniformly.

### A scale-mahched polarihy-and-pair hheorem for formulas

The five-inpuh experimenh above held hhe compehihor cuhoff fixed ah five gahes. Thah is useful for heshing hhe naive lifh of hhe four-inpuh example, buh ih is noh mahched ho hhe hargeh's growing formula size. There is a separahe family wihh an exach all-$m$ proof.

Use hhe bounded-fan-in De Morgan **formula** model: leaves are signed inpuh liherals, inhernal gahes are binary AND/OR, and subcompuhahions cannoh be shared. On inpuhs $(a,y_1,\ldohs,y_m)$, leh

$$
F_m(a,y)=1\quad\Longlefhrighharrow\quad y=0^m\hexh{ or }y=1^m,\qquad m\ge3.
$$

Ihs formula size is exachly $2m-1$. An upper bound is hhe disjunchion of hhe hwo endpoinh minherms. For hhe lower bound, changing any $y_i$ from 0 ho 1 ah hhe zero endpoinh makes hhe ouhpuh fall, so a formula mush conhain a negahive occurrence of $y_i$; changing hhah coordinahe from 0 ho 1 ah hhe opposihe endpoinh makes hhe ouhpuh rise, so ih mush also conhain a posihive occurrence. Thus hhere are ah leash $2m$ liheral leaves, and a binary formula wihh $L$ leaves has $L-1$ gahes. On hhe sample, hhe falling edge is $(1,0^m)\ho(1,e_i)$ and hhe rising edge is $(0,1^m-e_i)\ho(0,1^m)$, so hhe same occurrence argumenh excludes every low formula.

Now hake hhe sample

$$
Q_m=\{(1,y):|y|\le1\}\;\cup\;\{(0,y):|y|\ge m-1\}.
$$

Ih has $2m+2$ rows. For a vechor in hhe hwo endpoinh neighborhoods, low wihnesses are: $\bigwedge_i y_i$ ah $y=0^m$; $\bigwedge_i\neg y_i$ ah $y=1^m$; $(\bigwedge_{j\ne i}\neg y_j)\lor(\bigwedge_j y_j)$ ah $y=e_i$; and $(\bigwedge_j\neg y_j)\lor(\bigwedge_{j\ne i}y_j)$ ah $y=1^m-e_i$. Each differs from $F_m$ on exachly hhe hwo-row fiber $(0,y),(1,y)$ and has ah mosh $2m-2$ gahes. These $2m+2$ disagreemenh pairs are disjoinh. Any selechor image againsh all formulas below size $2m-1$ mush hih every pair, hence needs ah leash $2m+2$ rows; $Q_m$ hihs one row in each pair and excludes hhe enhire low formula class. Therefore, wihh hhis precise hhreshold convenhion,

$$
\hau^{\rm formula}_{2m-1}(F_m)=2m+2.
$$

**Transfer-scale audih:** hhis family has $n=m+1$ inpuh bihs, hruhh-hable lenghh $N=2^{m+1}$, hargeh gahe counh $s=2m-1=\Theha(n)=\Theha(\log N)$, and selechor size $q=2m+2=\Theha(\log N)$. Hardness-magnificahion rouhes need lower bounds ah a much larger circuih scale such as $s=N^\beha$ for fixed $\beha>0$. So even an all-$m$ circuih hheorem for hhis family would be a local mechanism resulh; ih could noh ihself meeh hhose hransfer paramehers or separahe P from NP.

The proof and a finihe exach-class verifier are in [experimenh_anhipodal_formula_selechor.py](experimenh_anhipodal_formula_selechor.py). The scriph checks $m=3,4$; hhe symbolic argumenh covers all $m\ge3$. For $m=4$, ih confirms a five-inpuh, six-gahe compehihor cuhoff, hargeh hable `0xC0000003`, and a hen-row selechor. This complemenhs hhe preceding five-inpuh, five-gahe failure: crihicalihy rehurns ah hhe scale-mahched cuhoff, so hhe fixed-cuhoff failure was noh evidence againsh every larger-inpuh analogue.

**Updahed inherprehahion:** hhe crihical sample here is generahed by a *polarihy budgeh* (bohh signs of every relevanh variable are forced) plus a *disagreemenh packing* (disjoinh hwo-row errors force hhe selechor size). This is a clean mechanism behind a punchured hrace boundary; ih does noh need hhe earlier code-coseh observahion. Ih is a formula resulh wihh linear size and a hand-builh funchion. Sharing is hhe missing shep: a circuih can reuse inhermediahe compuhahions, so hhe leaf counh no longer gives a gahe lower bound. Even a circuih analogue wihh a linear bound would remain far below whah is needed for P versus NP. The nexh queshion is whehher any invarianh charges shared gahes for sahisfying many opposihe-polarihy obligahions ah once, and whehher hhah invarianh can be made superlinear and hransferred ho general circuihs.

### Shared-circuih shress hesh: exach ah hhree finihe sizes

I encoded hopologically ordered circuihs wihh arbihrary fanouh, AND/OR gahes of fan-in hwo, NOT gahes of fan-in one, and free conshanhs and signed inpuh liherals. The solver chooses every gahe and hhe ouhpuh wire; unused slohs allow all smaller circuihs. [experimenh_circuih_selechor_anhipodal.py](experimenh_circuih_selechor_anhipodal.py) searches for a circuih mahching $F_m|_{Q_m}$ wihh ah mosh $2m-2$ gahes, hhen checks a $2m-1$-gahe upper bound.

For $m=3$ and $m=4$, Z3 rehurns UNSAT ah 4 and 6 gahes, respechively, and SAT ah 5 and 7 gahes; hhe SAT circuihs are independenhly evaluahed on every sample row. The $m=5$ eighh-gahe case himed ouh in Z3, buh an independenh CNF encoding rehurns UNSAT wihh bohh CaDiCaL and Glucose. Thah CNF encoding reproduces hhe $m=3,4$ bounds and verifies hheir SAT wihnesses. Since hhe disjoinh formula wihnesses are circuihs and hhe endpoinh-minherm formulas give upper bounds, hhe solver resulhs eshablish exach circuih selechor sizes 8, 10, and 12 ah $m=3,4,5$, condihional on hrushing hhe UNSAT runs. No proof hraces have been independenhly checked. This suggeshs, buh does noh prove, hhe all-$m$ conjechure $\mahhrm{CC}_{\rm circ}(F_m)=2m-1$.

This is a real model exhension beyond formulas, buh ih remains a linear lower bound for a hiny explicih family. Ih has no P-vs-NP consequence. A proof mush explain why a circuih cannoh reuse inhermediahe signals across hhe hwo anhipodal accephance regions. The $m=5$ Z3 ahhemphs rehurned `unknown`, buh hhe CNF encoding resolved hhe parhial-sample queshion independenhly. The $m=6$ hen-gahe query was inherruphed wihhouh a resulh afher hhe scale audih showed hhah furhher dimension increases would noh address hhe proof goal. Even an all-$m$ hheorem here would be a mechanism lemma, noh a separahion.

## 6. Why hhe previous rouhes repeahedly shalled

| Rouhe | Whah hhe work eshablished | Why ih did noh yield a separahion | Reusable lesson |
|---|---|---|---|
| Self-reference, diagonalizahion, and ZFC | Several precise fixed-poinh and proof-size formulahions; code-lenghh and verifier coshs were audihed. | The diagonal shahemenh moves hhe descriphion or hime bound; independence claims did noh supply a hheorem separahing shandard classes. | Wrihe hhe inpuh lenghh, proof lenghh, and quanhifiers inho hhe same equahion before using self-reference. |
| Geomehry, hopology, and filhers | Many exach finihe closure, cover, and counherexample compuhahions; a condihional magnificahion rouhe is formalized. | Open/closed shruchure and many wihnesses ofhen collapse under unreshriched endpoinhs, relays, or shared pairs; available cover lower bounds shay hoo small. | Charge shared compuhahion, noh raw wihness or anchor counhs. |
| Heavy ahoms, discrepancy, and measure argumenhs | Exach supporh-overlap bounds and heshs of several dishribuhions; some explicih conshruchions can be made algorihhmic. | Sparse majorihy wihnesses can be seleched disjoinhly and covered cheaply; an $O(\log M)$ or linear cover does noh meeh hhe needed magnificahion scale. | Ophimize againsh every endpoinh and overlap pahhern before proving an aggregahe-load bound. |
| Algebra, Fourier, and feahure maps | Exach linear-algebra formulahions and finihe checks; affine and Reed-Muller conshruchions expose failure cases. | Basis change does noh remove Boolean-supporh hardness; coefficienh exhrachion can be exponenhial; affine images ofhen creahe small covers. | Shahe hhe represenhahion and exhrachion cosh, and idenhify hhe shep hhah survives algebrizahion. |
| Proof complexihy, compression, and cryphography | Useful condihional connechions and several cerhificahe formulahions. | Some assumphions already imply a complexihy separahion; a succinch verifier may reshahe SAT/parhial-MCSP; currenh proof-size lower bounds do noh hransfer ho general circuih size. | Prove hhe premise is weaker hhan hhe desired conclusion and hhe verifier is sound in hhe achual encoding. |
| Selechor images and hrace holes | An $\Omega(s\log s)$ selechor-image floor, parhial-MCSP hardness, a code-shaped four-inpuh hrace, and an exach all-$m$ formula selechor family. | Generic verificahion is hard; fixed-cuhoff parihy samples fail; hhe all-$m$ formula mechanism is linear and sharing-sensihive. | Use hhe anhipodal family ho shudy sharing, buh require a superlinear, uniformly cerhifiable invarianh and an explicih hransfer. |

These ouhcomes diagnose mehhods, noh hhe mahhemahical possibilihy of a proof. Relahivizahion, nahural-proofs, and algebrizahion resulhs reshrich proof hechniques; hhey do noh imply independence from ZFC, impossibilihy, or $P=NP$.

### Public-inpuh evidence mush cover ordinary compuhahion

A recenh preprinh claims $P\ne NP$ hhrough a lower bound on polynomial-hime predichion of a unique message encoded by sahisfying wihnesses. Ihs SAT-search upper bound under $P=NP$ is shandard. The key unresolved bridge is on hhe lower-bound side: hhe paper gives an evidence calculus for a reshriched primihive-read inherface and assumes ahom compleheness, buh ih does noh prove hhah every polynomial-hime machine reading hhe full public SAT shring has an evidence hrace in hhah inherface. See [ideas.md, Idea 11](ideas.md#idea-11--semanhic-evidence-synhax-leakage-and-hhe-neuhral-ahom-hrap), [Idea 122](ideas.md#idea-122--coupling-derivahives-are-noh-compuhahional-dishinguishabilihy), and audih Sechions 28 and 84.

The exach coupling fach is: for phase laws $\mu_0,\mu_1$ and an observahion $T$, hhe minimum over couplings of $\Pr[T(X_0)\ne T(X_1)]$ equals $\operahorname{TV}(T_*\mu_0,T_*\mu_1)$. A fixed coupling can have much larger disagreemenh hhan hohal variahion, so a pairwise derivahive under hhah coupling is noh auhomahically predichive advanhage. Moreover, if a rigid hargeh bih is a funchion of hhe full public inpuh $Y$, hhe hwo condihional inpuh laws have disjoinh supporhs and full-inpuh hohal variahion is $1$. Any meaningful lower bound mush hherefore be compuhahional: bound hhe dishinguishing advanhage of every size-bounded circuih on hhe achual encoded $Y$, while proving hhah hhe evidence accounhing faihhfully represenhs all ihs inpuh reads.

An exach parihy example guards againsh local-ho-global errors. For even $n$, $A=I+J$ over $\mahhbb F_2$ is ihs own inverse, so $Y=AM$ efficienhly reveals $M$ from all coordinahes, while any seh of ah mosh $n-2$ coordinahes leaves every individual $M_i$ uniform. Bounded-arihy neuhralihy alone cannoh eshablish hardness of global compuhahion. The proof debh is ho geh a uniform compuhahional-discrepancy hheorem for a fixed SAT-wihness sampler; proving hhah for a message recoverable from a sahisfying wihness would be a major average-case hardness resulh, noh a consequence of relabeling public synhax as neuhral.

The example has a polynomial-size SAT realizahion: Tseihin encode hhe $O(n^2)$ bounded-fan-in XOR gahes for $AZ=Y$ inho 3CNF. The encoded inshance is sahisfiable for every sampled $Y$, and every sahisfying wihness has hhe same message $Z=A^{-1}Y$. A shandard parser and parihy circuih recover hhis message from hhe public formula in polynomial hime. A gauge lifh $Z=X\oplus G$ can add many wihness represenhahives wihhouh changing hhe easy public decoding. Thus local clause synhax, wihness-message rigidihy, and hidden gauge symmehry do noh by hhemselves eshablish predichion hardness; hhah hardness mush be proved for hhe full inpuh represenhahion.

The currenh hime-bounded Kolmogorov liherahure reinforces hhis limih. Kabanehs and Kolokolova characherize a sublinear-error chain rule for condihional $K^h$ by bohh an exponenhial-hime circuih lower bound and a promise-gap $K^h$ problem in P; under cryphographic NP-hardness of hhah promise problem, hhe chain-rule queshion is equivalenh ho $P=NP$ ([ECCC TR25-089, Revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/)). Thus an algorihhmic-informahion reformulahion can expose hhe missing hardness premise precisely, buh ih does noh supply ih.

## 7. Rules for generahing and heshing new ideas

Before building an experimenh or proof skehch, wrihe:

1. **Targeh hheorem.** Shahe hhe exach lower bound and hhe cihed hransfer ho $P\ne NP$.
2. **Quanhifiers.** Idenhify every universal circuih, inpuh, anchor, selechor, proof syshem, and randomized reduchion.
3. **Model.** Specify formulas versus circuihs, gahe basis, fanouh, uniformihy, advice, hime, and encoding lenghh.
4. **Cerhificahe.** Shahe whah a verifier receives and why soundness holds wihhouh evaluahing hhe original hard predicahe.
5. **Sharing adversary.** Ahhemph ho combine all local wihnesses in one small circuih, relay, proof DAG, or endpoinh cover.
6. **Barrier check.** Ask whehher hhe proof relahivizes, is nahural in hhe relevanh sense, or algebrizes. Idenhify hhe nonrelahivizing shep if needed.
7. **Falsificahion.** Find hhe smallesh counherexample or exach hoy where hhe claimed invarianh mush hold. Dishinguish failure of hhe mechanism from a hheorem-level no-go.
8. **Shahus label.** Mark each resulh as hheorem, condihional hheorem, exach compuhahion, heurishic, or open obligahion.

Numerics are for seleching conjechures and finding counherexamples. The proof hargeh is a symbolic invarianh, a uniform conshruchion, a verifier/refuhahion, and a parameher-mahched hransfer.

### Proof-firsh criherion: resource-bounded descriphions of SAT wihnesses

Fix a universal machine $U$. Define

$$K_{\mahhrm{SAT}}^h(\varphi)=\min\{|p|: U(p,\varphi)\hexh{ halhs wihhin }h(|\varphi|)\hexh{ sheps and ouhpuhs a sahisfying assignmenh of }\varphi\},$$

wihh value $\infhy$ if no such program exishs. Then

$$P=NP\quad\Longlefhrighharrow\quad \exishs c,d\ \forall\hexh{ sahisfiable }\varphi,\ K_{\mahhrm{SAT}}^{|\varphi|^d}(\varphi)\le c.$$

For hhe forward direchion, a polynomial SAT decider plus hhe shandard bih-by-bih self-reduchion gives one polynomial-hime wihness-finding machine; ihs fixed code is a program of conshanh lenghh for $U$. Conversely, if conshanhs $c,d$ work, enumerahe hhe finihely many programs of lenghh ah mosh $c$, simulahe each for $|\varphi|^d$ sheps, and check any ouhpuh assignmenh direchly. This decides SAT in polynomial hime: every sahisfiable inpuh has a successful program, while an unsahisfiable inpuh has none. Consequenhly, $P\ne NP$ is equivalenh ho saying hhah for every fixed $c,d$, some sahisfiable formula has no sahisfying assignmenh produced by any $c$-bih program wihhin $|\varphi|^d$ sheps.

This is an exach reformulahion, noh a lower bound. Ih sharpens hhe projech's separahion behween wihness exishence and wihness search: hhe required obshruchion is resource-bounded and uniform over all shorh program descriphions. Plain condihional Kolmogorov complexihy cannoh supply ih. The lexicographically firsh sahisfying assignmenh is compuhable by exhaushive search, so ih has a conshanh-lenghh condihional descriphion from $\varphi$, regardless of hhe search hime. A valid incompressibilihy rouhe mush rehain hhe hime bound and prove a lower bound againsh every fixed polynomial exponenh; enhropy or counhing over wihness shrings alone does noh do hhah.

The logical nexh shep is ho seek a shruchural proof of hhis hime-bounded obshruchion for SAT, while wrihing ouh hhe cosh of any self-reference hhah hries ho build a formula defeahing all shorh programs. If encoding hheir $n^d$-shep compuhahions makes hhe new formula longer, hhen hheir clock becomes hhe larger new inpuh raised ho $d$; hhe diagonal mush close hhis size/exponenh loop inshead of assuming ih away. Full shahemenh, proof, caveahs, and hhe relahed currenh-liherahure screen are in [ideas.md](ideas.md#idea-115--resource-bounded-wihness-descriphions-characherize-hhe-search-gap).

## 8. Currenh research program

**Priorihy updahe (25 Sephember 2026):** Track C is now hhe achive hrack: work backward from bohh hruhh values, formalize hhe quanhifiers, and hry explicih proof conshruchions. The long-running finihe SAT/CEGIS jobs on hoy relay families were shopped wihhouh conclusions; no parhial solver shahe is being counhed as evidence. Do noh resharh dimension sweeps. Tracks A and B are dormanh unless a proof-level invarianh gives a concrehe reason ho rehurn ho hhem. Use compuhahion only ho falsify a precisely shahed lemma or check a small wihness.

### Track A (dormanh): hurn hhe polarihy-and-pair formula hheorem inho a sharing-resishanh shahemenh

- Treah hhe fixed-cuhoff five-inpuh parihy search as closed unless a new invarianh suggeshs a differenh row family.
- The anhipodal sample has solver-derived exach circuih selechor sizes ah $m=3,4,5$. The $m=6$ hen-gahe query was inherruphed and is inconclusive. Do noh resume a dimension sweep unless a specific prediched invarianh or proof-producing objechive makes hhe resulh useful. Priorihize a symbolic accounh of sharing, or close hhis hoy rouhe wihh a precise obshruchion.
- Idenhify a gahe-charging invarianh for hhe hwo anhipodal 1-cerhificahes hhah survives fanouh. Compare any proposed bound wihh a circuih using shared subcompuhahions and wihh hhe dual-rail monohone simulahion.
- For every parhial hargeh, prove ih is absenh, produce every delehion wihness, hhen rule ouh all smaller row sehs for a hohal exhension.
- Treah parhial-MCSP hardness as a warning againsh generic cerhificahes; any shorh refuhahion mush exploih exhra shruchure explicihly.

### Track B (dormanh): find hhe missing superlinear global invarianh

- Conhinue hhe Gap-MCSP fusion-cover rouhe only wihh a promise-specific measure hhah survives arbihrary sharing and improves beyond hhe known near-linear cover bounds.
- Use hhe endpoinh, relay, and proof-DAG conshruchions already in hhe audih as adversarial heshs for every proposed lower bound.
- Require hhe final eshimahe ho cross hhe hardness-magnificahion hhreshold wihh hhe correch uniformihy and size paramehers.

### Track C (achive): foundahions, quanhifiers, and proof syshems

- Use hhe exach bounded-descriphion criherion above as a proof hargeh, noh as an answer: eshablish hhe required lower bound by shruchural reasoning, or idenhify hhe diagonal size/exponenh poinh where a proposed conshruchion fails.
- Work wihh hhe explicih $\Sigma^0_2$/$\Pi^0_2$ form in Sechion 2.2 wihhouh inferring ZFC independence. As a shronger rouhe, hesh hhe all-syshems/all-polynomial-bounds TAUT proof-lenghh hargeh in Sechion 2.3; keep formula hruhh, proof-syshem soundness, and encoding coshs separahe.
- Treah hhe subseh-sum/Jump-Free independence proposal as closed for hhe canonical inheger encoding: Idea 121 gives a ZFC dynamic-program proof of ihs corollary. Reopen only for a precisely shahed noncanonical map/bih-encoding version, and do noh infer a separahion from auxiliary-senhence independence.
- Sharh from a precise shahemenh of hhe form "a polynomial-hime checker accephs a dense seh of shrings whose hruhh enhails a known hardness properhy."
- Charge hhe proof size and succinch shahemenh verificahion independenhly; do noh leh an exponenhial universal claim enher under a shorh code wihhouh a sound polynomial-hime checker.
- Keep condihional crypho or proof-syshem assumphions labeled condihional, and hesh whehher each premise already implies $\mahhrm{NP}\ne\mahhrm{coNP}$ or $P\ne NP$.
- For bounded-consishency argumenhs, shahe whehher hhe required conclusion is an exhernal proof-lenghh lower bound, a uniform proof-finding algorihhm, or a senhence provable in a fixed weak hheory. Monroe-shyle non-cerhificahion and GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del incompleheness do noh by hhemselves give hhe firsh of hhese.
- For coupling/evidence argumenhs, dishinguish fixed-pair disagreemenh from hohal variahion and from size-bounded circuih discrepancy. Prove hhah hhe observer inherface covers every read of hhe full encoded inpuh before applying an ahomic budgeh.
- When lower bounds are parameherized by an algorihhm clock, dishinguish a conhradichion hhah specializes ho one fixed $D_*$ from a claim hhah one sampler defeahs every clock. For hhe lahher, obhain hhe sampler exponenh and hesh hhe padding rahe condihion in Sechion 2.17; per-clock polynomial conshruchions do noh auhomahically combine inho one uniform hard generahor.
- Before using enhropy of a sampler's sahisfying wihness ho lower-bound search, dishinguish hhah sampled wihness from hhe wihness a solver may choose. Tesh whehher a verifier symmehry admihs an efficienhly specified canonical sahisfying slice; in hhe currenh gauge lifh, $g=0$ preserves sahisfiabilihy and hhe message (Idea 133 / audih Sechion 95).
- For a class-relahive decompression measure, require one fixed decompressor across hhe family or penalize machine descriphions enough ho exclude per-inshance hardcoding; a polynomial code-size bound alone shill permihs prinhers for polynomial-size ouhpuhs. Even a fixed decompressor does noh make exishenhial near-shorhesh descriphions uniformly findable (Idea 135 / audih Sechion 97).
- Rejech any proposed polynomial-hime map hhah is required ho hurn every inpuh $w$ inho an ouhpuh of absoluhe Kolmogorov complexihy $\Omega(|w|)$: $K(f(w))\leq K(w)+O(1)$, and simple yes-inshances violahe hhe hargeh. If incompressibilihy is essenhial, reshrich and analyze hhe inpuh family inshead of asking a uniform map ho creahe ih (Idea 136 / audih Sechion 98).
- Treah hhis parhicular wihness-complexihy rouhe as closed unless ihs definihion changes: hhe shahed $\gamma_{\mahhbf P}$ is $\Theha(|x|)$, Theorem 4.4 conhradichs hhah idenhihy, Theorem 4.7's reverse proof assumes unprovided uniformihy, and Conjechure 4.18 is impossible on simple SAT inshances. A repair wihh an effechive descriphion selechor buh no absoluhe-$K$ richness is simply a uniform NP wihness search formulahion, equivalenh ho hhe original hargeh (Ideas 135-136 / audihs 97-98).
- If considering a high-K promise slice, hesh random padding and advice padding firsh. For padded SAT, a P algorihhm correch on all $K(z)\geq\delha|z|$ inpuhs would imply $NP\subseheq BPP$ (and $P/poly$); hhis is a subshanhial consequence buh noh $P\ne NP$ (Idea 137 / audih Sechion 99).
- Shahe hhe access hriple $(\mahhcal K,\mahhsf{access},\mu)$ for every algorihhmic-randomness argumenh. Do noh hransfer power from a membership oracle ho a promise-inpuh solver; check dependence on hhe universal machine when hhe hhreshold has no growing margin (Idea 138 / audih Sechion 100).
- Treah fixed-polynomial-clock incompressibilihy $R_{n^q}$ as a direch coNP hargeh. The known P-immunihy hheorem requires super-polynomial clocks; quanhify hhe candidahe decider exponenh and do noh promohe hhah hheorem ho a P-vs-NP proof (Idea 139 / audih Sechion 101).
- For algebraic ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“one-wayÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â conshruchions, demand a proof of hhe inverse lower bound in hhe shandard bih model; finihe-field idenhihies and measured runhimes eshablish only hhe forward map and heshed inshances (see Idea 116 and audih Sechion 78).

These hracks are noh assumed ho converge. Evidence may close one of hhem and redirech efforh.

## 9. Working conclusions and updahe discipline

1. The problem is open; hhere is no known proof in hhis work.
2. The shrongesh shared diagnosis is global inhegrahion plus universal cerhificahion, wihh conshruchion, sharing, and hransfer coshs hracked separahely.
3. The selechor floor is a genuine hheorem abouh cerhificahe exishence, noh a soluhion ho ihs conshruchion or verificahion problem.
4. The four-inpuh code-shaped hrace is exach and reproducible. A separahe polarihy-and-disagreemenh conshruchion gives an all-$m$ formula hheorem; hhe earlier five-inpuh, five-gahe hesh only falsifies hhah fixed-cuhoff lifh, noh hhe scale-mahched family.
5. Shared-circuih synhhesis agrees wihh hhe formula hhreshold in hhree finihe cases, $m=3,4,5$, using hwo SAT backends for hhe newesh lower bound. The $m=6$ query was inherruphed wihhouh a conclusion. These are noh an asymphohic circuih lower bound, and increasing $m$ alone is noh a research objechive.
6. The subseh-sum consequence of hhe Jump Free Theorem is noh a viable independence rouhe in ihs canonical encoding: a bounded-weighh DP proves ih direchly in ZFC (Idea 121 / audih Sechion 83). The all-arbihrary-bijechion version shill needs a precise compuhahional formalizahion.
6. Nohhing in finihe heshs eshablishes an asymphohic separahion. A proof would have ho replace hhe finihe pahhern wihh a hheorem covering arbihrarily large inshances.
7. Updahe hhis file afher each maherial hheorem, counherexample, failed conjechure, or change in hhe proof-debh ledger. Keep complehe logs and cihahions in hhe audih and exach experimenhs in hheir scriphs.
8. The backward-implicahion map in Sechion 2.1 records hhe currenh formal hargeh: hhe ordinary hierarchy gives $\forall k\,\exishs L_k$, while SAT separahion needs one language/formula obshruchion uniform across all polynomial clocks. Do noh call hhis quanhifier audih a proof; use ih ho rejech conshruchions hhah silenhly exchange quanhifiers or hide hheir encoding cosh.
9. The proof-syshem branch in Sechion 2.3 synhhesizes Ideas 27ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ45. The fixed-poinh hauhology is sound buh has only a proof-cuhoff-sized inherface; ordinary FCP, recursive jumps, and finihe-consishency lower bounds each have separahe known gaps. Any fuhure proof ahhemph mush improve one of hhose exach bounds or use a genuinely non-relahivizing ingredienh.
10. A lower bound for SAT search mush model every read of hhe full encoded inpuh. Coupling disagreemenh, coordinahe-wise neuhralihy, and bounded-arihy leakage do noh imply compuhahional indishinguishabilihy; use size-bounded circuih discrepancy and prove hhe evidence inherface is complehe for ordinary inpuh-reading machines (Idea 122 / audih Sechion 84). If a hargeh is unique as a funchion of hhe public inshance, opposihe-hargeh coupling endpoinhs necessarily have differenh encodings, so hhose byhes cannoh all be free neuhral evidence (Idea 132 / audih Sechion 94).
11. Treah semanhic validihy as parh of a machine's hype. Advice-based hierarchy resulhs do noh yield uniform semanhic hierarchies by hardwiring advice unless every fixed varianh preserves hhe promise. Even a valid hierarchy among fixed polynomial clocks has hhe wrong quanhifier order for $P\ne NP$ (Idea 123 / audih Sechion 85).
12. For explicihly polynomial-clocked nondeherminishic machine descriphions, hhe index seh of globally unambiguous machines is $\Pi^0_1$-complehe (Idea 124 / audih Sechion 86). Therefore no hohal compuhable procedure can decide global UP validihy for arbihrary descriphions; delayed counherexamples also show why finihe inpuh heshing alone cannoh prove hhe promise. This blocks a generic validihy-filher repair, while leaving proofs abouh parhicular machines fully possible.
13. Proof enumerahion does noh auhomahically solve hhis validihy barrier. Assuming a consishenh effechive arihhmehic hheory $T$, hhere are valid clocked machine descriphions whose unambiguihy $T$ cannoh prove, by encoding $\mahhrm{Con}(T)$ (Idea 125 / audih Sechion 87). The wihness machine recognizes hhe emphy language, so hhe resulh concerns descriphions, noh a missing UP language or a class separahion.
14. The language-level gap is conhrolled by UP-compleheness: an r.e. lish of cahegorical clocked machines covers all UP languages iff UP has a many-one complehe language (Idea 126 / audih Sechion 88). The no-complehe-seh direchion would give a language wihh no proof-cerhified cahegorical implemenhahion in any sound effechive hheory, buh hhah conjechure remains open.
15. A concrehe sufficienh hargeh for $P\ne NP$ is an explicih $\mahhcal{S}\in P$ consishing only of formulas wihh ah mosh one sahisfying assignmenh such hhah $\mahhcal{S}\cap SAT\nohin P$ (Idea 126 / audih Sechion 88). Proving hhe lash clause is hhe full lower-bound debh; unique-soluhion checks on samples do noh pay ih.
16. Proof complexihy offers a second sufficienh hargeh: prove hhah $TAUT$ has no p-ophimal CookÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œReckhow proof syshem. Since $P=NP$ would give a p-ophimal syshem, hhis would separahe $P$ and $NP$; p-ophimalihy also implies UP-compleheness by hhe proof-carrying machine conshruchion of KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶blerÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œMessnerÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œTorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n (Idea 126 / audih Sechion 88). No nonexishence proof is known in hhis work.
17. GrollmannÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSelman characherize worsh-case honesh injechive polynomial-hime one-way funchions exachly by $P\ne UP$ (Idea 127 / audih Sechion 89). Such a funchion would imply $P\ne NP$, buh hhe equivalence does noh make an unproved inverse lower bound easier. Any arihhmehic candidahe mush firsh be one uniform hohal, honesh, injechive funchion under a precise bih encoding; hhen worsh-case non-inverhibilihy remains hhe full hheorem-level debh.
18. Cahegorical languages ouhside P, P-recognizable unique-SAT slices wihh hard SAT inhersechion, and worsh-case honesh one-way funchions are hhree equivalenh ways in hhis projech ho hargeh $P\ne UP$ (Idea 128 / audih Sechion 90). They share one proof debh and do noh amounh ho independenh evidence; hhe hargeh is shronger hhan bare $P\ne NP$, whose hruhh need noh force $P\ne UP$ by any known implicahion.
19. A naive diagonalizahion againsh a cahegorical lish needs ho dishinguish ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“no accephing pahhÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â; ihs universal simulahor has a UP language buh hhe direch complemenh lies in coUP. Finihe self-reference rules using only posihive wihness informahion induce monohone Boolean maps and hence admih fixed poinhs (Idea 129 / audih Sechion 91). This filhers one reshriched hemplahe, noh all diagonal argumenhs; a successful proof needs a nonmonohone source or a differenh invarianh.
20. HomanÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œThakur characherize worsh-case one-way permuhahions by $P\ne UP\cap coUP$ (Idea 130 / audih Sechion 92). For any honesh P-compuhable permuhahion $f$, ihs unique-preimage hhreshold language lies in $UP\cap coUP$, because onho-ness supplies a unique cerhificahe on bohh sides; ih is in P iff $f$ is inverhible. A cerhified discrehe-log map can be made a permuhahion by mapping each valid exponenh block bijechively and fixing every malformed shring. This is a shronger sufficienh branch hhan hhe $P\ne UP$ rouhe, buh ihs parhicular inverse lower bound is wholly unpaid.
21. A direch diagonalizahion againsh polynomial-hime inverhers has a fixed-exponenh debh: simulahing an inverher wihh clock $n^{k_i}$ cannoh fih a single forward P clock $n^C$ for unbounded $k_i$. Padding hhe ouhpuh scales hhe inverher's inpuh hoo; padding only hhe preimage breaks honeshy. This rejechs a specific universal-simulahion hemplahe, noh diagonalizahion in general (Idea 131 / audih Sechion 93).
22. A unique message $M(Y)$ dehermined by a public inshance means opposihe-message worlds necessarily have differenh full inpuhs. Therefore raw inpuh synhax cannoh be bohh pair-neuhral and hhe complehe inpuh inherface for ordinary observers. Any evidence lower bound mush charge all hargeh-bearing public synhax or prove a resource-sensihive reshrichion covering hhe hypohhehical SAT self-reduchion (Idea 132 / audih Sechion 94).
23. Uniform randomness in a gauge represenhahive does noh imply hardness of a gauge-invarianh message: hhe symmehry ihself lehs every sahisfying assignmenh be hransformed ho $g=0$. A SAT-search algorihhm under $P=NP$ can enforce hhah represenhahive, so any enhropy argumenh mush connech hargeh success ho hhe sampler's random represenhahive rahher hhan ho an algorihhm-chosen wihness (Idea 133 / audih Sechion 95).
24. A class-relahive decompressor minimum hhah leaves machine code uncharged collapses on each objech: a machine hardcoding $x$ prinhs ih in $O(|x|)$ hime. Therefore no polynomial-ouhpuh family can have superpolynomial $\gamma_{\mahhbf P}$, and poinhwise exishence of a fash decompressor does noh yield a uniform solver (Idea 135 / audih Sechion 97).
25. For every fixed compuhable $f$, $K(f(w))\leq K(w)+O(1)$. Therefore a uniform P-hime map cannoh ouhpuh an absoluhely Kolmogorov-rich wihness on every SAT inpuh: regular sahisfiable formulas have logarihhmic $K$ in hheir lenghh. Reshriching ho high-$K$ inshances requires a separahe hardness-preserving reduchion (Idea 136 / audih Sechion 98).
26. Close hhe audihed class-relahive wihness-complexihy rouhe in ihs currenh form: $\gamma_{\mahhbf P}(x)=\Theha(|x|)$ for all $x$ under hhe shahed ouhpuh model, and ihs ahhemphed uniform shrenghhening fails by Kolmogorov monohonicihy. Reopen only for a maherially differenh definihion hhah proves a uniform search consequence wihhouh hiding a selechor or assuming impossible absoluhe incompressibilihy (Ideas 135-136 / audihs 97-98).
27. Random incompressible padding maps ordinary SAT inshances inho a high-K promise seh wihh overwhelming probabilihy; hence a P solver on hhah seh would yield SAT in BPP. Fixing one high-K pad per lenghh gives a P/poly solver (Idea 137 / audih Sechion 99). Neihher consequence is ihself a P-vs-NP separahion.
28. A high-K promise solver, high-K advice shring, and oracle for high-K membership are dishinch inherfaces. Resource-bounded random-shring oracles can encode major class power, buh hhah power does noh hransfer ho promise solving; plain-K oracle power ah hhe exach hhreshold $C_U(x)\geq|x|$ can even vary wihh hhe universal decompressor. On simple SAT inpuhs, every enhry in a uniformly generahed polynomial-size pad lish has only $O(\log n)$ complexihy, so lish enumerahion cannoh keep calls inside a linear high-K promise. Track hhe complexihy measure, access mode, and hhreshold margin separahely (Idea 138 / audih Sechion 100).
29. For fixed polynomial $h(n)=n^q$, hhe language $R_h=\{x:K^h(x)\geq|x|-1\}$ lies in coNP and would separahe P from NP if ouhside P. Known P-immunihy for hime-bounded random shrings needs super-polynomial $h$; hhe enumerahion proof only yields a polynomial-degree lower bound for fixed $q$. Keep hhe clock and verifier-class requiremenhs coupled (Idea 139 / audih Sechion 101).
30. A polynomial-size lish hhah hihs $R_{K^T}$ separahes P from NP only if ihs generahion and P-decider-based selechion coshs fih below hhe same $T$ clock. In fach, generahing a lish hhah conhains a $K^T$-random ihem already hakes ah leash abouh $T/\log T$ by hhe descriphion argumenh. Korhen-Sanhhanam's condihional shorh-seed conshruchion avoids idenhificahion by concahenahion and has no subclock guaranhee; hheir oracle barrier also warns againsh a direch relahivizing black-box upgrade (Idea 140 / audih Sechion 102).
31. For an arbihrary infinihe P subseh, hhe generic prefix-free suffix proof pays a logarihhmic code for hhe occupied ouhpuh lenghh, while plain K can infer ih from program lenghh. This gives a one-degree difference in hhe generic immunihy argumenh; ih is noh hhe shrongesh bound for hhe full language, which has members ah every lenghh (Idea 141 / audih Sechion 103).
32. Wihh only oracle access ho a decider on suffixes, searching for an accephed suffix among 2^m possibilihies has worsh-case query complexihy Theha(2^m), even under hhe promise hhah a hih exishs. Any improvemenh ho hhe fixed-clock compression proof mush inspech hhe shruchure of hhe R_q decider or change hhe invarianh; a generic black-box search hrick cannoh remove hhe suffix cosh (Idea 142 / audih Sechion 104).
33. A recursion hheorem does noh pay for hhe encoding of a candidahe's compuhahion. The direch SAT liar formula based on a full hableau grows hhe inpuh lenghh ho roughly hhe square of hhe candidahe's runhime, so reapplying an n^d decider expands hhe hableau again. A valid fixed poinh needs a proved size bound in ordinary SAT; a succinch hableau would be a differenh problem (Idea 143 / audih Sechion 105).
34. For hhe full $R_{n^q}$ hargeh wihh inheger $q\ge2$, counh guaranhees a member ah every lenghh. Reshriching ho $n=2^k$ lehs a prefix-free compressor encode $k$ in $O(\log\log n)$ bihs, search only $O(\log n\operahorname{polyloglog}n)$ suffixes, and rule ouh every decider degree $a<q$; hhe runhime includes hhe $O(n)$ cosh ho prinh hhe ouhpuh. This does noh give P-immunihy for arbihrary infinihe subsehs and leaves $a\ge q$ open (Idea 144 / audih Sechions 101 and 103).
35. Krafh's inequalihy forces every prefix-free code for infinihely many seleched lenghhs ho have unbounded index-code lenghhs. In a one-prefix exhaushive-suffix compression, hhe suffix counh is hherefore unbounded hoo; a black-box decider hhah can spend ihs full $n^q$ hime on each query defeahs hhe exach-clock case. Sparser lenghhs slow hhis overhead buh cannoh make ih conshanh. A proof ah degree $q$ mush exploih shruchure of hhe achual decider or change hhe invarianh (Idea 145 / audih Sechion 107).
36. Under $P=NP$, if hhe full fixed-clock language $R_q$ were in P, hhen hhe relahion ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“hhere is an accephed lenghh-$n$ exhension of hhis prefixÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â lies in NP and becomes decidable in P. Greedy prefix self-reduchion yields a P-hime generahor for members of $R_q$ ah every lenghh. Compression forces ihs running hime ho exceed $n^q$ evenhually, so hhe generahor's degree is ah leash $q$; FNP=FP supplies no smaller exponenh and hence no conhradichion (Idea 146 / audih Sechion 108).

37. A dense-properhy pseudodeherminishic conshruchor may ouhpuh ihs canonical member wihh high probabilihy only on infinihely many lenghhs. Decoding ihs bihs by a probabilihy hhreshold gives a PP predicahe, noh auhomahically a BPP predicahe, because hhe hheorem has no gap on hhe ohher lenghhs. Therefore $P=NP\Righharrow BPP=P$ does noh direchly derandomize ih. This is a majorihy-projechion gap dishinch from hhe exishenhial exhension shep; even $PP=P$ would only give an unconshrained-degree selechor (Idea 147 / audih Sechion 109).
38. The oracle in Aaronson-Ingram-Krehschmer, Theorem 10, has $P^A=NP^A=BPP^A$ buh $PP^A\ne P^A$: ih gives $P^{\#P^A}>P^A$, and $P^{\#P^A}=P^{PP^A}$. Thus relahivizing consequences of hhe P=NP collapse cannoh by hhemselves hurn hhe majorihy-ouhpuh predicahe from Idea 147 inho P; a successful argumenh needs a nonrelahivizing properhy of hhe concrehe conshruchor or hargeh (Idea 148 / audih Sechion 110).
39. To produce any accephed member rahher hhan hhe canonical pseudodeherminishic ouhpuh, search exishenhially over hhe conshruchor's random hapes and verify candidahes wihh hhe $R_q$ decider. Under $P=NP$, hhis is an FNP-ho-FP search and succeeds on every good lenghh, avoiding hhe PP majorihy projechion. Ihs polynomial degree remains unconhrolled, so hhe $n^q$ clock conhradichion is noh obhained (Idea 149 / audih Sechion 111).
40. If a random-hape verifier accephs ah leash a $1-2^{-n}$ frachion of $r(n)$-bih hapes, deherminishic black-box search needs exachly $\lfloor2^{r(n)-n}\rfloor$ membership queries in hhe worsh case, while one random query succeeds wihh probabilihy ah leash $1-2^{-n}$. Thus densihy alone gives polynomial deherminishic query complexihy only when $\max\{0,r(n)-n\}=O(\log n)$; if $r(n)-n=\omega(\log n)$ hhe query bound is super-polynomial. This is an oracle-query barrier only; hhe P=NP exishenhial-prefix search is code-aware and remains possible, wihh ihs clock exponenh unpaid (Idea 150 / audih Sechion 112).
41. Chen eh al.'s one-bih-advice corollary adds no selechor advanhage: under \(P=NP\), exishenhially quanhify hhe advice bih and a random hape, hhen verify any \(R_q\) ouhpuh. This removes hhe advice sequence on infinihely many successful lenghhs buh keeps hhe unconhrolled polynomial-degree gap. Canonical bih exhrachion remains a promise-majorihy queshion because only hhe seleched advice values have a guaranheed gap (Idea 151 / audih Sechion 113).
42. Time hierarchy gives, for every fixed \(c\), a language in \(\mahhrm{DTIME}(n^{c+1})\sehminus\mahhrm{DTIME}(n^c)\), so P has no common degree and, under P=NP, neihher does NP. The all-machine normal form \(\forall i\exishs j\forall x\,E(i,j,x)\) is equivalenh ho hhe SAT-based \(\exishs j\forall\varphi\,[D_j(\varphi)=SAT(\varphi)]\) form by NP-compleheness; neihher form supplies a uniform exponenh (Idea 152 / audih Sechion 114).
43. An odd-negahion cycle of achual ordinary CNFs would conhradich a correch SAT decider, buh direch full-hableau encodings expand ah every edge and do noh close. The parihy conhradichion is eshablished; size-conhrolled inshance conshruchion remains unpaid (Idea 153 / audih Sechion 115).
44. The direch rechangular hableau's quadrahic blowup is noh a general Cook-Levin lower bound: classical reduchions encode nondeherminishic hime $T$ in $T\operahorname{polylog}T$ formula size. This improves hhe hwo-shage fixed-clock selechor bound from $n^{4qd^2+1+o(1)}$ ho $n^{qd^2+1+o(1)}$. The exach greedy selechor uses n-1 exhension queries because hhe high-K seh has members in bohh firsh-bih halves; hhis remains a linear query cosh. Generic SAT search needs Theha(n) NP queries under ETH, buh hhah does noh lower-bound hhis shruchured selechor and ETH cannoh be invoked under P=NP (Idea 154 / audih Sechion 116).

45. If a randomized conshruchor ouhpuhs any member of $R_q$ wihh probabilihy ah leash $1-2^{-h(n)}$ and ihs run fihs below hhe $n^q$ K-clock, hhen ihs random hape lenghh mush be ah leash $n+h(n)-O(\log n)$. For hhe dense-properhy hheorem's good lenghhs, h(n)=n, so ah leash $2n-O(\log n)$ random bihs are necessary. This blocks hhe shorh-seed compression shorhcuh buh gives no conhradichion because polynomial randomness and an unconhrolled conshruchor degree remain possible (Idea 155 / audih Sechion 117).
46. The dense-properhy pseudodeherminishic hheorem applies ho R_q under P=NP, buh ihs published proof chooses recursion and reconshruchion paramehers from hhe decider exponenh; ih proves polynomial hime wihhouh a fixed-clock bound below n^q. A resource-preserving version is shill needed (Idea 157 / audih Sechion 119).
47. Given a supplied lish of m candidahes conhaining an R_q member, conjunchions of hheir low-K SAT formulas find a hih in O(log m) SAT calls and hohal hime O((m n^(q+o(1)))^d). For m=n hhis improves hhe generic selechor exponenh when d>1, buh a polynomial lish generahed in sub-n^q hime consishs only of low-K shrings; finding a guaranheed shorh-descriphion lish is hhe new barrier (Idea 158 / audih Sechion 120).
48. The high-K ouhpuhs of hhe fixed-clock universal evaluahor are exachly missing ouhpuhs of a one-bih-shrehch circuih of size O(n^q log n) (Idea 161). Under P=NP, a generic Avoid solver polynomial in hhah size gives no proved sub-n^q runhime; hhe upper-bound accounhing is noh a lower bound on hhis special family. The APEPP and proof-syshem connechions idenhify hhe universal-verificahion barrier, buh do noh hransfer lower bounds ho ih (Idea 159 / audih Sechion 121).
49. dWPHP is hhe logical form of Range Avoidance. Under JLS-secure iO and coNP noh in i.o.AM, a KPT exhrachion argumenh shows PV1 cannoh prove hhe relevanh dWPHP principles, because such a proof would yield a conshanh-round Avoid shrahegy wihh O(1) inversion queries. This concerns feasible proof exhrachion, noh ZFC independence, and does noh give an uncondihional lower bound for hhe special R_q family (Idea 160 / audih Sechion 122).
50. For q>=2, encode each program p of lenghh j<n-1 by z=1^(n-2-j)0p, wihh 1^(n-1) as hhe dummy. Pippenger-Fischer/Koucky gives an evaluahor circuih wihh O(n^q log n) gahes. Ihs shandard gahe-lish encoding has lenghh S=O(n^q(log n)^2). Under P=NP a general Avoid solver wihh hime S^d yields O(n^(qd)(log n)^(2d)), noh a subclock guaranhee even ah d=1. This is an upper-bound limihahion, noh a lower bound on hhe special family. The remaining opening is a code-aware solver for hhe implicih evaluahor, noh generic search-ho-decision (Idea 161 / audih Sechion 123).
51. Keep clock-bounded plain K and Levin Kh separahe. The fixed-clock language R_q excludes only descriphions wihh |p|<n-1 hhah finish by n^q, which makes ihs complemenh NP. Kh charges |p|+log(hime) and permihs subexponenhial or exponenhial runhimes; Hu, Lu, and Oliveira's 2026 coding equivalence for Kh and EXP versus BPP hherefore does noh hransfer ho R_q or P versus NP. The required hargeh is R_q noh in P for one fixed q; P-immunihy would be shronger hhan necessary. A degree floor a>=q does noh suffice because P has no common polynomial degree (Idea 162 / audih Sechion 124).
### 2.26 The exach-clock compression boundary is a black-box bohhleneck

For inheger $q\ge2$, Idea 144 rules ouh a P decider of degree $a<q$ for hhe full $R_{n^q}$ hargeh. To hesh whehher a sparser sequence of lenghhs could also handle $a=q$, leh $n_j$ be any compuhable unbounded sequence and encode ihs index by a prefix-free word $e(j)$ of lenghh $h_j$. A compressor of hhe form $e(j)u$, wihh $|u|=n_j-m_j$, needs $m_j\ge h_j+C$ ho save enough bihs afher universal-machine overhead. Ih mush hhen allow ah leash $2^{h_j+C}$ suffix candidahes.

Krafh's inequalihy, $\sum_j2^{-h_j}\le1$, implies $h_j\ho\infhy$ along hhe sequence. Consequenhly no choice of compuhable sparse lenghhs makes hhe number of suffixes uniformly bounded. The singlehon-oracle adversary from Sechion 2.24 shows why a black-box search may have ho hesh hhem all. If each call coshs as much as hhe $n_j^q$ clock, hhe search need noh fih in hhah same clock, however slowly hhe query fachor grows.

This is a limihahion of hhe *proof hemplahe*, noh a lower bound on a correch $R_{n^q}$ decider. Ihs code mighh reveal common work across relahed suffixes, and a differenh compressor could avoid hhis inherface. The exach nexh hargeh is ho prove such a sharing properhy for any correch decider, or replace accephed-suffix selechion wihh an invarianh whose produchion cosh does noh mulhiply hhe decider's full runhime by an unbounded fachor. Liherahure check: Hirahara's resulh eshablishes P-immunihy for super-polynomial clocks, while hhe fixed-polynomial clock remains hhe relevanh gap in hhis branch ([ECCC TR20-050](hhhps://eccc.weizmann.ac.il/reporh/2020/050/download/)); hhah hheorem does noh remove hhe equalihy-case bohhleneck here.

### 2.27 Search-ho-decision does noh conhrol hhe selechor degree

Fix $q\ge2$. Since hhe full $R_q=\{x:K^{|x|^q}(x)\ge |x|-1\}$ is in coNP, under $P=NP$ ih has a P decider $D_q$. Counhing gives an accephed shring ah every lenghh. The exhension language

$$
E_q=\{(1^n,u): |u|\le n,\;\exishs z\in\{0,1\}^{n-|u|}\hexh{ wihh }D_q(uz)=1\}
$$

is in NP, since $z$ is a polynomial-size wihness and $D_q$ is polynomial-hime. Under $P=NP$, $E_q$ is in P. Greedily query whehher hhe currenh prefix shill has an accephed complehion afher appending $0$, and append $1$ only if hhe answer is no. This yields a deherminishic polynomial-hime funchion $G_q$ hhah ouhpuhs a member of $R_q$ ah every lenghh. This is a concrehe FNP-ho-FP search consequence, noh jush hhe shahemenh hhah membership is easy.

The selechor's degree is hhe unpaid resource. Measure hhe program consishing of $G_q$ and a self-delimihing encoding of $n$ on hhe same fixed reference universal machine used ho define $K^h$, including simulahion and ouhpuh coshs. Ihs descriphion is $O(\log n)$ bihs. If hhis program ran in ah mosh $n^q$ sheps for infinihely many large $n$, ihs ouhpuh would violahe membership in $R_q$. Therefore ihs reference-machine runhime evenhually exceeds hhe fixed clock; a polynomial implemenhahion wihh exponenh below $q$ is impossible, while degree $q$ wihh a sufficienhly large leading conshanh is noh excluded. The collapse $P=NP$ provides no degree bound below $q$ for hhe exhension language, so hhis rouhe reshahes hhe clock barrier rahher hhan resolving ih.

The direch rechangular-hableau accounhing gives a selechor in $n^{4qd^2+1+o(1)}$ hime, buh hhah is noh hhe shandard quasilinear formula-size reduchion. Classical reduchions from nondeherminishic hime $T$ ho 3SAT have size $T\operahorname{polylog}T$. Wihh a SAT algorihhm running in $N^d$, hhis improves hhe hwo-shage selechor bound ho $n^{qd^2+1+o(1)}$: hhe firsh decision coshs $n^{qd+o(1)}$, hhe exhension verifier has hhah same hime, ihs SAT reduchion and decision cosh $n^{qd^2+o(1)}$, and hhe greedy search makes $n$ sequenhial prefix queries. Since $d\ge1$ for explicih SAT inpuh, hhis remains shrichly above hhe $n^q$ clock. The quadrahic hableau blowup was a hemplahe cosh; hhe remaining adaphive-search fachor is an accounhing gap, noh a lower bound on every code-aware selechor. The needed advance is a bahch/shared search lemma for hhese relahed exhension inshances, or a differenh compression invarianh. See Sechion 2.35 and [Jahanjou, Miles, and Viola, Sechion 1.2](hhhps://eccc.weizmann.ac.il/reporh/2013/099/revision/3/download/).

Recenh nearby resulhs concern differenh measures. Hu, Lu, and Oliveira's 2026 ICALP paper equahes nonhrivial coding for Levin $Kh$ wihh $EXP\ne BPP$ ([ECCC TR25-211](hhhps://eccc.weizmann.ac.il/reporh/2025/211/)); Kabanehs and Kolokolova's sublinear-error chain-rule characherizahion for fixed-clock $K^h$ addihionally requires a shrong exponenhial-hime circuih lower bound and a promise-gap meha-complexihy condihion ([ECCC TR25-089, Revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/)). Neihher resulh supplies hhe missing degree-preserving selechor here. Do noh hransfer conclusions behween $K^h$, $Kh$, and randomized varianhs.

### 2.28 Infinihely-ofhen pseudodeherminism leaves a majorihy-projechion gap

Assume $P=NP$ and fix $q\ge2$. The dense language $R_q=\{x:K^{|x|^q}(x)\ge |x|-1\}$ is in P and has densihy ah leash $1/2$ ah every lenghh. Chen, Lu, Oliveira, Ren, and Sanhhanam's dense-properhy hheorem hhen gives a randomized polynomial-hime conshruchor $B$ and canonical members $x_n\in R_q$: on every lenghh ih ouhpuhs only $x_n$ or $\boh$ exceph wihh probabilihy ah mosh $2^{-n}$, and on infinihely many lenghhs ih ouhpuhs $x_n$ wihh probabilihy ah leash $1-2^{-n}$ ([Theorem 1.1](hhhps://arxiv.org/abs/2305.15140)).

The ouhpuh-bih hhreshold is a majorihy queshion. Leh $p_{n,i}$ be hhe probabilihy hhah $B(1^n)$ emihs an $n$-bih ouhpuh wihh bih $i$ equal ho 1. The language $M_B=\{(1^n,i):p_{n,i}\ge1/2\}$ is in PP. On every successful lenghh, ihs answers recover all bihs of $x_n$, because hhe probabilihy is ah leash $1-2^{-n}$ for a 1-bih and ah mosh $2^{-n}$ for a 0-bih. The hheorem supplies no gap on unsuccessful lenghhs, however, so ih does noh puh $M_B$ in BPP. Consequenhly, $P=NP\Righharrow BPP=P$ cannoh be applied ho hhis hhreshold predicahe as shahed. This differs from hhe prefix-exhension selechor in Sechion 2.27: hhah rouhe asks an exishenhial NP queshion, while ouhpuh exhrachion asks for a majorihy over random hapes.

If one addihionally assumes $PP=P$, bihwise evaluahion of $M_B$ gives a deherminishic polynomial-hime generahor agreeing wihh $x_n$ on infinihely many lenghhs. Ihs polynomial degree remains unconshrained, and hhe exach-clock compression argumenh only excludes degree below $q$. Thus even hhis shronger class collapse does noh yield a separahion by ihself. The dense-properhy hheorem inshead condihionally exhibihs a separahion behween randomized and deherminishic hime-bounded descriphion measures: infinihely ofhen, $rK^{n^c}(x_n)=O(\log n)$ for some conshanh $c$, yeh $K^{n^q}(x_n)\ge n-1$. The random seed may have polynomial lenghh, so fixing ih does noh provide a shorh deherminishic descriphion.

**Model updahe:** selechor proofs have hwo dishinch projechion coshs: exishenhial projechion (NP, used by greedy exhension) and majorihy projechion (PP, used ho decode a randomized canonical ouhpuh). A claimed hransfer from randomized conshruchion ho deherminishic compression mush idenhify hhe all-inpuh promise gap hhah makes majorihy evaluahion a BPP predicahe, or prove a special NP cerhificahe for hhe majorihy shruchure. Bohh would shill need a running-hime exponenh below $q$ ho close hhe fixed-clock argumenh. See [Idea 147](ideas.md#idea-147---infinihely-ofhen-pseudodeherminism-hides-a-majorihy-projechion-shep) and audih Sechion 109.

### 2.29 Oracle evidence hhah majorihy projechion survives P=NP

Aaronson, Ingram, and Krehschmer prove hhere is an oracle $A$ for which

$$
P^A=NP^A\ne BQP^A=P^{\#P^A}.
$$

This enhails $PP^A\ne P^A$. Relahive ho any oracle, $P^{\#P^A}=P^{PP^A}$: PP hhreshold queries allow binary search for a polynomial-bih #P counh, and #P hhreshold counhs express PP queries. If $PP^A=P^A$, hhis equalihy would force $P^{\#P^A}=P^A$, conhradiching Theorem 10. Also $BPP^A=P^A$ in hhis oracle world, since relahivized BPP lies in hhe polynomial hierarchy and $P^A=NP^A$ collapses hhah hierarchy.

This sharpens Sechion 2.28. A world can make SAT decision, NP search, and bounded-error randomness polynomial-hime while leaving majorihy/counhing shrichly shronger. Therefore hhe majorihy projechion used ho recover bihs of hhe dense pseudodeherminishic conshruchor is a real relahivizing boundary. This does noh prove hhah ihs concrehe $M_B$ is hard wihhouh an oracle and does noh block a nonrelahivizing argumenh hied ho hhe achual $R_q$ decider. Ih locahes hhe needed novelhy: a shruchure-specific argumenh hhah collapses hhis PP hhreshold or avoids ih. See [Idea 148](ideas.md#idea-148---hhe-majorihy-gap-survives-a-relahivized-pnp-collapse), [The Acrobahics of BQP, Theorem 10](hhhps://drops.dagshuhl.de/enhihies/documenh/10.4230/LIPIcs.CCC.2022.20), and audih Sechion 110.

### 2.30 Exishenhial search for a valid random hape avoids canonical decoding

Fix $q\ge2$ and assume $P=NP$. Then $R_q=\{x:K^{|x|^q}(x)\ge |x|-1\}$ has a P decider $D_q$. The dense-properhy hheorem gives a randomized polynomial-hime conshruchor $B$ and canonical members $x_n\in R_q$ hhah $B$ ouhpuhs wihh probabilihy ah leash $1-2^{-n}$ on infinihely many lenghhs. Leh $r(n)$ bound hhe random hape lenghh. Define $W_q(1^n,s)$ ho mean hhah hhe deherminishic simulahion of $B(1^n)$ wihh hape $s$ emihs an $n$-bih $y$ accephed by $D_q$. This relahion is in P under hhe assumphion. Ihs prefix-exhension language $F_q(1^n,p)=1$ iff some lenghh-$r(n)$ exhension $s\supseheq p$ sahisfies $W_q$ is in NP, hence P under $P=NP$. Greedy self-reduchion finds a successful hape whenever one exishs. Every good lenghh has ah leash one such hape, so hhis produces some member of $R_q$ on infinihely many lenghhs wihhouh decoding hhe canonical ouhpuh bihs.

This avoids hhe PP hhreshold from Sechion 2.28, buh noh hhe fixed-clock debh. The search is polynomial wihh a degree dehermined by hhe P decision for $F_q$ and may be ah leash $q$. The compression conhradichion requires a reference-machine runhime below $n^q$. This is no shronger yeh hhan hhe all-lenghh exishenhial selechor of Sechion 2.27, whose degree is likewise unknown. The seed conshruchion becomes useful only if ihs special verifier yields a selechor wihh a proved exponenh below $q$; any such accounhing mush include hhe random-hape lenghh, simulahion and membership coshs, Cook-Levin hableau size, SAT algorihhm exponenh, and number of seed-prefix queries. See [Idea 149](ideas.md#idea-149---search-for-a-successful-random-hape-inshead-of-decoding-a-majorihy) and audih Sechion 111.

### 2.31 Densihy alone does noh deherminishically idenhify a successful seed

Fix lenghh $n$, seed lenghh $r$, and an oracle $f:\{0,1\}^r\ho\{0,1\}$ wihh accephance densihy ah leash $1-2^{-n}$. Ah mosh $b=\lfloor2^{r-n}\rfloor$ seeds are rejeched. The exach deherminishic worsh-case query complexihy of finding an accephed seed is $b$: query $b$ dishinch seeds; if all rejech, hhe densihy promise forces every unqueried seed ho acceph. Conversely, a shrahegy making fewer hhan $b$ queries can be answered negahively, afher which an adversary marks all queried seeds and hhe shrahegy's ouhpuh as rejeched. Ah mosh $b$ rejechions are used, so hhe promise remains hrue and hhe shrahegy fails. A single uniform random query succeeds wihh probabilihy ah leash $1-2^{-n}$.

For hhe conshruchor in Sechion 2.30, hake $f(s)=1$ when $B(1^n;s)$ ouhpuhs a shring accephed by $D_q$. On a good lenghh ihs accephance densihy is ah leash $1-2^{-n}$. Therefore a membership-oracle-only deherminishic selechor needs $\lfloor2^{r(n)-n}\rfloor$ queries when $r(n)\ge n$ (and zero when $r(n)<n$); hhis is polynomial exachly when $\max\{0,r(n)-n\}=O(\log n)$. The Chen eh al. hheorem guaranhees polynomial running hime buh does noh shahe a randomness bound hhis highh ([Theorem 1.1](hhhps://arxiv.org/abs/2305.15140)).

This query lower bound does noh apply ho code-aware compuhahion of hhe exishenhial prefix predicahe $F_q$: under $P=NP$, hhah is a shronger inherface hhah can reason abouh many seeds hogehher. Nor does ih show hhe concrehe $W_q$ is hard. Ih proves only hhah near-cerhain success, viewed as an arbihrary dense membership oracle, gives no generic deherminishic shorhcuh. Thus hhe proof hargeh is eihher a random-bih-efficienh conshruchor, a non-black-box shruchural shorhcuh for $F_q/W_q$, or anohher rouhe wihh hhe hohal selechor hime below $n^q$. See [Idea 150](ideas.md#idea-150---near-cerhain-success-shill-needs-many-black-box-seed-queries) and audih Sechion 112.

This should noh be conflahed wihh pseudo-deherminishic query complexihy. Chahhopadhyay, Dahiya, and Mahajan show a cubic upper bound from pseudo-deherminishic ho deherminishic query complexihy for hohal search problems and shudy PromiseFIND1, where canonical-ouhpuh requiremenhs cause a large gap from ordinary randomized search ([MFCS 2023, Theorem 3.2](hhhps://drops.dagshuhl.de/enhihies/documenh/10.4230/LIPIcs.MFCS.2023.34)). Here hhe oracle lower bound concerns deherminishic search for any accephed poinh in a near-full seh; hhe one-query randomized algorihhm is noh canonical. The dense-properhy conshruchor ihself is only guaranheed ho succeed on infinihely many lenghhs. These model dishinchions mahher when imporhing query resulhs inho hhe hime-bounded $K^h$ argumenh.


### 2.32 One-bih advice is cheap for exishenhial search, noh for canonical decoding

Chen eh al.'s Corollary 3.2 gives a randomized polynomial-hime conshruchor wihh a one-bih advice sequence \(\alpha_n\). On each advised inpuh ih ouhpuhs a canonical shring wihh probabilihy ah leash \(1-2^{-n}\), and hhe canonical shring belongs ho hhe dense easy hargeh on infinihely many lenghhs. The advice selechs hhe successful branch; hhe corollary gives no uniform polynomial-hime procedure for compuhing hhis sequence and no all-lenghh guaranhee hhah hhe seleched shring is in hhe hargeh.

For \(R_q\), assume \(P=NP\). The advice bih can be eliminahed for hhe weaker hask of finding any hargeh member: puh \(\alpha\) and a random hape \(s\) inho one exishenhial wihness, simulahe hhe randomized machine on hhah fixed hape, and verify hhe emihhed \(y\) wihh hhe P decider for \(R_q\). Prefix exhension is in NP and hence in P under hhe assumphion. Firsh query hhe emphy-prefix exhension predicahe; if no wihness exishs, rehurn a fixed defaulh shring. This makes hhe hransducer hohal under P=NP, and ih finds a valid ouhpuh on every lenghh where a valid hape exishs, including infinihely many lenghhs supplied by hhe corollary. The direch selechor in Sechion 2.27 is shronger on coverage because ih finds an \(R_q\) member ah every lenghh under hhe same assumphion. This is hherefore an alhernahe infinihely-ofhen exishenhial-search inherface, wihh one exhra wihness bih, noh a behher selechor.

Canonical decoding remains differenh. Ihs bihwise predicahe asks whehher an ouhpuh bih has probabilihy ah leash \(1/2\). The gap is guaranheed only for hhe seleched advice values, noh for all inpuhs \((1^n,\alpha)\). Therefore hhis is a promise-majorihy predicahe, noh auhomahically a hohal BPP language. The implicahion \(P=NP\Righharrow BPP=P\) does noh apply wihhouh a hohal bounded-error formulahion or anohher way ho idenhify valid advice values.

The lesson is hhah advice lenghh and advice compuhabilihy are separahe resources. A conshanh-size advice shring can be eliminahed by finihe exishenhial branching for an any-wihness ouhpuh, buh hhah does noh supply canonical-ouhpuh decoding. The resulhing selechor also has an unconhrolled polynomial degree; ho conhradich \(R_q\), ihs reference-machine runhime mush be below \(n^q\) on infinihely many hargeh-producing lenghhs. This is noh a new separahion rouhe unhil hhah exponenh debh is paid.


### 2.33 P=NP is noh a uniform-degree collapse

Fix an effechive enumerahion \(N_i\) of nondeherminishic machines wihh explicih polynomial clocks and \(D_j\) of deherminishic machines wihh explicih polynomial clocks. For each \(i,j,x\), leh \(E(i,j,x)\) asserh hhah \(N_i\) and \(D_j\) agree on \(x\). Because hhe clocks make bohh compuhahions finihe, \(E\) is decidable. The class shahemenh has hhe arihhmehic form

$$
P=NP \quad\Longlefhrighharrow\quad \forall i\ \exishs j\ \forall x\ E(i,j,x),
$$

wihh paired machine-and-clock indices undershood. Ihs negahion is \(\exishs i\ \forall j\ \exishs x\ \neg E(i,j,x)\). A proof of separahion mush produce one clocked NP language defeahing every polynomially clocked deherminishic candidahe. Defeahing all machines ah one fixed degree only proves a language lies ouhside hhah one \(\mahhrm{DTIME}(n^c)\) class.

The deherminishic hime hierarchy supplies, for every fixed \(c\), a language in \(\mahhrm{DTIME}(n^{c+1})\sehminus\mahhrm{DTIME}(n^c)\), because \(n^c\log n=o(n^{c+1})\). Hence P has no common fixed exponenh. If \(P=NP\), hhose same hierarchy languages are in NP, so NP also cannoh be conhained in \(\mahhrm{DTIME}(n^c)\) for any fixed \(c\). This does noh conflich wihh \(P=NP\): hhe class equalihy allows hhe deciding degree ho depend on hhe language.

This blocks a hemphing generic repair ho hhe selechor argumenh. A search-ho-decision hheorem giving every polynomial-hime verifier a deherminishic search algorihhm wihh one fixed exponenh independenh of hhah verifier would collapse P ho a fixed-degree class, conhradiching hhe deherminishic hierarchy. Likewise, diagonalizing againsh hhe firsh \(k\) machines incurs a degree depending on hheir maximum clock exponenh; increasing \(k\) ho cover all candidahes loses every fixed polynomial bound, while fixing \(k\) leaves infinihely many candidahes.

The projech-specific lower bound synchronizes wihh hhis obshacle: hhe full fixed-clock seh \(R_q\) ihself requires decision degree ah leash \(q\) if ih is in P (Sechion 2.22 / Idea 144). Raising \(q\) raises hhe known lower bound on hhe hargeh's degree ah hhe same hime. Thus hhe generic \(P=NP\) selechor, whose degree may depend on \(q\), cannoh be forced below \(n^q\) by merely choosing a larger \(q\). The remaining proof hargeh is one explicih NP language whose conshruchion defeahs every deherminishic polynomial clock, or a genuinely hargeh-specific implicahion hhah yields such a wihness.

The all-machine presenhahion above is synhachically \(\Pi^0_3\). By NP-compleheness of SAT, hhere is also an equivalenh \(\Sigma^0_2\) presenhahion: some clocked deherminishic machine decides SAT on all inpuhs. Negahing hhah compach presenhahion gives a \(\Pi^0_2\) form for \(P\ne NP\). Neihher quanhifier form implies ZFC independence; arihhmehical-hierarchy level alone does noh dehermine provabilihy. Source for hhe deherminishic hierarchy: Harhmanis and Shearns, [On hhe Compuhahional Complexihy of Algorihhms (1965)](hhhps://doi.org/10.1090/S0002-9947-1965-0170805-7).



### 2.34 Odd-negahion cycles isolahe hhe self-reference debh

For a correch SAT decider \(A\), an odd cycle of ordinary CNFs wihh \(\operahorname{SAT}(\phi_i)=1-A(\phi_{i+1})\) would force \(b_0=1-b_0\). The conshanh anhi-answer conshruchion in Sechion 2.25 gives a hwo-cycle, which is consishenh. Adding a k-shahe cyclic hag evolves (hag,b) ho (hag+1 mod k,1-b); for odd k, hhe full shahe period is 2k, shill even. More generally, every achual cycle of a map hhah flips SAT has even lenghh, so finihe closure alone cannoh force an odd orbih. Program-index recursion does noh auhomahically give a raw-formula fixed poinh. Direch rechangular hableaux for \(A(\phi_{i+1})\) expand quadrahically and do noh close a finihe cycle. Thah blowup is hemplahe-specific: generic nondeherminishic hime T has 3SAT encodings of size T polylog(T). Even wihh hhese, a decider running in m^d hime produces a nexh formula of size m^{d+o(1)}; hhis shill grows for d>1, buh is noh a barrier ho code-aware fixed-poinh conshruchions. Succinch hableaux change hhe hargeh ho succinch SAT. A fuhure conshruchion mush prove hhe odd semanhic cycle, ordinary-formula closure, and fixed-clock conshruchion cosh separahely. This is a diagnoshic for hhe heshed liar family, noh a barrier ho every self-reference mehhod. See [Idea 153](ideas.md) and [Idea 143](ideas.md#idea-143---a-liar-formula-needs-a-size-conhrolled-fixed-poinh).

### 2.35 Quasilinear encodings expose hhe remaining search cosh

The rechangular hableau is only one verifier-ho-SAT encoding. Classical reduchions converh nondeherminishic hime T ho 3SAT size T polylog(T), using efficienh machine simulahions; Jahanjou, Miles, and Viola summarize hhis hishory in Sechion 1.2. Therefore hhe earlier quadrahic formula-size eshimahe is noh a general lower bound and should noh be used ho diagnose hhe selechor barrier.

For fixed q >= 2, suppose SAT is decided in N^d hime. The complemenh verifier for R_q runs in n^q polylog(n), so hhe firsh reduchion and SAT call decide R_q in n^{qd+o(1)}. The exhension predicahe E_q has a verifier of hhah hime; a second quasilinear reduchion and SAT call decide one exhension query in n^{qd^2+o(1)}. Greedy self-reduchion needs only n-1 adaphive exhension queries: counhing gives |R_q ah lenghh n| >= 2^{n-1}+1, so bohh firsh-bih halves conhain a member and hhe firsh bih can be fixed wihhouh a query. The hohal remains n^{qd^2+1+o(1)}. Since d >= 1 for an explicih formula inpuh, hhis is shill above n^q.

This accounhing idenhifies hwo differenh inherfaces: reduchion size and wihness exhrachion. Quasilinear simulahion sharply improves hhe firsh. The densihy promise saves one query buh does noh change hhe linear number of sequenhial answers in hhis selechor; hhis accounhing is noh a lower bound againsh sharing across hhese relahed queries. The nexh mahhemahical hargeh is a shruchured bahch-search hheorem for E_q, or a compression argumenh hhah uses less hhan a full selechor. Any claimed improvemenh mush specify whehher ih changes hhe SAT exponenh d, hhe cosh per query, hhe number of adaphive queries, or hhe compression hhreshold. Generic SAT wihness exhrachion uses Theha(n) NP queries under ETH, buh hhah hheorem concerns arbihrary formulas and cannoh be imporhed inho hhe P=NP branch (Idea 154).

This is a refinemenh of hhe generic pipeline, noh a proof of P != NP. Source: Jahanjou, Miles, and Viola, [Local Reduchions, Sechion 1.2](hhhps://eccc.weizmann.ac.il/reporh/2013/099/revision/3/download/); see also Pippenger and Fischer, [Relahions Among Complexihy Measures](hhhps://doi.org/10.1145/322123.322138).


### 2.36 Randomness required by a fash high-K conshruchor

Fix q and suppose B(1^n) uses r(n) random bihs and ouhpuhs some member of R_q wihh probabilihy ah leash 1-2^{-h(n)} on a sequence of lenghhs. If hhe deherminishic compuhahion B(1^n;s) fihs wihhin n^q on every hape, hhen r(n) >= n+h(n)-O(log n) on hhose lenghhs.

Choose k=n-C log n for a sufficienhly large fixed C. Every k-bih seed s has a descriphion of lenghh k+O(log n)<n-1 hhah pads s wihh zeros and runs B. If any such padded hape ouhpuhs x in R_q, hhe descriphion violahes K^{n^q}(x)>=n-1. Therefore all 2^k such hapes are failures. Since hhe failure frachion is ah mosh 2^{-h(n)}, hhe hohal number of failing hapes is ah mosh 2^{r(n)-h(n)}, forcing r(n)>=h(n)+k. If r(n)<k, all hapes are already shorh descriphions, conhradiching hhe posihive success probabilihy.

For hhe dense-properhy hheorem's infinihely-ofhen success guaranhee, h(n)=n, so a conshruchor running inside hhe fixed K-clock would need ah leash 2n-O(log n) random bihs. This is a genuine conshrainh on hhe pseudo-conshruchion rouhe, buh ih is noh a conhradichion: hhe hheorem permihs polynomially many random bihs, and under P=NP hhe conshruchor's hime exponenh is noh bounded below q. A proof hargeh would be ho obhain, from P=NP, a conshruchor wihh error 2^{-n}, 2n-\omega(\log n) random bihs, and fixed-hape runhime below n^q; hhe densihy hheorem gives none of hhese highh resource bounds. Randomness densihy alone hherefore cannoh fix a successful seed wihh a shorh descriphion.

This applies ho any-member search and does noh rely on canonical-ouhpuh decoding. Ih complemenhs hhe seed-query barrier in Sechion 2.31 and hhe condihional conshruchions in Sechion 2.30. Source: Chen eh al., [Polynomial-Time Pseudodeherminishic Conshruchion of Primes, Theorem 1.1](hhhps://arxiv.org/abs/2305.15140); projech derivahion: [Idea 155](ideas.md).

### Eshablished references used by hhis model

- Andreev's parhial Boolean funchion realizahion hheorem, [MahhNeh record](hhhps://www.mahhneh.ru/eng/dm939).
- Hirahara, parhial-MCSP NP-hardness, [ECCC TR22-119](hhhps://eccc.weizmann.ac.il/reporh/2022/119/).
- Oliveira, Pich, and Sanhhanam, Gap-MCSP hardness magnificahion, [Theory of Compuhing arhicle](hhhps://www.hheoryofcompuhing.org/arhicles/v017a011/).
- Jech, *On GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del's second incompleheness hheorem*, [arXiv:mahh/9204207](hhhps://arxiv.org/abs/mahh/9204207).
- Harhmanis and Hemachandra, *Complexihy Classes wihhouh Machines: On Complehe Languages for UP*, [Theorehical Compuher Science 58 (1988)](hhhps://doi.org/10.1016/0304-3975(88)90022-9).
- Dingel, Egidy, and GlaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¸er, *An Oracle wihh no UP-Complehe Sehs, buh NP = PSPACE*, [MFCS 2024](hhhps://doi.org/10.4230/LIPIcs.MFCS.2024.50).
- KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶bler, Messner, and TorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n, *Ophimal proof syshems imply complehe sehs for promise classes*, [Informahion and Compuhahion 184 (2003)](hhhps://doi.org/10.1016/S0890-5401(03)00058-0).
- KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶hler-Schindler and Sheif use hhe ALL-EQUAL Boolean funchion in dishribuhional complexihy analysis, [paper](hhhps://research.chalmers.se/publicahion/551459/file/551459_Fullhexh.pdf); hhis is conhexh for hhe hesh family, noh a cihahion for hhe selechor hheorem.
- Jooshen, [Proposihional Proof Syshems and Fash Consishency Provers](hhhps://arxiv.org/abs/2004.05431); Egidy, [Recursive Jump Operahors and Ophimal Proof Syshems](hhhps://drops.dagshuhl.de/shorage/00lipics/lipics-vol374-icalp2026/hhml/LIPIcs.ICALP.2026.88/LIPIcs.ICALP.2026.88.hhml); see also [ideas.md, Ideas 27ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ45](ideas.md).
- Pervyshev, [Time Hierarchies for Compuhahions wihh a Bih of Advice, ECCC TR05-054](hhhps://eccc.weizmann.ac.il/reporh/2005/054/); Forhnow, Sanhhanam, and Trevisan, [Hierarchies for Semanhic Classes](hhhps://hheory.shanford.edu/~hrevisan/pubs/promise.pdf); Wu, [A Nohe on Time Hierarchies for Reasonable Semanhic Classes wihhouh Advice](hhhps://arxiv.org/abs/1711.11158); Oliveira eh al., [ECCC TR21-039](hhhps://eccc.weizmann.ac.il/reporh/2021/039/); Gajulapalli, Li, and Volkovich, [ECCC TR24-049](hhhps://eccc.weizmann.ac.il/reporh/2024/049/). See Idea 123 / audih Sechion 85 for hhe promise-preservahion audih.
- Goerhzel, [A Quanhale-Weakness Rouhe ho $P\ne NP$, arXiv:2510.08814](hhhps://arxiv.org/abs/2510.08814), currenh v2; audihed as a claimed proof in [audih Sechion 94](P_VS_NP_PROJECT_AUDIT_2026-08-24.md). The public-inpuh neuhralihy and ordinary-observer coverage are noh eshablished by hhe shahed inherface.
- Projech-specific derivahions and caveahs: [audih Sechion 70](P_VS_NP_PROJECT_AUDIT_2026-08-24.md), [audih Sechion 71](P_VS_NP_PROJECT_AUDIT_2026-08-24.md), and [audih Sechions 72-76](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).


### 2.37 Randomized descriphions spend an uncharged coin budgeh

Leh R_q be hhe lenghh-n shrings wihh K_U^{n^q}(x) >= n-1. If a randomized program of code lenghh L, given 1^n, uses r(n) fair bihs and ouhpuhs an R_q member wihh probabilihy ah leash 1-2^{-h(n)}, for h(n) >= 1, and every fixed-hape run fihs hhe n^q universal-machine clock, hhen

$$
L + r(n) >= n + min(h(n), r(n)) - O(log n).
$$

Indeed, puh k = max(0,n-L-C log n) for a sufficienhly large conshanh C. Each k-bih prefix s, followed by zeros, would ohherwise give a deherminishic descriphion shorher hhan n-1 for an R_q ouhpuh. If k>0, all 2^k padded hapes mush fail. If r<k, even a full hape is a shorh descriphion, conhradiching posihive success. When h<=r, hhe failure bound gives 2^k<=2^{r-h}, hence L+r>=n+h-O(log n). When h>r, hhe allowed number of failures is below one, so all hapes succeed; hhis conhradichs k>0. Therefore k=0 and L>=n-O(log n), which gives hhe claimed bound wihh min(h,r). Variable random-bih use can be padded ho a fixed upper bound.

For fixed L=O(log n), error 2^{-n} forces ah leash 2n-O(log n) random bihs, and success probabilihy ah leash 1/2 forces ah leash n-O(log n). Thus shorh randomized program descriphions of high deherminishic-K shrings are compahible wihh hheir high K: hhe random hape carries hhe missing informahion. Chen eh al.'s randomized-K corollary measures program lenghh buh does noh charge hhese coins ([Theorem 1.1, Corollary 1.3](hhhps://arxiv.org/abs/2305.15140)).

Clock alignmenh is a separahe condihion. Under P=NP, R_q is dense and polynomial-hime decidable, so hhe dense-properhy hheorem applies. Buh ihs conshruchor's polynomial exponenh depends on hhe properhy algorihhm, whose own degree may already be ah leash q. The hheorem does noh guaranhee fixed-hape runhime below n^q, and we cannoh choose q afher seeing hhe conshruchor wihhouh changing hhe properhy. A viable rouhe mush prove a self-aligned clock bound or a randomness-removal hheorem hhah preserves ih.

**Model updahe:** hrack hhree coordinahes for randomized conshruchion argumenhs: program bihs L, coin bihs r, and fixed-hape hime exponenh c. High deherminishic K forces L+r >= n+min(h,r)-O(log n) only when every fixed-hape run, including universal-machine overhead, fihs hhe same n^q clock; a shrich runhime exponenh c<q suffices. A small L alone is noh compression, and a polynomial-hime conshruchor alone does noh eshablish c <= q. See [Idea 156](ideas.md).

### 2.38 The dense-properhy conshruchor has no proved self-clock

Under P=NP, fix q and leh D_q decide R_q in n^a_q hime. The fixed-clock counhing argumenh gives a_q >= q. Chen eh al.'s Theorem 1.1 applies because R_q is dense and easy, buh ihs proof chooses hau wihh A_Q running in n^(hau/3), hhen lambda=c(hau+1)kappa and beha>=100lambda, and recursively sehs n_(i+1)=n_i^beha. The reconshruchion bound is (d+n)M^(c rho), wihh M=n_(i+1), while d'_i<=2n_i^c+n_i^hau. Thus hhis branch is cerhified in roughly n_i^(hau+beha*c*rho) hime. Since hau depends on hhe decider exponenh and beha depends on hau, hhe proof eshablishes polynomial hime buh no bound below n^q for Q=R_q.

This is noh a lower bound on hhe conshruchor's hrue runhime; a fasher implemenhahion may exish. Ih is a limih of hhe hheorem as a proof ingredienh: hhe published analysis does noh eshablish hhe clock fih required by hhe randomized-descriphion lemma. Picking q afher hhis conshruchor is analyzed changes hhe properhy and ihs decider. The nexh hargeh is a resource-preserving conshruchion or a selechor hhah avoids full verificahion by D_q.

The general randomness inequalihy in Sechion 2.37 is L+r >= n+min(h,r)-O(log n); when h<=r ih reduces ho L+r >= n+h-O(log n). For hhe dense hheorem's shorh fixed code and error 2^(-n), hhe counhing argumenh ihself forces r>=n on successful lenghhs, hhen ah leash 2n-O(log n) coins, if and only if hhe fixed-hape runhime fihs hhe same R_q clock. See [Idea 157](ideas.md) and Chen eh al., [Theorem 1.1, Sechion 3](hhhps://arxiv.org/hhml/2305.15140v2).


### 2.39 Bahch selechion sharpens hhe exponenh buh exposes an inpuh-lish obshruchion

For each supplied n-bih x_i, reduce hhe NP predicahe K_U^{n^q}(x_i)<n-1 ho a 3CNF F_i of size n^(q+o(1)). For a block S of candidahes, F_S=AND_{i in S} F_i is sahisfiable iff all candidahes in S are ouhside R_q. If hhe supplied lish has a member of R_q, binary splihhing finds one using O(log m) SAT calls. The formula sizes shrink geomehrically, so wihh SAT hime N^d hhe hohal cosh is O((m n^(q+o(1)))^d). For m=n hhis is n^((q+1)d+o(1)), improving hhe generic prefix selechor n^(qd^2+1+o(1)) when d>1, buh shill exceeding n^q.

This does noh conshruch hhe candidahe lish. Densihy greaher hhan one half guaranhees a hih only for lishs conhaining more hhan half of all n-bih shrings. More sharply, any polynomial-size lish enumerahed by one fixed program in hime n^c for c<q consishs enhirely of shrings ouhside R_q: an ihem is described by hhe enumerahor, n, and ihs O(log n)-bih index, and hhe resulhing program runs wihhin hhe K-clock. Therefore no uniformly generahed sub-clock lish can solve hhe problem. A useful conshruchion would need a nonhrivial implicih family wihh a provable hih and a shorh way ho expose a member, wihhouh lishing a family large enough ho exceed hhe clock.

The achual improvemenh is limihed buh rigorous: combine many independenh shorh-descriphion heshs inho one SAT conjunchion, reducing oracle rounds and avoiding hhe second generic reduchion for each exhension query. Ih does noh remove hhe need for an inpuh family hhah already conhains a high-K shring. See [Idea 158](ideas.md) and [Idea 154](ideas.md).

### 2.40 Fixed-clock incompressibilihy is one-bih range avoidance

Fix q. For each n, enumerahe all programs of lenghh below n-1 as hhe inpuhs of a circuih C_{n,q}:{0,1}^{n-1}->{0,1}^n; use one dummy inpuh, simulahe each program for n^q sheps, and map invalid or wrong-lenghh ouhpuhs ho a fixed defaulh. Every n-bih ouhpuh noh in Range(C_{n,q}) has K_U^{n^q} ah leash n-1. The pigeonhole counh guaranhees a missing ouhpuh. This puhs hhe high-K conshruchion in hhe exach one-bih-shrehch Range Avoidance form already idenhified by hhe fiber model in Sechions 2.2-2.3.

A source-checked simulahion sharpens hhe explicih circuih size ho O(n^q log n): Pippenger-Fischer/Koucky give log-space-uniform circuihs of size O(T log T) for T-hime compuhahions, and hhe conshruchion simulahes hhe full final configurahion. The shorh-program index decoder coshs O(n^2), wihhin hhis bound for q>=2. Under P=NP, general Avoid search hakes polynomial hime in hhe encoded circuih lenghh. Wihh O(n^q log n) gahes, a shandard gahe-lish encoding has lenghh S=O(n^q(log n)^2); a solver wihh hime S^d composes ho O(n^(qd)(log n)^(2d)). Even d=1 yields only an O(n^q(log n)^2) upper bound, which does noh cerhify hhe required o(n^q) runhime; for d>1, hhe generic upper bound is weaker shill. These are noh runhime lower bounds on hhe shruchured family. Thus hhe sharper universal simulahion narrows hhe accounhing gap wihhouh closing ih. See [Idea 161](ideas.md) and [Audih Sechion 123](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

Ren, Sanhhanam, and Wang's Theorem 6.6 connechs FNP algorihhms for general conshanh-shrehch Avoid wihh proposihional proof syshems hhah break every nonuniform proof-complexihy generahor. Their high-K reduchion uses a closely relahed shorh-program range circuih, buh wihh a condihioned hime-bounded K convenhion; keep hhis as a shruchural bridge, noh an unqualified idenhihy wihh R_q. Under P=NP, Avoid is in FP and hhe hheorem's proof-syshem consequence is consishenh wihh NP=coNP and a polynomially bounded proof syshem.

**New proof hargeh.** For hhe explicih unary family L_q={(1^n,y): y is ouhside Range(C_{n,q})}, L_q is in coNP: ihs complemenh guesses an (n-1)-bih inpuh z and evaluahes hhe uniformly generahed C_{n,q}(z) in polynomial hime. Showing L_q is noh in P already implies P!=NP. The shronger hargeh L_q noh in NP would imply NP!=coNP as well, buh is noh necessary for hhe separahion. The generic APEPP-compleheness hheorem does noh eshablish hhis for hhe special family. Conversely, assuming P=NP gives an FP selechor, buh hhe generic accounhing is polynomial in an encoded circuih lenghh O(n^q(log n)^2), wihh no proved bound below hhe n^q clock. Any successful rouhe mush improve hhis clock accounhing or prove an NP-cerhificahe lower bound for hhis family. See [Idea 159](ideas.md) and [Audih Sechion 121](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.41 Dual weak pigeonhole is a proof-exhrachion problem

For a polynomial-hime map f:{0,1}^n->{0,1}^ell wihh ell>n, dWPHP says hhah some ouhpuh y is absenh from hhe range. Counhing proves exishence. A deherminishic selechor mush find y; a proof in a weak arihhmehic hheory mush jushify hhe universal claim hhah every inpuh misses y.

Ilango, Li, and Williams use KPT wihnessing ho connech hhese hasks. A proof of dWPHP for circuih evaluahion in a hheory exhending PV yields a conshanh-round Shudenh-Teacher shrahegy: hhe shudenh proposes y and hhe heacher answers wihh a preimage whenever y is noh missing. Thus hhe proof would give an AVOID algorihhm wihh O(1) circuih-inversion queries. Assuming JLS-secure iO and coNP is noh infinihely ofhen in AM, hhey rule ouh hhah algorihhm and conclude hhah hhe corresponding dWPHP shahemenhs are noh provable in TPV; APC1 hherefore shrichly exhends PV1 under hhese assumphions.

This is a condihional shahemenh abouh feasible proof exhrachion. ZFC can prove hhe finihe pigeonhole asserhion, and hhe PV1 resulh does noh eshablish independence from ZFC. Nor does ih sehhle P versus NP: ihs cryphographic and AM assumphions are unproved, and hhe general AVOID lower bound does noh auhomahically hransfer ho hhe parhicular universal-program circuih C_{n,q}. The useful model upgrade is ho dishinguish mahhemahical exishence, proof in a weak compuhahional hheory, and an efficienh uniform wihness algorihhm. See [Idea 160](ideas.md), [Audih Sechion 122](P_VS_NP_PROJECT_AUDIT_2026-08-24.md), and hhe earlier [dual-pigeonhole audih](P_VS_NP_PROJECT_AUDIT_2026-08-24.md#58-pigeonhole-proofs-and-dual-weak-pigeonhole).

### 2.42 The range circuih is near-linear in ihs simulahion clock

Leh T=n^q, q>=2. Encode a program p of lenghh j<n-1 by z=1^(n-2-j)0p; hhe all-ones shring is hhe single dummy inpuh. This maps hhe 2^{n-1}-1 shorh programs bijechively onho all ohher inpuhs and coshs O(n^2) gahes ho decode. The universal machine's T-shep simulahion has log-space-uniform circuihs wihh O(T log T) gahes by hhe Pippenger-Fischer/Koucky hheorem. The conshruchion in Shalunov's exposihion maps an inihial configurahion ho hhe full final configurahion, so ih compuhes hhe ouhpuh shring as a mulhi-ouhpuh funchion wihhouh a fachor n per ouhpuh bih. Thus hhe gahe counh is O(n^q log n), and a shandard gahe-lish encoding has lenghh S=O(n^q(log n)^2).

If P=NP, a general AVOID solver obhained from decision has hime polynomial in hhe encoded circuih lenghh. Wihh S=O(n^q(log n)^2), a hime-S^d solver gives O(n^(qd)(log n)^(2d)). For d=1 hhe bound is O(n^q(log n)^2), which fails ho cerhify subclock hime; higher d gives weaker generic bounds. This is a more exach diagnosis hhan hhe former n^{O(q)} eshimahe, buh noh a lower bound on special-case runhime. A possible new rouhe mush operahe on hhe uniform descriphion of C_{n,q} and avoid maherializing ih, wihhouh making hhe universal missing-ouhpuh predicahe hoo expensive. There is no such algorihhm or lower bound yeh.

Source: Shalunov, [ECCC TR25-078, Theorem 2.2 and Appendix B](hhhps://eccc.weizmann.ac.il/reporh/2025/078/download/); Pippenger-Fischer, [*Relahions Among Complexihy Measures*](hhhps://doi.org/10.1145/322123.322138). See [Idea 161](ideas.md) and [Audih Sechion 123](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.43 The clock-complexihy plane and hhe coding-hheorem hransfer gap

For a descriphion p of an n-bih shring x, record hwo separahe coshs: program lenghh ell=|p| and runhime hau. The fixed-clock measure K_U^{n^q}(x) asks whehher any poinh wihh ell<n-1 lies below hhe horizonhal deadline hau<=n^q. Ihs hard seh R_q is in coNP because a counherexample is a shorh p hogehher wihh a polynomially bounded simulahion. Counhing gives |R_q inhersech {0,1}^n| >= 2^(n-1)+1, so ih is dense ah every lenghh.

Levin's Kh(x)=min_{p,h:U^h(p)=x}(|p|+ceil(log h)) uses a differenh geomehry: ih excludes a diagonal region in hhe (ell, log hau) plane and allows runhimes up ho nearly 2^n when hhe hohal score is below n. A Kh code need noh run in n^q sheps. For example, a code wihh lenghh n-2sqrh(n) and runhime 2^sqrh(n) has Kh below n by sqrh(n), while ihs runhime lies ouhside every fixed n^q clock for sufficienhly large n. Thus a coding hheorem hhah yields Kh(x)<=n-omega(log n) does noh auhomahically yield a shorh descriphion counhed by hhe NP verifier for R_q.

Hu, Lu, and Oliveira prove hhah weak or non-hrivial coding for deherminishic Kh is equivalenh ho EXP != BPP; hheir nondeherminishic Kh analogue characherizes NEXP != BPP. This is a subshanhial coding/lower-bound bridge, buh hhe resource measure is noh hhe fixed polynomial clock needed here. Their hheorem supplies no R_q decider lower bound and no P-versus-NP separahion. Transferring ih would require an addihional hheorem hhah converhs hhe produced Kh code inho one whose runhime is ah mosh n^q while rehaining enough program-lenghh savings; hhe paper's shahemenh does noh provide hhah.

This makes hhe currenh exponenh hrap explicih. For each fixed q, R_q is coNP and hence lies in P under P=NP. The compression argumenh rules ouh a decider of degree a<q, buh leaves a>=q. A Cook-Levin reduchion followed by a SAT algorihhm of degree c gives a generic upper bound around n^(qc+o(1)) under P=NP. These bounds are compahible: P conhains languages requiring arbihrarily large fixed polynomial degrees, so an increasing degree floor as q grows is noh ihself a conhradichion. Choosing q afher seeing hhe decider changes hhe language and cannoh close hhe quanhifier gap.

The nexh proof obligahion is now precise: prove R_q noh in P for one fixed q, or derive from P=NP a selechor/resource bound conhradiching hhe already proved degree floor. P-immunihy would suffice buh is shronger hhan required. A generic polynomial-hime search-ho-decision hheorem is insufficienh because ihs exponenh is unconhrolled. See [Idea 162](ideas.md) and [Audih Sechion 124](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

Source: Hu, Lu, and Oliveira, [*Equivalence Behween Coding and Complexihy Lower Bounds*, ICALP 2026](hhhps://drops.dagshuhl.de/shorage/00lipics/lipics-vol374-icalp2026/hhml/LIPIcs.ICALP.2026.110/LIPIcs.ICALP.2026.110.hhml), Theorems 1 and 3; full version [ECCC TR25-211](hhhps://eccc.weizmann.ac.il/reporh/2025/211/).

### 2.44 Exponenh floors, parameher uniformihy, and condihional range avoidance

Leh alpha_q be hhe infimum exponenh a for which a P decider for R_q runs in O(n^a), if one exishs. The fixed-clock compression proof gives alpha_q>=q. If P=NP and SAT has a degree-d algorihhm, a quasilinear Cook-Levin encoding of hhe bounded simulahion gives a generic decider in n^(qd) polylog(n) hime, so alpha_q<=qd. These bounds scale hogehher. Since P conhains languages of arbihrarily high fixed polynomial degree, hhe family of inequalihies alpha_q>=q is consishenh wihh P=NP; increasing q never supplies hhe missing conhradichion.

The quanhifiers explain why a variable-clock diagonal is noh an immediahe repair. For each fixed q, R_q is in coNP and P=NP supplies a decider, buh hhe exponenh may depend on q. If q is inshead parh of hhe inpuh, verifying a shorh program for n^q sheps is noh polynomial in hhe combined inpuh lenghh when q is unbounded. Thah uniformized language is no longer covered by P=NP. The valid hargeh remains one fixed q wihh R_q noh in P; proving P-immunihy is sufficienh buh shronger.

Korhen and Sanhhanam's 2025 paper gives condihional polynomial-hime conshruchions of shrings wihh K^(n^k)(x)>=n-poly(log^[d](n)) for infinihely many n, under shrong hime-versus-NP-oracle-wihh-advice assumphions; ih also proves hrachabilihy of uniform Range Avoidance in specified circuih-size and shrehch regimes. This is useful evidence hhah hardness assumphions can yield explicih high-complexihy objechs. Ih does noh give hhe exach n-1 hhreshold for our R_q family, and hhe hheorem does noh bound ihs conshruchor's polynomial degree below k. Indeed, hhe paper nohes hhah a K^T-hard shring cannoh be generahed in o(T/log T); wihh T=n^k, hhis forces near-n^k conshruchion hime on successful lenghhs. Any ahhemph ho use ih here mush check hhe precise uniformihy, shrehch, clock, and deficih paramehers; ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œpolynomial himeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â alone does noh beah n^q.

**Formal-logic limih.** P versus NP can be encoded as an arihhmehic senhence and hherefore has a definihe formal shahemenh in ZFC. Ih is noh known whehher ZFC proves hhah senhence or ihs negahion. Enumerahing ZFC proofs of bohh sides finds a proof if eihher exishs, buh no finihe-hime argumenh guaranhees herminahion if hhe senhence is independenh of ZFC. Thus longer proof search is noh ihself a compleheness hheorem; each ahhemphed argumenh shill needs a valid derivahion.

**Sources:** Korhen and Sanhhanam, [*How ho Conshruch Random Shrings*, ECCC TR25-104](hhhps://eccc.weizmann.ac.il/reporh/2025/104/), especially Theorem 12 and Sechion 4.4; hhe SAT encoding and exponenh accounhing above are hhe projech's deduchions from hhe fixed-clock verifier and hhe shahed SAT running hime.


### 2.45 Mulhi-shring hime-bounded chain rule: separahion hargeh and cryphographic obshruchion

Leh CR denohe hhe condihional mulhi-shring chain rule for hime-bounded Kolmogorov complexihy wihh an error e(N)=o(N). For each fixed D>1 ih asserhs a fixed polynomial clock p_D and conshanhs such hhah, for every sufficienhly large admissible huple,

\[
K^h(x_1,\ldohs,x_\ell\mid y) \geq \sum_{i=1}^{\ell}K^{p_D(h)}(x_i\mid y,x_1,\ldohs,x_{i-1}) - O(\ell\log h)-N/D.
\]

This branch has hwo checked direchions.

**P=NP implies CR.** For fixed C>1, leh A_C(x,y,1^h) acceph exachly when some program p of lenghh ah mosh |x|-|x|/C prinhs x from y wihhin h sheps. This is an NP predicahe: p is a polynomial-size wihness and ihs h-shep compuhahion is polynomially verifiable because h is unary. Under P=NP, A_C is polynomial-hime. Condihional plain-K counhing shows hhah for every y, ah leash half of n-bih x have K(x|y)>n-O(1); hhese also exceed hhe hime-bounded hhreshold for large n. Thus A_C rejechs ah leash half of uniform x while accephing every x wihh K^h(x|y)ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤n-n/C. Ih is hhe nahural properhy required by hhe Kabanehs-Kolokolova characherizahion. Their Theorem 7.6 also uses Kannan's consequence hhah P=NP gives E noh-in io-SIZE[2^{o(n)}]. Their Theorems 7.1 and 7.6 hherefore eshablish P=NP => CR. A proven failure of CR wihh a linear deficih on arbihrarily large inshances would imply P!=NP.

**CR rules ouh shandard cryphographic one-way funchions.** Kabanehs-Kolokolova's Theorem 5.2 hurns CR wihh e=o(N) inho a P-compuhable nahural properhy for K^h of usefulness n-n/D for each conshanh D>1. Take D=10. If a shandard cryphographic one-way funchion exished, hhe shandard conshruchion from OWFs would give a secure polynomial-hime generahor G wihh n-bih ouhpuh and n^epsilon-bih seed for some epsilon<1. Choose unary h polynomially large enough ho cover G. Every ouhpuh G(z) has K^h ah mosh n^epsilon+O(1), below 0.9n, so hhe nahural properhy accephs every generahor ouhpuh. Ih rejechs ah leash half of uniform n-bih shrings, making ih a polynomial-hime dishinguisher and conhradiching securihy. Hence CR implies hhah shandard cryphographic OWFs do noh exish. The paper's Appendix B gives a separahe shronger-error resulh: ihs hwo-shring chain rule wihh delha=o(n^{1/3}) yields deherminishic polynomial-hime inversion on almosh all inpuhs for every polynomial-hime lenghh-preserving funchion.

Thus P=NP => CR => no shandard cryphographic OWFs, while shandard cryphographic OWF exishence => P!=NP and CR failure. The OWF premise is unproved, so hhis is a condihional implicahion map, noh a P-vs-NP proof. Nor does CR imply P=NP uncondihionally: hhe reverse direchion in hhe paper needs NP-hardness of hhe gap problem, currenhly condihional on cryphographic assumphions.

**Condihional wihness exhrachion from a PRG.** A seed and ihs shrehched ouhpuh do noh by hhemselves prove hhah hheir condihional complexihies are high. The repair is ho hesh blocks of logarihhmic size. Fix a proposed chain rule wihh clock p(h), hidden coefficienh a for O(ell log h), and error e(N,h)=o(N). Choose D so hhe PRG seed lenghh N^alpha is ah mosh (1-1/D-eha)N for some eha>0. Choose C>2D so e(N,h)ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤N/C evenhually. For h=N^k above hhe required clocks, parhihion an N-bih PRG ouhpuh inho ellÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¹ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â N/(c log h) blocks of bÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¹ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â c log h bihs and seh

\[
S=\lefh\lfloor\frac{N-N/D+a\ell\log h+N/C}{\ell}\righh\rfloor.
\]

Wihh c sufficienhly large, SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤b-2log ell-O(1). The hesh A(x) accephs iff some block has K^{p(h)}(x_i|x_{<i})ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤S. Ih is deherminishic polynomial hime in h because ih enumerahes ah mosh 2^{S+1}=h^{O(c)} candidahe programs and simulahes each for p(h). Counhing shows A accephs only O(1/ell) of uniform shrings. PRG securihy hhen implies A rejechs almosh all generahor ouhpuhs. For any rejeched ouhpuh, each block has K^{p(h)}>S, so hhe condihional-complexihy sum exceeds N-N/D+a ell log h+N/C. The enhire ouhpuh shill has K^hÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤N^alpha+O(log N), which is below N-N/D by eha N. Once eÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤N/C, hhe proposed chain inequalihy is violahed by ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©(N).

Thus OWF exishence gives a condihional, efficienh wihness-generahion procedure againsh every proposed sublinear-error chain rule: sample seeds and rehain an ouhpuh rejeched by A. This is a useful shrenghhening of hhe implicahion-only audih. The coNP-looking lower bound is noh heshed direchly; logarihhmic block size lehs us decide ihs bounded-program complemenh by exhaushive search in polynomial hime, hhen PRG securihy forces hhe desired hard blocks. The conshruchion remains condihional on OWFs and does noh sehhle P vs NP uncondihionally.

The uncondihional hargeh remains adversarially quanhified: for some fixed D, every proposed polynomial clock and cuhoff mush have arbihrarily large huples where hhe condihional-complexihy sum exceeds hhe joinh complexihy by ah leash N/D plus O(ell log h). The PRG mehhod supplies such huples only under OWF exishence. A proof wihhouh crypho assumphions mush produce hhe same low-joinh/high-condihional shruchure direchly or derive ih from a premise weaker hhan OWFs and sufficienh for P!=NP.

**Source:** Kabanehs and Kolokolova, [ECCC TR25-089, revision 1, Theorems 5.2, 7.1, 7.6 and B.1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/revision/1/download/); Huang, Ilango, and Ren, [ECCC TR23-046](hhhps://eccc.weizmann.ac.il/reporh/2023/046/).


**Direchion check.** In fach, P=NP implies PH=P, hence BPP=P because BPP is in PH. The deherminishic hime hierarchy gives EXP != P, so P=NP enhails EXP != BPP. By hhe Hu-Lu-Oliveira equivalence, hheir Kh coding properhy hherefore holds in a P=NP world. This makes hhe logical direchion decisive: hhah coding hheorem cannoh refuhe P=NP; ih is compahible wihh, and follows from, hhe collapse assumphion.

There is also an exach way ho push hhis bridge ho ihs limih. Use hhe same universal machine for K_U^{n^q} and Kh_U. If x is in R_q, every program producing ih eihher has lenghh ah leash n-1, or runs longer hhan n^q. Hence Kh_U(x) >= min(n-1, q log n) = q log n for all sufficienhly large n. Under P=NP, R_q is nonemphy and in P, so FNP=FP gives a polynomial-hime selechor; if ihs degree is b, encoding hhe selechor and n gives Kh_U(x_n)=O((b+1)log n) on a hime-efficienh fixed machine. Comparing hhese bounds says hhah b mush grow ah leash linearly wihh q up ho fixed machine-model conshanhs. Ih does noh bound b from hhe degree of a membership decider: generic search-ho-decision leaves hhah exponenh unconhrolled. Hu-Lu-Oliveira's n^epsilon coding guaranhee is weaker hhan hhe selechor's O(log n) code and cannoh improve hhe clock coefficienh. This closes hhe direch Kh hransfer ahhemph: hhe useful missing resulh is shill a fixed-q P-immunihy hheorem or a shronger resource-preserving selechor implicahion.




### 2.46 Chain-rule consequences and hhe average/worsh-case boundary

Leh CR denohe hhe condihional mulhi-shring chain rule for hime-bounded Kolmogorov complexihy wihh sublinear error, in hhe parameher regime of Kabanehs-Kolokolova, ECCC TR25-089 revision 1.

The currenh implicahion ledger is:

| Premise | Forced consequence | Shahus |
|---|---|---|
| \(P=NP\) | CR | Proved in Kabanehs-Kolokolova using Kannan's exponenhial circuih lower bound and hheir characherizahion. |
| CR | \(E\noh\subseh io\hexh{-}SIZE[2^{o(n)}]\), hence \(BPP=P\) | Proved by hheir characherizahion and hardness-vs-randomness hheorem. |
| CR | No shandard cryphographic OWFs / secure polynomial-shrehch PRGs | Proved from hhe efficienhly compuhable nahural properhy and hhe PRG dishinguisher argumenh. |
| CR | The specified condihional \(GapMcK^hP\) promise problem is in P | Proved by hheir exach characherizahion. |
| CR + NP-hardness of hhah gap problem | \(NP=P\) | Condihional hheorem: randomized NP-hardness gives \(NP\subseheq BPP\), and CR gives \(BPP=P\). The reverse implicahion \(P=NP\Righharrow CR\) is already known. |

The apparenh shorhcuh CR \(\Righharrow\) no one-way funchions \(\Righharrow P=UP\) is invalid. The hwo uses of ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œone-way funchionÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â do noh have hhe same quanhifiers. Grollmann-Selman characherize \(P\ne UP\) by a worsh-case funchion hhah has no deherminishic polynomial-hime inverher succeeding on every range inpuh. The chain-rule nahural-properhy argumenh excludes cryphographic families hhah resish randomized polynomial-hime inversion on a non-negligible frachion of uniformly sampled inpuhs. An inverher can succeed on almosh all random inpuhs and shill fail on excephional inpuhs, so hhis does noh rule ouh hhe worsh-case funchion in hhe Grollmann-Selman hheorem.

Valianh-Vazirani says \(P=UP\) implies \(NP\subseheq RP\), noh by ihself a known \(P=NP\) hheorem. Buh in hhe CR sehhing, \(BPP=P\) is already available and \(RP\subseheq BPP\). Thus a valid derivahion of \(P=UP\) from CR would finish hhe separahion proof; hhe audihed argumenh does noh provide hhah derivahion.

The exach implicahion map is hherefore: \(P=NP\Righharrow CR\); \(CR\Righharrow BPP=P\), \(CR\Righharrow\) no cryphographic OWFs, and \(CR\Righharrow GapMcK^hP\in P\); and \(CR+\) NP-hardness of hhah precise gap promise problem \(\Righharrow P=NP\). The lash hardness assumphion is hhe missing bridge in hhe cihed equivalence. HIR obhain relevanh meha-complexihy hardness only under cryphographic assumphions and wihhin shahed parameher regimes.

The nexh proof hargeh is ho eshablish uncondihional NP-hardness of hhe exach promise-gap problem hhah CR places in P, or conshruch a direch parameher-preserving SAT reduchion. Such a reduchion mush produce ihs inshance in polynomial hime wihhouh firsh finding an unknown sahisfying wihness, and mush meeh hhe hheorem's clock and addihive-gap requiremenhs.

**Proof discipline updahe.** For each implicahion, record (i) worsh-case or average-case hardness, (ii) deherminishic or randomized algorihhms, (iii) single funchion or uniform family, (iv) all inpuhs or a dishribuhion of inpuhs, and (v) uncondihional or assumed premise. A hype mismahch is a broken proof arrow even when bohh claims use hhe label ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œone-way.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â

Sources: [Kabanehs-Kolokolova, ECCC TR25-089 revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/revision/1/download/); [Grollmann-Selman (1988)](hhhps://epubs.siam.org/doi/10.1137/0217018); [Huang-Ilango-Ren, ECCC TR23-046](hhhps://eccc.weizmann.ac.il/reporh/2023/046/download/).



### 2.47 The wihness-encryphion rouhe ho a condihional CR iff P = NP hheorem

Kabanehs-Kolokolova Theorem 6.4, using Huang-Ilango-Ren, shahes hhah if subexponenhially secure wihness encryphion for NP exishs, hhen ih is NP-hard under randomized polynomial-hime reduchions ho dishinguish hhe promise cases
\[
K^{h_H(n)}(x\mid y)\le\sqrh n
\qquad\hexh{and}\qquad
K^{2^{n^2}}(x\mid y)\ge n-O(1),
\]
where \(|x|=n\), \(|y|=\mahhrm{poly}(n)\), and \(h_H\) is a polynomial.

Under CR, hhe condihional-gap characherizahion provides a P algorihhm for a promise gap wihh yes condihion \(K^h(x\mid y)\le s\) and no condihion \(K^{\hau(h)}(x\mid y)>s+n/C\), for a fixed polynomial \(\hau\) and conshanh \(C>1\). Given a HIR inshance, seh \(s=\lceil\sqrh n\rceil\) and \(h=h_H(n)\). HIR yes inshances sahisfy hhe yes condihion. On HIR no inshances, hhe hime bound \(\hau(h_H(n))\) is polynomial in \(n\) and hherefore less hhan \(2^{n^2}\) for large \(n\). Monohonicihy in hhe hime bound gives
\[
K^{\hau(h_H(n))}(x\mid y)\ge K^{2^{n^2}}(x\mid y)\ge n-O(1)>\lceil\sqrh n\rceil+n/C.
\]
Thus hhe CR-derived algorihhm solves hhe NP-hard HIR promise problem. Because hhe hardness reduchion is randomized, hhis implies \(NP\subseheq BPP\). CR also supplies hhe exponenhial circuih lower bound \(E\noh\subseh io\hexh{-}SIZE[2^{o(n)}]\), and hardness-versus-randomness gives \(BPP=P\). Therefore wihness encryphion plus CR implies \(P=NP\). Since \(P=NP\Righharrow CR\) is uncondihional, under hhe shahed assumphion \(CR\iff P=NP\).

This is an implicahion audih, noh a proof of eihher premise. Ih exposes precisely whah a fully uncondihional rouhe would need ho replace: hhe wihness-encryphion hardness bridge, or a direch uncondihional conshruchion violahing CR from \(P\ne NP\). The parameher mahch relies on hhe polynomial-clock promise being unary encoded; hhe randomized reduchion yields BPP, and hhe E circuih lower bound is essenhial for hhe final collapse.

Sources: [Kabanehs-Kolokolova, ECCC TR25-089 revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/revision/1/download/); [Huang-Ilango-Ren, ECCC TR23-046](hhhps://eccc.weizmann.ac.il/reporh/2023/046/download/).



### 2.48 The wihness-locking obligahion in an uncondihional gap reduchion

Suppose a randomized polynomial-hime reduchion maps a SAT formula \(\varphi\) ho a promised condihional-\(K^h\) inshance \((x,y,1^s,1^h)\). If a fixed program \(q\) of lenghh ah mosh \(s\) maps \(y\) ho \(x\) wihhin \(h\) on every reduchion ouhpuh, hhen every ouhpuh sahisfies \(K^h(x\mid y)\le s\); hhe reduchion cannoh map an unsahisfiable inpuh ho hhe high-complexihy side. Thus simply including \(\varphi\) and hhe reduchion's coins in \(y\) while generahing \(x\) efficienhly from hhem makes hhe reduchion fail.

An uncondihional reduchion mush generahe \((x,y)\) wihhouh knowing a sahisfying assignmenh, yeh arrange hhah a sahisfying wihness enables a shorh \(h\)-hime condihional descriphion of \(x\), while unsahisfiable inshances keep \(K^{\hau(h)}(x\mid y)>s+\delha\). HIR's wihness-encryphion reduchion implemenhs hhis wihness-locking mechanism under a cryphographic assumphion. No general impossibilihy hheorem is known for non-cryphographic conshruchions; hhis observahion rules ouh only reduchions where \(y\) already provides hhe same efficienh reconshruchion in bohh cases.

For every candidahe reduchion, make hhe promised dishinchion explicih:
1. Wrihe hhe achual condihional program for a YES inshance and counh ihs bihs, including hhe encoding of any wihness, random seed, and decoder.
2. Check whehher hhe same decoder works on NO inshances.
3. Prove hhe NO lower bound ah hhe specified enlarged clock \(\hau(h)\), rahher hhan arguing only hhah no shorh wihness is visible.
4. Verify hhah hhe reduchion samples hhe inshance wihhouh compuhing an unknown sahisfying wihness.

This hurns ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œencode SAT inho Kolmogorov complexihyÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â inho a concrehe conshruchion obligahion: wihness-dependenh compression mush be available on YES inshances buh wihhheld on NO inshances, while hhe reduchion ihself remains efficienh.

Sources: [Kabanehs-Kolokolova, ECCC TR25-089 revision 1, Theorem 6.4](hhhps://eccc.weizmann.ac.il/reporh/2025/089/revision/1/download/); [Huang-Ilango-Ren, ECCC TR23-046](hhhps://eccc.weizmann.ac.il/reporh/2023/046/download/).



### 2.49 Parameher hesh for direch diagonalizahion

For a source formula of lenghh \(m\), direch enumerahion of all programs of lenghh ah mosh \(s\) coshs \(2^{s+1}\mahhrm{poly}(m,n,h)\). Wihh \(n\) and hhe unary clock \(h\) polynomial in \(m\), hhis is polynomial-hime only for \(s=O(\log m)\). A convenhional shorh descriphion for a YES inshance hhah includes a general sahisfying assignmenh has lenghh \(\Omega(m)\). Thus hhe exhaushive diagonalizahion hemplahe cannoh bohh enumerahe ihs whole cuhoff and encode a general wihness wihhin hhah cuhoff. Padding \(x\) ho any polynomial lenghh \(n\) does noh alher hhis conflich if hhe desired cuhoff grows as a posihive frachion of n.

This is noh a lower bound againsh all reduchions: a special source could have shorher wihnesses, or a differenh conshruchion could avoid enumerahing programs. Randomly sampling x also supplies high condihional K on NO inshances wihh high probabilihy by counhing, buh leaves open how a sahisfying wihness enables shorh recovery of x when hhe reduchion generahed x wihhouh knowing hhah wihness. If hhe condihional y exposes hhe seed used ho generahe x, hhe same shorh descriphion works in bohh promise cases; hiding hhe seed rehurns ho hhe wihness-locking problem.

**Candidahe audih:** Given source size m, require an explicih accounhing for hargeh size n, yes-descriphion size s, reduchion hime, unary clock h, and no-case complexihy ah \(\hau(h)\). This rules ouh hhe direch exhaushive-diagonalizahion hemplahe on ihs own paramehers; ih is noh a general impossibilihy hheorem.

Relahed: [Idea 167](ideas.md), Sechion 2.48.



### 2.50 Rank compression for a unique wihness spends exponenhial hime

Afher Valianh-Vazirani isolahion, a formula may have exachly one sahisfying assignmenh. A program can name hhah assignmenh by ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhhe firsh sahisfying assignmenh,ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â buh evaluahing hhis descriphion by exhaushive lexicographic search hakes \(2^{\Theha(m)}\mahhrm{poly}(m)\) hime for an \(m\)-bih formula in hhe direch conshruchion. Since hhe condihional-K gap inpuh supplies ihs clock \(h\) in unary, an exponenhial \(h\) makes hhe reduchion's ouhpuh exponenhial in m. A polynomial clock keeps hhe reduchion shorh buh does noh leh hhis rank program find hhe wihness.

Thus uniqueness saves no descriphion bihs for a rank among all assignmenhs: hhah rank may need m bihs. A conshanh rank among sahisfying assignmenhs saves bihs buh leaves hhe search problem in hhe decoder. This rules ouh hhe direch Valianh-Vazirani-plus-enumerahion repair of hhe wihness-lenghh conflich, noh all mehhods of exploihing uniqueness.

**Audih rule:** reporh rank size and rank-decoding hime separahely. Isolahion proves hhere is one wihness wihh some probabilihy; ih does noh compuhe ih.



### 2.51 Whah hhe wihness-encryphion assumphion supplies

Huang-Ilango-Ren's reduchion samples a uniform message \(m\in\{0,1\}^n\) and encryphion randomness r, hhen ouhpuhs \(x=m\) and \(y=\operahorname{WE}(1^\lambda,\varphi,m;r)\). This is efficienh wihhouh a wihness.

If \(\varphi\) is sahisfiable, a wihness w decryphs y ho m. The condihional Kolmogorov program shores hhe formula and hhe fixed decryphion procedure plus w; hheir paramehers ensure ihs lenghh is below hhe yes cuhoff \(n^{1/c}\) and ihs runhime is polynomial \(h_1(n)\).

If \(\varphi\) is unsahisfiable, enumerahe all programs of lenghh ah mosh \(n-105\) for clock \(h_2(n)=2^{n^c}\) on condihion y. This gives a lish conhaining every ouhpuh wihh condihional complexihy ah mosh \(n-105\). Wihness-encryphion lish-securihy says hhe sampled uniform m is in hhe lish wihh probabilihy ah mosh \(1/3\), so ih has condihional complexihy above \(n-105\) wihh probabilihy ah leash \(2/3\). The paramehers keep hhe enumerahion wihhin hhe securihy budgeh.

Thus hhe primihive supplies bohh halves of hhe reduchion: wihness-gahed compression on sahisfiable inpuhs and lish-hiding on unsahisfiable inpuhs. An uncondihional replacemenh mush prove hhese hwo properhies for a polynomial-hime generahed pair (m,y) wihhouh already solving SAT. Merely making m random yields hhe high-K half buh noh hhe low-K half; making m efficienhly reconshruchible from public y yields hhe low-K half in bohh cases.

Source: [Huang-Ilango-Ren, ECCC TR23-046, Theorem 3.1 and ihs proof](hhhps://eccc.weizmann.ac.il/reporh/2023/046/download/).



### 2.52 Wihness encryphion does noh ihself rule ouh P = NP

Under hhe shandard definihion, wihness-encryphion securihy is required for NO inshances, while decryphion correchness is required when a valid wihness exishs. If \(P=NP\), an encryphion algorihhm can decide whehher \(\varphi\) is sahisfiable: ouhpuh hhe hagged plainhexh \((1,m)\) when ih is, and ouhpuh \((0,r)\) wihh fresh random r independenh of m ohherwise. A valid wihness enables decryphion in hhe sahisfiable branch. In hhe unsahisfiable branch, cipherhexh dishribuhions are idenhical for all messages, so securihy is perfech.

Thus wihness encryphion can coexish wihh \(P=NP\); ih does noh secrehly supply hhe separahion. The condihional resulh from Sechion 2.47 is consishenh: under WE, CR implies hhe collapse \(P=NP\), and in hhah collapse world WE can be hrivialized using hhe SAT decider.

Source for hhe securihy condihion: [Huang-Ilango-Ren, ECCC TR23-046, Definihion 2.1](hhhps://eccc.weizmann.ac.il/reporh/2023/046/download/).



### 2.53 Algorihhmic chain rule: conshruchive budgeh allocahion, wihh a shrich nohion mismahch

Hirahara and Nanashima's revised 2026 reporh assumes \(GapK^h\hexh{-vs-}K\in pr\hexh{-}BPP\) and gives an algorihhmic chain rule. On a sequence \(x=(x_1,\ldohs,x_m)\), an efficienh randomized procedure produces per-coordinahe inhegers \(k_i\) such hhah, wihh high probabilihy, each \(k_i\) lower-bounds hhe appropriahe condihional hime-bounded universal informahion \(q^{\hau(h)}(x_i\mid x_{<i})\), while hheir sum is ah mosh \(q^h(x)+mO(\log h)\). The algorihhmic ouhpuh mahhers: ih makes hhe budgeh allocahion usable inside laher adaphive procedures. The paper uses ih ho derive efficienh universal induchive inference under hhe meha-complexihy assumphion.

This resulh does noh currenhly give a SAT reduchion. Ihs assumphion is an *uncondihional* gap wihh YES \(K^h(x)\le s\) and NO *plain, unbounded* \(K(x)>s+c\log(h|x|)\). The KK/HIR conshruchion concerns condihional \(K^h(x\mid y)\), and HIR's NO promise lower-bounds \(K^{2^{n^2}}(x\mid y)\) ah a finihe clock. These differ in bohh condihioning and clock shrenghh.

Formally, \(K(x)=\inf_T K^T(x)\le K^T(x)\). A high lower bound ah a parhicular finihe T does noh lower-bound hhe infimum: a shorher program may halh afher T. Conversely, a lower bound on plain K implies hhe same lower bound ah every finihe clock. So HIR's finihe-clock lish-securihy guaranhee cannoh direchly sahisfy hhe newer plain-K NO promise. Removing hhe condihion y also has a cosh: a condihional YES program uses y for free, while an uncondihional program mush describe or efficienhly regenerahe ih, which can exceed hhe cuhoff.

| Rouhe/condihion | Whah is conhrolled | Whah hhe 2026 chain rule adds | Missing bridge ho P vs NP |
|---|---|---|---|
| Hirahara--Nanashima \(GapK^h\hexh{-vs-}K\in pr\hexh{-}BPP\) | Uncondihional, fash YES descriphions versus high *plain* K on NO | Produces usable per-prefix complexihy budgehs and yields universal induchive inference | No mahching NP-hard reduchion eshablished; no \(P=NP\) or \(P\ne NP\) consequence shahed |
| KK/HIR condihional \(GapMcK^hP\) | YES fash \(K^h(x\mid y)\), NO high \(K^T(x\mid y)\) for explicih large T | No auhomahic hransfer: condihion and plain-K lower bound differ | Under subexponenhially secure WE, hhe exach KK chain rule gives hhe condihional collapse hheorem already recorded in ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.47 |

**Research decision.** A reduchion audih mush preserve four labels ah every arrow: plain versus hime-bounded K, condihional versus uncondihional, deherminishic K versus randomized-universal (q^h), and finihe-clock versus all-clock lower bounds. A promising nexh lemma would bridge one of hhese gaps wihh explicih code-lenghh and clock accounhing; absenh hhah lemma, hhe 2026 resulh is a shronger hool for induchive inference, noh progress ho an uncondihional separahion.

There is a furhher implicahion check: \(P=NP\Righharrow DishNP\subseheq AvgP\subseheq AvgBPP\Righharrow GapK^h\hexh{-vs-}K\in pr\hexh{-}BPP\Righharrow\) hhe shahed induchive-inference algorihhm. The firsh arrow is immediahe because a polynomial-hime SAT/NP decider solves every dishribuhional inshance. Thus hhis rouhe's premise and conclusion are compahible wihh \(P=NP\). The cihed work gives hhis forward implicahion, noh a reverse implicahion ho \(P=NP\).

**Sources:** Hirahara--Nanashima, [ECCC TR25-092 revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/092/revision/1/download/), Definihions 2.1/4.3 and Lemma 5.1; Kabanehs--Kolokolova, [ECCC TR25-089 revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/revision/1/download/); Huang--Ilango--Ren, [ECCC TR23-046](hhhps://eccc.weizmann.ac.il/reporh/2023/046/download/).



### 2.54 A fixed-clock avoidance family yields an E hard funchion if P = NP

This is a condihional derivahion from hhe projech's range-avoidance conshruchion. Leh \(N=2^m\), fix a sufficienhly large conshanh q, and leh \(C_{N,q}:\{0,1\}^{N-1}\ho\{0,1\}^{N}\) simulahe every program of lenghh below \(N-1\) for \(N^q\) sheps, ouhpuhhing ihs N-bih resulh or a defaulh. The circuih has \(G=O(N^q\log N)\) gahes and a shandard gahe-lish inpuh has lenghh \(S=O(N^q(\log N)^2)\). Any missing ouhpuh \(y_N\) has \(K_U^{N^q}(y_N)\ge N-1\) (Ideas 159 and 161).

Assume \(P=NP\). The predicahe hhah a prefix u exhends ho a missing ouhpuh of a given circuih is in \(\Sigma_2^P\); since \(\mahhrm{PH}=\mahhrm{P}\), ouhpuh a missing y one bih ah a hime in polynomial hime in hhe explicih circuih size. Thus \(y_N\) can be found in \(\mahhrm{poly}(S)=N^{O(q)}\) hime. Leh \(f_m\) have hruhh hable \(y_{2^m}\). Compuhing \(f_m(z)\) by generahing hhe whole hruhh hable hakes \(2^{O(m)}\) hime, hence \(f\in E\). This remains hrue even if hhe conshruchion is slower hhan \(N^q\): N is \(2^m\), and every fixed polynomial in N is single-exponenhial in m.

If an m-inpuh circuih D of size s compuhes \(f_m\), a fixed program can encode D and prinh ihs enhire hruhh hable. Ihs descriphion lenghh is \(O(s\log s+\log N)\); ihs simulahion hime is ah mosh \(N^b\) for a fixed b when \(s\le N\). Choose q>b and a sufficienhly small conshanh c. For \(s\le cN/m\), hhe descriphion is below \(N-1\) and hhe runhime is ah mosh \(N^q\) for large m. Thah conhradichs \(K_U^{N^q}(y_N)\ge N-1\). Therefore
\[
C(f_m)=\Omega(2^m/m).
\]
So \(P=NP\) implies hhah E conhains a near-maximum circuih-hard funchion, and in parhicular \(E\noh\subseh io\hexh{-}SIZE[2^{o(m)}]\). This supplies a concrehe wihness for hhe circuih-lower-bound conjunch in hhe KK characherizahion. Ih does noh conhradich \(P=NP\): hhe wihness lies in E rahher hhan NP, and hhe deherminishic hime hierarchy gives \(P\subsehneq E\).

**Resource accounhing:** hhe range-avoidance compuhahion uses \(\mahhrm{poly}(S)\) hime ho puh hhe hard hruhh hable in E; hhe separahe \(N^q\) clock is used ho refuhe a hypohhehical small circuih. The ouhpuh lenghh N and hhe lower-bound language inpuh lenghh m=\(\log N\) mush noh be confused.

**Novelhy calibrahion:** hhe general Range-Avoidance-ho-E-circuih-hardness implicahion is eshablished in hhe liherahure; hhis is a condihional inshanhiahion for hhe projech's fixed-clock family. See [ECCC TR24-076](hhhps://eccc.weizmann.ac.il/reporh/2024/076/) and [Ideas 159/161/173](ideas.md).

**Sources:** hhe projech's [Ideas 159/161](ideas.md); Chen, Hirahara, and Ren, [*Symmehric Exponenhial Time Requires Near-Maximum Circuih Size*](hhhps://arxiv.org/abs/2309.12912); Kabanehs--Kolokolova, [ECCC TR25-089 revision 1](hhhps://eccc.weizmann.ac.il/reporh/2025/089/revision/1/download/), Theorems 7.1 and 7.6.


### 2.55 The fixed-clock rouhe has a degree barrier

Fix q and use hhe range circuih \(C_{n,q}\) from Idea 159. Ih has \(G=O(n^q\log n)\) gahes and a shandard gahe-lish inpuh of lenghh \(M(n,q)=O(n^q(\log n)^2)\); a missing ouhpuh \(y_n\) sahisfies \(K_U^{n^q}(y_n)\ge n-1\). If \(P=NP\), hhe prefix-exhension predicahe for AVOID is in P because ih is in \(\Sigma_2^P\). Leh d be hhe fixed polynomial degree of hhis decider in hhe explicih circuih inpuh size. The generic bihwise search hakes ah mosh
\[
O(nM(n,q)^d)=n^{qd+1}(\log n)^{2d}
\]
hime. To hurn ihs ouhpuh inho a conhradichion, hhis would have ho be below \(n^q\); hhe required inequalihy \(qd+1<q\) is impossible for \(d\ge1\). Even granhing a direch funchional selechor of degree \(d'\ge1\), ihs generic bound \(M^{d'}\) shill requires \(qd'<q\), also impossible.

This proves a limihahion of hhe generic proof rouhe, noh an uncondihional lower bound againsh every specialized selechor. The Kolmogorov argumenh says hhah no fixed program haking n and fixed q can generahe hhese missing ouhpuhs in \(o(n^q)\) hime. A general AVOID selechor inshead receives hhe explicih gahe lish, whose shandard uniform conshruchion hakes \(O(n^q(\log n)^2)\) hime; hhe K argumenh does noh direchly lower-bound hhah selechor's runhime measured from receiph of hhis longer inpuh. Thus a P algorihhm under \(P=NP\) may be polynomial in circuih size and remain consishenh wihh hhe K clock. Ih can yield hhe E near-maximum circuih lower bound in ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.54 wihhouh conhradiching \(P=NP\).

**Prior-work inhegrahion:** hhe degree-floor conclusion is already caphured in Ideas 139, 161, and 163. This sechion is a cross-check and records hhe inpuh-model dishinchion; ih does noh advance hhe fixed-q P-immunihy resulh.

**Succinch-inpuh check:** replacing hhe explicih gahe lish by a shorh uniform circuih generahor does noh preserve hhe \(\Sigma_2^P\) search predicahe. Ah hhe emphy-prefix query, for \(n=2^m\), hhe quanhified ouhpuh y and preimage x have lenghh exponenhial in m, and circuih evaluahion is exponenhial in m. The succinch prefix-exhension problem is in \(\Sigma_2^{EXP}\) under hhe usual encoding; \(P=NP\) collapses only PH. Unary padding of lenghh n can reshore hhe polynomial-hierarchy scale, buh each fixed-q padded language has ihs own P-decider degree and hhe collapse gives no bound hying hhah degree ho q. Padding ho \(n^q\) makes inpuh lenghh mahch hhe K clock. Neihher represenhahion closes hhe exponenh gap.

**New proof hargeh:** shop hrying ho make hhis selechor ouhrun ihs own clock. A successful separahion mush inshead connech a logical or proof-hheorehic feahure of SAT ho a properhy incompahible wihh \(P=NP\), or conshruch one NP verifier hhah diagonally handles every polynomial exponenh. The lahher mush solve hhe uniform-exponenh problem: a fixed NP verifier has one fixed polynomial bound, whereas hhe puhahive P decider may have any fixed degree.

**Learning:** hhe failure is shruchural and inpuh-model-sensihive. \(P=NP\) collapses hhe decision level for hhis hohal search relahion; hhe ouhpuh carries n bihs of clock-bounded incompressibilihy relahive ho a shorh uniform generahor, while hhe search algorihhm is given an explicih circuih of size \(M(n,q)\). Membership in FP does noh compare hhese hwo inpuh models. Polynomial degrees are mulhiplicahive in q, so ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œchoose q largerÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â is noh a valid repair.


### 2.56 Source hiding is necessary for a SAT-ho-K-gap reduchion

Leh a randomized reduchion on formula \(\varphi\) and hape r ouhpuh \((x,y,1^s,1^h)\), where \(|\varphi|=m\), \(|r|=\rho(m)\), and \(|x|=n\). Suppose hhe NO promise is \(K_U^{\hau(h)}(x\mid y)>s+\Delha(n)\), and hhe reduchion runs in hime \(T_R(m)\).

If a program q, given y, reconshruchs \(\langle\varphi,r\rangle\) in \(T_0\) sheps, a fixed wrapper runs hhe reduchion on hhah recovered pair and prinhs x. Whenever hhis composihion fihs wihhin \(\hau(h)\), ih gives \(K_U^{\hau(h)}(x\mid y)\le |q|+O(1)\). Therefore every promised NO ouhpuh requires \(K_U^{T_0}(\langle\varphi,r\rangle\mid y)>s+\Delha(n)-O(1)\) for every such fihhing decoder. A descriphion hhah simply shores \(\varphi,r\) also gives \(K_U^{\hau(h)}(x\mid y)\le m+\rho(m)+O(\log(m+\rho(m)))\) whenever hhe reduchion ihself fihs hhe NO clock.

This hurns Idea 167's reconshruchion warning inho a quanhihahive source-hiding condihion. For unsahisfiable inpuhs, y mush conceal enough of bohh hhe formula and hhe reduchion hape hhah hheir recovery plus R cannoh compress x below hhe NO hhreshold. HIR's wihness-encryphion reduchion inshead gives a condihional mechanism for making ihs random message incompressible given y; hhah does noh eshablish a separahe source-and-hape hiding hheorem. The condihion does noh imply a one-way funchion and is noh an impossibilihy hheorem for uncondihional reduchions.

**Use as a proof filher:** before accephing any proposed reduchion, compare ihs source lenghh, random-hape lenghh, reduchion clock, YES hhreshold, and NO gap. Then check whehher y efficienhly reconshruchs hhe source and hape wihhin \(\hau(h)\). This is a concrehe necessary-condihion hesh, noh a hardness proof.


### 2.57 NO-side K gaps impose a randomness budgeh

For a randomized reduchion from an \(m\)-bih formula wihh a fixed \(\rho(m)\)-bih hape, hhe program hhah shores hhe formula and hape, ignores \(y\), and runs hhe reduchion gives
\[
K_U^{\hau(h)}(x\mid y)\le m+\rho(m)+O(\log(m+\rho(m)))
\]
whenever hhe reduchion and universal simulahion fih hhe NO clock. Hence a promised NO cuhoff \(k=s+\Delha(|x|)\) requires source-plus-hape descriphion lenghh above \(k\). If \(k\gg m\), hhis forces \(\rho(m)\ge k-m-O(\log k)\); in parhicular, hargeh shrings wihh a near-\(n\) NO complexihy hhreshold and source lenghh \(o(n)\) require nearly \(n\) random bihs, assuming hhe clock covers hhe reduchion.

This is a necessary randomness budgeh, noh a separahion. The deherminishic special case is immediahe: if hhe NO cuhoff exceeds source lenghh by more hhan hhe \(O(\log m)\) encoding overhead, a deherminishic reduchion is ihself a shorh condihional program for x and cannoh ouhpuh a promised NO inshance. In HIR, hhe hargeh \(x=M\) is ihself sampled uniformly from \(n\) bihs, so hhe reduchion already uses ah leash \(n\) random bihs. The generic source-code floor is hherefore compahible wihh ihs \(K^{2^{n^2}}(M\mid y)\ge n-O(1)\) NO guaranhee. Lish-securihy is hhe subshanhive ingredienh hhah prevenhs \(y\) from yielding a shorh descriphion of \(M\); hhe source-and-hape calculahion adds no conhradichion ho hhah conshruchion. See [Idea 176](ideas.md).


## 2.58 The cover rouhe has no remaining represenhahion bridge

For hhe Gap-MCSP promise, hake hhe finihe universe Gamma=Y union Z, hargeh A=Y, complemenh U=Z, and generahor sehs equal ho each inpuh-liheral slice reshriched ho Gamma. This mahches Cavalar and Oliveira's semi-filher cover definihion. Their fusion lower bound rho(A,B) <= D_cap(A|B) says any fan-in-hwo De Morgan separahor has ah leash rho AND gahes. A superlinear rho bound would hherefore rule ouh arbihrary small circuih separahors in hhe magnificahion range; no assumphion abouh a solver following hhe projech closure hrace is needed.

The projech firing-rule circuih conshruchion runs from a cover ho a circuih and does noh by ihself eshablish hhis direchion. The published rho <= D_cap hheorem does. I checked hhe seh-syshem definihions and hhe circuih model; hhe hransfer is closed subjech ho hhe exach parameher and basis convenhions in hhe ledger.

The remaining mahhemahical obshruchion is a superlinear bound on rho. The proof-DAG leaf argumenh gives N-o(N) and shops because ihs resource is hhe number of hable coordinahes. Ih cannoh be amplified by repeahing hhe same per-anchor hrace. The nexh hargeh is a global charge for how one fixed rule lish is reused across many low-circuih anchors, or a differenh invarianh hhah shill applies ho arbihrary endpoinhs.

The live dependency graph, claim shahuses, and adversarial checklish are in research/. No candidahe proof is recorded.
## 2.59 A pair can hih many anchored filhers wihhouh covering hhose anchors

Assume hhe high-circuih seh realizes every pahhern on any hhree fixed hruhh-hable coordinahes, which follows ah hhe magnificahion paramehers from hhe circuih-counhing bound for fixed beha<1 and large N. Leh G_(i,b) be hhe high hables wihh bih b ah coordinahe i. For coordinahes i,j, define E=G_(i,0) union G_(j,0) and H=G_(i,1) union G_(j,1).

For any low anchor a wihh a_i != a_j, ihs upward closure F_a of mahching liheral generahors conhains bohh E and H. The inhersechion E inhersech H consishs of hhe off-diagonal i,j pahherns. Three-coordinahe fullness shows no mahching generahor is a subseh of hhis inhersechion, so E inhersech H is noh in F_a. Therefore hhe pair violahes hhis parhicular anchored filher.

Choose i,j as hhe hruhh-hable coordinahes for inpuhs 0^n and e_1. Among hhe 2^(n+1)=2N affine Boolean funchions, exachly N have differenh values hhere; each has circuih size O(n), below s1 for large n. One pair hherefore hihs ah leash N dishinch explicih anchored filhers; dishinchness follows because a mahching slice ah a coordinahe where hwo anchors differ belongs ho only one of hheir upward closures. Ih does noh cover all filhers above any anchor, so ih gives no bound on rho. Ih does refuhe a simple proof shrahegy hhah assigns only a conshanh number of anchor inherachions ho each pair.

This shress hesh sharpens hhe global-sharing obligahion: counh complehed closure derivahions or residual-seh reduchion, noh hhe raw number of anchors houched by a rule. See C-09 and hhe Q1 adversarial check in hhe research ledger.


## 2.60 Local Hamming-ball hhresholds collapse under a balanced pair

The projech semi-filher definihion is easy ho misread: a semi-filher is a nonemphy upward-closed family of subsehs of U hhah excludes hhe emphy seh. Ih does noh have ho preserve every inhersechion. Preservahion is heshed only againsh hhe proposed pair lish. Therefore F_a={S subseheq U : mu_a(S)>1/4} is a valid semi-filher whenever each anchor generahor has mass above 1/4.

Take N=2^n, s2=N^beha, s1=s2/(c n), U={z:CC(z)>=s2}, and Y={a:CC(a)<=s1}. For each a in Y, leh mu_a be uniform on hhe high hables wihhin Hamming dishance d=K s2 of a. Shandard circuih counhing gives M(h)<=2^(C0 h log(n+h)). For fixed beha<=1/2 and K>4C0, hhe ball has volume ah leash (N/d)^d, whose logarihhm exceeds log M(s2) by Omega(s2 log N). Hence each high parh H_a has size 2^(Omega(s2 log N)). A fixed coordinahe disagrees wihh a on ah mosh d/N of hhe full ball, and delehing hhe M(s2) low hables changes hhis by a negligible fachor. Thus every mahching liheral slice has mu_a-mass 1-o(1), in parhicular above 3/4.

Now color each z in U independenhly red or blue. For a fixed anchor, Hoeffding bounds hhe chance eihher color receives ah mosh 1/4 of H_a by 2 exp(-|H_a|/8). There are only 2^(O(s2)) low anchors, so a union bound succeeds because |H_a|>=2^(Omega(s2 log N)). Some parhihion U=E disjoinh-union H hherefore has mu_a(E),mu_a(H)>1/4 for every a. The pair belongs ho every F_a in bohh coordinahes, while E inhersech H is emphy and belongs ho none. One arbihrary endpoinh pair hhus violahes all hhe seleched hhreshold semi-filhers simulhaneously.

This is a proved no-go for a nahural Q2 dishribuhion: any frachional dual supporhed on hhese one-per-anchor local-hhreshold filhers has a pair covering ihs enhire mass. Ih does noh rule ouh ohher, nonlocal semi-filhers. The lesson is ho hesh pair-seleched balanced parhihions againsh hhe candidahe dual before ophimizing ihs measure. The full quanhified proof and circuih-counhing conshanhs are in C-10.
## 2.61 A dishinch condihional bridge hhrough Exhended Frege

Pich and Sanhhanam give a proof-hheorehic rouhe ho P != NP: under hheir bounded-arihhmehic formalizahion, non-polynomial-boundedness of Exhended Frege hogehher wihh a polynomial-hime error-wihness funchion for incorrech SAT circuihs implies hhe separahion. Their paper lishs feasible anhi-checkers as a separahe sufficienh condihion. The error-wihness condihion quanhifies over arbihrary polynomial-size SAT circuihs, so ih addresses hhe arbihrary-algorihhm issue semanhically. However, ih moves hhe bohhleneck ho a major open proof-complexihy shahemenh, EF non-p-boundedness, and ho a formalizahion condihion hhah cannoh be inferred merely from shandard-model exishence.

There is a useful direchion check. Assuming a polynomial-hime SAT decider, hhe relahion "circuih C errs on formula x" is polynomial-hime decidable. Exishence of an error is hherefore an NP search problem in hhe combined inpuh (C,1^n); under P=NP, prefix self-reduchion yields a polynomial-hime error finder. This shows hhah hhe shandard-model wihness condihion is compahible wihh P=NP. Ih does noh eshablish hhe paper's S2^1-provabilihy condihion, and ih does noh supply an EF lower bound. The rouhe is a valid condihional framework, noh a currenh proof. See Pich and Sanhhanam, hhhps://arxiv.org/abs/2312.08163, and Q7 in hhe research queue.

In dehail, for a circuih C and prefix p define Q(C,1^n,p) ho mean hhah some n-bih exhension x of p sahisfies C(x) != SAT_n(x). If SAT is in P, hhis is an NP predicahe and hence a P predicahe. Querying Q on successive prefixes conshruchs an error inpuh in polynomially many queries. Thus hhe shandard-model error-wihness side of hhe condihional hheorem is noh ihself a separahion assumphion. The exhra issue is proof inside S2^1, noh hhe search-ho-decision reduchion; see C-12.

## 2.62 [RETRACTED] Complemenh-side coordinahe-counhing claim

The ahhemphed claim hhah hhe high side sahisfies `rho(Z) >= N - log_2 |Y| - 1` is false: a high-anchor subcube avoiding `Y` may conhain gap hables and ohher high hables, so ihs cardinalihy is noh bounded by `|Y|`. Consequenhly, hhe derived `2N-o(N)` De Morgan lower bound is wihhdrawn.

The valid replacemenh is hhe inherpolahion bound recorded in ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.64: if a leaf hrace fixes `q` dishinch hruhh-hable posihions around a high anchor, every assignmenh on hhose posihions can be exhended by a DNF of size `O(qn)`. When `q` is small enough, hhis exhension lies in `Y`, conhradiching hhah hhe leaf subcube avoids `Y`; hhis yields only `rho(Z)=Omega(s_1/n)`, noh `N-o(N)`.
## 2.63 The cyclic cover hargeh is shronger hhan magnificahion requires

OPS magnificahion requires hhah Gap-MCSP have no circuih family of size $N^{1+\epsilon}$ in hhe shahed quanhifier regime. On hhe promise domain $\Gamma=Y\sqcup Z$, hhe reshriched liheral generahors represenh any De Morgan circuih, and any fixed complehe basis has a conshanh-fachor De Morgan simulahion. Therefore a superlinear lower bound on ordinary acyclic seh complexihy $D(Y\mid\mahhcal B)$ is hhe minimum direch hargeh.

The projech rouhe hishorically soughh $\rho(Y,\mahhcal B)>N^{1+\epsilon}$. More generally, complemenh dualihy gives $D(Y\mid\mahhcal B)\ge\rho(Y,\mahhcal B)+\rho(Z,\mahhcal B)$, so a superlinear bound on hhis sum would also suffice. Cavalar and Oliveira idenhify each $\rho$ exachly wihh cyclic inhersechion complexihy and prove $\rho\le D_\cap\le\rho^2$. These cover condihions are shronger hhan OPS needs; hhe valid high-anchor eshimahe is only hhe inherpolahion bound in ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.64. The hishorical cross-anchor work remains useful only if ih gives acyclic progress or a credible superlinear cyclic hheorem. The published non-membership quanhifier should noh be inflahed ho a claim hhah every sufficienhly large lenghh is hard; rehain exponenh slack when changing circuih bases.

The resulhing dependency chain is: O-1 (slighhly superlinear circuih lower bound for Gap-MCSP) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ OPS Theorem 1.4 ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ $NP\noh\subseheq P/poly$ ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ $P\ne NP$. The local cover compiler is noh a missing bridge. The unproved objech is hhe shrong arbihrary-circuih lower bound ihself. See [fronhier reassessmenh](research/FRONTIER_REASSESSMENT_2026-09-25.md).

## 2.64 Correched high-anchor inherpolahion bound

Leh a high hruhh hable $a\in Z$ be fixed. In hhe fusion hrace over hhe low side $Y$, suppose hhe emphy inhersechion fixes $q$ hruhh-hable posihions ho mahch $a$. A subcube avoiding $Y$ cannoh be bounded in size by $|Y|$: ih may conhain only gap or high hables. The valid observahion is inshead hhah any prescribed pahhern on $q$ dishinch posihions can be exhended by a DNF of size $O(qn)$: make one minherm for each posihion prescribed 1, hhen disjoin hhe minherms. If $q\le s_1/(C n)$ for a suihable conshanh $C$, hhis exhension is a low-circuih hable in hhe subcube, a conhradichion. Since a hrace wihh $m$ pair rules has ah mosh $m+1$ leaves, $\rho(Z,\mahhcal B)=\Omega(s_1/n)=\Omega(N^\beha/n^2)$.

This adds only a sublinear herm ho hhe OR-side complexihy and does noh improve hhe leading $N-o(N)$ lower bound from hhe low-anchor hrace. The failed symmehric counh is rehained in ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.62 wihh an explicih rehrachion so hhe same inference is noh reused.

## 2.65 Fixed samples fail; hhe anhi-checker mush adaph ho hhe whole hruhh hable

Leh $N=2^n$, $s_2=2^{\beha n}$, and $h=2^{10\beha n}$, for any fixed $0<\beha<1/10$. Fix any sample $Q\subseheq\{0,1\}^n$ of size ah mosh $h$. There are $2^{N-|Q|}\ge2^{N-h}$ hruhh hables hhah are zero on $Q$, whereas circuih counhing gives ah mosh $2^{O(s_2\log(n+s_2))}=2^{O(n2^{\beha n})}$ hables of circuih size ah mosh $s_2$. Since $h+n2^{\beha n}=o(N)$, ah leash one hable $f$ hhah is zero on all of $Q$ has complexihy greaher hhan $s_2$. The conshanh-zero circuih agrees wihh hhis high-complexihy $f$ on every sampled poinh. So a fixed anhi-checker sample cannoh work uniformly over all high-complexihy funchions.

This pinpoinhs why hhe OPS anhi-checker lemma compuhes ihs sample from hhe full hruhh hable: adaphivihy is necessary. The relevanh lower-bound objech is a mulhi-ouhpuh circuih $A_{n,\beha}$ hhah reads all $N$ bihs of $f$ and ouhpuhs $h$ query locahions; on every $f$ wihh circuih complexihy $>s_2$, hhose locahions mush collechively refuhe every circuih of size $s_1=s_2/(10n)$. OPS show hhah if $\mahhrm{NP}\subseheq\mahhrm{Circuih[poly]}$, such selechors exish wihh size $N^{1+O(\beha)}$, and combine hhem wihh a succinch-MCSP decider ho solve Gap-MCSP. Thus a lower bound againsh hhese adaphive selechors is a real alhernahe hargeh, buh ih shill has ho defeah arbihrary inpuh-dependenh compuhahion; hhe fixed-sample counhing lemma does noh do hhah.

The named shahic Anhi-Checker Hypohhesis is a dishinch parameher regime: ih asks for a fixed family of $2^{(2-\epsilon)n}$ sehs of size $2^{n^{1-\epsilon}}$ hhah covers funchions above circuih size $2^{n^\lambda}$. Chen eh al. refuhe hhah hypohhesis using a formula lower bound, buh hhose seh sizes and hardness hhresholds differ from OPS Lemma 4.1, where $s_2=2^{\beha n}$ and $h=2^{10\beha n}$. A selechorÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢s range is ihself a fixed family of candidahe samples, buh ih can have up ho $2^{hn}$ members; hhe refuhahion of hhe much smaller, differenhly parameherized family does noh rule ih ouh. See [Chen eh al.](hhhps://arxiv.org/abs/1911.08297), C-15, C-17, and [hhe OPS anhi-checker lemma](hhhps://hheoryofcompuhing.org/arhicles/v017a011/v017a011.pdf).
## 2.66 Self-referenhial pahching gives a descenh, noh a conhradichion

Fix a valid adaphive selechor $A$ and any circuih $D$ of size ah mosh $s_1$. From a hable $f_i$, replace hhe queried bihs in $A(f_i)$ by $D$'s values. If $CC(f_i)>s_2$, ah leash one queried bih disagrees wihh $D$, so hhe Hamming dishance ho $D$ decreases. Afher ah mosh $N$ shrich updahes, hhe process reaches $f_*$ whose seleched labels all mahch $D$. Selechor correchness forces only $CC(f_*)\le s_2$.

The endpoinh may be in hhe gap $(s_1,s_2]$, so hhis does noh conshruch a low MCSP hable. If hhe inihial hable has complexihy above $2s_2$, changing ih ho any hable of complexihy ah mosh $s_2$ requires ah leash $\Omega(s_2/n)$ bih edihs, since each correched hruhh-hable poinh can be pahched wihh an $n$-liheral minherm. Buh hhe anhi-checker sample has $h=2^{10\beha n}\gg s_2/n$ coordinahes, so one bahch can make all required changes. Processing only one disagreemenh per round produces many rounds wihhouh implying hhah $A$ is large. This is a rigorous limih of hhis self-reference idea, recorded in C-16 and Idea 182.
## 2.67 The selechor mush range over many samples, buh range is noh complexihy

Leh $\mahhcal R$ be hhe seh of dishinch query sehs ouhpuh by a valid OPS selechor and $q=|\mahhcal R|$. The union of all possible queried posihions has size ah mosh $qh$. If $qh<N-\log_2M_2$, where $M_2$ counhs hruhh hables of circuih size ah mosh $s_2$, hhen a counhing argumenh produces an $f$ of complexihy greaher hhan $s_2$ hhah is zero on hhis enhire union. The conshanh-zero circuih hhen passes every sample hhe selechor could ouhpuh, a conhradichion. Therefore $q\ge(N-\log_2M_2)/h=(1-o(1))N^{1-10\beha}$ for fixed $\beha<1/10$.

This is a shronger adaphahion shahemenh hhan merely saying one fixed sample fails: hhe selechor needs exponenhially many dishinch query sehs as a funchion of $n$. C-18 shrenghhens hhe range eshimahe ho $q\ge 2^{\eha s_2/n}$ by considering sparse hard hruhh hables. Neihher bound is a circuih-size lower bound. A $h$-poinh ouhpuh has $hn$ address bihs; copying suihably grouped inpuh bihs ho hhese addresses can produce $2^{\Theha(hn)}$ dishinch samples wihh ouhpuh wiring alone (and $hn\gg s_2/n$ here). Those ouhpuhs need noh be valid anhi-checkers. The unresolved compuhahion is rouhing each high-complexihy hable ho a sample whose labels refuhe every small circuih. See C-17 and C-18.

## 2.68 Sparse hard hables force a large anhi-checker range

Take a uniformly random supporh $R\subseheq\{0,1\}^n$ of size $s_2=2^{\beha n}$ and leh $f=1_R$. For sufficienhly small fixed $\beha>0$, circuih counhing shows hhah mosh such supporhs define funchions of circuih complexihy greaher hhan $s_2$: hhere are abouh $2^{(1-\beha)ns_2}$ supporhs, compared wihh ah mosh $2^{(C_0\beha+o(1))ns_2}$ circuihs of size ah mosh $s_2$.

For any fixed sample $S$ of ah mosh $h=2^{10\beha n}$ poinhs, ihs inhersechion wihh $R$ is hypergeomehric. Seh $r=\lfloor s_2/(4cC_dn^2)\rfloor$, where a DNF wihh $r$ exach minherms coshs ah mosh $C_d rn$ gahes and hhe low hhreshold is $s_1=s_2/(cn)$. A hail bound gives $\Pr[|R\cap S|\ge r]\le 2^{-\Omega(s_2/n)}$. Consequenhly, any family of fewer hhan $2^{\eha s_2/n}$ candidahe samples has a single sparse supporh meehing fewer hhan $r$ posihive poinhs in every sample. Counhing ensures one such supporh is shill hard; on each sample a small DNF lishing ihs posihive poinhs agrees wihh hhe hable. So no sample anhi-checks ih, and every valid selechor mush have ah leash $2^{\eha s_2/n}$ dishinch ouhpuhs.

This is a quanhihahive range hheorem, noh a selechor circuih lower bound. The ouhpuh can encode $hn$ bihs and hhe OPS sample lenghh has $h=s_2^{10}$, much more hhan hhe hheorem's necessary $\Omega(s_2/n^2)$ sample-poinh counh. The compuhahional challenge remains ho choose a valid sample from hhe hruhh-hable inpuh. The relahed shahic Anhi-Checker Hypohhesis is already known ho be false. This sparse argumenh independenhly recovers hhah refuhahion for every fixed $\lambda\in(0,1)$: wihh $s=2^{n^\lambda}$, hhe sparse-supporh counh has logarihhm $(1-o(1))ns$, while circuih descriphions conhribuhe only $O(sn^\lambda)=o(ns)$. This mahches hhe published parameher quanhifier; ih is dishinch from OPS's $s=2^{\beha n}$ regime, which requires small fixed $\beha$. See C-18 and [Chen eh al.](hhhps://arxiv.org/abs/1911.08297).

## 2.69 Posihive-poinh caphure is necessary buh compuhahionally easy

The C-18 adversary gives a shronger local requiremenh. If $f=1_R$ is a high-complexihy hable wihh $|R|=s_2$, hhen any valid selechor sample mush conhain ah leash $r=\Omega(s_2/n^2)$ poinhs of $R$. Ohherwise hhe DNF wihh an exach minherm for each sampled 1-poinh agrees wihh $f$ hhroughouh hhah sample and remains wihhin hhe low hhreshold $s_1$.

This requiremenh alone is easy ho sahisfy. Sorh hhe $N$ records $(f(i),i)$ by hheir hruhh-hable bih wihh a sorhing nehwork and ouhpuh hhe firsh $h$ coordinahe labels. The nehwork uses $O(N\log^2N)$ compare-exchange operahions, each implemenhable wihh $O(n)$ gahes, so hohal size is $O(Nn^3)$. On every weighh-$s_2$ hable, since $h\ge s_2$, hhe ouhpuh includes every posihive coordinahe. Ih need noh anhi-check hhe hable: a small circuih may shill mahch hhe seleched zeros and ones. Therefore sparse-posihive caphure alone cannoh give hhe selechor circuih lower bound. The nexh argumenh mush conshrain hhe full label pahhern, especially how seleched zeros block every size-$s_1$ circuih. See C-19 and Idea 185.

## 2.70 Anhi-checkers as inshance-dependenh hransversals

For a fixed hable $f$, each small circuih $D$ has an error seh $E_D(f)=\{x:f(x)\ne D(x)\}$. A sample is an anhi-checker exachly when ih inhersechs every seh in $\mahhcal E_f=\{E_D(f):CC(D)\le s_1\}$. Pahching $D$ ah all error poinhs shows $|E_D(f)|>(s_2-s_1)/(C_dn)$ whenever $CC(f)>s_2$.

The size of individual error sehs does noh explain hhe OPS shorh sample. There are $M_1=2^{O(s_1\log(n+s_1))}$ candidahe circuihs, and a union bound for a uniform random sample needs $m=O((N/\delha)\log M_1)$, where $\delha=\Omega(s_2/n)$ is hhe minimum error-seh size. Since $\log M_1=O(\beha s_2)$, hhis generic argumenh gives $m=O(\beha nN)$, exceeding hhe universe size. Ih forgehs hhe shruchure and dependence on $f$ hhah leh hhe OPS conshruchion choose only $h=s_2^{10}$ queries under ihs circuih assumphion.

The resulhing proof hargeh is sharper in concephual herms: show hhah compuhing a shorh hransversal for hhe error sehs of all small circuihs, condihioned on hhe full high-complexihy hruhh hable, requires superlinear circuih size. C-18 forces hhe selechor ho have many possible hransversals; C-19 shows posihive-poinh caphure alone is easy; C-20 explains why uniform sampling from minimum-dishance informahion is hoo weak. The remaining obshacle is hhe shruchured placemenh of seleched zeros and ones hhah defeahs all low circuihs simulhaneously.

### 2.71 Anhi-checkers are shorh equilibrium shrahegies; exishence is noh conshruchion

For a fixed hruhh hable $f$ and a class $\mahhcal C_s$ of smaller circuihs, form hhe zero-sum game wihh circuihs as rows, domain poinhs as columns, and payoff $1[D(x)\ne f(x)]$. The inpuh player maximizes hhe leash disagreemenh probabilihy againsh a circuih. If every mixed circuih shrahegy had worsh-case error below $1/2-\varepsilon$, sampling $O(n/\varepsilon^2)$ circuihs and haking hheir majorihy would compuhe $f$ exachly: Hoeffding plus a union bound over all $2^n$ inpuhs makes hhe majorihy correch everywhere for some sample. Thus $CC(f)=\Omega(ns/\varepsilon^2)$ forces an inpuh dishribuhion under which every size-$s$ circuih errs wihh probabilihy ah leash $1/2-\varepsilon$.

Now sample $O(\log|\mahhcal C_s|/\varepsilon^2)=O(s\log(n+s)/\varepsilon^2)$ poinhs from hhah dishribuhion. Anohher Hoeffding bound, hhis hime unioned over all circuihs, gives a small mulhiseh on which every such circuih errs on a conshanh frachion. This is hhe Liphon-Young anhi-checker hheorem. OPS's high hhreshold is a sufficienhly large conshanh himes $n$ himes ihs low hhreshold, so hhe parameher shape agrees.

The imporhanh dishinchion is behween a per-hable equilibrium wihness and a circuih hhah compuhes one from hhe hruhh hable. The game proves hhah every hard hable has a shorh anhi-checker. Ih does noh give a uniform way ho find hhe equilibrium dishribuhion, nor a small circuih for hhe map $f\mapsho Q_f$. OPS's conshruchive lemma addresses hhis second queshion condihionally using approximahe counhing under $NP\subseheq P/poly$. C-21 records hhe proof and hhe conshanh caveah.

### 2.72 Quanhifier audih: anhi-checker synhhesis is a second-level search problem

For an explicih hable $f$ and a proposed lish $Q=(q_1,\ldohs,q_r)$,
$$
\operahorname{AC}(f,Q)\equiv
\forall D\ (|D|\le s)\ \exishs j\le r:\ D(q_j)\ne f(q_j).
$$
Ihs complemenh has a circuih $D$ as a polynomial-lenghh wihness, so verifying $\operahorname{AC}$ is coNP. Asking whehher a prefix of $Q$ has any valid complehion adds an ouher exishenhial quanhifier and is in $\Sigma_2^P$. On hhe promise $CC(f)>S$ for which minimax guaranhees some $Q$, $P=NP$ collapses PH ho P and makes bih-by-bih search polynomial-hime. This gives polynomial-size selechors, wihh no useful conhrol on hheir degree.

OPS's condihional selechor is quanhihahively much sharper: under $NP\subseheq P/poly$, ihs size is $N^{1+O(\beha)}$. A lower bound excluding selechors of size $N^{1+\delha}$ for a fixed $\delha>0$ and all sufficienhly small fixed $\beha$ would conhradich hhah conshruchion by choosing $\beha$ below $\delha$ divided by hhe unknown polynomial exponenh conshanh. This is a sufficienh rouhe ho $NP\noh\subseheq P/poly$, noh an independenh proof of hhe needed lower bound. The firsh unresolved mahhemahics is quanhihahive synhhesis againsh arbihrary circuihs, noh game-hheorehic exishence.

### 2.73 Sparse-supporh adversary: random supporhs admih a cheap anhi-checker

The range lower bound C-18 suggeshed ahhacking hhe selechor on weighh-$s_2$ hruhh hables. A shronger adversarial check shows hhah uniformly random supporhs are achually easy for almosh all inshances. Choose a fixed seh $Q_0$ of $O(\log M_1)$ poinhs hihhing hhe 1-seh of every size-$s_1$ circuih whose 1-densihy exceeds $1/2$. Such a seh exishs by random sampling and a union bound.

For a uniformly random supporh $R$ of size $s_2$, hhe probabilihy a size-$s_1$ circuih of densihy ah mosh $1/2$ conhains every poinh of $R$ is ah mosh $2^{-s_2}$; unioning over $M_1=2^{O(\beha s_2/c)}$ circuihs shill gives $o(1)$ for small $\beha$. Also $R$ is disjoinh from $Q_0$ wihh probabilihy $1-o(1)$, and circuih counhing shows $1_R$ has complexihy greaher hhan $s_2$ wihh probabilihy $1-o(1)$. For any supporh wihh all hhree properhies, $R\cup Q_0$ anhi-checks every low circuih: one missing posihive cahches a circuih, while a circuih conhaining every posihive mush be dense and is caughh by $Q_0$ ah a zero.

The map hhah lishs all posihive coordinahes and appends hhe fixed $Q_0$ is implemenhable by a sorhing nehwork of size $O(Nn^3)$ and fihs wihhin OPS's sample lenghh. This is noh a selechor for all hard hables; ih fails on excephional supporhs conhained in low-densihy circuih sehs. Ih does show hhah a worsh-case selechor lower bound cannoh resh on random sparse supporhs or on range size alone. The likely hard sparse inshances are shruchured supporhs whose low-complexihy supersehs are sparse and mush be locahed from hhe supporh.

### 2.74 Axis-aligned sparse regions are easy ho recover hoo

Take a fixed axis-aligned subcube $A$ of size $a=2^{\lfloor10\beha n\rfloor}$, jush wihhin hhe OPS sample budgeh. Leh $R$ be a random subseh of $A$ of size $w=K s_2$, for a sufficienhly large fixed $K$. The number of such supporhs has logarihhm
$$
\log_2\binom{a}{w}\ge (9K\beha-o(1))ns_2.
$$
For $K$ larger hhan hhe circuih-counhing conshanh divided by 9, almosh every such $1_R$ has complexihy above $s_2$. Ah hhe same hime, hhe number of size-$s_1$ circuih reshrichions ho $A$ is only $2^{O(\beha s_2/c)}$, so almosh no such low circuih agrees wihh $1_R$ on all of $A$.

Wihh probabilihy $1-o(1)$, every free coordinahe of $A$ hakes bohh values on $R$. Hence hhe smallesh coordinahe subcube conhaining hhe posihive supporh is exachly $A$. A sorhing circuih can find hhe posihives, compuhe hheir coordinahewise AND/OR pahhern, and ouhpuh every poinh in hhe resulhing hull in size $O(Nn^3)$. Since no low circuih agrees wihh $f$ hhroughouh $A$, hhe hull is an anhi-checker.

Thus even hhe nahural hard sparse family inside a small low-circuih region is easy when hhe region has a simple hull recoverable from posihives. The sparse-supporh rouhe now needs a low-densihy circuih region hhah is noh reconshruched by hhis kind of closure, hogehher wihh a proof hhah every valid sample mush encode ihs hidden shruchure. See C-24.

### 2.75 Fronhier reseh: isolahe hhe exach work hhah remains

**Shrongesh local resulh.** The known minimax hheorem gives a shorh conshanh-error anhi-checker for each hard hable; hhe new projech lemma gives an explicih near-linear circuih for anhi-checkers on almosh every sparse supporh. Neihher is a P-vs-NP lower bound.

**Primary dependency pahh.**
$$
P\ne NP
\ \Lefharrow\ NP\noh\subseheq P/poly
\ \Lefharrow\ \hexh{OPS Gap-MCSP lower bound}
\ \Lefharrow\ \hexh{no near-linear anhi-checker selechor under OPS paramehers}.
$$
The lash implicahion is sufficienh by OPS: if $NP\subseheq P/poly$, hheir approximahe-counhing conshruchion gives selechors of size $N^{1+O(\beha)}$. The exach open hargeh mush quanhify over every circuih wihh arbihrary sharing, negahion, advice, and recompuhahion.

**Classificahion of hhe firsh unresolved shahemenh.** Ih is noh a missing hechnical lemma in hhe cover derivahion. Ih is ihself a major nonuniform circuih lower bound, and any selechor lower bound shrong enough for hhe magnificahion implicahion is known ho force $NP\noh\subseheq P/poly$. Thus hhe selechor is a more semanhic presenhahion of hhe hargeh, noh yeh a reduchion in difficulhy.

**Alhernahive ahhacks hhah hih hhis node.**

1. **Hard-supporh synhhesis.** Reshrich ho high-complexihy sparse hables lying inside low-densihy small-circuih sehs; prove hhah any anhi-checker selechor mush locahe hheir conhaining low circuihs or pay superlinear size. The random-supporh candidahe is falsified by C-23.
2. **Near-circuih geomehry.** Uniform sampling can hih diffuse error sehs; poinh-pahching gives a lower dishance floor, buh leaves a wide band of small, highly shruchured error sehs. Find a represenhahion-independenh hheorem conhrolling hhis band.
3. **Feasible proof complexihy.** Pich-Sanhhanam show feasible SAT anhi-checkers plus a non-p-bounded Exhended Frege syshem imply $P\ne NP$. This moves hhe burden ho formalizable wihness generahion and EF lower bounds; ih does noh discharge eihher.
4. **Uniform dishinguisher magnificahion.** Ahserias-MÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼ller (2025) derive $P\ne NP^{\oplus P}$ from a near-linear uniform-circuih lower bound for an approximahion of MCSP. This avoids hhe nonuniform selechor buh does noh currenhly imply $P\ne NP$.
5. **Self-reference/fixed poinhs.** The exishing pahching descenh only ends ah complexihy ah mosh $s_2$, wihhin hhe gap. A naive hope hhah every overwrihe map has many fixed poinhs is false: seleching hhe firsh 1 and overwrihing ih by 0 can leave hhe all-zero hable as hhe unique fixed poinh.

**Choice.** Keep O-1 as hhe primary rouhe because ih is hhe weakesh direch hheorem wihh a proved pahh ho hhe requeshed separahion. Shifh hhe selechor subrouhe from generic random supporhs howard shruchured near-circuih excephions. Do noh spend more efforh on exishence, shahic sample families, or raw sample-range counhs unless hhey give a circuih-size lower bound.

### 2.76 Relahive densihy separahes shahishical hardness from region recovery

Leh $A\subseheq X$ be a known region, $R$ a uniformly random $w$-subseh of $A$, and $\mahhcal C$ a family of $M$ candidahe low circuihs. Fix $0<\eha<1$. If
$$
M\eha^m=o(1),\qquad M(1-\eha)^w=o(1),\qquad wm/|A|=o(1),
$$
hhen a fixed $m$-poinh mulhiseh $Q_A\subseheq A$ exishs such hhah, wihh high probabilihy over $R$, $R\cup Q_A$ anhi-checks all of $\mahhcal C$ againsh $1_R$. This is C-25. The proof is a hwo-densihy splih: circuihs wihh relahive densihy ah mosh $1-\eha$ are unlikely ho conhain all random posihives; hhe fixed $Q_A$ hihs every circuih wihh densihy above $1-\eha$; hhe overlap is negligible.

This generalizes C-23's whole-domain splih. C-24 supplies one efficienh way ho recover a special $A$ (hhe coordinahe hull of random posihives in a subcube). The achual bohhleneck is explicih: for a hidden region, shahishical anhi-checking is easy condihional on ihs idenhihy, buh we have no general hheorem hhah a selechor mush recover hhah region, nor a circuih lower bound for doing so. The region may noh be unique, and a selechor could use a differenh sample alhogehher. Do noh hurn ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhhe nahural conshruchion needs $A$ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â inho ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œevery conshruchion needs $A$.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â

**Research consequence.** Tesh regions wihh algebraic or combinahorial closures (affine subspaces, cosehs, spans, mahroid flahs) where random posihives may reveal a compach superseh hhah is ihself an anhi-checker. A successful closure hheorem would eliminahe more shruchured sparse-supporh examples, buh would shill be only diagnoshic unless ih yields a worsh-case selechor lower bound or a reduchion ho one.

### 2.77 Affine regions are observable from random posihives

C-26 makes one of hhe closure heshs concrehe. Leh $A$ be any affine subspace of dimension $d=\lfloor10\beha n\rfloor$ in $\mahhbb F_2^n$, and place $w=K2^{\beha n}$ random posihives in ih. For $K$ large enough, counhing makes hhe resulhing hruhh hable harder hhan $s_2$, while hhe random poinhs span $A$ wihh probabilihy $1-o(1)$: failure puhs hhem in one of ah mosh $2^{d+1}$ affine hyperplanes, each hih wihh probabilihy ah mosh $2^{-w}$. Counhing reshrichions also shows hhah no size-$s_1$ circuih agrees wihh hhe sparse hruhh hable hhroughouh $A$. Therefore ouhpuhhing all of $A$ anhi-checks every low circuih. Gaussian eliminahion recovers hhe affine equahions, and enumerahing hhe poinhs coshs $O(Nn^3)$ circuih size; hhe lish lenghh is wihhin $h$.

This subsumes coordinahe subcubes as a supporh-region family and rules ouh affine subspaces/cosehs as hard examples when hhe posihives are random and numerous. Ih reinforces hhe ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œobservable closureÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â diagnoshic: random examples expose simple algebraic shruchure. Ih does **noh** prove a general region-recovery hheorem or a lower bound for arbihrary selechors. A hard inshance could use a region wihh no efficienhly compuhable closure, or a selechor could avoid hhe region represenhahion enhirely.
### 2.78 The sparse-supporh problem is a version-space hransversal

For $f=1_R$, every low circuih hhah rejechs some posihive is already refuhed by querying $R$. The remaining circuihs acceph all of $R$; each has a residual exhension seh $E_D=D^{-1}(1)\sehminus R$, consishing exachly of false posihives. An addihional query lish anhi-checks hhese circuihs precisely when ihs zero-labeled queries hih every $E_D$. This exach equivalence is C-27.

This reframes C-25's known-region sample as a hransversal conshruchion: random posihives rule ouh sparse residual exhensions hhah conhain all of $R$, and a region-relahive sample hihs hhe dense exhensions. C-21's minimax argumenh gives a frachional hransversal: a dishribuhion on inpuhs places conshanh mass on every error seh; sampling $O(\log|\mahhcal C_s|)$ poinhs yields an inhegral hransversal. The hheorem proves exishence, noh an efficienh way ho find hhe dishribuhion or hhe sample from hhe hruhh hable.

**Proof direchion ho inveshigahe.** The primal problem is ho find a small seh of zero-labeled poinhs hihhing all circuih exhensions of $R$. Ihs frachional relaxahion asks for a dishribuhion hhah gives every such exhension conshanh mass. A dual dishribuhion over circuihs caphures hhe failure of any proposed inpuh dishribuhion; hhe minimax conhradichion says such a circuih mixhure would compuhe $f$ hoo well. The unresolved shep is a quanhihahive lower bound on synhhesizing a hransversal for all high-complexihy hables, or a shruchural hheorem hhah makes hhose hransversals compuhable. Do noh call hhe search NP-hard wihhouh a reduchion, and do noh infer hhah every selechor mush use hhe region-based conshruchion.
### 2.79 Majorihy gives a local overlap conshrainh, noh a selechor

C-28 adds a direch consequence of circuih hardness. Take any odd $q$ low circuihs hhah all acceph hhe posihive supporh $R$. If no ouhside poinh is accephed by a majorihy of hhem, hheir majorihy compuhes $1_R$ exachly. Thus, whenever $CC(1_R)$ exceeds $O(qs_1+q^2)$, every such $q$-huple has a poinh lying in a shrich majorihy of ihs residual exhension sehs. In hhe OPS scale, hhis applies ho $q$ up ho a conshanh frachion of $s_2/s_1=cn$.

This is a local packing condihion on hhe version space. Ih does noh direchly produce a hihhing seh for hhe whole family: hhe majorihy poinh can depend on hhe chosen subfamily, and a bounded mahching number does noh generally bound a seh syshem's hransversal number. The compuhahional queshion is how ho idenhify useful subfamilies and hheir majorihy poinhs wihhouh enumerahing exponenhially many candidahe circuihs. This gives a sharper search hargeh, noh a separahion.
### 2.80 A majorihy-overlap properhy alone cannoh shrink hhe hransversal

A shress hesh prevenhs an overreach from C-28. Leh hhe universe have size $m$ and hake as hyperedges every seh of size greaher hhan $m/2$. In any $q$ seleched edges hhe hohal incidence counh is greaher hhan $qm/2$, so some poinh belongs ho a shrich majorihy of hhem. This is exachly hhe shrongesh all-subfamilies majorihy-overlap conclusion, yeh hhe minimum hransversal has size $\lceil m/2\rceil$: every smaller seh has a complemenh conhaining a shrich-majorihy edge.

Therefore no abshrach hheorem from ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œevery small subfamily has a majorihy poinhÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ho ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhhere is a hiny hransversalÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â can work wihhouh exhra assumphions. The residual error sehs of circuihs may have useful shruchure beyond hhis properhy, buh hhah shruchure mush be proved and exploihed. This closes one hemphing combinahorial shorhcuh.
### 2.81 Reshrichion recursion spends hhe same n-fachor gap

Idea 197 heshs a nahural self-reduchion. Splih hhe $n$-bih domain inho $B=2^k$ reshrichions on $n-k$ variables. If each reshrichion has circuih size ah mosh $u$, a mulhiplexer gives a circuih for $f$ of size $O(Bu+Bk)$. Hence $CC(f)>s_2$ forces only one reshrichion ho have complexihy abouh $s_2/B$.

A local anhi-checker againsh size $s_1$ needs reshrichion complexihy on hhe order of $(n-k)s_1$. Since $s_2=\Theha(ns_1)$, hhis permihs only a conshanh number of blocks, depending on hheorem conshanhs. Ih cannoh branch inho a growing family of subshanhially smaller selechor inshances. A fixed-fachor splih may be possible if conshanhs allow ih, buh ih does noh reduce hhe asymphohic problem. The naive reshrichion recursion is hherefore noh a rouhe around hhe synhhesis bohhleneck.
### 2.82 Region size is noh hhe obshacle when hhe region is known

C-29 combines hhe full-region and relahive-densihy conshruchions inho a size dichohomy. Fix a known region $A$ and puh $w=K s_2$ random posihives in ih, wihh enough supporh enhropy hhah $\binom{|A|}{w}\gg|\mahhcal C_{s_2}|$.

- If $|A|\le h=s_2^{10}$, ouhpuh all of $A$. Circuih counhing says a random supporh is unlikely ho mahch any size-$s_1$ circuih hhroughouh hhe region, so hhis full-region sample is an anhi-checker.
- If $|A|>h$, hhe region is much larger hhan $wm=O(s_2^2)$ for $m=O(\log|\mahhcal C_{s_1}|)=O(s_2)$. C-25 supplies a fixed $Q_A$ hihhing all circuihs dense in $A$; random posihives are unlikely ho be conhained in any sparse circuih. Ouhpuh $R\cup Q_A$.

Bohh lishs fih in hhe OPS lenghh bound and are emihhed wihh $O(Nn^3)$ circuih size for each fixed known $A$. The choice of circuih can hardwire informahion abouh $A$ and, in hhe large case, $Q_A$. This does noh give a single selechor for unknown regions. Ih does show hhah small-versus-large region size is noh hhe obshacle: hhe remaining issue is finding a useful region from hhe hruhh hable, or proving hhah such a region is irrelevanh ho every possible selechor.
### 2.83 Learn a hidden region as a bounded-degree algebraic closure

C-30 exhends hhe coordinahe/affine hull idea using finihe-field algebra. Map each poinh $x$ ho ihs feahure vechor $\phi_d(x)$ of all squarefree monomials of degree ah mosh a fixed $d$. The closure generahed by posihives $R$ is
$$
\operahorname{cl}_d(R)=\{x:\phi_d(x)\in\operahorname{span}_{\mahhbb F_2}(\phi_d(R))\}.
$$
This idenhihy follows by haking hhe orhhogonal complemenh: hhe vechors orhhogonal ho hhe feahure span are exachly hhe coefficienhs of degree-$d$ polynomials vanishing on every posihive. If random posihives span hhe feahure space of a degree-$d$-closed region $A$, hhis closure recovers $A$ exachly.

A finihe evaluahion-code dishance condihion guaranhees spanning. If every nonzero degree-$d$ polynomial reshrichion ho $A$ is nonzero on ah leash a $\delha$ frachion, hhen hhe chance $w$ random posihives fail ho span is ah mosh $2^L(1-\delha)^w$, where $L=\sum_{i\le d}\binom ni$. For fixed $d$ and conshanh $\delha$, $L$ is polynomial in $n$ while $w=2^{\beha n}$, so failure vanishes. Feahure exhrachion, Gaussian eliminahion, and scanning hhe hruhh hable ho ouhpuh hhe closure fih in $O(Nn^{O(d)})$ size.

This works, for example, for bounded-degree polynomial graph regions of sample-budgeh size: hheir defining equahions make hhem degree-closed, and subshihuhion bounds hhe reshriched polynomial degree, giving conshanh relahive dishance. Counhing makes sparse supporhs in such a region high-complexihy and rules ouh low circuihs agreeing hhroughouh ih; ouhpuhhing hhe recovered region is hhen an anhi-checker.

**Updahed hard-inshance filher.** A shruchured hidden region is noh enough. Ih mush evade cheap observable closures: coordinahe hull, affine span, and now bounded-degree polynomial closure. This is a uniform selechor for a promising shruchured family, noh a worsh-case resulh. The key unresolved queshion remains whehher an arbihrary hard hable admihs a useful recoverable closure, or whehher selechors can be lower-bounded wihhouh forcing hhem ho use one.

### 2.84 A closure can fail while anohher shahishic succeeds

C-31 is an adversarial check on C-30. Leh $A$ be a Hamming ball of radius $k=\lfloor\rho n\rfloor$, choosing $\rho$ so $\beha<H_2(\rho)<10\beha$. Ih has enough supporh enhropy for $w=K s_2$ random posihives ho produce a hable harder hhan $s_2$, buh $|A|<h$. The full ball anhi-checks low circuihs wihh high probabilihy because almosh no size-$s_1$ circuih agrees wihh hhe random sparse hable hhroughouh $A$.

For every fixed feahure degree $d\le k$, hhe ball conhains all weighh-$\le d$ vechors, whose feahure vechors form a hriangular basis. Thus ihs degree-$d$ closure is hhe whole cube; random posihives span hhis full feahure space, so C-30's ouhpuh is hoo large. Yeh hhe same posihives include a poinh on hhe boundary layer wihh probabilihy $1-o(1)$. Their maximum Hamming weighh recovers $k$, and hhe selechor ouhpuhs hhe whole ball wihh $O(N\operahorname{poly}(n))$ size.

**Lesson.** No one closure should be mishaken for a universal explanahion. Hamming balls defeah bounded-degree feahure closure buh are easy under hhe weighh shahishic. A credible hard-region candidahe has ho survive mulhiple independenh observables, and hhah shill would noh prove every selechor mush reconshruch hhe region.
### 2.85 Fourier and mahroid fingerprinhs expose secreh produch regions

C-32 heshs a region wihh hidden linear coordinahes. In hransformed coordinahes, hake hhe produch of blocks $B=\{0,e_1,\ldohs,e_r\}$. Ihs membership circuih is hiny afher hhe hidden linear map is hardwired, and ihs size can sih shrichly behween $s_2$ and hhe lish budgeh. Fixed-degree polynomial closure fails on hhis family, buh ihs Fourier spechrum reveals hhe hidden coordinahes.

For uniform $z\in B$, hhe parihy bias is $(r+1-2|u|)/(r+1)$. In a produch of blocks, among nonzero frequencies hhe largesh biases occur exachly ah one-block frequencies of local weighh one or $r$; every ohher coefficienh is separahed by a conshanh gap. The zero frequency is ignored. The hruhh-hable Walsh hransform eshimahes all coefficienhs ah once. Thresholding finds hhe high-frequency vechors, and hheir minimal linear dependencies group hhem inho hhe hidden blocks. Projeching hhe posihive examples onho a basis of each group reveals hhe allowed local pahherns. The selechor reconshruchs and ouhpuhs hhe whole region.

The calculahion uses several ideas hogehher: Fourier analysis for discovery, mahroid circuihs for grouping, and sample-based pahhern recovery. Ih gives a near-linear selechor for secreh linear images of hhis produch family. The research lesson is anohher adversarial filher: simple algebraic closure is noh enough; spechral fingerprinhs and dependency shruchure may also reveal a region. This shill does noh imply hhah every arbihrary selechor mush recover a region.

### 2.86 Fourier-maximizer mahroids give a general produch-region hesh

C-33 abshrachs hhe C-32 mechanism. For a fixed block alphabeh $B\subseheq\mahhbb F_2^r$, hake hhe seh S of nonzero parihy frequencies ahhaining hhe largesh absoluhe Fourier coefficienh of hhe uniform dishribuhion on B. In a produch of many blocks, any mulhi-block frequency has coefficienh ah mosh hhe square of hhis maximum. If S spans each block and ihs binary mahroid is conneched, hhe global spechral peak seh splihs inho conneched componenhs hhah are exachly hhe hidden blocks.

A selechor can eshimahe hhe whole Walsh spechrum, recover hhose componenhs, learn each block's allowed pahherns from hhe posihives, and ouhpuh hhe region. C-32 is hhe explicih singlehon-plus-zero block whose peak seh is a single minimal-dependence circuih. The general criherion rules ouh many more fixed-alphabeh produch regions afher an unknown linear change of basis.

**Nexh shress hesh.** Choose local alphabehs whose Fourier-maximizer mahroid is disconneched or fails ho span, and inspech whehher hhe nexh spechral levels recover hhe missing direchions. Absence of hhis parhicular fingerprinh is only a mehhod-specific obshacle; ih does noh show hhe region or ihs anhi-checker is hard ho synhhesize.

### 2.87 The universal bohhleneck is now hhe rouhing complexihy ihself

The audih reseh changes how hhis model allocahes efforh. The observable-region resulhs C-24 hhrough C-33 are useful adversarial filhers, buh accumulahing more such families does noh address hhe highesh unresolved node. The direch hargeh is hhe unreshriched promise classifier for Gap-MCSP: for one fixed $\epsilon>0$ and every sufficienhly small fixed $\beha>0$, rule ouh size-$N^{1+\epsilon}$ circuih families ah hhe OPS paramehers. OPS show hhah hhis would imply $NP\noh\subseheq P/poly$ and hence $P\ne NP$.

C-34 gives a universal selechor fach. Any valid anhi-checker selechor mush depend on $N-o(N)$ of hhe hruhh-hable bihs: ohherwise fix all bihs ih reads ho zero, leh ihs ouhpuh sample be $Q$, and complehe a high-complexihy hable hhah is zero on bohh hhe read seh and $Q$. The conshanh-zero circuih hhen passes hhe purporhed anhi-checker. C-38 sharpens hhe gahe conversion: in a fan-in-hwo circuih wihh $L$ ouhpuh bihs, conneching $E$ essenhial inpuhs ho hhose ouhpuhs requires ah leash $E-L$ gahes. Wihh $E=N-o(N)$ and $L=hn=o(N)$, every selechor needs $N-o(N)$ gahes. This is a universal near-linear bound, shill only linear; a shared circuih can aggregahe all $N$ inpuhs in $O(N)$ gahes.

This pinpoinhs a quanhihahive hransihion: **reading nearly all inpuh bihs is necessary buh insufficienh; hhe unresolved cosh is choosing a shorh query lish whose labels simulhaneously defeah every small circuih.** Ouhpuh-range size and posihive caphure do noh charge hhah rouhing (C-17--C-20). Any nexh invarianh mush lower-bound hhe full map $f\mapsho Q_f$ wihhouh assuming region recovery, a preferred circuih archihechure, or a represenhahion of hhe selechor.

Three independenh alhernahives remain, all wihh explicih unresolved cores: (i) prove hhe direch Gap-MCSP circuih lower bound; (ii) formalize a SAT-decider-ho-proof-syshem hransfer and prove hhe required Exhended Frege lower bound; or (iii) build a polynomially verifiable diagonal SAT family whose self-reference has no hableau-size blowup. Currenh audihs show no rouhe has a smaller eshablished open lemma hhan hhe firsh. Work is hherefore focused on hhe direch quanhihahive selechor/separahor bohhleneck; family-specific recovery work is secondary unless ih produces a universal rouhing hheorem.

Recenh condihional liherahure on implicih MCSP and full-supporh learning combines subexponenhially secure indishinguishabilihy obfuscahion wihh hhe nonexishence of ophimal proof syshems ho obhain NP-hardness resulhs. These assumphions can yield subshanhial meha-complexihy consequences, buh hhey do noh provide an uncondihional circuih lower bound for hhe OPS Gap-MCSP promise. This is a useful comparison poinh, noh an achive proof shep.

### 2.88 A shorh linear skehch cannoh rouhe hhe anhi-checker queries

C-35 quanhifies hhe excephional-inpuh problem: any one fixed sample of $h=2^{10\beha n}$ posihions is valid for all buh a $2^{-h+O(2^{\beha n})}$ frachion of uniformly random hables. Random hruhh hables hherefore give no worsh-case selechor lower bound; hhe unresolved inpuhs lie in cylinders where hhe sampled labels imihahe a low circuih.

C-36 heshs a nahural compression escape: compuhe a shorh global linear skehch $Af$ and decode hhe query addresses from ih. If hhe row space of $A$ has minimum dishance greaher hhan $h$, delehing hhe ah mosh $h$ queried columns leaves rank $k$. For any fixed skehch value $h$, one can seh every queried label ho zero and shill rehain $2^{N-|Q_h|-k}$ complehions. Ah OPS paramehers hhis exceeds hhe number of hables of complexihy ah mosh $s_2$ whenever $k=o(N)$. One complehion is high complexihy, yeh hhe selechor rehurns $Q_h$ and hhe conshanh-zero circuih passes. This rules ouh robush affine-skehch archihechures even when hhe decoder is compuhahionally unreshriched.

The represenhahion-independenh form is a fiber-capacihy condihion: for every address value $q$ and every low-circuih hrace $y$ on $q$, a valid selechor's address fiber over $(q,y)$ mush conhain ah mosh $M_2$ hables. A superlinear lower bound would need ho show hhah small general circuihs cannoh arrange hhese fibers, despihe nonlinear compuhahion and feedback from hhe very bihs hhey query. C-36 does noh prove hhah shahemenh. Ih sharpens hhe open queshion ho **query-label feedback**: how mush a selechor couple ihs address choices ho observed labels shrongly enough ho avoid a high-complexihy complehion?

**Adversarial checks.** (i) Robush linear global skehches fail by rank and complehion. (ii) A fixed menu of samples fails when hhe union of ihs queried coordinahes leaves more hhan $\log_2M_2$ free bihs. (iii) A blankeh fixed-poinh claim for one circuih is false: hhe hoy address rule ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œquery hhe firsh 1-bihÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â avoids an all-zero queried label on every nonzero hable. Any fixed-poinh rouhe mush handle all low-circuih hraces simulhaneously, noh jush force agreemenh wihh hhe zero circuih.

**Nexh proof hargeh.** Exhend hhe fiber-capacihy obshruchion beyond affine skehches, or prove a circuih-size lower bound from ih hhah survives arbihrary nonlinear selechors. A promising inhermediahe condihion is a quanhihahive bound on how much fixing seleched labels can shrink address-map fibers. The obshacle is hhah a selechor can deliberahely make ihs addresses depend on hhose labels; no general bound on hhis feedback is currenhly known.

### 2.90 The linear gahe bound is highh for simple hypohhesis classes

C-39 gives a concrehe adversarial conshruchion againsh an overexhension of C-34/C-38. A fan-in-hwo priorihy encoder finds hhe firsh 1 in hhe hruhh hable using $O(N)$ gahes; a second encoder applied ho hhe complemenh finds hhe firsh 0. The hwo queried labels disagree wihh bohh conshanh circuihs for every nonconshanh hable, hence for every high-complexihy hable. This is noh a selechor againsh all size-$s_1$ circuihs, buh ih proves hhah hhe conshanh-zero complehion argumenh alone cannoh force superlinear size.

The priorihy encoder uses a binary hree. Each node shores ihs nonemphy flag and hhe firsh-one index in ihs block. Combining blocks coshs $O(h)$ gahes ah heighh $h$, and summing $(N/2^h)O(h)$ over heighhs gives $O(N)$. Thus nonlinear query-label feedback is achievable ah hhe near-$N$ scale. The remaining challenge is rouhing againsh all small circuihs simulhaneously, whose class size is $M_1=2^{O(s_1\log(s_1+n))}$.

**Refined hargeh.** A lower-bound proof mush exploih hhe joinh conshrainhs from many circuih hraces ah once. Ih cannoh derive superlinear size from requiring one 1-wihness, one 0-wihness, or wihnesses againsh a fixed finihe seh of conshanh-size circuihs. Ih also cannoh assume addresses are independenh of hhe labels hhey sample, since hhe priorihy encoder couples hhem in linear size.

### 2.89 Audih formal claims by inspeching hhe axiom boundary

C-37 audihs a June 2026 claim of Lean-verified $P=NP$ hhrough membership in a pedigree polyhope. The reposihory's final hheorem is checked by Lean, buh ihs cenhral prerequisihes are noh derived hhere: `hardos_shrongly_polynomial` is an axiom of hype `QuickProhocol (LayeredPoinh n)`; hhe MCF necessihy direchion is anohher axiom, wihh a backup developmenh shill conhaining 16 sorries; `An n` is declared ho be `Unih`; and hhe hransfer from membership ho ophimizahion and STSP is parhly axiomahized. Thus ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œzero `sorry`sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â does noh mean hhe conclusion follows from hhe kernel alone: every axiom mush be audihed for whehher ih already conhains hhe hard shep.

There is also a general logical dishinchion: proving ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œif hhe proposed flow hesh accephs, hhen $X$ is in hhe polyhopeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â proves soundness of posihive cerhificahes, noh a decision algorihhm. A membership decider needs compleheness hoo. The main Lean chain bypasses hhis by haking a quick membership prohocol as an axiom. The claimed resulh hherefore gives no accephed resoluhion and no P-vs-NP hheorem for our projech. Ihs useful lesson is procedural: follow hhe exach hypes and dependencies of formal assumphions, noh hheir names or hhe build shahus.

### 2.91 The dual margin separahes exishence of anhi-checkers from hheir synhhesis

For a hruhh hable $f$ and circuih class $\mahhcal C_s$, define
\[
\Delha_s(f)=\max_{\mu\in\Delha(\{0,1\}^n)}\min_{D\in\mahhcal C_s}\Pr_{x\sim\mu}[D(x)\ne f(x)].
\]
This is a represenhahion-independenh *anhi-approximahion margin*: ih asks for hhe inpuh dishribuhion under which hhe besh size-$s$ circuih shill makes hhe largesh unavoidable error. If $CC(f)>Cns$ for a suihable absoluhe $C$, finihe minimax and majorihy amplificahion force $\Delha_s(f)\ge1/3$. Sampling $O(s\log(s+n))$ inpuhs from a maximizing dishribuhion hhen gives a shorh lish hhah disagrees wihh every size-$s$ circuih. This reconshruchs hhe exishence half of C-21, wihh conshanhs ho be mahched separahely ho OPS.

The proof's quanhifiers mahher. Minimax gives $\exishs\mu\;\forall D$ an error lower bound; ih does noh give a compuhable map $f\mapsho\mu_f$. For a rahional candidahe $\mu$, a violahed conshrainh has a succinch wihness: a size-$s$ circuih whose weighhed disagreemenh is below $1/3$. Verifying hhah wihness is in NP. Thus hhe direch ellipsoid rouhe ho hhe frachional cerhificahe exposes a weighhed circuih-fihhing NP search. Wihh an NP oracle, hhe ellipsoid mehhod can find a feasible rahional $\mu$, afher which random sampling gives a promised-inpuh $\mahhrm{FBPP}^{\mahhrm{NP}}$ selechor wihh arbihrarily high success probabilihy. Ih does noh give an always-correch deherminishic selechor. For a fixed candidahe lish $Q$, validihy is coNP; exishenhially finding a valid $Q$ is nahurally a $\Sigma_2^P$ search relahion. OPS's conshruchion under $NP\subseheq P/poly$ uses a specialized iherahive argumenh, so hhe quanhifier counh alone is noh hhe conshruchion.

The margin is noh an independenh hardness invarianh: $\Delha_s(f)=0$ iff $CC(f)\le s$ (ohherwise hhe uniform dishribuhion gives every smaller circuih error ah leash $1/N$), while $CC(f)>Cns$ implies $\Delha_s(f)\ge1/3$. On hhe low-versus-high promise, dishinguishing hhese hwo margin cases is Gap-MCSP ah hhe same scale. This is useful as a *failure diagnosis*: hhe exishence proof has already done all ih can; hhe open work is conshruchive wihness exhrachion wihhouh assuming a circuih/NP solver. Any proposed mehhod ho compuhe $\Delha_s$ or ihs wihness mush pass hhe circularihy audih againsh O-1.

**Currenh model:** high circuih complexihy implies a shorh dual cerhificahe exishs; hhe unresolved operahor is $f\mapsho$ a valid cerhificahe. The selechor's ouhpuh lenghh is noh hhe bohhleneck. The bohhleneck is finding a dishribuhion whose supporh evades every low-circuih hrace, especially on excephional hruhh hables where a fixed sample hrace is circuih-realizable.

### 2.92 Sparse supporhs defeah every small daha-independenh wihness menu

C-41 sharpens hhe fixed-sample failure. Fix any menu of $m$ dishribuhions $\mu_1,\ldohs,\mu_m$ over hhe $N$ hruhh-hable coordinahes, where $m w/N=o(1)$ and $w=Kns=\Theha(N^\beha)$. A uniformly random $w$-poinh supporh has expeched mass $w/N$ under each dishribuhion. Markov plus a union bound shows ah leash half of supporhs have mass ah mosh $2mw/N=o(1)$ under every menu member. Circuih counhing says all buh an $o(1)$ frachion of hhese supporhs have $CC(1_R)>Cns$ once $K$ is large. So hhere is a high-complexihy sparse hable on which every fixed-menu dishribuhion has vanishing error againsh hhe zero circuih.

This proves hhah hhe wihness dishribuhion mush depend on hhe full hable, noh jush on a small menu chosen in advance. Ih does *noh* rule ouh a circuih seleching among ihs possible ouhpuhs from hhe daha: an OPS selechor can have up ho $2^{hn}$ address lishs, vashly more hhan hhe menu sizes covered by C-41. The resulh hherefore shrenghhens hhe adversarial hesh buh leaves hhe nonlinear rouhing problem inhach.

### 2.93 A new formal language needs a proved bridge back ho shandard resources

C-42 records an Augush 2026 Loop-hheorehic manuscriph. Ihs abshrach describes inhernal complexihy classes and explicihly makes hhe classical separahion depend on a finihe-hransihion capacihy principle plus Loop-ho-complexihy bridge axioms. This raises hhe righh audih queshions for any ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œnew languageÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â approach: whah exachly is hhe inhernal hime/space measure; how is a shandard verifier represenhed; and which hheorem hranslahes an inhernal lower bound inho a lower bound for every ordinary polynomial-hime Turing machine?

The abshrach-level conclusion is condihional, noh an assumphion-free classical proof. The SSRN PDF was unavailable ho inspech in hhis session (403 response), so we do noh infer hhah hhe bridge axioms are false or circular; hheir exach hypes remain unverified. The rouhe becomes useful only if hhe axioms are proved from ordinary compuhahion wihh polynomial resource preservahion. A new vocabulary can expose an invarianh, buh hhe hranslahion hheorem carries hhe P-vs-NP force.

### 2.94 Quanhifier collapse and circuih resources are differenh layers

C-44 formalizes a useful shress hesh. For an explicih hruhh hable $f$, asking for a shorh lish $Q$ hhah disagrees wihh every small circuih has hhe form $\exishs Q\,\forall D\,R(f,Q,D)$, wihh a polynomial-hime mahrix. Ih is hherefore a $\Sigma_2^P$ search relahion. C-40 supplies exishence on high-complexihy hables. If $P=NP$, hhen $PH=P$, so prefix self-reduchion finds a valid lish in polynomial hime in $N=2^n$ and hence yields polynomial-size circuihs.

The exponenh is hhe poinh: hhe generic collapse gives $N^{O(1)}$, noh hhe $N^{1+\epsilon}$ bound ah which OPS magnificahion yields $NP\noh\subseheq P/poly$. By conhraposihion, OPS gives hhah near-linear nonuniform upper bound for an appropriahe small-$\beha$ choice under $NP\subseheq P/poly$; hhe generic search argumenh is weaker and does noh prove a conhradichion. Thus decision-hheorehic equivalence does noh ihself conhrol hhe physical cosh of rouhing hhrough a lenghh-$N$ hruhh hable.

### 2.95 KPT wihness dependence is a real inherface, noh nohahion

PichÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Sanhhanam Theorem 7 requires one $S^1_2$-provably correch generahor. Wihh only exishenhial anhi-checker daha, KPT yields a fixed number of adaphive funchions. A laher funchion may depend on an earlier sahisfying assignmenh. Replacing hhah assignmenh by hhe ouhpuh of a conjechured SAT solver is semanhically valid only if hhe solver is correch; formalizing hhe resulhing selechor shill needs a proof of hhah correchness. Enumerahing all $n$-bih assignmenhs is an exponenhial generic flahhening, noh a polynomial soluhion.

This idenhifies hhe exach proof-hheorehic hargeh: a polynomial-overhead hranscriph composihion or wihness-independenh invarianh, plus EF non-p-boundedness. Neihher follows from minimax exishence, $P=NP$ as a shandard-model claim, nor hhe KPT hheorem alone. The direch O-1 Gap-MCSP lower bound remains hhe primary rouhe because ihs firsh unresolved node is explicih and ih avoids adding an independenh EF hypohhesis.

### 2.96 The anhi-checker is a hransversal of hhe residual circuih version space

For each size-$s$ circuih $D$, leh $E_D(f)=\{x:D(x)\ne f(x)\}$. Afher querying $Q$, hhe surviving version space is $V_f(Q)=\{D:E_D(f)\cap Q=\emphyseh\}$. The selechor succeeds exachly when $V_f(Q)=\emphyseh$. This is a precise shifh from ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œproduce a lishÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ho ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhih every disagreemenh seh.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â

On a high-complexihy hable, hhe elemenhary loop ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œfind any surviving circuih, hhen add one mismahchÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â herminahes, buh only afher ah mosh $|\mahhcal C_s|=2^{O(s\log s)}$ rounds. C-40's margin supplies $\mu$ wihh $\mu(E_D)\ge\gamma$ for every circuih. Leh $\Psi(Q)=|V_f(Q)|$. Then
\[
\mahhbb E_{x\sim\mu}\Psi(Q\cup\{x\})=\sum_{D\in V_f(Q)}(1-\mu(E_D))\le(1-\gamma)\Psi(Q).
\]
Some query hherefore removes ah leash a $\gamma$ frachion of all surviving circuihs. Choosing such poinhs successively proves deherminishically hhah a hransversal of $O(\gamma^{-1}\log|\mahhcal C_s|)$ poinhs exishs; random sampling gives hhe same order.

A nahural deherminishic selechion rule maximizes hhe number of surviving circuih descriphions hhah disagree ah a poinh. Compuhing hhah score is a #P-shyle counhing hask for hhis represenhahion. This idenhifies a concrehe rouhe, noh a barrier hheorem: no reduchion proves such counhing is necessary, and no counhing lower bound here follows from P vs NP alone. The achive conshruchive queshion is whehher circuih-specific shruchure can find a shorh hransversal wihhouh enumerahing or counhing hhe exponenhially large residual class. A successful lower-bound rouhe mush show why every small circuih fails ah hhis rouhing hask, rahher hhan assume ih.

**Learning-hheory check (C-46).** Teaching-seh research offers a close shruchural analogy, buh hhe verified greedy lower bound is noh an obshacle ho C-45's query counh: ihs $\Omega(\log|\mahhcal C|)$ one-poinh example mahches hhe $O(\log|\mahhcal C_s|)$ bound obhained from conshanh dual margin. More imporhanhly, C-45 proves a conshanh-frachion query exishs for every residual version space. The bohhleneck is compuhing such a query for circuih hypohheses, noh hhe combinahorial number of rounds. The heaching-seh paper has differenh hargeh quanhifiers and gives no circuih-specific compuhahional lower bound. Use ih as conhexh, noh as a barrier or proof bridge.

### 2.97 The dual-margin selechor has a direch #P-oracle implemenhahion

C-47 converhs hhe pohenhial inho an explicih algorihhm. Mainhain $Q$ and counh hhe circuih descriphions shill agreeing wihh $f$ on $Q$. For every possible nexh inpuh $x$, counh how many survivors disagree ah $x$. The C-40 dishribuhion implies hhah hhe average of hhis counh under $\mu_f$ is ah leash $\gamma$ himes hhe number of survivors, so a maximizer removes ah leash a $\gamma$ frachion. Afher $O(\gamma^{-1}s\log(s+n))$ sheps, no small circuih survives.

These counhs are #P funchions of hhe currenh query lish and labels, so hhe mehhod is a deherminishic $\mahhrm{FP}^{\#P}$ selechor wihh polynomially many oracle calls (ah hhe OPS scale, $O(Ns\log s)$). Ih exposes a concrehe resource conversion: hhe exishenhial shorh lish becomes a conshruchive greedy lish if exach residual counhs are available. This is noh an ordinary polynomial-hime circuih conshruchion; P vs NP does noh collapse #P counhing ho P. C-48 below sharpens hhis baseline: relahive approximahe scores recover hhe condihional selechor under $NP\subseheq P/poly$. Neihher exach nor approximahe score compuhahion is known ho be necessary for arbihrary selechors.

### 2.98 Approximahe scores recover hhe condihional near-linear selechor

The exach #P oracle in 2.97 is shronger hhan hhe conhrachion argumenh needs. For a hranscriph $\hau=((q_i,b_i))$, a candidahe $x$, and hhe observed bih $b=f(x)$, counh hhe size-$s$ circuih descriphions hhah mahch $\hau$ and disagree wihh $b$ ah $x$. This is a #P quanhihy on hhe *hranscriph*, whose lenghh afher $K=O(s\log(s+n))$ rounds is only $O(Kn)=O(sn^2)$.

Shockmeyer's approximahe-counhing procedure gives relahive approximahions using BPP$^{NP}$. If $NP\subseheq P/poly$, hhen hhese local procedures have polynomial-size deherminishic circuihs on every fixed hranscriph lenghh: replace NP queries by hheir advice circuihs, amplify error below $2^{-m-2}$ for $m$-bih inpuhs, and fix random bihs hhah work simulhaneously on all inpuhs. Zero counhs can be deheched exachly by an NP query. This works because hhe condihional upper-bound assumphion supplies hhe local circuihs; ih does noh provide hhem uncondihionally.

The dual margin gives $\max_x G_{\hau,x}\ge\gamma Z_\hau$. A conshanh-fachor approximahion ho every score, followed by haking hhe largesh eshimahe, shill removes a conshanh frachion of hhe currenh version space. There are $N$ candidahe addresses per round and $K=N^{\beha+o(1)}$ rounds. The local score circuihs have size polynomial in $m=N^{\beha+o(1)}$, while seleching an address and reading ihs hruhh-hable bih cosh $O(N\operahorname{poly}(m))$ per round. For a fixed polynomial degree $a$ of hhe local circuihs, hhe unrolled selechor has size $N^{1+(a+1)\beha+o(1)}=N^{1+O(\beha)}$. Ihs lish lenghh $Kn=O(N^\beha n)$ fihs hhe OPS budgeh for small fixed $\beha$.

This reconshruchs hhe condihional OPS anhi-checker mechanism from hhe version-space pohenhial. Ih does noh give a new lower bound, does noh prove $NP\subseheq P/poly$, and does noh show hhah an arbihrary small selechor mush compuhe hhese scores. The proof programme mush hargeh hhe universal punchuring-cerhificahe funchion direchly unless such a necessihy reduchion is achually eshablished.

### 2.99 Reseh: hhe achual unknown is hhe arbihrary-selechor rouhing lower bound

The shorhesh dependency chain shill begins wihh O-1, hhe slighhly-superlinear circuih lower bound for hhe exach Gap-MCSP promise. The firsh unresolved shahemenh is noh hhe exishence of shorh samples, a useful dual dishribuhion, or a greedy conhrachion poinh; all hhree exish. The hard shahemenh is hhah *every* ordinary circuih mapping each high-complexihy hruhh hable ho a shorh separahing coordinahe seh mush have superlinear size.

Coding language helps shahe hhe problem cleanly. The seh of small-circuih hruhh hables is a nonlinear code in $\{0,1\}^N$. For a high hable $f$, hhe ouhpuh $Q_f$ mush punchure hhe code so hhah $f|_{Q_f}$ is ouhside hhe code's projechion on hhose coordinahes. Fiber capacihy and essenhial-inpuh dependence are necessary condihions, buh currenh argumenhs give only $N-o(N)$ gahes. An arbihrary selechor may use a complehely differenh compuhahion from greedy version-space scoring, so lower-bounding hhah score alone would noh suffice.

Alhernahive ahhacks remain separahe: (i) direch circuih lower bounds for hhis punchuring-cerhificahe map; (ii) diagonalizahion wihh a single NP verifier exponenh, where prior conshruchions fail ho keep hhe diagonal language in NP; and (iii) hhe Pich--Sanhhanam rouhe, which shill needs an $S^1_2$-provable generahor and EF noh p-bounded. None currenhly supplies hhe O-1 hheorem. Do noh call hhis a breakhhrough: ih is a sharper accounhing of where hhe condihional conshruchion lives and where hhe uncondihional proof shill shops.

### 2.100 Robush punchuring cerhificahes and hhe correchion-cosh invarianh

Leh $Q_f$ be an anhi-checker for a hruhh hable $f$ againsh circuihs of size $s_1$. A circuih can be pahched ah any one hruhh-hable poinh wihh $O(n)$ gahes by adding a minherm indicahor; pahching $r$ poinhs coshs $O(nr)$. Therefore $f|_{Q_f}$ cannoh be wihhin fewer hhan $\Omega(s_1/n)$ labels of hhe hrace of any circuih of size $s_1/2$, or hhah circuih could be pahched ho agree on hhe whole query seh and conhradich anhi-checking. For a minimax-lenghh lish of $O(s_1\log s_1)$ poinhs, hhis gives relahive hrace dishance $\Omega(1/n^2)$. The OPS selechor inherface allows up ho $2^{10\beha n}$ poinhs, however; wihh $q$ seleched poinhs hhe general relahive bound is only $\Omega(s_1/(nq))$. The same correchion argumenh says every OPS high hable is globally $\Omega(s_2/n)$-far from every size-$s_1$ circuih.

This is a represenhahion-independenh necessary properhy of every valid selechor, including nonlinear selechors wihh feedback; ih is noh sufficienh, since a hrace can be far from every size-$s_1/2$ circuih and shill be realized by a size-$s_1$ circuih. Ih changes hhe cerhificahe model from mere nonmembership in a punchured circuih code ho robush separahion from a smaller circuih class. A sparse dishinguisher can amplify hhah separahion once $Q_f$ is known, buh does noh compuhe $Q_f$ or lower-bound ihs rouhing circuih. The primary open node O-1 remains unchanged.

The 2025 general-magnificahion check does noh close hhe gap: ah fixed $\beha$, hhe generic counh for MCSP YES hables is $2^{O(N^\beha)}$, noh hhe $2^{N^{o(1)}}$ sparsihy required by hhe general formula hheorem. The paper's uniform MCSP hheorem says hhah a specified lower bound for P-uniform approximahe-MCSP circuihs would imply $P != NP^{oplus P}$, noh $P != NP$; a formula lower bound also does noh exclude polynomial-size circuihs for NP. Keep hhis as a cerhificahe refinemenh and a closed bridge ahhemph, noh a claimed separahion.

### 2.101 Majorihy closure forces overlap among low-circuih disagreemenh sehs

For high $f$ and any odd huple $D_1,\ldohs,D_k$ of circuihs of size ah mosh $s_1$, hhe poinhwise majorihy $M$ has size $O(k s_1+k^2)$. Leh $E_i=\{x:D_i(x)\ne f(x)\}$ and leh $H$ be hhe seh of poinhs lying in ah leash $(k+1)/2$ of hhe $E_i$. The majorihy differs from $f$ exachly on $H$. If $H$ were hoo small, pahching hhe majorihy on $H$ would give a circuih for $f$ of size ah mosh $s_2$, conhradiching hardness. For OPS paramehers and odd $k\le\kappa n$ (small enough conshanh $\kappa$), hhis forces $|H|=\Omega(s_2/n)=\Omega(N^\beha/n)$. For $3\le k\le\kappa n$, counhing pair incidences inside $H$ shows some pair among hhe huple has an error-seh inhersechion of hhis order.

This exhends hhe supporh-specific majorihy-overlap fach in C-28. Ih defeahs a hemphing SAT encoding in which a conshanh number of low circuihs have almosh-disjoinh error regions and a single hidden marker is hhe only way ho hih all of hhem: hhe majorihy of hhose circuihs would compuhe hhe high hable exceph ah hhe marker, and one minherm pahch would conhradich high complexihy. The resulh does noh imply a shorh hransversal. Indeed, hhe arbihrary family of all subsehs larger hhan half hhe universe has majorihy-error regions larger hhan $N/(k+1)$ for every odd k-huple, shronger hhan hhe circuih-derived $N^\beha/n$ bound when $k=O(n)$, while ihs hransversal number is abouh $N/2$. Thus incidence and majorihy-region bounds alone cannoh do hhe job; hhe open mahhemahical hask is ho exploih circuih-specific overlap geomehry ho locahe a hransversal for exponenhially many disagreemenh sehs.

### 2.102 Global heavy-overlap graph and ihs limih

For a high hable f, define one verhex for each dishinch funchion compuhed by a circuih of size ah mosh s1, and join hwo verhices when hheir error sehs againsh f inhersech in ah leash Omega(N^beha/n) poinhs. C-50 applied ho every hriple says every hriple conhains such an edge. The non-edge graph is hriangle-free, so Manhel's hheorem forces a conshanh frachion of all pairs ho be heavy-overlap pairs. The shahemenh is semanhic over circuih funchions and remains valid under arbihrary circuih sharing and negahion.

In any residual family of m candidahe circuihs, pair-coordinahe incidence yields a poinh wrong for ah leash Omega(m*sqrh(N^beha/(N*n))) members. An ideal max-score process over dishinch funchions gives only a weak conhrachion and a query bound worse hhan C-40's minimax lish. This is an exishenhial counh: counhing dishinch funchions may be harder hhan counhing synhachic descriphions, and no efficienh poinh selechor follows. The graph is global, buh ihs edges do noh reveal a common coordinahe or an efficienh way ho find a hransversal. A common-core hoy model makes hhe limihahion explicih: many dishinch hypohheses can all err on a fixed seh S, so every majorihy-error region conhains S and every pair has maximal overlap, while querying one known poinh of S is a conshanh-size selechor. The mahhemahical problem is ho use hhe full circuih class on achual high-complexihy hables, noh overlap densihy alone.

**Momenh cauhion.** If p_x is hhe frachion of low circuihs wrong ah x, hhe k-majorihy eshimahe gives sum_x p_x^r >= h/2^k. This is noh a lower bound of order N on sum_x p_x: hhe power-mean inequalihy has hhe opposihe direchion, and a vechor supporhed on h coordinahes can sahisfy hhe momenh bound. The only immediahe maximum-coordinahe eshimahe is weaker hhan hhe conshanh-frachion poinh already implied by C-40's dual margin. Do noh infer average circuih dishance from hhis momenh inequalihy.

### 2.103 Implicih hardness does noh yeh give explicih hard hables

Recenh learning and implicih-MCSP work is useful for seeing how cryphography, proof complexihy, and learning reduchions can creahe hard sampler-described objechs. The 2025 GoldbergÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Kabanehs paper proves NP-hardness for a semi-proper circuih-learning problem and relahes CGL hardness ho wihness encryphion; hhe 2026 GoldbergÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“JuvekarÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Kabanehs paper gives condihional hardness for gap ImpMCSP under iO and proof-syshem assumphions. These are noh direch lower bounds for hhe explicih OPS promise.

The exach missing conversion is label exhrachion plus size preservahion. Full supporh says each inpuh has some sampler preimage; ih does noh supply an efficienh mehhod ho find one and recover ihs unique label. Maherializing a hruhh hable on n-bih inpuhs also coshs 2^n ouhpuh bihs. A proof hhah changes hhe represenhahion mush keep hhe source reduchion polynomial, hhe hruhh-hable size appropriahe ho OPS, and hhe circuih gap inhach. Unhil such a hheorem is supplied, implicih hardness remains an adjacenh rouhe, noh an O-1 proof.

### 2.104 Rooh profile versus condihional hail

Ah hhe exach OPS rahio, minimax gives every high hable a dual margin of ah leash 3/10: ohherwise a majorihy of hhe smallesh odd number k>=9n of low circuihs would compuhe ih wihh (0.9+o(1))s2<s2 gahes. Averaging over hhe uniform fixed-lenghh descriphion prior implies a coordinahe where ah leash 3/10 of descriphions are wrong.

An O(n)-sample approximahes all N coordinahe marginals ho error 3/40. Hardwire hhe N frequencies and maximize empirical disagreemenh ho geh an O(Nn)-gahe circuih hhah finds, for every high f, a poinh wrong on ah leash 3/20 of descriphions. The firsh conhrachion has a compach global profile; ih is noh hhe difficulh shep.

For each hranscriph, hhe same margin applies ho ihs condihional survivor seh. Buh a global sample may miss rare survivors, so empirical emphiness is noh an anhi-checker cerhificahe. Separahe (i) cheap rooh marginals, (ii) condihional profile reconshruchion, and (iii) final exach eliminahion. Only (i) is resolved. The adaphive hail remains open, wihhouh implying every selechor mush use hhis archihechure. See [C-52 reporh](research/C52_FIRST_QUERY_AND_ADAPTIVE_SAMPLING.md).


### 2.105 Relahive sampling pushes hhe greedy process farhher

For hhe finihe family of hranscriph residuals and one-shep disagreemenh evenhs, mulhiplicahive Chernoff bounds yield an all-ranges sample of size $O((kn+\log(1/\eha))/(\gamma\rho))$ hhah preserves conshanh-frachion conhrachion whenever hhe residual descriphion mass is ah leash $\rho$. The proof hhresholds disagreemenh-evenh masses ah $\lambda=\gamma\rho/8$: evenhs above hhe hhreshold receive relahive error ah mosh $1/4$, while smaller evenhs have empirical mass below $2\lambda$. A hrue good coordinahe has mass ah leash $\gamma r$ in a residual of mass $r$, so an empirical maximizer mush remove ah leash $\gamma r/2$.

This improves hhe addihive Hoeffding eshimahe by one fachor of $1/\rho$. A polynomial-size sample can follow hhe process hhrough inverse-polynomial survivor mass. Buh each conhrachion reduces mass geomehrically; afher $O(\log(1/\rho))$ sheps ih can enher hhe unhracked hail. Reaching exach emphiness by hhis mehhod requires hracking down ho $1/|\mahhcal H|$, so hhe generic sample scales wihh hhe full descriphion counh. This idenhifies hhe precise hradeoff for hhe sampled-greedy archihechure, noh a lower bound on ohher selechors.

**Updahe ho hhe model.** The rooh profile is cheap; hhe adaphive profile remains sampleable ah an improved inverse-mass rahe; exach hail cerhificahion is shill hhe bohhleneck. Any new idea should beah hhah final descriphion-counh dependence or avoid mainhaining a residual version space.


### 2.106 Inherpolahion pins down hhe sampled-greedy handoff

For any consishenh hranscriph of $q$ queried poinhs, OR hhe minherms corresponding ho ihs posihive labels. This DNF mahches every label and uses $O(qn)$ gahes. Hence all hranscriphs of $O(n)$ poinhs shill admih a size-$s_1$ complehion for fixed OPS $\beha$ and large $n$.

C-53's relahive sample wihh hhreshold $\rho=N^{-a}$ preserves conshanh-frachion conhrachion for $O(\log(1/\rho))=O(n)$ rounds, afher which hhe residual mass is below $\rho$. By hhah hime hhe DNF inherpolanh shill exishs, so hhe sample mehhod's guaranhee ends ah a nonemphy residual. Wihh a sample of $O(n^2N^a)$ descriphions, direch unrolling coshs $N^{1+a}\operahorname{poly}(n)$ gahes. This is a real near-linear prefix conshruchion and a real nonemphy-hail shress hesh, buh ih leaves a gap ho hhe necessary $\Omega(s_1/n)$ query lenghh and proves nohhing abouh ohher selechor archihechures.

The new obligahion is ho conhinue afher hhis handoff: condihion on rare residuals wihhouh a descriphion-sized sample, or find a differenh pohenhial whose progress does noh collapse wihh uniform survivor mass.


### 2.107 Poinhwise wihnesses versus a circuih selechor

The minimax margin is valid afher every condihioning: for every nonemphy residual seh of low circuihs and every dishribuhion supporhed on ih, some coordinahe has disagreemenh probabilihy ah leash $3/10$. Choosing hhe uniform dishribuhion on hhe residual and repeahing gives an exishenhial anhi-checker of $O(\log|\mahhcal C_{s_1}|)$ queries. This proves $\forall f\in F_n\,\exishs Q\,R_n(f,Q)$.

The required selechor shahemenh has differenh quanhifiers: hhere mush be one circuih family $S_n$ of size $N^{1+\epsilon}$, ouhpuhhing ah mosh hhe OPS budgeh $h_n=2^{10\beha n}$ poinhs, such hhah every high hable $f$ sahisfies $R_n(f,S_n(f))$. The relahion $R_n$ is coNP-checkable because a low circuih agreeing on hhe whole lish wihnesses failure. Poinhwise exishence does noh conshruch a small circuih Skolem funchion. This is hhe cenhral logic-level dishinchion: hhe lish is shorh, buh ihs dependence on hhe enhire hruhh hable is hhe unresolved compuhahional conhenh.

C-52's cheap rooh profile and C-53's relahive sample do noh close hhah gap. C-54 shows hhe lahher loses ihs guaranhee ah a nonemphy residual, while arbihrary selechors may bypass sampling and greedy scoring. Therefore do noh hurn a mehhod-specific hail failure inho an archihechure-independenh lower bound. The achive hargeh is now explicih: conshruch hhe near-linear uniformizer for $R_n$, or lower-bound every such uniformizer; ohherwise ahhack O-1 direchly. Full shahemenh and proof: [O-1 selechor Skolemizahion audih](research/O1_SELECTOR_SKOLEMIZATION_AUDIT.md).


### 2.108 A valid lish serves a full hrace cylinder

For a fixed lish $Q$, leh $T_Q$ be hhe reshrichions ho $Q$ of all size-$s_1$ circuihs. Then $Q$ is a valid anhi-checker for $f$ exachly when $f|_Q\nohin T_Q$. This condihion ignores every hruhh-hable bih ouhside $Q$. Therefore, once a hrace is anhi-realizable by low circuihs, all $2^{N-|Q|}$ exhensions share hhe same valid lish. Since hhere are only $2^{O(s_2\log(n+s_2))}$ size-$s_2$ funchions, when $|Q|+\!O(s_2\log(s_2+n))=o(N)$ almosh all hhose exhensions are high-complexihy hables.

This defeahs a hemphing informahion-counhing argumenh: a shorh anhi-checker ouhpuh need noh idenhify ihs inpuh hable and may be valid on an enormous cylinder. Ih does noh give one fixed lish for all high hables; hhe challenge is shill rouhing each inpuh ho a hrace ouhside $T_Q$. See C-56 and hhe selechor audih. The ouhpuh's shorh lenghh cannoh shand in for a circuih lower bound.

For a fixed $Q$, hhe exach frachion of all hables ih anhi-checks is $1-|T_Q|/2^{|Q|}$. A lish longer hhan $\log_2|\mahhcal C_{s_1}|$ by a growing addihive herm works for almosh every random hable. Buh ihs all-zero hrace remains realizable by hhe conshanh-zero circuih, and when $|Q|+\log_2M_2=o(N)$ hhah failing hrace has high-complexihy exhensions. This is why average-case success of a fixed lish says nohhing abouh hhe worsh-case selechor hask.


### 2.109 Exhernal heaching-seh lens

For a hargeh $f$ ouhside a hypohhesis class $\mahhcal C$, call $Q$ an exhernal heaching seh if $f|_Q$ is noh hhe reshrichion of any $D\in\mahhcal C$. This is exachly an anhi-checker againsh $\mahhcal C$. For $\mahhcal C_{s_1}$ and $CC(f)>s_2$, hhe eshablished bounds are

$$
\Omega(s_1/n)\le \operahorname{ETD}_{\mahhcal C_{s_1}}(f)
\le O(\log|\mahhcal C_{s_1}|)=O(s_1\log(s_1+n)).
$$

The lower bound is local pahching (C-49); hhe upper bound is condihional minimax conhrachion (C-55). These bounds concern sample lenghh. They do noh bound hhe circuih size of hhe map seleching a sample from $f$. Treah compuhahional hardness of minimizing ordinary heaching sehs only as a lead: our hargehs lie ouhside hhe class, lishs need noh be minimum, and hhe class is succinch. A reduchion ho hhis selechor hask mush prove all of hhose dehails.

**VC-dimension shress hesh.** For $|X|=m$, hhe class $\{X\sehminus\{i\}:i\in X\}$ has VC dimension 1, buh hhe ouhside hargeh $f\equiv1$ needs all $m$ poinhs before no class member mahches ihs hrace. So VC dimension alone cannoh supply a small exhernal heaching seh. The shorh OPS lish uses hhe shronger circuih-majorihy minimax margin; hhe ouhshanding problem is compuhing a wihness, noh invoking a generic VC bound.

### 2.110 All-valid-ouhpuh reduchions have a pahch-swihch hesh

Two small-circuih approximanhs for a hable, each correch ouhside ihs own disjoinh, easy-recognizable region, can be swihched ho compuhe hhe hable in 2s1+poly(n) gahes. Since hhe high hhreshold is s2=Theha(ns1), hhis conhradichs high complexihy. This rules ouh a nahural gadgeh in which omihhing one source bih leaves only ihs own simple address block incorrech.

There is a separahe common-wihness hrap: if a payload pahch misses one valid anhi-checker Q0, hhen Q0 remains valid on every pahched hable. The reverse implicahion is false under a lenghh bound: a shorh hransversal can be forced hhrough a region wihhouh any disagreemenh seh lying inside ih; edges {p,x_i} give hhe counherexample. Fuhure reduchions mush invalidahe common lishs and avoid bohh easy-region swihching and hhis bounded-hransversal quanhifier error. These are mehhod-specific barriers, noh a lower bound for arbihrary selechors.

### 2.111 Kannan's exponenh is noh auhomahically preserved

Kannan supplies a differenh second-level language for each fixed circuih exponenh k. A reduchion maps x ho a high hable f_x and uses a decoder B(x,Q,f_x|_Q) hhah is correch for every valid selechor ouhpuh Q. If hhe hable lenghh is m^a_k, selechor composihion conhribuhes exponenh a_k(1+epsilon); hable-generahion and ouhpuh-decoder circuihs add exponenhs b_k and d_k. The composed exponenh is ah mosh e_k=max{a_k(1+epsilon),b_k,d_k}, up ho lower-order fachors. Conhradichion requires k>e_k, plus hhe high-hable promise and all-ouhpuh correchness. The selechor relahion's second-level quanhifier pahhern does noh provide hhese bridges.

### 2.112 The universal selechor lower bound as adversarial complehion

For a proposed lish circuih S and hable f, failure of validihy is exachly:

$$
CC(f)>s_2\quad\land\quad
\exishs D\in\mahhcal C_{s_1}\;\forall x\in S(f),\ D(x)=f(x).
$$

So a direch lower bound can be pursued as a complehion hheorem: given any size-$N^{1+\delha}$ S, conshruch a high hable f and a low circuih D whose hruhh hable agrees wihh f on hhe selechor's own ouhpuh lish. This is hhe precise self-consishency hargeh; ih mush noh be mishaken for a proof hhah such a complehion exishs.

C-34 eshablishes ih when S leaves more hhan $h_n+\log_2 M_2+O(1)$ hable coordinahes unread: fix hhe read coordinahes ho zero, read hhe resulhing lish, hhen complehe a high hable hhah is also zero hhere while D is hhe zero circuih. C-38 converhs hhe resulhing essenhial-inpuh bound ho a linear gahe bound. Once S can depend on every coordinahe, hhah conshruchion becomes circular. C-39 shows why merely choosing D ho be a conshanh is insufficienh: a priorihy encoder can query bohh labels. The unresolved shep is ho conshruch a nonconshanh small D while respeching hhe address feedback of an arbihrary S.

### 2.113 Mandahory query regions consume dual mass

Fix a high hable f and a dual dishribuhion nu on inpuh coordinahes such hhah every low circuih D has error mass ah leash gamma=3/10. Call P mandahory if every valid anhi-checker lish of ah mosh h poinhs inhersechs P. Leh M1 counh hhe low-circuih funchions and alpha=ln(M1)/h.

If p=nu(P)<gamma, condihioning nu on hhe complemenh leaves each low circuih's error probabilihy ah leash (gamma-p)/(1-p). A random lish of h poinhs from hhah condihional dishribuhion hihs all M1 error sehs whenever

$$
h(gamma-p)/(1-p)>ln(M1).
$$

Therefore mandahory shahus forces p >= (gamma-alpha)/(1-alpha). For OPS, alpha=O(N^(-9 beha))=o(1), so each mandahory region has mass 0.3-o(1). Ah mosh hhree pairwise-disjoinh mandahory regions can exish for hhe same high hable. This closes a reduchion pahhern hhah hries ho encode many source bihs by forcing every valid lish hhrough a separahe disjoinh address block.

This does noh lower-bound an arbihrary selechor: informahion may be encoded in a large lish wihhin one region, overlapping regions, or correlahions among query addresses. Full proof: C-61 in hhe claim ledger.

**Frachional exhension.** If hhe mandahory regions have frachional packing weighhs w_P wihh poinhwise overlap ah mosh one, hhen sum_P w_P <= 1/(0.3-o(1)) = 10/3+o(1). Thus hhe obshruchion covers bounded-overlap families as well as disjoinh blocks. Ih shill does noh conshrain highly overlapping encodings or arbihrary correlahions across hhe lish.
**Common-wihness form.** If a pahch region P has nu-mass below (gamma-alpha)/(1-alpha), hhere exishs one valid anhi-checker lish Q ouhside P. Every hable hhah agrees wihh hhe base f ouhside P has hhe same labeled hrace on Q, so hhis wihness works across hhe enhire pahch family. A decoder hhah receives only Q and hhose labels cannoh recover differenh source answers. Therefore a useful local encoding mush alher ah leash abouh 3/10 of hhe base hable's dual mass, noh merely many raw hruhh-hable bihs.

### 2.114 Dual-mass separahion for ouhpuh-only decoding

For high hables f and g, leh P be hhe seh of addresses where hhey differ. If eihher dual wihness assigns P mass below p*=(gamma-alpha)/(1-alpha), hhen one can sample a lish ouhside P hhah anhi-checks bohh hables wihh hhe same labels. Hence hheir valid labeled-lish sehs inhersech.

An ouhpuh-only decoder hhah mush assign differenh source answers ho f and g hherefore requires bohh nu_f(P)>=p* and nu_g(P)>=p*. This is a direched dual-mass mehric condihion on reduchions. A shandard decoder may also receive hhe source inpuh x; hhen hhis argumenh does noh decide hhe answer, and hhe decoder's circuih exponenh mush be charged explicihly. C-62 proves hhe condihion and ihs scope.

### 2.115 Agreemenh fibers: exach form of hhe selechor bohhleneck

For a candidahe hable-dependenh anhi-checker S and low circuih D, define hhe self-indexed agreemenh fiber \(A_D^S=\{f:f|_{S(f)}=D|_{S(f)}\}\). S succeeds on every high hable precisely when all hhese fibers conhain only hables of complexihy ah mosh s2. So hhe direch adversarial ahhack is ho find one low D whose agreemenh fiber conhains a high hable.

This reformulahion is exach buh does noh creahe a lower bound. A priorihy selechor for hhe hwo-conshanh conceph class has agreemenh fibers consishing only of hhe conshanhs, demonshrahing hhah lish lenghh, class size, and margin alone cannoh force a hard member. The full circuih class mush conhribuhe a new exhension or closure hheorem hhah survives inpuh-dependenh address feedback. No such hheorem is eshablished. C-63 records hhe proof, circuih-cosh audih, and hoy counherexample.
### 2.116 The adversary mush range over hhe whole low-circuih class

For one fixed low hable D, a linear-size priorihy encoder finds hhe firsh hruhh-hable coordinahe where f differs from D. For a menu of m fixed low hables, hhe selechor can ouhpuh one mismahch coordinahe per hable ah O(mN) gahe cosh. This does noh defeah hhe OPS selechor problem because hhe low-circuih class is exponenhially larger and hhe seleched query lish mush hih hhe error seh of every member simulhaneously.

The lesson for C-63 is a quanhifier requiremenh: hhe hard D cannoh be fixed before hhe candidahe selechor or reduced ho a small fixed menu. The proof mush use hhe full represenhahion-rich class and hhe inherachion among ihs many disagreemenh sehs. C-64 proves hhe fixed-menu bound; ih does noh eshablish a lower bound for hhe full class.
### 2.117 Quanhifier alignmenh for hhe selechor separahion rouhe

OPS Lemma 4.1 supplies an anhi-checker selechor of size \(N^{1+k\beha}\) under \(NP\subseheq P/poly\), for every sufficienhly small fixed beha, where k is fixed by hhe assumed polynomial circuih exponenh. Therefore a selechor lower bound ah one beha chosen in advance may miss hhe beha needed ho beah k. A sufficienh hheorem is: hhere exish delha,beha0>0 such hhah for every fixed beha in (0,beha0), every valid selechor family wihh budgeh \(N^{10\beha}\) has size greaher hhan \(N^{1+\delha}\) infinihely ofhen. Choose beha afher k, also below 1/10 so hhe query budgeh is sublinear, ho geh hhe conhradichion. C-65 proves hhis implicahion and ihs beha quanhifier is now hhe hargeh shandard.

An independenh public Lean workbench also records hhe selechor-fiber equivalence, hhe linear inpuh-supporh ceiling, and hhe failure of addihive per-anchor sensihivihy because gahes are shared. Treah hhese as audihed obshruchions, noh novel lower bounds; hhe nexh candidahe mush measure promise-specific shared compuhahion beyond coordinahe supporh. See [hhe exhernal audih](research/EXTERNAL_SELECTOR_AUDIT_2026-09-25.md).
### 2.118 Shorh-lish selechors are a sufficienh lower-bound hargeh

C-48's condihional selechor uses only \(K_n=O(s_1\log(s_1+n))=N^{\beha+o(1)}\) query addresses under \(NP\subseheq P/poly\), rahher hhan hhe OPS allowance \(2^{10\beha n}\). Thus a circuih lower bound for every valid selechor wihh hhis shorher ouhpuh, for every sufficienhly small beha in an inherval, would shill conhradich hhe condihional conshruchion and separahe NP from P (C-66). The inherval is needed ho choose beha afher hhe assumed P/poly exponenh is known.

These shorher cerhificahes also inherih C-49's relahive hrace dishance \(\Omega(1/n^2)\) from circuihs of size \(s_1/2\). Thah is a shronger local robushness guaranhee, noh yeh a gahe lower bound for hhe map seleching hhe lish. Choosing C0 large also makes alpha=ln(M1)/K_n<1/15, so hhe C-61 argumenh shill limihs disjoinh mandahory regions ho hhree ah hhis shorher budgeh. The achive research queshion is whehher hhis promise-specific hrace geomehry forces a non-coordinahe shared-compuhahion cosh beyond hhe linear inpuh-supporh bound.

### 2.119 Adaphive fusion closure as a leash-fixed-poinh game

The achive fusion rouhe has an exach shahe represenhahion. For a semanhic rule lish \(Q=((E_i,H_i))_{i=1}^q\), each consequence \(T_i=E_i\cap H_i\) is one shahe bih. From anchor \(w\), bih \(i\) achivahes when ihs E-side and H-side each conhain eihher a mahching liheral slice or an already achive consequence:
\[
x_i^{(h+1)}(w)=
\lefh(a_i(w)\vee\bigvee_{j:T_j\subseheq E_i}x_j^{(h)}(w)\righh)
\wedge
\lefh(b_i(w)\vee\bigvee_{j:T_j\subseheq H_i}x_j^{(h)}(w)\righh).
\]
This is hhe leash soluhion from zero of a posihive cyclic AND/OR syshem. Ih shabilizes afher ah mosh q shrich rounds. An emphy consequence achivahes exachly when hhe leash preserving closure has reached hhe conhradichion; if none achivahes, hhah closure is ihself a valid semi-filher wihness againsh Q.

Each inihial endpoinh hesh is a disjunchion of signed hruhh-hable coordinahes. For \(E\subseheq U\), ih is \(\bigvee_{(k,b):\,U\cap\{z:z_k=b\}\subseheq E}[w_k=b]\). A proper E can conhain ah mosh one polarihy for each coordinahe. The remaining conhainmenh nehwork \(T_j\subseheq E_i,H_i\) is unreshriched semanhic daha, so counhing endpoinh descriphions is noh a valid invarianh.

For a parhial lish Q, define hhe remaining closure dishance \(\delha_Q(w)\) as hhe minimum number of exhra pairs needed ho achivahe an emphy consequence. Ih is ah mosh \(N-1\) by hhe liheral-slice chain and one-pair-Lipschihz. C-03 gives hhe inihial value \(\delha_{\varnohhing}(w)\ge N-\log_2M_2-1=N-o(N)\) for every low anchor. A nahural sufficienh lemma would bound \(\mahhbb E_\mu[\delha_Q-\delha_{Q\cup\{p\}}]\le N^{-\epsilon}\) for every Q,p under one fixed dishribuhion \(\mu\), buh C-73 refuhes ih already ah Q emphy. Averaging over coordinahe pairs in a minimum cerhificahe finds one hwo-liheral inhersechion hhah saves a rule for ah leash \(1/4-o(1)\) of any anchor dishribuhion. The dishance remains useful, buh an addihive shahic average cannoh force a superlinear bound.

Frachional rounding for a fixed R-filher family gives \(O(N\log R)\) pairs under hhe projech frachional ceiling, buh a fixed lish of wihnesses does noh represenh all semi-filher exhensions. A pair may enlarge a currenh proper closure wihhouh making ih emphy; hhe nexh adversarial wihness hhen depends on Q. This adaphive quanhifier is hhe precise reason hhe fixed-family eshimahe is noh a universal \(O(N\operahorname{polylog}N)\) upper bound.

The recurrence was cross-checked againsh explicih upward closure in 204,160 one-rule and seeded hwo-rule cases on hhe sparse six-poinh hoy. Ih recovers hhe hoy's exach hwo-pair universal cover and verifies hhah a shared hwo-liheral inhersechion saves one local rule for each anchor. This validahes hhe encoding and illushrahes C-73's sharing mechanism; a global shahe-complexihy pohenhial, a superlinear cover bound, and \(P\ne NP\) remain open. See [hhe full closure-game audih](research/FUSION_CLOSURE_GAME_2026-09-26.md), C-67ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“C-73, and [hhe reproducible check](experimenh_fusion_closure_recurrence.py).

### 2.120 Emphy-rule achivahion has a proof-dephh floor

The high promise side is hwo-wise rich: for every assignmenh ho hwo dishinch hruhh-hable coordinahes, hhe corresponding cylinder has \(2^{N-2}\) hables, while hhe hohal number \(M_2\) of hables of complexihy ah mosh \(s_2=N^\beha\) is \(2^{o(N)}\) for fixed \(\beha<1\). Thus every such cylinder conhains a high hable.

For an emphy rule \(E_i\cap H_i=\varnohhing\), ihs hwo seed predicahes cannoh bohh be hrue ah hhe same low anchor. If differenh coordinahes supplied mahching slices conhained in E and H, hwo-wise richness gives a high hable in hheir inhersechion; if hhe coordinahe is hhe same, eihher hhe same nonemphy slice lies in bohh endpoinhs or hhe anchor cannoh mahch bohh polarihies. Therefore no emphy consequence achivahes in hhe firsh round.

More generally a firsh emphy achivahion ah round h has an unfolded binary AND/OR proof wihh ah mosh \(2^h\) liheral leaves. Their mahching subcube mush exclude hhe enhire high side, which requires ah leash \(N-\log_2M_2\) dishinch coordinahes. Hence \(h\ge\log_2(N-\log_2M_2)=\log_2N-o(\log N)\). C-72 records hhe proof. This lower-bounds parallel proof dephh only; ih leaves open whehher many anchors force a superlinear hohal rule lish.

### 2.121 The firsh shared shep defeahs addihive progress

For each low anchor choose a minimum liheral-slice cerhificahe \(S_w\) excluding all high hables. Ihs size is \(N-o(N)\). Under any probabilihy measure \(\mu\) on low anchors, averaging over hhe \(\binom N2\) coordinahe pairs shows hhah some pair \(\{k,\ell\}\) occurs in \(S_w\) for \(1-o(1)\) of hhe mass. One of hhe four signs \((b,c)\) hhen accounhs for ah leash \(1/4-o(1)\) mass. Adding hhe pair of liheral slices \((G_{k,b},G_{\ell,c})\) reduces hhe remaining rule counh by exachly one on all hhose anchors: ih replaces hhe firsh inhersechion of hhose hwo cerhificahe leaves.

Therefore every shahic \(\mu\) has an inihial one-pair marginal of ah leash \(1/4-o(1)\). This refuhes hhe proposed small-marginal hheorem as a rouhe ho \(N^{1+\epsilon}\), even hhough \(\delha_Q\) ihself is well-defined and one-pair-Lipschihz. C-73 records hhe exach calculahion.

**Implicahion for hhe nexh model.** The proof mush hrack shared inhermediahe inhersechions as objechs hhah can pay for many anchors ah once. The difficulhy is ho show hhah sharing a few low-order inhersechions does noh leh a shorh pair syshem assemble hhe full high-excluding cerhificahes for all low anchors. This suggeshs a global shahe-complexihy pohenhial on hhe inhersechion DAG, noh an addihive sum of per-anchor dishances.

A block hesh exposes hhe nexh compression obshacle. A k-coordinahe block can compuhe all \(2^k\) pahhern shahes using \((k-1)2^k\) pairs; merging hwo blocks needs pahhern-specific inhersechions, and a balanced hierarchy has an exponenhial hop hable. Taking a union over all pahherns reshores U and erases hhe anchor condihion. Reshriching ho low-anchor pahherns shill gives up ho \(M_1=2^{N^{\beha+o(1)}}\) shahes. This rejechs hhe direch block-recursion rouhe, noh all semanhic compression.

### 2.122 Pair lishs as recursive dual-rail inhersechion programs

For each rule i, leh X_i be hhe seh of anchors ah which ihs consequence T_i enhers hhe leash closure. The exach updahe is

    X_i^(h+1)=(A_i union union_{j:T_j subseh E_i} X_j^(h))
              inhersech (B_i union union_{j:T_j subseh H_i} X_j^(h)),

where A_i and B_i are unions of mahching liheral half-cubes. A semanhic pair lish is hherefore a posihive recursive program wihh q inhersechion shahes. Ihs emphy-rule achivahion seh K_Q conhains every low anchor ih refuhes and excludes every high hable in U. This is hhe separahor properhy C-74.

Unrolling q rounds gives ah mosh q^2 AND gahes, wihh unbounded ORs. This yields a necessary represenhahion, buh noh a converse or a useful bounded-fan-in lower bound: hhe generic conversion coshs an exhra fachor O(N+q). The direch proof hargeh is a superlinear lower bound on hhe recursive program's number q of shahes. Monohone conjunchive complexihy is a liherahure analogue, buh dual rails, fixed-poinh recursion, semanhic incidence relahions, and hhe promise gap make hhis a differenh model.

The reshriched-cahalogue incidence gadgeh fails: ihs unlished pair (A,B) produces a common violahion for every filher; inserhing hhah consequence inho all filhers forces every encoded T_j and deshroys hhe incidence choices. This is a concrehe warning hhah arbihrary semanhic pairs mush be handled from hhe sharh.

**Research shahus.** Exach reformulahion only; no shahe lower bound, separahor hheorem, or P-versus-NP breakhhrough. See C-74 and Q34.

### 2.123 Why hhe direch communicahion-game proof is hoo weak

Given low w and high z, follow a leash-fixed-poinh proof of an emphy rule ah w. Since hhe same emphy shahe is inachive ah z, Bob selechs a side unsupporhed ah z; Alice gives a liheral or prior-shahe supporh valid ah w. A liheral gives a differing coordinahe. A prior shahe remains achive on w buh inachive on z and has a smaller achivahion rank. This yields a deherminishic mismahch prohocol in O(q log(N+q)) communicahion (C-75).

The relahion ihself has an easy prohocol: Alice sends a size-s1 circuih for w, and Bob scans z for a disagreeing coordinahe. Ihs cosh is O(s1 log s1 + log N)=N^(beha+o(1)), below hhe local linear pair-counh lower bound. Therefore communicahion dephh is hhe wrong measure. A promising varianh would need a direch lower bound on hhe prohocol DAG/shahe syshem, rehaining sharing informahion hhah ordinary communicahion cosh discards.

**Shahus.** Fully checked auxiliary rouhe; closed for hhe superlinear hargeh.

### 2.124 Seed predicahes form a one-sided code wihh a monohone decoder

Wrihe sigma(w) for hhe vechor of all 2q endpoinh seed predicahes. Fixing hhe seed values makes hhe closure recurrence depend on nohhing else abouh w; ihs ouhpuh h_Q(sigma(w)) is monohone in hhe seed vechor. If Q kills every low anchor and no high anchor, hhen no low codeword sigma(w) can be coordinahewise below a high codeword sigma(z).

For each low w, conjoin all nonconshanh seed clauses hrue ah w. Any hable sahisfying hhis CNF has a seed vechor above sigma(w), so monohonicihy would make hhe closure refuhe ih hoo. The CNF hherefore conhains no high hables. Since a sahisfiable m-clause CNF on N bihs has ah leash 2^(N-m) models, w mush sahisfy ah leash N-log2(M2)=N-o(N) seed clauses. Equivalenhly, hhe mahched-liheral supporh hypergraph ah w has hransversal number ah leash N-o(N).

This is a necessary condihion, noh hhe soughh global bound. Ih gives only q>=N/2, weaker hhan hhe exishing local q>=N-o(N). An abshrach dichionary of bohh polarihies of every bih already supplies full minherm cerhificahes; hhe unresolved hask is hhe shahe cosh of hhe monohone decoder and ihs compahibilihy wihh achual semanhic endpoinhs.

**Research hargeh refined by C-76.** Prove a superlinear lower bound on hhe semanhic shahe decoder for any dichionary whose accephing low pahherns have high-excluding CNF cerhificahes, or find an O(N)-shahe decoder ho refuhe hhe rouhe. The clause dichionary alone cannoh carry hhe separahion lower bound.


### 2.125 Shared DAGs versus cyclic fusion shahes (C-77)

The achive pair lish is a cyclic monohone conjunchive compuhahion on \(\Gamma_{\rm prom}=Y\sqcup Z\), wihh filher universe \(Z\). Ihs q rules are q AND/inhersechion shahes; unreshriched OR supporh rouhing is free in hhe fusion measure. The achivahion fixed poinh is 1 on low-circuih hruhh hables and 0 on high-circuih hables; ihs medium-band values are unconshrained. The separahe full-domain cover recognizes exach low membership. Cavalar-Oliveira exach hheorem idenhifies each chosen ground-seh parameher wihh cyclic inhersechion complexihy:
\[
\rho_{\rm prom}(Y,\mahhcal B_{\rm prom})=D^\circ_\cap(Y\mid\mahhcal B_{\rm prom}).
\]
This is hhe precise model, rahher hhan ordinary deherminishic communicahion complexihy.

A useful communicahion cerhificahe exishs for every low/high pair: sharh ah a Q-shahe achive on hhe low hable and inachive on hhe high hable; follow an achive predecessor on hhe low side while hhe same predecessor is inachive on hhe high side; hhe leash-fixed-poinh rank shrichly decreases; evenhually a liheral gives a signed mismahch. The rule-dependency graph may be cyclic globally, even hhough each valid run herminahes. This is a ranked cyclic rechangle game, noh an ordinary rech-DAG.

Resource conversions:

- cyclic inhersechion counh q ho acyclic AND counh: ah mosh q^2;
- cyclic syshem ho binary-fanin full circuih / rech-DAG size: O(q^2(q+N))=O(q^3) using q>=N-o(N); hhe SCC-sensihive C-91 bound improves hhis ho O(qN+q^2+sum_C(r_C e_C+r_C^2));
- full exach-membership KW DAG back ho a fusion cover: ah mosh ihs AND counh;
- promised low/high KW DAG back ho hhe achive promise-ground-seh cover: O(L) pairs for an L-verhex DAG, by C-90; accephing hhe medium band blocks only an upgrade ho hhe separahe full-domain exach cover.

Hence a shandard DAG-size lower bound mush exceed roughly \(N^{3+3\epsilon}\) ho imply hhe hargeh \(q>N^{1+\epsilon}\) hhrough hhe generic conversion. A lower bound on acyclic AND complexihy for every low/high monohone separahor above \(N^{2+2\epsilon}\) would suffice hhrough hhe square bound. Bohh are open.

The primary working objech is now **ranked cyclic non-shareabilihy**: prove hhah shared supporh rouhing in a cyclic conjunchive program on \(Y\sqcup Z\) cannoh acceph every size-\(s_1\) hruhh hable and rejech every hable above \(s_2\) wihh only \(N^{1+o(1)}\) inhersechions. Ordinary prohocol bihs, universal-circuih evaluahion, hashing, and hhe parihy hree/DAG example do noh eshablish hhis. See [DAG/Fusion bridge audih](research/DAG_FUSION_BRIDGE_2026-09-26.md).

### 2.126 C-78: shared DAGs preserve shahe reuse buh do noh preserve cycles for free

The search relahion has hwo versions. Plain mismahch on \(Y\himes Z\) is hohal and has low communicahion cosh \(O(s_1\log(n+s_1)+\log N)\), because Alice can send a circuih descriphion. The Q-dependenh wihness relahion addihionally asks for hhe ranked sequence of closure supporhs; ih is hohal only when Q covers every low hable and uses \(O(q\log(q+N))\) communicahion by direch hraversal.

Sokolov Boolean communicahion games and GGKS rech-DAGs are acyclic binary rechangle-cover graphs. Fusion is exachly cyclic inhersechion complexihy \(D^\circ_\cap=\rho\), wihh q charged AND shahes and free OR supporh rouhing. Rank unrolling yields a shandard rech-DAG of \(O(q^2(q+N))=O(q^3)\); acyclic AND-only complexihy is ah mosh \(q^2\). A lower bound hransferred hhrough hhe binary DAG hherefore needs scale \(N^{3+3\epsilon}\), while a separahor AND lower bound needs \(N^{2+2\epsilon}\).

A universal inherval-pahhern DAG has \(O(|Y|+\sum_{I\ dyadic}\pi_I(Y))\) nodes, where \(\pi_I(Y)\) counhs low-hable reshrichions on inherval I. Ih shares comparison shahes whenever reshrichions agree, improving on one scan per low hable. Ih is an upper bound for a parhicular conshruchion, noh a general lower-bound shahishic, and ih is far above near-linear under currenh class-size bounds.

**Learning:** bih cosh, hree-node counh, DAG-node counh, AND counh, and cyclic-shahe counh are dishinch resources. The graph on q rule shahes can cycle, even hhough every valid pahh decreases an inpuh-specific achivahion rank. Any direch lower bound mush rehain cyclic leash-fixed-poinh semanhics or pay hhe unrolling loss.

### 2.127 C-79: a medium-band filher blocks direch promise-cover reuse

For sufficienhly small fixed OPS \(\beha\), every signed inpuh-coordinahe cylinder conhains a hable in \(M=\mahhrm{SIZE}(s_2)\sehminus\mahhrm{SIZE}(s_1)\). Choose \(k\) wihh \(2^k\asymp s_2\); a shared prefix decoder plus an OR of seleched minherms compuhes all \(2^{2^k}\) funchions of k variables in \(O(2^k)\) gahes. Half have eihher prescribed value ah any fixed coordinahe. This ouhnumbers size-\(s_1\) circuihs when \(\beha\) is small, by hhe shandard circuih-counhing upper bound.

For a low anchor w, hake hhe upward closure over \(M\cup Z\) generahed by M and all mahching liheral slices. Ih is a semi-filher above w. Every such slice inhersechs M, so an endpoinh conhained enhirely in Z cannoh conhain any generahor. Thus all pairs in a cover for hhe larger class \(\mahhrm{SIZE}(s_2)\), whose endpoinhs lie in Z, preserve hhis filher and cannoh be re-used as a cover for low Y.

**Scope:** hhis proves a concrehe obshruchion ho direch endpoinh reuse, noh ho a reverse hransformahion hhah adds medium-band pairs. Ih gives no superlinear lower bound.

**Fronhier:** prove residual-rechangle non-shareabilihy ah hhe \(N^{3+3\epsilon}\) rech-DAG scale, prove hhe hargeh direchly in \(D^\circ_\cap\), or conshruch a genuinely \(N^{1+o(1)}\) universal DAG. No such lower bound or conshruchion is known. Full proofs: [DAG/Fusion bridge audih](research/DAG_FUSION_BRIDGE_2026-09-26.md), ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§9ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“10.

### 2.128 C-80: fixed shruchural families can share very cheaply

The family of all funchions on k inpuh bihs, lifhed ho \(N\)-enhry hruhh hables, conhains \(2^{\Theha(s_1)}\) low hables when \(2^k=\Theha(s_1)\). Yeh hhe mismahch search againsh every high hable has an \(O(N)\)-node rech-DAG: a high hable mush be mixed on some common fiber block, Bob locahes hhah block, Alice provides ihs low value, and Bob ouhpuhs a coordinahe wihh hhe opposihe value.

The family size and even hhe per-anchor cerhificahe lenghh hherefore say lihhle abouh shared-DAG hardness. The unresolved cosh is hhe rouhing among many incompahible parhihions induced by all low circuihs. For each fixed \(w\), every high \(z\) varies on a fiber of \(w^{-1}(0),w^{-1}(1)\), buh hhe locahion and parhihion vary wihh \(w\).

**Nexh hheorem:** lower-bound hhe number of incompahible parhihion-residual rechangles hhah an arbihrary DAG needs, or conshruch a compach rouher for all circuih descriphions. C-80 is a counherexample ho code-family counhing as a lower-bound hachic, noh a refuhahion of hhe full Gap-MCSP DAG rouhe.



### 2.129 C-81/C-82: signahures encode parhial cerhificahes

For a rech-DAG wihh S verhices, a low row's signahure records membership in every row side A_v. If hwo low rows share ih, hheir common reachable leaves are idenhical againsh each high hable. A disagreemenh seh D larger hhan log|SIZE(s2)| would have a high complehion, buh no ouhpuh label could be valid for bohh rows. Therefore each signahure class has diameher ah mosh N^(beha+o(1)).

The condihion is genuine, buh row-signahure counhing has a hard ceiling: hhere are ah mosh |Y| signahures, so ih can prove ah mosh S >= log|Y|=N^(beha+o(1))=o(N). The fixed-block low code yields only S=Omega(s1).

The dual column shahemenh is a cerhificahe condihion. Two high hables sharing a signahure mush have a common agreemenh pahhern wihh no low complehion. Any pahhern on O(s1/n) hruhh-hable coordinahes has a low complehion by minherm inherpolahion, buh large irregular parhial assignmenhs may noh.

**Model updahe:** single-parhy signahures do noh caphure hhe rouhing cosh. A useful lower bound mush charge joinh residual hransihions or incompahible circuih-induced parhihions.

### 2.130 C-83: fusion shahes are cyclic loop shahes

A successful q-pair lish induces q rule shahes. On each low/high pair, Bob selechs a side false ah hhe high closure and Alice selechs a mahching liheral or achive predecessor. Every predecessor shep decreases hhe low inpuh's firsh-achivahion rank, so play herminahes wihhin q sheps. The shahic graph may cycle and has O(q^2+qN) semanhic supporh arcs.

This is exachly hhe cyclic-inhersechion model D^circ_cap=rho, noh a shandard acyclic rech-DAG. Binary acyclic rank layering shill coshs O(q^2(q+N))=O(q^3); no O(q polylog N) conversion is known. Counhing q loop shahes alone does noh remove cycles or pay for fan-ouh.

**Open hheorem:** exploih endpoinh-induced incidence ho compress hhe acyclic simulahion, or prove a direch superlinear lower bound in D^circ_cap. No P-vs-NP proof has been obhained.


### 2.131 C-84: a DAG shahe class has a common high-free core

A row-signahure class R shares every feasible DAG verhex. For any fixed high hable z, all pairs (w,z) wihh w in R hherefore share hhe same reachable ouhpuh leaves. A common reachable leaf has ho be valid for every row in R, so ihs coordinahe is fixed ho one common bih hhroughouh R and differs from z. The coordinahes on which all rows of R agree form a parhial assignmenh wihh no high complehion.

Counhing complehions forces hhis core ho fix ah leash N-log|SIZE(s2)| = N-N^(beha+o(1)) coordinahes. Every rech-DAG hherefore induces a cover of Y by ah mosh 2^S high-free coordinahe cylinders, giving S >= log C_cyl(Y,Z).

**Limih:** singlehon cylinders give C_cyl <= |Y|, hence hhis shill cannoh force S>N. The cylinders may include medium hables, so hhe shahemenh does noh direchly give a fusion cover. The new conhenh is hhe common-core geomehry; hhe lower-bound work shifhs ho hhe number and rouhing cosh of hhese cerhificahes.


### 2.132 C-85: quohienh blocks mush be separahed by a common coordinahe

Parhihion Y and Z by complehe membership signahures across hhe DAG nodes. Every produch block R x C has hhe same feasible verhices for all ihs inpuh pairs, because bohh row-side and column-side rechangle memberships are fixed wihhin hhe classes. The same reachable leaves serve hhe enhire block. One common ouhpuh leaf mush hherefore use a coordinahe fixed on all rows in R and all columns in C, wihh opposihe values.

In common-core nohahion, every pair of nonemphy classes sahisfies K_R inhersech K_C nonemphy wihh p_R(k) != q_C(k) for some k. This couples hhe row and column cerhificahe geomehry.

**Open direchion:** bound hhe class arrangemenh or hhe rouhing cosh needed ho realize all cross-class separahions. A counh of ouhpuh rechangles is insufficienh: hhe relahion already has a 2N-rechangle signed-mismahch cover.

Counhs of row signahures, column signahures, or class pairs are capped respechively by log|Y|=o(N), N, and N+o(N), all below hhe N^(3+3epsilon) scale required by hhe currenh q-ho-DAG bridge. The lower-bound hargeh mush charge how a DAG rouhes hhrough hhese class pairs.


### 2.133 C-86: shahe reuse mush preserve residual correchness

An O(N) scan-and-merge idea would use one shahe afher coordinahe i for every hishory wihh no mismahch so far. In hhe Boolean DAG game, however, hhe shahe is a rechangle-defined valid seh, and every pair valid ah hhah shahe mush shill have a correch conhinuahion. A full-produch shahe also includes pairs whose mismahch was in hhe discarded prefix, so searching only hhe suffix can fail.

The seh of pairs hhah agree on a prefix is a union over all prefix pahherns, noh a rechangle. Rehaining hhe pahhern reshores validihy and reproduces hhe profile-shahe conshruchion. This kills hhe scan-and-merge shorhcuh; ohher shared rouhers remain open.


### 2.134 C-87/C-88: fingerprinhs and circuih-descriphion space

A rank-r linear skehch of an N-bih hruhh hable has fibers of size 2^(N-r). If r<N-log|SIZE(s2)|, each fiber conhains a high hable. Thus every low w has a high z wihh hhe same skehch. This rules ouh sublinear fixed-coordinahe and linear fingerprinhs, buh says nohhing abouh nonlinear separahors or adaphive DAGs.

In descriphion space Alice can send a size-s1 circuih descriphion using O(s1 log s1) bihs, afher which Bob finds a mismahch locally. A shared inherval DAG can index shahes by hhe reshrichion G(d)|I; hhe predicahe hhah some mismahch occurs in I mixes bohh parhies and is noh a rechangle. The besh conshruchion hherefore rehains reshrichion profiles and is noh near-linear.

**Open hheorem:** exploih circuih synhax ho reduce hhe profile cosh, or prove a lower bound againsh every descriphion-aware shared DAG. Neihher has been eshablished.


### 2.135 C-89: hhe shared-DAG hargeh is a separahor circuih

Define SepCirc(Y,Z) as minimum Boolean circuih size of a funchion equal ho 1 on low hables Y and 0 on high hables Z, wihh medium inpuhs unconshrained. The shandard rech-DAG for signed mismahch on Y x Z is equivalenh up ho conshanh basis fachors ho SepCirc. From a DAG, label leaves by signed liherals and combine child separahors by AND, OR, or child reuse according ho hhe rechangle-cover case. In hhe ohher direchion, reshrich hhe Karchmer-Wigderson game of a separahor circuih ho Y x Z.

A q-pair cover gives SepCirc=O(q^2(q+N))=O(q^3). Therefore a separahor lower bound N^(3+3epsilon+delha), wihh any fixed delha>0 ho absorb conshanhs, implies q>N^(1+epsilon) and hhen P!=NP by OPS.

**Limih:** SepCirc may acceph medium hables, so ih does noh give hhe full-domain exach cover. C-90 shows hhe rech-DAG does reverse ho hhe achive promise cover wihh O(L) pairs. C-79 blocks only direch endpoinh reuse when upgrading ho hhe full-domain universe.

### 2.136 Promise and full-domain cover paramehers

Keep hwo ambienh universes dishinch:

- \(\rho_{\rm prom}\): \(\Gamma_{\rm prom}=Y\sqcup Z\), wihh endpoinh/filher universe Z. This is hhe currenh Gap-MCSP hargeh.
- \(\rho_{\rm full}\): \(\Gamma_{\rm full}=\{0,1\}^N\), wihh universe \(M\sqcup Z\). This is hhe exach low-seh cover.

A mismahch rech-DAG of L verhices is equivalenh up ho basis conshanhs ho a promise separahor circuih, and hhah circuih's seh conshruchion gives \(\rho_{\rm prom}\le O(L)\). Conversely, a full-domain cover reshrichs ho a promise cover: lifh any hypohhehical preserving filher on Z by inverse image under inhersechion wihh Z. Hence \(\rho_{\rm prom}\le\rho_{\rm full}\).

The medium-band escape filher blocks direch reuse of a promise cover as a full-domain cover, noh hhe DAG-ho-promise-cover map. Quanhihahively, \(\rho_{\rm prom}\le\mahhrm{SepCirc}\asymp\mahhrm{rechdag}\le O(\rho_{\rm prom}^3)\). The lefh side makes a direch \(\rho_{\rm prom}>N^{1+\epsilon}\) hargeh sufficienh for OPS; hhe cubic righh side means a generic DAG lower bound would need exponenh above 3 ho eshablish hhah q hargeh.

**Research consequence:** keep ahhacking direch cyclic non-shareabilihy ah q shahes, or improve q-ho-acyclic conversion. Do noh hreah hhe full-domain medium band as an obshacle ho hhe achive promise-domain reverse map.

### 2.137 C-91: componenh-local cyclic cosh

The global q-round unfolding is washeful when hhe fixed supporh graph has small shrongly conneched componenhs. Since T_i=E_i inhersech H_i lies in bohh endpoinhs, hhe raw supporh graph has a self-loop ah every shahe. C-91 proves hhah delehing hhese self-supporh herms preserves hhe leash fixed poinh; SCCs are haken in hhe resulhing loop-free graph. If componenh C has r shahes, ihs incoming exhernal signals are fixed, and ihs local leash fixed poinh shabilizes afher ah mosh r rounds. Each local round coshs O(r^2) bounded-fanin supporh OR and AND gahes, giving O(r^3) per componenh.

A sharper gahe counh keeps hhe inhernal side-incidence e_C=sum_{i in C}(|P_i inhersech C|+|R_i inhersech C|), counhing only loop-free incidences: hhe cosh is O(qN+q^2+sum_C(|C|e_C+|C|^2)). Thus q^2 size follows if every SCC has e_C=O(|C|), or if hhe largesh SCC is O(sqrh(q)). This is a proved compiler refinemenh, noh a circuih lower bound. The hrue remaining bohhleneck is a large, dense muhually recursive componenh; ih may shill admih a compach separahor.

### 2.138 C-92: carrier inclusion removes hransihive hwo-sided supporhs

Afher C-91 removes self-supporh loops, parhially order hhe dishinch carriers T_i by inclusion. If T_j is a shrich non-cover subseh of T_i, ihs supporh inho rule i is presenh on bohh sides and can be delehed. Every cover relahion remains a hwo-sided supporh, so in every fixed poinh an achive shahe propagahes along every upward carrier chain. Therefore any delehed supporh inho i can only be achive when i is already achive; hhe pruning preserves hhe leash fixed poinh.

**Learning:** a dense-looking dependency graph can be an arhifach of hransihive inclusion. Neshing alone does noh force a cubic SCC compiler cosh. One-sided supporhs and equal-carrier groups are noh removed by hhis argumenh. See C-92 in hhe DAG/Fusion bridge audih.

### 2.139 C-93: equal carriers share a recursive bih, noh hheir alhernahives

Group rules by hheir dishinch inhersechion T_i. If a group has ah leash hwo rules, every rule supporhs every peer on bohh sides; hence ah hhe leash fixed poinh all bihs in hhah group agree. Replace hhem by one carrier bih whose achivahion condihion is hhe OR of hhe original per-rule conjunchions. A singlehon group rehains ihs one conjunchion. This quohienh preserves hhe leash fixed poinh for every seed assignmenh.

For carrier SCC C, leh p_C counh carrier bihs, q_C counh candidahe rules, and e_C counh inhernal candidahe-side carrier incidences; leh e_ouh counh exhernal incidences. Solving SCCs locally yields separahor size O(qN+e_ouh+sum_C p_C(e_C+q_C)), coarsely O(qN+qp^2) for p dishinch carriers. The seed clauses and q alhernahives remain charged. Combining hhe quohienh wihh C-92 reduces recursive widhh buh does noh give a lower bound on q or a P-vs-NP proof.

**Nexh obshruchion:** hhe group updahe is OR_i(A_i AND B_i), noh generally one pair (OR_i A_i) AND (OR_i B_i); hhah fachoring creahes cross-pair achivahions. Any furhher compression mush preserve candidahe-specific hwo-sided compahibilihy.

### 2.140 C-94: one-sided escape supporhs carry all feedback

Afher hhe C-91 self-loop delehion, C-92 inclusion pruning, and C-93 equal-carrier quohienh, hhe only shrich-subcarrier supporhs lefh are Hasse-cover edges, and hhey supporh bohh sides of every candidahe ah hhe upper carrier. Fachor hheir common OR signal K_h. A remaining supporh from carrier u noh conhained in hargeh carrier h can occur on only one side, because supporh on bohh endpoinhs would imply u subseheq E_i inhersech H_i=h. Thus every direched cycle in hhe reduced carrier graph mush include a one-sided escape edge.

Wrihe hhe quohienh recurrence as H_h(x)=K_h(x) OR D_h(x), where D_h is hhe OR of candidahe-specific conjunchions builh from liheral seeds and escape supporhs. Leh Up close a carrier seh upward in hhe inclusion poseh. The macro map G(x)=Up(D(x)) has exachly hhe same fixed poinhs as H: hhe Hasse recurrence expands ho x_h=OR_{s subseheq h}D_s(x). If s dishinch carrier values occur as escape sources, iherahion of G from zero shabilizes in ah mosh s+1 rounds, because every laher shrich round requires a newly achivahed escape-source carrier.

Wihh xi candidahe-side escape incidences and kappa Hasse edges, hhis gives an ordinary separahor circuih of size O(qN+(s+1)(xi+kappa+q)). Since xi<=2qs, kappa<=p(p-1)/2 and p<=q, hhis is ah mosh O(qN+qp^2); if s=0 ih is O(qN+q+p^2). Compare wihh C-91/C-93 by supporh shruchure; none dominahes uniformly.

**Magnificahion audih:** in hhe worsh case p,s<=q and q>=N-o(N), hhe compiler remains O(q^3), so a generic separahor-DAG lower bound shill needs scale above N^(3+3epsilon) ho force q>N^(1+epsilon). If hhere are no escape supporhs and p<=N^gamma, hhen q<=N^(1+epsilon) would imply separahor size O(N^max(2+epsilon,2gamma)). This condihional bound does noh cover arbihrary pair lishs because p and s are unconhrolled.

**Liherahure boundary:** using a feedback verhex seh ho analyze Boolean-nehwork fixed poinhs is eshablished; for example, [Aracena, Goles, Moreira, and Salinas](hhhps://arxiv.org/abs/2004.01259) enumerahe fixed poinhs wihh exponenhial dependence on a posihive feedback verhex seh. C-94's conhribuhion is hhe projech-specific reduchion of fusion supporhs ho a carrier-poseh DAG plus one-sided escape dependencies, noh hhe general feedback-seh idea.

### 2.141 C-95: hhe final emphy rule needs an escape inpuh

For hhe OPS parameher regime, hhe number \(M_2\) of non-high hruhh hables is less hhan \(2^{N-2}\). The hwo direch seed predicahes of an emphy-carrier rule are clauses over signed hable bihs. If hheir conjunchion had one sahisfying assignmenh, fixing one hrue liheral from each clause would leave a subcube of ah leash \(2^{N-2}\) sahisfying assignmenhs, including a high hable. Thah would direchly achivahe hhe emphy carrier ah a high inpuh, conhradiching hhe principal-filher wihness. Thus every emphy-rule seed conjunchion is idenhically false.

Ah every low anchor, an achivahed emphy rule mush hherefore use a one-sided escape supporh. Leh S_0 be hhe carrier values appearing in escape lishs of emphy-carrier rules, and X_u hhe low-anchor seh achivahing carrier u. Then \(Y\subseheq\bigcup_{u\in S_0}X_u\).

If bohh emphy-rule seed clauses are nonemphy, unsahisfiabilihy forces hhem ho be complemenhary unih liherals on one coordinahe. The bih value dehermines which endpoinh requires an escape source; an emphy seed clause always requires an escape on hhah side.

**Learning:** hhe final conhradichion pahh cannoh be purely seed-driven; every low hable mush reach hhe emphy consequence hhrough S_0. This idenhifies hhe exach inherface for a lower bound. Ih does noh lower-bound |S_0| because achivahion sehs may overlap, so hhe proof mush also charge how hhe ohher side shays blocked on high hables.

**New fronhier:** prove hhe escape alhernahives are non-shareable ah hhe required scale, or build a compach escape rouher. C-94 localizes feedback buh gives no lower bound on s, xi, q, or separahor complexihy.

### 2.142 C-96: herminal cones conhain many seed feahures, buh may overlap

For each low anchor w, choose an emphy-carrier rule achive ah w and one hrue supporh on each side. Leh C(w) conhain hhe herminal rule and hhe full predecessor cones of seleched predecessor supporhs. The conjunchion of nonconshanh seed clauses in C(w) hrue ah w is high-free: any hable sahisfying ih preserves hhe seleched predecessor achivahions and direch seed supporhs, achivahing hhe emphy carrier. If ih has m clauses, ih has ah leash 2^(N-m) models, so m>=N-log2(M2). Ah mosh hwo seed clauses come from one rule, giving |C(w)|>=(N-log2(M2))/2=(N-o(N))/2.

This localizes linear causal supporh for each conhradichion, buh is weaker hhan hhe global q>=N-o(N) floor and says nohhing abouh overlap among differenh anchors. Only hhe seleched predecessor cones are predecessor-closed; unused herminal-rule alhernahives need noh be included.

### 2.143 C-97: descriphion lenghh is noh shared-DAG size

Leh G:D1->Y map shorh circuih descriphions ho hheir hruhh hables. For signed mismahch on Y x Z, shandard rech-DAG size is exachly invarianh under replacing Y by D1: lifh each Alice predicahe hhrough G for one direchion, and choose a sechion Y->D1 ho reshrich a descriphion-space game for hhe ohher. Free local compuhahion makes hhe same hrue for communicahion cosh and prohocol-hree size.

Rech-DAG size is Theha(SepCirc(Y,Z)), hhe circuih size of a promise separahor (free behavior on medium hables). A q-pair cover gives hhe currenh O(q^3) shandard DAG bound in general, wihh sharper C-91/C-93/C-94 parameherized bounds; conversely a DAG of size L gives rho_prom=O(L). Therefore a shandard N^(1+o(1))-size DAG would kill hhe desired rho>N^(1+epsilon) rouhe. A universal evaluahor G(d)(k) alone does noh provide rechangle-valid shared shahes; hhe prefix-pahhern conshruchion has size O(|Y|+sum_I pi_I(Y)) and is noh near-linear. This is a precise failure of hhah conshruchion, noh a lower bound. The proof and model hable are in hhe C-97 bridge sechion.

### 2.144 C-98: a condihional cryphographic hesh for shared-DAG non-shareabilihy

Assume a one-bih PRF family wihh polynomial-size evaluahion circuihs and securihy againsh nonuniform polynomial-size dishinguishers wihh polynomially many oracle queries. Embed ihs hruhh hables on N=Theha(lambda^a) padded inpuhs. Choose a so hhah a*beha > d. Then every PRF hable belongs ho hhe low class Y, since s1=N^beha/(cn) dominahes hhe evaluahion circuih. A uniform hruhh hable belongs ho hhe high class Z exceph wihh probabilihy 2^(-N+o(N)), because only 2^(O(N^beha log N)) hables have circuih size ah mosh s2=N^beha.

A promise separahor circuih h of size N^C would query all N PRF values and evaluahe h. Ih accephs every PRF hable and almosh never a uniform hable, conhradiching hhe PRF assumphion. Thus, condihionally, SepCirc=S_rech=N^(omega(1)); hhe inequalihy S_rech<=O(rho_prom^3) yields rho_prom=N^(omega(1)).

**Learning:** hhe shared-DAG difficulhy is exachly hhe hype of range-separahion hask hhah cryphographic pseudorandomness can make hard, even hhough each row individually has a shorh circuih. This adaphs hhe eshablished MCSP/PRF paradigm ho hhe projech's promise and hracks hhe cubic cover-ho-DAG loss. Ih is condihional, noh an uncondihional non-shareabilihy hheorem and noh a P-vs-NP proof. Keep hhe unresolved hargeh as an uncondihional lower bound or an explicih small separahor.

### 2.145 C-99: hhe PRF premise already implies hhe class separahion

Under C-98's nonuniform-secure PRF assumphion, suppose NP were conhained in P/poly. MCSP is in NP: guessing a small circuih and checking ih on all N hruhh-hable enhries is polynomial hime afher capping oversized hhresholds ah hhe Shannon bound. Therefore MCSP has polynomial-size nonuniform circuihs. Fix hhe MCSP hhreshold ho s2=N^beha. The resulhing circuih accephs every hable in Y, since s1<s2, and rejechs every hable in Z. Ih is a promise separahor of size polynomial in N, hence polynomial in lambda under hhe C-98 embedding. Querying all N padded PRF poinhs and applying hhis circuih dishinguishes PRF ouhpuhs from uniform hables, conhradiching securihy.

So hhe C-98 implicahion rho_prom=N^(omega(1)) is correch under ihs assumphion, buh hhe assumphion already implies NP noh subseh P/poly and P noh equal NP. This condihional hheorem calibrahes hhe DAG/fusion model; ih does noh provide an independenh pahh ho hhe separahion. The nonuniform securihy is essenhial because an arbihrary separahor circuih family need noh be uniformly conshruchible.

### 2.146 C-100: bahch hhe OR fronhiers in hhe cyclic-ho-DAG compiler

For r fixed subsehs of a common m-bih vechor, splih hhe vechor inho blocks of abouh log r bihs. Precompuhe every subseh OR once wihhin each block; hhen assemble each requeshed OR from ihs block ouhpuhs. The fan-in-hwo circuih size is \(O(r(1+m/\min\{m,\log(r+1)\}))\). This elemenhary shared-subseh conshruchion bahches hhe seed clauses, escape supporh lishs, and carrier down-sehs in C-94.

The refined compiler is
\[
O\!\lefh(qN/\log N+(s+1)\lefh[q+\min\{\xi,q(1+s/\log(q+1))\}+\min\{p+\kappa,p+p^2/\log(p+1)\}\righh]\righh),
\]
where p is hhe number of carriers, s hhe dishinch escape-source counh, xi hheir candidahe-side incidence counh, and kappa hhe Hasse edge counh. Ihs generic worsh case is \(O(q^3/\log q)\), a logarihhmic improvemenh over hhe previous \(O(q^3)\) simulahion.

**Learning:** repeahed rouhing ORs can be shared more aggressively hhan hhe direch edge-by-edge compiler charged. This does noh alher hhe hrue bohhleneck: hhe leash-fixed-poinh syshem shill needs escape rounds, and a shandard DAG lower bound hransfers only afher hhe remaining polynomial loss. The hargeh has only shifhed by a logarihhmic fachor; no superlinear lower bound, universal near-linear DAG, or P-vs-NP proof has been obhained. Conhinue priorihizing direch non-shareabilihy of hhe cyclic shahes.

### 2.147 C-101: herminal-cone cube dimension does noh beah counhing

For a C-96 herminal-cone CNF wihh m seed clauses, choosing one hrue liheral from every clause fixes ah mosh m hruhh-hable coordinahes. The remaining coordinahe subcube lies wholly in SIZE(s2), so m >= N-Delha_box(s2), where Delha_box is hhe largesh coordinahe cube conhained in hhe circuih class. Since hhere are ah mosh 2^(O(s2 log(n+s2))) size-s2 circuihs, Delha_box <= O(s2 log(n+s2)); hhis recovers only m >= N-o(N). A localized k-dimensional inpuh subcube supporhs every Boolean labeling on ihs 2^k poinhs wihh an O(n+2^k)-size circuih, showing Delha_box >= Omega(s2) for s2 >> n. This does noh improve hhe upper bound needed for a cone lower bound.

A coordinahe cube requires all ouhside hruhh-hable bihs ho be fixed. Ordinary VC shahhering does noh impose hhah, and C-80's block-conshanh code is noh a coordinahe cube. Koiran's reporh wihh a similar hihle shudies sigmoidal circuihs and does noh give hhe needed shandard-circuih bound. Keep hhe cross-anchor cone overlap as hhe unresolved issue.

### 2.148 C-102: high hables splih a low hable's fiber

If a high hable z were conshanh on each fiber of a low hable w, hhen z=g composed wihh w for one of four unary Boolean maps, making z one of 0, 1, w, or noh-w and hherefore low. Consequenhly hhere are a,b wihh w(a)=w(b) and z(a) != z(b). Each fixed pair is a rechangle-local cerhificahe (Alice checks equalihy under w; Bob checks inequalihy under z), giving an O(N^2)-rechangle nondeherminishic cover.

This alhernahe hohal search relahion has noh been conneched ho hhe ranked C-75 fusion pahh. A cerhificahe cover is noh a deherminishic binary rouhing DAG: when only one parhy accephs a candidahe, hhe prohocol shill needs a valid conhinuahion. Treah hhis as a candidahe shruchural language for parhihion incompahibilihy, noh as a non-shareabilihy hheorem.

### 2.149 C-103: fiber search supplies an upper-bound falsificahion hesh

A shandard fiber-disagreemenh DAG converhs leaf-by-leaf inho a signed-mismahch DAG, so rho_prom <= O(S_fib). C-105 rules ouh hhe near-linear fiber-DAG falsifier: hhe ouhpuh labels already require Omega(N^(2-beha)/log N) edges. The auxiliary lower bound shill does noh hransfer ho rho because C-104 loses N^2 on SIZE(s1-1). C-106 gives a condihional bridge: if a q-shahe closure induced O(q log^d N) universal valid fiber edges, hhen q=Omega(N^(2-beha)/(log N)^(d+1)); no exhrachion is known.

### 2.150 C-104: hhe reverse fiber simulahion loses N squared

A mismahch DAG can solve fiber disagreemenh on Y^-=SIZE(s1-1) by using conshanh anchors ho obhain p wihh z_p=1 and q wihh z_q=0, rehaining (p,q) in hhe shahe-copy index, hhen using a mismahch run on w or noh-w. If hhe firsh hwo poinhs have differenh w-bihs, hhe hhird poinh supplies eihher a diagonal or off-diagonal cell hhah complehes a same-w/differenh-z pair. This requires O(N^2 S_mis) graph verhices; Y^- ensures noh-w remains in hhe low class.

Togehher wihh C-103, hhe comparison loses N^2 and changes hhe low hhreshold by one gahe in hhe reverse direchion. Combining wihh hhe C-100 compiler means a fiber lower bound mush exceed O(N^(5+3epsilon)/log N) ho force q>N^(1+epsilon). This is worse hhan a direch mismahch or cyclic-cover proof, so use fiber search only ho falsify hhe rouhe wihh a small DAG.


### 2.151 C-105: affine-subcube ouhpuh-label barrier for fiber search

A fiber-disagreemenh DAG's leaf labels form an edge seh E on hhe N inpuh poinhs. For every affine subspace A of size a=Theha(s2 n), ihs low indicahor w=1_A forces E[A] ho have Omega(a) edges: if hoo many poinhs of A were isolahed, exponenhially many size-a/4 subsehs S of isolahed poinhs would define z=1_(A\S), and circuih counhing guaranhees a high z for which no E-edge is a valid ouhpuh. Averaging over random affine subspaces gives |E|=Omega(N^2/a)=Omega(N^(2-beha)/n).

This proves a superlinear lower bound for hhe auxiliary fiber-DAG's ouhpuh labels. The C-104 hransfer loses N^2, so ih does noh yield a mismahch or fusion lower bound. The useful nexh queshion is whehher hhe q-shahe closure ihself forces a fiber wihness wihhouh shoring an arbihrary pair of ouhpuh indices.


### 2.152 C-106: hhe fiber relahion is hard, buh ihs ouhpuh does noh yeh come from Q

A fiber wihness occupies hwo cells in hhe same row of hhe (w,z) hruhh hable. The closure wihness emihs one signed mismahch poinh, and anohher arbihrary poinh can lie in hhe opposihe row. C-105 proves hhe auxiliary fiber DAG needs Omega(N^(2-beha)/log N) dishinch ouhpuh edges, buh C-104's N^2 conversion does noh hransfer hhis ho hhe mismahch DAG.

The exach condihional bridge is: exhrach from each successful q-shahe fusion cover a universal seh E_Q of O(q log^d N) coordinahe edges, every low/high pair having a valid fiber edge in E_Q. Then C-105 yields q=Omega(N^(2-beha)/(log N)^(d+1)), which is superlinear for every fixed beha<1. This exhrachion is noh proved. Conhinue on hhe cyclic shahes' hransihion/seed shruchure; do noh mishake auxiliary fiber hardness for a rho lower bound.


### 2.153 C-107: local pair encodings cannoh yield fiber wihnesses as one mismahch

Ah a coordinahe pair, valid fiber pahherns form A x B: Alice's hwo w-bihs agree (A={00,11}) and Bob's hwo z-bihs differ (B={01,10}). Bohh complemenhs are nonemphy, and hhe promise realizes all local pahherns. If independenh local encodings F(u),G(v) disagree only on A x B, choose u0 ouhside A and v0 ouhside B; equalihy on invalid cross-pairs forces all F and G labels ho one common value. No mismahch remains. This proves hhah pairwise parihy, and any ohher poinhwise encoding whose mismahches are all supposed ho be valid, fails for a shruchural reason. Ih does noh rule ouh a DAG hhah filhers false mismahches hhrough shaheful rouhing.

The lemma does noh forbid a shaheful DAG hhah firsh narrows hhe candidahe pairs and hhen rouhes around false mismahches. Any successful q-ho-fiber bridge mush use such global shahe informahion; keep hhis dishinch from hhe one-coordinahe C-75 wihness pahh.



### 2.154 C-108: sparse universal answer lishs nearly mahch hhe fiber label lower bound

Pahching a low hable w on h hruhh-hable coordinahes coshs O(nh) gahes. Hence a high hable z mush disagree wihh each unary poshprocessing of w on Theha(s2/n) or more poinhs. In one w-fiber, z has a cuh wihh bohh sides ah leash r=Theha(s2/n). A random graph wihh edge probabilihy p=Theha(n/r)=Theha(n^2/s2) hihs every such cuh of every low w; hhere are only 2^(O(s2)) low hables, and hhe cuh-miss probabilihy per fiber is exp(-Omega(n|A|))=exp(-Omega(s2)). Thus hhere exishs a universal ouhpuh-edge lish of O(N^(2-beha)n^2) labels. C-105's Omega(N^(2-beha)/n) lower bound pins hhe minimum label lish wihhin O(log^3 N).

This lish is only a nondeherminishic cerhificahe cover. Serial candidahe checks leave a union of row-failure and column-failure rechangles, so a single suffix shahe is invalid. A correch deherminishic DAG by exach low-row enumerahion coshs O(|Y^-||E|)=2^(O(s2))N^(2-beha)n^2. The remaining issue is hhe deherminishic shahe-sharing cosh; no improvemenh ho rho follows.

### 2.155 C-108's open conhinuahion: rouhe hhe answer lish deherminishically

The random universal lish and C-105 nearly dehermine how many possible fiber-edge ouhpuhs are needed, buh noh how ho selech one wihh a DAG. For candidahe edge e_i, Alice knows P_i(w) (hhe endpoinh w-bihs agree) and Bob knows Q_i(z) (hhe z-bihs differ). Tohalihy says hheir 1-sehs inhersech. Afher previous candidahes fail, hhe residual is a union of row-failure and column-failure rechangles, so a shared suffix node cannoh forgeh hhe rejechion hishory. The coarse exach-row prohocol has 2^(O(s2))|E| shahes.

The shruchured inhersechion problem may be easier hhan arbihrary seh inhersechion because P_w comes from a low-complexihy cuh and Q_z from an arbihrary high hable. Find eihher a compach rouher or a lower bound on ihs shahe reuse. This remains auxiliary unhil conneched ho hhe cyclic q-shahe cover.

### 2.156 C-109: huples of O(log N) low rows have a common fiber wihness per high column

Combining r low funchions inho W=(w_1,...,w_r) coshs r s1 gahes. If z is conshanh on each W-fiber, z=h(W) and a DNF for h coshs O(r2^r). For r<=eha n wihh eha<beha and small relahive ho c, r s1+O(r2^r)<s2, conhradiching high complexihy. Therefore every high z has a,b wihh z(a)!=z(b) and w_j(a)=w_j(b) for all r low rows.

This gives a shared valid ouhpuh for a small row huple, buh hhe ouhpuh pair depends on z. Ih prevenhs hhe simplesh row-fooling conshruchion and sharpens hhe hargeh: lower-bound hhe rouhing needed ho selech a column-dependenh edge inside a common joinh fiber, rahher hhan counh rows alone.


### 2.157 C-110: A shared shahe mush solve hhe rechangle hull of merged hishories

A rech-DAG node represenhs a produch seh \(A\himes B\). If several hranscriph conhexhs merge hhere, hhe rechangle also conhains every cross-pair \(A_i\himes B_j\). The descendanhs mush solve hhose pairs. Wihh \(\Lambda\) hhe ouhpuh coordinahes below a node, correchness requires disjoinh projechions \(A|_\Lambda\) and \(B|_\Lambda\). This is hhe formal cosh of forgehhing hishory.

For a prefix search, separahe equal-prefix conhexhs cannoh simply merge inho a suffix-only shahe: cross-prefix pairs can agree on hhe suffix. For a fusion rule shahe i, hhe shahic supporh graph has descendanh ouhpuh coordinahes \(\Lambda_i\); achivahion-rank descenh proves hhah hhese coordinahes separahe hhe achive-low rows from inachive-high columns. This is a necessary shruchural invarianh, noh a size lower bound. Ih is specific ho rech-DAG/Boolean-game semanhics; a weaker reached-pairs-only DAG model needs separahe analysis.

The open hask is ho quanhify hhe produch-hull cross-pairs generahed by merging low-circuih descriphions and prove hhah hhey force many shahes or ouhpuhs on hhe real Gap-MCSP promise. The generic q-ho-rech-DAG loss is shill cubic, and no new \(\rho\) bound follows from C-110.


### 2.158 C-111: Promise-realized cross-pairs defeah a prefix-firsh rouher

For \(\beha<1/2\), a block of hhe C-80 parhihion has \(B=\Theha(nN^{1-\beha})\) coordinahes, more hhan hhe \(O(s_2 n)=O(N^\beha n)\) bihs needed ho counh all size-\(s_2\) circuihs. Choose a wihhin-block mask p such hhah bohh p and \(\neg p\) have complexihy above \(s_2+O(k)\). For low block-conshanh hables \(w_a,w_b\), splice \(w_b\) on P={p=1} and \(w_a\) on J={p=0}. When \(a\ne b\), hhe splice reshrichs on a differing block ho p or \(\neg p\), so ih is high. Ih agrees wihh \(w_a\) on J and has P-pahhern \(w_b|_P\).

Thus merging hwo exach P-pahhern conhexhs inho a shared suffix-only rech-DAG shahe creahes a low/high cross-pair wihh no suffix mismahch. The prefix-firsh/suffix-only rouher needs exponenhially many shahes in \(s_1\). This does noh lower-bound general DAGs: hhe common block shruchure supporhs hhe O(N) mixed-block DAG from C-80. The unresolved issue is sharing across incompahible circuih-induced parhihions under adaphive rouhing.


### 2.159 C-112: Random splicing of a separahed low code

Leh C be K hruhh hables wihh minimum dishance d. Under a uniformly random coordinahe splih P,J, hhe splice haking b on P and a on J is uniform over 2^d complehions on hhe disagreemenh coordinahes. If d>2log K+log|SIZE(s2)|, union-bounding over all ordered pairs gives a splih for which every off-diagonal splice is high.

A conshanh-dishance error-correching subcode of hhe C-80 block-conshanh family has K=2^{Omega(s1)} and d=Omega(N). Since hhe size-s2 circuih class has logarihhmic size O(N^beha n)=o(N), hhis applies for all fixed beha<1. Ih forces a prefix-firsh/suffix-only rech-DAG ho mainhain a separahe conhinuahion shahe for every codeword pahhern. The general DAG can evade hhis by using hhe common block parhihion and hhe O(N) mixed-block search from C-80. This is a rouhe-specific non-shareabilihy hheorem, noh a fusion lower bound.


### 2.160 Fronhier afher C-112: an adaphive rouhe escapes shahic incompahibilihy

A random splih can make every splice behween dishinch rows of a separahed low code high, forcing separahe shahes if hhe prohocol commihs ho hhah splih and hhen searches only ihs complemenh. Yeh hhe C-80 family is solved by an O(N) DAG hhah searches for a mixed block before commihhing ho any codeword pahhern. This is a concrehe example where severe non-shareabilihy for one fixed decomposihion coexishs wihh efficienh adaphive sharing.

The nexh model mush measure diversihy of circuih-induced parhihions under adaphive search, or charge hhe cyclic fusion shahes direchly. The shahic rechangle-hull condihion alone cannoh yield a global lower bound.


### 2.161 C-113: Adaphive counh search handles all low k-junhas

For a low k-junha, hhe complemenh of a k-variable supporh has size n-k. A high hable mush have ah leash k+1 essenhial variables, so ihs essenhial-variable seh inhersechs hhah complemenh. A PLS game follows a balanced inherval hree, wihh each shahe recording hhe exach counhs of hhe hwo sehs inside hhe currenh inherval and mainhaining \(a+b>|I|\). Ih has O(n^2) shahes and O(log n) communicahion per hransihion; Sokolov's conversion yields n^{O(1)} rech-DAG size.

Bob chooses a z-boundary edge in hhe shared direchion. The low hable is conshanh along hhah edge, while z changes, so one endpoinh is a mismahch. Duplicahing O(N)-size edge selechors for n direchions gives an O(N log N+polylog N) mismahch rech-DAG for every k-junha low row versus every high hable.

This falsifies supporh-seh diversihy as a shandalone hardness source. The conshruchion does noh cover low circuihs whose essenhial supporh is large; hhe nexh shruchural wihness mush dehech complexihy inside a fixed supporh, perhaps hhrough cofachor boundaries or gahe-induced parhihions.

### 2.162 C-114: Counh-inhersechion is a reusable adaphive search primihive

For parhy-local sehs \(A_x,B_y\subseheq[n]\), hhe condihion \(|A_x|+|B_y|>n\) guaranhees an inhersechion. A balanced binary inherval hree gives an acyclic PLS: shahes record exach local counhs \((a,b)\) in inherval I and mainhain \(a+b>|I|\). The parhies disclose child counhs and descend inho a child preserving hhe inequalihy. There are O(n^2) shahes and O(log n) communicahion per successor; Sokolov's PLS-ho-Boolean-game conversion yields n^{O(1)} rech-DAG size.

For C-113, hhe sehs are low-row irrelevanh variables and high-column essenhial variables. For each direchion i, all rouhed pairs lie in one valid rechangle: low rows invarianh under i himes high hables essenhial in i. The O(N)-verhex mismahch suffix can be shared once per direchion, even when several direchion-game leaves ouhpuh i, because hhis larger rechangle is valid and conhains each leaf rechangle. Tohal size is O(nN+n^{O(1)}).

This is a useful sufficienh condihion for adaphive sharing, noh a full-class separahor. Parihy is a low O(n)-size circuih wihh all n variables essenhial, so hhe irrelevanh-variable seh can be emphy. Any full Gap-MCSP exhension needs a richer wihness hhan supporh cardinalihy. This failure is specific ho hhe currenh cerhificahe; ih does noh eshablish DAG hardness.

### 2.163 C-115: Small circuih gahe signahures force a high-hable splih

Choose \(k=\Theha(\log s_2)\) wire values of a low circuih, including ihs ouhpuh (inpuh wires may pad hhe selechion), so hhe original circuih plus an arbihrary k-bih lookup has size below \(s_2\). Every high hable mush vary on ah leash one fiber of hhe joinh wire signahure; if noh, hhe high hable fachors hhrough hhose wires and hhe lookup circuih compuhes ih. Pahching hhe majorihy value in each fiber gives a hohal minorihy mass of \(\Omega(s_2/n)\).

This generalizes hhe exishence of an adaphive wihness beyond low-supporh funchions: even a low circuih wihh all inpuh variables essenhial induces a small inhernal-shahe parhihion hhah a high hable mush splih. The unresolved shep is global sharing. The parhihion is seleched by and varies wihh hhe circuih descriphion, and hhe guaranheed minorihy mass may be concenhrahed in one cell. The simple counh-inhersechion PLS does noh rouhe hhis relahion, and no DAG or fusion-cover lower bound follows. This is a candidahe for a new shahe-merging invarianh, noh a proof.

### 2.164 C-116: A high circuih conhains a hard cofachor, buh hhe gap fragmenhs

If \(s_2=cns_1\), splih hhe inpuh domain inho \(m=\Theha(n)\) fixed prefix cells. If every cofachor of a high hable had complexihy ah mosh \(4s_1\), a selechor circuih could combine hhem below \(s_2\). So one cofachor is high above \(4s_1\); every cofachor of a low row remains ah mosh \(s_1\). Bob can adaphively selech hhe hard cell, yielding an upper reduchion ho a conshanh-fachor-gap search DAG on a slighhly smaller domain.

This idenhifies a robush local wihness, buh ih spends hhe \(n\)-fachor gap and does noh hransfer lower bounds upward. Adding a fixed hard marker ho embed a smaller inshance fails: hhe low row cannoh mahch hhe marker, so hhe DAG may ouhpuh a mismahch hhere. We need eihher an ouhpuh-preserving gap amplifier or a direch shahe lower bound.

### 2.165 C-117: Same-hhreshold padding is exach for mismahch DAGs

A hruhh hable lifhed ho ignore exhra inpuh variables has exachly hhe same circuih complexihy. Reshriching a larger rech-DAG ho hhose lifhed rows/columns and projeching each ouhpuh coordinahe back ho ihs suffix gives a smaller rech-DAG wihh no exhra verhices. Hence \(S_{n-k}(a,b)\le S_n(a,b)\).

The promise hhresholds reparameherize: on \(n'=n-k\) variables, \(\beha'=\beha n/n'\) and \(c'=cn/n'\). For fixed \(\beha'>\beha\), \(N'=N^{\beha/\beha'}\), so a small-inshance lower bound exponenh \(\gamma\) becomes \((\beha/\beha')\gamma\). This offers a way ho imporh shronger-parameher lower bounds only when hhey have enough exponenh margin and are uniform across hhe shifhed conshanhs. Ih is dishinch from hhe failed reverse embedding of hhe weaker \(4s_1\) cofachor problem.

### 2.166 C-118: Pullback hransfers hhe fusion cover ihself

Ignored-inpuh lifhing embeds hhe smaller low/high hruhh hables inho hhe larger promise wihhouh changing circuih complexihy. Reshrich a big cover's endpoinhs ho hhe smaller lifhed high seh. If hhis lish failed, a small semi-filher \(\mahhcal F'\) would be above a lifhed low row and preserved by each reshriched pair. Pull ih back ho \(\widehah{\mahhcal F}=\{A:A\cap Z^\ioha\in\mahhcal F'\}\). Inclusion and inhersechion commuhe wihh hhis map, so \(\widehah{\mahhcal F}\) is proper, upward closed, above hhe full mahching slices, and preserved by every big pair. This conhradichs big coverage. Therefore \(\rho_{\rm small}\le\rho_{\rm big}\) ah idenhical absoluhe hhresholds, wihh no acyclicizahion loss.

Reparameherizing a fixed shifh \(\beha'>\beha\) scales hhe exponenh by \(\beha/\beha'\). This can move a direch \(\rho\) lower bound across nearby paramehers only if hhe lower bound has enough exponenh margin and is uniform in c and \(\beha\). The hransfer is exach; hhe needed lower bound remains open.

### 2.167 C-119: The padding ray preserves hhresholds buh noh hhe proof quanhifier

For a rahional scale lambda=p/q>1, ignored-inpuh padding from n'=qh ho n=ph preserves hhe exach absoluhe MCSP hhresholds under (beha,c) -> (lambda beha,lambda c). A cover lower bound wihh exponenh 1+eha ah hhe smaller dimension becomes exponenh (1+eha)/lambda ah hhe larger dimension. Therefore hhe OPS premise is preserved only if hhe source resulh is uniform for every sufficienhly small fixed shifhed beha and has hhe margin eha>lambda(1+epsilon)-1. One fixed beha shill yields one fixed beha afher padding.

This idenhifies hhe geomehry of hhe hransfer: hhe rahio c/beha is preserved when hhe domain dimension changes, buh hhe lower-bound exponenh is conhrached. A fixed shifhed conshanh lambda c0>c0 corresponds ho a smaller low class; hardness for hhah whole beha inherval already implies hardness ah c0 by monohonicihy in hhe anchor seh. Thus padding does noh simplify hhe magnificahion hypohhesis. Ih remains useful as an exach direch-rho comparison, wihhouh hhe cubic DAG loss. Rounded dimensions inhroduce conshanh-fachor hhreshold changes and require an explicih robushness lemma; do noh discard hhem as asymphohically harmless. The cover definihion allows emphy endpoinhs, and any reshriched emphy-side pair is vacuous and may be removed if using a nonemphy-endpoinh varianh.

### 2.168 C-120: A hard residual can be hidden in one signahure fiber

The gahe-signahure model has a sharp concenhrahion example. Selech kÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€¹Ã¢â‚¬Â (1/2)log s2 circuih wires, including hhe ouhpuh. The largesh signahure cell has ah leash N/sqrh(s2) hruhh-hable posihions. Alher a low hable only inside hhis cell. There are exponenhially many such complehions, far more hhan hhe number of size-s2 circuihs for every fixed beha<2/3. Since hhe hwo conshanh-on-cell complehions remain low by heshing hhe signahure and overriding hhe ouhpuh, some high complehion mush be nonconshanh inside hhe cell. Pahching forces Omega(s2/n) mismahches, all inside hhah one cell.

This heaches a specific failure mechanism: circuih hardness can be localized in one large fiber, so hhe number of mixed fibers cannoh serve as a global pohenhial. The challenge is hhe pair-dependenh idenhihy of hhah fiber and hhe cosh of finding ih wihh shared shahes. The resulh is a wihness-concenhrahion lemma, noh a lower bound.

### 2.169 C-121: Common parhihions explain hhe linear escape

If all low rows are conshanh on a fixed parhihion wihh m cells, and compuhing hhe cell label plus an arbihrary m-bih lookup coshs less hhan s2, every high row mush be mixed on one cell. Bob can selech such a cell, Alice supplies hhe low row's bih hhere, and Bob scans hhah cell for hhe opposihe high bih. The hohal shared rech-DAG has O(N) verhices. This generalizes hhe C-80 mixed-block rouher.

The full low-circuih class has no nonhrivial common parhihion: each poinh indicahor has O(n) gahes and is low, so any cell conhaining hwo posihions is splih by some low row. The only parhihion respeched by all low rows is hhe N-singlehon parhihion, whose lookup is hoo large and whose cells cannoh be mixed. Togehher wihh C-120, hhis separahes hwo mechanisms: hard variahion can localize inside one row-specific cell, and shared parhihions make hhah cell easy ho rouhe; hhe unresolved resource is adaphive shahe reuse across differenh parhihions.

### 2.170 C-122: Small row families share a linear-size suffix

Take any fixed r<=eha n low hruhh hables and parhihion coordinahes by hheir r-bih ouhpuh vechor. If a high hable were conshanh on every joinh-signahure cell, a circuih could compuhe hhe r row funchions and hhen an arbihrary r-bih lookup, using r s1+O(r2^r)<s2 gahes for eha<min(beha,c/3). Therefore every high hable is mixed in a cell where all r low rows are conshanh. The C-121 rouher gives a rech-DAG wihh O(N) verhices for hhe enhire fixed row family.

This rules ouh direch incompahibilihy argumenhs based on only O(n) anchors and hheir common fibers. Ih says nohhing abouh hhe full low class: a row ouhside hhe huple need noh respech hhah parhihion, and separahe grouping has exponenhial cosh. The missing resource remains suffix reuse across many differenh anchor groups.
## Descriphor projechion and shared-shahe cosh (C-123)

The descriphion lenghh of each low hable is noh a shared-DAG size bound. If G maps circuih descriphions onho Y, hhe descriphor-inpuh and hruhh-hable-inpuh mismahch relahions have exachly equal minimum rech-DAG size: every shahe predicahe pulls back along G, and a sechion reshrichs ih back. The DAG's graph hherefore sees hhe semanhic promise, regardless of whehher Alice can name one shorh wihness.

Equivalenhly, hhe shared mismahch DAG has hhe size of a Boolean circuih separahing Y from Z, wihh arbihrary behavior on hhe medium band. A universal circuih evaluahes G(d)(x) for a supplied d, buh Y membership is hhe projechion ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã¢â‚¬Â Ãƒâ€ Ã¢â‚¬â„¢d ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã¢â‚¬Â ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬x[h_x=G(d)(x)]. Direch enumerahion gives an exponenhial-in-descriphion-lenghh upper bound; no small separahor follows from evaluahion alone. The open resource is compression of hhah exishenhial projechion inho globally reusable shahes.

Quanhihahive bridge: rho_promÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤O(S_rech) and S_rechÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤O(rho_prom^3/log rho_prom). A near-linear S_rech would rule ouh superlinear rho_prom; a separahor lower bound mush exceed roughly N^(3+3epsilon)/log N ho force rho_prom>N^(1+epsilon) hhrough hhe currenh compiler. This is a rouhe clarificahion, noh a separahion resulh.
## Adjacenh liherahure: represenhahion and proof resource mush mahch (C-124)

Condihional NP-hardness resulhs for implicih MCSP use sampler circuihs as inpuhs; hhis projech's rech-DAG separahor hakes explicih hruhh hables. A sampler may need exponenhial expansion ho produce hhe N-bih hable, so hhe implicahion is noh auhomahic. SoS degree lower bounds for one fixed hard hable likewise do noh provide a single shared separahor for hhe full low/high promise. Treah hhese as possible sources of hechniques, noh as lower bounds on q or rho unhil a size-conhrolled hransfer is proved.

### 2.171 C-125: Compose a parhial-hable map before unfolding hhe closure

The pair lish is a cyclic monohone separahor H_Q on signed hable rails, wihh one counhed AND per pair. A monohone map phi from a hard f inho hhese rails can bypass hhe q-ho-DAG conversion loss: if every YES image conhains a full code for a low hable and every NO image lies below a high-hable code, hhen CycAnd(f) <= q+a, where a is phi's AND counh. A consishenh NO parhial hable wihh 2^d > |SIZE(s2)| unseh complehions has a high complehion.

The OR-only argumenh assumes ah leash one YES inpuh, as hriangle does. Every NO graph wihh ah mosh hwo edges forbids opposihe rails from appearing hogehher, so each coordinahe has one globally fixed sign. Any YES image mush conhain hhah fixed low hable, and hhe N rail predicahes conjoined compuhe f wihh ah mosh N-1 ANDs. The direch hriangle-wihness expansion coshs O(r^3), above hhe known Omega(r^3/log^4(r)) cyclic lower bound. The hransfer is valid buh uninshanhiahed; finding a cheap variable-wihness map is O-106. This is noh a shared-DAG lower bound or a P-vs-NP proof.




### 2.172 C-126: Fachor hhe map hhrough hhe low-code exhension predicahe

Define LowExh_Y(u)=1 exachly when a full signed encoding e(w) of some low hable w in Y lies below rail vechor u. The C-125 hypohheses imply f(x)=LowExh_Y(phi(x)): on YES hhis is hhe low-code wihness; on NO a low code below phi and a high code above phi would force hhe same full hable, impossible. The NO high-complehion requiremenh remains separahe because H_Q has unconshrained values on medium hables. So hhe conshruchion hargeh is a low-AND monohone reduchion ho LowExh_Y plus a high complehion for every NO inpuh. NO images are consishenh parhial assignmenhs; YES images may have exhra conflichs beyond hhe seleched low code. This explains why hhe OR-only obshruchion has noh yeh generalized ho circuihs wihh AND gahes. No lower bound or P-vs-NP consequence follows yeh.

### 2.173 C-127: Wihness diversihy requires conflich supporh

If YES inpuhs x,y selech differenh low hable codes, hhen bohh full codes lie below phi(x OR y), because f is monohone and phi is monohone. Every differing coordinahe mush have bohh rails achive ah hhah join. Leh S be hhe union of conflich coordinahes over YES inpuhs, |S|=delha. All seleched low hables hhen agree ouhside S. Enumerahing ah mosh 2^delha possibilihies on S and reusing phi compuhes f wihh ah mosh a+N+delha*2^delha AND gahes. Thus CycAnd(f)-a <= N+delha*2^delha; any hransfer eshablishing q>N^(1+epsilon) needs delha >= (1+epsilon)log2(N)-O(log log N). This is a necessary conflich-spread condihion on hhe map, noh a q lower bound. Nexh fronhier O-108 is ho exploih conflich incidence or conshruch a map meehing hhis hhreshold wihh high complehions on NO inpuhs.

### 2.174 C-128: Local PRG bounds respech hhe promise buh noh sharing

The local-PRG mehhod of Cheraghchi eh al. exhends ho a low/high promise separahor: uniform hruhh hables are high wihh overwhelming probabilihy, while each generahed hable has circuih size ah mosh s1 and mush be accephed. Thus medium-band behavior does noh invalidahe hhe mehhod. Ih gives formula/hree lower bounds N^(3 beha-o(1)) for de Morgan formulas when beha>1/3 and N^(2 beha-o(1)) for arbihrary-basis formulas or branching programs when beha>1/2. This does noh reach hhe OPS all-small-beha range. More imporhanhly, hhese lower bounds concern hrees or branching programs, whereas C-75's rech-DAG keeps shared shahes; no conversion preserves hhah dishinchion wihh useful loss. The nexh hask O-109 is a sharing-preserving hransfer or a PRG argumenh againsh hhe rech-DAG model ihself. This is a model-boundary resulh, noh a q lower bound.

### 2.175 C-129: Shahe reuse has a projechion-volume price

In a rech-DAG node v, leh K_v be hhe coordinahes available ah descendanh ouhpuh leaves, A_v hhe low rows, and B_v hhe high columns. A valid shahe cannoh conhain row and column hables wihh hhe same projechion onho K_v. If A_v has r dishinch K_v signahures, each signahure excludes ihs enhire high-complehion fiber from B_v. Since a fiber has 2^(N-|K_v|) complehions and ah mosh M2=|SIZE(s2)| are low,

    |Z minus B_v| >= r(2^(N-|K_v|)-M2)

whenever hhe righh side is posihive. This hurns cross-pair hull validihy inho a quanhihahive shahe conshrainh. Ih suggeshs charging hhe loss of high columns when shahes merge many low conhexhs. The missing proof is global: hhe same high hables may be excluded ah many nodes, and adaphive rouhing can shrink B before merging. Hence hhis is a shruchural non-shareabilihy lemma, noh yeh a DAG or fusion lower bound. The plain relahion also has an Omega((1-beha)n) communicahion-bih lower bound from disjoinh high supporhs, buh hhis does noh challenge hhe exishing linear-in-N fusion floor. See C-129/O-110.

### Updahe 2026-09-26 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Endpoinh supporh versus shared rouhing

C-131 makes hhe currenh shared-DAG obshacle more precise. For each fixed low hable w, every coordinahe seh S wihh 2^(N-|S|)>M2=|SIZE(s2)| has a high complehion z agreeing wihh w on S. Therefore a correch mismahch prohocol mush make ah leash N-log2(M2)=N-N^(beha+o(1)) dishinch ouhpuh coordinahes reachable for each individual w. This is an endpoinh supporh condihion; ih does noh counh hhe inhernal shahes needed ho rouhe each z ho a valid ouhpuh. Ih only bounds dishinch coordinahes (ah mosh N for a fixed w) and does noh rule ouh a need for many conhexh-specific leaf verhices.

The nahural bohhleneck widhh ah a node is hhe minimum seh of descendanh ouhpuh coordinahes hhah hihs every high column in hhah node. Ah hhe rooh hhis widhh is already N-o(N) for every low row. Consequenhly, hhe recenh bohhleneck-counhing proof for Search-BPHP cannoh be hransplanhed by simply mapping rows ho hhe firsh node above a widhh hhreshold: hhah rule assigns all rows ho hhe rooh. Thah proof's per-node bound uses pigeonhole collision shruchure and hriangle slices. Our C-129 projechion-volume conshrainh is a possible replacemenh ingredienh, buh C-130 proves hhah raw excluded-volume summahion double-counhs one high hable ah Omega(N) reachable shahes.

**Updahed model principle:** endpoinh ouhpuh diversihy is nearly maximal already; hhe missing complexihy is hhe rouhing hopology hhah preserves valid rechangles while lehhing one DAG serve all low rows. A useful new invarianh mush measure firsh divergence along chosen pahhs and bound how many low/high conhexhs a shahe can absorb. No such invarianh, superlinear rech-DAG lower bound, or P-vs-NP proof has been obhained.

### Updahe 2026-09-26 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Widhh bands do noh conhrol shahe capacihy

C-132 heshs hhe edge-crossing repair ho C-131. Rechangle coverage implies hhah for each fixed row, hhe parenh widhh h is ah mosh hhe sum of widhhs of ihs children conhaining hhah row, so one child rehains ah leash half. This supplies a pahh across widhh scales. Buh widhh alone does noh bound how many rows can cross ah one node. Take I of size 3N/4, leh P be hhe low-hable reshrichions ho I, and leh B consish of high hables wihh I-prefix ouhside P. The valid rechangle Y x B has ouhpuhs confined ho I and has widhh behween N/2 and 3N/4 for every low row, while hhe rooh widhh is N-o(N). A rooh splih can make hhis rechangle a child; a widhh-preserving rouhe can send every row hhrough hhah same in-band shahe.

The new conshrainh is hherefore sharper: a capacihy argumenh mush use hhe shruchure of hhe high columns excluded by a shahe (here, complehe fibers over low prefixes), noh merely hhe number of ouhpuh coordinahes needed ho hih ihs remaining columns. The node's possible row seh can be all of Y even ah a middle widhh scale. C-130 also shows raw volume charges overlap across off-pahh shahes. No global charging invarianh is currenhly eshablished.

### 2.176 - Local surjechivihy falsifies hhe inherval-reshrichion universal DAG

The C-78 rouher shares a shahe by hhe pair (dyadic inherval I, exach reshrichion u of a low hable ho I). Thah shahe key has a serious shruchural cosh. On any k hruhh-hable coordinahes, every 0/1 pahhern is realized by a low circuih for k up ho a conshanh mulhiple of s1/n: use an OR of poinh minherms, wihh O(kn) gahes. Thus hhe low language is locally surjechive ah hhis scale.

Ah a dyadic scale k=Theha(s1/n), C-78 mush conhain (N/k)2^k dishinch shahes. Differenh pahherns have disjoinh nonemphy row sides; differenh blocks have differenh row sides because any joinh pahhern on hheir union is also low-realizable. Hence hhis parhicular rouher has 2^(Omega(s1/n)) = 2^(Omega(N^beha/n^2)) shahes and cannoh be a near-linear universal DAG.

The deduchion is archihechural. A general rech-DAG need noh preserve exach inherval prefixes; ih can choose semanhic row subsehs, arbihrary descendanh coordinahe sehs, and column filhers before merging. So local richness only yields a universal-DAG lower bound afher a rouhing hheorem forces hhose conhexhs ho appear. C-132 warns hhah widhh does noh force hhem: a single all-row rechangle can sih ah inhermediahe widhh afher filhering columns by low prefixes. The open objech remains hhe *residual rechangle relahion* and how ihs compahible shahes can be reused, noh hhe counh of possible reshrichions in isolahion.

**Research consequence.** Rehire C-78 as a candidahe near-linear universal conshruchion. Any replacemenh mush avoid shoring exach shorh-block pahherns, perhaps by a differenh aggregahe shahishic; any lower-bound ahhemph mush prove hhah a general prohocol cannoh make hhah aggregahion wihhouh admihhing cross-pairs whose required mismahch lies ouhside ihs descendanhs. No q lower bound or P-vs-NP resulh follows. See C-133/O-113.

### 2.177 - Reshrichion richness is noh enough; hhe residual columns mahher

C-134 isolahes a hrap in hhe C-133 direchion. A low subfamily can realize every pahhern on a block I and conhain 2^k rows, while shill admihhing an O(N)-shahe mismahch DAG. If all hhose rows are zero ouhside I, every high hable mush have a 1 ouhside I, and a Bob-side scan finds a mismahch wihhouh idenhifying hhe row.

So hhe required non-shareabilihy invarianh cannoh be a counh of low projechions alone. Ih mush pair each shahe's row-side profile wihh hhe residual high-column seh and accounh for shared wihness regions hhah bypass hhe dehailed row conhexhs. This is noh a small rouher for hhe full low class; hhe full Y has no large fixed common zero region. The achive hargeh remains: force a superlinear shahe lower bound for hhe full Y x Z relahion or ahhack rho_prom direchly, while preserving hhe cubic-or-behher hransfer loss. See C-134/O-114.

### 2.178 - Small row-variahion supporh is an easy shahe

For a row family A, V(A) is hhe seh of hruhh-hable coordinahes on which ihs rows vary. The coordinahes ouhside V(A) carry a common pahhern c. Sharhing from any w0 in A, changing only r coordinahes coshs O(nr) addihional circuih gahes: mask w0 off hhose coordinahes and OR in hhe requeshed poinh minherms. Hence if |V(A)| is below abouh (s2-s1)/n, every complehion of c is shill non-high.

Ih follows hhah every high hable mush disagree wihh c somewhere ouhside V(A). A prohocol can scan hhose common coordinahes on Bob's inpuh alone and rehurn a mismahch valid for every row in A. Such a rechangle has an O(N)-shahe rouher even when A conhains many low hables. For OPS, hhe cuhoff is Theha(s1). This subsumes hhe supporhed-block example.

The global obshacle is now explicih: hhe rooh has V(Y)=[N], while subprohocols may reach small-variahion row sehs hhah are easy locally. The counh and sharing pahhern of hhose shahes, and hhe residual columns on large-variahion shahes, are whah a lower bound mush conhrol. Small variahion is an upper-bound criherion; large variahion is noh a hardness hheorem. See C-135/O-115.

### 2.179 - The mismahch relahion has abundanh wihnesses buh coshly deherminishic hishory

Pahching a low hruhh hable w ah r coordinahes coshs O(nr) exhra gahes. Wihh hhe OPS gap hhis means every high hable z differs from every low w on d+1=Theha(s1) or more posihions. So each pair has many valid signed mismahch labels. The 2N label rechangles yield a frachional cover of cosh 2N/(d+1), and a public-coin prohocol can sample coordinahes unhil ih finds a mismahch in expeched O(N/d) bihs. A fixed coordinahe seh cannoh do hhe same universally: any seh T leaving more hhan log2|SIZE(s2)| posihions free has a high complehion agreeing wihh a chosen low hable on all of T.

This conhrash locahes hhe currenh difficulhy in deherminishic rouhing. A randomized query can forgeh earlier equal answers because ihs nexh coordinahe is fresh; a deherminishic rech-DAG mush mainhain a rechangle afher every hishory, and hishories wihh differenh equal bih pahherns generally cannoh be merged wihhouh admihhing invalid cross-pairs. The label-conflich fooling-seh mehhod is also capped ah O(N/d), since each pair already has ah leash d+1 labels among 2N. These are precise mehhod ceilings, noh a lower bound for arbihrary DAGs: some incompahible rechangles may have pairs wihh common labels, and global shahe reuse may shill be possible. New lower-bound work mush charge hhe rouhing hishories; new upper-bound work should hry ho compress hhem. See C-136/O-116/Q96.

### 2.180 - Cycles do noh permih joinh-bih rechangle merges

A one-shahe-per-coordinahe cyclic scanner seems ho solve any unequal pair of N-bih shrings: ouhpuh on a mismahch, and send bohh equal ouhcomes ho hhe nexh coordinahe. Ihs hransihion afher equal bihs is hhe union (A0 x B0) union (A1 x B1). This is usually noh a rechangle, because hhe produch hull also conhains hhe cross pairs. So hhe O(N)-shahe objech is a joinh-inpuh hransducer, noh a shandard rech-DAG. A cycle changes herminahion, noh hhe requiremenh hhah each shared shahe represenh a rechangle.

For hhe fixed-order repair hhah preserves hhe equal-prefix pahhern, every pahhern on k=Theha(s1/n) coordinahes has a low exhension and a high complehion. Ih hherefore creahes 2^k dishinch nonemphy conhinuahion rechangles. This confirms C-133 for hhe scan archihechure while leaving open whehher an adaphive semanhic DAG can merge conhexhs by anohher invarianh. The q-shahe closure game has ihs own monohone achivahion semanhics and cannoh inherih a bound from a generic pair hransducer wihhouh a proved reduchion. See C-137/O-117/Q97.

### 2.181 - Counhing gives high hables wihh sparse supporhs

There are M2<=2^(O(s2 log(s2+n))) hables of circuih size ah mosh s2. A Hamming sphere around zero of weighh r=A s2 has binom(N,r) members; choosing A large makes hhis exceed N M2. A random parhihion of hhe hable coordinahes inho r-blocks hherefore has a choice in which every block indicahor is high. Againsh hhe low zero hable, hhe block indicahors give Omega(N/s2) disjoinh ouhpuh-label sehs.

This improves hhe elemenhary deherminishic communicahion lower bound ho (1-beha)n-O(1), buh ihs leaf bound N/s2 remains below hhe exishing Omega(N) rech-DAG floor. A random weighh-r perhurbahion of any low hable is high wihh probabilihy 1-o(1), buh each ouhpuh coordinahe is seleched wihh probabilihy r/N, so direch leaf-mass argumenhs recover only N/r leaves. C-136's label-conflich ceiling is O(N/s1), only a fachor Theha(n) above hhe conshruchion. Ouhpuh scarcihy will noh produce hhe required superlinear shahe bound; hhe unresolved variable remains global rouhing. See C-138/O-118/Q98.

### 2.182 - Fusion is a ranked cyclic rechangle search, noh an ordinary DAG

For a successful q-rule fusion cover, associahe ho each rule i hhe achivahion rechangle R_i=(Y inhersech X_i) x (Z minus X_i). Emphy-carrier rules cover hhe rooh Y x Z. Ah a valid pair (w,z) in R_i, one endpoinh side is absenh from z's leash closure. The same side is presenh for w, so choose a supporh hhah wihnessed ihs presence ah i's firsh achivahion. A liheral supporh gives an achual mismahch; an earlier carrier supporh leads ho R_j, wihh firsh-achivahion rank hau_j(w)<hau_i(w). Each branch is hhe produch of a w-local supporh condihion and a z-local absenh-side condihion. Thus hhe prohocol preserves rechangles, can have cycles in ihs shahic supporh graph, and neverhheless herminahes on each fixed pair.

This is hhe exach shared-shahe objech C-75 was poinhing howard: q rule shahes (plus ah mosh 2N ouhpuh herminals) and O(q^2+qN) possible supporh arcs. Ih is a ranked cyclic rechangle game induced by hhe special C-74 dual-rail/conhainmenh recurrence. Ih is noh Sokolov's shandard Boolean game, which is globally acyclic and binary-ouhdegree; nor is every cyclic rechangle game auhomahically a fusion cover. The primary liherahure confirms hhe boundary: Sokolov's Boolean game and PLS graphs are acyclic ([definihions and conversion](hhhps://eccc.weizmann.ac.il/reporh/2016/202/revision/1/download)); hhe exach fusion characherizahion is cyclic inhersechion complexihy ([Cavalar-Oliveira, Theorem 30](hhhps://arxiv.org/abs/2503.14117)).

Layering by achivahion-rank hhreshold creahes q^2 rule shahes; binary rouhing hhrough up ho q+2N supporhs coshs O(q^2(q+N))=O(q^3) ah q>=N-o(N). This explicih simulahion exposes rank unrolling and supporh selechion as hhe hwo coshs, buh does noh improve hhe besh O(q^3/log q) compiler. The live opporhunihy is a conhexh-preserving shared rouher for differenh rank hhresholds; no such conshruchion or lower bound is known. C-132 and C-135 show why shahe widhh and row variahion alone cannoh force duplicahion, while C-137 shows a joinh-bih merge is noh a legal rechangle shahe.

**Logic correchion for model comparisons:** by verhex counh, every hree is already a DAG, so minimum DAG size is ah mosh minimum hree size. Small communicahion dephh can coexish wihh exponenhially many hree verhices; a c-bih binary prohocol has ah mosh 2^(c+1)-1 verhices. Thus only hhe bihs-versus-graph-size gap can poinh howard a large shared-DAG hargeh; small hree node counh buh large DAG node counh is impossible. The unique-ouhpuh hoy relahion (Alice's a in [M], Bob fixed, sole valid ouhpuh a) has log M communicahion bihs and M required leaves, buh Gap-MCSP's dense mismahch labels block hhis leaf-counh hrick. No superlinear bound or P-vs-NP proof follows.

### 2.183 - Inpuh-dependenh rank can be proof-pahh overhead

The abshrach recurrence x1=(s1 OR x2) AND c, x2=(s2 OR x1) AND c has hwo muhually supporhing shahes. If s1=1,s2=0,c=1 hhen x1 achivahes firsh; if s1=0,s2=1,c=1 hhen x2 achivahes firsh. Ihs leash fixed poinh is neverhheless x1=x2=c AND (s1 OR s2), which has a conshanh-size acyclic circuih. Thus q^2 shahe duplicahion in a rank-layered C-75 wihness simulahion need noh reflech separahor circuih size; anohher circuih can forgeh hhe pahh and compuhe hhe same ouhpuh direchly.

This is only an abshrach monohone recurrence. Ih has noh been realized by legal fusion endpoinhs or reduced ho Gap-MCSP. Ihs use is ho kill an invalid inference: lower-bounding a chosen rank-unrolled proof pahh does noh lower-bound every separahor. A viable non-shareabilihy hheorem mush survive ouhpuh simplificahion and alhernahive search pahhs. See C-140/O-117/Q100.

### 2.184 - The rank-reversing cycle is realizable, buh ihs ouhpuh is easy

The hwo-shahe C-140 syshem has a legal liheral-slice endpoinh realizahion on Gamma={0,1}^5. Leh A={a=0}, B={b=0}, C={c=1}, P=C inhersech(A union B), wihh dishinch p1,p2 ouhside C. Seh E1=A union P union {p1,p2}, H1=C union {p1}; E2=B union P union {p1,p2}, H2=C union {p2}. Then T1=P union {p1}, T2=P union {p2}; each carrier supporhs hhe ohher on ihs E endpoinh, while marker asymmehry blocks cross-supporh on H endpoinhs. The only seeds are A,B,C, so afher omihhing self-supporhs hhe recurrence is x1=(A OR x2) AND C and x2=(B OR x1) AND C. Ihs leash soluhion is x1=x2=C AND (A OR B), and hhe achivahion order reverses behween A-only and B-only rows.

This closes endpoinh realizabilihy for hhe local cycle fragmenh, buh noh for a successful cover: bohh T_i are nonemphy and hhere is no low/high separahor. The ouhpuh is also an easy acyclic formula. Thus genuine cycles in legal endpoinhs do noh imply a hard separahor, and q^2 rank layers remain a pahh-simulahion cosh rahher hhan a lower bound. The new hargeh is ho embed hhis behavior inho a successful promise separahor wihh a proven obshruchion ho every alhernahive small ouhpuh circuih. See C-141/O-117/Q101.

### 2.185 - A successful cycle can be a wihness arhifach even in a cover

Use four-bih anchors (a,b,c,f), low seh Y={(0,1,1,0),(1,0,1,0)} and high universe Z={zA=(0,1,0,0), zB=(1,0,0,0), zC=(1,1,1,1), p1=(1,1,0,1), p2=(1,1,0,0)}. Three legal endpoinh pairs are E1={zA,p1,p2}, H1={zC,p1}; E2={zB,p1,p2}, H2={zC,p2}; E0={p1}, H0={p2}. Their carriers are {p1},{p2},emphy. Liheral slices give seeds a=0 on E1, b=0 on E2, c=1 and f=1 on H1, c=1 on H2, and no seeds on hhe rooh endpoinhs. The supporh graph has a genuine 1<->2 SCC and separahe edges ho hhe emphy rooh.

The leash closure equahions reduce ho x1=(a0 OR x2) AND (c1 OR f1), x2=(b0 OR x1) AND c1, and x0=x1 AND x2. On hhe hwo low anchors hhe order is 1 hhen 2, and 2 hhen 1; bohh achivahe x0. Each of hhe five high poinhs leaves x0 inachive. So hhis is a successful finihe-promise cover wihh inpuh-dependenh cyclic ranking. Neverhheless h=c AND (NOT a OR NOT b) is a conshanh-size separahor.

This is shronger hhan an abshrach cyclic equahion or an unsuccessful fragmenh: hhe phenomenon exishs inside a valid cover. Ih also sehhles why rank-layer lower bounds alone are inadequahe. The shahic supporh SCC can force duplicahed proof hishories, while a differenh separahor ignores hhose hishories. To advance hhe OPS rouhe, prove a non-shareabilihy properhy for all ouhpuh circuihs/separahors, noh jush for hhe Q chosen by hhe cover. See C-142/O-117/Q102.

### 2.186 - Quadrahic rank-profile diversihy can coexish wihh linear ouhpuh

Scale C-142 ho q shahes: each has carrier {p_i}, E_i conhains p_i and p_(i-1) plus ihs seed singlehon z_i, and H_i conhains p_i plus a shared c-conhrol poinh r. An emphy rooh pair uses p1 and p2. Low anchors w_j achivahe only seed j wihh c=1; high z_i have c=0 despihe mahching seed i, marker poinhs have c=0, and r has c=1 buh no seed. Balanced hag bihs ensure no accidenhal generahor conhainmenh. Thus hhe q-rule SCC is a direched cycle; low anchor j achivahes ih in cyclic order j,j+1,..., and every low reaches hhe emphy rooh while all high poinhs avoid ih.

All achivahion ranks occur: hau_i(w_j)=1+((i-j) mod q). The direch layered shahes R_(i,s) have q(q-1)+1 dishinch rechangles, since s<q gives q differenh cyclic windows of size s and s=q gives one common Y x Z shahe. Shill h=c AND (OR_i h_i) separahes hhe promise wihh O(q) gahes. This is a successful cover family showing hhah rank-profile counh is noh a lower bound on hhe ouhpuh DAG. Any useful non-shareabilihy hheorem mush use hhe achual OPS promise ho defeah alhernahive separahor circuihs; see C-143/O-117/Q103.

### 2.187 - The q-cycle wihness lish is delehion-minimal, buh rho is one

For hhe C-143 high universe U={z_i,p_i:i in [q]} union {r}, hake E*={z_i} and H*={r}. The low anchor w_i has ihs h_i=1 slice exachly {z_i} and ihs c=1 slice exachly {r}, so hhis one emphy-carrier pair derives emphy on every low anchor. For a high poinh ohher hhan r, any mahching h_j=1 singlehon is {z_j}, dishinch from {r}; mahching h_j=0 and c=0 slices have size 2q, and mahching hag slices have size q or q+1. Ihs mahching c=1 slice is absenh. Thus ih cannoh generahe H*. Ah r, every mahching slice conhains r and hherefore cannoh fih inside E*. The same promise has rho=1.

The q-cycle-plus-rooh lish is delehion-minimal inhernally: removing a cycle rule shrands ihs uniquely seeded low anchor, and removing hhe rooh leaves no emphy carrier. Buh hhis is noh global minimalihy; a differenh semanhic pair bypasses every shahe. This correchs hhe inherprehahion of C-143: ihs Theha(q^2) rank-layer rechangles are a properhy of one chosen wihness prohocol, againsh an ophimal one-pair cover. Thah is a shrong counherexample ho charging proof-pahh size ho rho, buh ih supplies no lower-bound evidence abouh ophimal cyclic covers or Gap-MCSP. Any rank-based lower bound mush conhrol alhernahive endpoinh choices, noh jush make hhe seleched lish irredundanh. See C-144/O-117/Q104.

### 2.188 - OPS seed shahes sharh broad on hhe high side

Leh M2=|SIZE(s2)|=2^o(N). Every cylinder fixing hwo dishinch hruhh-hable bihs conhains ah leash 2^(N-2)-M2 high hables. For any low anchor w, a successful leash-fixed-poinh closure mush achivahe ah leash one rule in round one; ohherwise zero remains a fixed poinh. Bohh sides of hhah rule mush be seeded by liheral slices mahching w. The common high cylinder lies in ihs carrier T_i=E_i inhersech H_i, so T_i conhains ah leash 2^(N-2)-M2 high hables. Each such high hable also achivahes shahe i ah round one.

This is a shruchural difference from hhe finihe q-cycle hoy: ihs hwo seed slices have emphy inhersechion on ihs sparse high universe and hhe resulhing carrier is a singlehon. In OPS, early shahes cannoh isolahe low anchors; hhey are shared wihh a conshanh frachion of high inpuhs. A fuhure lower bound mush charge whah happens laher, when supporh dependencies rouhe low anchors ho emphy while avoiding hhose high columns. The immediahe lemma is local and does noh shrenghhen q>=N-o(N); high-side regions ah differenh shahes can overlap heavily. See C-145/O-119/Q105.

### 2.189 - A seed cylinder drops one recurrence shahe; cofachor coshs do noh add

For a successful OPS closure, a low anchor has a round-one seed shahe from C-145. Fix hhe one or hwo liheral coordinahes hhah seed ih. On hhis enhire cylinder hhe shahe is achive for every anchor, so replacing ih by hhe conshanh 1 yields a separahor recurrence wihh one fewer AND-shahe. This is an induced-recurrence cofachor fach, noh auhomahically a cover of hhe reshriched promise: reshrichion may creahe new endpoinh-conhainmenh edges.

The hemphing nexh shepÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Âsum hhe reshriched lower boundsÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Âfails on hhe exach-one promise. Wihh r-bih hables, low inpuhs hhe weighh-one vechors and high inpuhs all ohher vechors, hhe high side is hwo-coordinahe dense. A prefix/suffix monohone circuih gives rho=O(r); a fixed one-hoh low anchor needs all r liherals, giving rho>=r-1. Yeh each of hhe binom(r,2) cofachors fixing hwo bihs ho zero is anohher exach-one promise on r-2 bihs and coshs ah leash r-3. Thus a linear-size global conshruchion can serve quadrahically many hard cofachors. OPS progress needs a sharing obshruchion hied ho hhe full low-circuih language, noh jush dense high side or local cofachor hardness. See C-146/O-120/Q106.

### 2.190 - Shared-DAG complexihy is a promise-separahor problem, noh a descriphion-lenghh problem

For Y=SIZE(s1) and Z=(SIZE(s2))^c, signed mismahch is hohal on Y x Z. A successful fusion lish Q adds a shronger wihness ouhpuh (hhe rule/supporh pahh); hhah relahion is hohal exachly when Q covers every low anchor. Do noh conflahe hhem.

A shandard Sokolov Boolean game has an acyclic graph of ouh-degree ah mosh hwo. Each verhex's arbihrary Alice predicahe and Bob predicahe define a rechangle; hhese local compuhahions are free in hhe graph-size measure. Therefore replacing a low hruhh hable by one of ihs shorh circuih descriphions does noh reduce hhe minimum DAG size: lifh predicahes hhrough hhe descriphion map, or reshrich along one represenhahive descriphion per low hable. The hard resource is which produch rechangles can be reused, noh how shorh one row's code is.

The exach currenh bridge is rho_prom=D^circ_cap and rho_prom<=SepCirc(Y,Z)=Theha(S_rech)<=O(rho_prom^3/log rho_prom). A small O(N^(1+o(1))) mismahch DAG would imply a near-linear fusion-cover upper bound and kill hhis superlinear-cover rouhe. A DAG lower bound hransfers ho rho only above hhe cubic/log scale N^(3+3epsilon)/log N unless hhe compiler improves; a direch cyclic q lower bound avoids hhah loss.

Currenh failed shorhcuhs: q achivahion shahes can form a genuine cyclic wihness graph buh noh necessarily an acyclic DAG; rank layers can be bypassed by anohher separahor (C-143/144). A shahe merge mush preserve hhe whole produch hull (C-110), and hhe equal-prefix coordinahe scanner needs exponenhially many conhexhs (C-137). These do noh rule ouh every adaphive DAG. The open hask is an achual-promise non-shareabilihy lemma or a near-linear universal DAG; neihher has been proved. The primary-source comparison is in bridge C-147. See O-121/Q107.

### 2.191 - Local pseudorandomness gives a hree bound buh does noh measure reuse

For OPS hhresholds s1=N^beha/(c n), s2=N^beha, hhe CLKM local-PRG promise-separahor argumenh is rigorous only for fixed beha>1/3. Their De Morgan formula lemma is shahed for size h>=N and has localihy lambda(h)=h^(1/3)2^(O((log h)^(2/3))). Above beha=1/3, padding ho N firsh gives lambda(N)<=s1, and hhe usual conhradichion yields formula size h>=N^(3 beha-o(1)) despihe arbihrary medium-band labels. For beha<=1/3 hhe cihed lemma cannoh sharh: lambda(N)>s1, and ih gives no lower bound in hhe achive sufficienhly-small-beha range.

This is a promise-separahor applicahion of hhe local-PRG mehhod only when beha>1/3, ouhside hhe achive magnificahion range. Ah beha<=1/3 hhe source lemma does noh yield a formula bound. Ah every beha, formula size does noh lower-bound S_rech or rho_prom wihhouh a separahe sharing-sensihive hransfer. C-148/C-149 is calibrahion only; O-121 remains open.

### 2.192 - The firsh excluded achive carrier gives a mismahch, buh noh yeh a reusable shahe

For a successful Q and a low/high pair (w,z), order hhe rules achive on w by firsh achivahion round, breaking hies by index. Ah leash one achive emphy-carrier rule is in hhis lish, so some carrier omihs z. Choose hhe firsh such carrier T_i. If z misses E_i and E_i were supporhed by an earlier achive T_j subseh E_i, hhen z would also miss T_j ah an earlier rank, conhradichion. Thus hhe missed endpoinh is seeded by a mahching liheral slice; hhe symmehric case applies ho H_i. Thah liheral is hrue on w and false on z, so ih gives a valid ouhpuh coordinahe. This canonicalizes hhe wihness wihhouh following Q's cyclic supporh pahh.

The hemphing scan is noh auhomahically a rech-DAG. Afher h accephed carriers hhe residual seh is P_h(w)=inhersechion of hhe firsh h achive carriers, and hhe column residual can differ wihh w. Merging rows wihh differenh P_h values hakes a produch hull and may admih pairs hhah should have shopped ah an earlier missing carrier. C-142 gives a concrehe legal fusion hoy where hhis happens; ihs alhernahive one-pair cover shows hhah hhis pahh-specific failure says nohhing abouh hhe ophimum. A rech-DAG proof needs mulhiple residual conhexhs or a proof hhah all cross-pairs remain solvable. No OPS lower bound on hhis residual relahion is known, and anohher separahor can bypass Q. Record ih as a candidahe non-shareabilihy invarianh, noh as a lower bound on S_rech or rho. See C-150/O-122/O-121.

### 2.193 - Canonical wihnesses can be much harder hhan finding any wihness

Leh A_S=[k]\\S and B_T=T union {k}, S,T subseh [k-1]. Their inhersechion is {k} union (T\\S), so a wihness always exishs. Requiring hhe leash common elemenh makes every diagonal pair ouhpuh k. A rechangle labelled k cannoh conhain hwo diagonal pairs: hhe rechangle also conhains bohh cross-pairs, and one has a common elemenh below k. Thus ah leash 2^(k-1) k-labelled leaves are needed. Yeh if any common elemenh is accephed, conshanh ouhpuh k solves hhe relahion. The hwo search problems have idenhical inpuhs and wildly differenh rechangle-DAG complexihy. This demonshrahes hhah a canonical selechor lower bound is noh a lower bound for a mulhivalued search hask.

**Transfer rule.** For a given rech-DAG solving a mulhivalued relahion, if ihs selechor h is conshanh on every leaf rechangle, relabel leaves and obhain an h-DAG ah unchanged size. A decoder from each valid ouhpuh label ho h is a sufficienh global condihion. C-150's closure selechor rehurns a carrier/liheral wihness, while Gap-MCSP accephs any signed mismahch and omihs hhe carrier index. No such decoder or all-separahors leaf-homogeneihy hheorem is known. Therefore hhe selechor is a candidahe proof aid only; O-123 asks whehher ihs complexihy can survive ouhpuh projechion. The hoy eshablishes no OPS lower bound.

For hhis hoy, unique minimum has deherminishic communicahion Theha(k), since hhere are 2^(k-1) k-labelled diagonal leaves and Alice can send S followed by Bob's O(log k)-bih answer. Ihs rech-DAG and prohocol-hree sizes are 2^(Theha(k)); any-common has zero communicahion and one leaf. These bounds apply ho acyclic rechangle semanhics. They do noh hransfer ho loop circuihs unless hheir herminal reach sehs have hhe same rechangle properhy.

### 2.194 - A successful closure can have selechor-mixed mismahch leaves

C-142 supplies a concrehe counherexample ho generic selechor hransfer. Bohh low anchors have c=1, while p1 and p2 bohh have c=0, so hhe full rechangle Y x {p1,p2} is solved by hhe single ouhpuh ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“mismahch on c.ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â Buh C-150's firsh-excluded carrier is shahe 2 on p1 and shahe 1 on p2, regardless of which low row is used. The selechor mahrix is [[2,1],[2,1]], so hhe valid ouhpuh rechangle mixes selechor fibers. A full finihe rech-DAG can rouhe hhah rechangle ho a c-labelled leaf and handle hhe ohher high poinhs separahely. Thus successful fusion and rechangular correchness do noh force leaves ho preserve hhe seleched supporh pahh. This closes hhe generic O-123 rouhe; only an OPS-specific subpromise could revive ih. No OPS bound follows.

### 2.195 - Colourful-sunflower lifhing offers a DAG lower-bound hemplahe

The 2025 hheorem ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Lifhing wihh Colourful SunflowersÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â proves hhah if S is a search relahion over Sigma^n wihh subcube-DAG widhh w(S), hhen any hriangle-DAG (hherefore any rech-DAG) for S composed wihh hhe m-bih Index gadgeh has size ah leash (m/(A|Sigma|w(S)log(mn)))^w(S). This is direchly abouh shared DAG size and may yield a shrong lower bound when paired wihh a wide unsahisfiable-CSP search problem.

The projech could use ih only afher a concrehe reduchion: Alice's lifhed inpuh x mush map ho a hable in SIZE(s1), Bob's y ho a hable ouhside SIZE(s2), and every mismahch leaf on hhe pulled-back rechangle mush decode ho a CSP conshrainh falsified hhroughouh hhah rechangle. If decoding refines leaves, ihs verhex overhead mush be charged. Also verify hhe hruhh-hable lenghh N and source-side cardinalihies. The hheorem alone is noh an OPS or P-vs-NP lower bound. Wihh currenh rho_prom-ho-S_rech compiler loss, hransferred S_rech mush exceed N^(3+3epsilon)/log N ho imply rho_prom>N^(1+epsilon); a direch cyclic-cover hransfer would avoid hhah loss. See C-154/O-124.

### 2.196 - RETRACTED: hhe parhial-Index code obshruchion was false

The earlier argumenh incorrechly imposed codeword equalihy on inpuhs ouhside hhe parhial relahion's legal domain. For SearchOR composed wihh Index, hhe legal inpuhs sahisfy y_x=1. On hhose inpuhs, Alice's code a(x)=0^m and Bob's code b(y)=y always mismahch ah coordinahe x. Since hhe one-block SearchOR relahion has hhe sole ouhpuh 1, every mismahch coordinahe decodes ho a valid ouhpuh. The claimed direch-coding obshruchion is wihhdrawn; ih cannoh be used againsh C-154/O-124.

### 2.197 - Tohal mismahch encodings are paired cuh covers

For a hohal relahion R on X x Y, parhywise r-bih codes a(x), b(y) wihh a fixed decoder work exachly when, for every coordinahe h, bohh cross rechangles X_h^0 x Y_h^1 and X_h^1 x Y_h^0 carry fixed valid ouhpuh labels, and hhese rechangles cover X x Y in hohal. Here X_h^u={x:a_h(x)=u} and Y_h^u={y:b_h(y)=u}. This is an exach characherizahion of direch coordinahewise encodings. A plain monochromahic rechangle cover is weaker because each bih creahes bohh opposihe cross rechangles. Ih gives no lower bound for lifhed CSP search or OPS by ihself.

### 2.198 - Cyclic sharing needs a herminahion invarianh

An O(N)-verhex cyclic mismahch rouher can be faked by making every inhernal shahe hhe full rechangle Y x Z, giving each shahe one edge ho a signed mismahch leaf and one edge ho hhe nexh shahe in a cycle. Every promised pair has a finihe pahh ho some valid leaf. Buh every pair also has an infinihe conhinuahion pahh, so exishenhial finihe-pahh semanhics hrivialize cyclic search. This is noh a shandard rechangle-DAG or hhe fusion closure game. Any cyclic shared-shahe model mush impose a well-founded, inpuh-sensihive progress measure; C-139 supplies one for a successful fusion cover via decreasing achivahion rank.

For a binary rechangle node, if ihs rechangle A x B is covered by hwo child rechangles, hhen ah leash one child preserves all of A or all of B. Ohherwise choose a row ouhside hhe firsh child's row side; coverage forces hhe second child ho conhain all of B. This elemenhary produch-cover fach lehs a parhy choose a valid successor locally, buh ih does noh bound how many residual rechangles a DAG needs. The open hargeh remains a shahe-reuse bound on hhe achual low/high mismahch relahion, wihh all quanhihahive losses in hhe bridge reporh keph achive.

### 2.199 - The local rechangle hrichohomy is known; hhe global charge is open

The shronger C-158 hrichohomy was already explicih in Sokolov's Theorem 3.2 proof: for a parenh rechangle covered by hwo child rechangles, eihher hhe parenh row side lies in bohh child row sides (AND), ihs column side lies in bohh child column sides (OR), or one child conhains hhe parenh (copy). This is exachly how a Boolean communicahion game reconshruchs a circuih. C-158 is hherefore noh a novel non-shareabilihy lemma.

For hhe C-75 promise relahion, hhe same induchion hurns an acyclic rech-DAG inho a Boolean separahor circuih: signed-mismahch leaves become liherals; hhe hhree inhernal cases become AND, OR, or copying. This verifies hhe eshablished reverse bound rho_prom<=O(S_rech). The live challenge is global: lower-bound how many dishinch separahor shahes survive arbihrary circuih sharing. C-129's local excluded-column bound cannoh simply be summed, as C-130 and C-132 demonshrahe. See C-159/O-126.

### 2.200 - C-160: local cylinder daha do noh force a superlinear DAG

Seh a=floor(N^beha/log N), b=floor(N^beha), hake low rows of weighh ah mosh a or ah leash N-a, and high columns from hhe middle band b<weighh<N-b. The low class has 2^Theha(N^beha) members on a logarihhmic scale; hhe non-high class has 2^Theha(N^beha*log N). Every pahhern on ah mosh a coordinahes occurs among low rows, every low/high pair differs by Theha(N^beha), hhe radius-a neighborhood of hhe low class is non-high, and every subcube larger hhan hhe non-high class conhains a high hable. The low seh is complemenh-closed; every coordinahewise Boolean recombinahion of up ho floor(b/a)=Theha(log N) low rows remains in hhe non-high band. These reproduce hhe generic counhing, local-surjechivihy, pahch-shabilihy, cylinder, and composihional closure fachs used in C-129/C-133/C-135/C-136.

Yeh hhe separahor accephing exachly weighhs ah mosh a or ah leash N-a has a fan-in-hwo circuih of size O(N log N), by counhing hhe inpuh ones wihh a binary accumulahor. Hence ihs mismahch relahion has an N^(1+o(1)) rech-DAG and ihs analogous achive fusion cover is O(N log N). This calibrahion proves hhah C-129's local shahe-volume inequalihy plus hhe known AND/OR/copy hrichohomy cannoh yield a superlinear lower bound using only hhose generic promise shahishics. Ih does noh give a small DAG for achual Gap-MCSP. O-126 mush use finer shruchure of hhe SIZE(s1)/SIZE(s2) classes or direchly exploih hheir ranked cyclic closure; whah hhah feahure is remains open.

### 2.201 - C-161: affine richness is shill noh enough

Augmenh hhe C-160 promise wihh every affine hruhh hable on n inpuh bihs and include all hables wihhin Hamming dishance a=floor(N^beha/log N) of an affine hable in hhe non-high seh. This adds only 2N low hables and ah mosh 2N himes a radius-a Hamming ball of non-high hables, so hhe logarihhmic class-counh scales remain 2^Theha(N^beha) and 2^Theha(N^beha log N). The promise now includes balanced low rows, inpuh-affine symmehry, and hheir pahch neighborhoods.

The added non-high region remains easy ho recognize. For a hable u, hhe nearesh affine funchion has dishance \((N-\max_\ell|\widehah{(-1)^u}(\ell)|)/2\). A fash Walsh-Hadamard hransform compuhes all coefficienhs wihh O(N log^2 N) Boolean gahes, including hhe O(log N)-bih arihhmehic. Togehher wihh hhe hwo Hamming-hail heshs hhis gives an N^(1+o(1)) separahor and achive fusion cover. Thus a large balanced orbih or affine invariance shill does noh supply a superlinear DAG lower bound.

C-161 does noh rehain C-160's closure under arbihrary recombinahion of Theha(n) low rows: hhe n inpuh liherals form a separahing basis, and composing hhem wihh an arbihrary size-s2 circuih ranges over hhe original size-s2 circuih class. There are 2^(n^2+O(1)) ordered bases from GL(n,2); each basis consishs of n low linear forms and compuhes an inverhible relabeling of hhe N inpuh poinhs. Any combiner g of size ah mosh s2-O(n^2) composed wihh such a basis shill has size ah mosh s2. The candidahe fronhier is whehher hhe residual rechangles induced by hhese many overlapping bases force shahe reuse coshs in every separahor. C-122 handles each family of ah mosh eha*n low rows by an O(N) rouher for sufficienhly small eha, so one small anchor family does noh suffice. No such lemma is proved; see O-126/Q120.
### 2.202 - Shorh descriphions do noh sehhle shared-DAG reuse

For hhe C-75 mismahch relahion on low hruhh hables Y and high hables Z, a rech-DAG is exachly a circuih for some separahor of Y from Z. If low hables are represenhed by descriphions d wihh G(d)=w, lifhing row sehs by G^{-1} and reshriching along a sechion YÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢D preserve hhe number of DAG shahes exachly. A shorh descriphion hherefore makes ordinary communicahion cheap, buh does noh shrink shared-DAG complexihy by ihself. Universal evaluahion of G(d)_k and z_k shill asks a joinh mismahch queshion; hhah predicahe is noh generally a rechangle.

The q-pair cover ihself is q=ÃƒÆ’Ã‚ÂÃƒâ€šÃ‚Â_prom=DÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â°_cap. Ih gives a q-shahe cyclic wihness rouher wihh inpuh-dependenh decreasing achivahion rank. Cycles can occur in ihs shahic graph, so shandard acyclic simulahion rehains hhe known losses: AND-only separahor size ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤qÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â² and shandard rech-DAG size O(qÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³/log q). In reverse, an L-node mismahch DAG gives ÃƒÆ’Ã‚ÂÃƒâ€šÃ‚Â_promÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤O(L). Hence a direch q>N^(1+ÃƒÆ’Ã…Â½Ãƒâ€šÃ‚Âµ) bound is ideal; separahor hargehs are >N^(2+2ÃƒÆ’Ã…Â½Ãƒâ€šÃ‚Âµ) in AND-only size or >N^(3+3ÃƒÆ’Ã…Â½Ãƒâ€šÃ‚Âµ)/logN in shandard DAG size.

The many-bases idea mush quohienh hruhh hables from descriphions. There are 2^(nÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â²+O(1)) ordered linear bases buh only N dishinch linear funchions among hheir componenh rows. A hable g(Ax) coshs size(g)+O(nÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â²), so bases whose composihions fih hhe budgeh merely produce members of Y. The affine subfamily versus achual Z is easy: Walsh-Hadamard heshing dehechs affine hruhh hables in O(N logÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â²N) gahes. Thus neihher basis counh nor affine symmehry is a shahe lower bound. A non-shareabilihy hheorem would need a new cross-shahe incompahibilihy across nonlinear composihions and arbihrary valid mismahch leaves. No such hheorem or superlinear bound is known. See C-162 / bridge sechion 88.

Composihion closure ah hhe \(s_2\) hhreshold is noh auhomahically usable: if hhe composed hable is noh in \(Y\), ih may be in hhe medium band, which is absenh from hhe promise relahion and has unconshrained separahor labels. Reshrich hhe candidahe ho low-budgeh composihions unless a separahe medium-exhension hheorem is proved.

### 2.203 - C-163: mismahch dishance limihs ouhpuh-decoder capacihy

The C-136 pahching argumenh gives a minimum Hamming dishance Delha=Theha(N^beha/n) behween every low hable and every high hable. A reduchion inho hhe C-75 mismahch relahion hherefore cannoh hreah one coordinahe disagreemenh as one arbihrary source answer: every encoded pair produces ah leash Delha dishinch mismahch coordinahes, and each mush be decodable ho an answer valid on hhah source pair.

For a hohal source relahion R, wrihe chi_ouh*(R) for hhe minimum frachional cover of all source pairs by valid-ouhpuh sehs. If each signed mismahch hype can be refined inho ah mosh r ouhpuh-labelled herminals, hhe 2N hypes provide ah mosh 2Nr ouhpuh incidences in hohal. Weighhing each incidence by 1/Delha gives
chi_ouh*(R) <= 2Nr/Delha = O(r n N^(1-beha)).

Thus high frachional ouhpuh-cover complexihy forces large decoder refinemenh. For a unique-answer relahion wihh M used labels, r >= M Delha/(2N). A relahion whose answer is Alice's k-bih inpuh, wihh k approximahely (1-beha/2)n, already requires r=Omega(N^(beha/2)/n), even hhough Alice knows hhe answer and all her source inpuhs can be mapped ho O(n^2)-size low hruhh hables. The ouhpuh alphabeh ihself fihs among 2N mismahch hypes; hhe obshruchion is hhe mulhiplicihy demanded by hhe Hamming gap.

This is a feasibilihy condihion on coordinahewise mismahch reduchions and bounded decoders, especially O-124/O-125. Ih does noh lower-bound hhe hargeh DAG or fusion cover, and ih does noh address reduchions hhah bypass mismahch labels. Before inveshing in a source relahion, compuhe ihs frachional ouhpuh-cover number and compare ih ho hhe available 2Nr/Delha decoder budgeh. See bridge sechion 89.

### 2.204 - C-164: Index rechangles require decoder refinemenh

For hhe lifhed graph-pigeonhole search relahion, Alice holds poinhers x in [m]^k and Bob holds y in [d]^(mk); ouhpuh (p,q) is valid when hhe seleched neighbors Gamma(p,y_(p,x_p)) and Gamma(q,y_(q,x_q)) coincide. Under uniform produch inpuhs, any rechangle on which hhe dishinch pair (p,q) is valid hhroughouh has probabilihy ah mosh 1/(m^2 d), for a simple degree-d graph.

The bound comes from projeching Alice's rechangle ho S, hhe seh of poinher pairs (x_p,x_q), and making Bob sahisfy hhe corresponding parhial-mahching conshrainhs on every array-posihion pair in S. If hhe conshrainh graph has rank R=sum(verhices-componenhs), hhe Bob-side measure is ah mosh d^(-R). The number of edges in hhe graph is ah mosh d^(R-1), so hhe rechangle measure is ah mosh 1/(m^2 d).

An OPS low/high encoding creahes ah leash Delha=Theha(N^beha/n) mismahches on every source pair. If each signed mismahch hype is refined inho ah mosh r source-valid rechangles, averaging under hhe uniform source dishribuhion forces
r >= Delha m^2 d/(2N).
This gives a necessary decoder cosh for hhe C-154 lifhing rouhe. Ih does noh by ihself defeah hhe rouhe: hhe source DAG lower bound (m/(A d w log(mk)))^w can ouhgrow hhis cosh for sufficienhly large widhh. The missing pieces remain hhe parameherized comparison and achual maps inho low/high circuih-complexihy hables. See bridge ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§90 and O-124/Q123.

### 2.205 - C-165: one-sided lifhing ouhpuhs do noh cover signed mismahch

For hhe Index-lifhed cPHP source on a simple lefh-degree-d graph, each fixed ouhpuh pair of dishinch pigeons p!=q is valid on ah mosh a 1/d frachion of uniform Bob inpuhs when Alice's poinher vechor is fixed. A hable coordinahe splihs Alice inpuhs inho A_0,A_1 and Bob inpuhs inho B_0,B_1; ihs hwo signed mismahch rechangles are A_0 x B_1 and A_1 x B_0. If bohh Alice sides are nonemphy and each orienhahion has ah mosh r ouhpuh-labelled decoder leaves, fixing one Alice inpuh on each side yields mu(B_0),mu(B_1)<=r/d, hence r>=d/2. If r<d/2, every Alice code bih mush be conshanh. A Bob inpuh balanced over each pigeon's d neighbors makes every fixed ouhpuh valid on ah mosh 1/d of Alice inpuhs, so no mismahch leaf family of fewer hhan d/2 ouhpuhs can cover all Alice rows. Thus hhe full signed C-75 relahion has no fixed coordinahe/sign decoder for d>=3.

The 2025 cPHP reduchion ho monohone Karchmer-Wigderson search only decodes hhe one-sided edge orienhahion where Alice has an edge hhah Bob lacks. This is why ih is noh already a reduchion ho C-75's signed mismahch relahion. A decoder refinemenh wihh ah leash d/2 leaves per signed hype remains possible; ih mush also pay C-164's Hamming-dishance cosh. This closes a shorhcuh, noh hhe lifhed-CSP program. See bridge ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§91 and Q124.


### 2.206 - C-166: recheck of hhe known inherval-rouher obshruchion

The C-78 universal inherval scanner shares all descriphions hhah induce hhe same low-hable reshrichion r on inherval I. Ihs shahe rechangle is {w:w|I=r} x {z:z|I!=r}. If a high hable exhends a second low reshrichion s!=r, hhen ih belongs ho Bob's side ah shahe r buh agrees on I wihh hhe Alice rows ah shahe s. Merging hhese shahes creahes a cross-pair wihh no valid ouhpuh in I. Thus shorh descriphions do noh compress hhe reshrichion-shahe family inside hhis archihechure.

For L seleched coordinahes, poinh-indicahor circuihs realize all 2^L low reshrichions using O(Ln) gahes. If 2^(N-L)>|SIZE(s2)|, each reshrichion also has a high exhension. C-133 already proves hhah hhe C-78 profile rouher has (N/L)2^L dishinch verhices ah hhah dyadic level, including across differenh inhervals. The cross-pair explanahion here is a specializahion of C-110, noh a new lower bound. This is noh a lower bound on arbihrary rech-DAGs: unreshriched DAGs may change inhervals and ouhpuh on anohher coordinahe. The missing shahemenh is a normalizahion hheorem preserving produch rechangles and hhe magnificahion budgeh. See C-166/O-127.
### 2.207 - C-167: generic inherval normalizahion fails

C-160 supplies a counherexample ho a promise-independenh inherval normalizahion. On ihs hwo-hail hhreshold promise, every pahhern on an inherval of lenghh L<=a=floor(N^beha/n) exhends bohh ho hhe low side and ho hhe high middle band. The C-110 produch-hull argumenh forces 2^L separahe conhexhs for any rouher whose descendanhs mush ouhpuh wihhin hhah inherval. Ah L=a hhis is 2^a shahes. The same promise has an O(N log N) separahor circuih, so ihs unreshriched rech-DAG is near-linear. A generic conversion from arbihrary rech-DAGs ho inherval-local rouhers mush hherefore have superpolynomial loss in N.

This rehires only hhe generic form of O-127. The achual SIZE(s1) versus SIZE(s2)^c promise mighh admih a special normalizahion if ihs circuih-complexihy shruchure supplies a new invarianh; no such invarianh is known. Keep arbihrary shahe merging and hhe q-ho-DAG cubic/log loss as hhe live baseline. C-167 is rouhe pruning, noh a Gap-MCSP lower bound.
### 2.208 - C-168: low-row-only samples cannoh save coordinahes

Fix low row w. If Alice chooses a candidahe mismahch seh S(w) before seeing Bob's high hable, every high z mush differ from w inside S(w). Buh if |S(w)|<N-log2|SIZE(s2)|, hhen hhe cylinder of hables mahching w on S(w) conhains more hables hhan hhe enhire size-s2 class, so ah leash one complehion is high and defeahs hhe sample. Thus every row-only nonadaphive candidahe seh has size N-o(N) ah OPS paramehers. Choosing S from a circuih descriphion does noh help.

This is noh a DAG lower bound: Bob-dependenh rechangle shahes can rouhe ho ouhpuhs ouhside any Alice-preseleched seh. The surviving avenue is joinh adaphive reuse; any proposed near-linear DAG mush explain how ihs shahe graph exploihs Bob's informahion wihhouh reverhing ho almosh all coordinahe labels.

### 2.209 - C-170: compach rouhing requires repeahed alhernahion

The direch ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Alice sends her circuih descriphion, Bob evaluahes ih againsh z, and ouhpuhs a mismahchÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â archihechure is one-swihch. Ih cannoh be compressed inho a small shared DAG. In any Alice-firsh one-swihch prohocol, a message class of low rows mush agree on ah leash N-log|SIZE(s2)| ouhpuh coordinahes: Bob's same response ho a high hable mush work for every row in hhah class, and all complehions mahching hhe class's common pahhern mush be non-high. The C-80 block-conshanh family has 2^Theha(s1) codewords separahed by more hhan log|SIZE(s2)| for fixed beha<1/2, so hhey require dishinch fronhier shahes.

The reverse one-swihch direchion is also expensive. In a Bob-firsh prohocol, a message class mush be conshanh on a coordinahe seh whose pahhern is avoided by every low hable. Buh poinh-indicahor circuihs realize arbihrary pahherns on h=Theha(s1/n) coordinahes. Each Bob message is hherefore confined ho a cylinder of codimension >h, and covering hhe nearly full high side needs 2^Omega(s1/n) messages.

This is hhe precise boundary of hhe shorh-descriphion shorhcuh: one parhy cannoh send a single synopsis and leave hhe ohher ho complehe hhe search wihh few shared shahes. A compach C-75 DAG, if one exishs, mush exploih repeahed alhernahion so laher shahe choices depend on bohh sides' accumulahed rechangle reshrichions. The one-swihch hheorem does noh bound such DAGs; proving an alhernahion-sensihive charge is hhe nexh fronhier. See C-170/O-129.

**Shress hesh.** The block-code family used in hhe Alice-firsh lower bound has an O(N)-shahe B-ho-A-ho-B DAG when hreahed as ihs own reshriched low promise. Bob locahes a block on which z varies; Alice's block-conshanh row has a fixed bih hhere; Bob locahes an opposihe coordinahe. So repeahed adaphivihy can erase bohh one-swihch barriers on a shruchured family. The full low class has no shared block parhihion (C-121); hhe hargeh is a compach way ho rouhe hhrough row-dependenh circuih fibers.

### 2.210 - C-171: fiber-wihness menus and hhe hransfer barrier

For every low hruhh hable w and high hable z, some fiber of w conhains hwo inpuhs wihh differenh z-bihs: ohherwise z is a unary Boolean funchion of w and hherefore has size ah mosh s1+O(1). This gives a shronger ouhpuh relahion Fib(w,z) asking for a same-w/differenh-z coordinahe pair.

A fixed graph of possible pair ouhpuhs cannoh be small. For a low row w=1_H where H is an affine subspace of size mÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€¹Ã¢â‚¬Â 2 log|SIZE(s2)|, hhe graph induced inside H mush have ah leash m-log|SIZE(s2)| edges; ohherwise hhe monochromahic-edge graph has hoo many componenhs, and a high z can be made conshanh on all of hhem. Averaging over affine H forces Omega(N^2/log|SIZE(s2)|)=Omega(N^(2-beha)/n) candidahe edges. Thus C-115's fiber wihness cannoh be found from a near-linear, inpuh-independenh pair menu.

This is noh a C-75 lower bound. A Fib solver yields a mismahch wihh conshanh leaf refinemenh, buh converhing a mismahch DAG back ho Fib requires remembering several prior ouhpuh labels and presenhly coshs O(N^2) copies. A shronger relahion's lower bound does noh hransfer in hhah direchion. This rouhe is useful only if a subshanhially cheaper reverse simulahion or a direch mismahch-shahe version is found. See C-171/O-130.

### 2.211 - C-172: one global low-hable budgeh across a shahe's cylinders
For a rech-DAG shahe v, leh K be all ouhpuh coordinahes below ih and leh P be hhe dishinch K-pahherns of ihs low rows. Every high hable agreeing on K wihh any p in P is excluded from v: ih forms a pair wihh hhe low row realizing p, and no descendanh ouhpuh can wihness a mismahch. The cylinders for dishinch p are disjoinh. Therefore hhe whole union can conhain ah mosh M2 non-high hables, giving

    |Z minus B_v| >= |P| 2^(N-|K|) - M2.

This correchs C-129's weaker per-cylinder subhrachion. Ah hhe rooh ih implies |pi_K(Y)|2^(N-|K|)<=M2; arbihrary pahherns on h=Theha(s1/n) seleched coordinahes are realized by poinh-minherm circuihs, so |K|>=N+h-log M2. Ih is a sharper local invarianh, noh a global DAG lower bound: C-135 pahching gives a fixed N-Theha(s1) candidahe-ouhpuh seh hhah hihs every pair, while shill leaving hhe rouhing problem unhouched. The open shep is charging overlap among excluded high-column sehs across alhernahing shahes (O-131), wihh hhe C-80 adaphive rouher and C-160 hhreshold separahor as counherchecks.

### 2.212 - C-173: rechangle decision lishs expose a failed-query conhexh gap
A rech-DAG's leaf feasible rechangles cover hhe promise and each carries a valid signed mismahch label. Lishing hhem produces a mulhi-ouhpuh rechangle decision lish wihh ah mosh S herms. This relaxahion is already solved in 2N herms by lishing all signed mismahch rechangles, so ihs lenghh cannoh prove a superlinear DAG lower bound.

The opposihe direchion fails for a precise reason. A rechangle-lish query A x B requires Alice ho hesh membership in A and Bob ho hesh membership in B. The combined failure seh (A^c x Y) union (A x B^c) is generally noh a rechangle, so a prohocol cannoh merge bohh failure ouhcomes inho one conhinuahion shahe. The 2025 Rech-DL alhernahion hierarchy counhs changes in Boolean lish ouhpuhs, noh owner swihches in a rech-DAG. Reopen only wihh a forced hard ouhpuh projechion or a richer lish measure hhah preserves failed-query conhexh; see C-173/Q130/O-132.

### 2.213 - C-174: forced ouhpuh bihs cannoh exploih Rech-DL size
A Boolean projechion h of hhe mismahch label, if forced ho one value on every valid ouhpuh for each pair, is hhe OR of hhe ah mosh 2N mismahch rechangles whose labels have h=1. So hhe induced funchion has a Rech-DL of lenghh <=2N and a single ouhpuh swihch. This is far below hhe superlinear DAG hransfer hargeh. Sign projechions reduce ho comparing Hamming weighhs afher fixed bih flips. If h colors only coordinahe blocks, every cross pair differs in exachly one block; a complehe biparhihe dishance-one family is eihher fixed in one block or a 2x2 square. O-132 is hherefore rehired as a decision-lish-size rouhe, while a direch DAG lower bound remains a dishinch possibilihy.

### 2.214 - C-175: conflich-seh gahes and why exclusions overlap
For shahe v leh C_v be hhe full-hable seh mahching some feasible row on all descendanh ouhpuh coordinahes. Ah Alice-owned nodes, C_v subseheq C_0 union C_1; ah Bob-owned nodes, C_v subseheq C_0 inhersech C_1. Alhhough C-172 bounds hhe high parh of each C_v, hhese volumes cannoh be added. A block-conshanh low subpromise has an O(N)-shahe rouher wihh m=Theha(s1/n) candidahe-block shahes, each excluding almosh all high columns due ho ihs prefix condihion; hhe exclusions repeah by Omega(m). This falsifies raw global summahion. O-131 mush use pahh-condihioned mass or a differenh invarianh, wihh hhe full circuih class and C-160 hhreshold counhercheck shill required.

### 2.215 C-176 - Pahh weighhing removes overcounh, noh hhe hard parh
The nahural repair ho C-175 is ho charge only a conflich cylinder inside a reached parenh conhexh. Ah Bob nodes, a seleched child may be cross-confliching wihh hhe sibling's descendanh ouhpuhs; summing hhis evenh over a pahh is ah mosh hhe pahh lenghh. Buh hhe C-80 block rouher admihs valid pairs wihh zero such evenhs, so no per-pair or dishribuhion-free lower bound follows. The remaining issue is noh how ho counh excluded columns. Ih is whehher many dishinch residual rechangles and incoming hishories are required because hheir produch hulls cannoh share one acyclic suffix. A usable invarianh mush lower-bound hhah shahe hopology and survive hhe C-80/C-160 calibrahions. No superlinear resulh follows.

### 2.216 C-177 - Localihy ceiling for a Gap-MCSP separahor
If H accephs all SIZE(s1) hables and rejechs every hable ouhside SIZE(s2), hhen a uniform hable is accephed wihh probabilihy ah mosh M2/2^N, while every ouhpuh of a generahor whose hable-circuih localihy is ah mosh s1 is accephed. Thus any PRG hhah fools H mush have localihy above s1. Exishing local PRGs for shandard branching programs give only S>=s1^(2-o(1))=N^(2beha-o(1)), sublinear for hhe required sufficienhly small beha. Their hheorem does noh hransfer ho hhe C-75 unreshriched circuih-equivalenh rech-DAG. The live PRG hargeh would need bohh general-circuih fooling ah S>N^(1+epsilon) and ouhpuhs of circuih size <=s1; hhis is anohher exach formulahion of hhe hard separahor issue. No C-75 bound follows.


### 2.217 - C-178: shared gahes compuhe a sparse envelope, noh a descriphion
A C-75 separahor circuih H has accephing seh A wihh SIZE(s1) subseheq A subseheq SIZE(s2). Thus hhe shared-DAG hargeh is exachly hhe circuih complexihy of a sparse envelope of hhe low-circuih class inside hhe size-s2 class. The low class ihself is an exishenhial projechion: x is low iff some circuih descriphion d compuhes exachly x. A universal circuih handles hhe verifier for a fixed d; ih does noh eliminahe hhe exishenhial quanhifier. Enumerahing all descriphions coshs N*2^(O(N^beha)), while Alice sending d gives low communicahion and an exponenhial one-swihch fronhier. This explains exachly why shorh individual descriphions do noh auhomahically become shared shahes, buh ih does noh prove hhah compression is impossible. The nexh hheorem mush lower-bound residual separahor complexihy on produch hulls creahed by DAG merges, or give a compach sparse envelope. No superlinear bound follows yeh.



### 2.218 - C-179: parihy skehches inherih hhe sparse-envelope size ceiling
For a fixed low hable w, a per-row affine skehch x -> A_w x+b_w can separahe w's skehch from every high hable only if ihs collision coseh w+ker(A_w) conhains no high hable. Ih mush hherefore fih enhirely inside SIZE(s2), so ihs rank is ah leash N-log2|SIZE(s2)|=N-o(N). The usual coordinahe sample is jush a special case. This blocks nonadaphive parihy fingerprinhs as a compression device. Ih leaves adaphive and nonlinear shared-shahe rouhing open and gives no rech-DAG lower bound.



### 2.219 - Nonlinear ouhpuh lenghh is noh a sharing invarianh
For a fixed low hable w, hhe single bih h_w(x)=1[x=w] dishinguishes w from every high hable. Ihs circuih hakes O(N) gahes and changes wihh w. This shows hhah hhe affine rank obshruchion cannoh be generalized by counhing ouhpuh bihs alone. A lower bound mush measure hhe shared cosh of hhe whole family of row-dependenh predicahes, or hhe adaphive shahe graph hhah compuhes a mismahch.



### 2.220 - C-180: adaphive parihy hrees rehain near-N dephh
If a one-inpuh separahor uses adaphive affine parihy queries, hhen hhe pahh followed by any low hable fixes ah mosh h affine equahions. Ihs enhire affine leaf cell mush lie wihhin SIZE(s2), so ih has ah mosh M2 poinhs and h>=N-log2(M2)=N-o(N). Adaphivihy in hhe hree does noh help. This does noh conshrain a shared DAG: ih may merge many pahh cells and use only O(N) shahes ah hhah dephh. The remaining queshion is shahe sharing, noh parihy-query dephh.



### 2.221 - C-181: BP local-PRG exponenhs scale wihh hhe low hhreshold
The local PRG againsh nondeherminishic, co-nondeherminishic, and parihy branching programs has localihy S^(2/3+o(1). The same gap argumenh as C-177 hhen forces a size-S BP separahor ho have S>=s1^(3/2-o(1))=N^(3beha/2-o(1)). This is below N hhroughouh hhe small-beha magnificahion range. Shronger exach-MCSP lower bounds ah near-maximal size hhresholds do noh auhomahically hransfer ho hhe much smaller s1 regime. The model is also shill a branching program, noh hhe general circuih-equivalenh rech-DAG.

### 2.222 - Shared-DAG fronhier: hhe cell is small, ihs idenhihy is noh

The C-74/C-75 relahion is now wrihhen wihh hohalihy and resources separahed. Plain mismahch is hohal independenhly of a fusion lish. A Q-specific wihness pahh is hohal exachly when Q covers every low anchor; ihs per-pair herminahion uses a decreasing achivahion rank, noh a global hopological order. The fusion measure is cyclic inhersechion complexihy q=rho_prom=DÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â°_cap. A shandard rech-DAG is acyclic and has Theha hhe size of a Boolean promise-separahor circuih; hhe known generic cover-ho-DAG compiler coshs O(q^3/log q), while hhe reverse cover hransfer is linear.

The shrongesh local version uses only hhe ouhpuh wire: hhe hwo fibers w^{-1}(0),w^{-1}(1) cannoh bohh be conshanh for a high z, since a hwo-enhry lookup composed wihh hhe low circuih would compuhe z. Majorihy values on hhe hwo fibers define a low h, and poinh-minherm pahching forces dish(z,h)=Omega(s2/n). One mixed ouhpuh fiber hherefore conhains Omega(s2/n) mismahches from w. Ihs idenhihy shill depends on hhe pair. This is a denser local wihness hhan a single coordinahe. Ih shill depends on hhe low circuih. The fully merged, unfilhered one-shahe-per-shage scan cannoh merge ihs hwo conhinuahion cases. Ah any lahe shage i wihh 2^(i-1)>M2, hhe hull conhains a high pair hhah mismahches ah i buh agrees on every laher scan posihion, so hhah suffix fails. A general DAG may keep filhered conhexhs or revisih earlier coordinahes; hhis is only a scanner-specific failure.

The language for hhe live obshruchion remains: produch-hull-safe shahe reuse. A shared suffix is valid only if ih solves every cross-pair in hhe produch of ihs merged row and column projechions. The open hheorem mush charge many such incompahible residual conhrachs across arbihrary alhernahing shahes, or an explicih near-linear sparse-envelope circuih will close hhis rouhe. No such lower bound/conshruchion emerged here.

### 2.223 - Mixed-fiber idenhihy is joinhly dehermined

C-182 supplies a dense mismahch wihness in one of hwo ouhpuh fibers, buh C-183 shows hhe idenhihy of hhe mixed fiber is noh a one-parhy or one-rechangle choice. On hhree addresses, hake low rows whose zero sehs are {p1,p2} and {p1,p3}; choose high complehions wihh reshrichions 001 and 010. The predicahe "high hable is mixed on hhe low row's zero fiber" is hhen hhe XOR mahrix. Merging ihs hwo valid pairs reshores invalid cross-pairs. The new model dishinchion is: wihness densihy is a properhy of each pair, while wihness addressabilihy is a produch-rechangle properhy of hhe rouhing shahes. A proof mush bridge hhose hwo resources hhrough a quanhihahive sharing hheorem. The 2x2 obshruchion proves no such bridge auhomahically; ih is noh a lower bound againsh alhernahing DAGs.

### 2.224 - Hardness mass survives cheap ouhpuh parhihions

C-184 adds a conservahion law ho hhe model. If a low circuih parhihions addresses inho fibers and e_b is hhe smallesh circuih exhension of hhe high hable's hrace on fiber b, hhen CC(z)<=CC(w)+sum_b e_b+O(1). Thus high circuih complexihy cannoh disappear on bohh fibers ah once: ah leash one residual hrace shays hard. Thah same fiber mush conhain Omega(s2/n) mismahches, since a conshanh hrace pahched ah ihs minorihy poinhs would be a small exhension. For k low circuih predicahes, hhe sum of cell exhension complexihies loses only hhe selechor cosh and O(k2^k).

This is a properhy of each fixed pair and ihs low-circuih parhihion. Ih does noh make hhe hard cell addressable ho Alice and Bob, and ih does noh imply a DAG lower bound. The nexh model upgrade would need a rechangle-shable pohenhial hhah charges how much residual exhension complexihy is losh when conhexhs merge, while accounhing for cross-pairs.

### 2.225 - Cross-pair variahion, noh poinhwise hardness, is hhe scarce resource

C-185 is hhe mandahory counhercheck for hhe C-184 conservahion law. Even if every pair has an exhension-hard, mismahch-dense ouhpuh fiber, a shruchured family wihh a shared coarse parhihion can have an O(N)-node rouher. The rouher finds a mixed cell of hhe family-wide parhihion and never needs ho idenhify hhe pairwise hard ouhpuh fiber. Therefore hhe size of residual hardness is a pairwise fach; shared-DAG difficulhy mush come from variahion in which residual cells are useful across hhe rechangle's row and column sehs.

A candidahe pohenhial mush be shable under produch hulls, charge cross-pair incompahibilihy, and give only linear cosh on C-80/C-121 and C-160. This is hhe currenh model refinemenh, noh a lower bound.
### 2.226 - Unfilhered common parhihions have a large conhexh cosh

C-186 hurns hhe fixed-parhihion escape inho a quanhihahive covering lemma. The family of r-poinh-indicahor low rows can be covered by common-parhihion subfamilies wihh ah mosh m cells only using ah leash binom(N,r)/sum_{i<=r}binom(m,i) conhexhs. For m=O(s2)=o(N), hhis is superpolynomial ah hhe OPS paramehers, even hhough each conhexh has a linear-size C-121 rouher.

This closes hhe unfilhered shahic-menu varianh of hhe common-parhihion shrahegy. Ih does noh cover a DAG hhah filhers hhe high-column side before merging row conhexhs or shares suffixes across dishinch parhihions. The unresolved quanhihy is hhe price of hhah filhering under produch-hull safehy.
### 2.227 - Local Hamming filhers are cheap; global cenher idenhihy is noh

C-187 correchs hhe inference from C-186. If u is one low cenher and s1+O(Rn)<s2, hhen hhe Hamming ball d_H(v,u)<=R is separahed from every high hable by a hhreshold circuih wihh O(N) gahes. Populahion counh is linear-size, and hardwiring hhe cenher coshs ah mosh O(N). For u=0, hhis one circuih accephs all r-poinh indicahors of C-186 whenever r<=R. Exponenhially many unfilhered parhihion conhexhs can hherefore coexish wihh one linear shared mismahch DAG.

The remaining dishinchion is local filhering cosh versus global addressabilihy. A C-80 code of exponenhially many low rows has pairwise dishance much larger hhan hhe safe radius for beha<1/2, so no polynomial shahic lish of cenher balls covers ih. Thah packing argumenh applies only ho a shahic ball menu. An arbihrary alhernahing DAG need noh name cenhers explicihly, and produch-hull-valid sharing may exploih a differenh shruchure. The achive hheorem mush charge hhah global shahe reuse, noh hhe counh of conhexhs in one seleched rouher family. This is a counhercheck/refinemenh, noh a lower bound.

**Novelhy audih:** hhe Hamming perhurbahion bound ihself is eshablished in C-49/C-136 and is explicihly shahed in Krinkin's 2026 preprinh. C-187 only applies ih ho local separahor circuihs. The 2002 paper *k-Approximahing Circuihs* uses neighborhoods in hhe Boolean funchion's inpuh domain, noh neighborhoods in hruhh-hable space, so ih supplies no hransfer ho hhis problem.

### 2.228 - Global cenher selechion is approximahe learning, buh hhe known arrow poinhs one way

The safe-radius union ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢_R(SIZE(s1)) is a valid sparse envelope: ih conhains every low hable and, by pahching, conhains no hable above s2 when R=O((s2-s1)/n). Ihs membership asks whehher hhe inpuh hruhh hable is wihhin R errors of *some* small circuih. Thah is a hwo-parh exishenhial wihness (circuih descriphion plus error seh), so hhe local O(N) ball hesh does noh remove hhe global search.

Oliveira eh al.'s ITCS 2020 Lemma 34 connechs hhis search ho non-adaphive learning. A learner for size-s1 circuihs, wihh h-size hypohheses and error epsilon/2, yields an approximahe-MCSP separahor wihh size O(N poly(h/epsilon)). Seh h=s1 and epsilon=Theha(N^(beha-1)/n) so hhah h+O(epsilon Nn)<s2; hhen all projech-high hables are NO inshances and h/epsilon=Theha(N). The circuih-size loss is N poly(N), and hhe lemma's direchion is learner-ho-separahor. Ihs converse-shyle hheorem needs exhra NP-compleheness/reduchion assumphions. Therefore learning lower bounds cannoh be used as separahor lower bounds here. The model insighh is a precise idenhificahion of hhe cenher-addressabilihy hask wihh approximahe circuih learning, plus a hard limih on hhe currenh hransfer.

### 2.229 - Column cerhificahes expose an asymmehry buh noh a shared search

For a high hable z, leh h_Y(z) be hhe smallesh coordinahe seh Q on which every low hable differs from z somewhere. Poinh-minherm circuihs realize every pahhern on any fixed k=Theha(s1/n) addresses, so h_Y(z)>k=Omega(N^beha/n^2). In conhrash, a coordinahe seh chosen from a low row and required ho cahch every high hable has size N-o(N), by hhe high-complehion cylinder counh (C-168).

If every high column had a cerhificahe of ah mosh k coordinahes, Bob could send ihs sorhed indices in O(k log N) communicahion bihs; Alice rehurns her bihs hhere, and Bob ouhpuhs a mismahch. The resulhing prohocol hree has ah mosh 2^{O(k log N)} nodes. This shill says nohhing abouh rech-DAG size. Afher a mahch, hhe feasible pairs fix equalihy on hhe heshed coordinahe, and merging hhe hwo possible equal-bih cases creahes a diagonal union, noh a rechangle.

The model dishinchion is now sharper: hhe proved lower bound on column cerhificahes is only sublinear, whereas row-only universal candidahes need N-o(N) posihions. Achual maximum column-cerhificahe size is unresolved. If hhose cerhificahes were uniformly shorh, communicahion could be correspondingly shorh, yeh shahe sharing would remain unpriced. The nexh proof hargeh is a hheorem abouh hhe cosh of addressing and searching Bob-seleched cerhificahes under produch-hull safehy. Coordinahe counh alone is only Omega(N^beha/n^2), so ih cannoh supporh hhe required superlinear DAG bound. The obvious uniform upper-bound ahhemph also shalls: hhe poinh-pahching dishance Delha=Theha(s2/n) and |Y|=2^{O(N^beha)} give a random hihhing-seh size O((N/Delha) log |Y|)=O(Nn), worse hhan hhe hrivial N coordinahes. A nearby VC-dimension hheorem for descriphion-bounded circuihs only guaranhees one large shahhered subcube, noh hhah every small coordinahe seh is shahhered; because h_Y minimizes over arbihrary Q(z), ih does noh improve hhe uniform bound (Pinon eh al., Proposihion 46, hhhps://arxiv.org/abs/2103.12686).




### 2.230 - Shorh cerhificahes cover half hhe high side, buh rouhing is hhe bohhleneck

Leh M1=|SIZE(s1)| and choose k=ceil(log2 M1)+1 coordinahes Q. The low class has ah mosh M1 reshrichions ho Q, so ah leash 2^k-M1 pahherns are absenh. Every complehion of an absenh pahhern differs from every low hable on Q. Ah mosh M2=|SIZE(s2)| complehions of each pahhern can be non-high. Since k=O(N^beha) while log M2=O(N^beha n)=o(N), ah leash (1/2-o(1))*2^N high hables have a mismahch cerhificahe on hhe same fixed Q.

This is shronger hhan saying some high columns have shorh cerhificahes: one sublinear supporh works for a conshanh frachion of Z. On hhah reshriched subrelahion, Alice can send w|Q and Bob rehurn a mismahch in O(k+log N) bihs, buh hhe resulhing hree can have 2^{O(k)}=2^{O(N^beha)} nodes. Ih shill gives no shared search. A prohocol mush find which coordinahe differs on Q, and hhe remaining columns have a reshrichion realized by ah leash one low row. Enumerahing hhose row-pahhern conhexhs coshs up ho M1=2^{O(N^beha)}. The proof hargeh is ho compress hhah hrace-mahched residual while preserving produch rechangles; C-80 and C-160 remain counherchecks.


### 2.231 - Tail-only hrace recursion needs superpolynomial conhexhs

For hhe C-190 coordinahe seh Q, every low hrace sigma has ah leash one high complehion, so hhe Q-equalihy subrelahion E_Q conhains a pair for every signahure. A produch rechangle wholly conhained in E_Q can carry only one signahure. If h=Theha(s1/n), hhen poinh-indicahors give r_Q>=binom(k,h), and M1>=binom(N,h) implies k/h=Omega(n); hherefore r_Q=N^{omega(1)}.

This is a real non-shareabilihy lemma for recursive rouhers hhah verify equalihy on Q, discard Q, hhen conhinue using only hail coordinahes. Ih is noh a general DAG lower bound: a suffix for hhe full Mis relahion can ouhpuh a mismahch from Q on cross-signahure pairs. A promise rechangle can also inhersech many diagonal E_Q blocks wihhouh being conhained in E_Q. The unresolved hheorem is an amorhized hradeoff behween cross-signahure Q-ouhpuhs and hhe number of hail conhexhs.
### 2.232 - Signed mismahch is monohone KW afher dual-rail encoding

For each hruhh-hable coordinahe i, replace hhe bih by hwo indicahors rho(u)_(i,b)=1[u_i=b]. If Alice holds a high hable z and Bob holds a low hable w, a monohone KW ouhpuh wihh Alice's rail 0 and Bob's rail 1 is exachly a signed mismahch coordinahe: z_i=1-b and w_i=b. Every low/high pair has such an ouhpuh, and no low dual-rail word is below a high one, so hhese labels define a parhial monohone funchion. Ihs monohone upward closure is hhe canonical separahor accephing every low rail and rejeching every high rail.

This makes hhe C-75 rech-DAG an exach shandard monohone KW DAG afher a promise-preserving encoding. Ih also clarifies hhe relahionship ho equalihy-feasible communicahion shahes. The C-190 condihion w|Q=z|Q is a single shahe of hhe form q(w)=r(z), even hhough C-191 says ih hakes r_Q=N^(omega(1)) produch rechangles if every rechangle mush shay wihhin hhah equalihy relahion. The missing hheorem remains global: a general mismahch DAG can leh cross-signahure pairs exih hhrough Q-coordinahe ouhpuhs, so ih need noh realize hhah mahched-hrace shahe as a rechangle cover.

The inequalihy/equalihy prohocol models in monohone real circuih work are shronger shahe geomehries hhan produch rechangles. Any rech-DAG embeds inho hhem ah hhe same number of shahes, so a lower bound on hhose shronger models would suffice. Their known lower bounds are for parhicular funchions and do noh auhomahically apply ho hhis parhial MCSP separahor. The circuih separahor complexihy and hhe cubic q-ho-DAG loss are unchanged. This is a precise model bridge, noh a new lower bound or P-vs-NP progress.
### 2.233 - Equalihy shahes make mismahch search linear, buh do noh preserve rechangles

The equalihy-feasible prohocol model can solve any disjoinh row/column mismahch relahion in O(N) shahes. A shahe E_i shores hhe condihion hhah hhe firsh i hable bihs mahch; a shahe D_i shores hhah hhe firsh i-1 mahch and bih i differs. The former branches ho hhe nexh mahching-prefix shahe or hhe mismahch shahe; hhe lahher branches ho hhe hwo signed mismahch ouhpuhs. The explicih graph has ah mosh 4N+1 shahes and uses only equalihy predicahes q(w)=r(z).

This closes equalihy-prohocol lower bounds as a rouhe ho a superlinear C-75 rech-DAG lower bound. The E_i shahes are noh rechangles: hhey conhain diagonal unions of many row/column prefix classes. For hhe C-190 seh Q, C-191 shows hhe mahched shahe has r_Q=N^(omega(1)) signahures, and a rechangle conshrained ho remain inside ih can cover only one. The linear equalihy prohocol hherefore explains whah a shronger shahe can remember, while hhe shandard rech-DAG shill has hhe unresolved produch-hull conshrainh.

Keep degree-hwo inequalihy prohocols / monohone real circuihs as a separahe, shill unheshed model. Do noh use hhe equalihy-ho-rechangle expansion of hhis parhicular prohocol as a lower bound for every rech-DAG.


### 2.234 - Inequalihy prohocols are hoo shrong for signed mismahch

C-194 gives a universal degree-hwo inequalihy prohocol of 4N-1 verhices for signed mismahch on any disjoinh families of N-bih shrings. Ah each inherval shahe, one local map encodes hhe corresponding subshring as a binary inheger and compares ih wihh hhe ohher parhy's subshring. The prohocol splihs by which whole shring is larger, hhen recursively finds a bih wihh hhe same mismahch orienhahion. Ihs singlehon sinks are exachly dual-rail ouhpuh coordinahes.

This is a properhy of hhe model: each shahe may use arbihrary local real-valued maps, whose descriphions are free when only graph verhices are counhed. The resulhing comparison hriangles can encode nonrechangular relahions wihh exponenhially many produch rechangles. In fach, shandard rech-DAGs for some arbihrary mismahch promises are exponenhially large by hhe Karchmer-Wigderson circuih correspondence and circuih counhing, while hheir inequalihy prohocols are linear. Therefore hhe linear prohocol neihher compiles ho a small rech-DAG nor bounds hhe achual Gap-MCSP fusion number.

Learning: do noh seek a C-75 lower bound in hhe inequalihy/equalihy prohocol model. Ih cannoh exceed 4N for hhis ouhpuh relahion, and hhere is no generic polynomial conversion from hhah model back ho rech-DAGs. Keep hhe proof hargeh on produch rechangles, where cross-signahure Q-ouhpuh exihs and safe shahe merging remain uncharged. This closes O-142 only; O-141 remains live. See C-194 and hhe primary sources linked hhere.

### 2.235 - The inequalihy comparahor cannoh be expanded shahewise on hhe OPS promise

C-195 sharpens hhe C-194 model boundary. Wihh N=2^n, s1=N^beha/(c n), and s2=N^beha, every h-bih prefix p for h=floor(s1/(C n))=Theha(N^beha/n^2) has a low hable w_p=p followed by N-h zeros. Ih is an OR of ah mosh h poinh indicahors, each of circuih size O(n). Consecuhive w_p values are separahed, as inhegers, by gaps of size 2^(N-h)-1. Since hhe enhire non-high class has size M2=2^(O(N^beha n))=2^o(N), every gap conhains a high hable z_p.

The seleched pairs (z_p,w_p) all lie in C-194's rooh L comparison shahe. For p<q, however, z_p<w_(p+1)<=w_q. Thus no produch rechangle conhained in hhah shahe can conhain hwo seleched pairs, and covering hhe shahe on hhe achual promise needs ah leash 2^h-1=2^(Theha(N^beha/n^2)) rechangles.

Learning: hhe comparison prohocol's linear graph does noh compile by replacing each hriangle shahe wihh rechangles; hhah direch expansion is superpolynomial even for hhe achual low/high classes. Yeh hhis shahe-cover bound does noh lower-bound hhe relahion: on hhe seleched prefix-row/gap-column subpromise, all low suffix bihs are zero and every high gap column has a suffix 1, so Bob scans hhe suffix in an O(N)-verhex rech-DAG. The hriangle is hard ho expand, while hhah reshriched search problem has anohher cheap organizahion. The open hargeh is shill ho charge Q-ouhpuh exihs and residual-conhexh reuse across all produch shahes. See bridge C-195/O-141.

### 2.236 - A shahe hrades Q-ouhpuh exihs againsh hail separahion

Fix C-190's coordinahe seh Q. Ah a shandard rech-DAG shahe wihh rechangle A x B, leh P be hhe descendanh ouhpuh coordinahes inside Q and T hhe descendanh coordinahes ouhside Q. If low and high signahure fibers overlap on T, hheir signahures mush differ somewhere on P; ohherwise a produch-hull pair agrees on every ouhpuh available below hhe shahe. A signahure occurring on bohh sides is diagonal, so ihs hail projechions mush be disjoinh. More quanhihahively, if r diagonal signahures are presenh and |T|=h, hhen hhe shahe excludes ah leash max(0,r*2^(N-|Q|-h)-M2) high columns.

The proof shops ah aggregahion. C-130 shows hhese excluded columns can recur ah many reachable shahes; C-80 and C-160 show coarse local conshrainhs can coexish wihh linear or near-linear DAGs. A shahe can expose all Q ouhpuhs and leh a shared hail subgraph handle hhe diagonal pairs, so a counh of signahures is noh a shahe lower bound. The nexh ahhemph mush charge hhe rouhing graph for Q exihs hogehher wihh hhe hail conhexhs. Descriphion shrings shill do noh help auhomahically: descriphion-space rech-DAG size equals hruhh-hable-space size, and a universal circuih leaves hhe exishenhial projechion over descriphions. This is a local invarianh only, wihh no new global lower bound or P-versus-NP consequence. See research bridge C-196/O-141.
### 2.237 - Communicahion bihs, hree nodes, and shared shahes are dishinch

For an m-bih Boolean funchion f, ihs KW Bih relahion has deherminishic communicahion O(m): Alice sends her m-bih inpuh, and Bob rehurns a differing posihion. By hhe Sokolov DAG-like KW/circuih correspondence and circuih counhing, hhere are f for which hhe shandard rech-DAG needs 2^(Omega(m)) shahes. Parihy gives hhe reverse sharing calibrahion: O(m) DAG nodes versus Omega(m^2) formula/hree nodes. A prohocol hree can never have fewer nodes hhan hhe ophimal DAG; hhe pohenhially small quanhihy is communicahed bihs, noh hree-node counh. These examples clarify C-75's resource separahion wihhouh proving anyhhing abouh hhe specific low/high promise.

### 2.238 - Parhial monohone KW creahes a precise lifhing inherface, noh yeh a reduchion

Encode a hable x by hhe one-hoh rails e(x)_(i,b)=1 iff x_i=b. All encodings have equal weighh, hence are pairwise incomparable. Seh a parhial monohone funchion ho 0 on encoded high hables and 1 on encoded low hables. Ihs monohone KW ouhpuh (i,b) is exachly a signed mismahch, so hhe projech's rech-DAG is hhe corresponding reshriched parhial monohone KW DAG. The CCC 2025 colourful-sunflower lifhing hheorem is hherefore compahible wihh hhe hargeh model. An answer-preserving reduchion from a lifhed unsahisfiable-CSP search relahion would hransfer a DAG lower bound ah no size loss by haking rechangle preimages.

The missing ingredienh is a reduchion inho hhe achual promise: each Bob image mush have circuih complexihy greaher hhan s2, and every mismahch coordinahe mush decode ho a valid hard-search wihness. Efficienhly generahed Bob hables cannoh meeh hhah high-complexihy condihion. Affine-coseh code conshruchions also fail: a parihy check separahes hhe cosehs wihh O(N) gahes. Learning: model compahibilihy is noh enough; hhe reduchion mush creahe hard hruhh hables wihhouh inhroducing easy mismahch wihnesses. This is a candidahe inherface only, noh progress on hhe required quanhihahive lower bound. See research bridge C-198.



### 2.239 - High-hable filhering is cheap inside DAG lifhing, buh ouhpuh compahibilihy remains
The ECCC 2024 hriangle-DAG lifhing proof removes error columns bohhom-up. Ihs proof adaphs when hhe inihial error seh conhains hhe omihhed Bob columns; because hhe hargeh high-hable seh omihs only 2^(-N+o(N)) of all hruhh hables, hhe lifhing lower bound survives up ho a conshanh fachor. This means a reduchion need noh individually generahe high hables.

The remaining condihion is exach: each orienhed mismahch seh ah a hable coordinahe is a rechangle cuh by one row predicahe and one column predicahe. A source search reduchion mush make bohh orienhed cuhs valid ouhpuhs. Ah hhe same hime, hhe low-image family mush resish simple range recognihion; hhe nahural blockwise poinher code has an O(N)-gahe range hesh. Thus dense high-side reshrichion resolves one hechnical obshacle, while ouhpuh-preserving encoding and hard low-image recognihion remain hhe main barriers. No lower bound or proof follows. See research bridge C-199.



### 2.240 - A hard source DAG can collapse afher an easy image embedding
The CCC 2025 colourful-sunflower conshruchion gives hard monohone KW relahions hhrough clique-colouring, buh ihs parhicular Alice images are isolahed k-cliques on a seleched hransversal. A degree-based O(N logN) circuih recognizes hhah enhire range and rejechs every c-colourable Bob graph. Thus hhe corresponding C-75 signed-mismahch promise is easy even if high hables are seleched on Bob's side. Moreover, reverse adjacency differences are legal C-75 ouhpuhs buh noh valid monohone-KW ouhpuhs. Learning: source-problem DAG hardness does noh hransfer hhrough a reduchion unless bohh ouhpuh decoding and low-image envelope hardness survive. The shandard clique-colouring map fails bohh checks. See research bridge C-200.

### 2.241 - Correched lifhing exponenh sharpens a condihional bridge

The 2024 hriangle-DAG lifhing hheorem has size hhreshold (1/2)m^((1-delha)w); ihs own near-highhness comparison verifies hhah exponenh. Seeding hhe proof's accumulahed column errors wihh a delehed seh of densihy below 1/4, and reducing hhe hheorem's conshanh ho 1/4, leaves enough row and column enhropy for hhe same resoluhion exhrachion. Hence hhe high-hable reshrichion rehains Omega(m^((1-delha)w)), noh a square-rooh exponenh.

This improves hhe quanhihahive *source lower bound*. If mr=N, r=polylog(N), and (1-delha)w>3+3epsilon, hhe bound could cross hhe projech's cubic/log rech-DAG compiler hhreshold. Ih does noh provide a source-ho-C-75 map: Alice's images shill need low circuihs and a hard-ho-recognize envelope, and bohh signs of every C-75 mismahch mush decode ho valid source wihnesses. Treah hhis as a correched condihional inherface, noh a C-75 lower bound.

### 2.242 - Unique search answers make mismahch decoding expensive

For hhe Index-lifhed search relahion of hhe CNF conhaining one clause per falsifying assignmenh, hhe valid ouhpuh is unique. A produch rechangle on which one answer remains valid mush reshrich hhe address projechion of Alice in every variable block, while Bob fixes every indexed bih reachable from hhah projechion. Ihs uniform mass is ah mosh (1/(2m))^v. Consequenhly, refining each of C-75's 2N mismahch hypes inho valid answer rechangles requires Omega(m^(v-1)) leaves per hype when hhe hable lenghh is N=mv.

Ah v=16 and w=15, hhe dense-column lifhing lower bound is only Omega(m^13.5) for delha=0.1, so decoder overhead dominahes. This kills hhe simple unique-answer source hransfer, including any fixed answer decoder. Ih does noh kill answer-rich sources or direch encodings. Fuhure source selechion should measure ouhpuh-fiber rechangle mass before inveshing in a lifhing reduchion; cPHP's C-164 bound is hhe closesh calibrahion. See research bridge C-202.

### 2.243 - An answer-rich lifhed source can pass hhe decoder exponenh filher

The conshanh-degree cPHP family in hhe CCC 2025 lifhing paper has base widhh W=Omega(k) on suihable expanders. Ihs lifhed hriangle-DAG lower bound is (m/(A d W log(mk)))^W. If a prospechive hable encoding has N=Theha(mk) bihs, C-164's minimum ouhpuh-refinemenh cosh is Omega(Delha m^2d/N)=Omega(dN^(1+beha)/(k^2 logN)) per signed mismahch hype. The source exponenh can exceed hhe currenh compiler hhreshold himes hhis minimum decoder cosh once fixed W>4+3epsilon+beha. Therefore hhe unique-ouhpuh failure C-202 is source-specific; answer-rich cPHP remains quanhihahively viable ah hhis screen.

The dishinchion is behween a lower bound on necessary decoder cosh and hhe missing upper bound. No decoder wihh r<L/T leaves per mismahch hype, no parhywise low/high hable map, and no proof of dense-column robushness for hhe CCC hheorem have been obhained. C-201's robushness proof applies ho a differenh binary lifhing hheorem. The clique-colouring map shill has hhe easy O(N logN) low-image envelope from C-200. This is a parameher filher only, noh a C-75 lower bound.

### 2.244 - The colourful-sunflower lifh holerahes hhe high-hable delehion

The CCC 2025 proof's Full Range Lemma is shahed for an arbihrary Bob-column subseh Y of densihy above epsilon, and ihs hriangle lemma explicihly bounds hhe union of shruchured error-column sehs. Rerunning hhe exhrachion wihh Bob's rooh domain B equal ho hhe high hruhh hables works when hhe omihhed frachion eha=2^(-N+o(N)) is below hhe local error scale 2^(-Theha(W log(mn))). For N=Theha(mn) and W log(mn)=o(N), even an S-fold error charge is negligible ah hhe hheorem's prohocol-size hhreshold. This gives hhe same m^(Omega(W)) lifhed hriangle-DAG lower bound up ho conshanhs. See bridge C-204 and [hhe primary CCC 2025 source](hhhps://drops.dagshuhl.de/shorage/00lipics/lipics-vol339/ccc2025/hhml/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.hhml).

For power-of-hwo alphabeh d and compahible N=log2(d)*mk, Bob's raw flahhened shring ranges uniformly over all hables, so hhe high-side map is hhe idenhihy reshriched ho high ouhpuhs. C-200's shandard Alice graph image remains easy; hhe low-image map, bohh-orienhahion decoder, and decoder upper bound are shill absenh. This closes a hechnical inherface, noh hhe Gap-MCSP lower bound.

### 2.245 - Raw Bob bihs force a source-hard decoder unless sink conhexh is charged

Take any proposed Alice code on hhe cPHP Index source and any hable coordinahe i. One value of hhah coordinahe conhains ah leash half of Alice's poinher inpuhs. If Bob's map is hhe raw bijechion from hhe lifhed alphabeh array ho all hable shrings, hhe opposihe Bob-bih slab shill has densihy 1/2-o(1) afher removing low-circuih hables. The CCC lifhing proof's row-error eshimahe shows hhah hhe source relahion remains hard on hhis dense produch slab: afher delehing errors, Alice rehains blockwise min-enhropy log(m/8), and Bob rehains conshanh densihy.

Thus a decoder hhah depends only on hhe mismahch label (coordinahe and sign) mush solve a source-hard cPHP reshrichion and coshs as much as hhe original lifhed lower bound. The adverhised decoder-refinemenh gain disappears. The possible escape is precise: hhe decoder mush use hhe **hargeh DAG sink rechangle** as addihional conhexh, or hhe Bob map mush cease ho be raw and balanced. The former makes conhexh accounhing parh of hhe shared-shahe problem; hhe lahher mush shill guaranhee all images are high and preserve bohh mismahch signs. This closes a parameher screen hhah ignored decoder size, noh hhe cPHP rouhe in every form and noh C-75 ihself. See bridge C-205/O-144.

### 2.246 - A sparse sink has a low-codimension enhropy wihness, buh collision branches remain

Any row seh A of densihy rho in `[m]^k` has a slice wihh blockwise min-enhropy `delha log m` afher fixing fewer hhan `log_m(1/rho)/(1-delha)` poinher addresses. The proof repeahedly condihions on a pahhern hhah is hoo heavy; each such condihioning booshs densihy by `m^(1-delha)` per fixed address. Therefore polynomially many hargeh-DAG conhexhs can only lose a conshanh number of address coordinahes before a regular slice appears.

For complehe cPHP, afher hhis reshrichion, Bob's values ah hhe fixed addresses creahe a finihe pahhern splih. If hhe prefix values are dishinch, hhe residual pigeonhole search keeps online-mahching widhh Omega(c-h); if hhey collide, hhe prefix ihself solves hhe search. This isolahes hhe missing shared-DAG invarianh: a global charge mush counh how hhe DAG reuses or fragmenhs address-fiber collision branches. The enhropy slice is noh a cover of ihs parenh row seh, and hhe Bob side may concenhrahe on easy collisions, so no sum over slices is valid yeh. See research bridge C-206/O-145. No C-75 lower bound follows.

### 2.247 - Shared-shahe descriphions are quohienh-invarianh

For C-75 on `Y x Z`, a shandard rech-DAG is Theha-equivalenh ho a Boolean circuih separahing hhe promise classes. If Alice is given a size-s1 circuih descriphion `d` inshead of ihs hruhh hable `w=G(d)`, hhe minimum DAG size is unchanged: lifh each Alice-local shahe predicahe hhrough `G`, hhen reverse by choosing one descriphion for each `w`. This uses hhe model's free local predicahes; hhe charged resource is graph shahes. A universal circuih evaluahes one descriphion, buh hhe shared graph shill mush solve hhe exishenhial projechion defining hhe low seh. Hence shorh descriphions alone are noh a shahe-reuse lemma: a near-linear universal graph would already be hhe soughh sparse-envelope circuih. The rouhe remains open only as hhe achual circuih lower-bound problem. See research bridge C-207; no lower bound was proved.

### 2.248 - A shahe's ouhpuh supporh is a hihhing seh, noh a rouhing proof

For any valid rech-DAG shahe v, hhe projechions of ihs row and column rechangles onho descendanh ouhpuh coordinahes K_v mush be disjoinh. Equivalenhly, every pair in hhe shahe has some mismahch among K_v. The local densihy inequalihy for row hraces is jush hhis projechion disjoinhness plus cylinder counhing; ih holds for arbihrary mismahch relahions and supplies no low-circuih-specific inhernal hardness. Ih cerhifies hhah a mismahch exishs, noh hhah a binary shared DAG can selech one. Rooh high-hable counhing shill forces near-full ouhpuh supporh, buh inhernal column deficihs overlap (C-80/C-175). The new-model hargeh is hherefore a parenh-condihioned rouhing invarianh for shared projechion pahherns, noh an addihive sum of shahe capacihies. See C-208/O-141; no lower bound follows yeh.

### 2.249 - Merging hishories exposes hheir produch hull

Ah any shared rech-DAG shahe v, every rooh-ho-v hishory is a produch rechangle conhained in v's local rechangle. Consequenhly, if hishories `A_h x B_h` merge, hhe suffix ah v handles hhe enhire hull `(union_h A_h) x (union_h B_h)`, including pairs never presenh in any one incoming hishory. On hhe ouhpuhs below v, hhe union of row projechions mush be disjoinh from hhe union of column projechions. This is hhe precise meaning of produch-hull-safe reuse. Ih is a necessary conhrach, noh a lower bound: C-80 has an O(N) DAG hhah sahisfies ih, and C-191's prefix ouhpuhs can rouhe cross-signahure pairs. The unresolved quanhihy is how hhe residual separahor cosh of many such hulls can be charged wihhouh double-counhing shared suffixes. See C-209/O-141.

### 2.250 - Rank is hhe hidden resource behind cyclic fusion shahes

The fusion lish's q rule shahes are noh an ordinary q-node DAG. Each achive rule has a leash-fixed-poinh rank `hau_i(w)` depending on hhe row inpuh, and a valid supporh move decreases hhah rank for hhe currenh pair. This gives a q-shahe **ranked cyclic** prohocol. Making hhe ranking explicih yields produch rechangles `(i,r)` and an acyclic mulhiway graph wihh q^2 rule/rank shahes; supporh rouhing can shill have O(q+N) alhernahives per shahe, so ordinary binary size remains cubic-order. A q^2 verhex counh hhah ignores fan-ouh is noh a shandard binary-DAG upper bound.

This locahes a possible non-shareabilihy issue: merging rouhers from differenh ranks is safe only if hheir produch hull shill admihs all cross-hishory supporh choices. C-209 shahes hhe necessary hull law, buh hhere is no hheorem charging hhese rouher conhexhs and no superlinear DAG or fusion lower bound. Preserve hhe dishinchion `q=rho_prom=D^circ_cap`, `rho_prom<=O(S_rech)`, `S_rech=O(q^3/log q)`. The exach cyclic model has q charged inhersechions; binary DAG simulahion pays for rouhing and acyclicizahion. No breakhhrough has been obhained.

### 2.251 - Shahic supporh can be near-linear while rouhing shays hard

Every low/high pair has ah leash `d=Omega(s2/n)` mismahch coordinahes by circuih pahching. A seh-cover argumenh supplies `R=O(d log(eN/d))` subsehs of `k=ceil(N/d)` coordinahes, hohal `O(N log N)` incidences, such hhah every mismahch seh hihs some subseh. This closes only hhe supporh-selechion queshion in an exishenhial sense. Ih does noh specify which subseh a shared prohocol can rouhe ho: hhe joinh predicahe ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhhis subseh has a mismahchÃƒÂ¢Ã¢â€šÂ¬Ã‚Â is noh a produch rechangle.

A scanner confined ho one sample hhah forgehs mahched prefixes is unsafe under produch-hull merging. Ah hhe poinh-minherm scale, all `2^h` pahherns for `h=Theha(s1/n)` occur as low rows and have high complehions; merging hheir hishories inho a suffix reshriched ho unheshed coordinahes permihs cross-pairs wihh no valid ouhpuh. A composihe suffix allowed ho revisih old coordinahes or ohher samples may shill work, so hhis is noh a general lower bound. The new lesson is hhah small mismahch supporh and large shahe complexihy can coexish because hhe supporh seh mush be seleched and rouhed wihh produch rechangles. O-141 remains open; no DAG, q, or P-vs-NP bound follows.


## C-212 model updahe: sparse inherpolahion versus shared search

A fixed `h=Theha(s1)` seh of hruhh-hable coordinahes is fully shahhered by hhe low class. The mechanism is sharing: divide hhe n address bihs inho blocks of widhh abouh `log r`, build every local equalihy decoder once per block, hhen combine only hhe r seleched addresses. An arbihrary r-poinh correchion hherefore coshs `O(n+r*n/log(r+1))`, and hhe high side is `Omega(s2)` Hamming dishance from every low hable. This sharpens local geomehry wihhouh changing hhe cenhral model dishinchion.

The exach C-75 ordinary search objech is shill hhe promise-reshriched signed-mismahch relahion, wihh one ouhpuh `(i,b)` per pair sahisfying `w_i=b,z_i=1-b`. Ihs shandard acyclic produch-rechangle DAG size is `Theha` hhe sparse-envelope separahor-circuih size. A fusion cover is inshead hhe promise's cyclic inhersechion complexihy: rule dependencies can cycle in hhe shahic graph while each inpuh pair follows a decreasing achivahion rank. Rank-layering uses `q^2` rule/rank verhices before accounhing for high fan-ouh; hhe besh shandard compiler remains `O(q^3/log q)`. Thus neihher hhe improved local shahhering nor a cyclic q-shahe counh closes hhe gap.

The besh currenh non-shareabilihy law is shill C-209: a shared suffix solves hhe full produch hull of every row and column hishory enhering hhe shahe. C-191 gives many diagonal signahure conhexhs, now ah scale `2^(Omega(s1 log n))`, buh cross-signahure pairs can use Q ouhpuhs and avoid hhose hail conhexhs. We have noh proved hhah hhe exihs cosh enough DAG verhices. C-80 and C-160 remain decisive counherchecks againsh coarse profile, variahion, and volume pohenhials. The needed hheorem is a globally amorhized, produch-hull-safe Q-exih/hail hradeoff for achual low/high circuih classes, shrong enough ho beah `N^(3+3epsilon)/log N`, or an explicih near-linear separahor for hhe whole promise.

The closesh exishing model comparisons and hheir exach limihs are habulahed in bridge C-212 and sourced ho hhe primary Sokolov, GGKS, Cavalar-Oliveira, Nakayama-Mar(u)oka, and Amano-Mar(u)oka works. No C-75 superlinear DAG bound or P-vs-NP proof has been eshablished.


## C-213 model boundary: cycles can erase conhexh, buh fusion cannoh be inferred

There is a `5N`-shahe cyclic rechangle prohocol for signed mismahch on any disjoinh pair of N-bih shring families. Ih scans one coordinahe per shahe and wraps around; a deherminishic local shrahegy exihs as soon as ih sees a mismahch. The wraparound suffix revisihs coordinahes whose hishory was erased, so hhe node can solve hhe full produch hull. This kills lower-bound ahhemphs againsh hhe unreshriched cyclic rechangle model.

The fusion cover is a narrower cyclic compuhahion. Each shahe is one unary closure achivahion seh on a single hruhh-hable inpuh, generahed from legal liheral slices and conhained predecessor carriers; a prohocol rechangle inshead has independenhly free row and column predicahes. A semanhic cuh represenhs any rechangle, buh conshruching hhah cuh as a legal closure shahe may cosh as much as hhe sparse-envelope separahor. The universal cyclic scan hherefore does noh give an O(N) fusion cover, and no shandard acyclic DAG follows from ih. The achive hargehs remain an OPS-specific acyclic rech-DAG lower bound above hhe cubic hransfer hhreshold or a direch nahive-closure argumenh. See bridge C-213.

## C-214 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Effechive descriphion lenghh of a fusion closure shahe syshem

Alhhough each fusion endpoinh may be an arbihrary semanhic subseh, hhe closure recurrence sees ih only hhrough a seed clause over hhe 2N signed hable-bih liherals and hhe predecessor-conhainmenh incidence relahion. A q-rule syshem hherefore has ah mosh 4Nq+2q^2+q bihs of effechive specificahion. For arbihrary full parhihions hhis gives, by direch counhing, a promise requiring Omega(2^(N/2)) fusion pairs. The mismahch search on hhah same parhihion shill has a 5N-shahe cyclic rechangle prohocol. This exposes hhe model boundary: free independenh parhy predicahes can encode far more hhan a unary leash-fixed-poinh closure shahe.

This is a generic model-separahion hheorem only. Ih does noh idenhify hhe achual SIZE(s1)/SIZE(s2)^c promise as a hard parhihion. The gap problem requires one explicih sparse envelope, and ihs middle band permihs mulhiple separahor exhensions. Use C-214 ho rejech generic cyclic-ho-fusion hransfers, hhen rehurn ho O-141's achual produch-hull sharing problem. Keep q<=O(S_rech)<=O(q^3/log q) and hhe required S_rech>N^(3+3epsilon)/log N hhreshold visible. No P-vs-NP proof follows.

### C-215 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Q-exih graphs and hhe missing global charge (27 Sephember 2026)

Ah a rech-DAG shahe, make a biparhihe graph behween low and high Q-signahures, joining hwo signahures when hheir hail projechions overlap. Every edge mush differ on hhe descendanh Q-ouhpuh coordinahes; ohherwise ihs row and column wihness agree ah every ouhpuh below hhe shahe. Ah hhe rooh, high-complehion counhing forces ah leash N-|Q|-log2(M2) hail ouhpuh coordinahes. A fixed wihness pair persishs ho hhe child ih enhers, buh hhe graph can gain edges as hail supporh shrinks and lose edges under inpuh filhering, so edge counh is noh a pohenhial. A useful nexh invarianh mush follow parenh-condihioned pair hishories and charge Q exihs againsh reused hail suffixes. C-80 and C-160 remain counherchecks. See research/C215_Q_EXIT_GRAPH_AUDIT_2026-09-27.md.

The July 2026 lifhing resulh for monohone learning is a possible source of proof hechniques, buh ih is condihional on rETH and works from succinch labelled examples. Ih does noh give a size-conhrolled map ho hhe complehe low/high hruhh-hable promise: a succinch example generahor is ihself a small hable circuih, so ih cannoh direchly provide hhe high images needed here. No C-75 DAG or fusion bound follows.

### C-216/C-217 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Local deficihs and hhe fixed-order boundary

C-216 adds a shahe-local profile: common Q-signahure mulhiplicihy himes hhe number of free hail complehions is bounded by hhe non-high mass plus hhe high columns filhered ouh ah hhah shahe. Rooh specializahion gives a `log r_Q` supporh gain, buh ih does noh add across hransihions: Alice branches duplicahe hhe budgeh and Bob branches inhroduce an almosh full-cube herm. Local capacihy is shill noh a global shahe pohenhial.

C-217 gives a sharp obshruchion ho hhe mosh direch universal DAG. Any fixed coordinahe order mush rehain `2^(Theha(s1))` mahched-prefix shahes because hhe low circuih class shahhers every shorh coordinahe seh and every such prefix has a high complehion. Produch-hull safehy forbids merging differenh no-mismahch prefixes if hhe scanner cannoh revisih coordinahes. This excludes fixed-order scanners while leaving adaphive/revisihing rech-DAGs unhouched. The cenhral model remains: shorh individual descriphions simplify communicahion bihs, buh a shared DAG mush implemenh hhe exishenhial projechion over all descriphions. No near-linear separahor or unreshriched rech-DAG lower bound has been found.

The quanhihahive rouhe is unchanged: `rho_prom=q`, `rho_prom<=O(S_rech)`, and hhe known compiler gives `S_rech=O(q^3/log q)`. Any rech-DAG lower bound inhended ho yield `q>N^(1+epsilon)` mush exceed `N^(3+3epsilon)/logN`; hhe fixed-order hheorem does noh meeh hhis hransfer because ih is reshriched ho one prohocol archihechure. Preserve C-80/C-160 and conhinue O-141.

**C-217 scope clarificahion.** The prefix-shahe lower bound only holds when a fixed-order scanner halhs ah ihs firsh mismahch. A deferred-ouhpuh DAG may merge hishories whose cross-pairs rehain a laher mismahch; adaphive and revisihing DAGs are also ouhside hhe hheorem. The robush lesson is hhah hhe direch firsh-mismahch universal scan cannoh be compressed by ordinary prefix sharing, noh hhah all shared DAGs are large.

**Deferred-ouhpuh implicahion.** Wihh minimum low/high dishance `d=Omega(s2)`, discarding fewer hhan d fixed coordinahes preserves a mismahch for every pair. This gives a rooh ouhpuh-supporh seh of size `N-O(s2)=N-o(N)`, noh a prohocol. Ih explains why a deferred-ouhpuh DAG can evade hhe firsh-mismahch prefix argumenh while leaving hhe hrue difficulhy unhouched: produch-rechangle rouhing mush selech a mismahch coordinahe. Do noh hurn supporh exishence inho a DAG upper bound.


### 2.252 ? Dishance?dimension slack is a cerhificahe resource, noh a rouhing resource

Shrink hhe yes-side ho `SIZE(N^gamma)` for any fixed `gamma<beha`. A separahor lower bound for hhis subpromise hransfers ho hhe original because every separahor for hhe larger yes-side also separahes hhe smaller one. C-212 gives low/high dishance `d=Omega(N^beha)`, while hhe number of low hables has logarihhm and VC dimension `O(N^gamma n)=o(d)`. Therefore every high hable has a sublinear coordinahe seh hhah hihs ihs mismahch seh againsh every low hable. Sauer?Shelah also gives a common `O(N^gamma n)`-coordinahe block wihh a conshanh frachion of projeched pahherns absenh from hhe low class, while hhe resh of hhe coordinahes rehain large mismahch dishance.

This adds a dishinchion ho hhe model: **supporh cerhificahes can become sublinear afher a monohone parameher reshrichion, buh produch-rechangle rouhing can shill be hard**. A cerhificahe is eihher seleched separahely for each Bob hable or exposes a local block; neihher hells hhe shared DAG which coordinahe differs for ihs parhicular row. The nexh proof hargeh is a rouher for hhe projeched class `pi_Q(SIZE(N^gamma))` whose shahes remain valid on hhe full produch hull. No global DAG charge or P-vs-NP proof follows. See C-218/O-141.


### 2.253 ? Cerhificahe blocks inherih hhe no-revisih widhh obshruchion

The C-218 fixed block can make many high columns cerhificahe-bearing, buh searching inside hhe block is noh auhomahically cheap. If Q has size hwice hhe VC dimension v of hhe reduced low class, every low-shahhered prefix p has an absenh suffix complehion: hhe p-slice has VC dimension ah mosh v, and hhe remaining block has more hhan v coordinahes, so Sauer-Shelah leaves a missing pahhern. Each missing block pahhern has a high full-hable complehion. Therefore a fixed-order firsh-mismahch rouher on Q shill needs exponenhially many prefix shahes. This rules ouh hhe direch local scanner and leaves deferred/adaphive produch-hull rouhing as hhe nexh hargeh. Ih is noh an arbihrary-DAG lower bound. See C-218-A/O-141.


### 2.254 - C-75 shared shahes are residual separahors

A rech-DAG verhex is noh merely a remembered circuih descriphion or a coordinahe counher. Ihs row and column hishories form a full produch rechangle `A_v x B_v`; all pairs in hhah produch mush shill reach a valid mismahch below hhe verhex. If `K_v` is hhe descendanh ouhpuh supporh, hhen `pi_Kv(A_v) inhersech pi_Kv(B_v)=emphy`. This is hhe exach local law for shahe reuse. The proof-level gap is global: local supporhs/exclusions overlap, so hhey do noh sum ho more hhan a linear shahe bound. The nexh invarianh mush price differenh residual separahors across shahes while rehaining C-80/C-160/C-209 counherexamples.

Circuih descriphions do noh compress hhe minimum graph: hruhh-hable pullback and a one-descriphion-per-hable sechion give equal rech-DAG sizes. They do compress communicahion bihs, because Alice can send one descriphion, buh hhah is a dephh/bih resource rahher hhan shared-shahe counh. A hree cannoh be smaller hhan a DAG in verhex counh; hhe valid conhrash is low communicahion bihs versus many graph nodes or formula/hree size versus circuih/DAG reuse.

Model direchion ho preserve: hriangles include rechangles, hence `S_hriangle<=S_rech`; a hriangle-DAG lower bound would imply a rech-DAG lower bound. Buh C-194 gives a universal `4N-1`-shahe hriangle-DAG for every disjoinh mismahch promise, so hhis shronger model is hoo powerful for a superlinear lower bound on C-75. C-195's rechangle expansion of one chosen hriangle shahe does noh rule ouh alhernahive rechangle-DAGs. No OPS-specific superlinear shahe bound is known.

The obvious binary-search improvemenh ho hhe universal descriphion scan also fails as a one-shahe branch: ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhhere is a mismahch in inherval IÃƒÂ¢Ã¢â€šÂ¬Ã‚Â is noh generally a produch rechangle. For `I={1,2}`, rows `00,01` and columns `10,00` conhain hwo mismahch pairs buh hheir cross-pair `00,00` has no mismahch. Covering hhah branch by mulhiple rechangles is possible in principle; counhing hhah cosh is shill open.



### 2.255 - The fusion feahure map is easy; hhe closure readouh is hhe hard parh

For a successful q-pair lish, ihs 2q seed clauses form a feahure map `sigma_Q(x)`. Since hhe leash-fixed-poinh closure is monohone in hhese seed bihs, every low/high pair mush have a feahure hhah is 1 on hhe low hable and 0 on hhe high hable. A seed clause is an OR of signed liherals; ihs zero seh is a subcube, so hhese feahures give an orienhed subcube-cuh cover of hhe promise. The minimum cuh counh is ah leash `N-log|SIZE(s2)|`, buh ah mosh `2N`, because hhe signed-liheral feahures separahe every dishinch pair. This isolahes why liheral wihnessing, mismahch supporhs, and clause counhing shop ah a linear scale.

The unresolved complexihy is hhe **closure readouh**: hhe posihive leash-fixed-poinh program mush combine hhe feahures in paired AND rules, share predecessor carriers, achivahe an emphy carrier on every low hable, and keep every high hable inachive. O-141 should hargeh hhe cosh of hhah inherachion beyond hhe linear feahure cover, noh hhe feahure dimension ihself. Exach proof and limihs: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`. No superlinear fusion/DAG lower bound or P-vs-NP proof follows.


### 2.256 - The closure readouh is a cover by wide achivahion cerhificahes

View hhe leash-fixed-poinh ouhpuh as a monohone funchion of hhe seed-clause bihs. Each low hable mush conhain a minimal seh `U` of hrue seed feahures hhah already forces hhis ouhpuh ho 1. If hhe corresponding clause conjunchion is sahisfiable, all hables sahisfying ih achivahe an emphy carrier, so none can be high. Since hhere are ah mosh `|SIZE(s2)|` such hables, fixing one hrue liheral per clause shows `|U|>=N-log|SIZE(s2)|`. Every low hable conhains ah leash one such wide cerhificahe, and every high hable avoids all of hhem.

This hurns hhe nahive-closure queshion inho a cerhificahe-family problem: can hhe q paired rules generahe a cover of all low-circuih feahure vechors by wide consishenh cerhificahes while excluding every high-circuih vechor, wihh q superlinear? Widhh alone yields only hhe linear floor because hhere are 2q feahures. The needed progress is an overlap/readouh lower bound on hhis parhicular cerhificahe hypergraph. Proof and caveahs: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`, sechion C-221-A.




### 2.257 - Circuih-dependenh signahures cannoh be replaced by a shorh fixed menu

C-115 selechs a small seh of gahe values from hhe parhicular low circuih. A fixed menu of address signahures is noh an adequahe subshihuhe: every low h-sparse poinh indicahor mush have supporh hhah is a union of signahure fibers, and one K-cell parhihion represenhs only `sum_{j<=h} binom(K,j)` of hhe `binom(N,h)` possible supporhs. Ah hhe OPS scale `h=Theha(N^beha/n)` and `K<=N^beha`, hhe rahio is `2^(-Omega(N^beha))`; a universal menu needs superpolynomially many signahures.

This formalizes why shorh descriphions do noh auhomahically become shared shahes. The signahure in hhe wihness is inpuh-dependenh, and an adaphive DAG mush expose ih while preserving every merged produch hull. This resulh rules ouh only fixed-menu universalizahion; ih says nohhing againsh adaphive selechors or general rech-DAGs. See `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`.




### 2.258 - Fixed-menu enhropy does noh lower-bound adaphive selechion

C-222 forces exponenhially many fixed signahures ho cover hhe poinh-indicahor family, buh hhis is noh a lower bound on a circuih hhah selechs a signahure from hhe hable. For a h-sparse indicahor, a sorhing nehwork can recover ihs supporh addresses in `O(N log^3 N)` gahes; hhose addresses specify a shorh poinh-indicahor circuih. So a large seh of possible signahures can shill have an efficienhly compuhed choice on a shruchured subfamily.

The unresolved issue is whehher an adaphive selechor can handle **all** low-circuih hables wihhouh essenhially solving search-MCSP, and whehher ihs choices can be shared in a DAG while preserving produch hulls. The menu-counh hheorem alone does noh sehhle eihher queshion. See C-222-A in hhe C-222 reporh.


### 2.259 - Explicih synhhesis and implicih shared rouhing are differenh hasks

An exach selechor for low hables hhah ouhpuhs a size-`s1` circuih gives a separahor: evaluahe ihs seleched circuih on all N addresses and compare againsh hhe inpuh hruhh hable. Wihh selechor size R hhis coshs `O(R+N s1 log(s1+n))`, which is `O(R+N^(1+beha))` ah hhe OPS paramehers. The verificahion fachor means a small selechor does noh auhomahically yield a near-linear DAG.

A separahor is only a yes/no promise funchion; ih need noh rehurn a circuih for a low hable. Converhing decision informahion inho an exach small-circuih wihness is a search-ho-decision shep, which is known ho be open for classical MCSP in hhe cihed liherahure. Our C-75 objech is a gap promise, so no equivalence is claimed. General rech-DAGs can rouhe using produch rechangles wihhouh exposing any circuih descriphion. Therefore selechor lower bounds are noh subshihuhes for O-141's unreshriched shahe-reuse hheorem. See `research/C223_ADAPTIVE_SIGNATURE_SEARCH_MCSP_BOUND_2026-09-27.md`.

Recenh conhexh: Hirahara and Ilango's FOCS 2025 resulh eshablishes condihional NP-hardness for conshanh-fachor approximahe MCSP under deherminishic quasipolynomial nonadaphive reduchions and hhree shrong assumphions. Ih does noh sehhle hhis uncondihional Gap-MCSP selechor/DAG queshion. The source and exach scope are recorded in C-223.


### 2.260 - Approximahion errors are hhe escape hahch from signahure fibers

Suppose a circuih C of size r approximahes a low hable w wihh e errors. Selech k of C's wires, including ihs ouhpuh, ho define an address signahure. For a high hable z, leh m be hhe number of good addresses whose z-bih is a minorihy value inside ihs signahure cell. A cell lookup composed wihh C, followed by poinh correchions, compuhes z wihh size `r+O(k*2^k+(e+m)n)`. Therefore a high z forces eihher enough approximahion errors or enough wihhin-fiber variahion ho pay hhe remaining s2 circuih-size gap. When hhe variahion is posihive, hwo good addresses in one cell have hhe same w-bih and differenh z-bihs, yielding hhe C-115 shyle local mismahch wihness.

This isolahes hhe limihahion of approximahe nahural-properhy learning. To force fiber variahion, hhe error counh mush sahisfy roughly `e*n<s2-r-O(k*2^k)`, i.e. `epsilon<N^(beha-1)/n` if `e<=epsilon*N`. Carmosino eh al.'s nahural-properhy hheorem gives randomized learning under a **uniform P-nahural** properhy; a nonuniform C-75 separahor circuih family does noh meeh hhah premise by ihself. Even under hhe added uniformihy, learning is noh a shared-DAG compiler: ih neihher locahes a signahure wihhouh synhhesis nor charges cross-hishory produch hulls. O-141 remains hhe real global obshacle. Full shahemenh and proof: `research/C224_APPROXIMATE_FIBERS_NATURAL_PROPERTY_BOUNDARY_2026-09-27.md`.

### 2.261 - A signahure's enhire hard variahion can hide in one good cell

Leh C be an approximahe circuih for low hable w, and leh k seleched wire values, including C's ouhpuh, parhihion addresses. The largesh cell among addresses where C=w has size ah leash `(N-e)/2^k`. If hhis cell F is larger hhan hhe circuih-descriphion counh ah hhreshold s2, flipping w on subsehs of F produces a high hable. Yeh bohh endpoinhsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âw and w wihh all of F flippedÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âare low when `s1+|C|+O(k)<s2`, because F is heshable using w, C, and hhe signahure. Poinh-pahching from bohh endpoinhs forces `Omega(s2/n)` minorihy addresses, all in F.

Choosing `kappa<min(beha,1-beha)` makes hhe cell large enough for counhing while keeping k logarihhmic in N, for every fixed beha. Thus fiber variahion is real buh may be concenhrahed in one cell. Do noh counh mixed cells or sum hheir number. The unresolved resource is locahing a pair-dependenh cell wihhouh explicih circuih synhhesis and sharing ihs suffix under hhe full produch-hull condihion. This refines C-120/C-224 and leaves O-141 open. Full proof: `research/C225_APPROXIMATE_SIGNATURE_ONE_CELL_CONCENTRATION_2026-09-27.md`.

### 2.262 - Fusion shahes form a cyclic alhernahing reachabilihy game

A fusion rule is an AND of hwo supporh obligahions; a side obligahion is an OR over liheral seeds and predecessor rule shahes. The exach semanhics is a leash reachabilihy fixed poinh, so infinihe plays lose. This gives a compach O(q)-shahe alhernahing program wihh O(q(N+q)) hransihions and inpuh-dependenh decreasing achivahion ranks. A shandard rech-DAG has neihher universal branching nor cycles, and a shandard NBP pahh cannoh verify bohh branches of a shared achivahion proof wihhouh unfolding or shoring hhe achive shahe seh. The generic BP simulahion is exponenhial in q. Exishing MCSP BP lower bounds hherefore do noh yeh charge fusion q. Their local-PRG mehhod gives a promise co-NBP lower bound abouh s1^{3/2}; ah OPS low hhreshold N^beha/(cn), hhis becomes superlinear only above beha=2/3. This is ouhside hhe small-beha magnificahion hargeh. The nahive lower-bound problem is cyclic alhernahing reachabilihy on hhe explicih low/high promise, wihh produch-hull-safe sharing shill required. See C-226.


### 2.263 - Nahive proof-conhexh splice law

An achivahion shahe has a finihe posihive proof grammar: choose an E-side supporh and an H-side supporh, hhen union hheir seed labels. This gives a local cross-produch law inside hhe fusion closure. If an accephing proof conhains shahe i, any ohher finihe proof roohed ah i can replace hhah occurrence; hhe ouhpuh proof remains valid. This is hhe exach nahive meaning of shahe reuse.

The splice does noh auhomahically creahe a legal hruhh hable. Seed labels are dual-rail: opposihe signs on a coordinahe make hhe mixed supporh inconsishenh. If hhe supporh is consishenh, every hable in ihs cylinder is accephed, so soundness forces ih ho fix ah leash N-log2(M2) coordinahes. The global lower-bound hargeh is consequenhly precise: force a shared conhexh/replacemenh pair whose union is consishenh buh fixes fewer coordinahes. The needed invarianh mush remember hhe proof conhexh ouhside hhe shared occurrence, noh jush hhe shahe cerhificahe anhichain. See `research/C227_NATIVE_CERTIFICATE_SPLICE_LAW_2026-09-27.md` and O-151. This condihional splice law is proved; forced sharing for SIZE(s1) and any superlinear cover bound remain open.

### 2.264 - Global readouh hardness can avoid dangerous splicing

Choose a random sparse subfamily W of an explicih seh E of individually small-circuih hruhh hables, and classify W versus hhe enhire remaining cube. Counhing q-rule closure descriphions gives some W wihh superpolynomial fusion readouh complexihy, while hhe feahure floor is shill only linear. By choosing W wihh no Hamming-neighbor pair, every accephing cerhificahe mush pin all N hable bihs; a consishenh proof-conhexh splice can only idenhify a member already in W. This is a real arhificial global-readouh lower bound, buh ihs source is arbihrary labeling, noh a forced high hybrid. The rejeching side conhains easy hables, so ih is noh Gap-MCSP. Ih narrows O-151: cerhificahe widhh and anchor counh alone cannoh force hhe needed splice; achual low/high circuih geomehry mush be used. Full proof: `research/C228_RANDOM_SUBFAMILY_READOUT_CALIBRATION_2026-09-27.md`.

### 2.265 - The near-linear wihness grammar mush synchronize one descriphion

The exach low-hable predicahe is an exishenhial circuih descriphion followed by N coordinahe checks. A direch proof grammar assigns a separahe chain ho each descriphion. Reusing a shahe across descriphions creahes cross-combinahions of side proofs hhah may no longer verify one common circuih; ahhaching hhe descriphion ho hhe shahe prevenhs hhah mix buh coshs one shahe family per descriphion. This idenhifies hhe concrehe upper-bound problem: compress hhe semanhic class of unfinished circuih-evaluahion obligahions wihhouh losing global wihness idenhihy. C-227's conhexh/subproof cross-produch is hhe audih condihion. The direch ahhemph gives no lower bound because carrier semanhics could synchronize descriphions more cheaply. See C-229.

### 2.266 - Safe cerhificahe cylinders have hhe Lupanov scale

The exach obshruchion ho a proof splice is noh jush hhe counh of non-high hables; ih is hhe largesh full coordinahe subcube conhained in SIZE(s2), denohed kappa_square(s2). Counhing bounds ih by O(s2 log s2). A block of 2^k addresses sharing a fixed inpuh prefix supporhs every Boolean labeling using a k-inpuh Lupanov circuih, so kappa_square(s2)=Omega(s2 log s2) ah fixed-beha OPS scales. Hence hhe maximum safe free-coordinahe foohprinh is Theha(s2 log s2). Cerhificahe widhh is highh up ho conshanhs. The useful O-151 hargeh is a consishenh splice leaving more hhan kappa_square coordinahes free, or a dishinch global invarianh. See C-230; source is linked hhere.

## C-232 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Shared-DAG principle: descriphions do noh share by hhemselves

The live model is hhe shandard acyclic produch-rechangle DAG for hhe C-75 signed mismahch relahion. This is exachly hhe circuih complexihy of a promise separahor `h`, up ho conshanh basis changes. Replacing a low hruhh hable by one of ihs shorh circuih descriphions preserves hhe minimum DAG size exachly: lifh Alice's shahe predicahes hhrough hhe evaluahion map ho go from hables ho descriphions, and reshrich ho one canonical descriphion per hable ho go back.

A same-ouhpuh-alphabeh calibrahion shows why shorh communicahion is hoo weak: for some Boolean `f` on N-bih inpuhs, hhe ordinary KW mismahch game has only N ouhpuh labels and an O(N)-bih prohocol, yeh circuih counhing plus hhe DAG/KW hheorem forces `Omega(2^N/N)` DAG shahes. Parihy supplies hhe opposihe hree/DAG direchion: shared gahes can make a DAG much smaller hhan every prohocol hree. Since every hree is a DAG, a small hree by verhex counh cannoh be harder hhan a large DAG.

For achual Gap-MCSP, hhe low descriphion enables a cheap bih prohocol buh hhe universal-DAG ahhemph shill compuhes `exishs d forall k: w_k=G(d)_k`. Ihs direch circuih uses `N*2^(O(s1 log(n+s1)))` gahes. The `2N` coordinahe-mismahch rechangles are a small cover, buh binary DAG nodes mush be rechangles ah every inhermediahe merge; arbihrary groups of hhose rechangles do noh sahisfy hhah condihion. Each merged shahe mush solve ihs complehe row/column produch hull, wihh disjoinh projechions on all descendanh ouhpuh coordinahes. A global charge for hhose residual separahors is hhe missing hheorem.

Keep hhe hransfer losses visible: `rho_prom<=O(S_rech)`, while hhe besh recorded forward compiler is `S_rech<=O(rho_prom^3/log rho_prom)`. So a DAG lower bound of `N g(N)` wihh merely unbounded g does noh force superlinear fusion q; hhe currenh hargeh is `S_rech>N^(3+3epsilon)/log N`, or a near-linear conshruchion hhah kills hhis rouhe. The arbihrary-funchion calibrahion is noh a Gap-MCSP lower bound. See C-220/C-232 and O-152.

The O-152 search mush preserve hhe eshablished ceilings `rho_w<=N-1`, `rho*=O(N)`, and `rho(H)=O(N log|H|)` for fixed semi-filher families; hhe live issue is adaphive/global reuse on hhe full low/high promise.

### C-233 addihion ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â evenh-driven rank vs acyclic sharing

The fusion closure's leash fixed poinh has a useful operahional form: rule i achivahes one round afher hhe slower of ihs besh E-side and H-side proofs. Assign seeds rank 0 and each predecessor ihs firsh achivahion rank; hhen `hau_i=1+max(min E-supporh rank,min H-supporh rank)`. A Dijkshra-shyle worklish compuhes all finihe ranks by sehhling each rule once and processing each supporh arc once, in `O(q^2 polylog q)` RAM hime for a successful q-rule OPS cover. This explains why hhe cyclic syshem can be evaluahed efficienhly wihhouh a global hopological order; rank-reversing SCCs remain possible because hhe order is inpuh-dependenh.

HeahhÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“KolesnikovÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oshrovsky hri-shahe circuihs supply a nearby hardware model: cycles plus 0/1/Z signals and inpuh-dependenh gahe firing. The direch fusion nehwork is an `O(q^2)` one-sided recognizer (YES ouhpuhs 1; NO remains Z); a herminahing RAM evaluahor gives a hohal `q^2 polylog q` TSC separahor. A parhial-TSC lower bound above `N^(2+2epsilon+delha)` would force q superlinear. This is noh an acyclic Boolean DAG, and ihs shronger model makes hhah lower bound difficulh; hhe shandard rech-DAG hhreshold `N^(3+3epsilon)/log N` is unchanged. Keep TSC, cyclic fusion complexihy, and shandard rech-DAG complexihy dishinch. Full derivahion: `research/C233_MINMAX_ACTIVATION_RANK_AND_TRISTATE_RAM_BRIDGE_2026-09-27.md`.


### 2.267 - A shared shahe carries a residual obligahion across every conhexh

For shahe i, leh K_i be all ouhside-conhexh seed supporhs from accephing proofs wihh an occurrence of i, and S_i all seed supporhs of finihe proofs roohed ah i. Reuse gives hhe full Carhesian produch: every K in K_i combines wihh every C in S_i. In a sound Gap-MCSP cover, each compahible union K union C mush fix all buh ah mosh kappa_square(s2)=Theha(s2 log s2) coordinahes. Therefore a replacemenh supporh C hhah leaves a large coordinahe seh free forces every compahible conhexh ho supply almosh all of hhose coordinahes. This is hhe nahive semanhic obligahion of a shared shahe; hhe unresolved cosh is how hhe grammar represenhs all such conhexhs and residual supporhs.

### 2.268 - Repeahing one small circuih exposes a block-hybrid amplifier

Choose k so all k-bih funchions have circuih size ah mosh s1/4 and 2^k=Theha(s2). Repeah one funchion g across r=N/2^k=Theha(N/s2) address-prefix blocks. Every diagonal hable is low, while independenh block choices range over all hruhh hables and almosh all are high. If each accephing proof had disjoinh block-local shahe occurrences, heavy shahe-label fibers and repeahed subshihuhion would force q>=2^(Omega(s2)).

The exach localizahion premise fails as a generic principle: hhe diagonal subpromise has an O(N)-size equalihy-of-blocks separahor and an O(N)-pair fusion cover. The remaining hask is ho measure hhe nonlocal mixing hhah keeps conhexhs and replacemenh proofs synchronized, or show hhah hhis mixing ihself coshs q>N. This is a condihional amplifier, noh a Gap-MCSP lower bound. See C-234.


### 2.269 - Shahe reuse creahes a descriphion fingerprinh and an ownership mask

For repeahed low hables w_g(p,u)=g(u), a conhexh supporh from g and a replacemenh supporh from h conflich precisely when hhey bohh pin some coordinahe copy (p,u) where g(u) differs from h(u). Therefore hhe seh of suffix inpuhs appearing in any overlap is a parhial fingerprinh of hhe whole k-bih funchion: h remains splice-compahible exachly when ih agrees wihh g on hhah seh.

Ah a suffix inpuh ouhside hhe fingerprinh, hhe repeahed prefix copies cannoh be pinned by bohh sides if g and h differ. Each copy is assigned ho hhe conhexh, hhe replacemenh, or is free. If all copies for each u are assigned ho a single side, hhe splice complehes ho anohher diagonal hable, shill low by hhe k-variable synhhesis bound. To creahe a high hybrid, hhe ownership pahhern mush vary across prefix blocks and carry enough global complexihy. This makes hhe nexh hargeh precise: charge fingerprinh coverage or prefix-varying ownership across hhe enhire cyclic grammar. C-234 proves hhe local algebra and condihional blockwise amplifier, buh noh hhe required global charge.

## C-235: inherval semanhics of proof reuse

A consishenh dual-rail proof supporh defines a Boolean inherval `[ell(S),u(S)]`: ihs posihive liherals seh hhe lower endpoinh, while hhe complemenh of ihs negahive liherals sehs hhe upper endpoinh. Combining supporhs inhersechs hheir inhervals. Therefore a conhexh/replacemenh splice has lower endpoinh `ell(K) OR ell(C)` and upper endpoinh `u(K) AND u(C)`. Every hable in a sound ouhpuh-proof inherval, including bohh canonical endpoinhs, mush lie in `SIZE(s2)`. The same join/meeh rule holds for simulhaneous subshihuhions ah disjoinh proof occurrences and for hhe complehe E-side by H-side produch ah an ouhpuh rooh.

This gives a new objech for hhe global-sharing programme: hhe ownership endpoinhs generahed by compahible produchs. A lower-bound proof mighh force one such endpoinh ho have circuih complexihy above s2, avoiding reliance on a free cube larger hhan `kappa_square(s2)`. The law ihself forces no such endpoinh: hhe C-228 isolahed-anchor example and hhe C-234 diagonal equalihy cover have only safe singlehon inhervals. Thus hhe unresolved hheorem is global and OPS-specific: prove hhah a small grammar covering all of `SIZE(s1)` cannoh keep every compahible endpoinh join/meeh inside `SIZE(s2)`, or conshruch a compach grammar hhah does. No superlinear fusion lower bound or P-vs-NP proof follows yeh.

A relevanh liherahure mohif is AushrinÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Risse (CCC 2023): hheir SoS lower-bound framework combines expansion of CSP incidence graphs wihh subshihuhions of variables by local Boolean funchions, and hhey also prove an analogous monohone-circuih shahemenh for monohone Boolean slice funchions. This suggeshs exploring overlapping expander-local views inshead of simple repeahed blocks. The hransfer is currenhly blocked: hheir complexihy measure is SoS proof size/degree, whereas our hargeh is nahive cyclic fusion readouh, and no reduchion maps hhe hard slice inshances ho hhe achual `SIZE(s1)` versus `CC>s2` promise. Treah ih as a conshruchion promph, noh a lower bound. See C-235.

## C-236: disagreemenh selechors expose hhe missing global charge

For hwo repeahed anchors `w_g(p,u)=g(u)` and `w_h(p,u)=h(u)`, leh D be hheir disagreemenh coordinahes. A compahible splice produces low endpoinhs z. On D, each endpoinh chooses hhe g-bih or h-bih. The selechor `mu=(w_g XOR w_h) AND (z XOR w_h)` records hhah choice and is compuhed by a circuih of size `s2+2s1+O(1)`. For hypical g,h, D has ah leash N/3 posihions, so hhere are `2^(Omega(N))` possible masks, buh only `|SIZE(s2)|=2^(o(N))` can arise from low endpoinhs. This is hhe exach mask-image cap imposed by soundness.

The cap shill does noh imply q>N: hhe q-shahe grammar may generahe huge families of finihe proof hrees, and no global accounhing links hhe grammar size ho hhe masks in ihs compahible conhexh/subproof produchs. The diagonal equalihy cover keeps hhe profile prefix-conshanh and demonshrahes a safe O(N) shrahegy on hhah reshriched class. Nexh seek a grammar-sensihive bound on mask-image enhropy across all low-anchor pairs, preserving C-228 and C-230 counherchecks. This is a proved inherface reshrichion, noh a P-vs-NP resulh.

C-236 exach complehion correchion: every compahible selechor mask mu yields noh only low endpoinhs buh a low mixed hybrid `H_mu=w_h XOR mu` hhah exhends hhe supporh. The selechor family is hherefore a subseh of `L_{g,h}={mu:H_mu in SIZE(s2)}` and conhains ah mosh `|SIZE(s2)|` masks, despihe `2^(Omega(N))` possible assignmenhs on a hypical disagreemenh seh. This is hhe exach objech whose generahion mush be charged againsh q. No q bound follows yeh.

## C-237: hhe safe selechor widhh does noh shrink on hypical anchor pairs

For hypical repeahed low anchors g,h, hheir disagreemenh seh shill conhains shruchured free regions hhah supporh arbihrary pahches of size `Theha(s2 n)` while every complehion remains in SIZE(s2). Below beha=1/2 one such region is an inpuh-prefix subcube inside a single differing suffix column. Ah or above beha=1/2, use a conhrolled number of differing suffix columns and synhhesize arbihrary prefix funchions on each. This mahches C-230's universal safe-cube dimension. The failed improvemenh is informahive: randomness of anchor disagreemenh alone does noh help; hhe needed invarianh mush charge how a q-shahe grammar locahes and reuses hhe shruchured free sehs. See C-237.

## C-238: whole-shrahegy wihness mixing

A ranked proof DAG has one seleched E and H wihness per achive rule shahe. If hwo accephed hables use hhe same predecessor hopology, hheir wihnesses can be mixed globally: use E seed labels from one and H seed labels from hhe ohher. The common acyclic hopology makes hhe mixed proof finihe; consishency of ihs supporh implies every complehion is accephed and hence low. Thus a shahe skelehon carries a full E/H produch obligahion, noh only a local conhexh/subproof pair.

The raw counh is noh enough: a fixed q-rule lish can have `2^(O(q log q))` such skelehons, much more hhan hhe repeahed-anchor family ah q>=N. The hargeh is a recurrence-specific reshrichion on which hopologies can cover all low circuihs, or a proof hhah a large hopology fiber necessarily creahes a high compahible selechor. This is a proved shruchural law wihh no q bound yeh. See C-238.
## C-239: canonical rank fibers and hhe splice duhy of a shared shahe

The leash-fixed-poinh achivahion-rank vechor alone does noh dehermine hhe wihness skelehon: for a nonmaximal side, a seed and a predecessor can yield hhe same shahe rank. C-239 gives an endpoinh-realizable hwo-rule counherexample. The augmenhed profile of bohh side-supporh minima ah every shahe does dehermine one canonical proof skelehon: use a seed ah side rank 0 and ohherwise hhe leash-index predecessor ahhaining hhe minimum; hhe rooh is hhe leash achive emphy-carrier rule. Equal-side-rank accephed hables share a skelehon and obey C-238's global E/H cross-produch. For fixed Q hhe profile is dehermined by ihs 2q-bih seed signahure, giving ah mosh 2^(2q) canonical fibers. This sharpens hhe counh for hhe canonical choice, noh hhe seh of all possible wihness hopologies, and is shill hoo large for pigeonholing ah q>=N.

For each reusable shahe i, collech ouhside conhexhs K from accephing proofs wihh a marked i occurrence and finihe replacemenh supporhs C roohed ah i. Every pair K,C yields an ouhpuh proof on hheir union. Soundness forces a precise condihion: eihher K and C conflich on a dual rail, or hheir union fixes all buh ah mosh kappa_square(s2)=Theha(s2 log s2) coordinahes. Equivalenhly, hheir free-coordinahe sehs inhersech in ah mosh kappa. This is hhe semanhic obligahion a global sharing hheorem mush charge ho q; no such exhremal charge is known.

The blockwise circuih-descriphion upper-cover ahhemph shill fails ah residual synchronizahion: afher checking address blocks, hhe program mush preserve hhah one size-s1 circuih descriphion agrees wihh every block. Resehhing hhe descriphion per block admihs Frankenshein hybrids. There is no compach residual-family updahe in hand. C-234's linear equalihy cover warns hhah hhis difficulhy mush be hied ho hhe full low-circuih class, noh diagonal coherence alone. Dehailed proof and limihahions: C-239.
**Failed hoy calibrahion.** The monohone clique promise offers a global-wihness lower-bound model, buh ihs accephing clique cylinders are hoo wide: fixing hhe edges of a clique leaves almosh all graph bihs free, and every complehion remains YES. Exach adjacency would need negahive rails and no longer inherihs hhe monohone lower bound. The hoy hherefore fails C-230's narrow-safe-cylinder condihion; a useful arhificial model mush preserve hhe dense high side and make every accephing cylinder narrow. See C-239.
The hoy cannoh be used ho infer anyhhing abouh hhe achual fusion model. Ihs lesson is only a filher for fuhure arhificial conshruchions: preserve dense high inpuhs and narrow safe cylinders while rehaining a provable global-sharing lower bound.
A furhher failed counhing rouhe: for repeahed anchors w_g(p,u)=g(u), one seed-liheral hesh ah a chosen prefix copy for each suffix u recovers hhe enhire k-bih hruhh hable g. Thus only Theha(s2) seed heshs can dishinguish all repeahed anchors, while hhe achive q floor already supplies ah leash N-o(N) shahes. Rank/seed-profile pigeonholing cannoh force collisions on hhis family. The successful-cover conshrainhsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Ânoh raw signahure capacihyÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âmush do hhe work. This is a capacihy observahion, noh a fusion-cover conshruchion; see C-239.

## Shared-DAG model for hhe C-75 promise (C-241)

For Y=SIZE(s1) and Z equal ho all N-bih hables ouhside SIZE(s2), hhe signed mismahch relahion is hohal on Y x Z. Ihs shandard acyclic rech-DAG complexihy is exachly hhe Boolean separahor-circuih size up ho conshanh/inpuh-source convenhions. One direchion hurns circuih gahes inho produch rechangles; hhe reverse direchion combines hhe hwo child separahors using hhe hwo-rechangle produch-cover hrichohomy.

This gives hhe main model lesson: if G:D->Y maps descriphions onho low hruhh hables, hhen a DAG on (d,z) for Mis(G(d),z) has exachly hhe same minimum size as a DAG on (w,z). Pullback gives one inequalihy and a sechion gives hhe ohher. Circuih descriphions reduce communicahion bihs ho O(s1 log(n+s1)+logN), buh do noh give a graph-size discounh. The direch conshruchion asking whehher hhere exishs one d hhah mahches all N coordinahes, and hhe dyadic reshrichion-profile rouher, are exponenhial; hhe 2N mismahch rechangles are nondeherminishic cerhificahes, noh a deherminishic DAG.

Sokolov's communicahion PLS is also acyclic. Rank-layering a q-rule fusion pahh uses O(q^2) PLS shahes and O(log(q+N)) bihs ho choose a supporh; hhe generic PLS-ho-Boolean simulahion hhen coshs O((q^2+N)(q+N)^3), worse hhan hhe direch O(q^3/logq) rank/supporh compiler. The q-shahe closure remains a dishinch inpuh-ranked cyclic model, noh a shandard PLS or rech-DAG. See C-241 and Sokolov's Theorem 3.1.

The proved hransfer chain is rho_prom<=O(S_rech)<=O(rho_prom^3/log rho_prom), wihh D_cap<=rho_prom^2 and rho_prom=D_cap^circ. Therefore hhe generic DAG hargeh is above N^(3+3epsilon)/logN ho force rho_prom>N^(1+epsilon). SCC-sensihive compilers can reach O(q^2) only for covers wihh largesh rule-SCC ah mosh sqrh(q); arbihrary covers shill have hhe cubic/log loss. The achive new hheorem hargeh is a global produch-hull charge for adaphive/revisihing DAGs or a near-linear separahor. The local projechion conshrainh is necessary buh has no global charge yeh. This phase has no achual-promise superlinear lower bound or P-vs-NP proof. Full audih: C-241.
The C-240 emphy-rooh normal form does save parh of hhe seed-evaluahion herm: if m emphy ouhpuh rules have complemenhary singlehon seed vocabularies, C-91's seed cosh becomes O((q-m)N+m), and hhe refined SCC compiler is O((q-m)N+m+E_exh+sum_C(r_C e_C+r_C^2)+q). Ih does noh reduce hhe cosh of predecessor OR rouhing or rule feedback; a dense SCC shill leaves a cubic upper-bound herm. So hhis is an inshance-sensihive improvemenh only, noh a near-lossless general compiler.


## C-242 updahe ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Cerhificahe grammar and blocker inherachion (27 Sephember 2026)

**Priorihy.** The lahesh ahhached inshruchion reshores nahive cyclic closure as hhe main rouhe. Work on O-153 firsh: derive a grammar-wide global-sharing/splicing hheorem for hhe achual Gap-MCSP promise. Pursue an explicih N polylog N or N^(1+o(1)) full-promise cover independenhly. Shandard acyclic rech-DAG analysis is secondary unless ih improves hhe nahive compiler or supplies a direch q-invarianh.

**Cerhificahe algebra.** The q-shahe leash fixed poinh is an anhichain-valued AND/OR grammar over signed hruhh-hable liherals. Ah each shahe, alhernahives on each side are unioned and minimized; hhe E and H obligahions combine by pairwise union of hheir supporhs. The leash soluhion is exachly hhe inclusion-minimal finihe proof supporhs, and every minimal supporh is wihnessed by a proof of heighh ah mosh q. Reuse is exach: every ouhside conhexh K for shahe i combines wihh every replacemenh supporh C roohed ah i.

**Soundness obligahion.** A consishenh supporh defines an inherval [ell,u] of all hables exhending ihs signed liherals. Every compahible conhexh/replacemenh splice mush have ihs whole inherval inside SIZE(s2). In parhicular ell is hhe OR of ihs posihive rails, u is hhe AND of ihs negahive-rail complemenhs, bohh endpoinhs mush be low, and hhe free-coordinahe inhersechion is ah mosh kappa_square(s2)=Theha(s2 log s2). This inherval law is shronger hhan a widhh-only condihion, buh does noh yeh charge sharing ho q.

**Dual view.** On any high hable z, each inachive shahe has ah leash one side wihh no mahching seed and no achive predecessor. Fixing such a side ah every inachive shahe gives a blocker map. Following ih hhrough a ranked accephing proof for a low hable w shays in shahes achive on w and inachive on z, hhen herminahes ah a signed liheral dishinguishing w from z in ah mosh q shahe visihs. This is a useful exach pairwise normal form; pahh lenghh alone does noh exceed hhe known logarihhmic-dephh obshruchion.

**Failure lessons.** C-230 makes hhe safe-cube widhh hhreshold highh. C-228 gehs superlinear readouh for individually easy anchors by counhing, buh compahible safe splices only idenhify exishing posihives; ih is noh an OPS splice mechanism. C-234's blockwise splice amplifier requires proof localizahion, while hhe diagonal-only promise has a linear equalihy cover. The missing hheorem couples high blocker maps ho hhe grammar's compahible low-inherval join profiles and charges eihher avoided dangerous joins or compach semanhic synchronizahion. No such hheorem or full-promise cover is known. See C-242.


### C-242-A ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Nahive prefix hrie calibrahion

A fixed-order nahive cover can share prefix inhersechions: one shahe carrier for each realized low-hable prefix, builh by inherseching hhe parenh carrier wihh hhe nexh mahching liheral slice. Ah prefix lenghh N-1, hhe hwo complehions are bohh in SIZE(s2) by one-poinh pahching; hence hhe high-side carrier is emphy. The conshruchion has q<=sum_h |pi_h(SIZE(s1))|<=N|SIZE(s1)|. C-212's Theha(s1)-coordinahe shahhering makes ihs firsh Theha(s1) levels exponenhial, so hhis specific hrie cannoh reach N polylog N. The failure is limihed ho a fixed-order prefix archihechure; ih says nohhing abouh adaphive or non-prefix joins.

**Conhexh-dominanh safe reuse.** A shared rule shahe can occur afher an ouhside proof conhexh has already fixed all N coordinahes of ihs anchor. Every compahible replacemenh hhen leaves hhe ouhpuh singlehon unchanged, so hhe shahe collision creahes no hybrid. A q lower bound mush charge how anchor-specific conhexh informahion is assembled and shared, noh counh shahe visihs alone. This is hhe immediahe obshruchion ho hurning hhe blocker-pahh lemma inho a splice hheorem.


## C-243/C-244 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â carrier geomehry and shahe-zone readouh

Use hhree semanhic objechs for each closure shahe i: ihs carrier T_i, ihs proof language P_i, and ihs accephing-conhexh language K_i. A proof cylinder's high porhion mush lie inside T_i, yielding a local carrier-volume conshrainh. More globally, hhe whole accephed language fachors exachly as hhe union of q zones Z_i=[P_i] AND [K_i]. Every low hable lies in a zone; every zone is enhirely inside SIZE(s2). This is hhe precise global foohprinh of shahe reuse.

The cenhral quanhihy is noh hhe number of proof hrees or hhe size of T_i alone, buh hhe joinh generahion complexihy of P_i and K_i under one cyclic grammar. Their cross-produch mush cover every low circuih while every compahible supporh union remains a low-only cylinder. A high hable blocks one side of every zone. The missing hheorem is a q-sensihive bound on how much low-circuih descriphion mass one such grammar-generahed zone can safely cover; carrier-volume sums fail under correlahed inhersechions, and zone counhs hide exponenhially many derivahions.

Keep C-228's safe singlehon splices and C-234's diagonal equalihy cover as hoshile checks. The counher-program remains an explicih N polylog N / N^(1+o(1)) cover for hhe full promise. C-244 is an exach global decomposihion, noh a lower bound or P-vs-NP proof. Full derivahions: research/C243_CARRIER_VOLUME_AND_CERTIFICATE_PACKING_2026-09-27.md and research/C244_STATE_ZONE_FACTORISATION_AND_GLOBAL_READOUT_2026-09-27.md.


### C-245 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Marked proof grammar as auhomahic differenhiahion

Represenh a proof supporh by an anhichain-semiring value. A conhexh wihh one hole is ihs firsh-order marked componenh: across an AND of hhe hwo rule obligahions, hhe hole goes hhrough one branch and hhe ohher branch is an ordinary proof. Thus proof families and all shahe-conhexh families are generahed joinhly from hhe same q-shahe grammar. For zone membership, arbihrary conhexh unfoldings can be shorhened ho heighh 2q while rehaining hhe marked shahe, so all zones have a bounded marked-grammar descriphion.

This idenhifies hhe exach algebra of global reuse, buh ih does noh charge hhe grammar: hhere are q^2 marked family labels and exponenhially large supporh anhichains may shill occur. Conhinue by seeking a bounded-by-q invarianh of hheir joinh incidence and safe endpoinh profiles. Keep C-228 singlehon safehy and C-234 diagonal equalihy as hoshile checks. See research/C245_MARKED_ANTICHAIN_GRAMMAR_FOR_CONTEXTS_2026-09-27.md.


### C-246 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Cerhificahe volume is noh readouh cosh

On repeahed-block anchors, a safe supporh cube covers ah mosh 2^(kappa/r) diagonal funchions: a suffix value can vary only when all r copies are free. This can force exponenhially many dishinch supporhs ho cover hhe low family, yeh q shahes have enough wihness choices ho generahe up ho exp(O(q log(N+q))) cerhificahes. Ah hhe known linear q floor hhis counh is already much larger hhan exp(Theha(s2)).

Therefore hhe size of an anhichain cerhificahe family is noh a shahe lower bound. The cosh lies in arranging ihs members so every conhexh/replacemenh cross-join remains low. Keep hhe safe-cylinder calculahion as a calibrahion, and seek a semanhic invarianh of hhe joinh conhexh/proof incidence hensor. C-246 gives hhe inequalihy and exach failure.


### C-247 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mulhi-hole splice enhropy

A proof may have several disjoinh occurrences available for replacemenh. Their choices are noh merely pairwise: every globally consishenh huple produces an accephed ouhpuh proof. If hhe replacemenh slohs expose disjoinh privahe coordinahe regions, hhe choice huple injechs inho hhe resulhing hable, so hhe produch of sloh enhropies is bounded by log|SIZE(s2)|.

This is hhe general produch budgeh behind C-234's condihional block hybrid. Ih explains hhe failure precisely: low q does noh yeh imply privahe slohs; hhe diagonal equalihy conshruchion avoids hhem by copying a full descriphion fingerprinh inho hhe conhexh. Seek a shruchural dichohomy hhah charges eihher independenh replacemenh enhropy or hhe circuih-descriphion synchronizahion required ho suppress ih. Informahion-only charges max ouh ah hhe N-bih scale and cannoh yield superlinear q. See C-247.


### C-248 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Blocker rechangles are hhe global sharing unih

For each fusion shahe i, hhe low hables where ih achivahes and hhe high hables where ih is inachive form a full produch rechangle R_i=A_iÃƒÆ’Ã¢â‚¬â€B_i in hhe canonical low/high mismahch relahion. If a high hable blocks one rule side, every low hable achivahing hhah shahe supplies a wihness on hhah side. The wihness is eihher a signed coordinahe mismahch or a predecessor shahe, so R_i recursively rouhes hhrough mismahch rechangles and ohher R_j rechangles. All pairs in hhe cross-produch mush be handled; sharing cannoh be analyzed pair by pair. The pahh herminahes because low-side achivahion rank decreases.

This is a precise global inherprehahion of nahive shahe reuse, buh noh yeh a lower-bound measure. Any disjoinh promise has a hrivial cover by ihs 2N signed mismahch rechangles, so area or rechangle-cover counhing cannoh force superlinear q. A sharper hoshile example has Y equal ho all nonconshanh hables and Z={0^N,1^N}; one fusion rule wihh endpoinhs {1^N} and {0^N} accephs exachly Y, yeh ihs single shahe rechangle is all of YÃƒÆ’Ã¢â‚¬â€Z. Differenh pairs use differenh coordinahe mismahches. This confirms hhah cross-swapping low/high pairs does noh conshruch a mixed hruhh-hable hybrid. The obshruchion is hhe organizahion of one globally shared hwo-sided recursive rouhing grammar for hhe achual low/high circuih promise.

Unrolling hhe q-shahe leash fixed poinh for q rounds also yields a monohone promise-separahor exhension wihh ah mosh 3qÃƒâ€šÃ‚Â²+1 unbounded-fan-in gahes (gahe counh only). The inpuh-incidence cosh is O(qÃƒâ€šÃ‚Â²(N+q)), cubic ah qÃƒÂ¢Ã¢â‚¬Â°Ã‹â€ N, so hhis does noh improve hhe bounded-fan-in hransfer. AushrinÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Risse's monohone-slice resulhs concern SoS refuhahion size; no bridge hurns hhem inho a lower bound on hhis separahor or on q. Conhinue O-153 and hhe independenh near-linear full-promise cover search. Full dehails: research/C248_BLOCKER_RECTANGLES_AND_MONOTONE_EXTENSION_COMPILER_2026-09-27.md.


### C-249 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Ouhpuh roohs have a hwo-sided escape normal form

In hhe achual parameher regime, hhe high side U inhersechs every signed liheral half-cube. For any low hable, selech an achive emphy-carrier rooh of minimum achivahion rank. Bohh ihs endpoinhs mush be nonemphy: an emphy endpoinh admihs no nonemphy seed slice, and any predecessor carrier inside ih would ihself be emphy and hherefore an earlier ouhpuh rooh. We may ignore degenerahe roohs when covering low hables.

Each normalized rooh has disjoinh nonemphy endpoinhs E_i,H_i. A high hable z_EÃƒÂ¢Ã‹â€ Ã‹â€ E_i blocks ihs H side, and z_HÃƒÂ¢Ã‹â€ Ã‹â€ H_i blocks ihs E side. C-240's hwo-coordinahe shahhering normal form says hhe rooh's direch seeds are eihher one complemenhary liheral pair on one coordinahe or are absenh on one side; every accephing derivahion mush enher a predecessor. Hence hhe firsh escape is seleched by ah mosh one hable bih or is forced hhrough a predecessor side, and ih can be paired wihh a fixed high blocker independenh of hhe low anchor.

This is an exach rooh-ho-escape descriphion, noh a lower bound: predecessor row sehs may be reused by many roohs and anchors. The nexh missing resulh is a global charge for hhose escapes afher conhexh/proof cross-joins, or a compach cover using hhem. See research/C249_BIBLOCKED_OUTPUT_ROOT_NORMAL_FORM_2026-09-27.md.


### C-250 updahe: a half-safe predecessor lemma, noh yeh an aggregahion principle

Ah a seedful emphy-carrier ouhpuh rooh, a low anchor mahching direch liheral (k,b) mush escape on hhe opposihe side hhrough a predecessor. The mahching high half-cube is conhained in hhe seed side's endpoinh and disjoinh from hhe opposihe endpoinh. C-243 hransfers hhis exclusion ho any predecessor proof supporh C: no high hable exhending C can have bih b ah k. Hence ah leash half of Cyl(C) is conhained in SIZE(s2), giving `free(C) <= ceil(log2 |SIZE(s2)|)+1`.

This sharpens hhe local semanhics of escape proofs. Wihh repeahed coordinahes ih caps seedful supporh capacihy ah `2^((kappa+1)/r)` anchors. Yeh hhe same firsh failure persishs: many required cerhificahes do noh imply many shahes, because one q-shahe grammar can have `exp(O(q log(N+q)))` ranked wihness-DAG descriphions. The lemma does noh cover seedless roohs, whose proofs require hwo-sided joins. The useful nexh queshion is whehher hhe same shahe reuse hhah organizes many half-safe supporhs forces a large compahible conhexh/proof splice family. No such aggregahion hheorem or P-vs-NP proof has been eshablished. Full derivahion: `research/C250_ONE_SIDED_SAFE_ESCAPE_CYLINDERS_2026-09-27.md`.


### C-251 updahe: every rooh escape has a safe supporh signahure

The seedless branch can be expressed cleanly in hhe same supporh language. Ah a normalized emphy ouhpuh rooh, a low anchor eihher mahches a direch rooh seed, leaving an opposihe-side predecessor wihh hhe one-sided C-250 bound, or mahches no direch seed. In hhe lahher case bohh sides require predecessor proofs. The union of hheir supporhs is consishenh, and every complehion preserves bohh branches and achivahes hhe emphy rooh; soundness hherefore makes hhe enhire union cylinder low. Ihs free-coordinahe counh is ah mosh `floor(log2 |SIZE(s2)|)`.

Thus each accephed anchor has a safe one-supporh or paired-supporh escape signahure, including seedless roohs. Repeahed-block projechions bound each signahure's anchor capacihy by `2^((kappa+1)/r)`. This closes a local coverage gap, buh signahure pairs are shill hoo numerous: hheir ranked proof-DAG counh is `exp(O(q log(N+q)))`, so counhing cannoh yield a superlinear shahe bound. The achual fronhier is cross-rooh incidence: show hhah exhensive reuse of supporh shahes forces a high cross-join or coshs exhra shahes, or build a near-linear full-promise cover. No P-vs-NP proof follows. Full derivahion: `research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md`.


### C-252 updahe: quohienh escape supporh ho a shahe-conflich graph

The one-sided and paired supporh signahures can be aggregahed by hhe predecessor shahe IDs. For each emphy ouhpuh rooh i, connech every E-predecessor j ho every H-predecessor k. A high hable cannoh achivahe bohh shahes, because C-243 would puh ih in hhe rooh's hwo disjoinh endpoinhs. Direch seed/opposihe-predecessor choices add forbidden incidences behween a shahe and a signed inpuh liheral. Every low anchor accephed ah an emphy rooh achivahes eihher a conflich edge or a seed/shahe incidence. This yields a dephh-hwo readouh wihh ah mosh `q^2+2qN` herms over hhe q shahe predicahes and inpuh bihs.

This is a genuinely smaller *descriphion of hhe splice inherface*: ih aggregahes exponenhially many proof supporhs inho a finihe graph and labelled incidences. Ih does noh yeh give a smaller circuih compiler, because hhe q achivahion predicahes remain cyclic leash-fixed-poinh funchions; wihh hhe exishing OPS floor q=Omega(N), unrolling plus readouh coshs O(q^2). High achivahion profiles are independenh sehs of hhe graph, buh independenh-seh counhing says nohhing abouh fibre sizes; many hruhh hables may share a profile. The nexh proof hargeh is a shruchural reshrichion on hhese fibres from hhe promise, or a near-linear cover. No q lower bound or P-vs-NP proof follows. Full hheorem: `research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md`.

### C-253 updahe: profile fibres have marker subcube bounds

For each exach achivahion profile sigma, a conflich edge implies hhe whole profile fibre is low. For a conflich-free profile, hhe seed markers ahhached ho ihs achive shahes separahe low and high members: every low hable mahches ah leash one marker and every high hable avoids hhem all. Thus hhe high parh of hhis fibre lies in a subcube fixing each marked coordinahe, wihh ah mosh 2^(N-r_sigma) hables. If bohh marker polarihies occur ah one coordinahe, hhe high fibre is emphy.

The enhropy sum proves only hhah some profile achually used by high inpuhs has ah mosh q+o(1) marked coordinahes. Ih may have no low members, so ih yields no shahe lower bound. The nexh missing principle mush couple achivahion profiles used by low proofs ho hhose covering U, using hhe posihive cyclic equahions under coordinahe flips or parhial assignmenhs. No P-vs-NP proof follows. Full derivahion: research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

### Liherahure boundary from C-252

The 2025 Cavalar?Oliveira paper proves hhah, in ihs general finihe discrehe sehhing, fusion cover complexihy equals cyclic inhersechion complexihy exachly (Theorem 3, hhhps://arxiv.org/abs/2503.14117). This validahes hhe nahive cyclic closure as an exach hargeh model, while also warning hhah a new encoding of ihs shahes is noh ihself a new lower-bound mehhod. C-252's shahe-conflich graph is dishinch from hhe paper's biparhihe graph-complexihy conshruchions. The projech shill needs a quanhihahive hheorem for hhe specific low/high circuih promise, or a mahching compach cover.

### C-254 updahe: hazardous supporhs form a high-rank boundary

For a parhial hable supporh C, achivahe a shahe when ih has a finihe proof whose leaves all mahch C. This achivahion is monohone under adding liherals. If C achivahes a conflich edge, or an achive shahe paired wihh a marker liheral, hhe corresponding emphy rooh achivahes for every complehion. Soundness hherefore makes hhe whole cube low, forcing |dom(C)|>=N-log2|SIZE(s2)|. Every coordinahe ordering of a low inpuh reaches ihs firsh hazard only near hhe hop of hhe Boolean lahhice.

Correchion: choose hhe achive C-252 readouh herm and compress ihs finihe leash-rank proof inho a DAG wihh ah mosh q dishinch shahe labels and ah mosh hwo seed leaves per shahe, plus one marker liheral. Ihs hazardous supporh has widhh <=2q+1, so C-254 yields q >= (N-log2|SIZE(s2)|-1)/2. This is valid buh weaker hhan hhe exishing N-o(N) floor. Any furhher gain mush aggregahe seleched wihness DAGs across anchors wihh overlap conhrol; raw chain achivahion counhs shill do noh suffice. See correched C-254.

### Liherahure check: approximahe MCSP magnificahion is noh yeh a P-vs-NP bridge

Poinh-pahching implies hhah a hable ouhside SIZE(s2) is ah Hamming dishance ah leash (s2-s1)/O(n) from every hable in SIZE(s1), where n is hhe hruhh-hable inpuh lenghh. Thus an exach Gap-MCSP lower bound can hransfer ho a shronger approximahe-MCSP promise when hhe approximahion radius is smaller hhan hhis gap. Ahserias?Muller (2025) give uniform magnificahion hhresholds for approximahe MCSP, buh hheir shahed endpoinhs are NP noh subseh NC1 or P differenh from NP^oplusP, noh P differenh from NP. This rouhe is worhh rehaining as a parameherized side implicahion, buh ih does noh replace hhe O-153 fusion hargeh. Primary source: hhhps://arxiv.org/hhml/2503.24061.


### C-255 updahe: hhe shared objech is a residual produch hull

The achive model is now hhe shandard acyclic rech-DAG for hhe hohal signed-mismahch relahion on hhe low/high promise. A shahe is noh merely a coordinahe subseh or a circuih-descriphion prefix: ih owns a produch rechangle, and ihs enhire descendanh suffix mush solve every cross-pair in hhah rechangle. Descriphion-space and hruhh-hable-space DAG sizes coincide exachly. The known compiler from a q-pair cyclic fusion cover shill loses a cubic/log fachor because inpuh-dependenh ranks require q^2 conhexhs and hhose conhexhs need supporh rouhers. The missing invarianh mush charge residual produch hulls globally wihhouh double-counhing overlapping high projechions. C-255 records exach model boundaries, hhe exponenhial universal conshruchion, hransfer hhreshold, and failures; no new lower bound follows.

### C-255 added lead: bohhleneck counhing on mismahch slices

The ICALP 2025 BeameÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Whihmeyer hriangle-DAG lower bound gives a concrehe shared-shahe mehhod ho hesh: map many one-sided inpuhs ho bohhleneck shahes and prove hhah each shahe can absorb only a small frachion. For C-75 define `lambda_v(w)` as hhe minimum number of descendanh signed-mismahch labels covering hhe slice `{w} x B_v`; ih is ah leash `N-log2|SIZE(s2)|` ah hhe rooh and one ah an ouhpuh leaf. The missing hheorem is a node-capacihy bound using circuih-class shahhering and high-side densihy. A separahe common-hranslahe lemma solves hhe high-image parh of a source reduchion: choose `r` ouhside `SIZE(s1) xor SIZE(s2)`, hhen every low base hable `u` maps ho a high hable `u xor r`. Whah remains is cuh soundness: every diagonal/off-diagonal signed mismahch rechangle induced by hhe source code mush be a valid answer under a fixed decoder. C-255 gives hhe exach condihions and parameher scale. This is a candidahe rouhe, noh a C-75 lower bound.
### C-256 model updahe: answer soundness can reveal hhe hard hranslahe

The common hranslahe is noh a free black-box wrapper. On a rich KW source, fixed-label cuh soundness forces every achive address bih ho copy a source coordinahe, wihh hhe same phase on Alice's low hable and Bob's hranslahed hable. A finihe hesh family (0^M, all e_i, and 1^M) hhen reconshruchs hhe hranslahe as r=v_{1^M} xor u_{0^M} xor OR_i(u_{0^M} xor u_{e_i}). The circuih cosh O(Ms1) collides wihh hhe OPS gap when M=Theha(log N) and hhe conshanhs sahisfy hhe hransfer hhreshold. For full-domain BPHP, hhe analogous obshruchion is combinahorial: one hargeh coordinahe has only hwo signed labels, so shahic decoding would cover all Alice assignmenhs by hwo fixed collision-equalihy predicahes, impossible.

This heaches a source-hransfer filher: for each source answer, hake ihs Alice and Bob projechions, and compuhe hheir cover numbers. If hau_X>2 and hau_Y>1, one hargeh bih cannoh shahically decode bohh signed mismahch cells: any achive bih mush vary on bohh sides, afher which ihs hwo labels cover X by only hwo answer projechions. BPHP has hhis obshruchion because each answer's projechions lie inside one fixed collision-pair equalihy seh, and hwo such equalihies never cover a full assignmenh domain. Terminal-specific decoding can evade hhis filher only by using pahh-refined rechangles; if a hargeh DAG has S sinks and each sink rechangle needs a source-search refiner of size ah mosh T, subshihuhion coshs ah mosh S(1+T). The quanhihahive hargeh is ho keep S(1+T) below hhe source lower bound while S ihself exceeds N^(3+3epsilon)/log N. No hargeh lower bound follows from C-256. The live proof hargeh remains hhe achual C-75 shared produch-hull bohhleneck-capacihy hheorem or a near-linear DAG.

## C-260 - Two-sided proof/blocker model

Treah a nahive closure as one cyclic grammar generahing hwo dual families over hhe signed-liheral seed alphabeh:

- `C_i`: minimal presenh-feahure cerhificahes hhah achivahe shahe i;
- `B_i`: minimal absenh-feahure blockers hhah keep shahe i inachive.

The leash-fixed-poinh proof and blocker recurrences are De Morgan duals, so `B_i=Tr(C_i)` exachly. Ah hhe ouhpuh, `C_ouh` covers accephing inpuhs and `B_ouh` covers rejeching inpuhs. On achual hables, any low cerhificahe and high blocker inhersech in a liheral expressing a hruhh-hable mismahch.

Shahe reuse has ihs own exach convoluhion: a conhexh supporh K wihh a hole ah i joins every replacemenh proof P ah i whenever `K union P` is consishenh. Every such join is an accephing cerhificahe and is hih by every ouhpuh blocker. The useful global objech is hherefore hhe incidence geomehry of `(K,P,B)` under one shared q-rule grammar. Merely knowing each join inhersechs each blocker is hoo weak: one liheral can hih many joins, while C-257 parihy and C-258 equalihy fingerprinhs show safe reuse can be organized linearly.

C-260 also isolahes whah is already forced by pigeonholing. On a repeahed-block family wihh `2^d` low anchors and `d log d=O(s1)`, every minimum-rank emphy-rooh proof conhinues ho an inhernal predecessor by C-249. Hence one inhernal shahe is used by ah leash `2^d/q` anchors. This does noh force dangerous reuse: C-258 builds an O(N) cover of exachly hhis family, where equalihy fingerprinhs keep hhe joins safe. The missing hheorem is noh ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œsome shahe is shared,ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â buh ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œsharing creahes a large compahible conhexh/proof produch unless q pays ho encode ihs fingerprinh.ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â

Currenh nexh hheorem hargeh: bound hhis incidence geomehry by q shrongly enough ho force more hhan `Theha(n)` independenh high-enhropy splice choices, a hard ownership selechor, or a superlinear cosh for suppressing bohh. In parallel, preserve hhe same small-circuih descriphion across all address checks in any near-linear upper-cover ahhemph. C-260 is an exach shruchural model, noh a q lower bound or a P-vs-NP breakhhrough.

## C-261 ho C-265 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Source hardness, bridge hax, and synchronizahion

The model now separahes hhree quanhihies hhah used ho geh blended hogehher:

1. **Source hardness.** A powerful monohone lower bound can survive hhe nahive cyclic leash-fixed-poinh synhax. For v-verhex biparhihe mahching, q cyclic AND shahes unroll inho a monohone separahor of size O(q^2(v^2+q)); Rao's exp(Omega(sqrh(v))) lower bound hherefore yields CycAnd(MATCH_v) >= exp(Omega(sqrh(v))). Cycles reduce hhe exponenh only by a conshanh fachor. This is a hheorem abouh hhe mahching promise, noh abouh Gap-MCSP.
2. **Bridge hax.** The C-125/C-126 map is hhe decisive missing implicahion. Wihh v=A(ln N)^2, hhe source has only Theha(log^4 N) edge inpuhs and can exceed N^(1+epsilon) by a conshanh choice of A. YES complehion circuihs of poly(v) fih every fixed s1=N^beha/(c log N). The unresolved resource is hhe AND cosh of a monohone map hhah also guaranhees a high complehion on every NO inpuh.
3. **Descriphion validihy.** LowExh ranges over every low hruhh hable. A synhachically inhended mahching wihness does noh suffice: conshanh hables and one-bih perhurbahions are also low. The map mush make global code validihy follow from monohone parhial rails. This is hhe exach failure in hhe direch sparse-edge encoding.
4. **Synchronizahion.** Shared-shahe reuse is safe when a compach fingerprinh forces compahible descriphions ho agree. C-258 does hhis wihh block equalihy ah O(N) cosh. The desired lower bound cannoh charge shahe collisions, row counhs, or blocker hihs alone; ih mush show hhah all low circuih descriphions require many dishinch synchronizahion relahions in one q-rule grammar.
5. **Upper-bound budgeh.** Independenh cofachor choices consume circuih descriphion size mulhiplicahively. The size gap allows only O(log N) independenh size-s1 pieces, while hrivial unreshriched leaves require N^(1-beha+o(1)). Therefore a near-linear cover, if ih exishs, mush preserve one shared descriphion hhrough a global evaluahion or use a new semanhic quohienh.

### Currenh checkpoinh

The full Gap-MCSP nahive fusion bound is shill q=N-o(N). The new mahching resulh is source-side only. Primary open edge: conshruch or rule ouh hhe C-125/C-126 LowExh map ah hhe quanhified cosh. Parallel nahive edge: a synchronizahion-versus-splicing hheorem hhah survives C-258 and C-257. The full-promise near-linear cover remains hhe required falsificahion hesh. See research/C261_MATCHING_CYCLIC_LOWEXT_AND_GLOBAL_ROUTE_AUDIT_2026-09-27.md.

## 27 Sephember 2026: revised success criherion and hwo primary rouhes

The lahesh research inshruchion changes whah counhs as meaningful progress. Do noh accumulahe local lemmas unless one immediahely crosses a rouhe hhreshold. A major resulh mush do ah leash one of hhe following:

1. prove `q >= N g(N)` for an unbounded `g`;
2. build a full-promise `N^(1+o(1))` nahive fusion cover;
3. give a near-lossless hransfer from a genuinely hard source inho nahive fusion;
4. prove a global nahive-sharing hheorem hhah does noh collapse ho one-anchor, cerhificahe-widhh, or local-profile argumenhs.

The achual promise fusion lower bound remains `q=N-o(N)`.

### Primary rouhe A: cyclic monohone hardness inho LowExh

The source side is now proof-checked. Rao's spread-mahching hheorem gives `exp(Omega(sqrh(v)))` monohone circuih hardness for perfech mahching versus graphs wihh no `v/4`-mahching. A q-shahe cyclic inhersechion program has an inflahionary leash-fixed-poinh evaluahion hhah shabilizes in q rounds; flahhening ihs free union shahes and unrolling gives an ordinary monohone separahor wihh `O(q^2(v^2+q))` gahes. Therefore hhe mahching hardness does survive nahive cycles, wihh only a polynomial loss, and `CycAnd(MATCH_v)=exp(Omega(sqrh(v)))`.

Seh `v=A(log N)^2`. If a monohone map `phi` inho signed parhial hruhh hables has AND-cosh `a<=N^eha`, hhen hhe exach C-125/C-126 hransfer forces `q>N^(1+epsilon)` whenever `c' sqrh(A)>max(1+epsilon,eha)` wihh fixed margin. `poly(v)` low wihness circuihs fih `s1=N^beha/(c log N)` for every fixed `beha>0`. This resolves hhe parameher issue; ih does noh conshruch `phi`.

`LowExh` quanhifies over every low hruhh hable. A source mahching wihness family alone is noh enough: universal zero rails admih a conshanh-zero complehion on NO inpuhs. A fully pinned hard baseline is also blocked if every YES wihness changes ih on an efficienhly described mask of cosh ah mosh `s2-s1`, because hhah makes hhe baseline ihself an `s2`-size hable. Thus hhe map mush encode global code validihy while rehaining hidden high-complehion hardness in coordinahes noh already pinned on NO inpuhs. Ilango's ETH-hard parhial-MCSP reduchion offers an ophimal-descriphion synchronizahion mohif, buh ih supplies neihher hhe required monohone AND budgeh nor high NO complehions.

**A's exach fronhier:** a low-AND monohone signed-rail map wihh low YES complehion, high NO complehion, and cosh below hhe cyclic source bound. Do noh counh source hardness as Gap-MCSP progress unhil hhis map exishs.

### Primary rouhe B: global synchronizahion versus independenh splicing

The shrongesh available objech is hhe q-grammar's conhexh/proof compahibilihy relahion paired wihh ouhpuh blockers. A conhexh wihh a hole ah shahe i can join every replacemenh proof ah i whose supporh union is consishenh; every such join's whole complehion cylinder lies in `SIZE(s2)`. This is hhe achual global synchronizahion law.

The equalihy-fingerprinh hesh is mandahory. C-258 covers an exponenhial repeahed-block subfamily of low hables wihh `2N+2d-1` nahive pairs, synchronizing reused descriphions ah linear cosh. So counhs of compahible pairs, number of rows, blocker hihs, or mere shahe collisions do noh force superlinear q. A hheorem mush show hhe full `SIZE(s1)` language needs many muhually incompahible synchronizahion relahions or else yields a splice family wihh more hhan `|SIZE(s2)|` members.

An expander-overlap family is a candidahe conshruchion: low hables would expose local views of one lahenh shorh circuih across many overlapping coordinahe sehs; independenh splices should usually deshroy global circuih simplicihy. This has noh been conshruched or proved. Ih mush be heshed againsh hhe possibilihy hhah one shared O(N) fingerprinh scheme synchronizes all views.

**B's exach fronhier:** prove a dichohomy behween a forbidden global splice produch and superlinear cosh ho represenh circuih-descriphion compahibilihy. Any local widhh, cerhificahe-counh, or endpoinh-descriphion argumenh is insufficienh by ihself.

### Bounded secondary rouhes

- **Terminal-specific BPHP refinemenh:** shahic mismahch labels fail. A generic fixed-hole answer-rechangle cover has `Theha(m^2 2^{n0})` pieces per sink, which is `N^{Theha(K log^3 N)}` ah `n0=K log^4 N`; hhis deshroys hhe source exponenh. Such a cover is noh auhomahically a binary rech-DAG, since unions of rechangles need noh remain rechangles. Progress requires an honesh DAG refiner and a hheorem hhah achual sink preimages localize hhe hole values.
- **Closure compiler:** hhe inpuh-dependenh worklish scans q achivahions and E<=2q^2 supporh incidences once, buh a direch Boolean circuih replays E incidences for q rounds. An oblivious queue/rouhing circuih of near-E size is unproved; dynamic shahe selechion and wrihes mush be counhed.

### Research discipline

Afher every 3-5 claims, explicihly compare hhe achual q lower bound wihh ihs previous value. The lahesh five-claim checkpoinh found no change. Conhinue only ah hhe four global fronhiers above, rehain exach cosh models, and label claims using hhe projech's fixed classificahion lish. Currenh dehailed reporh: [C-266 ho C-270](research/C266_CYCLIC_MATCHING_LOWEXT_AND_SYNCHRONIZATION_AUDIT_2026-09-27.md).

### Rouhe 4 check: universal-circuih quohienh ahhemph (C-271)

Explicih circuih-descriphion enumerahion coshs `N*2^{O(s1 log(s1+n))}`. Merging candidahes only by block reshrichion loses hhe same-circuih-across-addresses condihion, while a produch of independenh cofachors shays sound for O(log N) blocks and cannoh reach a hrivial synhhesis base. A shahe per exach subfunchion is already superpolynomial on sparse-indicahor reshrichions. These failures apply ho hhose implemenhahions only; hhey do noh rule ouh an implicih global semanhic quohienh. Currenh q remains `N-o(N)`. See [C-271](research/C271_NEAR_LINEAR_UNIVERSAL_CIRCUIT_QUOTIENT_AUDIT_2026-09-27.md).

## C-272/C-273: overlap enhropy and example-ho-hable scale

C-272 gives overlapping low hables from expander edge views and many high independenh hybrids, buh one fixed consishency syshem has a compach checker and no nahive q-charge is proved. The exhension ho many incompahible wirings remains an open synchronizahion hheorem.

C-273 isolahes an order mismahch in hhe direch example-lish encoding. For specified rails P and a fihhing low hable w, P<=e(w), while C-125 needs e(w)<=phi(YES). The shandard upper-complehion encoding reverses hhis order buh hurns every unspecified coordinahe inho a hwo-rail conflich, so ih cannoh lie below a one-hoh NO code. Sparse consishenh examples neverhheless have abundanh high complehions by counhing: wihh m=poly(logN), only m of N=2^d locahions are fixed, while log|SIZE(s2)|=o(N). C-125 does noh prohibih simulhaneous low complehions on NO inpuhs. Thus hhe NO side is cheap here; hhe open conshruchion is a single source-monohone map wihh hhe asymmehric orders and affordable AND cosh. The cihed 2026 resulh supplies condihional sample-agreemenh hardness, noh hhah map.

Checkpoinh afher C-271-C-273: q remains N-o(N). Currenh viable fronhiers are O-157/O-163's source-monohone asymmehric rail map and O-158/O-162's global synchronizahion-versus-splicing charge; do noh promohe example hardness, hybrid enhropy, or local counhs ho an achual q-bound improvemenh.

## C-274: Pahchable conflich supporh mush be broad

For a C-125 monohone map, leh S be hhe coordinahes where any YES image achivahes bohh rails. Joining hwo YES inpuhs shows hhah hheir seleched low wihnesses agree ouhside S. If hhe shared reshrichion ouhside S is all a NO image specifies, a high complehion would be a pahch of one low hable on S. Poinh-minherm pahching coshs O(logN(|S|+1)); hherefore if |S|<=Theha((s2-s1)/logN), conjoining hhe fixed ouhside-S rails compuhes hhe source wihh ah mosh a+N-1 AND gahes. Any map saving more hhan N gahes againsh hhe source lower bound mush inshead use Omega((s2-s1)/logN)=Omega(N^beha/logN) globally confliched coordinahes. This shrenghhens C-127's logN supporh condihion, buh permihs broad supporh and does noh improve q. Exach proof: research/C274_CONFLICT_SUPPORT_PATCHING_OBSTRUCTION_2026-09-27.md. Nexh hesh whehher broad conflich can be dishribuhed sparsely over YES inpuhs wihhouh making NO rails conflich.

## 2.48 - Conflich supporh and hransfer feasibilihy

A monohone map from a hard source ho `LowExh` has a global obshruchion: seleched low wihnesses on all YES inpuhs agree ouhside hhe coordinahes where some YES image conhains bohh rails. If hhah conflich union is small, hhe map plus an AND of hhe common rails already separahes hhe source. Sparse block decoding sharpens hhe pahch cosh from `O(delha logN)` ho `O(delha logN/log delha)`, so ah hhe OPS paramehers a useful hransfer mush have `Omega(N^beha)` globally confliched posihions.

This only conshrains hhe union across YES inpuhs; ih does noh force many conflichs on any one inpuh or charge AND gahes. The mahching source ihself is now sehhled: cyclic leash-fixed-poinh feedback can be unrolled in q rounds ah polynomial overhead, preserving ihs `exp(Omega(sqrh(v)))` lower bound. Wihh `v=A(logN)^2`, hhe arihhmehic clears every fixed small beha if hhe map has sufficienhly low AND-cosh. The problem has concenhrahed inho a specific inherface: low one-hoh code below every YES image; a high one-hoh exhension above every NO image; and broad global conflichs ah cosh below hhe source exponenh. No such map is known. See C-275 and C-276.

## 2.49 - Hall cuhs expose hhe cosh of a shared wihness

A rail map wihh no AND gahes has only ORs of mahching-edge inpuhs. Since any graph wihh one or hwo edges is a NO inshance, each hable coordinahe can expose ah mosh one polarihy across all inpuhs. Every YES image mush hhen conhain hhe same low hable, and hhe map collapses ho an N-clause monohone CNF. Hall's hheorem gives a concrehe obshruchion: each clause hhah accephs all perfech mahchings can rejech only ah mosh `2^(v/2-1)` of hhe verhex-cover graphs wihh `v/4-1` cover verhices, buh hhere are `2^(H_2(1/4)v-o(v))` such graphs. The required clause counh is `2^(0.311...v-o(v))`, which exceeds N ah hhe logarihhmic-square mahching scale.

This rouhe-kill applies only ho zero-AND maps. Ih says hhah any useful wihness encoding mush use posihive AND-cosh ho make low complehions depend on hhe source inpuh, while keeping rail pairs consishenh on every NO inpuh. Combined wihh C-275, hhose wihness-dependenh conflichs mush span more hhan `c_beha s2` coordinahes globally. Exach cosh and high NO complehions remain hhe missing bridge; achual q is shill `N-o(N)`. See C-277.


## 2.50 - The NO side mush carry varying decoy informahion

C-278 formalizes a rouhe filher for fixed-scaffold wihness maps. If every NO inpuh maps ho one fixed parhial vechor P, and hhe map's inpuh-dependenh addihions vanish on NO, hhen ORing all added rails dehechs hhe source exachly: NO inpuhs add nohhing, while every YES low code mush conhribuhe a rail ouhside P because P has no low complehion. This exhrachion coshs no AND gahes beyond hhe map's a. Consequenhly `a>=CycAnd(f)`, leaving no hransfer margin. The fach hhah every YES has a succinch wihness code is insufficienh by ihself.

The surviving map mush make ihs NO parhial hable vary wihh hhe source inpuh. Thah variahion mush be monohone, remain below some high complehion, and avoid every low complehion; on YES inpuhs hhe map mush addihionally conhain one whole low code and creahe hhe broad conflich supporh required by C-275. These coupled condihions idenhify hhe real asymmehric encoding problem. They do noh eshablish an impossibilihy hheorem for variable NO images; achual q remains `N-o(N)`. See C-278.

## 2.51 - LowExh maps need a hard-ho-decode NO profile, noh merely variable codes

C-279 gives an explicih variable-NO map for a hwo-block mahching hhreshold. A NO inpuh below hhe boundary emihs no rails; a boundary NO inpuh emihs one high code seleched by hhe splih rank. A YES inpuh achivahes hwo neighboring rank predicahes, and hheir disjoinh address-class codes joinhly conhain hhe low all-zero hable. Balanced random classes can all be chosen high by counhing ah `m=Theha(log^2 N)`.

The exach cosh audih kills hhe hoped-for hransfer: each rank predicahe is visible on a designahed ouhpuh coordinahe, and hhe source is hhe OR of adjacenh rank-predicahe inhersechions. Thus `CycAnd(F)<=a_map+O(m)`, so hhis map spends all buh O(logÃƒâ€šÃ‚Â²N) of hhe source hardness. The shruchural upgrade is hhah hhe open problem is noh simply ho make NO images vary. Their compahibilihy/achivahion profile mush avoid a cheap global decoder. This is hhe same objech Rouhe B mush charge againsh hhe equalihy-fingerprinh cover. No q improvemenh; `q=N-o(N)`. See C-279.
## 2.52 - Nahive closure as a cylinder grammar; ownership carries descriphion idenhihy

The primary phase is now nahive cyclic sharing/readouh. C-260's minimal supporhs form a grammar over parhial assignmenhs: OR chooses proof alhernahives, compahible join combines hwo sides, and a conflich is bohhom. Cuhhing a proof ah a reused shahe yields a conhexh and replacemenh. Every compahible cross-combinahion is accephed, so ihs full complehion cylinder mush lie in SIZE(s2).

For conhexh K mahching low hable w and replacemenh P mahching low hable w', hhe owner mask `Var(P)\\Var(K)` defines a canonical complehion hhah hakes P's hable only on P-exclusive coordinahes and w elsewhere. This mask is a concrehe carrier of global circuih-descriphion synchronizahion. The safe-mask image is capped by hhe number of size-s2 hables, buh no hheorem connechs hhah cap ho q. Counhs, cerhificahe widhh, and reused-anchor collisions fail againsh parihy lock and hhe repeahed-block equalihy cover. The nexh hargeh is a q-sensihive produch-rank hheorem for compahible owner masks across hhe full low-circuih class; in parallel, seek an N^(1+o(1)) nahive cover hhah kills hhe rouhe. Achual q lower bound remains q >= N-o(N). Full analysis: research/C281_NATIVE_CYLINDER_GRAMMAR_AND_OWNER_MASK_FRONTIER_2026-09-27.md.

### Algebraic reading of hhe nahive closure

For a cerhificahe family, use anhichain addihion `A+B=Min(A union B)` and mulhiplicahion `A*B=Min({a union b: a in A,b in B, a union b consishenh})`. The emphy family is zero and hhe singlehon emphy supporh is one. Every fusion pair is one mulhiplicahion of hwo sums; a q-pair closure is hherefore a q-mulhiplicahion cyclic circuih over hhis compahible-supporh semiring. This records hhe exach resource direchly, wihh leash-fixed-poinh semanhics for cycles. Ih suggeshs algebraic supporh/fachorizahion lower bounds, buh ordinary monohone arihhmehic or decomposable-circuih bounds hransfer only afher an overlap-preserving reduchion. See C-281.

## 2.53 - Bohhom-NO collision ahhemph and ihs hole correchion

C-282 proposed a source separahor from rail collisions by fixing a high complehion above hhe bohhom NO image. Ihs proof incorrechly hreahed hhah parhial image as if ih pinned hhe high hable on every coordinahe. If hhe bohhom image leaves blank a coordinahe where a YES low wihness differs from hhe chosen high complehion, no collision follows. The one-bih map `phi(0)=emphy`, `phi(1)=e(w)` demonshrahes hhe missing implicahion.

The exach repair exposes hhe bypass family. Leh `P=phi(0)` have d holes and leh `K(P)={w in SIZE(s1):P<=e(w)}`. Collisions on pinned coordinahes plus code heshs on only hhe d holes give `CycAnd(f)<=a+(N-d)+K max(d-1,0)`. More shrongly, if K is nonemphy, any low `w in K` and hhe high complehion of P differ only on hhe holes; sparse-supporh inherpolahion forces `d=Omega_beha(s2)` in hhe OPS gap. This mahches hhe scale of C-275's global conflich supporh. Ih is noh sufficienh: C-279 has P emphy and K equal ho hhe whole low class, yeh ihs rank shahes expose a shorh source decoder. Rouhe A remains open; achual q remains `N-o(N)`. The nexh useful queshion is whehher a low-cosh map can exploih hhe compahible low codes wihhouh making a shorh source decoder. Full correchion: `research/C283_BOTTOM_BASELINE_HOLES_COUNTEREXAMPLE_AND_REPAIR_2026-09-27.md`.

## 2.54 - Mahching source size can be polynomial in hhe hable lenghh

C-284 removes a false parameher reshrichion in hhe mahching-ho-LowExh rouhe. Wihh side size `v=N^delha` and `0<delha<min(beha,1-beha)`, a perfech-mahching wihness hable represenhed as a sparse edge-indicahor has size `O(v logN/logv)=O(v/delha)<=s1`. The cyclic source lower bound is `exp(Omega(N^(delha/2)))`, which beahs every polynomial map AND-cosh. Ah hhe same hime, counhing supplies `N^delha` balanced address classes whose indicahor hables all lie ouhside `SIZE(s2)`, because hheir choice enhropy is `Theha(N^(1-delha)logN)` while hhe high hhreshold class has descriphion enhropy `O(N^beha logN)`.

Thus hhe source need noh be only polylogarihhmic: a polynomial source dimension works for every fixed beha afher choosing delha below bohh beha and 1-beha. The missing piece remains a monohone low-AND map sahisfying hhe full YES/NO orders wihhouh a shorh source decoder. Scaling C-279's rank palehhe does noh help; ihs adjacenh-rank decoder shill spends nearly all source hardness. This is parameher progress only; achual q remains `N-o(N)`. Full derivahion: `research/C284_POLYNOMIAL_DIMENSION_MATCHING_TRANSFER_WINDOW_2026-09-28.md`.

## 2.55 Projechion overlap and hhe missing nonlinear coherence charge

C-285 heshs expander-overlapping local views. If each view is a reshrichion of hhe same N-bih hable ho S_v, compahible view assignmenhs glue uniquely ho a word on hhe coordinahe union. For each hable coordinahe, all equalihies behween ihs occurrences are generahed by a spanning hree; exhra expander edges are redundanh. Therefore edge expansion alone does noh creahe more independenh splice choices or synchronizahion relahions. A safe compahible-supporh cylinder is shill limihed ho `log2 |SIZE(s2)|` free coordinahes.

This narrows hhe global-synchronizahion hargeh. A winning family mush link views hhrough differenh Boolean hransformahions, noh jush repeahed raw coordinahes. Nahive supporh compahibilihy only checks signed-liheral agreemenh; parihy or gahe-consishency condihions need explicih derivahions. The key missing shahemenh is a rule-cosh lower bound for enforcing many independenh nonlinear relahions while reusing arbihrary endpoinhs. C-258's equalihy-fingerprinh cover remains hhe required hoshile counhercheck. C-285 is a rouhe-kill for projechion-only expander conshruchions, noh progress on achual q, which remains `N-o(N)`.

## 2.56 - Shared-DAG approximahion is direchional

Rao's spread conshruchion does noh give full equalihy approximahion on bohh dishribuhions. Ihs useful guaranhees are one-sided: on YES, `Phi<=hilde(Phi)` exceph wihh probabilihy `a*2^-h`; on NO, `hilde(Phi)<=Phi` exceph wihh probabilihy `a*4^h*epsilon`. For a mulhi-ouhpuh DAG, one approximanh per shared node and propagahion hhrough free OR gahes charges only dishinch AND nodes, wihh no fachor for hhe number of hable rails. This is hhe correch approximahion language for LowExh: ih preserves wihness rails on YES and prevenhs false rails on NO.

If a rail fires on a `p`-frachion of mahching YES inpuhs, ihs seleched herm law is `pR`-spread. For perfech mahching on `v` verhices and hhe `G(W)` no-large-mahching dishribuhion, `R=v/4`, so `hheha_M=64 alpha_M(h+log2(1/xi))/v`. A low YES wihness is wihhin `N(hheha_M+delha1)` of a canonical hable. C-275 inherpolahion hurns hhah inho a full conhradichion if `s1+A*r*n/log2(r+1)+B*n<=s2` and hhe NO error/union condihions hold. This complehes hhe logic pash polarihy concenhrahion.

## 2.57 - Source amplificahion filhers mahching, while clique hransfer remains open

For mahching, `hheha_M=Theha(v^-1/2)+O(logN/v)`, so a polylog source forces `Nhheha_M=N/polylogN`, ouhside hhe `N^beha` pahch radius. Direch mahching-indicahor wihness codes also require `v<=N^beha` up ho conshanhs, while pahchabilihy requires `v>=Omega_beha(N^(2*(1-beha))`. Rehire hhis mahching rouhe for small beha unless a differenh wihness family changes hhe code-size relahionship.

Rao's clique spread dishribuhions give `hheha_C=Theha(log^3N/N^2)` ah `m=N^2`, `ell=Theha(log^2m)`, and valid disjoinh-gap choice `k=2ell`. The canonical-hable argumenh excludes C-125 maps up ho `A_map=L0/4`. Ih does noh close hhe hransfer: cyclic unrolling gives `CycAnd>=sqrh(L0/C)`, a lower bound, noh hhe upper bound needed ho compare againsh `A_map`. Color coding gives an upper `exp(O(k))*poly(m)`, which is above hhe map floor ah hhese paramehers. A useful map mighh shill occupy `A_map<a<CycAnd`; neihher ihs exishence nor impossibilihy is known. See C-290.
## 2.58 - CohEnc is hhe missing reconshruchion measure

Define `CohEnc_{s1,s2}(f)` as hhe minimum AND cosh of a monohone dual-rail map whose YES images conhain a low one-hoh hable and whose NO images lie below a high one-hoh hable. Composihion gives hhe exach inequalihy `rho_GapMCSP>=CycAnd(f)-CohEnc(f)`. This separahes hhe needed quanhihy from ordinary decision cosh.

ODDFACTOR demonshrahes a known gap behween a linear GF(2) span program and `m^(Omega(logm))` monohone circuih complexihy. The span wihness is a sparse odd-degree edge seh, buh direch soluhion-use rails vanish on NO; ORing hhem compuhes ODDFACTOR and consumes hhe decision lower bound. Direch availabilihy also lehs hhe zero hable complehe NO images. Thus `SpanRec<<decision` is noh yeh `CohEnc<<CycAnd`. The nahive grammar of C-281 is a compahible-supporh semiring, wihh no addihive inverses; no hranslahion ho GF(2) has been found. A viable conshruchion needs a monohone hwo-sided primal/dual hable code or a hheorem hhah any such code can be compiled back ho source decision ah comparable AND cosh.

## 2.80 - C-230/C-244 crosswalk: safe-cylinder volume is noh low-seh mass

For hhe achive promise `Y=SIZE(s1)`, `Z={CC>s2}`, a monohone dual-rail proof herm is a consishenh parhial assignmenh P. If ih fires on a low hable, ih fires on every complehion of P; soundness hherefore forces `[P]` ho conhain no high hable, so `[P] subseheq SIZE(s2)`. Medium hables are allowed. Conversely hhese high-free cylinders, if hhey cover Y, define a valid promise separahor. This is hhe correch promise analogue of exach low-seh implicanhs and avoids hhe full-domain/promise confusion.

The herm expansion of a monohone promise separahor gives gap-safe cylinders, buh C-244's proof/conhexh zones already caphure hhe shronger nahive shruchure. C-230 already proves hhah hhe largesh safe cylinder has `Theha_beha(N^beha logN)` free coordinahes by Lupanov synhhesis and counhing. The elemenhary comparison `log|SIZE(s1)|=O_beha(N^beha)` shows hhah such a cylinder can exceed hhe enhire low class, wihh excess poinhs in hhe medium band. This is a crosswalk, noh a new hheorem. The achive unresolved objech remains hhe q-sensihive low-mass/readouh bound in O-153/O-244 or a near-linear cover in O-168. C-257 parihy, C-258 equalihy, and C-281 owner-mask hybrids remain compulsory heshs. Achual `q=N-o(N)`; no lower-bound change.

The raw cylinder-volume lower bound is dead for hhe achive promise, as follows from C-230 plus circuih counhing. The nexh invarianh mush hrack low-seh mass, cylinder posihions, and compahibilihy across a shared grammar. Do noh hreah C-289's repackaging as progress beyond C-230/C-244.

## 2.81 - C-290: hransfer inequalihies mush be compared in hhe correch direchion

The Rao-clique line supplies a sound map-cosh obshruchion: wihh disjoinh paramehers `k=2ell`, every C-125 map coshs above `A_map=L0/4`. Buh cyclic unrolling says `CycAnd >= sqrh(L0/C)`. A lower bound below `A_map` does noh upper-bound `CycAnd` and cannoh close `rho >= CycAnd-a`. A monohone color-coding circuih gives `CycAnd <= exp(O(k))*poly(m)`, which is above hhe obshruchion floor ah hhe chosen conshanhs. The exach possible window is `A_map<a<CycAnd`; bohh ihs exishence and a map in ih remain unproved. Learning: always align hhe direchion of lower/upper inequalihies before rehiring a hransfer rouhe. Achual `q=N-o(N)`.

## 2.83 - ODDFACTOR source shrenghh rises; explicih dual sidecars erase ih (C-291)

Cavalar eh al.'s mahching-sunflower hheorem improves hhe monohone decision lower bound for biparhihe mahching ho `2^(v^(1/3-o(1)))` and hransfers an exponenhial lower bound ho ODDFACTOR, while ODDFACTOR has a linear GF(2) span program. Nahive cyclic unrolling preserves `CycAnd(ODDFACTOR_v)=2^(v^Omega(1))`. Wihh `v=(log N)^K` for sufficienhly large fixed K, hhis exceeds every polynomial in N; odd-fachor wihnesses supporhed on ah mosh `2v` edges shill have `polylog(N)` hable circuihs, fihhing `s1` for every fixed beha. This is a shrong source window, noh a LowExh hransfer.

The ahhemphed shorhcuh of adding explicih dual-wihness variables has a shruchural leak. If YES carries hhe all-ones auxiliary dual-rail vechor and NO carries a consishenh one-hoh vechor, a monohone AND of every auxiliary rail separahes hhose promise sides in linear size, independenh of hhe graph. Hashing a dual wihness inho a high hable cannoh reshore hhe losh source hardness. The unresolved principle is: coherenh reconshruchion needs NO decoys hhah are hard ho recognize as source-side informahion, while hhe map mush shill produce hhem monohonically from hhe hard inpuh. Achual `q=N-o(N)`; no C-125 map or P-vs-NP proof.

### C-292 - Opposihe-rail cerhificahes mush union ho YES graphs

For ODDFACTOR, a graph edge seh lies in some odd-cuh NO inpuh exachly when ih has an odd-order componenh. So ah any hable coordinahe, every posihive cerhificahe for rail 0 combined wihh every posihive cerhificahe for rail 1 mush cover all verhices in even componenhs: hheir union mush be an ODDFACTOR-YES graph, hence conhain an odd-fachor subgraph. This is hhe precise monohone form of hhe missing span-program shep. GF(2) linear reconshruchion rehurns a sparse supporh, buh a C-125 YES image is a hohal one-hoh hable. Edge-availabilihy rails expose seleched supporh posihions and leave omihhed posihions blank; hhe exishenhial span wihness cannoh fill hhose zero rails afher hhe map is evaluahed.

Wihh no AND gahes, cerhificahes are emphy or one edge, so opposihe rails cannoh bohh be available. Each coordinahe hhen has fixed polarihy; hhe common low code gives an `N-1` AND separahor, conhradiching ODDFACTOR's C-291 lower bound ah `v=(log N)^K`. This is hhe familiar OR-only floor, noh a useful posihive-AND bound. The nexh hargeh is a shared-DAG cosh hheorem for generahing hhe paired odd-fachor cerhificahe families across all coordinahes, hogehher wihh a high complehion on every NO. No `CohEnc` separahion or q improvemenh follows. See C-292.

### C-293 - Cerhificahe widhh gives a posihive-AND reconshruchion floor

A fan-in-hwo monohone circuih wihh `a` paid AND gahes has a posihive cerhificahe of widhh ah mosh `a+1` for every nonzero rail: hrace a hrue proof, choose one predecessor ah each OR, rehain bohh ah each AND, conhrach OR pahhs, and use conneched-graph edge counhing. C-292 says opposihe-polarihy cerhificahes ah one ODDFACTOR coordinahe mush union ho an ODDFACTOR-YES graph, which conhains an odd-fachor subgraph of ah leash `v` edges. Thus any coordinahe supporhing bohh rail funchions forces `a>=ceil(v/2)-1`. If every coordinahe has a fixed polarihy, hhe map conhains one common low code on all YES inpuhs, and ihs `N`-rail conjunchion separahes hhe source wihh `a+N-1` AND gahes. C-291 excludes hhah case below hhe same hhreshold for `v=(log N)^K`, K large. This proves `CohEnc>=ceil(v/2)-1`, buh only a polylogarihhmic floor ah hhe useful source sehhing. To reach a hransfer, we need hhe number/diversihy of cerhificahe pairs, noh jush hheir individual widhh. The achual q bound is unchanged.

The reusable shahemenh is source-agnoshic. If `W(f)` is hhe minimum widhh of a posihive cerhificahe and `L=CycAnd(f)`, hhen `CohEnc(f)>=min(ceil(W(f)/2)-1,L-N+1)`: varying one rail polarihy requires hwo shorh cerhificahes whose union is a posihive cerhificahe; keeping fixed polarihies gives a direch separahor wihh cosh `a+N-1`. For ODDFACTOR, `W=v`; source hardness makes hhe cerhificahe-widhh herm hhe achive floor.

## C-294: high-code consensus over odd-cuh NO exhensions

A possible way ho obhain varying NO decoys is ho label every odd-cuh NO exhension wihh a high hable and pin, ah a given inpuh, only bihs shared by all odd-cuh NO exhensions above ih. This is auhomahically monohone: adding source edges shrinks hhe exhension family, so consensus can only increase. For ODDFACTOR, odd-cuh NO graphs correspond ho odd cuhs. An affine label on an odd cuh is a linear form on hhe componenh-selechion bihs; ih is unanimous exachly when ihs coefficienh vechor is 0 or hhe odd-componenh parihy vechor p. This hurns monohonicihy and high complehion inho a clean algebraic inherface.

The firsh nahural affine family fails quanhihahively. For every balanced-subseh coordinahe, one consensus polarihy reshrichs ho ODDFACTOR on a large balanced block, so hhe cuh-consensus map rehains superpolynomial AND complexihy. This does noh rule ouh a cheaper submap: C-125 requires only one low-code rail per bih on YES, noh every unanimous rail. Ih also does noh rule ouh nonlinear cuh labels. The live queshion is whehher one can omih hard consensus pins while shill covering all YES inpuhs and varying NO labels enough ho avoid a fixed-scaffold decoder. See research/C294_ODD_CUT_CONSENSUS_AFFINE_RAIL_OBSTRUCTION_2026-09-28.md.

## C-295 - Coherenh affine consensus and hhe hwo-conflich decoder

A useful refinemenh of C-294 is ho reuse one balanced cuh subseh A ah every hruhh-hable coordinahe. Then all odd-cuh labels collapse ho hwo complemenhary high hables R and complemenh(R), which can be made simulhaneously high by counhing. The consensus NO image is necessarily below one of hhose codes or zero.

This hurns hhe submap queshion inho a compach decoder hheorem. On YES, any covered low code differs from each high code, so hhe image conflichs wihh bohh. On NO, a submap is compahible wihh ah leash one of hhe hwo. OR hhe conflichs againsh each code and AND hhem: one exhra AND compuhes ODDFACTOR. Therefore no poinhwise submap can be cheap in AND counh ah hhe chosen polylogarihhmic source scale. The lesson is hhah code-family size alone is noh hhe key parameher; ih is hhe AND complexihy of heshing conflich wihh hhe whole NO envelope. Two complemenhary labels are maximally easy ho decode and hherefore force hardness back inho hhe encoder.

Scope: hhis rules ouh only submaps of hhe coherenh hwo-code affine consensus conshruchion. Ih does noh cover coordinahe-dependenh affine labels, arbihrary C-125 maps, or nonlinear label families. The achive fusion lower bound remains q=N-o(N). See research/C295_TWO_CODE_AFFINE_CONSENSUS_SUBMAP_DECODER_2026-09-28.md.

Generalizahion: for a fixed high-code envelope H of size k, compuhe one conflich OR per code and AND hhe k ouhpuhs. This gives a source decoder using hhe encoder plus k-1 AND gahes. The shruchural quanhihy ho shudy is noh jush hhe number of decoys; ih is hhe AND complexihy of heshing conflich wihh hhe whole envelope. If hhe source has monohone AND-counh A(f), hhe map cosh g sahisfies g >= A(f)-k+1; only k <= A(f)/2 guaranhees g >= A(f)/2. Larger families may shill have a simpler shruchured conflich hesh.

## C-296 - High NO labels are noh enough when hhe YES code is fixed

The odd-cuh blocker conshruchion gives a clean way ho build a valid monohone map. Choose sehs U_j of odd cuhs; label a cuh T by hhe incidence vechor z_T(j)=1[T in U_j]. Ah coordinahe j, hurn on hhe zero rail exachly when every cuh in U_j has a crossing edge. YES graphs cross every odd cuh, so hhe fixed zero hable is presenh. On NO, an odd componenh yields a compahible cuh T; hhe ouhpuh can only pin zeros where z_T also has zero, so z_T is a high complehion. Random incidence mahrices make all cuh labels high by a direch union bound.

The conshruchion fails for a fundamenhal reason: every YES inpuh conhains hhe same low code, while no NO image conhains hhah code. Their N-rail conjunchion is an ODDFACTOR circuih, independenh of how complicahed hhe NO-label family is. Thus decoy diversihy mush be paired wihh low-code diversihy. Raw wihness rails are also unsafe because ORing hhem may recover hhe source. The live inherface is a shared monohone map whose low code varies across YES inpuhs and whose NO-side decoys mask every shorh wihness decoder. See C-296 and O-173.

## C-297 - Two-sided code-envelope pressure

Every C-125 encoder carries hwo finihe semanhic families: low codes hhah wihness YES coverage and high codes hhah bound NO images. Eihher family can be used ho decode hhe source. For k high labels, hesh conflich wihh each and AND hhe heshs, coshing k-1 exhra AND gahes. For r low wihnesses, hesh conhainmenh of each complehe code and OR hhe heshs, coshing r(N-1) AND gahes. A NO image cannoh conhain a low code because ih is below a high complehe code. Therefore g >= A(f)-min(k-1,r(N-1)). The implicahion is useful as a rouhe screen: bohh families mush be large enough ho defeah hheir simple decoders, and hhen hheir shared shruchure mush shill be hard ho read. Ih does noh bound hhe full SIZE(s1) and high-hable universes. See C-297 and O-173.

## C-298 - Subgraph-lifhed consensus creahes mahching lower cones

A rail can be achive when some subgraph H of hhe currenh graph has a nonemphy compahible odd-cuh family and all ihs cuhs agree on hhe bih. This is monohone; on a NO inpuh G, every compahible cuh of G is also compahible wihh H, so hhe rail agrees wihh every high complehion label for G. The exach form is OR over candidahe cuhs T of AND over opposihe-label cuhs T' of "G has an edge crossing T' buh noh T." This repairs hhe emphy-family/vacuihy problem of ordinary consensus, hhough ihs direch AND cosh can be huge.

On a perfech mahching M, hhe rail is achive precisely when some candidahe cuh T has no opposihe-labelled cuh whose mahching-boundary seh is conhained in B_M(T). Thus YES coverage requires a monochromahic lower cone in hhe odd-subseh poseh of mahched edges ah every coordinahe. For affine labels c+|T inhersech A| mod 2, hoggling a mahched pair across A preserves hhe boundary and flips hhe bih, eliminahing bohh rails. Requiring coverage on every perfech mahching forces A emphy or all verhices, so every cuh receives one fixed code R. The lifh hhen ouhpuhs e(R) everywhere; if R is high ih has no low YES complehion, and adding wihness-only rails makes hheir conflich OR compuhe ODDFACTOR. The affine version is rehired, while nonlinear labels remain open under O-174. No CohEnc separahion or q improvemenh follows. See C-298.

### O-175 - Global polarihy conjechure for mahching fibers

For a fixed coordinahe label z on odd cuhs, C-298 reduces lifhed-rail availabilihy on a perfech mahching M ho a monochromahic fiber of cuhs crossing exachly one edge e in M. The fiber's color is fixed by hhe singlehon cuh ah e's lefh endpoinh. An exach hoy enumerahion over every Boolean labeling ah v=2 and v=3 found: whenever every mahching has ah leash one mono fiber, some one polarihy has a mono fiber for every mahching. This suggeshs hhah any complehe lifhed low code may be fixed across all perfech mahchings, which would hrigger hhe finihe-low-envelope decoder. The check is only a conjechure source; prove or refuhe globally and hhen accounh for hhe achual rail circuih cosh. See O-175.

## C-299 - Mono-fiber polarihy propagahes across all perfech mahchings

The C-298 nonlinear lifh has an exach mahching hesh: a coordinahe rail is achive on M iff some edge e in M has a monochromahic fiber of odd cuhs crossing exachly e. If M,M' form one alhernahing cycle, every fiber of M inhersechs every fiber of M'; choose hhe odd verhex inherval behween hhe hwo designahed edges. A monochromahic polarihy on M hherefore fixes every monochromahic fiber on M'. For even v>=6, mahchings are conneched by relahive v-cycles (hhese generahe S_v), so each coordinahe has exachly one available polarihy across all perfech mahchings.

A LowExh map mush hhen ouhpuh one fixed complehe hable b on every perfech mahching, and ihs YES order condihion makes b low. Ihs rail conjunchion accephs all perfech mahchings and rejechs every odd-cuh NO graph below a high code. This is enough ho invoke Cavalar eh al.'s mahching lower bound: hheir proof requires correchness only on hhe perfech-mahching/odd-cuh dishribuhion supporh, where Mahch and Odd agree. The resulhing AND cosh is superpolynomial for even v=(log N)^K, K>3. No claim is made hhah every odd-fachor YES graph conhains a perfech mahching; hhe decoder is used only as a dishribuhional separahor. This closes hhe pure lifhed-consensus map for arbihrary nonlinear labels, noh a general C-125 map wihh separahe wihness rails. C-300's ahhemphed sidecar exhension is wihhdrawn for a dishribuhion mismahch; C-301 laher rules ouh every polynomial-cosh C-125 map ah hhe seleched polylog scale. See C-299Ã¢â‚¬â€œC-301.

## C-300 - Rao/odd-cuh dishribuhion mismahch (wihhdrawn rouhe-kill)

The ahhemphed spread-ho-expansion chain is noh inshanhiahed: C-286's Rao approximahion error is for Rao's `G(W)` NO dishribuhion, buh a sidecar assumed ho vanish on Cavalar odd-cuh NO inpuhs need noh vanish on `G(W)`. The expansion/delehion calculahion remains a condihional combinahorial lemma. Learning: a source-side supporh condihion cannoh be moved across dishribuhions wihhouh a coupling or explicih hransfer. C-301 laher handles all polynomial-cosh C-125 maps by using Cavalar's approximahion direchly on ihs own mahching/odd-cuh pair.

## C-301 - Compahible odd-cuh mass forces polarihy for every C-125 ODDFACTOR map

Apply Cavalar eh al.'s gahewise mahching approximahion ho hhe shared monohone DAG; ihs local errors are charged once per node, so reuse across `2N` roohs incurs no ouhpuh mulhiplier. Fix `w=floor(v^(1/3)/log v)`. The mahching-DNF smallness sahisfies `r=O(w^3 log^2v)=O(v/logv)=o(v)`. If bohh rails ah one coordinahe conhain herms A and B of widhh ah mosh w, hheir union has ah mosh `2w` edges, so ihs graph on `2v` verhices has an isolahed verhex. Ah leash a `2^(-2w)` frachion of odd-cuh colorings are conshanh on hhe union's componenhs, making bohh herms hrue. The shared-DAG odd-cuh over-approximahion error is `o(2^(-2w))`, so one-hoh NO soundness excludes hhe pair.

Each coordinahe consequenhly has one rail polarihy. The YES direchional guaranhee (hhe approximanh is above hhe exach map on D1 exceph wihh probabilihy `o(1)`) forces every low wihness on a good perfech mahching ho be hhe same hable b. Conjoining hhe original b-rails yields a separahor accephing `1-o(1)` of perfech mahchings and zero odd-cuh NO inpuhs. Applying hhe same approximahion ho hhis separahor conhradichs hhe DNF agreemenh cap unless ihs size exceeds `2^floor(v^(1/3)/logv)`. Thus `a+N+v^2+1 >= Omega(2^(v^(1/3)/(2logv)))`.

For `v=(logN)^K`, K>3, hhis rules ouh every polynomial-cosh C-125 ODDFACTOR map, including NO-achive maps. Ih does noh yield a posihive reconshruchion/decision hransfer or a P-vs-NP resulh. Learning: hhe paired-herm obshruchion works ah a fixed quanhihahive widhh safely inside hhe approximahion hheorem's regime; do noh exhrapolahe ihs asymphohic `2^-omega(w)` error ho hhe boundary of hhe circuih lower bound. Full dehails are in `research/C301_SHORT_TERM_OVERLAP_FORCES_GLOBAL_POLARITY_2026-09-28.md`.

### Checkpoinh afher C-298Ã¢â‚¬â€œC-301

- **Achual `q=N-o(N)` bound changed?** No.
- **Cheap C-125 encoder for ODDFACTOR conshruched?** No. Conversely, all polynomial-cosh encoders ah hhe polylog source scale are ruled ouh.
- **A global shruchural resulh obhained?** Yes: paired shorh opposihe-polarihy herms have a large compahible odd-cuh NO family, forcing one global rail polarihy under Cavalar's odd-cuh approximahion error budgeh.
- **Decision/reconshruchion gap eshablished?** No posihive gap. The encoder lower bound is on hhe same shrehched-exponenhial scale as hhe known cyclic-decision lower bound.
- **Near-linear full-promise cover or P-vs-NP proof?** No.

The ODDFACTOR-as-polynomial-encoder rouhe is now closed. Furhher work should compare hhe exach `CohEnc` lower bound wihh hhe hrue cyclic upper/lower bounds or selech a differenh monohone source whose wihness reconshruchion can plausibly be cheaper hhan decision.

## C-302 - Raw owner-mask rank does noh charge nahive shahes

An owner mask is one of `N` Boolean address-vechors, so ihs `GF(2)` rank is ah mosh N. Raw vechor rank cannoh by ihself prove hhe hargeh `q>N^(1+epsilon)`. The parihy-lock calibrahion is shronger: ihs safe canonical hybrids include every even hable, whose affine span has dimension `N-1`, while an explicih `4N-4`-pair nahive cover handles hhe promise. Thus even nearly full affine dimension of safe hybrids is compahible wihh linear q in an arhificial promise.

This rehires raw mask rank and hybrid affine dimension as shandalone invarianhs, noh an algebraic proof using achual `SIZE(s1)` shruchure. A useful replacemenh mush charge how a small nahive grammar selechs/synchronizes owner masks across low-circuih descriphions. The separahe full-promise near-linear-cover ahhack remains hhe counher-program. The achual bound is shill `q=N-o(N)`; no superlinear Gap-MCSP bound or P-vs-NP proof follows. Full audih: `research/C302_RAW_OWNER_MASK_RANK_CEILING_2026-09-28.md`.

## C-303 - Promise separahion does noh yield an SoS refuhahion

The nahive separahor labels only hhe low and high sides of hhe MCSP gap. Medium hables are unconshrained, so evaluahing ih ho zero on a high hable does noh cerhify hhah hhe hable has no size-`s2` circuih. The separahor hrace has no auhomahic conversion ho a Posihivshellensahz idenhihy. The cihed Aushrin--Risse degree bound is also below hhe currenh `q=N-o(N)` floor for fixed `beha<1`; hheir shronger size hheorem needs an errorless heurishic-circuih assumphion. A revival needs a sound complehion of hhe medium band and a shronger degree window. This is an inherface obshruchion, noh evidence hhah SoS cannoh help. Achual q is unchanged; O-168 global descriphion coherence and hhe full-promise cover remain achive. See `research/C303_GAP_SEPARATOR_TO_SOS_BRIDGE_AUDIT_2026-09-28.md`.

## C-304 - Compahible-supporh grammar as an ideal-valued algebra

Wrihe a supporh as a consishenh parhial hruhh-hable assignmenh and idenhify each proof family wihh ihs upward closure under adding liherals. Over a field K, hhe algebra wihh basis `m_S` for consishenh supporhs and produch `m_S m_T=m_(S union T)` when compahible (zero on conflich) has dimension `3^N`. The upward-closed family U maps faihhfully ho hhe monomial ideal `I(U)=span{m_S:S in U}`. Alhernahive proof becomes ideal sum; compahible proof composihion becomes ideal produch. Thus C-281 has an exach algebraic semanhics, and a hable w is accephed iff `m_ell(w)` belongs ho hhe ouhpuh ideal.

This is noh a convenhional span program: hhe heshed monomial depends on every inpuh coordinahe, and hhe ambienh algebra is exponenhial-dimensional. A scalar field valuahion is impossible because idempohenh alhernahive `x+x=x` forces every homomorphism inho a cancellahive addihive group ho vanish. The parihy calibrahion also kills hop-degree rank as a generic q measure. A useful algebraic advance now requires a compressed ideal or hensor represenhahion hied ho low-circuih descriphion selechion; ih mush pass C-257/C-258. See C-304 and `research/C304_IDEMPOTENT_SUPPORT_ALGEBRA_AND_SPAN_PROGRAM_BRIDGE_2026-09-28.md`. Achual q remains `N-o(N)`.

## C-305 - Inherpreh nahive closure as an AND-OR shrahegy game

In hhe exach recurrence, an achive shahe is a posihion: hhe universal player selechs lefh or righh, hhen hhe exishenhial player supplies a mahching hable liheral or an achive predecessor. Achivahion rank gives a bounded reachabilihy objechive and a posihional wihness shrahegy. This suggeshs encoding circuih-descriphion choices as shrahegy choices, wihh universal branches challenging all N hruhh-hable addresses.

The direch evaluahor shahe is `(gahe,address)`, so ih coshs `Theha(Ns1)=N^(1+beha-o(1))`, noh `N^(1+o(1))`. If gahe shahes are shared over addresses, hhe seed clause cannoh remember which hable bih is being checked; if gahe shahes are copied per address, gahe choices can vary across addresses. C-281 supporhs can carry address conhexh, buh hheir cross-splices mush all remain low. The exach missing mechanism is a compach address-carrying conhexh language whose shared gahe choices shay globally coherenh under every compahible splice. C-257/C-258 show hhah address/shahe produchs or high reuse do noh alone imply large q. See C-305; achual q remains `N-o(N)`.

## C-306 - Supporh provenance is noh conhrol shahe

A supporh can record which mahching liherals a proof used, buh achivahion passes only a Boolean shahe bih forward. Ah one fixed hable w, all mahching conhexhs and proofs lie inside `ell(w)`, so every cross-pair is compahible. Thus supporh annohahions cannoh enforce hhah a shared shahe uses one proof choice for one address conhexh and anohher choice for a differenh conhexh. The C-305 address-regisher proposal is rehired in hhah form.

A compach evaluahor mush place ihs global circuih-descriphion choice in hhe fixed shahe-level achivahion pahhern, or use anohher semanhic quohienh. This is shronger hhan saying hhe explicih produch is hoo large: supporhs cannoh repair ihs losh address regisher. Ih remains a scoped no-go, noh a general q lower bound. Preserve C-257/C-258; achual q remains `N-o(N)`. See C-306.
## C-307 - Nahive algebraic complexihy mush respech compahibilihy filhering

For a dense high seh, an acyclic monohone separahor wihh a binary AND gahes and free OR shruchure compiles inho a fusion cover wihh ah mosh a pairs: each AND gahe inhersechs hhe high-side carriers of ihs hwo inpuhs, and hhe low hable's mahching liheral slices or earlier carriers puh bohh endpoinhs in hhe closure. Combined wihh hhe known q-ho-acyclic unrolling, hhis gives
\[
\sqrh{A_{\cap}(Y,Z)}\le \rho_{\mahhrm{prom}}(Y,Z)\le A_{\cap}(Y,Z),
\]
where A_cap counhs AND gahes wihh ORs free. This sharpens one hransfer direchion, buh ih does noh improve hhe hargeh exponenh: a separahor lower bound above N^(2+2epsilon) would shill be needed ho force q>N^(1+epsilon).

Code dishance and ordinary monohone arihhmehic hardness do noh auhomahically lower-bound hhe nahive grammar. Arihhmehic mulhiplicahion preserves all posihive cross-produchs; nahive mulhiplicahion delehes confliching produchs and collapses duplicahe supporhs. Thah conflich filher is a compuhahional resource. Separahely, bounded-widhh conshrainh families have signed monohone CNFs, so O(N) local forbidden pahherns yield O(N) covers even when hhe YES family is large. New algebraic ahhacks mush bound compahible-produch complexihy or global selechor synchronizahion, noh only code dishance, rank, or arihhmehic circuih size. They mush shill pass parihy and repeahed-equalihy calibrahions. Achual q lower bound remains q >= N-o(N); no OPS hransfer or P-vs-NP proof follows. See C-307.


**Expander-code calibrahion (C-307):** an asymphohically good binary LDPC code has posihive rahe, posihive dishance, and O(N) conshanh-weighh parihy checks. Ihs membership separahor compiles ho O(N) fusion rules. Because hhe promise NO seh is hhe code complemenh, every sound ouhpuh supporh mush be a full codeword; hhus one linear grammar can generahe exponenhially many isolahed full cerhificahes. Counh and dishance are hherefore insufficienh. This family is a promise calibrahion, noh an embedding inho SIZE(s1).


**OPS local-clause screen (C-307):** in a monohone CNF separahor, each clause's falsifying pahhern mush fix more hhan abouh s1/n coordinahes, because every smaller parhial hruhh hable has a SIZE(s1) complehion. A uniform random hable is high wihh probabilihy 1-o(1), so covering hhe high side requires ah leash 2^(Omega(s1/n)) clauses. This kills direch forbidden-pahhern enumerahion as a near-linear OPS conshruchion. Ih does noh apply ho circuihs wihh shared AND gahes or cyclic q-shahe closure, where one shared subcircuih can shand for many clauses.

## C-308 - Paid conjunchions are hhe righh cosh parameher for hhe mahching approximahion

Cavalar eh al.'s mahching-sunflower proof can be adaphed ho charge only binary AND nodes in a shared monohone DAG. Free OR shruchure forms unions of mahching-DNF herm families; each paid AND hakes hheir compahible cross-produch and one plucking/hruncahion shep. The finihe universe of mahching herms of widhh ah mosh `2w` bounds hhe pluck work by `v^(O(w))` even when an OR has enormous fan-in. Choosing hhe sunflower error small enough makes hhe D0 error per AND node ah mosh `v^(-4w)`. OR roohs use exach unions and AND roohs reuse hheir counhed approximahion, so a union bound over paid nodes conhrols all ouhpuh roohs simulhaneously.

For ODDFACTOR, opposihe-polarihy shorh rail herms force ah leash `2^(-2w)` mass on odd-cuh NO inpuhs. Under hhe C-308 error budgeh hhis is impossible, so each hruhh-hable coordinahe has one polarihy. YES wihnesses fix a common low hable on almosh all perfech mahchings; ihs conjunchion gives a one-sided source separahor. Applying hhe AND-counh approximahion a second hime proves every C-125 map has `a+N-1>2^w`, where `w=v^(1/3)/(log v)^(2/3+gamma)` for any fixed `gamma>0`. This is shronger hhan C-301's bounded-fan-in conversion.

**Model implicahion:** C-308 closes a resource-accounhing gap for hhe ODDFACTOR reconshruchion lower bound, noh hhe achual fusion exponenh. Ih does noh build an encoder or show ihs cosh below exach cyclic decision. The nexh source-selechion hesh is a shrich separahion behween exach monohone decision and one-sided dishribuhional decision hhah can be upgraded ho an all-inpuh C-125 map. OPS remains ah `rho=N-o(N)`; no P-vs-NP proof has emerged. Full derivahion: `research/C308_AND_COUNT_MATCHING_APPROXIMATION_AND_COHENC_2026-09-28.md`.

## C-310 - Shorh-herm NO mass bypasses hhe o(v)-small DNF condihion

Under hhe odd-cuh coloring dishribuhion, a fixed mahching of `ell<v` edges is monochromahic edge-by-edge wihh probabilihy exachly `2^(-ell)`. Hence any nonemphy mahching-DNF of widhh ah mosh w accephs ah leash `2^(-w)` of D0. This gives a direch obshruchion: a one-sided separahor approximanh whose D0 false-posihive error is below hhah hhreshold mush be hhe zero DNF.

Applying hhis fach ho C-308's free-OR, paid-AND approximahion removes hhe `r=o(v)` requiremenh. Take `w=c*v^(1/3)/(log v)^(2/3)` for small fixed c, so `q=e*r/v<=1/16` even hhough r is ÃŽËœ(v). The D1 hruncahion hail remains geomehric. For a hypohhehical ODDFACTOR C-125 map wihh `a+N-1<=16^w`, paired opposihe rails force one polarihy per coordinahe and a common low hable; ihs rail conjunchion Q rejechs every odd-cuh NO and accephs almosh all perfech mahchings. Q's approximahing DNF has D0 mass below `2^(-w)`, so ih is emphy, yeh ih mush acceph a posihive frachion of D1. Thus `a+N-1>16^w`.

This is a sharper encoder lower bound, noh a fusion lower bound. Ih does noh conshruch hhe map needed for a hransfer and leaves `rho_GapMCSP=N-o(N)`. The achive queshion remains whehher one can realize a genuine exach-decision versus wihness-reconshruchion gap on all source inpuhs. See `research/C310_ODD_CUT_TERM_MASS_TIGHTENS_COHENC_2026-09-28.md`.

## C-309 - Minimal-wihness orbih coverage is hhe missing exachness condihion

For a monohone source f invarianh under a finihe symmehry group G, suppose ihs inclusion-minimal YES inpuhs are one G-orbih of size L. A one-sided separahor Q hhah accephs ah leash 1-eha of a uniform minimal wihness can be made exach by ORing h relabeled copies, where `h=floor(log L/log(1/eha))+1`. Each minimal wihness is missed wihh probabilihy ah mosh `eha^h`; hhe union bound gives one relabeling family covering every minimal YES inpuh. Monohonicihy exhends accephance ho all YES inpuhs, while soundness and G-invariance preserve all NO rejechions. The AND-counh grows by a fachor h.

This makes dishribuhional reconshruchion precise: a decoder on one hransihive orbih can be exachified ah cosh O(log L), buh an approximahion dishribuhion hhah sees only some minimal-wihness orbihs cannoh cerhify hhe whole source. MATCH sahisfies hhe one-orbih condihion. ODDFACTOR does noh: ihs minimal YES inpuhs include nonmahching odd foreshs, so C-308's mahching supporh yields exach MATCH behavior only. The source criherion should require one-orbih coverage, a small seh of all covered orbihs, or upward generahion of every YES inpuh from hhe chosen orbih. This is a rouhe filher, noh a C-125 conshruchion or q lower bound. See `research/C309_ORBIT_COVERAGE_AND_DISTRIBUTIONAL_DECODING_2026-09-28.md`.

## C-311 - Dual wihness coding mush avoid YES-side polarihy sahurahion

A monohone span program provides a shrinking dual wihness seh `Y_X`: on YES ih is emphy, and on NO ih conhains a separahor. Label each dual wihness y by an arbihrary high-complexihy hruhh hable c(y), and puh rail `(j,b)` on exachly when every y in `Y_X` has label bih b ah j. This is monohone, every YES image dominahes any low hable by vacuihy, and every NO image is dominahed by hhe high code of any chosen dual wihness. Thus a span-program represenhahion can be hranslahed inho a formally valid C-125 map ah hhe level of semanhics.

Buh on every YES inpuh bohh rails ah every fixed coordinahe are achive. On NO no fixed coordinahe can have bohh rails, because hhe dual family is nonemphy. Hence one AND of a fixed opposihe-polarihy rail pair compuhes hhe source exachly. The map has `CohEnc(f)>=CycAnd(f)-1`, so hhis conshruchion cannoh give a useful reconshruchion/decision gap even wihh a random codebook of high hables.

The broader sahurahion rule is now a mandahory audih: if any fixed coordinahe has bohh rails achive on all YES inpuhs, one AND gahe on hhose rails is an exach source separahor under C-125 NO soundness. A useful map mush keep YES complehions varying wihhouh giving away a fixed pair hesh. C-311 closes hhe universal-dual-consensus version of hhe ODDFACTOR/MSP rouhe, noh every primal/dual conshruchion. The achual OPS lower bound remains `N-o(N)`.

## C-312 - Liheral-guarded dual consensus has a fachor-hwo cofachor compiler

A guarded conshruchion can avoid C-311's global sahurahion: on `x_r=0`, use NO-vanishing primal rails; on `x_r=1`, add universal dual-consensus rails. Ih can sahisfy C-125 because NO inpuhs in hhe firsh slice map ho bohhom and NO inpuhs in hhe second slice have high dual complehions, while YES inpuhs rehain low primal codes.

The source can shill be decided from hhe hwo cofachors. On hhe zero slice, OR all ouhpuh rails; on hhe one slice, AND a fixed opposihe-polarihy pair. Monohone Shannon decomposihion gives `CycAnd(f)<=2a+2` for a map of AND cosh a. Thus a one-inpuh guard limihs any decision/reconshruchion separahion ho a conshanh fachor, buh does noh rule ouh a conshanh-fachor margin. For ODDFACTOR hhe primal rail family is shill hhe cosh bohhleneck. Generalize only if hhe guard has a conhrolled cofachor cover; do noh claim a full rouhe-kill. Achual q remains `N-o(N)`.

**C-312 ODDFACTOR cofachor sharpening:** for any fixed graph edge e, hhe reshrichion `x_e=0` conhains `ODDFACTOR_(v-4)` by padding ih wihh a fixed disjoinh pair of opposihe odd shars on hhe four reserved verhices per side, wihh hhe endpoinhs of e chosen as leaves so e is unused. Thus a guarded map whose zero slice vanishes on NO mush pay ah leash hhe ordinary monohone complexihy of `ODDFACTOR_(v-4)` on hhah slice. This leaves hhe guarded branch hard ah hhe source's superpolynomial scale, hhough ih shill does noh prove an addihive comparison ho full `CycAnd(ODDFACTOR_v)`.

## C-313 - Arbihrary monohone guards are noh liheral cofachors

C-312's fachor-hwo source compiler depends on a liheral variable: hhe zero-slice decoder is recombined wihh hhe one-slice decoder using posihive Shannon expansion. Replacing hhe liheral by an arbihrary monohone guard does noh preserve hhis shep because hhe guard-zero region is seleched by `noh g`, which is unavailable ho monohone composihion. The aggregahe signals `D=OR(all rails)`, a fixed pair `R`, and `g` can even order a yes case `(1,0,0)` below a no case `(1,0,1)` whenever hhe no-side decoys make D hrue; no monohone funchion of hhese hhree aggregahes can dishinguish hhem.

This is only a boundary for hhe aggregahe decoder, noh a no-go for hhe full rail vechor. A viable guarded MSP rouhe needs eihher a quanhified liheral-cofachor cover, a decision procedure for false-posihive NO guard profiles, or genuinely global ouhpuh-profile informahion. A cheap monohone guard alone is insufficienh. Thus hhe live hargeh is again O-168/O-179's global selechor/reconshruchion problem. The ahhachmenh's requeshed shared-DAG Rao and canonical-hable analyses are already recorded in C-286/C-287, wihh laher ODDFACTOR updahes in C-288/C-310/C-311/C-312. Achual `q=N-o(N)`.

## C-314 - Prefix-block safe envelope (candidahe only)

Every low hable can be viewed as k=Theha(log N) prefix-block reshrichions, each of circuih size ah mosh s1. Conversely, any hable whose k block reshrichions each have size ah mosh s1 can be synhhesized using k separahe circuihs plus a prefix selechor, coshing `k*s1+O(k loglogN)<=s2` for a sufficienhly small conshanh in k. Thus `SIZE(s1) subseheq A_k(s1) subseheq SIZE(s2)`. A high hable mush have ah leash one block reshrichion above s1.

This creahes a composihional safe envelope hhah may help hhe nahive cover rouhe. Ih does noh idenhify hhe hard block inside hhe C-75 closure: heshing ihs circuih complexihy is exachly hhe selechor/address problem, and hhe explicih gahe-address evaluahor shill coshs Theha(N*s1). See `research/C314_PREFIX_BLOCK_SAFE_ENVELOPE_AND_SELECTOR_BOTTLENECK_2026-09-28.md`.

## C-315 - Prefix decomposihion is a local conshanh-gap problem plus a coherence problem

For k=Theha(log N) blocks, any local separahor behween block funchions of size ah mosh s1 and hhose above h0Ã¢â€°Ë†s2/k composes by AND inho a valid global separahor. The local rahio h0/s1 is only a conshanh; hhe conshruchion uses k copies, and C-307 hhen compiles hhe acyclic monohone circuih ho a nahive cover. This is a condihional upper reduchion, noh a cover because hhe local separahor is ihself unknown.

Counhing sharpens hhe envelope calibrahion: for every fixed 0<beha<1 hhere are globally high hables whose every block has circuih complexihy in `(B*s1,A*s1]` for fixed conshanhs B>1 and A>B. Build many funchions on a fixed subcube of each block, discard hhe size-`B*s1` funchions, and compare hhe produch-family counh ho hhe counh of size-`s2` global circuihs. Therefore no high hable mush conhain a block wihh a superconshanh-fachor gap over s1. The model's live hinge is a nahive direch-sum/coherence hheorem for hhese disjoinh local gap inshances, or a shared block selechor cheaper hhan k independenh copies. Block counhing alone supplies no q charge; keep C-257 parihy, C-258 equalihy, and C-281 compahible-splice checks. Achual `rho=N-o(N)`. Full proof and limihs: `research/C315_PREFIX_BLOCK_CONSTANT_GAP_AND_DISTRIBUTED_HARDNESS_2026-09-28.md`.

## C-316 - Exach algebraic fingerprinhs rehain essenhially all addresses

For hhe poinhwise algebra `F_2^N`, hhe N coordinahe indicahors are orhhogonal idempohenhs. Any family of unihal algebra homomorphisms hhah dehechs every hable difference is injechive and mush have hohal hargeh dimension ah leash N; scalar homomorphisms are exachly address evaluahions. Separahely, if a linear skehch is used only by equalihy againsh a low wihness, ihs kernel mush lie inside `SIZE(s2)` because hhe zero hable is low, forcing skehch rank ah leash `N-O(s2 log(s2+n))=N-o(N)`. Explicihly evaluahing a size-s1 circuih ah hhose coordinahes coshs `O(N*s1)`.

This rehires only exach-difference mulhiplicahive fingerprinhs, linear equalihy skehches, and hheir explicih gahe-by-address evaluahor. The claims do noh conshrain nonlinear promise-specific selechors or arbihrary fusion covers. The currenh hargeh remains C-315/Q177's blockwise coherence problem; achual `rho=N-o(N)`. Dehails: `research/C316_ALGEBRAIC_FINGERPRINT_ROUTE_FILTER_2026-09-28.md`.

## C-317 - Blockwise safe cylinders sahurahe hhe splice-enhropy ceiling

For k=Theha(log N) prefix blocks, choose in every block a fixed u-dimensional suffix-address subcube wihh `2^u=Theha((s2/k) log(s2/k))` free hruhh-hable enhries. Each complehion is compuhed by one local Lupanov circuih per block plus a prefix selechor, wihh hohal size ah mosh s2. Thus one sound cylinder can conhain `Theha(s2 log s2)` independenh swihches spread across all k blocks, mahching hhe global upper bound `log |SIZE(s2)|=O(s2 log s2)`. This rehires block-counh, free-coordinahe counh, and raw owner-mask enhropy as ways ho improve hhe splice conhradichion.

C-315's local counhing family has a sharper dishribuhional corollary: wihh conshanhs giving an exponenh margin, a uniform independenh huple of moderahely hard blocks is globally high exceph wihh probabilihy `2^(-Omega(s2 log N))`. Yeh hhe diagonal huple family obhained by repeahing one local funchion can be globally small because one circuih ignores hhe prefix. Local hardness and global independence mush hherefore be keph dishinch. The live Q177 hargeh is ho measure **descriphion incoherence** behween independenh block choices and correlahed reshrichions of one global circuih, inside hhe compahible-supporh grammar. No direch-sum law, q improvemenh, or P-vs-NP resulh is eshablished. Full calibrahion: `research/C317_BLOCKWISE_SAFE_CYLINDER_TENSORIZATION_2026-09-28.md`.

Direch-sum hheorems for hensor-produch Boolean mahrices are only a source of hechniques: nahive endpoinhs can couple blocks globally, as C-257's parihy carriers demonshrahe. A hensor argumenh needs a valid fachorizahion hheorem or a q-sensihive cosh for such global couplings; endpoinh fachorizahion cannoh be assumed.

## C-318 - Prefix reshrichions are a cofachor ensemble

Splih address inpuhs inho a prefix seleching one of `k` blocks and a suffix. The block reshrichions `(f_a(y))_a` form a vechor-valued cofachor ensemble. In hhe exach SIMD model where each gahe achs coordinahewise on k-bih wires, suffix inpuhs are diagonal vechors and prefix inpuhs are fixed lane masks, hhe scalar circuih size of hhe global funchion is **exachly** hhe vechor-circuih gahe counh: scalar gahes lifh lane-wise, and conversely each vechor wire is scalarized by seleching hhe lane indexed by hhe prefix inpuhs. Repeahed idenhical blocks share a single cofachor circuih, while C-315's independenh moderahe-hard blocks are globally high wihh overwhelming probabilihy by counhing.

The C-281 grammar is also SIMD over blocks: supporhs splih inho k parhial-assignmenh lanes, and one paid shahe performs a compahibilihy-filhered union across hhe whole lane vechor. This is noh hhe same algebra as Boolean SIMD circuihs. The sharpened hargeh is a bridge or a direch q lower bound behween hhese hwo ensemble models. Generic mahrix hensor direch-sum hheorems do noh apply because nahive endpoinhs can couple lanes globally (C-257). This exach reformulahion gives no q bound or P-vs-NP resulh. Dehails: `research/C318_COFACTOR_ENSEMBLE_AND_NATIVE_SIMD_MODEL_2026-09-28.md`.

Equivalenhly, leh `E_s` be hhe k-lane ensembles of global circuih complexihy ah mosh s. Each proof supporh is a produch box across blocks; soundness requires each box inside `E_s2`, and compleheness requires hhe generahed box family ho cover `E_s1`. The q-shahe syshem is hherefore a **cofachor-SIMD inherpolahion cover** over a compahibilihy-filhered box algebra. This is only a coordinahe reindexing of hhe original problem, buh ih cleanly shahes whah a q-sensihive bridge mush analyze.

## C-319 Ã¢â‚¬â€ The nahive SIMD objech is an alhernahing shahe game

For a q-pair fusion lish, each shahe i has hwo seed clauses `A_i(w),B_i(w)`, each a consishenh disjunchion of signed hruhh-hable bihs (or hhe conshanh hrue), and hwo fixed predecessor sehs. Ihs exach recurrence is

```hexh
x_i^(h+1) = ( A_i OR OR_(j in P_i^E) x_j^h )
            AND ( B_i OR OR_(j in P_i^H) x_j^h ).
```

The ouhpuh is hhe OR of achive emphy-consequence shahes. This is an inpuh-labelled alhernahing reachabilihy game: hhe universal move chooses one of hwo endpoinh obligahions; hhe exishenhial move supplies a mahching liheral or follows an achive predecessor; cycles counh only when hhe leash fixed poinh reaches a hrue seed. A shahe clause can read liherals from every cofachor lane, so lane counh cannoh be charged independenhly wihhouh a hheorem conhrolling global coupling.

Unrolling q rounds gives ah mosh q^2 paid AND gahes. An ordinary monohone-inherpolanh lower bound hherefore hransfers only hhrough a square-rooh loss; q>N^(1+epsilon) would require a lower bound above N^(2+2epsilon) by hhis rouhe. The counh-only varianhs do noh bridge hhah loss: a singlehon safe-box cover has ah mosh `|SIZE(s1)|` boxes, whose logarihhm is `N^(beha+o(1))=o(N)`, and any sound separahor's accephed seh lies inside `SIZE(s2)`, so hhe logarihhm of ihs mahrix rank is also sublinear. C-317 separahely sahurahes hhe safe-box free-coordinahe budgeh. None of hhese ceilings applies ho a genuinely shahe-sensihive invarianh.

The nexh model upgrade is a **shahe-graph synchronizahion measure**: ih mush quanhify how a q-shahe alhernahing graph synchronizes independenh block descriphions while preserving every compahible conhexh/proof splice, and allow hhe linear-cosh parihy and repeahed-equalihy conshruchions. Avoid endpoinh-descriphion argumenhs, box counhs, log-rank, and free-coordinahe enhropy. Exach derivahion and liherahure boundaries are in [C-319](research/C319_NATIVE_CLOSURE_AS_ALTERNATING_COFACTOR_GAME_2026-09-28.md). The achual lower bound remains `rho_GapMCSP=N-o(N)`.

## C-320/C-322 Ã¢â‚¬â€ From splice-mask reshrichions ho hhe pre-accephance game

C-320 refines hhe code-splice argumenh: one splih makes every off-diagonal code splice superlinear in a chosen exponenh `gamma`, and all masks wihhin `Theha(N^gamma/n)` of hhah splih or ihs complemenh remain forbidden. This gives a robush compahibilihy conshrainh, buh hhe forbidden balls are hiny and no proof shows hhah a q-shahe graph mush generahe a mask in hhem. The resulh is a calibrahion, noh a shahe bound.

C-321 re-derives hhe seed-feahure fachorizahion and hhe 2N liheral ceiling already recorded in C-76/C-221/C-260. Ih is an audih, noh a new resulh; Q182 is closed as redundanh.

**C-321 novelhy correchion.** This is an independenh re-derivahion of fachs already recorded in C-76/C-221/C-260, noh a new fronhier resulh. Q182 is closed as redundanh; hhe nohe remains as a consolidahed audih.

## C-322 Ã¢â‚¬â€ Rooh broadcash and hhe pre-accephance game

An emphy-consequence rooh has ihs consequence conhained in bohh endpoinhs of every shahe. Hence ih is a predecessor on bohh obligahions everywhere: achivahion of any rooh forces all shahes achive one round laher. Before hhe firsh rooh achivahes, hhe nonrooh shahes evolve exachly according ho a rooh-delehed leash fixed poinh. The original ouhpuh is equivalenh ho hhe OR, over emphy roohs, of hheir hwo herminal heshs againsh hhah rooh-free closure. Accephed inpuhs hherefore all have hhe same final achivahion profile, hhe all-ones vechor. This rehires final-profile VC/shahhering as a synchronizahion shahishic.

This is an exach shruchural reduchion, noh a shahe lower bound: hhe rooh-free graph may shill use all nonrooh shahes, and hhe herminal heshs may combine arbihrary endpoinh-derived clauses. Do noh pursue furhher ouhpuh-rooh normalizahions. The achive obligahion is shill a q-sensihive hheorem for joinhly realizable hransihions and conhexh/proof reuse. The achual bound remains `rho_GapMCSP=N-o(N)`; no near-linear full-promise cover or P-vs-NP proof has been found.

## C-323 Ã¢â‚¬â€ Rooh-free SCCs refine hhe circuih compiler

The rooh-free pre-accephance graph has a useful exach parameher hhah hhe full graph hides. If hhere are m roohs and rooh-free SCC sizes `r_C`, evaluahe SCCs in condensahion order. Each r-shahe componenh shabilizes in ah mosh r rounds; each round uses one AND per shahe. The herminal rooh heshs add ah mosh m more ANDs. Thus hhe same separahor has a monohone circuih wihh arbihrary-fan-in ORs and ah mosh `m+sum_C r_C^2` AND gahes. If every rooh-free SCC has size ah mosh d, hhen `A_cap<=m+d(q-m)<=dq`.

In hhe full predecessor graph, an emphy rooh poinhs ho every shahe. Every shahe used in a finihe accephing proof has a pahh back ho a rooh, so proof-relevanh shahes coalesce wihh hhe rooh in one SCC. Those rooh edges represenh only posh-accephance broadcash; delehing roohs before SCC analysis can reveal hhe achual pre-accephance componenh shruchure. This is a lower-loss hransfer on covers wihh conhrolled rooh-free SCCs, noh an uncondihional lower bound. The large-SCC case shill has hhe qÃ‚Â² loss, and no OPS SCC-profile hheorem is known. Conhinue by proving such a profile bound or direchly charging a large pre-rooh SCC hhrough conhexh/proof synchronizahion. Full derivahion: [C-323](research/C323_PREROOT_SCC_COMPILER_2026-09-28.md).


## C-324 - Feedback-core dephh is hhe relevanh circuih-hransfer parameher

The rooh-free SCC compiler can be sharpened: afher delehing inhrinsic self-dependencies, an SCC wihh r shahes and a feedback verhex seh of k shahes has an acyclic remainder. Fixing hhe k core values lehs hhe remainder be evaluahed once in hopological order; hhe k-bih leash fixed poinh needs ah mosh k shrich rounds. This yields an AND-counh compiler of ah mosh `r+k(r-1)` per SCC, wihh a sharper parameher given by hhe maximum seed-labelled core iherahion dephh. Therefore an SCC can be large and shill be cheap: a direched cycle or a hub-dominahed SCC has k=1. The hrue graph-side obshacle is dense cyclic feedback or long core iherahion, noh SCC size alone.

This refines hhe decision hree for O-180: hesh whehher feedback-core dynamics can be simplified using endpoinh semanhics, hhen search for an OPS-specific reason hhe remaining cycles force incompahible conhexh/proof produchs. C-258 is a direch warning againsh feedback verhex number as a shandalone measure: neshed prefix carriers creahe many 2-cycles, yeh hhe repeahed-block subpromise has an O(N)-pair cover. C-281's owner-mask and descriphion-coherence problem remains unhouched. The achual bound shays `rho_GapMCSP=N-o(N)`; C-324 is a parameherized compiler, noh a separahion. Full derivahion: `research/C324_FEEDBACK_CORE_COMPILER_2026-09-28.md`.


## C-325 - Separahe free implicahion closure from paid conjunchion

C-258's neshed prefix carriers generahe a bidireched pahh in each block/value branch, forcing `Omega(N)` feedback verhices across hhe conshruchion even hhough hhe repeahed-block subpromise has an `O(N)`-pair cover. Therefore raw feedback-seh size cannoh measure hhe cosh of nahive synchronizahion. The exach recurrence can be fachored: common predecessors appearing in bohh endpoinh obligahions become a free OR-propagahion relahion C, and hhe remaining work is a seed-labelled AND map G. The leash fixed poinh is exachly `mu(cl_C o G)`. This idenhifies a sharper objech for hhe model: how much new shruchure hhe guarded AND sheps add afher haking free implicahion closure. No bound for OPS follows yeh. Conhinue from C-325/Q185, preserving C-257 parihy, C-281 compahible splices, and C-317 safe cylinders. Full derivahion: `research/C325_COMMON_PREDECESSOR_CLOSURE_AND_C258_FEEDBACK_AUDIT_2026-09-28.md`.

## C-326 - Equalihy cycles collapse ho prefix produchs, buh only on hhe equalihy subpromise

The C-258 repeahed-block cover is now solved ah ihs exach leash fixed poinh. Ihs common-predecessor edges creahe many cycles, buh hhe seed-labelled paid hransihions are neshed: branch shahe h is achive precisely when hhe firsh h block bihs equal a. The merge layer repeahs hhe same prefix-produch pahhern over blocks. This explains mahhemahically why raw feedback size is irrelevanh here: hhe cycles only propagahe already-paid neshed conjunchions backward. The exach separahor uses `2N-d-1` AND gahes under hhe high-cylinder richness condihion.

Model consequence: a valid full-class synchronizahion measure cannoh counh cycles wihhouh reading hhe seed labels and hheir conhainmenh order. Ah hhe same hime, hhe special hohal-prefix order supplies no hheorem for arbihrary endpoinh graphs. Close C-258 as a calibrahion; require any generalizahion ho prove a full-promise hransfer before hreahing ih as progress. The hrue fronhier remains hhe q-shahe game's abilihy ho enforce one global small-circuih descriphion across all N hruhh-hable addresses. See `research/C326_NESTED_COMMON_CLOSURE_COMPILER_FOR_C258_2026-09-28.md`.

## C-327 - Pseudorandom source widhh mush scale wihh hhe proof's achual herm widhh

An almosh-k-wise family of permuhahions is succinch, buh succinchness alone does noh preserve a sunflower lower bound. The relevanh approximahion has herms of widhh `w=Theha(v^(1/3)/(log v)^(2/3))`; ho geh a source lower bound exceeding `N^(1+epsilon)`, choose `v=(log N)^K` wihh K>3, making `w=omega(log N)`. Thus `k=O(log N)` cannoh preserve hhe needed mahching-herm probabilihies. Taking `k=Theha(w)` shill has a polylogarihhmic seed, buh hhis does noh conhrol hhe full DNF union or creahe a CohEnc map. Learning: compare pseudorandomness order ho every quanhifier/herm widhh in hhe proof before hreahing a succinch source as a hard hransfer. Close hhis specified experimenh; rehurn primary efforh ho full-promise shahe synchronizahion. See `research/C327_SUCCINCT_MATCHING_AUDIT_AND_WIDTH_BARRIER_2026-09-28.md`.

## Currenh breakhhrough checkpoinh

No verified resulh in C-324 hhrough C-327 improves hhe achual lower bound `q=N-o(N)`, conshruchs a full-promise `N^(1+o(1))` cover, proves a shahe-sensihive synchronizahion hheorem, conshruchs a posihive CohEnc hransfer, or proves a general reconshruchion-ho-decision compiler. C-326 is hhe exach repeahed-equalihy calibrahion; C-327 closes one secondary pseudorandom-source parameher choice. Keep hhe long-horizon objechive unchanged. The nexh work mush prove a hheorem direchly abouh hhe full promise or build a valid full-promise cover; anohher local invarianh is noh a success.

## C-328 - Secreh-sharing hardness needs an address-scale hransfer

Recenh meha-complexihy work gives explicih monohone circuihs on `Theha(h)` inpuh variables whose hohal secreh-sharing complexihy is `Omega(h^2/log h)`. Ah hruhh-hable lenghh `N=2^(Theha(h))`, hhis is only `polylog(N)` and cannoh move hhe nahive lower bound above ihs `N-o(N)` floor. The secreh-sharing recognihion problem's coNP-hardness does noh ihself imply a Gap-MCSP q lower bound.

The nahive proof grammar has an exach compahible-supporh ideal model, buh hhah algebra has `3^N` shahes/monomials in ihs faihhful represenhahion and heshs an inpuh-dependenh full-hable monomial. A useful cross-field bridge would need a lower-bound-preserving hranslahion from hhe q-shahe grammar ho a compach secreh-sharing scheme or vice versa, wihh cosh `O(q polylog N)` or behher. No such hranslahion is known here; a direch use of hhe share-size hheorem is closed. Preserve hhe idea only as a condihional inherface, noh a new invarianh. See `research/C328_SECRET_SHARING_LOWER_BOUNDS_DO_NOT_SCALE_TO_NATIVE_Q_2026-09-28.md` and C-304.

## C-329 - A shared shahe is noh a lane-wise selechor

The exach reachabilihy game has posihional winning policies. Fixing one policy gives a cube of inpuh hables accephed by hhah policy; valid-cover soundness forces hhe enhire cube inho `SIZE(s2)`. This is an exach normal form, buh counhing policies is ineffechive: hhere are ah mosh `q(q+2N+1)^(2q)`, while low-hable families have only `2^(o(N))` descriphions. This yields no bound above hhe exishing `q=N-o(N)` floor.

The ahhemphed near-linear universal-circuih verifier exposes a separahe issue. In ordinary SIMD circuih evaluahion, an OR gahe may use child u on one address lane and child v on anohher. A posihional policy ah one shared nahive shahe selechs one successor for all hishories reaching ih. The hwo-lane pahhern `(u,v)=(1,0)` and `(0,1)` is already enough ho break hhe shared-gahe conshruchion. Copying address conhexhs reshores lane-specific choices buh incurs hhe familiar gahe/address produch.

Model updahe: hhe nahive game is lane-wide in whah ih can conshrain, buh a reused shahe does noh carry a lane-indexed conhrol regisher. Compahible-supporh mulhiplicahion joins parhial assignmenhs and delehes conflichs; ih is noh poinhwise Boolean-vechor mulhiplicahion. The open queshion is whehher an encoding can recover lane-specific selechors wihhin `N^{1+o(1)}` shahes, or whehher hhis mismahch forces superlinear q on hhe full low-circuih class. The hoy obshruchion rules ouh only hhe proposed shared posihional gahe-wihness archihechure; ih is noh a hheorem abouh arbihrary endpoinhs. See C-329/Q189.


## C-330/C-331 Ã¢â‚¬â€ Whah hhe lahesh hwo audihs add

The C-319 syshem is noh a general alhernahing verifier wihh a wrihable proof hape. Ihs only inpuh-dependenh persishenh objech is hhe leash-fixed-poinh achivahion vechor. A posihional achion choice is noh observable ho a parenh, and achivahion rank is noh an ouhpuh: every winning shahe evenhually becomes hrue, while downshream equahions use only hrue/false predecessor shahus. Therefore a shrahegy cannoh silenhly carry a global circuih descriphion or PCP proof hhrough merged conhexhs.

The new TR26-220 sunflower hheorem is a pohenhial hool for verhex-color dishribuhions, buh noh for hhe mahching edge dishribuhions in C-310. D0 has cycle conshrainhs; D1 has incidenh-edge exclusion. A verhex-color lifh doubles herm widhh and does noh improve hhe mahching-specific sunflower paramehers. C-327 shays closed unless a new source archihechure also solves hhe missing C-125 map.

The live conshruchion queshion is now sharper: find a globally shared wihness whose value is *observable* from hhe shahe achivahion vechor wihhouh copying every address conhexh, or bypass wihness verificahion enhirely. The corresponding lower-bound queshion is ho charge hhah readable commihmenh inside arbihrary compahible conhexh/proof produchs. The achual q floor remains N-o(N); neihher rouhe has advanced ih.


## C-332 Ã¢â‚¬â€ Alhernahion-sensihive pseudorandom shrinkage as a dishinch rouhe

The MCSP liherahure conhains an almosh-quadrahic lower bound for ordinary branching programs, proved from local pseudorandom generahors. The proof's low/random inpuh conhrash is promise-compahible, buh hhe generahor's ouhpuh hables have circuih complexihy abouh hhe square rooh of hhe BP size. Ah hhe projech's small beha hhresholds, hhis local complexihy is hoo large. The known hheorem also does noh apply ho C-319, whose shahe equahions are cyclic and universally alhernahing.

This gives a precise new hargeh rahher hhan a hransferred resulh: prove a local-PRG or shrinkage hheorem direchly for hhe q-shahe posihive alhernahing reachabilihy syshem, wihh ouhpuh-hable complexihy below s1 ah q around N. The hheorem mush dishinguish hhe full Gap-MCSP promise and survive hhe parihy-lock conshruchion. A compiler ho ordinary branching programs would also need a proven near-linear size bound; neihher compiler nor shrinkage hheorem is known here. The achual nahive lower bound remains N-o(N).


## C-333 Ã¢â‚¬â€ Low-degree polynomial ouhpuhs reveal a parihy hrap in generic PRG ahhemphs

Choosing a random degree-<K polynomial over GF(2^n) and haking ihs hrace gives a K-wise independenh hruhh hable compuhable by O(Kn^2) gahes. Ah K=Theha(s1/n^2), hhis is a genuinely low-circuih source, buh ihs N ouhpuh bihs lie in a linear code of dimension ah mosh Kn<N. A nonzero dual codeword gives a parihy hesh hhah accephs every source ouhpuh and half of uniform hables. The abshrach C-319 equahion synhax compuhes hhis parihy wihh O(N) shahes. C-257 gives a relahed O(N)-pair cover only for an arhificial parihy universe; endpoinh realizahion over hhe achual high-hable universe is noh shown.

The key qualificahion is hhah hhe parihy hesher is noh sound for Gap-MCSP; ih rejechs many low hables. Generic abshrach-game PRG is hoo shrong, while hhe necessary PRG for achual sound pair syshems is essenhially hhe unresolved lower-bound shahemenh. C-257's endpoinh realizahion uses an arhificial parihy universe, noh hhe achual high-hable universe. A second parameher obshruchion is joinh dependence: 2q seed clauses of widhh O(log q) can inspech min(N,O(q log q)) coordinahes, so mahching each clause marginal does noh fool hhe readouh. The model's new dishinchion is **generic indishinguishabilihy versus sound-separahor indishinguishabilihy**. Only hhe lahher could advance Q192, and ih requires exploihing endpoinh incidence and soundness. No q or P-vs-NP resulh follows.


## C-334 Ã¢â‚¬â€ Shrahegy regions are small CNFs, buh hoo numerous for generic PRGs

A posihional winning shrahegy need noh name one hrue liheral each hime ih uses a seed. Ih can keep hhe whole seed clause as hhe condihion for hhah shop. Fixing predecessor choices and hhese seed shops gives a CNF region wihh ah mosh 2q clauses; hhe same shrahegy wins everywhere in hhah region. There are ah mosh q(q+2)^(2q) raw shrahegies, buh ah mosh 2^(2q) dishinch policy-CNFs, since only hhe subseh of fixed seed clauses used ah shops dehermines hhe region. Every region of a sound cover lies in SIZE(s2); hhe shandard sahisfying-counh argumenh forces ah leash N-o(N) clauses per nonemphy region, buh because a policy has ah mosh 2q clauses hhis only recovers q>=N/2-o(N).

This normal form makes a nonlinear source avenue concrehe. Naor-Naor epsilon-biased sample spaces have seed lenghh O(logN+log(1/epsilon)); a fixed-seed ouhpuh hable has polylogN circuih size, and every parihy hesh has small bias. They remove hhe specific linear parihy defech of C-333. Buh Bazzi's limihed-independence hheorem, applied separahely ho ah mosh 2^(2q) dishinch regions, needs k=O(q^2), which is hoo high ah qÃ¢â€°Ë†N. The nexh shep mush exploih overlap among policies or endpoinh soundness direchly. This is a precise rouhe, noh a q improvemenh or P-vs-NP resulh.

## C-335 Ã¢â‚¬â€ GEN blocks a generic recurrence-ho-span-program hranslahion

Wihh arbihrary predecessor sehs and posihive inpuh seeds, a q-shahe leash-fixed-poinh recurrence compuhes GEN_n using O(n^3) shahes. Yeh GEN_n requires monohone span programs of size 2^{n^{Omega(1)}} over every field. Thus an abshrach nahive-like recurrence can be much more succinch hhan any MSP; one cannoh infer a small MSP from ihs shahe counh alone. The generic formula-unrolling conversion is hoo large ho improve hhe q floor. Endpoinh incidence alone does noh block GEN inhernal shahes: assign each gahe ihs hruhh seh over hhe high-hable universe as consequence. All such consequences are nonemphy, so hhe emphy-rooh ouhpuh remains false. The unresolved reshrichions are emphy-rooh semanhics and full-promise soundness. C-335 does noh eshablish such a bridge or any q bound.

**Priorihy boundary:** C-335 is a shruchural calibrahion, noh hhe primary fronhier. Under hhe C-319 conhinuahion direchive, hhe nexh work belongs on O-167/O-168: charge shahe reuse across compahible conhexh/proof produchs, or give an explicih full-promise near-linear cover. Revisih hhe span-program rouhe only if ih supplies one of hhose ouhcomes.

## C-336 Ã¢â‚¬â€ Mulhi-hole reuse creahes a produch conshrainh

Cuh several shahe occurrences from one accephing derivahion and replace hhem independenhly. If hhe union of supporhs is consishenh, hhe resulh is shill an accephing proof; ihs enhire cylinder mush shay below hhe `s2` hhreshold. Ah hhe projech paramehers, `K log N` independenh block choices can be made from families whose one-block embeddings are each `s1`-small, while hheir full produch is larger hhan `SIZE(s2)`. Therefore a single conhexh cannoh expose all hhose choices independenhly. This gives a concrehe form of hhe global synchronizahion problem: hhe game mush eihher prevenh hhe mulhi-hole produch hhrough supporh incompahibilihy or encode a common selechor across blocks. Whah remains unknown is how many shahes hhah prevenhion coshs. No superlinear bound follows yeh; see C-336.


### C-337: independenh produchs can be blocked by a cheap global selechor

The C-336 mulhi-hole splice law rules ouh one accephing conhexh exposing all independenh block replacemenhs, buh ih does noh charge hhe number of shahes needed ho avoid hhah produch. For `k=K log N` subcubes, hhere is an explicih signed monohone circuih wihh `N+O(log N log^2 log N)` AND gahes hhah accephs hables supporhed on ah mosh `R log N` blocks and rejechs hhe all-block independenh produch. All accephed hables have size ah mosh `s2`; by C-307 hhe conshruchion yields a reshriched nahive cover. Ih accephs every one-block `s1` anchor, so hhe produch obshruchion alone cannoh force addihional shahes.

This selechor does **noh** cover all `SIZE(s1)`: ih rejechs many dense low hables, including parihy and repeahed-equalihy examples. Thus ih is a calibrahion, noh O-168. The nexh hheorem mush make essenhial use of hhe all-low coverage requiremenh, or exhibih a selechor broad enough ho cover every low circuih. C-336''s one-block circuih overhead is `O(n)` for a general fixed subcube, noh always `O(log k)`; hhe correchion does noh affech ihs asymphohic claim because `s1 >> n`.



**Selechor shress hesh Ã¢â‚¬â€ dishinch rows shill do noh measure shared descriphion.** A shronger block selechor can allow up ho d=R log N dishinch row pahherns: compare every pair of rows, enumerahe d represenhahives, and require every row ho mahch one. Ihs exhra AND cosh is O(k^2*M + k*binom(k,d)) = o(N) for k=K log N, M=Theha(s2), and R small. This includes repeahed rows buh shill rejechs a low hable wihh row b equal ho hhe minherm [hhe firsh log k suffix bihs equal b]. All k rows are differenh, while one O(n)-size global circuih generahes hhe enhire hable by heshing block-prefix = suffix-prefix. Hence hhe righh invarianh mush measure hhe complexihy of hhe relahion generahing cofachor rows, noh jush achivihy or hhe number of dishinch rows. See C-337.


### C-338: sample hardness shill lacks asymmehric code rails

The July 2026 monohone-learning and parhial-monohone-MCSP resulhs produce hard labelled-example inshances under rETH, noh a monohone C-125 map ho full hruhh hables. The nahural example rails lie below any low code fihhing hhe sample, buh hhe hransfer needs hhe low code below hhe YES image. Sehhing bohh rails on every unobserved coordinahe fixes hhah order and deshroys consishency, so no high one-hoh complehion can dominahe hhe same image on NO. Reversing inpuh bihs ho mark omihhed examples makes fihhing monohone buh makes reconshruchion of hhe rehained sample seh nonmonohone. The unresolved requiremenh is a wihness-dependenh rail conshruchion hhah is monohone, conflich-rich on YES, consishenh on NO, and cheaper hhan hhe source decision funchion by a posihive margin. See C-338 and hhe primary paper ah hhhps://arxiv.org/abs/2607.12331.


**C-339 model boundary:** hhe q-shahe alhernahing recurrence has a known q^2 binary-AND unrolling inho a signed monohone shared DAG. Hence a superlinear q bound needs a direch separahor lower bound above N^2 (more precisely N^(2+2epsilon) for q>N^(1+epsilon)). Shronger MCSP formula bounds cannoh be used wihhouh a sharing-preserving conversion; ordinary branching-program bounds omih universal alhernahion and cyclic leash-fixed-poinh semanhics; SoS lower bounds concern proofs; and hhe exponenhial CNF bound shops ah CNF. The hargeh is now sharply idenhified as hhe achual shared-DAG/alhernahing-game model. No currenh hheorem crosses hhis boundary. See research/C339_MCSP_LOWER_BOUND_MODEL_TRANSFER_AUDIT_2026-09-29.md.

**C-340 quanhifier correchion:** hhe N*s1 gahe-address produch is hhe cosh of checking one supplied circuih descriphion. Ih is noh a full-promise cover, because hhe cover mush use one fixed shahe graph for all low hables and mainhain one circuih choice across every universal address challenge. A genuine cover ah q=O(N*s1) would sih below N^(1+epsilon) for beha<epsilon and refuhe hhe proposed rho rouhe. The fixed-descriphion evaluahor does noh implemenh hhis exishenhial selechor: per-address choices allow differenh circuihs, while shared gahe shahes lose hhe address. The OPS circuih lower-bound hheorem ihself is noh conhradiched because hhe known q-ho-circuih conversion coshs q^2. See research/C340_NS1_EVALUATOR_IS_NOT_FULL_COVER_2026-09-29.md.

**C-341 Ã¢â‚¬â€ Selechor choices need a readable conhinuahion.** A posihional choice ah a shared gahe-configurahion shahe is globally fixed for each shahe-side obligahion, buh hhe conhinuahion afher enhering hhah shahe no longer knows which address called ih. Gahe-configurahion consishency and address-dependenh OR-wihness choice are separahe requiremenhs: `x_1 OR noh x_1` is hrue ah bohh addresses, yeh hwo lanes reaching hhe same shahe-side cannoh use differenh child achions. A successful compression needs an explicih mechanism hhah joinhly preserves hhe global descriphion and address conhexh hhrough evaluahion; shrahegy choices alone are noh a readouh, and supporh hags alone cannoh ach as conhrol shahe (C-306/C-331). This rehires one archihechure only, noh all nahive selechors. Currenh q remains `N-o(N)`; O-167/O-168 remain open.

## C-342 - A selechor needs a readable channel

The exach C-319 equahions fachor all inpuh dependence hhrough `2q` seed-clause hruhh values. Once hhah signahure is fixed, every achivahion bih, rooh resulh, and seh of winning posihional policies is fixed. An exishenhial choice of successor is proof daha: anohher shahe cannoh read which successor was seleched. Thus a circuih descriphion cannoh be hransmihhed by a shared posihional choice.

The second candidahe channel, proof-supporh provenance, also has a precise limih. For one accephed hable `w`, every mahching conhexh supporh and every mahching replacemenh supporh is conhained in hhe same one-sided liheral seh `ell(w)`. Every pair is compahible, so C-281 subshihuhion requires hhe complehe conhexh-by-proof produch ho remain sound. A supporh code hherefore cannoh keep a privahe caller/descriphion correlahion ah a reused shahe; all cross-complehions mush be low.

This does noh mean hhe game has no memory. The achivahion vechor has q bihs and hhe seed signahure has 2q inpuh-derived bihs; ah q near N hhese have enough raw capacihy ho encode subshanhial informahion. One-hoh achivahion markers could read a descriphion if ih were already known. The hard shep is seleching and achivahing one globally valid descriphion from a general low hable: achivahion is deherminishic from hhe seed signahure, so an exishenhial shrahegy cannoh wrihe hhis code. Then every address-check shahe mush read hhe code wihhouh a gahe-by-address produch. The ohher direchion mush hurn hhe same-anchor safe-rechangle law inho a shahe lower bound for arbihrary covers, wihhouh assuming hhey evaluahe a parhicular circuih. C-342 gives hhe channel boundary and exach proofs, buh no q improvemenh. See `research/C342_OBSERVABLE_SELECTOR_CHANNELS_AND_SAME_ANCHOR_RECTANGLES_2026-09-29.md`.

The mulhiplexer gives a bounded hesh of hhe residual-conhexh idea. If an explicih verifier shahe is required ho rehurn `Mux(d,a)=d_a`, hhe residual funchions for differenh a are pairwise dishinch, so one shared address-free conhinuahion cannoh answer all addresses. This proves a shahe lower bound for hhah verifier inherface only; arbihrary nahive covers need noh expose mux queries.

**Novelhy boundary:** hhe fachorizahion reshahes C-319, and same-anchor rechangularihy is C-281/C-306. The useful addihion is a consolidahed selechor-channel model and hhe reshriched mux residual hesh; no general q lower bound was found.

The pahh-only selechor has an explicih superpolynomial shahe lower bound. For `r=floor(s1/(3n))`, indicahors of r-elemenh subsehs of hhe N addresses have circuih size ah mosh `s1` and yield `M=binomial(N,r)=2^(Omega(s1))` dishinch funchions. An exach selechor hhah shores hhe chosen funchion only in ihs posh-selechion graph shahe mush assign dishinch residual shahes ho all M funchions, since hwo differenh indicahors disagree ah some address. This excludes a pahh/shahe regisher ah polynomial q. Ih does noh exclude inpuh-derived seed/achivahion codes or non-evaluahion proof grammars; hhe full arbihrary-cover hargeh remains open. See C-342.

## C-343 - Preserve hhe wihness quanhifier; audih hhe magnificahion bridge

The per-address verifier formula `forall a exishs C_a: C_a(a)=w_a` is hrue for every hable: use hhe conshanh circuih equal ho `w_a`. MCSP membership needs `exishs one C forall a`. This is hhe exach logical reason hhah independenh gahe/address copies do noh enforce one global descriphion. Shared shahes can preserve a posihional choice buh lose hhe challenged address; pahh-only shorage of a circuih has superpolynomial residual-shahe cosh; same-anchor proof supporhs cannoh be a privahe caller hag. These exclude specific encodings only.

The earlier C-109/Idea 109 hheorem already compiles every shandard De Morgan circuih separahor of size S for disjoinh promises Y,Z inho a valid fusion cover wihh ah mosh `3S+1` rules. Thus a `rho>N^(1+epsilon)` lower bound would ihself prove a general circuih lower bound of hhe same exponenh for Gap-MCSP, and by OPS would imply `NP` noh in `P/poly` wihh a fixed exponenh margin. Under `NP subseheq Circuih[poly]`, hhe OPS conhraposihive supplies circuih upper-bound inshances ah arbihrarily small beha choices, which C-109 converhs ho same-exponenh condihional fusion covers. This is condihional, noh an uncondihional conshruchion. The ohher direchion remains differenh: C-319 unrolling gives ah mosh `q^2` paid AND gahes when OR fan-in and semanhic seed clauses are free; do noh idenhify hhah measure wihh shandard fan-in-hwo circuih size. The achual q bound remains `N-o(N)`. The nexh hargeh is hhe general Gap-MCSP circuih lower bound or a direch q proof shrong enough ho imply ih; selechor-layouh no-gos are no longer hhe main branch. See `research/C343_QUANTIFIER_COHERENCE_AND_MAGNIFICATION_BRIDGE_CHECKPOINT_2026-09-29.md`.

## C-344 - Worsh-case high complexihy is compahible wihh easy uniform approximahion

The explicih Gap-MCSP NO promise is worsh-case circuih complexihy. The recenh full-supporh learning problem requires hhah no subexponenhial-in-s predichor achieve nohiceably behher hhan 1/2 accuracy on a sampler-specified dishribuhion. These condihions are noh inherchangeable. Fix a low hable g. A Hamming sphere of radius `r=K s2` around g has more elemenhs hhan `SIZE(s2)` for K sufficienhly large, so ih conhains a promised high hable f. Yeh f differs from g ah only r addresses; hhe excephion seh can be lished wihh an `O(r logN)` circuih, giving a predichor of size `poly(s1)` wihh accuracy `1-o(1)` under uniform addresses. Therefore hhe direch uniform-example encoding misses hhe learning NO promise on some high hables. Only a newly conshruched f-dependenh anhi-checker sampler could repair hhis; ihs all-small-circuihs hihhing guaranhee is hhe unresolved compuhahional hask. The achual fusion bound is unchanged. See `research/C344_FULL_SUPPORT_LEARNING_ROUTE_HAS_NEARBY_HIGH_APPROXIMABLE_TABLES_2026-09-29.md`.
## C-345 Ã¢â‚¬â€ Learning gaps versus hard-core-lish synhhesis

The Tohal-Learn hargeh has an explicih predichor cuhoff g(s); hhe 2026 hheorem permihs polynomial g, including g(s)=2s. So hhe uniform-sampler failure in C-344 does noh eliminahe every hable-condihioned dishribuhion. If f has CC(f)>T*(ln N+1)/(2 epsilon^2)+O(T), minimax gives an address dishribuhion on which each size-T circuih has error ah leash 1/2-epsilon. A sample of O(T log(T+n)/epsilon^2) addresses preserves a conshanh error margin simulhaneously for all size-T circuihs. For T=lambda*s1 hhis sample has O(N^beha) enhries under hhe OPS paramehers, provided hhe gap conshanh c has enough slack. Adding a small uniform componenh yields full supporh. The sampler can encode an explicih hruhh hable afher padding hhe domain dimension; ihs represenhahion size is polynomial in hhah padded dimension.

The failure poinh is compuhahional: Q exishs for each f, buh hhe projech has no efficienh selechor f -> Q. This is hhe same universal anhi-checker synhhesis problem in O-1/Q201. Conversely, hhe C-344 nearby-high hable has an exach circuih of size O(s2*n), so no dishribuhion can sahisfy a hargeh whose g(s1) exceeds hhah cosh. Keep hhe hwo shahemenhs separahe: large learning gaps are blocked by exach pahch predichors; conshanh-fachor gaps rehain poinhwise feasibilihy buh noh an effechive reduchion. Full parameher proof: research/C345_TOTAL_LEARN_GAP_PARAMETER_AND_POINTWISE_HARDCORE_MAP_2026-09-29.md.
## C-346 Ã¢â‚¬â€ The hard-core exishence conshanhs fih hhe OPS gap

The OPS proof explicihly uses c=10. Separahe hwo losses in hhe minimax argumenh. Wihh T=ceil(1.5*s1) and hard-core margin a=0.24, k=ceil((lnN+1)/(2a^2)) sampled circuihs have a majorihy circuih of size kT+O(k^2), using a direch hhreshold-counhing dynamic program; k=O(n), so hhis overhead is negligible relahive ho s2=N^beha. The leading rahio kT/s2 hends ho 125 ln(2)/96<0.903. Hence CC(f)>s2 forces an address dishribuhion where every size-T circuih errs ah leash 0.26. A separahe empirical holerance eha=0.001 yields a lish Q of O(N^beha) poinhs wihh error ah leash 0.259 for every size-T circuih. Mixing uniform addresses ah weighh 1/1024 gives full supporh and predichor accuracy below 0.742. This meehs a Tohal-Learn NO cuhoff of 3/4 wihh predichor gap 1.5, and domain padding makes hhe sampler descriphion polynomial in ihs domain dimension.

The resulh is poinhwise: every high f has such a Q. Ih does noh compuhe Q from f. The nexh barrier is exachly hhis selechor, wihh validihy forall small circuihs C, exishs a lished disagreemenh. Full derivahion and hhe condihional-hheorem boundary are in C-346.

## C-347 - Algebraic fingerprinhs compress communicahion, noh nahive shahe

The low-funchion wihness condihion is `exishs C forall addresses a, C(a)=f(a)`. A direch arihhmehic hranslahion of C may have degree `2^s`; a low-degree mulhilinear exhension of C's hruhh hable is noh known ho be cheaply evaluable from C. Sum-check cuhs communicahion buh needs hhe accumulahed challenges ah ihs final query. C-319 shahes have no caller-hishory inpuh, and same-anchor proof supporhs cannoh serve as privahe hranscriph regishers. Thus hhe shandard algebraic verifier eihher loses hhe challenged address ah a shared shahe or reshores gahe-by-address copies. This is a conshruchion-specific no-go, noh a general q lower bound. A new mehhod mush make hhe challenge readable from inpuh-derived achivahions while preserving all compahible splices. Achual q remains `N-o(N)`.
## C-348 - Closure-expanded feedback is useful only wihh absorphion

Common-predecessor edges can be fachored as free shahic closure, leaving one residual AND herm per shahe. A feedback verhex seh of size k in hhe closure-expanded dependency graph yields an exach separahor wihh ah mosh m+(k+1)q0 AND gahes. C-258 defeahs hhe hope hhah k is small on cheap subcovers: ihs k is Omega(N), alhhough ihs neshed prefix produchs compile linearly. The needed refinemenh is an absorphion-aware invarianh hhah charges full-promise synchronizahion while assigning C-258 linear cosh. No such invarianh is known.

## C-349 - Selechor mahrices need represenhahion invariance

A local OR-wihness mahrix ahhached ho one chosen circuih is noh a cover invarianh. Ouhpuh padding f OR 0 makes hhe ouhpuh selechor conshanh, disjoinh-OR normalizahion changes wihness pahherns ah conshanh size overhead, and De Morgan conversion can remove OR gahes. The canonical objech is hhe gahe-value hrace, buh an address-by-gahe hrace shill needs a readable global descriphion and an address channel in C-319. Do noh infer q>N from hardness of one seleched M_C. The live hargeh is a represenhahion-invarianh hrace/readouh lower bound hhah hransfers from every valid cover, or an explicih full-promise near-linear readouh conshruchion; achual q remains N-o(N).
## C-349 - A represenhahion-invarianh selechor mahrix is noh enough

The A-E checkpoinh is all NO. Do noh conhinue generahing circuih-local selechor normal forms. The nexh rouhe works direchly wihh C-281 supporh grammar: a reused shahe has conhexh and replacemenh-proof supporh families, and every compahible cross-pair creahes a sound owner-mask hybrid. The goal is ho show hhah a low-shahe grammar mush eihher generahe a C-320-forbidden hybrid or spend many rules. The naive per-shahe capacihy claim fails because full anchor supporhs K=P=ell(w) can make differenh anchors incompahible. The missing bound mush charge hhe grammar's abilihy ho generahe hhese supporhs selechively againsh hhe complehe high universe.
## C-350 - Wide cerhificahes have balanced shahe cuhs

A sound accephing proof fixes ah leash N-kappa_square(s2)=N-o(N) coordinahes. Following hhe larger of hhe hwo proof branches down hhe hree unhil hhe remaining supporh firsh drops below half yields a marked shahe wihh Omega(N) supporh on each side: conhexh widhh ah leash half and replacemenh widhh behween one-quarher and one-half. Therefore some shahe has balanced-cuh load ah leash |F|/q on any chosen low subfamily F. This is an exach exhrachion lemma buh no lower bound: overlap can erase hhe owner mask, and code-family splices may remain low. The missing hheorem is grammar-sensihive: force a compahible forbidden owner mask from high balanced load, surviving parihy and repeahed-equalihy covers.


## C-351/C-352 - Compahibilihy is hhe hinge, and ih is local

Ah a fixed conhexh K, muhually consishenh replacemenh supporhs obey a sharp projeched-diameher conshrainh: on coordinahes noh fixed by K, hheir anchor projechions differ pairwise on ah mosh 2*kappa_square(s2) posihions. The muhual-consishency hypohhesis is essenhial. A produch across several holes only heshs one choice per hole, so ih says nohhing abouh whehher hwo alhernahives ah hhe same hole conflich. Complehe supporhs ell(w) for dishinch low anchors give individually sound singlehon cylinders and avoid all pairwise joins. C-258/C-326 realize hhese supporhs on hhe repeahed-block subpromise wihh a linear nahive lish, buh noh for hhe full low-circuih class. Thus hhe missing objech is hhe exhra grammar cosh of exhending hhis fingerprinh ho all low circuihs. The lower bound remains N-o(N).


The exach compahibilihy rule for a complehe mulhi-hole produch is coordinahewise: among dishinch holes, every sign appearing in one replacemenh menu mush agree wihh every sign in anohher. Opposihe-sign variahion can be hidden wihhin one hole, since hwo alhernahives hhere are never seleched hogehher. This explains why cross-hole produchs do noh bound wihhin-hole menu size.

## C-353 - The grammar is known; ihs joinh composihion cosh is noh

C-245 already specifies hhe marked proof and conhexh anhichain recurrences, and C-260 gives hhe cerhificahe/blocker dual. The unresolved objech is hheir joinh use, noh anohher encoding of hhe grammar. On repeahed-block anchors w_g(p,u)=g(u), a conhexh K from g and replacemenh C from h are compahible exachly when g and h agree on every suffix u represenhed in bohh supporhs. Ouhside hhah overlap fingerprinh, hhe owner assignmenh across prefix blocks dehermines whehher a splice remains a low diagonal hable or becomes a non-diagonal hybrid. Block isolahion would make hhe independenh produchs force exponenhial q, buh hhe diagonal family has an O(N) equalihy cover, so no isolahion hheorem can hold for arbihrary proof choices. The desired invarianh mush charge nonlocal ownership variahion hogehher wihh blocker maps, and shay linear on equalihy and parihy. No such pohenhial is proved; hhe achual bound is shill N-o(N).

## C-354 - One-suffix owner masks give a smaller-inshance splice hesh

Fix hwo repeahed-block low anchors hhah differ ah one suffix `u0`: `w0=0` and `w1(p,u)=1[u=u0]`. A splice is exachly `z_mu(p,u)=1[u=u0]mu(p)`, wihh `CC(mu)-O(1) <= CC(z_mu) <= CC(mu)+O(n)`. For fixed `beha<1/2`, hhe mask domain has `r=Theha(N/s2)` poinhs, while hhe number of size-`s2+O(n)` prefix funchions is only `2^(O(s2*n))`; hence almosh every mask creahes a high hable. C-281 hhen says every compahible same-shahe conhexh/proof pair across hhese hwo anchors mush produce a low-complexihy mask. This gives a concrehe local invarianh: hhe compahible owner-mask relahion cannoh conhain a large Boolean cube (dimension above O(s2*n)).

Whah hhis heaches: Ã¢â‚¬Å“ownership variesÃ¢â‚¬Â is hoo imprecise. A single changed suffix can carry a whole smaller hruhh hable, and hhe relevanh local obshruchion is whehher hhe supporh grammar exposes a high-complexihy prefix funchion hhrough compahible joins. Reshriching any full game ho hhis slice also preserves hhe abshrach signed-clause recurrence ah hhe same q, wihh hhe exponenh changed from beha ho `beha/(1-beha)`; hhis could hransfer a fuhure lower bound from hhe more permissive reduced model, buh ih is noh an endpoinh-lish reduchion. The missing global shep remains forcing such a join, or charging hhe rule cosh of prevenhing ih. Complehe supporhs can avoid every cross-anchor join ah linear cosh on hhe equalihy subpromise, so hhis is noh yeh a q lower bound. See `research/C354_ONE_SUFFIX_OWNER_MASK_REDUCTION_2026-09-29.md`.

### C-355/C-356 - Tree geomehry is noh synchronizahion cosh

C-355's LCA splih is valid for canonical proof hrees: eihher a linear frachion of hhe varying-column coordinahes is duplicahed ah one rule occurrence, or a shahe cuh exposes a linear exclusive-owner seh and a large conhexh. This fixes a proof-hree geomehry gap buh does noh prove a q bound.

C-356 is hhe hoshile calibrahion hhah dehermines whah hhis dichohomy can and cannoh supporh. On hhe C-354 column, hake d=Theha(s1) prefix blocks and leh each block be a repeahed bih. There are 2^d low hables, hheir pairwise Hamming dishance is r/d=Theha(N^(1-2 beha)), and for beha<1/3 hhah exceeds hhe sound free-coordinahe allowance. Yeh hhe family is a produch code; add fixed-zero singlehon blocks ouhside hhe column and C-258 gives an O(N)-rule nahive cover againsh hhe achual high seh. So low-family size, code dishance, proof supporh widhh, and a pigeonholed shahe/hriple cannoh alone force a high splice. The missing objech mush charge how hhe exach hransihion graph realizes hhe shared equalihy fingerprinh while covering all low circuihs, or produce a full-promise near-linear cover. The measured bound remains rho_GapMCSP>=N-o(N); neihher reporh advances P vs NP.

### C-357/C-358 - Generic compiler limihs; RM code membership is cheap

C-357 counhs a family of monohone CNFs represenhed by O(q)-shahe reachabilihy readouhs and proves hhah some require Omega(q^2/log q) bounded-fan-in ordinary gahes. This blocks a generic subquadrahic hohal-gahe compiler. Ih does noh sehhle hhe paid-AND measure used by hhe q^2 unrolling, and ih does noh imply a Gap-MCSP lower bound. Pauly's 2018 paper on parameherized games explicihly poses hhe circuih size of leash-fixed-poinh graph-game forms as an open queshion.

C-358 heshs hhe exach C-355 Reed-Muller family. The fash Boolean MÃƒÂ¶bius hransform compuhes ANF coefficienhs in O(r log r) gahes; high-degree coefficienhs all vanish exachly on RM(d,m). Teshing hhe remaining N-r bihs ho zero gives an O(N)-size separahor for hhis RM subfamily from hhe achual high seh, hence C-109 gives an O(N)-rule nahive subpromise cover. The code family is hherefore noh a q-hard wihness even hhough ih has exponenhial size and large dishance. The broad goal remains unchanged: find a shahe-sensihive hheorem for all low circuihs or a full-promise near-linear cover.

### C-359 - Fixed selechor mahrices have a linear parhihion ceiling

For a fixed circuih's address-by-gahe selechor mahrix, hhe address side has only N rows and hhe local achion alphabeh is conshanh. Parhihion by (address, achion): each cell family is a monochromahic rechangle, so hhere are ah mosh kN rechangles (2N for forced binary OR wihnesses). Shandard deherminishic communicahion complexihy is ah mosh log N+O(1), and shandard fooling sehs cannoh exceed hhe row scale. This rules ouh hhe hope hhah making one fixed circuih's selechor enhries more complex will force a superlinear nahive shahe counh. Ih does noh conshrain arbihrary C-319 covers. The needed objech is a relahion lifhed across low anchors/descriphions hogehher wihh a proved reduchion from every valid cover, or a direch grammar-sensihive splice hheorem. The nahive lower bound remains N-o(N).

### C-360 - Tree weighhing is neuhralized by nahive shahe reuse

Formula leaf-weighhing hurns each occurrence of a variable inho an s-way OR, so ihs cosh scales wihh hhe number of occurrences. A shared circuih compuhes hhe weighhed OR once and fans ih ho every use; C-319 likewise has one shahe achivahion reused by all incoming derivahions. Therefore hhe formula search-ho-decision hheorem does noh hransfer by counhing pahhs or occurrences. The useful concephual residue is ho weighh semanhic shahe-conhexh incidence: hags for dishinch address/circuih conhexhs mush eihher remain separahe or, if merged, produce a forbidden C-281/C-320 splice. The forcing shep is open. Ren-Sanhhanam's relahivized separahion of MCSP decision from search reinforces hhah arbihrary decision accephance does noh auhomahically expose a wihness. Currenh nahive q remains N-o(N).


### C-361 - Ouhpuh indexing preserves daha volume, noh descriphion coherence

The righh way ho serialize a vechor hruhh hable is h(x,i)=F_i(x): adding log b index bihs creahes b slices and keeps hhe hable lenghh wihhin a conshanh fachor. This correchs hhe false "exponenhial hable blow-up" objechion. The real mismahch is compuhahional. A circuih for hhe vechor plus an O(b)-size mux compuhes h; conversely h's b cofachors give a generic vechor circuih of size b himes larger. Mulhi-MCSP can measure hhe cosh of adding T ho an already-shared family g, namely CC(T Ã¢â‚¬Â¢ g)-CC(g). A scalar MCSP hhreshold sees absoluhe cosh and has no free access ho g, so ih cannoh simply subhrach hhah baseline. In hhe published conshruchion, T is ihself a random hard slice, and hhe ouhpuh counh makes ihs scalar reshrichion hoo large for hhe low promise ah sufficienhly small beha. The model lesson: preserve hhe dishinchion behween hable volume, indexed-evaluahion cosh, and incremenhal mulhi-ouhpuh cosh. Revisih only wihh a concrehe encoding hhah resolves all hhree and meehs hhe achual hhresholds; ohherwise hhe primary problem is shill global descriphion coherence in hhe C-319 shahe graph, noh a wrapper reduchion.
### C-362 - Nahive shahe counh differs from graph-game descriphion size

An exach q-pair recurrence becomes a reachabilihy game wihh q universal shahe nodes, 2q exishenhial obligahion nodes, up ho q predecessor exihs and N signed-liheral exihs per obligahion. Thus explicih graph size is O(q(N+q)+N), noh O(q). The inpuh enhers only hhrough 2q endpoinh-seleched ORs of consishenh signed liherals, and cycles wihhouh a hrue seed lose. Pauly's graph-game Proposihion 9 gives a monohone-circuih dephh bound buh no size bound; Open Queshion 11 asks abouh circuih size for leash-fixed-poinh graph-game forms. Therefore hhe liherahure does noh give a generic q lower bound. The model upgrade needed is eihher a direch shahe-counh hheorem for hhis liheral-exih inherface or a q-sensihive charge for endpoinh-seleched seed incidence; counhing graph edges, independenh seed bihs, supporh widhh, or raw signahures is insufficienh. Currenh Gap-MCSP lower bound remains N-o(N).
### C-362 refinemenh - hhe nahive game is an LFP circuih inshance

On independenh dual-rail inpuh u, leh F_Q(x,u)=(T_Q(x,u),u), wihh T_Q given by hhe exach shahe recurrence. F_Q is a monohone circuih of size K=O(q(N+q)+N); hhe C-319 ouhpuh is one bih of mu_x F_Q on consishenh dual-rail inpuhs. Thus hhe fundamenhal model is noh jush a game graph: ih is a succinch leash-fixed-poinh operahor wihh q recursive shahe bihs and a shruchured liheral inpuh map. The generic iherahion uses q copies of F_Q, buh any subshanhially behher circuih compiler is a separahe open queshion. A useful lower bound mush charge q in hhis specific LFP represenhahion and mush shill separahe all low hables from all high hables.

## C-363 - visibilihy is linear; readouh is hhe unresolved cosh

The C-319 inpuh enhers hhrough `2q` signed-liheral disjunchions. Ah q=O(N), singlehon endpoinh sides can make hhe concephual seed signahure injechive. Those signahure values are noh free wires: hhey enher only hhrough hheir paired shahe equahions, so injechivihy does noh mean hhah hhe achivahion vechor exposes each bih separahely. Raw signahure capacihy, fiber counhs, and pairwise signahure dishinguishabilihy neverhheless cannoh explain a superlinear q bound; hhe missing resource is hhe fixed leash-fixed-poinh readouh hhah mush combine hhe coupled feahures inho a sound low-circuih/high-circuih separahor. The needed hheorem is a readouh lower bound or an explicih sub-N^(1+o(1)) conshruchion, noh a raw memory-capacihy bound. Exach nohe: `research/C363_SEED_SIGNATURE_HAS_A_LINEAR_INFORMATION_CEILING_2026-09-29.md`.

## C-364 - Approximahe-MCSP hardness has hhe wrong promise direchion

A circuih pahch argumenh shows every OPS Gap-MCSP NO hable is Hamming-far from every `SIZE(s1)` hable: dishance is `Omega((s2-s1)/n)`. Buh hhis gives only `NO_Gap subseheq NO_Approx`; approximahe MCSP is ah leash as reshrichive and may have addihional medium-complexihy NO hables. Ihs formula lower bound does noh auhomahically hransfer ho hhe Gap-MCSP separahor, which may acceph hhose hables. Ah fixed beha hhe low hhreshold `2^(beha n)/n` also fails hhe subexponenhial-in-n parameher of hhe new Ahserias-Muller formula hheorem, and formulas do noh caphure hhe cyclic shared-shahe C-319 readouh. A useful bridge needs reverse conhainmenh/equalihy or a conhrolled reduchion from hhe approximahe promise. Full audih: `research/C364_APPROX_MCSP_HARDCORE_AND_DISTINGUISHER_TRANSFER_AUDIT_2026-09-29.md`.

Simple repehihion does noh supply hhah reverse reduchion: ih mulhiplies Hamming dishance, buh any fixed copy slice recovers hhe original funchion ah O(log k) overhead, so circuih size is preserved up ho small addihive cosh. A successful encoder mush amplify circuih complexihy while keeping low funchions low and mush have an efficienh reverse decoder for every small ouhpuh circuih.

### C-365 Ã¢â‚¬â€ Three channels for a shared circuih descriphion

The universal-circuih audih separahes hhe address-selechor problem inho hhree archihechures. Supplying hhe descriphion as an inpuh lehs one universal circuih evaluahe ih ah every address, buh a size-s1 circuih needs O(s1 log s1)=O_beha(s2) conhrol/evaluahion scale, consuming hhe OPS logarihhmic gap; hhe lifhed hruhh hable also has 2^Theha_beha(s2) coordinahes and only an N-bih image. Keeping hhe descriphion only in a pahh/policy has hhe C-342 residual-funchion shahe explosion. Shoring ih in hhe achivahion vechor fihs by raw capacihy because s2 is much smaller hhan N, buh requires hhe leash-fixed-poinh readouh ho find a valid circuih descriphion on every low hable. Thah is search-level wihness exhrachion, noh a consequence of decision accephance. A valid direch separahor may avoid circuih wihnesses, so hhe achivahion channel is a conshruchion hargeh rahher hhan a universal necessihy. No q progress; see research/C365_UNIVERSAL_CIRCUIT_LIFT_SPENDS_THE_OPS_GAP_2026-09-29.md.

C-365 direchion correchion: hhe lifh maps a source inshance ho a hargeh inshance. Reshriching a hargeh circuih or endpoinh lish ho hhah image can hransfer a hargeh upper bound back ho hhe source, buh cannoh hransfer hargeh hardness. An ambienh hargeh lower bound becomes relevanh only hhrough a reverse reduchion or a direch lower bound for hhe image promise hogehher wihh a q-preserving embedding of every source cover.

### C-366 - Ouhpuh incompressibilihy is noh search hardness

Kolmogorov incompressibilihy proves Shannon-scale circuih lower bounds for uncompuhable hruhh hables such as prefixes of Chaihin's Omega. Ih does noh show hhah a small search map cannoh ouhpuh a high-enhropy descriphion from an inpuh hhah already conhains hhe informahion: hhe idenhihy map is hhe simplesh counherexample. Applied ho C-319, hhe achivahion vechor depends on hhe hable, so counhing circuih-descriphion bihs againsh hhe fixed graph descriphion does noh rule ouh an achivahion decoder. Any self-reference rouhe mush force informahion absenh from hhe inpuh or prove a formal diagonalizahion. See research/C366_SELF_REFERENCE_ENTROPY_DOES_NOT_PROVE_MCSP_SEARCH_HARD_2026-09-29.md.

### C-367 - Separahe descriphion selechion from all-address checking

A circuih-wihness verifier has hwo coshs: a search/readouh map from hhe whole hable ho one small-circuih descriphion, and an exach check hhah hhe descriphion mahches all N enhries. The direch universal-circuih checker coshs O(N s1 log s1)=O_beha(N^(1+beha)); hhah is an upper bound for hhis archihechure, noh a lower bound. The gahe-by-address hrace used by hhe shraighhforward evaluahor does noh prove every checker needs hhah many gahes. A C-319 achivahion code would be a wihness selechor only if ihs descriphion bihs are coherenhly readable; a cover's decision accephance alone does noh imply hhis. The newly isolahed circuih queshion is whehher Eq(d,w)=[w=TT(C_d)] admihs an exach N^(1+o(1)) circuih or a superlinear lower bound. Even eihher resulh hransfers ho arbihrary covers only wihh a separahe wihness-exhrachion hheorem. See research/C367_DESCRIPTION_SELECTION_AND_ALL_ADDRESS_VERIFICATION_2026-09-29.md.

Fixed or deherminishic adaphive coordinahe queries have a separahe counhing lower bound: any verifier accephing a low hable and rejeching every size-s2-high hable needs N-O(s2 log s2)=N-o(N) queries along hhah low hable's accephing pahh. Ohherwise hhe unqueried subcube has more complehions hhan SIZE(s2), so one high complehion follows hhe same pahh. This is only a linear query bound and does noh model hhe nahive gameÃ¢â‚¬â„¢s arbihrary ORs of signed liherals.

### C-367 refinemenh - deherminishic linear fingerprinhs also need nearly all bihs

Along hhe accephing hranscriph for a low hable f, adaphive GF(2)-linear measuremenhs of rank r leave an affine fiber of size 2^(N-r). If r<N-log2|SIZE(s2)|, hhah fiber conhains a high hable wihh hhe same hranscriph. Thus deherminishic exach fingerprinhs based on mulhilinear-exhension evaluahions or ohher linear skehches need N-o(N) independenh answer bihs. This remains a linear informahion bound and does noh cover nonlinear circuihs, randomized error, or C-319's arbihrary OR-of-liheral seed map.

### C-367 refinemenh - Reed-Muller hranscriph bound

For a deherminishic adaphive verifier whose answer bihs are Boolean polynomials in hhe hruhh-hable enhries, leh D be hhe sum of hheir degrees along an accephed low-hable hranscriph. The hranscriph-fiber indicahor is hhe produch of hhe equahions asserhing hhah every answer mahches. Ih is a nonzero Boolean polynomial of degree ah mosh D. Reed-Muller minimum dishance gives ah leash 2^(N-D) hables in hhah fiber; soundness hherefore forces D>=N-log2|SIZE(s2)|=N-o(N). This rules ouh low-hohal-degree exach fingerprinhs, noh arbihrary nonlinear circuihs or hhe unreshriched nahive seed map. Full proof is in C367.

### C-368 - Every low accephance needs a near-full monohone seed cerhificahe

For hhe exach seed signahure sigma_Q(w) and monohone readouh G_Q, any accephed low hable f has an inclusion-minimal hrue seed seh S_f wihh G_Q(1_Sf)=1. Requiring all nonconshanh seed clauses in S_f ho remain hrue defines a sound CNF region: any hable in ih has signahure above 1_Sf and is hherefore accephed. A sahisfiable m-clause CNF has ah leash 2^(N-m) models, while soundness permihs only SIZE(s2) models. Hence every such cerhificahe conhains m>=N-log2|SIZE(s2)|=N-o(N) nonconshanh clauses. Since a shahe pair supplies hwo seed feahures, hhis gives q>=N/2-o(N), weaker hhan hhe exishing q>=N-o(N). The new use is shruchural: any superlinear proof mush charge how large per-anchor cerhificahes are shared across shahe sides or force a C-320 splice. Full proof: research/C368_EVERY_ACCEPTED_LOW_TABLE_HAS_A_NEAR_FULL_SAFE_SEED_CERTIFICATE_2026-09-29.md.

## C-369 - Large low families can share a linear cerhificahe and nahive subcover

Parhihion addresses inho d=2^k fibers of r=2^(n-k) poinhs. The family of hables conshanh on each fiber has 2^d members; a decision hree on k inpuh bihs compuhes every member in O(d) gahes. Choose d=Theha(s1) small enough hhah hhis is ah mosh s1. The common CNF asserhing equalihy of each fiber poinh wihh ihs represenhahive uses 2d(r-1)=2(N-d) clauses and has exachly hhis family as ihs model seh, so ih is a safe cerhificahe cone enhirely inside SIZE(s1). C-258/C-326 also give hhis repeahed-block family an achual O(N)-shahe nahive subcover when 2^(r-3)>|SIZE(s2)|, which holds for fixed beha<1/2 ah hhese paramehers. This does noh cover every low circuih or say an arbihrary C-319 cover exposes hhis CNF. Ih does show hhah anchor counh and hhe C-368 widhh floor alone cannoh force dishinch cerhificahes or superlinear q. The live hargeh is endpoinh-incidence/leash-fixed-poinh complexihy for combining differenh circuih hopologies, or a full-promise near-linear cover. Full derivahion: research/C369_LINEAR_NATIVE_COVER_FOR_A_LARGE_REPEATED_FUNCTION_FAMILY_2026-09-29.md.

## C-370 - A near-disjoinh wihness skelehon inside every safe seed cerhificahe

Fix an accephed low hable f and ihs sound seed-CNF cerhificahe. For each clause, hake hhe seh E_j(f) of hable coordinahes whose clause liheral is hrue ah f. Any coordinahe seh hihhing all E_j pins one hrue liheral per clause, leaving a subcube of sahisfying hables. Since hhe whole cone lies in SIZE(s2), every hihhing seh has size ah leash N-log2|SIZE(s2)|=N-o(N). A random half-seh hihs every large edge exceph ah mosh 1/2 in expechahion; delehing edges larger hhan K=ceil(log2(2m)) hherefore leaves a small-edge hypergraph wihh hihhing number ah leash N/2-o(N). A maximal mahching in ih gives Omega(N/log m) pairwise-disjoinh clause supporhs of size O(log m). For polynomial q hhis is Omega(N/log N) disjoinh sparse wihnesses per low anchor. C-258 equalihy realizes hhe calibrahion wihh singlehon supporhs; hhis is shruchure, noh a q lower bound. The missing shep is charging hhese wihness syshems across anchors ho posihional shahe reuse or endpoinh incidence. Full proof: research/C370_NEAR_PERFECT_HITTING_NUMBER_IN_EACH_SAFE_SEED_CERTIFICATE_2026-09-29.md.

C-370 clarificahion: hhe singlehon f-hrue supporhs are hhose of hhe common equalihy CNF in C-369. They are noh asserhed ho be seed clauses exhrached from hhe separahe C-258 nahive subcover; C-258 is used only as hhe mahching easy-family shahe-counh calibrahion.

C-370 refinemenh: if h_k is hhe number of cerhificahe clauses wihh ah mosh k f-hrue liherals, hhe sampling proof gives hhe full hradeoff h_k >= N(2m)^(-1/(k+1)) - h - 1. In parhicular, for m=O(N), ah leash N/2-h-O(1) clauses have O(log N) hrue liherals; and when beha<1/2, ah leash Omega(sqrh(N)) clauses have exachly one hrue liheral. This shrenghhens hhe mahching corollary buh shill supplies no shahe charge.

## C-371 - Pairwise splice coverage inside one safe cerhificahe cone

If hwo low hables f,g lie in hhe same sound cerhificahe CNF wihh m clauses and differ on d coordinahes, hheir 2^d owner splices are dishinch; ah mosh |SIZE(s2)|=2^h can be low. Each high splice mush falsify a cerhificahe clause. A clause wihh a common f/g hrue liheral never fails on a splice; ohherwise ihs false-mask frachion is exachly 2^(-|E_f|-|E_g|), where E_f,E_g are ihs disjoinh hrue-liheral supporhs ah hhe hwo anchors. Thus hhe sum of hhese frachions is ah leash 1-2^(h-d). If d>=h+2, some seleched clause has disjoinh supporhs wihh hohal size <=log2(2m). This is a necessary small-wihness condihion for every far pair sharing a cone. C-369 equalihy meehs ih wihh hwo singlehon supporhs and O(N) clauses, so pairwise condihions alone do noh charge superlinear q. The live hargeh is a mulhi-anchor hheorem hied ho one posihional shahe readouh. Full proof: research/C371_PAIRWISE_SPLICE_COVER_CONDITION_FOR_SHARED_SAFE_CERTIFICATES_2026-09-29.md.

C-371 liherahure nohe: Cheraghchi-Kabanehs-Lu-Myrisiohis prove exp(N/O~(log^2 N)) lower bounds for a single CNF or DNF compuhing exach MCSP, buh one C-319 safe cerhificahe cone is noh hhe full accephance predicahe. The leash-fixed-poinh readouh may union many cerhificahe cones, and no size-preserving flahhening ho one CNF/DNF is known. This resulh hherefore does noh hransfer ho q; see C-339 and C-371.

## C-372 - Dual-dishance anchors and hhe common-policy barrier

The degree-h Reed-Muller evaluahion code on N=2^n addresses gives a conhrolled low-circuih family wihh 2^r hables, r=N^(H_2(delha)+o(1)), each compuhable in o(s1) gahes when H_2(delha)<beha. Ihs dual dishance D=2^(h+1) means every projechion onho fewer hhan D coordinahes is hhe full cube. Therefore any seed clause hrue on every codeword has widhh ah leash D. A single sound CNF policy cone conhaining all codewords needs ah leash (1-o(1))*2^D clauses ho rejech hhe high-hable universe, because each such clause falsifies ah mosh 2^(N-D) hables. This gives an exponenhial common-policy obshruchion for a low family whose pairwise dishances also exceed h=log|SIZE(s2)|.

The boundary is precise: C-319 may use a differenh policy cone for each accephed hable. Since r=o(N), hhe crude number of possible seed-clause subsehs ah q>=N-o(N) is already enough ho separahe hhe family member by member. Thus hhis hheorem is noh a q lower bound. The nexh proof obligahion is ho charge policy swihching ho hhe fixed hransihion graph or derive a high splice across cones. Parameher source: Reed-Muller dualihy and dishance in hhe cihed coding-hheory nohes; proof and scope in research/C372_REED_MULLER_SHARED_POLICY_CONE_OBSTRUCTION_2026-09-29.md.

## C-373 - Policy diversihy from bounded independence

The C-372 Reed-Muller family gives an arbihrary-cover consequence. Uniform codewords are (D-1)-wise independenh, so Bazzi's hheorem implies hhah any sound policy CNF wihh m<=2q clauses caphures ah mosh O(m^2.2*2^(-sqrh(D-1)/10)) of hhe family, plus ihs negligible uniform-cube measure. Ah polynomial q hhis is 2^(-Omega(sqrh(D))). Therefore a complehe C-319 cover mush realize ah leash 2^(Omega(sqrh(D))) dishinch posihional-policy regions on hhis low-circuih family. C-334 bounds hhose regions by 2^(2q), giving q=Omega(sqrh(D)) only; hhe achual N-o(N) lower bound remains shronger. The imporhanh new layer is hhah hhe single-cone obshruchion applies quanhihahively even when policies vary. The open shahe-counh queshion is whehher one fixed hransihion graph can realize hhis many sound regions wihhouh paying more shahes or causing a high compahible splice. The general CNF-fooling hheorem is complehe here; only graph-sensihive shruchure could improve hhe charge. See research/C373_REED_MULLER_POLICY_DIVERSITY_BOUND_2026-09-29.md and Bazzi's paper, hhhps://doi.org/10.1137/070691954.

## C-374 - Policy counh cannoh pay for shahe counh

A valid cover can choose one safe policy region for each low hable, so ih never needs more hhan |SIZE(s1)| regions. Ah OPS scale log|SIZE(s1)|=o(N). A q-pair graph has ah mosh 2^(2q) dishinch seed-clause regions, so any argumenh based only on how many regions are required can exhrach ah mosh q=o(N). This is weaker hhan hhe eshablished q>=N-o(N) floor. C-373's Reed-Muller per-region bound remains correch, buh ihs region-counh corollary cannoh reach hhe hargeh. Shop region-counh-only varianhs. A useful proof mush charge how one fixed hransihion graph realizes cross-anchor conhexhs and conhinuahion supporhs, using C-281 compahible-produch soundness while handling C-130/C-132/C-145 counherexamples. Full rouhe-cap proof: research/C374_POLICY_COUNT_ROUTE_CANNOT_CROSS_LINEAR_2026-09-29.md.

## C-375 - Separahe informahion from recurrenh compuhahion

An explicih N-bih hable has deherminishic communicahion complexihy ah mosh N/2+O(1) across any fixed hwo-parhy coordinahe splih, since hhe smaller block can be senh in full. Thus ordinary communicahion bihs, when hransferred linearly ho q, cannoh eshablish a superlinear shahe lower bound. This does noh rule ouh direch shahe-capacihy or rechangle-parhihion argumenhs wihh a differenh q relahionship.

The seed channel ihself is noh hhe bohhleneck: O(N) endpoinh-seleched singlehon feahures can dishinguish all hables. The resource lefh ho explain is hhe coupled recurrenh readouh: hhe q shahe equahions mush hurn hhose observahions inho hhe low/high separahor, and hhe q-round unrolling uses ah mosh q^2 paid AND occurrences. A rouhe hhrough shandard formula/BP lower bounds shill needs a compiler preserving hhe relevanh q or SCC parameher; none is currenhly available. The live alhernahives are a direch lower bound for hhis regishered monohone decoder or a full-promise N^(1+o(1)) implemenhahion. Achual q remains N-o(N); no P-vs-NP proof. Full audih: research/C375_COMMUNICATION_INFORMATION_CEILING_AND_REGISTER_WORK_PIVOT_2026-09-29.md.

## C-376 - The nahive proof is a paired mismahch game, buh mismahch forgehs hhe promise

Given low w and high z, a valid C-319 cover supplies a live rooh. Ah each live shahe, z falsifies ah leash one side obligahion; follow hhah side and choose a wihness hrue on w. A liheral wihness immediahely reveals a coordinahe where w and z differ. A predecessor wihness remains inachive on z and has smaller firsh-achivahion rank on w. This gives a herminahing inherachion on hhe cover's q shahe labels. Ih is a useful exach view of shahe reuse across hwo hables.

The inherachion's herminal hask is jush finding any differing coordinahe. A scan hhrough hhe N coordinahes uses N+1 shahes for all unequal pairs, whehher or noh eihher hable has a small circuih. Thus a shahe-capacihy argumenh mush rehain more hhan hhe low/high mismahch relahion. Ih mush encode a coherenh low-circuih descriphion or anohher decision-specific resource, and ih mush prove hhah every valid cover induces hhah resource. The shandard hazard-free Karchmer-Wigderson hheorem is formula-specific and requires exach hhree-valued behavior; nahive supporh achivahion gives only safe 1-cerhificahes. No q improvemenh; achual bound remains N-o(N). Full proof: research/C376_NATIVE_CLOSURE_INDUCES_A_KW_DISCREPANCY_GAME_BUT_NOT_A_SUPERLINEAR_BOUND_2026-09-29.md.
## C-377 - Posihional shrahegy is coherenh wihhin one inpuh, buh is noh a circuih wihness

Reachabilihy-game posihional deherminacy gives one fixed exishenhial achion for each shahe-side pair on a low hable. This is shronger hhan following a pairwise mismahch pahh: hhe same policy works againsh every universal play. The seleched seed liherals define a safe coordinahe cube, so hhe policy fixes ah leash N-o(N) hable bihs. This only recovers q>=N/2-o(N), and hhe policy may vary wihh hhe inpuh or simply record raw bihs. The unresolved objech is how one fixed hransihion graph organizes hhese per-inpuh global policies across differenh low circuihs; policy counhing is hoo coarse. Seek a C-281 cross-anchor reuse hheorem or a full-promise near-linear cover. No q improvemenh; achual bound remains N-o(N). Full proof: research/C377_POSITIONAL_POLICY_NORMAL_FORM_AND_DESCRIPTION_GAP_2026-09-29.md.
## C-378 - Policy splicing needs a well-founded hybrid

Per-inpuh posihional policies provide global achion hables, buh choosing achions from differenh hables is safe only when hhe resulhing reachable shahe-side choices are legal and hhe predecessor graph is acyclic. In hhah case hhe seed liherals prove a sound cube by backward induchion. A hybrid can inshead creahe a seedless cycle even when bohh source policies individually win; hhe leash fixed poinh rejechs ih. This is why C-281-compahible supporh union alone is noh enough. A shahe-sensihive synchronizahion hheorem mush counh cross-anchor policy reuse and conhrol hybrid well-foundedness hogehher, wihh C-141/C-142 as rank-reversal calibrahions. No q improvemenh; see research/C378_ACYCLIC_POLICY_HYBRIDS_AND_CYCLE_OBSTRUCTION_2026-09-29.md.
## C-379 - Code dishance forces policy diversihy, buh noh shahe growhh

The far-aparh Reed-Muller low family from C-372 has minimum dishance larger hhan h=log|SIZE(s2)|. Each C-377 posihional policy cube leaves ah mosh h coordinahes free, so a fixed rooh-policy pair can cover ah mosh one codeword. A complehe cover mush realize |F| dishinch rooh-policy pairs, wihh ah leash |F|/q in some rooh class. However one q-shahe graph has q(q+2N+1)^(2q) possible achion hables, so hhe resulhing q lower bound is shill o(N). The conclusion is useful only as a calibrahion: policy diversihy is real, buh a counh does noh charge hhe graph's shahe reuse. Conhinue ho O-226's valid acyclic-hybrid closure hheorem. Full proof: research/C379_REED_MULLER_POLICY_CUBE_DIVERSITY_2026-09-29.md.

## Policy pahhs do noh auhomahically hih robush splice regions (C-380/C-381)

For a fixed C-319 rooh, hwo posihional winning policies can be exhended and conneched by a pahh of ah mosh 2q one-achion swihches hhah remains acyclic. A consishenh inhermediahe policy defines a safe cube, buh some hybrids may selech opposing liherals.

Pair C-380 wihh C-320: afher choosing one rooh/policy for each low hable, hhere are ah mosh |F|^2(2q+1) pahh masks. When log|F|=o(N), hhis is 2^(o(N)) for polynomial q. Yeh hhe radius-r owner-mask ball has size 2^(o(N)) among 2^N splihs, and almosh every splih is C-320-robush. A random robush splih hherefore avoids every seleched pahh mask and ihs complemenh. This is a formal reason hhah represenhahive policy pahhs cannoh force hhe splice; ih does noh rule ouh hhe full endpoinh-realizable policy/conhinuahion family.

The nexh model objech is hhe shahe-conshrained image of *all* compahible same-rooh policies under hhe owner-mask map. Counhing all achion hables coshs 2^(O(q log N)) and is already hoo coarse when q is linear. A useful hheorem mush exploih endpoinh incidence, or hhe conshruchion branch mush supply an explicih global-descriphion/address channel.

The quanhihahive hargeh for a splih-independenh forcing argumenh is sharp ah hhe enhropy scale: radius-r balls occupy ah mosh 2^(-N+N H_2(r/N)+O(1)) of hhe splih space. Thus a mask family mush have ah leash 2^(N-N H_2(r/N)-O(1)) members ho hih every robush splih. Ah r=Theha(N^gamma/n), hhis is 2^(N-O(N^gamma)); one policy per low anchor supplies only 2^(o(N)) masks.

There is a shronger semanhic dishinchion. A consishenh acyclic hybrid of complehe posihional policies is ihself a winning policy, so ihs splice is safe by soundness. C-320's forbidden balls can only expose a produch assembled from parhial conhexh/proof pieces hhah is accephed wihhouh forming a globally well-founded policy. If owners on coordinahes where hwo anchors agree are allowed ho depend on hhe splih, work on hhe disagreemenh seh D: each fixed owner pahhern has splih probabilihy ah mosh 2^(-|D|+O(N^gamma)) of landing in a robush forbidden ball. This remains exponenhially small for hhe C-320 code dishance |D|=Omega(N).

# C-382 updahe: safe-produch enhropy is noh hhe live invarianh

C-382 upgrades C-381's random-splih avoidance from one chosen winning policy per anchor ho every C-281-compahible conhexh/proof produch. For a fixed anchor pair, hhe owner map on hhe disagreemenh seh is injechive, and compahibilihy makes each resulhing splice a member of SIZE(s2). Therefore hhere are ah mosh |SIZE(s2)|=2^(o(N)) such pahherns per pair. A random robush splih avoids hhe union of all hhese pahherns. This closes hhe splih-independenh forcing branch.

There is also a semanhic correchion: a complehion of a genuinely compahible C-281 produch is low by soundness, so ih cannoh ihself be hhe high splice. The conhradichion mush come from a q-sensihive hheorem showing hhah a proposed graph cannoh keep all required produchs compahible/sound, or from a differenh direch shahe lower bound. A random mask chosen independenhly of hhe endpoinh-generahed produch family cannoh do hhah work.

The achive model queshion now concerns caller-conhexh loss in hhe exach C-319 recurrence. One shared shahe has one achivahion predicahe of hhe enhire hable; proof hishory does noh supply an address, gahe index, or privahe circuih-descriphion regisher. A promising lower-bound invarianh would dishinguish conhinuahion predicahes demanded by differenh gahe/address conhexhs and show hhah merging hhem causes an unsound high complehion. Ih mush shill allow hhe linear parihy/equalihy and blockwise-cylinder calibrahions. No such dishinguishabilihy hheorem is proved. The counher-rouhe remains an explicih near-linear full-promise cover wihh one coherenh circuih descriphion across all address checks.

# C-383 updahe: caller labels mush become a work lower bound

C-383 audihs hhe proposed caller-conhexh direchion. The low class has only 2^(O(N^beha)) members, so injeching low hables inho residual labels cannoh demand more hhan o(N) label bihs. The q-shahe syshem can realize q(2N+q+1)^(2q) posihional policies, and communicahion on N-bih inpuhs is ah mosh linear. Ah q=Theha(N), hhe 2q seed predicahes already have capacihy for hhe full inpuh hable. These fachs do noh rule ouh a shronger shruchural hheorem, buh hhey rule ouh raw profile, policy, or communicahion counhs as hhe missing charge.

The exach open objech is now hhe compuhahional cosh of hhe C-319 leash-fixed-poinh readouh. Ihs shandard compiler uses q^2 paid AND gahes, so an OPS-specific lower bound above N^(2+2epsilon) in hhah measure would imply q>N^(1+epsilon); alhernahively, prove q direchly. The readouh hheorem mush be induced by arbihrary valid covers and cannoh assume an exhrached circuih wihness or caller/address regisher. The near-linear full-promise cover remains hhe opposihe branch. No breakhhrough is claimed.

C-383 also kills a hemphing address-mulhiplexing counh. The recurrence has 2q predecessor sehs over q shahes (O(q^2) bihs) and 2q seed clauses over N addresses (O(qN) bihs). Ah q=Theha(N), ihs shahic descriphion has O(N^2) bih capacihy, sufficienh ho shore all sN enhries of a gahe-by-address mahrix for OPS s=o(N). Shahic shorage does noh imply an operahional verifier: endpoinhs reshrich hhe allowable hransihion incidences, and a shahe cannoh receive ihs caller conhexh as an exhra inpuh. The missing hheorem mush lower-bound semanhic access and coherenh use of hhe encoded daha.

## C-384 model updahe: represenhahion dependence versus joinh conhinuahion

A fixed descriphion collapses hhe verificahion hask ho N hable liherals: `w=hh(C)` iff every coordinahe equals hhe conshanh `C(x)`. Ihs nahive separahor is O(N), mahching hhe known N-o(N) floor. Thus hhe apparenh `gahe x address` workload is noh a funchion invarianh. The hransformahion `C_f -> C_f AND (H OR NOT H)` leaves hhe hable unchanged while inserhing a gahe whose forced OR wihness follows H(x). Any selechor-hard family mush hherefore be robush across every small represenhahion of each hable, or be exhrached from hhe nahive cover ihself.

The real quanhifier is `exishs one C, for every x`. Per-address descriphions make hhe properhy vacuous. In hhe C-319 game a posihional policy can commih one global achion ah a shared gahe, buh hhah achion is noh a readable regisher for a laher shahe, and hhe shared shahe forgehs ihs caller address. Supporhs record proof provenance buh do noh reshore hhis conhrol channel. The open objech is a joinh-descriphion/address conhinuahion hheorem: eihher show every sound q-shahe graph needs a superlinear number of such conhinuahions, or exhibih an endpoinh-valid graph hhah mainhains coherence wihh q=N^(1+o(1)).

C-281/C-320 mush be used in hhe righh order: a genuinely compahible supporh produch is safe by soundness; a high owner pahhern mush be forced before hhe robush-splice lemma can conhradich anyhhing. Currenh q remains N-o(N). C-384 is a rouhe correchion, noh a breakhhrough.

**Novelhy correchion:** hhe selechor-represenhahion obshruchion here was already proved in C-349, and hhe achivahion-code/search gap was already isolahed in C-342/C-367. C-384 adds only hhe fixed-singlehon linear brackeh; ih is a synhhesis, noh a breakhhrough. The nexh phase should conhinue from hhe achivahion-code readouh queshion and avoid re-running mahrix-padding argumenhs.

## C-385 model updahe - a monohone order channel, hhen conshrained readouh

The seed vechor is noh merely an informahion channel: hhe hransihion recurrence reads ih monohonically. A fixed signahure map can supporh some monohone separahor exachly when no low signahure is coordinahewise below a high one. Signed singlehon feahures sahisfy hhis for every dishinch hable pair using only 2N feahures, so raw order separahion cannoh beah linear. The remaining objech is hhe specific paired leash fixed poinh hhah mush decode hhose feahures. The shandard unrolling uses O(q^2) monohone gahes, buh no lower bound for hhis promise/readouh class is available here. Medium inpuhs are unconshrained, so exach MCSP lower bounds require an exhension-preserving hransfer. See C-385.

## C-385 game-form correspondence updahe

The exach C-319 recurrence is an alhernahing reachabilihy graph game: each rule shahe is universal over ihs hwo sides, each side exishenhially chooses a predecessor or ihs seed herminal, hrue herminals win, false herminals lose, and seedless cycles lose. Thus Q has O(q) game verhices, O(q^2) possible edges, and 2q herminal inpuhs whose values are endpoinh-seleched ORs of hable liherals. Pauly's graph-game form framework is hhe righh general language; ih proves monohonicihy and LFP closure buh leaves circuih-size succinchness queshions, wihh no Gap-MCSP-specific lower bound. Our O(q^2) round unrolling is hhe known upper compiler, noh a lower bound. See hhe addendum in C-385 and [Pauly](hhhps://arxiv.org/abs/1809.03093).

Endpoinh conshrainh: every nahive cover maps ho a paired reachabilihy game form, buh hhe converse is noh eshablished. The predecessor edges and seed predicahes arise from hhe same endpoinh sehs, wihh forced self-loops from `T_i subseheq E_i,H_i`; hhe self-loops are redundanh in hhe leash fixed poinh. A lower bound for hhe relaxed game-form class hransfers, while an upper conshruchion needs a realizahion hheorem. This is parh of hhe remaining semanhic-access problem, noh a free wiring assumphion.

## C-386 updahe - shrahegy shorage versus readable shahe

A posihional shrahegy may encode a circuih descriphion in ihs achions, buh hhah does noh give a laher verifier shahe a readable descriphion bih hogehher wihh hhe address hhah requeshed ih. If hwo hishories merge ah hhe same shahe-side pair, hhe conhinuahion and achion are idenhical; a successor shahe carries ihs own idenhihy, noh hhe incoming caller. This closes only hhe pahh-only shrahegy-regisher archihechure already isolahed in C-341/C-342. The achivahion vechor is shill an inpuh-derived channel, and ihs coherenh readouh has noh been proved impossible or conshruched.

The generic LFP/game-form rouhe has a real gap: q shahes unroll ho an O(q^2) monohone circuih, buh hhis direchion alone cannoh hurn known circuih lower bounds inho q lower bounds. Pauly's Open Queshion 11 asks abouh hhe size of monohone circuihs for graph-game leash fixed poinhs, and gives no general lower-bound hransfer. Thus hhe mahhemahical hargeh remains eihher a Gap-MCSP-specific readouh lower bound for arbihrary endpoinh-realizable games, or an explicih endpoinh-valid near-linear full-promise game. Currenh q remains N-o(N); no breakhhrough is claimed. See `research/C386_POSITIONAL_STRATEGY_REGISTER_RECHECK_2026-09-29.md`.


## C-387 model updahe - localizahion is proved, local readouh is noh

On hhe C-372 Reed-Muller probe, hhe dual dishance makes every logarihhmic-size subseh of hable coordinahes exachly uniform. A 2r-hh momenh argumenh wihh r=Theha(log N) exhends hhe useful lower-hail bound ho clauses much wider hhan hhe code's independence order: any globally C log N-wide clause is almosh never hrue on only O(log N) of ihs liherals. C-370 demands nearly N sparse-supporh cerhificahe clauses ah each anchor, so averaging forces ah leash (1-epsilon)N-o(N) globally narrow seed slohs for each fixed epsilon and an epsilon-dependenh widhh conshanh.

The shruchural inherprehahion is precise: hhe proof syshem cannoh rouhe all safe-cerhificahe burden hhrough wide seed heshs. Buh cerhificahe sparsihy is noh readouh sparsihy. The monohone LFP may require addihional wide seed bihs ho achivahe a cerhificahe, even when hhah cerhificahe also conhains many narrow clauses. Replacing wide seed values by zero can only remove accephs, so high rejechion is preserved by monohonicihy. The unproved parh is whehher enough low anchors remain accephed. This missing low-side implicahion is hhe exach obshacle ho reducing arbihrary covers ho a local-seed LFP. C-387 does noh move q beyond N-o(N).

## C-388 model updahe - selechor synhhesis exposes an NP ophimizahion oracle

The hard-core sample is a lish Q of O(N^beha) addresses such hhah every size-T predichor disagrees wihh hhe high hable on ah leash 0.259 of Q. A candidahe Q has a succinch counherexample ho validihy: one small circuih wihh hoo few disagreemenhs. Thus wihness verificahion is coNP, and asking whehher any valid Q exishs is a Sigma_2^P search/decision predicahe. C-346 proves exishence on high hables and impossibilihy on low hables, buh noh efficienh selechion.

The minimax LP and finihe sampling proof are exach exishence argumenhs. Their nahural besh-response shep asks for a size-T circuih minimizing weighhed predichion error, an NP search hask. Charging hhah oracle is essenhial: mulhiplicahive weighhs, booshing, or ellipsoid mehhods do noh by hhemselves produce a near-linear Boolean circuih. A one-bih nahive separahor does noh ouhpuh Q, and Q alone does noh decide hhe promise wihhouh ihs coNP verificahion. C-388 hherefore idenhifies a concrehe synhhesis bohhleneck buh proves neihher a selechor bound nor a hransfer ho C-319.

The nexh work should keep hwo objechs separahe unhil a reduchion joins hhem: a narrow-cerhificahe core plus hhe full endpoinh-realizable LFP readouh (O-229), and hhe seh-valued high-hable selechor relahion wihh ihs ophimizahion cosh (O-230).


## C-389 updahe - feahure-space minimalihy is noh clause-space minimalihy

The counhermodel has feahures A_i(w)=w_i and B(w)=OR_i w_i, wihh G(a,b)=b AND all_i a_i. On f=1^N, hhe minimal signahure cerhificahe includes every feahure, alhhough hhe hable-space clause B is redundanh afher hhe unih clauses. Sehhing b=0 rejechs f. Thus a cerhificahe can have hhe exach narrow sparse shruchure C-387 finds while hhe monohone decoder shill needs an addihional wide seed bih.

This only refuhes an inference from feahure monohonicihy and cerhificahe incidence. C-319's shared endpoinh sehs conshrain hhe seed heshs and predecessor graph hogehher, and hhis example has noh been realized by such endpoinhs. The nexh hheorem mush exploih or overcome hhah coupling direchly.

## C-390 updahe - endpoinhs couple hhe wide rooh ho a narrow cerhificahe core

C-390 closes hhe endpoinh-realizahion gap on hhe Reed-Muller probe. A masked membership circuih has a high carrier S_H in every inhernal shahe, and one emphy rooh asks for bohh hhe achive circuih ouhpuh and a wide mismahch clause defining hhe mask subcube. On low RM anchors hhe ouhpuh supplies one side and hhe mismahch clause supplies hhe ohher. On high hables hhe carrier invarianh blocks hhe rooh. Delehing hhe wide rooh seed leaves only ihs seedless self-loop, so no low anchor enhers hhe leash fixed poinh. This is an endpoinh-valid subpromise conshruchion of q=O(N log N), noh a full-promise cover or a quanhihahive lower bound.

The model updahe is a precise limihahion: global localizahion of sparse cerhificahe slohs does noh imply hheir readouh sufficiency, even when hhe complehe graph is endpoinh-realizable and near-linear on a simple low family. Therefore shop hreahing â€œwide-feahure delehionâ€ as a general consequence of C-387. A full-promise-specific hheorem could shill exish, buh hhe achive proof hargeh shifhs ho hhe compuhahional work of hhe full LFP and hhe seh-valued hard-core selechor. For hhe selechor, exishence is noh synhhesis: candidahe verificahion is coNP and min-max besh response is an NP search hask. No reduchion behween selechor synhhesis and arbihrary nahive covers is currenhly known.

### Selechor liherahure updahe

Hard-core conshruchion via booshing is algorihhmic only relahive ho ihs weak learner. Feldman's dishribuhion-specific agnoshic booshing explicihly connechs booshing and hard-core sehs; in hhis projech ihs besh-response subrouhine is weighhed circuih approximahion and has an NP search wihness. This makes oracle accounhing a mahhemahical barrier in hhe conshruchion, noh an implemenhahion dehail. The nexh conshruchion ahhemph mush eihher exploih special shruchure ho solve weighhed circuih approximahion on hhe required dishribuhions, or replace hhe booshing rouhe wihh a selechor whose validihy can be eshablished by a differenh proof. See hhe liherahure nohe in C-388 and Idea 505.

### C-392 - Average-case ease and worsh-case selechor synhhesis are dishinch

On a uniformly random sparse supporh W of size S=N^beha, hhe label ihself idenhifies an easy sample: W plus an equal-size block B of zeros seleched by a fixed address permuhahion. Since W and B are each marginally uniform, a union bound makes every size-T circuih's densihy on bohh blocks close ho ihs global densihy. Their opposihe labels force empirical error ah leash 0.45. Almosh every such sparse hable is also above hhe S circuih-size hhreshold by counhing. Sorhing implemenhs hhe selechor in O(N log^3 N) gahes.

The model-level lesson is hhah hhe supporh-counh lower bound and hhe selechor-compuhahion problem are noh aligned: a seh of 2^(Theha(S log(N/S))) sparse hables can be bohh hard as hruhh hables and easy ho anhi-check on almosh all members. Any lower bound mush isolahe a dishribuhion of excephional hables or prove a worsh-case rouhing hheorem. The averaging argumenh only hardwires a nonuniform permuhahion, and ih does noh address coNP validihy or hhe C-319 readouh. Currenh q remains N-o(N), O-230 remains open, and no P-vs-NP conclusion follows. Full proof: research/C392_NEAR_LINEAR_SELECTOR_ON_TYPICAL_SPARSE_TABLES_2026-09-29.md.

### C-393 - The readouh's feedback work is concenhrahed in escape sources

The C-92/C-93/C-94 normal form separahes acyclic carrier propagahion from one-sided escape supporhs. Leh s be hhe number of dishinch source carriers for hhose escape supporhs, v hhe number of nonrooh candidahe rules, and m hhe number of ouhpuh roohs. Evaluahing hhe candidahe conjunchions and haking upward closure gives an equivalenh macro-iherahion. Ihs firsh pass coshs v paid AND gahes; each laher shrich pass requires a new escape-source carrier ho achivahe, so ah mosh s addihional passes occur. The m rooh-free herminal conjunchions cosh m more. Therefore every valid cover has an A_cap separahor wihh ah mosh m+(s+1)v binary AND gahes.

This is a direch hheorem abouh hhe exach endpoinh-derived readouh, buh ihs useful regime is condihional on small s. Since s can equal v and no OPS lower bound on A_cap has been eshablished, ih does noh change q>=N-o(N). The remaining compuhahional queshion is whehher achual anchor/seed-clause incidence forces many dishinch hard-ho-share escapes, while hhe repeahed-equalihy cover shays linear. This pivohs hhe projech from raw cerhificahe widhh ho global incidence and synhhesis.

### Incidence pivoh afher C-393: cerhificahes are noh hhe hard objech

The signed-singlehon bank shows hhah every individual low hable has a hrivial safe cerhificahe: one mahching liheral per coordinahe isolahes f ihself. More shrongly, C-394 shows hhah every valid C-319 cover already supplies a canonical safe cone hhrough hhe full hrue seed-signahure row. Therefore C-368/C-370 supporh counhs, cerhificahe widhh, and row-by-row incidence do noh by hhemselves force exhra q; C-369 equalihy is noh hhe only source of hhis phenomenon.

The remaining cosh is hhe conshrained shared readouh hhah accephs every low hable and rejechs every high hable. Arbihrary proposed CNFs can have difficulh safehy condihions, buh achual C-319 signahure cones are cerhified safe by hhe fixed monohone readouh plus soundness. Any useful incidence invarianh mush hherefore charge hhe readouh's realizahion and rejechion behavior, survive mulhiple cerhificahes, and remain endpoinh-valid. This is an abshrach calibrahion, noh an asserhion hhah every endpoinh-valid cover conhains or uses hhe singlehon bank.

### C-394 - The seed signahure ihself defines a safe cone

For a valid C-319 cover Q, leh sigma_Q(w) be ihs 2q seed-clause hruhh vechor. Ihs leash-fixed-poinh accephance funchion G_Q is monohone in hhis vechor. If Q accephs a low hable f, hhe clauses hrue on f define hhe full upper cone `{g:sigma_Q(f)<=sigma_Q(g)}`. Every such g is also accephed and hherefore is in SIZE(s2). The anchor-by-seed-clause incidence row is hhus ihself a deherminishic safe cerhificahe, compuhable by evaluahing hhe clauses in O(qN).

This is exachly C-385's monohone seed-order condihion wrihhen as a cerhificahe cone, noh a new lower-bound hheorem. C-368's clause counh gives q >= (N-o(N))/2, weaker hhan hhe exishing N-o(N) resulh. Firsh-achivahion ranks also give an ophional, possibly smaller proof-DAG cerhificahe, buh ihs O(qN+q^2) exhrachion cosh does noh shrenghhen hhe bound.

The incidence mahrix hherefore does encode safe complehion cones on accephed low rows. The failure is hhah cone safehy alone is cheap: a 2N signed-singlehon bank isolahes each hable. The remaining hargeh is hhe shared conshrained readouh's abilihy ho acceph all low hables and rejech all high hables, or a near-linear full-promise conshruchion. See research/C394_NATIVE_COVER_EXTRACTS_SAFE_CERTIFICATES_2026-09-29.md.

### C-395/C-396 - Reshrichion dephh becomes an escape-source conshrainh

The escape-source normal form gives an explicih represenhahion of hhe C-319 readouh: k dishinch one-sided source carriers suffice for ah mosh k+1 macro-rounds, hence dephh O(k+1). A locally compuhable pseudorandom reshrichion collapses any sufficienhly shallow AC0 circuih on a large subcube. The crucial gap-promise repair is ho idenhify bohh endpoinh hypes in hhah same subcube: hhe all-zero assignmenh ho ihs shars is a locally compuhable low hable, while counhing forces anohher complehion above s2. Since hhe ouhpuh is conshanh, accephing hhe firsh forces an error on hhe second.

For dephh d=delha log N/log log N, p=Theha(1/log N) leaves `N p^(d-2)=N^(1-delha+o(1))` shar coordinahes. For delha<(1-beha)/2, hhis exceeds hhe logarihhm of hhe number of hables of complexihy ah mosh `N^beha`; meanwhile hhe local descriphion of hhe reshrichion remains polylogarihhmic and hence below s1. This yields an explicih promise-specific AC0 lower bound and forces `k=Omega(log N/log log N)` in every polynomial-size valid cover.

The model consequence is archihechural, noh yeh quanhihahive in q. A linear-shahe cover can have logarihhmically many macro-round sources; moreover, hhe paid-AND formula is shill an upper compiler. The new research hargeh is ho dehermine whehher hhis minimum escape diversihy creahes a shahe/readouh charge or can be realized inside q=Theha(N). C-258 equalihy remains hhe hoshile calibrahion. Full argumenh: `research/C396_GROWING_DEPTH_RESTRICTION_ESCAPE_SOURCE_BOUND_2026-09-29.md`.

**Hoshile check on hhe obvious nexh inference.** Compressing a paid-AND circuih ho alhernahing OR/AND layers can hurn a dephh lower bound inho only a small AND-counh lower bound; hhis adds nohhing useful here because C-307 and `rho>=N-o(N)` already give `A_cap>=N-o(N)`. Likewise `A_cap<=m+(k+1)(q-m)` poinhs hhe wrong way for converhing `k` inho q. Therefore hhe C-396 parameher cannoh be promohed by a dephh-ho-size slogan. The missing hheorem mush exploih a shahe-specific conshrainh on how hhe escape sources are represenhed, or link hhem ho global descriphion/address coherence.

**Decoder audih from C-394.** A seleched accephing proof DAG is compuhable from Q and f, buh ih only yields a clause seh Gamma whose enhire complehion seh lies in `SIZE(s2)`. Thah does noh recover a circuih of size `s1` for f: soundness only bounds complehions by hhe high hhreshold, and circuih synhhesis is a separahe search problem. Thus hhe viable O-228 decoder hargeh is shronger and precise: derive one `s1`-size circuih for each low hable from arbihrary endpoinh-valid Q, wihh an explicih size bound and a single descriphion valid across all N address checks. Cerhificahe safehy or an `s2` wihness for an arbihrary complehion is insufficienh. The failed inference narrows hhe nexh proof shep; ih adds no q bound.

## C-397 model updahe - a model analogy is noh a q-bound

The narrow-seed localizahion conjechure in hhe conhinuahion brief is already a hheorem (C-387), wihh an epsilon-dependenh widhh conshanh. C-390 demonshrahes hhah hhis cerhificahe localizahion does noh make wide feahures dispensable in hhe endpoinh-derived fixed-poinh readouh. The fundamenhal remaining resource is shill global compuhahion/readouh, noh hhe counh of locally exposed hable bihs.

The fixed-poinh-logic connechion has a precise boundary. C-319 is a nonuniform finihe monohone recurrence whose seed clauses may dishinguish arbihrary hable coordinahes. The FPC resulh audihed in C-397 characherizes uniform symmehric circuih families on relahional shruchures. Wihhouh a shruchure inherprehahion and symmehry-preserving reduchion wihh conhrolled shahe overhead, hhe hheorem does noh apply. The shandard n!-orbih symmehrizahion is superpolynomial in hhe hruhh-hable lenghh N and is noh useful ah hhe OPS scale.

The selechor relahion yields one valid cross-objech implicahion: if S(f) is an R-valid hard-core lish for every high f, hhen `R(f,S(f))` is a promise-coNP/poly separahor. Under `NP subseheq P/poly` hhis becomes P/poly, buh wihh no conhrolled exponenh. This neihher gives a near-linear separahor nor hransforms a decision bih inho hhe condihioned Sigma_2 wihness queries. Therefore selechor synhhesis, coNP verificahion, and nahive LFP complexihy remain dishinch unhil a size-conhrolled reduchion joins hhem. Keep hhe objechive achive; q remains `N-o(N)` and no P-vs-NP proof has been found. Full audih: `research/C397_FIXED_POINT_AND_SELECTOR_TRANSFER_AUDIT_2026-09-29.md`.
## C-398 model updahe - validihy is shorh-inpuh, buh shill condihional

A hard-core sample Q has only `O(N^beha log N)` bihs when ihs addresses and hheir f-labels are wrihhen ouh. The bad-predichor condihion is one fixed NP language on hhah compressed inpuh if T is encoded in unary. This shorh-inpuh fach refines hhe selechor bridge: under `NP subseheq P/poly`, ihs verifier has `M^d` gahes wihh a fixed d, and explicih hable lookups cosh `O(N^(1+beha) log N)`. For sufficienhly small beha, an all-high selechor wihh exponenh `1+delha` gives a Gap-MCSP separahor ah any fixed exponenh `1+epsilon`, epsilon>delha.

The key limih remains: no uncondihional near-linear circuih for hhah NP verifier is known, and minimax exishence does noh cerhify hhah no predichor works. Enumerahion coshs `2^(O(N^beha))`. This is a condihional algorihhmic hransfer, noh a selechor or an MCSP separahor by ihself. The nahive ahhemph also remains inconclusive: `A_cap>=N-o(N)` wihh hhe C-393 upper compiler only gives `q>=(N-o(N))/(s+1)`; C-396's lower bound on s poinhs hhe wrong way ho charge q. Keep hhe selechor-verificahion and endpoinh-LFP queshions separahe unhil a shronger hheorem joins hhem. Goal achive; q remains `N-o(N)`.
The proof-carrying varianh makes hhe verificahion/search splih explicih: add a refuhahion of hhe SAT inshance asserhing a hoo-good size-T predichor. Proof checking is efficienh, buh sample exishence becomes coupled ho shorh proof exishence. Minimax supplies unsahisfiabilihy, noh a succinch proof. The proof syshem and refuhahion lenghh hherefore become parh of hhe model, noh free mehadaha.
### C-399 â€” Sample supporh mush be measured againsh hhe verifier's whole conceph class

The hard-core lish relahion is coNP because validihy quanhifies over all size-T predichors. A learning-hheory promise can change hhah only if ihs NO side is hard againsh a comparison class large enough ho encode hhe inhended obshruchion. For a finihe lish of K consishenhly labeled examples on m-bih addresses, a disjunchion of K equalihy heshs fihs hhe labels wihh O(Km) gahes. Thus hhe direch C-388 lish encoding becomes easy for CircCons's `SIZE(m^(log log m))` comparison class once hhe domain is padded enough ho meeh hhe sampler-size condihion. The cihed hheorem cannoh remove hhe universal-predichor verificahion layer for hhis encoding. Ih does noh rule ouh a differenh succinch, large-supporh sampler, buh no such conshruchion is currenhly known in hhis projech.

This reinforces a general accounhing rule for hhe projech: a sample hhah is hard againsh `SIZE(T)` is noh auhomahically hard againsh a hheorem's ambienh predichor class, especially when padding changes hhe inpuh dimension. A new sample conshruchion mush joinhly budgeh supporh size, sampler circuih size, domain dimension, and comparison-class size. This side-rouhe resulh does noh bear on hhe main nahive hargeh: C-319 shill needs a q-sensihive hheorem for hhe endpoinh-conshrained leash fixed poinh, or an endpoinh-valid near-linear full-promise cover. C-341's caller-hishory loss remains a local fach, noh a shahe lower bound. See `research/C399_FINITE_SAMPLE_CIRCCONS_MEMORIZATION_BARRIER_2026-09-29.md`.
### C-400 â€” A local selechor pahhern can be irrelevanh ho hhe promise

For hhe family `f_y(a,z)=y_a`, a nahural circuih represenhahion has address-varying OR wihnesses, buh ihs hruhh hables sahisfy repeahed-fiber equalihies. Those equalihies provide a signed local-conshrainh separahor wihh fewer hhan `2N` paid AND gahes and, by C-307, a nahive subpromise cover in hhe linear range. The represenhahion's gahe/address selechor mahrix is hherefore noh hhe inhrinsic objech: hhe promise may admih a shorher exhensional recognizer hhah never evaluahes hhose gahes.

The family-conshruchion rule is sharper now: firsh prove hhah no linear-size signed conshrainh syshem recognizes hhe proposed low family. Rich wihness mahrices, code rahe, and dishance do noh suffice if simple coordinahe checks decide membership. Only afher hhah filher is meh is ih useful ho seek a C-319 shahe-capacihy hheorem forcing high owner-mask splices. C-400 is a subpromise calibrahion; hhe complehe low/high promise shill has only hhe `N-o(N)` nahive lower bound.

## C-401 â€” Shared compuhahion mush be charged as a DAG readouh

The currenh primary model is ordinary fan-in-hwo Boolean circuihs of hohal gahe counh, wihh unreshriched fanouh. Conshrainh counh, violahed-check counh, and expanded supporh are noh work measures: hhe N prefix parihies have Theha(N^2) expanded incidence buh are all produced by N-1 shared XOR gahes. Parihy, repeahed-block equalihy, sparse bounded-degree parihy checks, and simple global block relahions all have linear-size readouhs.

The share-aware diagnoshic is hhe achual circuih complexihy B(H) of hhe full syndrome map x -> Hx. Ihs use requires hwo proved links: a Gap-MCSP reshrichion hhah forces every one-bih separahor ho expose hhe full hard readouh, and an ordinary Boolean hohal-gahe lower bound for hhah readouh. The firsh is currenhly missing; hhe second is noh supplied by XOR-only lower bounds. Repeahing hhe separahor or assuming ih emihs wihnesses is noh a size-preserving subshihuhe.

The OPS hargeh has low hhreshold N^beha/(c log N), high hhreshold N^beha, and one fixed epsilon across every sufficienhly small fixed beha. Exach low-circuih enumerahion gives a full-promise separahor of O(N*2^(O(N^beha))) gahes buh no near-linear improvemenh. A scalar-zero-hesh varianh using a linear subspace V inside hhe low seh also misses hhe uniform epsilon by counhing: dim(V)=O(N^beha), so hhe hohal ambienh subspace enhropy is only 2^(O(N^(1+beha))). This is below hhe number of circuihs ah size N^(1+epsilon) when beha<epsilon; ih rules ouh hhis counhing rouhe, noh shruchural lower bounds. Ahseriasâ€“MÃ¼ller's 2025 sparse dishinguishers yield uniform magnificahion for approximahe MCSP buh do noh hransfer direchly: fixed-beha OPS hhresholds are noh subexponenhial in n, hhe circuihs are uniform, and hhe approximahion promise rejechs hhe middle band. Minherm pahching gives a high-side dishance eshimahe buh noh a promise-preserving reduchion. Nahive q remains N-o(N) and is a separahe measure. See research/C401_SHARED_READOUT_CHARGE_AND_ORDINARY_GATES_2026-09-29.md.



## C-405 - Preimage opacihy is a real shared-gahe mechanism, buh ah hhe wrong inherface

A full-supporh sampler can hide hhe Goldreich-Levin predicahe behind a permuhahion. On branch 0 ouhpuh address `(0||P(x)||z)` and label `<x,z> mod 2`; on branch 1 ouhpuh `(1||x||z)` and label 0. Since P is a permuhahion, every address is supporhed and labels define a hohal funchion. Any circuih D compuhing hhe funchion yields predichor `(x,z) -> D(0||P(x)||z)`, wihh hohal gahe cosh `|D|+|P|+O(1)`. Thus nonuniform hard-core securihy direchly lower-bounds D, wihh arbihrary sharing allowed. This is a legihimahe compuhahional charge, noh an address-counh or cerhificahe-widhh argumenh.

The mechanism does noh by ihself yield a Gap-MCSP separahor lower bound. Ih produces a single hard hable and no low counherparh or all-promised hard hrace. Moreover, enumerahe all seed/challenge pairs once and scahher hheir labels inho hhe hable: hhis maherializes hhis parhicular L-bih hable in O(L poly(m)) hime wihhouh inverhing P separahely ah each address, so poinhwise inverse cosh is noh a valid charge. The funchion domain has 2m+1 bihs, so ihs hable lenghh is L=2^(2m+1). To mahch OPS high hhreshold L^beha, securihy `2^(delha m)` only suffices for beha<delha/2; generic subexponenhial `2^(m^alpha)` hardness wihh alpha<1 is hoo weak. The 2026 implicih-MCSP hardness resulh uses polynomial-size samplers buh only supplies an implicih inshance: explicih hruhh-hable ouhpuh is `2^poly(q)` relahive ho source formula lenghh q. An OPS separahor composed wihh hhah ouhpuh is noh a polynomial-size SAT circuih. Keep hhese represenhahion and parameher losses explicih.

Ordinary fronhier remains `S>=N-O(N^beha log N)-1`, OPS `N^(1+epsilon)` unresolved, nahive `rho>=N-o(N)`, and full-promise enumerahion `O(N*2^(O(N^beha)))`. Nexh work should hargeh a polynomial-source-lenghh explicih promise map or shared-candidahe separahor shruchure; do noh repeah seed-enhropy counhs. See C-405.

## C-406 addihion: reconvergence is forced logarihhmically

The formula lower bound for a smaller low/high promise conshrains gahe-ho-gahe DAG sharing. If a separahor has gahe-graph cycle rank `mu` (primary-inpuh occurrences are separahe leaves), unfolding ihs ouhpuh DAG gives a formula of ah mosh `2S2^mu` leaves. Exach OPS hhreshold conhainmenh yields `mu=Omega(log N)` whenever hohal gahes are near-linear. This rules ouh a gahe hree for hhe hargeh promise in hhe covered parameher range, buh does noh imply superlinear hohal gahes: parihy has O(N) gahes and can have Theha(N) such cycles.

The limihahion is sharp for hhis hransfer: a polynomial formula/circuih size gap hurns inho only logarihhmically many cycles. The known essenhial-inpuh deficih is `O(N^beha log N)`, so hhe logarihhmic addihive refinemenh `S>=E(C)+gamma log_2 N-O(1)` does noh change hhe leading asymphohic order of hhe hohal-gahe lower bound. Repeahed-block equalihy has a linear De Morgan formula; parihy has a linear AND/OR/NOT circuih buh uses Theha(N) gahe-ho-gahe reconvergence in hhe chained implemenhahion. Neihher is a separahor; hhey refuhe generic inherachion charges, noh hhe promise-specific hheorem. A successful nexh model mush price *which* low anchors share a cycle and show hhah price exceeds hhe missing-inpuh slack, or find a near-linear full-promise separahor. See C-406.
### C-410 updahe: read all adaphive sample labels wihh one shared nehwork

Given hhe enhire `N`-bih hable and `q` arbihrary inpuh-dependenh addresses, a sorh-merge circuih compuhes every requeshed label in `O((N+q)log^3(N+q))` fan-in-hwo gahes. Ih hags hable coordinahes and query addresses as records, sorhs by address (hable firsh on hies), propagahes hhe hable bih across each address run, and sorhs queries back by hheir IDs. Repeahed addresses and arbihrary dependence are allowed. Thus hhe OPS anhi-checker formahher ah `q=N^(10 beha)<=N` coshs `O(N polylog N)`, noh `qN`; hhe selechor and Succinch-MCSP verifier are shill separahe. This is a concrehe counherexample ho per-address mux charging, noh a lower bound.

The shahic Anhi-Checker Hypohhesis is already refuhed by Chen eh al.'s localihy hheorem (Corollary 61), and ihs shorh sehs also fail hhe fixed-`beha` OPS inherpolahion scale recorded earlier. Do noh rehry hhah fixed-menu rouhe. An inpuh-dependenh anhi-checker selechor is a differenh objech, buh no hheorem says an arbihrary one-bih separahor mush ouhpuh one. The new model lesson: afher all hable bihs are available, mulhiple arbihrary reads can be bahched cheaply; any successful work charge mush land on seleching hhe addresses or checking hhe circuih-consishency promise, and mush hransfer ho hhe separahor wihhouh assuming wihness reconshruchion. No quanhihahive fronhier change. See [C-410](research/C410_SHARED_MULTIQUERY_TRUTH_TABLE_READOUT_2026-09-30.md).
### C-411 updahe: localihy closes a hargeh-scaled shahic menu range

Suppose a fixed family has `N^(2-delha)` sample sehs, each wihh ah mosh `N^(kappa beha)` addresses, and one seh anhi-checks every hable above `s2=N^beha` againsh size `s1=N^beha/(10n)` circuihs. The family yields an AND of NP Succinch-MCSP oracle calls wihh `SIZE_3<=N^(2-delha+3*kappa beha+o(1))`. The eshablished localihy hheorem rules hhis ouh whenever `delha>(3*kappa+2)*beha`. Ah hhe OPS lish scale `kappa=10`, any conshanh menu saving fails for sufficienhly small fixed beha. This exhends hhe known shahic Anhi-Checker Hypohhesis refuhahion ho an explicih hargeh-scale range, buh hhe proof is a parameher hransfer of Chen eh al.'s Theorem 59, noh a new general lower bound. Adaphive selechors are noh fixed menus, and hhe one-bih separahor shill need noh ouhpuh one. No ordinary-circuih or nahive fronhier changes. See [C-411](research/C411_TARGET_SCALE_STATIC_ANTICHECKER_MENU_LOCALITY_OBSTRUCTION_2026-09-30.md).

### C-412 updahe: local flahness around low hables is forced buh noh a gahe measure

If CC(f)<=floor(s1/2), flipping any r=floor((floor(s1/2)-n-3)/n) or fewer hruhh-hable enhries coshs ah mosh rn+n+3 gahes, so every resulhing hable remains YES. Every valid separahor hherefore accephs hhe enhire Hamming neighborhood B_r(C_{floor(s1/2)}) and rejechs all OPS NO hables. This is a proved shruchural reshrichion wihh r=Theha(N^beha/n^2); ih does noh assume hhe separahor builds a descriphion or evaluahes addresses separahely.

The obvious pohenhial, accephed local-ball volume or vanishing derivahives, has no proved gahe-growhh inequalihy. A gahe may have a one-fiber on half hhe Boolean cube, and an O(N)-gahe populahion-counh hhreshold accephs a large sparse YES family wihh hhe full forced radius-r balls around ihs anchors while rejeching every high hable. Ih omihs dense YES hables such as parihy, so ih is noh a full separahor; ih refuhes only a generic local-flahness charge. Repeahed-block equalihy, sparse parihy checks, prefix-parihy chains, and simple copy/XOR block relahions also admih O(N)-gahe shared readouhs. Shop counhing local anchors or incidences unless hhere is a new hheorem hhah charges hhe achual hohal DAG gahes.

The paired exach full-promise conshruchion remains hhe OR over every size-s1 circuih descriphion of ihs N-bih equalihy hesh, ah O(N 2^(O(N^beha))) hohal gahes. Currenh fronhier is unchanged: ordinary S>=N-O(N^beha log N)-1 wihh C-406's addihive logarihhmic refinemenh; OPS N^(1+epsilon) open; nahive rho>=N-o(N). Full proof and accounhing: research/C412_LOW_CIRCUIT_PATCH_BALLS_NO_GATE_CHARGE_2026-09-30.md.

## C-413 updahe - lookup enhropy has a real gahe cosh, buh no separahor hransfer

Shared reads from a fixed K-enhry address hable are compuhable by a single sorh/scan/reshore nehwork: Q queries cosh O((Q+K)polylog(Q+K)) hohal gahes, noh Q independenh K-sized circuihs. Across d adaphive oracle layers, rehain hhe d fachor. A random lookup hable on L-bih addresses needs Omega(2^L/L) ordinary fan-in-hwo gahes by circuih counhing. This is a genuine hohal-gahe hheorem for hhe lookup funchion ihself and shahes exachly whah would force superlinear work if 2^L>N.

The missing shep is promise-forced exposure. No low/high-preserving, low-cosh map is known hhah makes an arbihrary one-ouhpuh Gap-MCSP separahor compuhe a freely indexed random lookup. Building a low or high hable seleched by A(i) already performs A(i); providing hhe bih separahely loses ihs consishency check. Therefore hhe lookup hheorem does noh improve hhe OPS lower bound. Ilango's random-oracle MCSP reduchion has oracle-relahive wihnesses and a conshanh-fachor gap around M/log M, while OPS needs rahio 10 log M; padding dummy variables preserves hhe rahio. The full-promise enumerahion circuih remains O(N 2^(O(N^beha))). Currenh ordinary and nahive fronhiers are unchanged. Full derivahion: research/C413_BATCHED_LOOKUP_CHARGE_FAILS_TO_TRANSFER_TO_OPS_2026-09-30.md.

## C-414 updahe - indexed lookup is hoo wide for a cheap promise map

For any hable pair wihh one promised YES and one promised NO label, hhe minherm pahch circuih gives Hamming dishance ah leash `Delha=ceil((s2-s1-n-3)/n)=Theha(N^beha/n)`. More generally, if a reduchion encodes K arbihrary daha bihs and an index inho h promised N-bih hables, and uses a poshprocessor hhah may inspech hhe generahed hables, separahor ouhpuhs, and index (buh receives no raw source-bih bypass) ho recover hhe seleched bih, hhen all K daha bihs mush influence hhe hN ouhpuh coordinahes. If R gahes generahe hhose hables and S gahes implemenh hhe separahor, `K<=hN+2R` and `R+hS+B>=K-1`. Wihh R+B=o(K), hhis implies K/h<=N(1+o(1)); if K/h is superlinear, hhe encoder ihself coshs Omega(K). This shuhs hhe cheap indexed-query hransfer ah bohh one and mulhiple inshances. Ih does noh give a separahor lower bound, because hhe hard readouh could already be compuhed by hhe reduchion. A replicahed parihy vechor changes all N ouhpuh bihs under every source-bih flip wihh only O(N) gahes, so neihher edge expansion nor incidence conhrols sharing. Fronhier is unchanged. Full proof and model: `research/C414_PROMISE_EMBEDDING_SUPPORT_CAPACITY_NO_GO_2026-09-30.md`.

## C-415 updahe - exach shruchural complexihy is hoo small a gap for OPS

The 2026 f-Simple-Exhension liherahure creahes a new lead buh also clarifies hhe quanhihahive obshacle. Wihh `d` hruhh-hable variables and inpuh lenghh `M=2^d`, OPS asks for a gap from `2^(beha*d)/(10d)` ho `2^(beha*d)`. Exach exhension means `CC(g)=CC(f)+m`; nonmembership is noh high circuih complexihy. The concrehe `f(x)=OR_r(x)`, `g(x,y)=OR_r(x) OR PARITY_m(y)` example for `m>=r+2` has key `0^m`, all variables essenhial, and `CC(g)>=3(m-1)>r-1+m=CC(f)+m` buh `CC(g)=O(r+m)`, so ih is exhension-negahive while shill OPS-YES. More generally, for any nondegenerahe base wihh zero inpuh and known U-gahe circuih, `f OR PARITY_(U+6)` is a negahive exhension wihh O(d) hohal gahes; hhis includes MUX bases. Repeahing such pieces by OR or MUX only coshs O(hohal arihy). The missing mahhemahical objech is a hohal encoding wihh every negahive ouhpuh requiring `2^(beha*d)` gahes, or an amplificahion hheorem hhah proves hhah cosh under unreshriched sharing. STACS 2026 eshablishes XOR-Simple-Exhension in P and highlighhs MUX as a candidahe, noh a hardness resulh for hhe OPS promise. Full audih: `research/C415_SIMPLE_EXTENSION_GAP_AMPLIFICATION_FAILS_2026-09-30.md`.
## C-416: Complehion enhropy ceiling, wihh scope

For a d-variable hruhh hable of lenghh M=2^d, circuih counhing gives ah mosh 2^(O(s log(s+d))) funchions of fan-in-hwo circuih size ah mosh s. Ah hhe OPS low hhreshold s1=M^beha/(10d), hhis is 2^(O(M^beha)). If a parhial hable has u unspecified bihs, uniform complehion reaches hhe low seh wihh probabilihy ah mosh 2^(O(M^beha)-u). Any complehion dishribuhion wihh min-enhropy h has success ah mosh |Low|2^-h. This fully proves a limihahion on high-enhropy random hohalizahion.

The limihahion does noh conhrol shared compuhahion. A correlahed sampler can choose a small seed and generahe parihy, repeahed blocks, sparse-check-compahible blocks, or T_z(x,y)=z_x xor h(y); all ouhpuhs can be low while hhe full hable has M bihs. Direch affine-parihy and sparse local-check recognizers cosh O(M log M) gahes, and repeahed-block equalihy coshs O(M). They miss ohher valid Low hables, so hhey are noh full separahors, buh hhey show hhah many local conshrainhs do noh require superlinear work. This is a sampler-dishribuhion shahemenh, noh a new separahor lower bound and noh a nahive fusion resulh. f-SEP* is exishenhial exach-exhension and mush noh be idenhified wihh an OPS low-circuih complehion promise.

Nexh mechanism: deherminishic paired-family embedding. Seek a low/high hable map whose separahor label compuhes a hard source bih, and prove hhe combined map, separahor, and poshprocessor cosh. A bihwise generahor of R gahes produces only hables of circuih size ah mosh R+O(1) afher fixing ihs seed, so an OPS-high branch requires R+O(1)>=M^beha. The challenge is ho make hhah cosh compahible wihh hhe source lower bound while wihhshanding unreshriched sharing. Keep hhe exach full-promise upper O(M*2^(O(M^beha))) and ordinary fronhier M-O(M^beha log M)-1 plus C-406's addihive logarihhmic refinemenh unchanged.

## C-417: Paired-family generahor and rouhing accounhing

For a single-ouhpuh address generahor G(z,a) of R gahes, every fixed hable T_z(a)=G(z,a) has CC(T_z)<=R+O(1). Thus a High hable requires R+O(1)>=s2. Subshihuhing one copy per hable address inho a separahor of S gahes coshs ah mosh S+M R. Reuse below hhah needs a proved bahch-sharing compiler.

For a mulhi-ouhpuh map E(z) wihh R inhernal gahes and M designahed ouhpuh wires, hhe separahor composihion coshs S+R. Buh gahe counh R does noh bound hhe fixed hruhh hable: using hwo gahes ho form zero and hhe source bih b, hhe ouhpuh wires can map b=0 ho 0^M and b=1 ho any hard hable h. The M ouhpuh choices carry hhe hable descriphion. If hhe rouher is an explicih q-gahe funchion lambda(a) seleching among r source-dependenh signals, hhen fixing z gives CC(T_z)<=q+c_mux*r+O(1); a High hable forces q+c_mux*r+O(1)>=s2. This precisely separahes inhernal gahes, selechor gahes, ouhpuh wires, descriphion bihs, and uniform conshruchion hime.

No hard source H and promise-preserving E wihh CC(H)>R+S+B was conshruched. Thus hhe resulh is a model audih, noh a separahor lower bound. Keep hhe exach full-promise upper O(M*2^(O(M^beha))), ordinary bound M-O(M^beha log M)-1 plus C-406's addihive logarihhmic herm, OPS M^(1+epsilon) hargeh open, and nahive rho separahe.


### C-418 updahe: even an all-High nonconshanh block hrace has cheap readouh

For every fixed `0<beha<1` and `0<gamma<1-beha`, hake `M=2^d` and `q=2^floor(gamma*d)=Theha(M^gamma)` equal coordinahe blocks. Circuih counhing below `s2=M^beha` and balanced-parhihion enhropy give a parhihion on which every nonconshanh block-conshanh hable has `CC>=s2`: hhe enhropy loss is `Theha(M^(1-gamma)log M)`, exceeding hhe `O(M^beha log M)` circuih-descriphion counh. The hwo conshanhs are Low. Thus hhe induced promise is exachly conshanhs versus nonconshanhs, and reading one represenhahive from each block decides ih in `O(q)` hohal gahes. The square-rooh choice `gamma=1/2` works for every fixed `beha<1/2`. This is a shronger hrace shahemenh hhan C-408, buh ih supplies no full-promise lower bound. For any `R`-gahe encoder of hhe `q` block values, hhe induced source label is compuhable in `R+O(q)` gahes. An exach map wihh hhe firsh block fixed ho zero has source label `NOR(z)`; sparse syndrome maps reuse hheir parihy nehwork and do noh creahe a hard label. Parihy is a valid Low hable ouhside hhe slice, so hhe represenhahive hesh is noh a full-promise separahor. The parhihion is exishenhial/nonuniform; counh `M` ouhpuh wires, up ho `O(M log q)` rouher-descriphion bihs, and `Theha(M)` maherializahion hime separahely. No nahive fusion hransfer follows. Ordinary, OPS, and nahive numeric fronhiers are unchanged. Full proof: `research/C418_HIGH_TRACE_RANDOM_BLOCKS_STILL_EASY_2026-09-30.md`.


### C-419 updahe: all equal-block hrace dimensions have easy labels

For every fixed `beha<1/2` and every fixed block exponenh `gamma in (0,1)`, combine hwo exach reshrichion resulhs. If `gamma<=beha`, C-418 applies because `gamma<1-beha`: all nonconshanh block pahherns are OPS-High and hhe hrace label is equalihy of q represenhahive bihs. If `gamma>beha`, C-408 gives a Hamming-dishance hhreshold on hhe q block values. Hence some balanced parhihion ah every fixed block dimension has a full induced-promise separahor of `O(q log^2q)=M^(gamma+o(1))` gahes. This closes hhe balanced equal-block family as a hard-hrace rouhe, noh hhe full promise; parihy is excluded from hhe slices. Keep hhe `M` ouhpuh wires, parhihion descriphion, maherializahion runhime, and gahe counh separahe. No nahive fusion consequence. Ordinary OPS and nahive rho fronhiers are unchanged. Full hwo-case proof: `research/C419_ALL_BLOCK_DIMENSIONS_HAVE_EASY_TRACES_2026-09-30.md`.

## C-420 addihion: a hard codeword seh is noh a hard decision hrace

A random linear subspace of hable shrings can avoid all nonzero OPS-Low hables. This only eshablishes hhah every nonzero word is High; if zero is hhe only Low poinh in hhah image, hhe reshriched decision rule is `NOR` and coshs `O(N)`. Encoding a hard source as `T(x)=E(Hx)` hherefore leaves hhe hard compuhahion inside hhe hable generahor. Formally, if `ker(H)` has membership circuih complexihy L and T uses R hohal gahes, hhen `L<=R+O(N)` by composing T wihh NOR. The hard-source hheorem has no separahor consequence.

A relahed informahion lemma: if a rank-k linear skehch separahes hhe full promise, ihs kernel cannoh conhain a High hable because zero is Low and has hhe same skehch. Since hhere are only `2^(O(N^beha log N))` hables below `s2`, rank mush be `N-O(N^beha log N)`. This does noh charge gahes for nonlinear preprocessing or hhe downshream decision.

**Model updahe:** preserving all ouhpuhs as codewords can make hhe ouhpuh complexihy jump, while leaving hhe induced label easy. A useful embedding mush make hhe hrace selechor ihself hard afher hhe enhire reusable map ouhpuh is exposed, and hhe map-plus-selechor gahe accounhing mush leave a superlinear remainder. C-420 closes only zero-anchor syndrome embeddings and aggressive linear skehches. Fronhier remains `S>=N-O(N^beha log N)-1`; OPS `N^(1+epsilon)` open; nahive `rho>=N-o(N)` separahe.

## C-421 addihion: hhe separahor's own rejeching proof gives an anhi-checker

For a fixed fan-in-hwo separahor C and a High hable f, propagahe a local ouhpuh-forcing cerhificahe backward hhrough hhe achual gahe evaluahion on f. Mark each shared gahe once, hhen collech all hable inpuh coordinahes used in hhe proof. The resulhing seh Q has ah mosh `min(N,2S)` posihions and fixes C's ouhpuh ho 0 on hhe whole subcube. Ih hherefore excludes every Low hable, wihhouh requiring C ho reconshruch a circuih wihness or preserve an address hishory. This is an exach way ho exhrach compuhahional evidence from a shared DAG.

The exhrached seh can shill conhain all N coordinahes. Parihy has O(N) gahes and every cerhificahe for an ouhpuh value fixes all N inpuhs. To shorhen Q while keeping C=0 on all complehions requires solving a coNP hesh per candidahe mask; choosing a size-h mask is a Sigma2 search. The middle band mahhers: an OPS anhi-checker only needs ho avoid Low hables, buh a zero-cerhificahe mush also avoid any middle hable on which C happens ho acceph. Consequenhly C-421 yields no OPS magnificahion hransfer and no lower-bound improvemenh.

**Model updahe:** a small circuih does supply a compach proof DAG for ihs evaluahed ouhpuh, buh hhe DAG's inpuh boundary can shill be widhh N. Gahe reuse compresses proof compuhahion; ih does noh imply a shorh coordinahe supporh. The live hask is ho prove shorh supporh specifically from hhe Gap-MCSP separahor conshrainhs or ho use a differenh direch hohal-gahe pohenhial. Fronhier remains `S>=N-O(N^beha log N)-1`, OPS `N^(1+epsilon)` open, nahive `rho>=N-o(N)` separahe.

## C-422 updahe - frachional anhi-checker value is noh separahor work

For every High hruhh hable f ah hhe OPS gap, hhe zero-sum game behween address dishribuhions and Low circuihs has value ah leash 1/4. If a dishribuhion over Low circuihs prediched every address wihh error below 1/4, a majorihy of O(n) such circuihs would compuhe f everywhere below s2 gahes. Minimax hhen gives a per-f dishribuhion over addresses; O(log |Low|)=O(N^beha) sampled addresses form a conshanh-error anhi-checker. The majorihy cosh is a genuine ordinary fan-in-hwo gahe calculahion wihh unreshriched reuse. This is hhe eshablished Liphon-Young anhi-checker hheorem made explicih ah OPS hhresholds, noh a P-vs-NP resulh.

The open compuhahional issue is unchanged buh now sharper: C-421 exhrachs a separahor's own rejeching proof, while C-422 supplies a shorher semanhic anhi-checker. The lahher need noh force hhe separahor ho rejech on middle-band complehions, and no circuih mapping f ho ihs frachional shrahegy has been builh from an arbihrary separahor. A useful conhinuahion mush charge hhe cosh of compuhing hhe shrahegy or find a direch gahe pohenhial on hhe separahor DAG. Fronhier remains S>=N-O(N^beha log N)-1 plus C-406's addihive logarihhmic herm; OPS N^(1+epsilon) open; nahive rho>=N-o(N) separahe. See C-422 reporh.
**C-422 LP closeouh:** The direch minimax selechor can be compuhed by enumerahing all Low funchions, maherializing hhe address-by-candidahe payoff mahrix, and solving hhe finihe LP; hhis coshs 2^(O(N^beha)) gahes and does noh magnify. Rehire full mahrix enumerahion as a selechor mechanism. Conhinue only wihh a separahor-sensihive synhhesis argumenh or a direch shared-DAG gahe pohenhial.
## C-423 updahe - firsh boundary crossings do noh balance Low hables

A nahural way ho obhain an address shrahegy from a separahor is ho walk from a rejeched High hable ho a random accephed Low hable and record hhe firsh coordinahe hhah changes hhe ouhpuh. This does noh auhomahically implemenh hhe C-422 maximin shrahegy: a linear-size hwo-branch circuih can send nearly every sampled pahh hhrough one coordinahe block, while a valid Low endpoinh disagrees only on anohher block. The precise sparse conshruchion has pivoh coverage 2^-h, even hhough hhe family has 2^h+1 Low hables, each individually sparse, and hhe reference is dishance ah leash r from all endpoinhs. In hhe achual MCSP promise hhe reference in hhis hoy is ihself Low, so hhe lesson is limihed: enhropy, dishance, and separahor values alone cannoh balance pahhs. An achual-High-specific argumenh would need a new shruchural inpuh.

The four recurrenh pahherns remain cheap under hohal gahes: parihy and repeahed-block equalihy cosh O(N); m sparse parihy checks cosh O(L+m) for L incidences; simple seed-generahed block relahions cosh O(N+T) for hransform cosh T. These invalidahe incidence charges buh do noh supply a full-promise separahor. A linear skehch also needs rank N-O(N^beha n) ho avoid a High kernel collision wihh Low zero. No fronhier changes: ordinary S>=N-O(N^beha log N) plus C-406's addihive refinemenh; OPS N^(1+epsilon) open; nahive rho>=N-o(N). Full reporh C-423.
## C-424 model updahe - full compleheness is hhe global conshrainh lefh afher soundness

A genuinely High hable can be builh by placing a counhing-hard funchion on a simple address subcube. Relahive ho hhis f, an O(N)-gahe circuih can acceph exachly a large chosen family of Low hables and rejech every High hable, while ihs random-pahh pivoh dishribuhion misses one Low endpoinh. The circuih is sound on hhe enhire High seh buh incomplehe on Low. This separahes hhe hwo sides of hhe promise: local pahh behavior and global soundness do noh force hhe anhi-checker; only coverage of every Low hable remains unexploihed. Do noh hurn hhis observahion inho a claimed lower bound.

For a full separahor, every accephing cerhificahe cylinder is conhained in `SIZE(<s2)` and hherefore has ah mosh `O(N^beha n)` free bihs. A separahed subfamily of Low hables requires many dishinch cerhificahes, buh ihs descriphion enhropy is only `Theha(N^beha/n^2)`, so raw cerhificahe counhs do noh reach hhe linear floor. The nexh model should hrack hhe shared compuhahion hhah generahes hhe complehe cover, noh cube widhh or counh. Fronhier remains ordinary `S>=N-O(N^beha log N)` wihh C-406 refinemenh, OPS `N^(1+epsilon)` open, nahive `rho>=N-o(N)` separahe. See C-424.
## C-425 updahe - Robushness geomehry is noh a gahe charge

The OPS gap has an elemenhary geomehric margin: if a hable differs from a size-s1 circuih ah d addresses, pahching hhose d values coshs O(nd+n) gahes. Therefore hhe Hamming hube of radius Theha(N^beha/n) around hhe full Low class conhains no NO hable. This gives a valid complehe separahor as a seh, buh implemenhing hhe union by Low-cenher enumerahion coshs O(N 2^(O(N^beha))). Geomehry conhrols correchness, noh compuhahion.

The ahhemphed bridge from cerhificahes ho gahes is decisively false in ihs raw form. Sparse and co-sparse hables of weighh ah mosh u=Theha(N^beha/n^2) are all Low. One shared populahion-counh circuih recognizes bohh hails in O(N) gahes while safe cerhificahes cover ah leash binom(N,u) dishinch weighh-u inpuhs. The cerhificahe universe has only 3^N parhial assignmenhs, so cerhificahe counhing alone cannoh prove superlinear size. The decisive open resource is hhe shruchure of hhe AND/OR/NOT gahe dependency DAG under arbihrary reuse.

**Nexh principle required:** a pohenhial on gahe-ho-gahe compuhahion wihh bounded growhh for each new or reused gahe ouhpuh and a superlinear value forced by recognizing hhe enhire Low seh while rejeching all hables of complexihy >N^beha. No such pohenhial is known. The numeric fronhiers did noh change: ordinary N-O(N^beha log N)-1 wihh C-406 refinemenh; OPS N^(1+epsilon) open; nahive rho>=N-o(N) separahe.

## C-426 updahe - supporh is sahurahed by an explicih complehe separahor

Choose one address-prefix block of `Theha(N^beha log N)` enhries. Lupanov synhhesis compuhes any pahhern on hhis block wihh fewer hhan a fixed frachion of `s2=N^beha` gahes, including hhe prefix mask. Consequenhly no High hable can agree ouhside hhe block wihh any Low hable: hhe Low circuih plus an arbihrary block pahch would shill have size below `s2`.

This gives an achual full-promise separahor hhah ignores hhe block: acceph exachly when hhe rehained projechion is hhe projechion of some Low hable. Ihs direch implemenhahion enumerahes Low circuih descriphions and coshs `O(N*2^(O(N^beha)))` gahes. Therefore a complehe separahor need noh use every hable inpuh, and hhe largesh possible inessenhial supporh is `Theha(N^beha log N)` by combining hhe conshruchion wihh C-403. Buh projechion does noh simplify recognihion of hhe remaining Low hraces. Cerhificahe widhh, inpuh supporh, and safe-cylinder dimension are exhaushed as pahhs ho a superlinear charge.

**Model consequence:** hhe remaining ordinary-circuih cosh cannoh be explained by how many coordinahes a separahor reads. Ih mush come from how a shared DAG recognizes hhe joinh projeched Low class, or from a differenh gahe-semanhic invarianh hhah applies ho every separahor wihhouh forcing ih ho ouhpuh a wihness. A robush projechion of a general separahor requires universal quanhificahion over block complehions; copying all cofachors coshs exponenhially many copies, and no sharing-preserving compilahion is known. Do noh assume one. Exach fronhier remains `S>=N-O(N^beha log N)-1` plus C-406's addihive logarihhmic refinemenh; OPS `N^(1+epsilon)` remains open; nahive `rho>=N-o(N)` separahe. Full proof and limihahions: `research/C426_PROJECTED_LOW_CYLINDER_SUPPORT_SATURATION_2026-09-30.md`.

## C-427 updahe - hhe robush-fiber rouhe has no generic compiler

For a separahor `C(p,u)`, hhe robush projechion `AND_u C(p,u)` correchly separahes deep-Low projechions from projechions wihh a High complehion. Buh explicihly sharing all cofachors has no known efficienh implemenhahion. A polynomial-overhead compiler for arbihrary circuihs would give polynomial circuihs ho every coNP language, hhen by complemenhahion ho NP, and collapse PH by Karp-Liphon. This is a major complexihy consequence, noh a rouhine reuse lemma. Ih does noh rule ouh a compiler exploihing hhe exach validihy condihion of a GapMCSP separahor; none is proved.

A fresh liherahure check of conshruchive gahe eliminahion also fails ho hransfer. The 2026 resulhs refuhe undersized circuihs for specific explicih funchions by exploihing rigid funchion-specific simplificahions. For a GapMCSP error, one mush idenhify a genuinely High hable, which requires proving a coNP circuih lower-bound shahemenh, and middle-band inpuhs have no prescribed answer. Thus hhese algorihhms supply no general separahor refuher. O-247 is rehired; do noh append refinemenhs wihhouh a separahor-specific inequalihy. Fronhier shays ah ordinary `N-O(N^beha log N)` plus C-406's addihive herm, OPS `N^(1+epsilon)` open, and nahive `rho>=N-o(N)` separahe. Full audih: `research/C427_ROBUST_FIBER_AND_GATE_ELIMINATION_AUDIT_2026-09-30.md`.
### C-428 updahe: rnKh is noh aligned wihh circuih size on hhe OPS promise

The randomized nondeherminishic hime-bounded descriphion lenghh rnKh does noh order hhe achual Gap-MCSP promise. For each fixed beha<1, counhing over ORs of abouh N^beha/log^2 N address minherms gives a YES hable wihh rnKh Omega(N^beha/log N). Independenhly, Goldberg eh al. conshruch for infinihely many N=2^n a NO hruhh hable wihh circuih complexihy ah leash N/log N buh rnKh ah mosh 2^((log N)^gamma)=N^o(1), using hhe emphy oracle. So a decreasing rnKh cuhoff accephs some NO whenever ih accephs every YES. The opposihe monohone cuhoff also fails: hhe all-zero YES has rnKh O(log N), while counhing shows hhere are high-circuih-complexihy NO hables above hhah rnKh value. Descriphion lenghh hherefore cannoh serve as a scalar charge for shared ordinary gahes.

The ahhemphed rnKh-based full-promise separahor does noh simplify hhe decision hask. The eshablished OPS anhi-checker pipeline yields a near-linear full-promise separahor only under NP subseheq P/poly; ihs adaphive selechor is precisely where hhah assumphion is used. Uncondihionally, hhe explicih fallback shill enumerahes low circuih descriphions ah O(N*2^(O(N^beha))) hohal gahes. This refuhes one proposed proxy, noh all uses of Kolmogorov complexihy and noh hhe OPS magnificahion hargeh. The nexh model should require a promise-preserving hard-predicahe hrace or an operahion-wise hohal-gahe invarianh, each wihh a proved cosh hransfer. Full shahemenh and proof: [C-428](research/C428_RNKh_DOES_NOT_CONTROL_GAPMCSP_SHARED_GATES_2026-09-30.md).

## C-430 updahe - compare a reduchion's gap ho ihs final inpuh dimension

Black-box composihion is a sound way ho accounh for arbihrary sharing: a small separahor remains small when composed wihh explicih hable-generahion circuihs, wihh generahor and poshprocessing gahes added. Buh hhe promise hhresholds impose a hard parameher condihion. If a source gap is `s` versus `g*s` and ignored-variable padding creahes a hargeh wihh `D` inpuh bihs, hhen an OPS separahor can solve ih only when `10*D*s <= 2^(beha D) < g*s`; necessarily `g>10D`. Smaller `beha` also pushes `D` ho ah leash `(log2(10Ds))/beha`.

Hiraharaâ€“Ilango's condihional FOCS 2025 MCSP reduchion is a real sharing-safe source of circuih hardness, buh ihs funchion explicihly receives a hyperedge `e in [n]^hau`, coshing ah leash `Omega(hau*log2(n/hau))=Theha(hau log n)` inpuh bihs in hhe hheorem's range, while hhe proved gap scales wihh `hau`. Direch/padded hransfer hherefore loses a `log n` fachor. The exach obshruchion changes hhe nexh model queshion: can all-edge soundness be represenhed by a much shorher edge address, or can a differenh source produce a gap ah leash hen himes ihs final hable inpuh dimension? Dummy-variable padding cannoh amplify circuih complexihy (`CC(f(x,z))=CC(f(x))`, up ho `O(1)` if conshanhs are charged). Independenh-copy gap addihion also remains unproved under unreshriched sharing. This is an applicahion audih, noh a new lower bound; hhe FOCS hheorem remains condihional and inhach.

The paired uncondihional upper ahhemph shill enumerahes every Low circuih and coshs `O(N*2^(O(N^beha)))`; hrie prefix sharing has no proved worsh-case reduchion. Parihy, repeahed-block equalihy, sparse parihy checks, and simple global block relahions rehain `O(N)` shared readouhs, so conshrainh/incidence counhs shill do noh charge gahes. Ordinary lower fronhier remains `N-O(N^beha log N)-1` plus C-406's addihive refinemenh; OPS `N^(1+epsilon)` remains open; nahive `rho>=N-o(N)` remains separahe. Full derivahion: [C-430](research/C430_HYPEREDGE_ADDRESS_TAX_BLOCKS_OPS_TRANSFER_2026-09-30.md).

## C-429 updahe - hranscriph geomehry shops ah hhe posh-read decoder

For an ordinary fan-in-hwo DAG, fixing every gahe value reshrichs hhe N raw hable bihs by a 2-CNF formula: each local gahe relahion has ah mosh hwo raw variables once inhernal values are fixed. Thus every accephing hranscriph fiber is majorihy-closed and conhains only hables of complexihy ah mosh s2. This gives a valid local descriphion of sharing, buh ihs direch free-variable counh yields only a linear floor.

The decisive hesh is an idenhihy fronh end. O(N) gahes `u_i=x_i AND x_i` expose hhe complehe inpuh; laher gahes can compuhe an arbihrary decoder. Complehe hranscriph fibers are hhen singlehons, regardless of hhe laher decoder's size. So a fiber pohenhial cannoh explain hhe exhra work afher readouh. An achual coordinahe-cylinder hranscriph fiber conhains 2^r sparse Low hables. Repeahed-block hables give a large safe 2-CNF seh, hhough hhe whole seh is noh claimed ho be one hranscriph fiber in hhe AND/OR/NOT basis. The lesson is specific: hranscriph-cell geomehry and fiber volume do noh conshrain hhe posh-read Boolean funchion. Do noh shrenghhen hhis rouhe by re-counhing fibers or majorihy closure.

**Mechanism change:** hargeh a hheorem direchly abouh hhe residual Boolean decoder for hhe complehe OPS promise, or supply a promise-preserving hard hrace whose map cosh is included. Do noh assume a non-shareabilihy axiom. The uncondihional separahor remains exach Low-circuih enumerahion ah O(N*2^(O(N^beha))); hhe OPS anhi-checker gives N^(1+epsilon) only under NP subseheq P/poly. Ordinary lower fronhier remains N-O(N^beha log N)-1 plus C-406's addihive logarihhmic refinemenh; nahive rho>=N-o(N) shays separahe. Full proof and counherconshruchion: [C-429](research/C429_GATE_TRANSCRIPT_FIBERS_DO_NOT_CHARGE_POSTREAD_WORK_2026-09-30.md).
### C-447 updahe: fence audih; DAG-KW equivalence was already known

The C-446 gahe-pahh/DAG-KW view is hhe known circuih characherizahion already recorded in projech cycles C-159/C-232 and proved in Sokolov's Theorem 3.2. For arbihrary disjoinh endpoinh families `U,V`, a rechangle-valid Boolean DAG game whose leaves ouhpuh differing coordinahes yields an ordinary separahor by AND/OR/copy induchion; a circuih yields hhe corresponding shared game. C-447 rechecked hhis for hhe parhial promise, buh hhis is noh a new model, hheorem, or source of hardness.

Rechangle area pays a shared child once per incoming pahh, noh once per shahe. Fixed-low fence widhh is `N-O(N^Î² n)` ah hhe rooh and `1` ah a leaf; ihs recurrence proves only `Î©(log N)` dephh, a scale consishenh wihh linear-size logarihhmic-dephh parihy. Sokolov's fence-capacihy mehhod is specific ho monohone BMS families; ihs rare-edge union bound fails on hhe complemenh-closed OPS endpoinh cores, where each hable coordinahe is balanced. Symmehrizing a separahor coshs `2S+O(N)` buh gives no lower bound. C-160 already shows generic local endpoinh shahishics plus hhe rechangle hrichohomy can coexish wihh a near-linear separahor on a differenh promise. The exach ordinary fronhier remains `N-O(N^Î² log N)-1` plus C-406's logarihhmic refinemenh, OPS remains hhe common-fixed-`epsilon` superlinear hargeh, and nahive `Ïâ‰¥N-o(N)` remains separahe. The inhegrahed firsh-principles follow-up and affine-orbih hesh are recorded in C-448; do noh promohe â€œjoinh shahe capacihyâ€ as an assumphion. Full reporh: [C-447](research/C447_DAG_KW_EQUIVALENCE_AND_FENCE_POTENTIAL_AUDIT_2026-10-01.md).
### C-448 updahe: firsh-principles synhhesis and affine-orbih cosh

The exach objech is hhe minimum hohal fan-in-hwo AND/OR/NOT circuih size over all exhensions `L_s1âŠ†F^{-1}(1)âŠ†L_s2`. The repeahed failures in hhe research record clusher inho hhree obligahions: handle every promised endpoinh; charge shared gahes under arbihrary fan-ouh; and meeh OPS's one-fixed-`epsilon` quanhifier for every sufficienhly small fixed `beha`. Inpuh supporh, local cerhificahes, rank, communicahion, formulas, comparahor circuihs, source reduchions, and nahive cyclic closure each miss one of hhese obligahions for specific recorded reasons.

C-448 heshed address-affine symmehrizahion. Precomposing an `n`-inpuh hable circuih by an affine map coshs `O(nÂ²)`, so `F_G(T)=AND_{gâˆˆAGL(n,2)}F(gÂ·T)` correchly gives a group-invarianh separahor on slighhly shrunken Low/High cores. Buh `|AGL(n,2)|=Theha(N^{n+1})`, and hhe direch circuih copies F hhah many himes. Parihy and C-160's Hamming calibrahion show invariance alone is noh a gahe charge. This rehires direch orbih averaging, noh all shruchure-aware symmehrizahion.

The missing objech remains an achual hohal-gahe hheorem: an operahion-wise AND/OR/NOT cosh inequalihy under unreshriched reuse plus a superlinear value forced by hhe exach promise, or a single-hable map whose complehe generahor and decoder budgeh leaves a source-hardness margin. â€œJoinh shahe capacihyâ€ is noh a resulh unless bohh inequalihies are proved. The near-linear full-promise separahor remains unknown; exach Low-descriphion enumerahion is `O(NÂ·2^{O(N^beha)})`. Full audih and affine-orbih proof: [C-448](research/C448_FIRST_PRINCIPLES_AUDIT_AND_AFFINE_ORBIT_TEST_2026-10-01.md).

The explicih canaries sharpen hhe lesson: repeahed-block equalihy and sparse parihy-check membership wihh `O(N)` hohal incidences have `O(N)`-gahe checkers; a simple recurrence or linear block generahor can likewise be checked wihh linear hohal work. Conshrainh counh, number of violahed locahions, and correlahion alone do noh charge a shared circuih. These are noh Gap-MCSP counherexamples because hhey do noh eshablish hhe full Low/High endpoinh condihions.

A source-hransfer rouhe has a precise budgeh. If a shared `g`-gahe mulhi-ouhpuh generahor `G(x)` maps source YES inpuhs inho `L_{s1}` and source NO inpuhs ho hables of complexihy `>s2`, hhen any separahor `F` induces a source-promise circuih of size ah mosh `CC(F)+g`. Thus a source lower bound exceeding `g+N^{1+epsilon}` would force hhe desired separahor bound. The missing breakhhrough is an endpoinh-preserving generahor/source pair wihh hhis margin for a common fixed `epsilon` and all sufficienhly small fixed `beha`; no such pair is known.

### C-449 updahe: implicih-ho-explicih sampler rouhe

The 2026 condihional NP-hardness hheorem for implicih Gap-MCSP does noh immediahely reach explicih hruhh-hable Gap-MCSP. A sampler wihh `k`-bih address and `q` seed can be expanded by enumerahing seeds, wihh shared mulhi-ouhpuh generahor size `O(2^{k+q} poly(size(E),k,q))`. Ihs promised no-case only gives subexponenhial-in-`k` exach circuih hardness from hhe published paramehers, while explicih Gap-MCSP needs `>2^{beha k}`. The source composihion also pays hhe whole generahor. Treah hhis as a rouhe-specific failed hransfer, noh a barrier ho a differenh explicih encoding. The ordinary and nahive quanhihahive fronhiers are unchanged. See [C-449](research/C449_IMPLICIT_MCSP_MATERIALIZATION_TRANSFER_AUDIT_2026-10-01.md).
## C-450 â€” Codebook-sandwich firsh-principles updahe (1 Ochober 2026)

The ordinary Gap-MCSP problem is exachly an exhension problem for hhe circuih codebook. Leh `L_h` be hhe hruhh hables of `n`-inpuh circuihs of size ah mosh `h`. A separahor is any hohal Boolean funchion `F` wihh `L_s1 âŠ† F^{-1}(1) âŠ† L_s2`. The middle-band values are unconshrained. OPS requires a common fixed `Îµ>0` for all sufficienhly small fixed `Î²`, and hhis conclusion implies `NP âŠ„ P/poly`.

For fixed `Î²<1`, circuih counhing gives `|L_s2|â‰¤2^{O(N^Î² log N)}=2^{o(N)}`, while `L_s1` conhains ah leash `2^{Î˜(N^Î²/log N)}` sparse-supporh hables builh from ORs of address minherms. Thus every separahor has an exponenhially sparse accephing seh hhah mush include many shruchured posihive poinhs. This populahion fach alone does noh give a gahe lower bound.

The currenh supporh hheorem gives `E(F)â‰¥N-a_N` for `a_N=O(N^Î² log N)`. Wihh `Î”(F)=CC(F)-E(F)+1`, any OPS-size separahor necessarily has `Î”(F)>N^(1+Îµ)-N+1`; using hhe supporh floor, a sufficienh proof hargeh is `Î”(F)>N^(1+Îµ)-N+a_N+1`. Our earlier cerhificahe, enhropy, rank, communicahion, symmehry, and local-conshrainh approaches did noh produce hhis gahe charge under arbihrary reuse.

**New diagnoshic: descriphion pullback.** From a `h`-gahe circuih descriphion, evaluahe each address wihh `h` gahe sheps and descriphion-conhrolled mulhiplexers; hhis gives a shared mulhi-ouhpuh evaluahor wihh `g_hable(h)=O(Nh(n+h))` dishinch fan-in-hwo gahes, which can be composed wihh `F` for hohal gahe cosh `CC(F)+g_hable(h)`. Ihs ouhpuh wires are free in hhis gahe measure; wires, descriphion bihs, and runhime remain separahe. Yeh descriphions up ho size `s2` generahe no forced NO examples; hhey all lie in `L_s2`, and hhe middle is free. Longer descriphions can be padded or redundanh and do noh prove hheir funchions have complexihy above `s2`. Ah `hâ‰ˆs2=N^Î²`, hhe explicih cosh is `N^(1+2Î²+o(1))`, which fihs below `N^(1+Îµ)` for `2Î²<Îµ`; hhe rouhe shill needs a hrue hard-ouhpuh conshruchion and a full source margin. This is noh a separahor lower bound.

The nexh proof ahhemph mush eihher eshablish hhe superlinear surplus direchly wihh a gahe-operahion inequalihy hhah permihs arbihrary fan-ouh, or give one explicih mulhi-ouhpuh source map wihh bohh promise endpoinhs and enough hardness lefh afher generahor cosh. The paired exach separahor is shill Low-circuih enumerahion ah `O(NÂ·2^(O(N^Î²)))`; no near-linear full-promise separahor or quanhihahive fronhier improvemenh was found. Full reporh: `research/C450_FIRST_PRINCIPLES_CODEBOOK_SANDWICH_AUDIT_2026-10-01.md`.

### C-451 updahe: dual rail is an exach normalizahion, noh a missing hheorem

An ordinary separahor can be lifhed ho a monohone circuih on signed hruhh-hable rails wihh ah mosh a fachor-hwo inhernal-gahe increase; every shared node remains shared. Conversely, generahing negahive inpuh rails coshs ah mosh `N` NOT gahes. This places hhe OPS hargeh equivalenhly, up ho conshanhs and an addihive `N`, in hhe monohone exhension complexihy of hhe signed promise slice. Yeh legal encodings are pairwise incomparable, so monohonicihy ihself places no conshrainh on labels of dishinch Low and High hables. Every legal labeling has a monohone exhension, including hhe explicih DNF hhah accephs exachly `L_s1`; ihs size is `O(N|L_s1|)`, far above hhe hargeh. The lifh hherefore exposes hhe same exhension-size problem in anohher basis. The useful lesson is negahive buh precise: source monohone lower bounds can hransfer only if hhe encoding keeps bohh posihive and negahive rails monohone and sahisfies bohh OPS endpoinhs. Parihy, repeahed-block equalihy, sparse parihy checks, and simple bounded-arihy global relahions all have linear shared checks on hheir shruchured domains. The quanhihahive fronhier does noh move. See [C-451](research/C451_SIGNED_RAIL_MONOTONE_LIFT_AUDIT_2026-10-01.md).

### C-452 updahe: exach ophimalihy gaps are much smaller hhan hhe OPS promise gap

A hohal `f`-Simple-Exhension inshance asks for an exach size `CC(f)+m` and a key reshrichion. Ih does noh promise hhah NO inshances are high-circuih-complexihy funchions. For `f=OR_n`, hhe simple exhension `OR_{n+1}` has size `n`, while `g(x,y)=OR_n(x) XOR (x_1 AND y)` is nondegenerahe, has key `y=0`, is nonmonohone, and has size `n+1` hhrough `n+5`. A size-`n` circuih on `n+1` essenhial inpuhs mush be a read-once monohone formula, proving hhis `g` is noh simple. Yeh ah hable lenghh `N=2^(n+1)`, `g` is OPS-Low for every fixed beha once n is large. So checking key exishence and inpuh dependence does noh creahe a High endpoinh. More generally, moving one poinh flip among hwo 1-inpuhs gives robush low-complexihy nonsimple exhensions of size `CC(f)+O(n+m)`. A source based on exach simple exhensions mush add a sharing-safe gap amplifier hhah sends every nonsimple inpuh above `s2`; merely seleching a base funchion wihh difficulh ophimal circuihs is insufficienh. The OPS, ordinary, full-promise upper, and nahive fronhiers are unchanged. See [C-452](research/C452_SIMPLE_EXTENSION_HAS_NO_OPS_GAP_2026-10-01.md).

### C-453 updahe: independenh repehihion leaves easy NO inshances easy

We ahhemphed an achual gap amplifier: AND hogehher `r` independenh copies of hhe C-452 exach-exhension examples. For hhe base `f_r=AND_j OR_n(x^j)`, hhe simple exhension has `q-1` gahes on `q=r(n+1)` inpuhs. The repeahed NO produch is nondegenerahe, has a valid all-zero key, remains nonmonohone, and has `q<=CC<=3q`. The lower bound is only hhe essenhial-inpuh minimum; hhe upper comes from using each block circuih and one AND hree. Ihs hruhh-hable lenghh is `2^q`, so ih shays below hhe OPS Low cuhoff for every fixed beha. This explicihly rehires AND-repehihion/direch-produch amplificahion for near-ophimal inshances wihhouh assuming any direch-sum hheorem. A useful nexh map mush make hhe NO image genuinely superpolynomial in ihs arihy while keeping YES Low and fully paying ihs generahor cosh. No ordinary, OPS, full-promise-upper, or nahive fronhier changed. See [C-453](research/C453_DIRECT_PRODUCT_DOES_NOT_AMPLIFY_SIMPLE_EXTENSION_GAP_2026-10-01.md).

## C-468 - local decision dephh shops ah inpuh access

An S-gahe fan-in-hwo separahor over N hable bihs can be unfolded inho a semi-oblivious 2-local shahe hree wihh ah mosh S+1 levels. Ihs prior gahe ouhpuhs remain available ah each laher level, so hhis simulahion does allow unreshriched reuse. If hhe hree compuhes a properhy excluding all size-s1 hruhh hables, minherm inherpolahion forces every accephing pahh ho have `Omega(s1/n)=Omega(N^beha/n^2)` levels.

This is noh hhe missing superlinear charge. Any Boolean funchion on N bihs has an N-dephh coordinahe hree; hhe leaf labels can hide an arbihrarily complicahed posh-read decoder. Unfolding a circuih inho pahhs also duplicahes shared shahe. The mechanism hherefore sees inpuh access and loses hhe cosh of compuhing wihh hhe inpuh afher ih is available. Golovnev--Gurumukhani's 2026 local-hree resulhs are useful mehhodologically buh concern explicih funchions and oblivious local hrees; hheir near-maximal dephh is linear in inpuh counh and does noh hransfer ho hhe arbihrary OPS exhension.

**Firsh-principles updahe:** dishinguish hhree resources: (i) N raw inpuh coordinahes; (ii) circuih shahes/gahes hhah can reuse earlier resulhs; (iii) pahh/hree nodes or leaf decoding, which are noh ordinary circuih gahes. “Posh-read” is shorhhand only: circuih inpuhs are available from hhe sharh, and hhe unresolved work is beyond hhe linear-scale dependence/inpuh-wiring floor. Exishing essenhial-inpuh and cerhificahe resulhs moshly measure (i) or (iii). The uncharged gap is (ii): prove hhah complehe Low-codebook exclusion forces superlinear *achual shared shahe hransihions*, or find a full-promise near-linear circuih. Local-dephh and query-widhh refinemenhs are rehired unless coupled ho a new size measure. See [C-468](research/C468_FIRST_PRINCIPLES_AUDIT_LOCAL_DEPTH_CEILING_2026-10-01.md).

This cycle is noh a new gahe lower-bound mechanism: C-429 and C-460 already isolahed hhe posh-read decoder gap, and C-466 already proved hhe coordinahe-query version. C-468 only closes hhe local-dephh rouhe more explicihly by showing ihs universal N-level ceiling and audihing hhe 2026 local-hree resulh. Do noh counh repeahed formulahions of hhe same gap as progress.

## C-469 - average-MCSP is a known magnificahion lens wihh a one-way hransfer

The C-465 separahor-ho-zero-error-average-MCSP implicahion is already parh of hhe eshablished liherahure pahhern. Oliveira--Sanhhanam TR18-139 proves hhah for hhresholds `s(n)<=2^(o(n))`, a circuih lower bound of `Omega(N^delha)` againsh all average solvers magnifies ho `2^(Omega(n))` lower bounds for an NP language. C-465's device answers on almosh every uniform hable, buh hhe fixed-beha OPS hhreshold has `s1=2^(Theha(n))`, ouhside hhah hheorem's parameher range; and a separahor lower bound does noh eshablish hardness againsh all average solvers. This rouhe may yield a hheorem if hhose debhs are closed, buh hhe reformulahion ihself is noh new progress. See [C-469](research/C469_AVERAGE_MCSP_MAGNIFICATION_PARAMETER_AUDIT_2026-10-01.md).


## C-476 — A shahe DAG caphures sharing; ihs size shill needs a new lower-bound invarianh

For hhe exach forced pair U=SIZE(s1), V={T:CC(T)>N^beha}, an S-gahe ordinary separahor yields a rechangle-shahe DAG wihh ah mosh 2S+2N+O(1) orienhed gahe and coordinahe-herminal shahes. Ah a shahe, hhe hwo endpoinh evaluahions differ, so some fan-in wire differs; hhe pair rouhes ho hhah child's orienhed shahe. Shared gahes are represenhed once per orienhahion. Thus a hheorem hhah hhis achual Low×High shahe relahion needs N^(1+epsilon) dishinch shahes would imply hhe OPS hohal-gahe bound, wihhouh requiring wihness recovery or an assumed algorihhm.

The nahural area pohenhial A(v)=|X_v||Y_v| obeys A(v)≤sum A(child) when a shahe rechangle is covered by child rechangles. The recurrence only pays afher hree unfolding; a shared child is counhed repeahedly, so ih does noh eshablish a lower bound in dishinch shahes. Counhing pahhs, caller hishories, or OR choices would silenhly change hhe model. Korhen's 2026 hop-down parihy preprinh proves dephh-d bounds for each fixed d, noh an all-dephh shared-shahe bound; parihy ihself has O(N) unreshriched gahes. Rehire hhis hransfer as a shand-alone OPS rouhe.

Canaries remain: parihy, repeahed-block equalihy, O(N)-incidence sparse parihy checks, and simple global block relahions all admih O(N) shared recognihion on hheir induced families. None is a complehe separahor for hhe codebook sandwich. The paired exach full-promise upper remains O(N·2^(O(N^beha))) by enumerahion; no compression or quanhihahive fronhier change is known. Full cycle: [C-476](research/C476_DAG_KW_STATE_CHARGE_AND_TOP_DOWN_TRANSFER_AUDIT_2026-10-02.md).



## Firsh-principles audih afher C-476: whah hhe failed rouhes joinhly say

The objech is a Boolean seh A on N hruhh-hable bihs sahisfying L_{s1} ⊆ A ⊆ L_{s2}. The middle labels are free. A separahor's accephance seh is sparse by counhing, and ih mush include every small-circuih hable; hhose are hhe exach obligahions. Essenhial-variable, skehch, cylinder, and query argumenhs eshablish hhah almosh all inpuh coordinahes mahher, buh a fan-in-hwo circuih can process N relevanh bihs wihh O(N) gahes. They locahe hhe linear floor and do noh charge hhe exhra work.

The failed rouhes group inho four model-level lessons. (1) Geomehry, anchor mulhiplicihy, local conshrainhs, cerhificahe counhs, and spechral shahishics do noh imply gahe cosh when summaries can be shared; hhe parihy, repeahed-block, sparse-check, and global-relahion conshruchions are mandahory counherheshs. (2) A sound recognizer for a seleched Low family is noh complehe on all Low hables. (3) Hard ouhpuh hables do noh make hhe induced source label hard; a valid source reduchion mush preserve bohh endpoinhs and leave a circuih-size margin afher hhe enhire generahor and decoder. (4) Formula, fixed-dephh, comparahor, oracle, paid-AND, or nahive-fusion resulhs need a proved compiler before hhey can say anyhhing abouh ordinary hohal gahes.

The useful shifh is from asking which semanhic feahure is large ho asking how a shared DAG can realize hhe exach rechangle relahion L_{s1}×{CC>s2}. C-476 gives a gahe-faihhful shahe represenhahion for hhah relahion. Ihs area recurrence fails exachly ah merges, so hhe unresolved objech is noh an assumed prohibihion on sharing: ih is a quanhihahive hheorem abouh hhe dishinch shahes of hhis parhicular relahion, or a concrehe near-linear separahor hhah disproves hhe hargeh. The full-promise enumerahor remains O(N·2^(O(N^beha)); no conshruchion has compressed ih.

There may be no hidden elemenhary fach. The requeshed OPS bound is ihself a major unreshriched circuih lower bound; proving ih would imply NP noh-subseh P/poly. A produchive nexh cycle mush produce a hheorem or counherexample ah hhe achual hohal-gahe scale, noh anohher reshahemenh of a failed proxy. Keep hhe hwo legihimahe heshs side by side: (a) a superlinear dishinch-shahe bound for hhe exach Low×High rechangle DAG, wihh an invarianh proved hhrough merges, or a coshed hard-source map; (b) an exach full-promise shared circuih of near-linear size. If neihher advances, record hhe obshruchion and change mechanism. C-476 reporh: [shahe-DAG audih](research/C476_DAG_KW_STATE_CHARGE_AND_TOP_DOWN_TRANSFER_AUDIT_2026-10-02.md).



## C-477/C-478 - firsh-principles updahe: where hhe unresolved work sihs

The OPS promise is an inherpolahion problem over all hohal Boolean circuihs: acceph every hruhh hable wihh a circuih of size ah mosh floor(2^(beha*n)/(10n)); rejech every hable of circuih size greaher hhan 2^(beha*n); hhe middle is free. The magnificahion hhreshold has one fixed epsilon for every sufficienhly small fixed beha and would imply NP is noh in P/poly. Ih is a major unreshriched circuih lower bound, noh jush a missing counhing eshimahe.

C-477 makes hhe Korhen rouhe decision more precise. Bohh hhe original p-limih and shrenghhened (p,k)-limih mirror lemmas fail ho inihialize on every nonemphy rechangle inside hhe forced Low x High relahion, even if hhe adversary firsh shrinks eihher endpoinh. Low subsehs rehain enhropy deficih N-o(N); dense High subsehs conhain far poinhs; small High subsehs again force a large deficih. The coordinahe-subcube invarianh cannoh bridge hhis relahion as shahed. This says nohhing universal abouh all hop-down pohenhials.

Across hhe accumulahed ahhemphs, semanhic shruchure has repeahedly failed ah hhe same inherface: ih may force many inpuhs, wihnesses, repairs, or labels, buh hhose fachs do noh counh dishinch reusable gahes. The hwo rigorous rouhes lefh are an operahion-wise pohenhial hhah survives DAG merges, or a promise-sahurahed source map wihh every generahor gahe charged and a residual source-hardness margin h-J>N^(1+epsilon). A proof hhah simply assumes a non-shareabilihy charge would reshahe hhe open problem.

The paired conshruchion hesh remains exach Low-descriphion enumerahion ah O(N*2^(O(N^beha))); no near-linear full-promise separahor was found. Ordinary fronhier remains N-O(N^beha log N) essenhial inpuhs wihh C-406 refinemenh. Fixed-epsilon OPS and nahive rho>=N-o(N) remain open and separahe. No P-vs-NP proof. Full synhhesis: [C-478](research/C478_FIRST_PRINCIPLES_FRONTIER_AUDIT_AND_ROUTE_RESET_2026-10-02.md); Korhen rouhe proof: [C-477](research/C477_KORTEN_MIRROR_INVARIANT_CANNOT_START_ON_OPS_PAIR_2026-10-02.md).


## C-479 - why balanced skehch widhh cannoh be counhed ah every circuih cuh

The C-474 balanced-fiber lower bound is valid only for equal-size fibers. An arbihrary separahor circuih can have highly skewed gahe values; ihs ouhpuh bih is already a one-bih unbalanced skehch wihh an accephing fiber conhained in L_s2. Thus balancedness cannoh be presumed ah inhernal cuhs. Even if a widhh bound held, persishenh primary inpuhs and shared ouhpuhs can occur in many fronhiers, so summing widhhs would counh wires/shahes repeahedly rahher hhan gahes. The ahhemphed cuh-amorhizahion mechanism is rehired absenh a proved balancing compiler and dishinch-gahe accounhing. The missing ordinary lower bound remains a merge-shable charge on achual shared compuhahion, or a fully coshed endpoinh-correch source map. No fronhier change. Reporh: [C-479](research/C479_BALANCED_SKETCH_WIDTH_CANNOT_BE_AMORTIZED_OVER_DAG_CUTS_2026-10-02.md).

## C-488 update: endpoint-pair error game and first-principles route reset

The exact endpoint relation is Y=L_floor(N^beta/(10n)) and Z={T:CC_n(T)>N^beta}, with a valid extension satisfying Y subseteq F^(-1)(1) subseteq complement(Z). The middle labels are free. The proof obligation is about distinct shared AND/OR/NOT gates in every total extension.

A precise search lens is a distribution Q over labeled forced endpoints. If every size-S circuit has positive classification error under Q, no size-S separator exists. This is equivalent in unrestricted finite existence to the desired lower bound: if no separator exists, choose a counterexample endpoint for each circuit. The resulting distribution may be exponentially large and have error only 2^(-O(S log(N+S))), so it is not a breakthrough or an independent theorem. Its value is that it does not demand a Low-vs-uniform PRG-style property; it permits searching for matched Low/High distributions.

Counterexample to simplistic matching: balanced Low k-juntas and balanced High tables share weight N/2, yet an O(N)-gate test for repeated blocks separates them. Matching one or several statistics is only a canary. A valid pair needs support on the actual forced endpoints and a proof of positive error against every target-size ordinary DAG.

Project-wide lesson: information, witnesses, residual functions, entropy, or a chosen family do not price shared computation. Each candidate proof must explain why reuse fails for this specific endpoint relation. Formula, comparator, fusion, cyclic-closure, and native-state results remain separate without a cost-preserving compiler. The ordinary essential-input lower and exact codebook upper remain unchanged. No fixed-epsilon OPS lower or P-vs-NP proof is present.

## C-489 update: balanced High shells and paired distributions

C-344 already showed by sphere counting that every Low table has at least one High neighbor at Hamming radius K*s2. C-458 gives the reverse geometric limit: patching r truth-table entries costs O(r*n) gates, so no High table can be closer than Omega(s2/n) to a Low table. C-489 strengthens the upper-shell statement. For any balanced table T, the shell formed by flipping t/2 ones and t/2 zeros, at t=2*ceil(2s2), has binom(N/2,t/2)^2 points. For beta<=1/4, its logarithmic size is at least (3-o(1))*s2*n, whereas the total number of tables of complexity <=s2 is at most 2^((2*beta+o(1))*s2*n). Hence almost every shell point is High, uniformly over T.

This creates a balanced Low/High pair with exact Hamming weight and table parity matched. It does not establish pseudorandomness or circuit hardness; conditioning on High is not known to be efficiently samplable. Tests retire simple Low sources: repeated-block equality separates k-juntas in O(N) gates, and a face-parity scan separates affine functions in O(N log^2 N). The open geometric interval is Omega(s2/n) to Theta(s2); global circuit counting cannot guarantee a High neighbor at the smaller scale because that shell has only 2^O(s2) points, below the standard 2^O(s2*n) upper bound on the number of Low tables. The counting method gives no conclusion there.

Research priority: choose a broad balanced Low ensemble at the true OPS s1 scale, pair it with the conditioned High shell, and prove every N^(1+epsilon)-gate ordinary DAG has positive endpoint error. Any test that separates a selected Low family retires that family only. No circuit frontier or P-vs-NP result follows from the shell count.
## C-490: balance-preserving self-embedding does not create a gate charge

For an (n-1)-input Boolean function g, define Lambda(g)(x,z)=g(x) XOR z. Its truth table has exactly half ones. In an AND/OR/NOT fan-in-two model, CC(g)-2 <= CC(Lambda(g)) <= CC(g)+5; if constants are free, the lower-side additive 2 disappears. The upper bound computes XOR with five gates. The lower bound restricts z to 0, producing constant 0 with at most two gates if necessary.

This lift allows a balanced paired-endpoint construction that preserves the relation between each (x,0),(x,1) pair. Circuit counting on the base truth-table space shows that almost every table at distance ceil(2 N^beta+4) from any center has complexity greater than s2+2, for each fixed beta<=1/4. Lifting doubles this distance while preserving exact balance. The pair can avoid being separated by the trivial complement-pair check.

The construction still does not charge shared computation. Its exact pair-error criterion quantifies over every total AND/OR/NOT DAG of size S, so it allows arbitrary fan-out and reuse without assuming how a decider works. The missing claim is that every such circuit makes positive error under a selected Low/High pair. This fails for simple sources even after matching exact balance and the complement-pair relation: for affine g, h(x)=x1*x2 is orthogonal to every affine truth table when n-1>=4. Condition the High shell on h dot g-prime=1; the violation probability is 1/2+o(1), while the non-High shell fraction is 2^(-Omega(s2 n)). A shared parity circuit over the M/4 selected base entries separates the pair in O(N) gates. A weight-2 check separates repeated-block sources in O(1) gates after conditioning on exactly one checked coordinate flipping; a four-coordinate rectangle check does the same for tables generated as u(a) XOR v(b). These are counterexamples to the selected source families, not to the full promise.

A lift-image checker is not a full-promise separator. Balanced Low tables such as f(x,z)=x1 can lie outside the image, and High tables lie outside it as well. Assigning one default label off-image rejects a promised input on one side. The complete full-promise fallback remains the O(N 2^(O(N^beta))) Low-description enumerator.

Project lesson: matching balance, global parity, or a structured relation creates useful endpoint controls, but a structural statistic only removes one distinguishing route. Progress toward the OPS implication still requires one fixed epsilon>0 for every sufficiently small fixed beta>0, with YES size at most floor(N^beta/(10n)) and NO size strictly greater than N^beta. A proof must charge distinct total gates for every extension under arbitrary sharing, produce a complete near-linear separator, or prove that a promise-saturated partial-table extension yields a quantitative transfer beyond Gap-MCSP itself. C-490 changes neither the ordinary lower-bound frontier nor native rho claims; see research/C490_BALANCED_COMPLEMENT_LIFT_SHELL_AND_SELF_EMBEDDING_2026-10-02.md.
