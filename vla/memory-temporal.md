<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / memory-temporal

[← vla](README.md) · [CSV master](../papers.csv)

15 records · Published date 降順（同日 ID 降順）

### Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- ID: `VLA-0235`
- Published: 2026-10-22
- Authors: Chenyuan Chen; Ran Ding; Lechen Zhang; Zewen He; Yoshihiko Nakamura
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.31166) · [PDF](https://arxiv.org/pdf/2610.31166) · [Project](https://memory-before-goal.github.io/)
- Tags: pre-history-memory, object-event, humanoid, loco-manipulation, SAM3, benchmark
- Model size: 凍結Qwen3-VL-2B backbone；全体パラメータ数未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

WholeBodyMemは、目標に向けて動く前に観測され後から消える手掛かりを全身VLAへ保持する知覚メモリ。SAM3で追跡した物体の出現・消失などから最大7フレームを選び、外観・幾何・時刻を持つ物体トークンとともに行動expertへ渡す。

**主な貢献**

記憶依存のHuMeGo（シミュレーション6課題・Unitree G1実機6課題）を整備。基盤方策Ψ0に対し、シミュレーション成功率29.1%→72.6%、実機では各課題10試行の計60試行で22/60→53/60と報告する。未検出物体の手掛かりは保持できず、追跡計算負荷とsim-to-real gapが残る。

**確認記録**

- Checked: 2026-10-23 · Review: verified
- 2026-10-22 v1。https://arxiv.org/html/2610.31166v1 のSections III–VI（memory budget、凍結2B backbone、real trials、limitations）と公式projectを確認。RA-Lは投稿中との著者記載のみで採録未確認。公式ページは匿名review版だがarXivから直接リンクされる。コード・重み・実装ライセンスの公開先を確認できずunknown。PDFはabsの実hrefのみ検証し未取得。 実機は各課題15demoで別々に学習した評価で、課題横断の単一汎用方策とはしない。

### GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- ID: `VLA-0230`
- Published: 2026-10-21
- Authors: Qinfan Zhang; Yifan Luo; Haoyuan Shi; Guanlin Liu; Han Dong; Haozhe Shan; Yong Dai; Xiangcong Ren; Xiaozhu Ju
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.29866) · [PDF](https://arxiv.org/pdf/2610.29866) · [Code](https://github.com/GeoMem-VLA/GeoMem-VLA) · [Project](https://geomem-vla.github.io/)
- Tags: GeoMem-VLA, GeoPlan, geometric-supervision, causal-episodic-memory, VGGT, Qwen3-VL, flow-matching, LIBERO, RoboTwin
- Model size: Qwen3-VL-4B backbone + GR00T-style action expert（総規模unknown）
- Open-source: unknown
- Code / weights / license: available / unavailable / unknown

**概要（日本語）**

VGGTの点mapと将来手先軌道を補助教師として、専用GeoPlan tokenへ幾何情報を学習させる。観測・幾何のepisode内memoryから因果的に履歴を検索・融合し、推論では3D教師や明示再構成を使わずaction chunkを生成する。

**主な貢献**

幾何教師と有界の時間memoryを結合し、標準設定のLIBERO平均98.9%、RoboTwin Clean/Randomized 91.10/91.24%を報告。実機は2platform・5課題各10rolloutで平均78.0%。公開sourceは短いLIBERO workflowとRoboTwin adapterで、論文全体の再現packageではない。

**確認記録**

- Checked: 2026-10-22 · Review: needs-review
- arXiv absでv1初稿2026-10-21 15:23:18 UTC、改訂なしを確認。著者はabsのXiangcong Renを採用したがHTMLはXiancong Ren表記。本文前に既存376件とcanonical arXiv/DOI alias・正規化/近似題名をvalidate\_csv.py --candidateで照合し一致なし。読了範囲は https://arxiv.org/html/2610.29866v1 §§3–4、Appendix A、再現/倫理声明の選択精読。公開比較値は各原著protocolを保持し統制ランキングではない。公式GitHub commit a71a643770d86d38b93653f47886431be02346bb のREADME/RELEASE\_NOTES、QwenGeoGR00T.py、geoplan実装を確認。READMEは20k-step既定例が論文protocolでなく、実機package未収録と明記。論文§3.2の同座標frameのEEF教師に対し、公開QwenGeoGR00T.py冒頭は正規化action変位でVGGT frameと未共通と記載し、完全一致は未解決。LICENSE全文はMIT表記にupstream2commit保持の追加文を含むため、標準OSI MITとしてopen\_source=trueを確定せずlicense unknown。HF https://huggingface.co/rxc205/GEOMEM-VLA はcoming soonでfilesは.gitattributes/READMEだけ、重みunavailable。HFカードapache-2.0をcodeへ流用しない。projectのcoming soon表示より実際のsourceを優先。PDF/重みdownload・実行再現なし。 arXiv absの生HTMLで実在するPDF相対href /pdf/2610.29866 を抽出し絶対URLへ解決。PDF本体は取得しない。

### FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring

- ID: `VLA-0229`
- Published: 2026-10-21
- Authors: Liwen Yang; Yutian Zhang; Jiaqi Zhai; Li Yang; Tutian Tang; Qiwei Shan; Yancheng Bi; Qiankuan Shangguan; Yangkun Zhu; Ce Hao; Dong Wei; Qiaojun Yu; Dibo Hou
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.29692) · [PDF](https://arxiv.org/pdf/2610.29692)
- Tags: FlowVLA-pouring, quantitative-pouring, physical-completion, force-belief, mass-estimation, residual-outflow, pi0.5
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

見た目や姿勢が変わらない注ぎ中にも進む物理量を、視覚・関節・手首力覚・再帰beliefの履歴から推定する。π0.5の運動生成と物理的な完了判定を分け、移送済み質量と戻し動作中の残流量の合計で復帰を開始する。

**主な貢献**

行動chunkの段階境界をまたぐ教師信号を抑制し、target非依存の質量推定と残流予測を接続。coffee-pot/waterで完了試行の目標均等MacroMAE 13.1g、全試行に対する完了かつ目標±10%は53.7%を報告した。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absで全著者とv1初稿2026-10-21 13:07:39 UTC、改訂なしを確認。本文前に既存376件とcanonical arXiv/DOI alias・正規化/近似題名をvalidate\_csv.py --candidateで照合し一致なし。読了範囲は https://arxiv.org/html/2610.29692v1 §III、IV-A–C、結論、Tables I–IIIの選択精読。物理量の持続状態による観測aliasing解消を主眼としvla/memory-temporal。主実験は123attempt・79完了質量記録。83.5%の±10%率は完了質量記録だけが分母で、全attemptの53.7%と混同しない。150/250gは同一モデルの補間だが、他の容器/液体はdomain別再訓練でzero-shot転移ではない。訓練にoffline電子秤教師を要し、grasp失敗も残る。題名と著者を含む限定検索、abs/HTMLで公式実装・重み・project・実装license取得先を確認できずunknown。別著者の2025年同名FlowVLAと混同しない。PDF/重みdownload・実行再現なし。 arXiv absの生HTMLで実在するPDF相対href /pdf/2610.29692 を抽出し絶対URLへ解決。PDF本体は取得しない。

### REKI: Registering Knowledge in VLAs

- ID: `VLA-0224`
- Published: 2026-10-15
- Authors: Juliette Marrie; Paul Pacaud; Adrien Ramanana Rahary; Shizhe Chen; Moritz Böhle
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.22178) · [PDF](https://arxiv.org/pdf/2610.22178) · [Code](https://github.com/kyutai-labs/reki) · [Project](https://kyutai.org/reki/)
- Tags: REKI, register-memory, KV-cache, flow-matching, public-data-pretraining, Qwen3.5, LIBERO-Plus, RoboTwin, RoboCasa365
- Model size: 2.4B (2.2B VLM + 0.2B action expert)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

公開のロボット・一人称人間動画・視覚言語データのみで事前学習した2.4B VLA。Qwen3.5-2Bとflow-matching行動expertを組み合わせ、フレームごと32個のregister tokenをexpert内のKV cacheへ残す。通常は1秒間隔の3フレームを使い、過去画像をVLMへ再入力せず短い履歴を行動生成へ渡す。

**主な貢献**

行動ノイズやflow時刻に依存しないregisterをdenoising間・フレーム間で再利用する記憶機構と、データ整備から実機配備までの実装を提示。原著条件でLIBERO-Plus 90.4%、RoboTwin Clean2Rand 65.8%、RoboCasa365 38.4%。同じ重みから履歴を除くとRoboTwinの往復振動episodeが4.1%から14.8%に増えた。

**確認記録**

- Checked: 2026-10-19 · Review: verified
- arXiv v1初稿2026-10-15 16:34:06 UTC、改訂なし。本文前に既存355件とcanonical arXiv/DOI alias・NFKC/casefold/Greek/句読点正規化題名、およびvalidate\_csv.py --candidate/--titleを照合し一致なし。https://arxiv.org/html/2610.22178v1 §4、6–7、Appendix D.3–4を選読。比較モデルの事前学習data・計算量は一致せず、21.8 ms/chunkはH100・2画像・compiled経路の値。実機はUR5の5課題、各10評価episodeで部分点を含む。公式実装reki/policy/modeling.pyとMIT LICENSE本文、Apache-2.0由来のNOTICEを確認。GitHub確認commit 8823011f76358e4dd4d800e9182251b00c157fc1（2026-10-19）。公式HF https://huggingface.co/kyutai/reki-2b のimmutable revision c6b747e9c8ab046f41917870f966a0c12eb7792eでmodel.safetensors 4814273856 bytes、ema.safetensors 8608097048 bytesとLFS oidをtree APIで確認。重みはCC-BY-NC-SA-4.0で商用自由利用ではなく、上流data/model条件は別。新規state layoutには入力層の学習、推論周期には学習時strideとの整合が必要。download・実行再現は未実施。

### Physical Time as a Missing Dimension of Robot Policy Memory Dynamics

- ID: `VLA-0217`
- Published: 2026-10-14
- Authors: Yushen Liang; Yue Peng; Baosheng Jin; Tianluo Zhang; Xinyu Zhang; Shuyi Zhou; Zhuoran Chen; Xinqi Liu; Shenji Wan
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.20524)
- Tags: physical-time, continuous-time-memory, diffusion-policy, flow-matching, pi0.5, real-robot
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

Temporal Flow Policyは、観測回数では区別できない待機時間や遮蔽前の運動を、実測経過時間で発展する記憶状態に保持する。Diffusion Policyとπ0.5に組み込み、観測周期が変わる制御課題と実機操作で評価する。

**主な貢献**

観測と過去記憶から候補状態・チャネル別時定数を別々に予測し、経過時間を積分区間とする指数更新を導入。更新記憶を動作生成器の適応正規化へ与え、時計入力への介入で行動時刻との関係を検証。

**確認記録**

- Checked: 2026-10-16 · Review: verified
- v1初出2026-10-14、改訂なし: https://arxiv.org/abs/2610.20524 。canonical arXiv/DOI・正規化/近似題名を本文前に照合し一致なし。HTML https://arxiv.org/html/2610.20524v1 §3、§4.1–4.4を選読。時間aware記憶の比較は制御シミュレーション、Galaxea A1実機は各backboneのreactive方策と比較し各課題・方式20試行。指数更新の区間合成は候補と時定数を固定した局所性質。論文・検索で公式project、実装、重み、実装ライセンスは確認できずunknown。arXiv掲載PDFの取得がツール内部エラーとなりpdf\_urlは空欄、本文はHTMLで確認。PDF・重み・data未download、再現実験なし。

### MemoryVLN: From Ego-Aware Memory Representation to Cross-Context Memory Reuse in Vision-Language Navigation

- ID: `VLA-0214`
- Published: 2026-10-13
- Authors: Xueyao Wei; Yifei Wang; Delun Li; Shaoan Wang; Junzhi Yu; Wenjie Song; Xingyu Chen
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18478) · [PDF](https://arxiv.org/pdf/2610.18478) · [Code](https://github.com/ZGCA-HMI-Lab/MemVLN) · [Project](https://zgca-hmi-lab.github.io/MemVLN/)
- Tags: MemoryVLN, vision-language-navigation, hierarchical-memory, cross-context-reuse, spatial-grounding, long-horizon
- Model size: Qwen2.5-VL-7B + frozen VGGT-1B (reference configuration)
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

長距離の視覚言語ナビゲーションで、観測履歴を新旧に応じて圧縮し、2D意味特徴・3D幾何特徴・6D自己姿勢を含む記憶を構築する。エピソード内と環境文脈ごとの記憶を階層的に維持し、現在状態に関係する記憶を検索して次の離散移動行動の予測に組み込む。

**主な貢献**

履歴圧縮から空間的記憶の構築・更新・再利用まで統合し、R2R-CE/RxR-CEのval-unseenでデータ量を揃えた比較先に対する成功率差を約2.0/6.5ポイントと報告。

**確認記録**

- Checked: 2026-10-15 · Review: needs-review
- arXiv v1公開2026-10-13 UTC、改訂なし。arXiv要旨・HTMLの記憶設計・R2R-CE/RxR-CE val-unseen評価、著者project、公式GitHub README/CODE.md/THIRD\_PARTY\_NOTICES.md/LICENSE\_VGGT.txt、論文からリンクされたHugging Face model indexを確認。GitHubは評価コードのみを公開し学習コードと訓練データ構築を意図的に非公開。自作部分はApache-2.0だが同梱VGGT派生ファイルに用途制限付きVGGT licenseが適用されるため全実装はOSI適合と言えない。HF indexはSafetensors/9Bを表示するがtree取得が失敗しMemoryVLN学習済みcheckpointの実ファイルを確認できないためweights unknown。要再確認: HFのfiles一覧とcheckpoint内容/モデルカードを開き、同梱VGGT派生範囲と配布条件を照合。https://arxiv.org/abs/2610.18478 ; https://arxiv.org/html/2610.18478v1 ; https://github.com/ZGCA-HMI-Lab/MemVLN ; https://github.com/ZGCA-HMI-Lab/MemVLN/blob/main/CODE.md ; https://github.com/ZGCA-HMI-Lab/MemVLN/blob/main/THIRD\_PARTY\_NOTICES.md ; https://github.com/ZGCA-HMI-Lab/MemVLN/blob/main/LICENSE\_VGGT.txt ; https://huggingface.co/xiaoxiaoxiaoyyy/MemVLN

### Dual-Stream Memory for Vision-Language-Action Policies

- ID: `VLA-0202`
- Published: 2026-10-09
- Authors: Yang Wang; Ping Liu; Ruiyu Wang; Xuhua Chen; Lingfeng Zhang; Tao Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.13262) · [PDF](https://arxiv.org/pdf/2610.13262)
- Tags: dual-stream-memory, Gated-DeltaNet, execution-context, task-conditioned-retrieval, multi-scale-fusion, pi0.5, RoboMME, Piper
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

記憶依存の操作に必要な実行段階と、現在は見えない視覚証拠を別の記憶経路で扱う。Gated DeltaNetが履歴を一つのtemporal tokenへ圧縮し、task条件付きretrieverが関連frameを保持する。各frameを16個のmulti-scale spatial tokenとしてpi0.5のaction expertへ渡す。

**主な貢献**

固定幅の再帰的実行文脈と選択的な視覚履歴アクセスを統合する二段階学習を提案。原著RoboMME 16 task平均は49.22%（公開FrameSamp+Modul参照44.51%）、Piper実機4 task平均は62.5%（参照37.5%）だが、cup swap時の持続的な物体同一性追跡は未解決。

**確認記録**

- Checked: 2026-10-12 · Review: verified
- arXiv v1は2026-10-09 09:14:59 UTC、改訂なし。書誌・Sec.III–Vを選読。RoboMMEは各task/seed 50 episode、3 seed、published checkpoint aggregation参照でmatched architectural effectとは区別。実機は4 task各30 rollout、全method同じ400実演だがcheckpoint基準はtraining stepを揃えない。temporal memoryは固定幅でもspatial bankと全履歴scoringは保持frame数・prefix長とともに増える。Shellは40.0%で参照53.3%を下回り、全task改善や持続的identity追跡成功を主張しない。arXiv/HTMLに公式code/project/weights提供先を確認できずunknownを保持。論文のarXiv perpetual non-exclusive licenseを実装ライセンスと混同しない。総parameter数未確認、結果未再現。

### Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models

- ID: `VLA-0185`
- Published: 2026-10-08
- Authors: Hongyu Shi; Sen Zhao; Zuyu Zhang; Lifeng Shen; Ding Zou; Xinyu He; Xu Zhang; Qinghua Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.12090)
- Tags: latent-reasoning, reasoning-reuse, multi-episode-memory, zero-shot-robustness
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

成功した潜在推論の流れを保存し、現在の状況に合う断片を複数エピソードから再構成・修正して行動expertへ渡すFlowMem。観察の蓄積だけでなく、再利用可能な推論過程を記憶する。

**主な貢献**

RoboMME Full-16で48.0%（記憶なしLaST₀は46.3%）、標準LIBERO学習後のLIBERO-Plusで77.3%（73.2%）。互換性・順序・進捗に関する記憶介入も検査した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.12090 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.12090v1 。§3.3–3.6/4.1–4.3とTables1–2選読。RoboMMEは16課題各50固定episodeの課題macro平均、LIBERO-Plusは10,030 instanceのpooled平均。学習・記憶供給・評価episodeは分離。コード/重み/実装ライセンスの公式releaseは未確認でunknown。 PDF未取得。

### PMTRM: Pseudo-Memory Temporal Re-encoding Module for Embodied Policy Learning

- ID: `VLA-0178`
- Published: 2026-10-08
- Authors: Changchuan Yang; Haoxuan Xu; Wenbo Chen; Shuai Ren; Jianlong Zheng; Huarui Zhang; Tianfu Li; Guanzhong Tian
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.11168)
- Tags: phase-ambiguity, executed-history, supporting-method, temporal-reencoding
- Model size: 追加module: 訓練7.61M / 推論3.81M
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

実行済みstate/actionの有界履歴を再encodeし、似た観察でも異なる操作phaseを区別するPMTRM。時間的heterogeneityと再構成教師を使い、既存のACT・DP・VLAのaction headを保つ。

**主な貢献**

訓練用decoderを捨て、推論時は3.81M encoderだけを使う。T=128のACT判断でRTX4090上0.42ms追加という条件付き測定と、反復操作での履歴効果を報告した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.11168 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.11168v1 。§III-F–G/IV-A–BとTABLE V選読。総訓練module7.61Mと推論encoder3.81Mを区別。0.42msは6.8ms base ACTに対する6.2%増で、全VLA共通latencyではない。preceding executed actionのみqueueに入れ将来chunkは含めない。実機は各10rolloutでconfidence幅が広く、simulation multi-seedと証拠強度を分ける。MemoryVLAへの追加結果はaligned action stream不足で省略。コード/重み/実装ライセンス未確認。 PDF未取得。

### MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation

- ID: `VLA-0192`
- Published: 2026-09-30
- Authors: Egor Cherepanov; Nikita Kachaev; Aleksandr I. Panov; Alexey K. Kovalev
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.00604) · [Code](https://github.com/CognitiveAISystems/MIKASA-Robo) · [Project](https://mikasarobo.github.io/)
- Tags: MIKASA-Robo-VLA, memory-benchmark, language-conditioned, partial-observability, information-gap, ManiSkill, RLDS, LeRobot
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

行動に必要な手掛かりが消えた後の記憶を測る、90言語条件付き操作task・10memory typeのbenchmark。80taskは記憶を必要とし、10taskは手掛かりが見えるreactive control。情報が確実に見えないintervalとepisode horizonを区別し、22,500 oracle trajectoryをRLDS/LeRobot形式で提供する。

**主な貢献**

記憶内容、遅延、観測interface、seed、成功基準を明示してVLA評価を標準化。現時点のpi0.5参照baselineはhistory/明示memoryなしの14task subset・各20episodeで平均成功0.211±0.044。全90taskの代表成績とは扱わず、Long-split低下はopen-loop chunkとmemory type構成が交絡する。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv IDは2610だがsubmission history v1は2026-09-30、改訂なし。https://arxiv.org/html/2610.00604v1 の§3、§5.2、Datasheet Distributionを選択確認。公式docs/repoにVLA suiteと評価code、MIT licenseはhttps://github.com/CognitiveAISystems/MIKASA-Robo/blob/main/LICENSE で確認。weightsは未確認でunknown。dataset releaseとmodel weightsを混同しない。projectのICLR2026引用は前身MIKASA-Robo論文であり、このVLA論文のvenueとは扱わない。PDF未取得。

### Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

- ID: `VLA-0141`
- Published: 2026-09-29
- Authors: Yaxin Zhao; Dianye Huang; Chenwei Wang; Chenguang Yang; Zhongliang Jiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.37307) · [PDF](https://arxiv.org/pdf/2609.37307)
- Tags: ActMem-VLA, action-history, Mamba-2, dual-expert-denoising, frozen-base-policy, LIBERO-Mem
- Model size: 追加パラメータは基盤VLAの3.45%（総パラメータ数は未確認）
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ActMem-VLAは、実行済み行動の履歴をMamba-2で記憶し、軽量PreAction Expertが高ノイズ側の生成を担当した後、凍結した元のAction Expertへ途中状態を引き継ぐ。調整済み基盤VLAのVLMとAction Expertを固定し、記憶モジュールとPreAction Expertだけを学習して、観測が似る異なる作業段階の混同を抑える。

**主な貢献**

行動履歴による初期デノイジングと凍結方策による後段精密化を分離し、追加パラメータ3.45%で時間的適応を行う。シミュレーションではデモ長に基づくタスク別ステップ制限下のLIBERO-Mem 10タスクで80.8%（π0.5:65.2%、MemoryVLA:49.5%）。DOBOT Novaの4タスク各20試行ではπ0.5の35.0%から63.75%へ改善した。

**確認記録**

- Checked: 2026-10-04 · Review: needs-review
- 書誌と履歴: https://arxiv.org/abs/2609.37307 。v1は2026-09-29 11:43:19 UTC、改訂なし。方法・評価: https://arxiv.org/html/2609.37307v1 のIII節・IV-B・IV-C・IV-D。80.8%は標準600step制限の数値ではなく、デモ長95分位から作るタスク別期限での平均。標準条件では循環動作で成功でき、記憶利用を識別しにくい限界を本文が明記。実機の28.8%表記はIV-Dの35.0%→63.75%から28.8 percentage pointsと解釈し、相対改善率にはしない。部品除去の効果はタスク依存。abs/HTMLに公式公開先はない。検索で https://github.com/hit-my/PhaseVLA と https://huggingface.co/HITdongdong/ActMem-VLA を確認したが、論文著者による公式提供との結び付きを検証できないため正式URL/statusには採用せずneeds-review。候補repoの https://github.com/hit-my/PhaseVLA/blob/main/LICENSE はApache-2.0だが、本文との公式関係は未確認。候補の https://github.com/hit-my/PhaseVLA/blob/main/releases/2026-09-28/README.md とモデルカードは、修正前後の履歴勾配・タスク別plugin・探索的checkpoint選択を区別し、matching baseの公開downloadを示していない。論文CC BY-SA 4.0とコード・重みのライセンスは別。PDF URLはabsページのリンクのみ確認し、PDFを取得していない。

### Vision-Language-Action Autonomous Driving Agent with Language-based Memory

- ID: `VLA-0140`
- Published: 2026-09-29
- Authors: Kai Yan; Xiangyu Chen; Yulong Cao; Alex Naumann; Peter Karkus; Yan Wang; Jef Packer; Alex Schwing; Yuxiong Wang; Boris Ivanovic; Wenjie Luo; Marco Pavone
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.38641) · [Project](https://kaiyan289.github.io/projects/ad-memo/)
- Tags: AD-Memo, driving, language-memory, Da-Capo, semi-closed-loop-RL, supporting-foundation
- Model size: Alpamayo 2 2B VLA backbone; 8B SFT ablation
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

運転に重要な周辺物体を言語メモとして書き、後の軌跡予測と質問応答に再利用するAD-Memo。Da Capoは運転トークンへ時点別、メモへ将来依存の学習信号を割り当てる。

**主な貢献**

四方停止と一般運転の実映像クリップで軌跡品質・記憶質問応答・他モデルへのメモ移植を評価。制御入力は正解履歴を再生し、記憶だけを閉ループ化するため、実車の閉ループ走行成功や安全性能を実証した結果ではない。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.38641v1 の3節、4節のbaseline設定、付録D.2/Fと公式projectの評価を確認。主実験は約10秒の言語メモと2B VLA backboneで、Alpamayoのaction expertは含まない。8BはSFT追加評価。本文/公式projectに専用code・weight・実装license提供先を確認できずunknown。運転分野の支援研究として扱い、マニピュレーションへの効果は未検証。PDF未取得。

### D²-VLA: Dual-Memory Dual-Frequency Vision-Language-Action Model For Long Dynamic Manipulation

- ID: `VLA-0124`
- Published: 2026-09-28 · Updated: 2026-09-30
- Authors: Zijian Ye; Chengqi Wei; Wei Huang; Anlin Zheng; Chunyu Zou; Liangyu Wu; Zikang Zhao; Zhenjie Peng; Yushuo Yang; Shuman Zhao; Zhongrui Wang; Xiaojuan Qi
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.34792)
- Tags: dual-memory, kv-cache, multi-rate, dynamic-manipulation
- Model size: PaliGemma-3B backbone; total unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

過去の視覚情報を保持しながら動く物体へ素早く反応するD²-VLA。VLMと行動専門家に別々の履歴KV参照を持たせ、低頻度VLM更新の間は新しい視覚特徴で行動条件を補正する。

**主な貢献**

ブロック単位の因果KV再利用と非対称な二重記憶、異なる更新周期の制御を統合。過去の視覚手掛かりと動的操作を要するDOMINO-Longを導入。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 and v2 exact dates verified; one identity, not two additions. Primary HTML https://arxiv.org/html/2609.34792v2 links https://github.com/CVMI-Lab/DMDF-VLA; repository currently shows Readme.md and images only, so actual implementation, code license and weights remain unknown. Linked project on zijianyy.github.io failed to fetch; exact project path not recorded. Backbone stated in §5.1; total parameters not verified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### MemBodied: Recurrent Associative Memory for Vision-Language-Action Models

- ID: `VLA-0130`
- Published: 2026-09-23
- Authors: Tej Deep Pala; Navonil Majumder; Bryce Goh; Raphael Yee; Jianfei Yang; Liming Chen; Soujanya Poria
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.28256) · [Code](https://github.com/declare-lab/MemBodied) · [Project](https://declare-lab.github.io/MemBodied/)
- Tags: associative-memory, episodic-anchor, recurrent, partial-observability
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

エピソードの初期場面を保持するアンカーと、行動後の結果を書き込む連想記憶をVLAへ追加するMemBodied。過去画像列を無制限に入力せず、固定サイズの状態から行動を生成する。

**主な貢献**

層別の連想読み出しと遅延した遷移条件付き書き込みにより、履歴依存の操作を支援。5RMBenchタスクで平均成功率50%を報告し、記憶の構成を比較。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv submission history shows v1 only on 2026-09-23, despite secondary indexing timestamps on Sep 24; do not treat indexing as revision. Official project and implementation verified. https://github.com/declare-lab/MemBodied/blob/main/LICENSE is Apache 2.0; vendored components retain their licenses. README explicitly says trained checkpoints are not bundled; no public weight download verified, so weights unknown. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

- ID: `VLA-0116`
- Published: 2025-08-26 · Updated: 2026-01-30
- Authors: Hao Shi; Bin Xie; Yingfei Liu; Lin Sun; Fengrong Liu; Tiancai Wang; Erjin Zhou; Haoqiang Fan; Xiangyu Zhang; Gao Huang
- Venue: ICLR 2026
- Links: [Paper](https://arxiv.org/abs/2508.19236) · [PDF](https://arxiv.org/pdf/2508.19236) · [Code](https://github.com/shihao1895/MemoryVLA) · [Project](https://shihao1895.github.io/MemoryVLA)
- Tags: MemoryVLA, working-memory, episodic-memory, temporal-context, long-horizon
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / available / unspecified

**概要（日本語）**

現在観測の知覚・認知トークンをworking memoryとし、過去の低レベル詳細と意味情報をmemory bankへ保持するVLA。必要な記憶の検索・融合・重複統合を行い、記憶条件付き拡散行動生成で長期操作を評価した。

**主な貢献**

Perceptual-Cognitive Memory Bankとworking-memory検索を接続し、現在フレームだけでは解けない時間依存操作へ対応。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。実装とモデルcollectionを確認。2026-10-01時点で公開リポジトリrootにLICENSEなし、GitHub license=null。ライセンス未指定のためopen\_sourceはunknown。https://huggingface.co/collections/shihao1895/memoryvla
