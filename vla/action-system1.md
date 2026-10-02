<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / action-system1

[← vla](README.md) · [CSV master](../papers.csv)

17 records · Published date 降順（同日 ID 降順）

### WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation

- ID: `VLA-0134`
- Published: 2026-10-01
- Authors: Samuel Zhen; Siwon Jo; Yanze Zhang; Wenhao Luo
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01083)
- Tags: safety-filter, whole-body, attached-geometry, control-barrier-function
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ロボット全身と把持物の形状をまとめた安全集合を構成し、VLAの運動指令をCBF-QPで小さく修正する推論時安全フィルター。把持の有無で保護対象を切り替え、グリッパ指令は維持する。

**主な貢献**

Bernstein多項式距離場による幾何制約を操作空間へ写像。SafeLIBEROの1600シミュレーション試行でScene Safety 97.38%、Safe Success 59.38%を報告するが、理想的な固定把持モードの保証と近似・緩和付き実装は区別される。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2610.01083v1 のIII–IV節、V節、結論の限界を読んだ。評価はシミュレータ由来の対象物役割情報を利用し、実機安全保証ではない。本文の公開リンクと対象タイトル検索で公式実装・重み・実装ライセンスを確認できずunknown。PDF未取得、正確なPDF href未抽出のためpdf\_urlは空欄。

### Spike-driven Vision-Language-Action Model

- ID: `VLA-0126`
- Published: 2026-09-30
- Authors: Shuai Wang; Malu Zhang; Mingquan Liu; Weihui Dai; Dehao Zhang; Jieyuan Zhang; Yimeng Shan; Zijian Zhou; Yang Yang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.39514)
- Tags: spiking-neural-network, neuromorphic, efficiency, action-chunking
- Model size: 0.15B
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

スパイキング視覚・言語エンコーダー、疎な多勝者融合、スパイキング行動チャンクTransformerを組み合わせたVLA。LIBEROとMeta-Worldで小規模モデルの操作性能と計算量を評価する。

**主な貢献**

直接エンドツーエンド学習できるスパイク駆動VLAを提案し、0.15Bパラメーターで操作方策を構成。エネルギーは演算ベースの推定値で、実測電力や実機汎化の証拠と区別する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.39514v1 Tables 1–2 verify 0.15B and estimated energy; §5 uses simulation benchmarks. No author-owned project/code/license or weights verified. Paper text and Table 3 disagree on LIBERO-Plus aggregate (53.2% versus 54.9%), so that metric is deliberately omitted. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation

- ID: `VLA-0125`
- Published: 2026-09-30
- Authors: Di Wu; Rongtian Shen; Ping Liu; Yan Shen; Zhenhan Yin; Shun Zuo; Xuhua Chen; He Zheng; Lingfeng Zhang; Jianglin Zhang; Tao Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.39822) · [Code](https://github.com/MagiclabRobotics/Inference) · [Project](https://embodied.magiclab.top/works/inference/index.html)
- Tags: real-time, flow-matching, latency, distributed-runtime
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

VLA推論と物理ロボット実行の時間差を端から端まで測定し、流れ場の段階差に基づく2段階ノイズ除去を提案する。推論・行動公開・制御を独立周期で動かす実時間フレームワークを評価。

**主な貢献**

10ステップを非一様な2ステップへ削減し、論文のモデル推論時間を61.557msから21.956msへ短縮。双腕衣服折り畳みで6実行方式を共通条件で比較。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. arXiv comments directly link official project and GitHub. Actual client/server/scripts/tests present; README reports source release 2026-09-30, identifies Apache License 2.0, and GitHub shows Apache-2.0. Root LICENSE content independently read via GitHub connector and confirmed Apache-2.0: https://github.com/MagiclabRobotics/Inference/blob/main/LICENSE . Runtime supports external checkpoints, but paper-specific weights download unverified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models

- ID: `VLA-0119`
- Published: 2026-09-24 · Updated: 2026-09-24
- Authors: Yufei Duan; Hang Yin; Alberta Longhini; Chao Tang; Danica Kragic
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.28865) · [PDF](https://arxiv.org/pdf/2609.28865) · [Project](https://vla-dsd.github.io/)
- Tags: DSD, action-representation, direction-scale-decomposition, tokenization, mixed-dataset
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

位置・回転の増分を方向と大きさへ分解してからトークン化するDSDを提案。速度やデータセットごとの正規化による表現の変化を抑え、BINとB-spline tokenizerで単一・混合データと実機の効果を評価した。

**主な貢献**

動作の幾何学的方向と振幅を別チャネルに保ち、トークン化前の表現設計を改善。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。一次arXivと公式projectのHTMLを確認。公式projectに実装・checkpointリンクを確認できず、release/licenseはunknown。

### Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs

- ID: `VLA-0118`
- Published: 2026-09-24 · Updated: 2026-09-29
- Authors: Riccardo Andrea Izzo; Rimvydas Rubavicius; Gianluca Bardaro; Subramanian Ramamoorthy; Matteo Matteucci; Alessandro Suglia
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.29382) · [PDF](https://arxiv.org/pdf/2609.29382) · [Code](https://github.com/esgi-research-group/ee-vla)
- Tags: early-exit, compute-allocation, flow-matching, KV-cache-synthesis, SmolVLA, π0.5
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

flow-matching VLAのVLM深さ、action expert深さ、denoising回数を独立に調整する。中間層のExit Transformerを最終表現へ蒸留し、飛ばしたVLM層のKV cacheを合成してexpertとの深さの結合を解く。

**主な貢献**

三つの計算軸の分離とKV cache synthesisにより、タスクごとの性能・FLOPs・遅延のtrade-offを制御。

**確認記録**

- Checked: 2026-10-01 · Review: needs-review
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。論文本文はコード・モデル公開を記載するが、リンク先は2026-10-01のweb/公開GitHub API確認で404。公開実装・ライセンス・重みの確認待ち。https://arxiv.org/html/2609.29382v2

### Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

- ID: `VLA-0120`
- Published: 2026-09-21 · Updated: 2026-09-21
- Authors: Fukang Liu; Yipu Chen; Jaehwi Jang; Danfei Xu; Zsolt Kira; Ye Zhao
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.23968) · [PDF](https://arxiv.org/pdf/2609.23968) · [Project](https://opt2vla.github.io/)
- Tags: Opt2VLA, force-conditioning, humanoid, whole-body-control, trajectory-optimization
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

接触の多いヒューマノイド操作で、VLAが幾何的動作目標と接触力参照を同時に予測する。力を明示した全身軌道最適化で教師を作り、task-specificなRL全身制御器が動作と力を追従する。

**主な貢献**

言語から接触力への明示的なVLA-to-controllerインターフェースと、物理整合性のある力・トルク教師。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式projectのCodeボタンは同ページ内placeholderで公開実装先なし。実装の公開・ライセンスは未確認、重みはunknown。

### VLPSA: Vision-Language-Poisson-Safe Actions for Full-Body Safety of Learned Policies

- ID: `VLA-0132`
- Published: 2026-09-18
- Authors: Meg Wilkinson; Emily Fourney; Joel W. Burdick; Aaron D. Ames
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.22462)
- Tags: safety-filter, control-barrier-function, full-body, collision-avoidance
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VLAを再学習せず、知覚から生成するPoisson安全関数とCBF-QPでロボット全身および把持物の衝突回避を制約するVLPSA。複数解像度を組み合わせて実時間実行を目指す。

**主な貢献**

把持物を最終リンクの延長として安全制約へ含め、SafeLIBEROとFranka FR3の動的障害物環境で評価。安全保証は知覚・障害物速度・到達可能性等の仮定付き。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.22462v1 checked; no official implementation/license or weights verified. §IV-C5 explicitly states sensing/update-delay and robot velocity limitations; reported 91.2% collision avoidance is benchmark evidence, not unconditional real-world safety. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation

- ID: `VLA-0129`
- Published: 2026-09-17 · Updated: 2026-09-18
- Authors: Kaivalya Agrawal; Md Ashiqur Rahman; Raymond A. Yeh; Zachary Kingston
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.20648)
- Tags: classical-motion-planning, hybrid-control, efficiency, frozen-backbone
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

接触を要する操作だけをVLAに任せ、自由空間の移動を古典的な衝突回避プランナーで行うSkipVLA。凍結VLMの特徴からプランナー目標姿勢を予測する。

**主な貢献**

全区間で重い方策推論を繰り返さず、既存VLAの知識から目標予測器を学習。3VLA・13LIBEROタスクとYAM実機で、同程度の成功率のまま最大2.5倍の実行高速化を報告。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv exact v1/v2 submission dates verified; one identity. Primary HTML https://arxiv.org/html/2609.20648v2 checked; no official implementation/license or trained weights verified. Category is vla/action-system1 with hybrid-control tag: a classical planner alone is not inferred to be an LLM agent. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs

- ID: `VLA-0121`
- Published: 2026-09-17 · Updated: 2026-09-17
- Authors: Yiheng Ji; Xingru Zhou; Luis Sentis; Mingyo Seo
- Venue: CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2609.21022) · [PDF](https://arxiv.org/pdf/2609.21022) · [Code](https://github.com/jidaxian010/VLA-Feedback-release) · [Project](https://vla-feedback.github.io/)
- Tags: VLA-Feedback, real-time-feedback, two-timescale-control, feedback-denoising, dynamic-manipulation
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

低頻度のVLA拡散計画と高頻度の視覚feedbackを分ける。動作列の最後のdenoisingを軽量feedbackインターフェースとして残し、各動作を最新観測で補正して、動く物体への追従を改善する。

**主な貢献**

全VLMを再推論せずに動作チャンク内へ視覚feedbackを挿入する、最終denoising-stepの再利用。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。実装Apache-2.0。公開はsimulation checkpoint cp\_sim\_obs/cp\_libero\_obs: https://huggingface.co/jidaxian010/vla-feedback-sim 。実機重み公開とは区別。 Code license: Apache-2.0; https://github.com/jidaxian010/VLA-Feedback-release/blob/main/LICENSE.

### SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

- ID: `VLA-0108`
- Published: 2025-06-02 · Updated: 2025-06-02
- Authors: Mustafa Shukor; Dana Aubakirova; Francesco Capuano; Pepijn Kooijmans; Steven Palma; Adil Zouitine; Michel Aractingi; Caroline Pascal; Martino Russi; Andres Marafioti; Simon Alibert; Matthieu Cord; Thomas Wolf; Remi Cadene
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2506.01844) · [PDF](https://arxiv.org/pdf/2506.01844) · [Code](https://github.com/huggingface/lerobot) · [Project](https://huggingface.co/lerobot/smolvla_base)
- Tags: SmolVLA, efficient-inference, asynchronous-control, community-data, flow-matching
- Model size: 450M (main model; ~100M action expert)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

小型VLMとflow-matching action expertを組み合わせ、低価格ロボットのコミュニティデータで学習。観測・推論と動作実行を非同期化し、推論待ちによる反応遅延を減らす。シミュレーションと実機で大規模VLAとの比較を行った。

**主な貢献**

VLM層・視覚トークン削減、交互のcross/self-attention、非同期実行を統合する低計算量VLA。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。一次本文§4.3で規模を確認。重みApache-2.0: https://huggingface.co/lerobot/smolvla\_base Code license: Apache-2.0; https://github.com/huggingface/lerobot/blob/main/LICENSE.

### GR00T N1: An Open Foundation Model for Generalist Humanoid Robots

- ID: `VLA-0109`
- Published: 2025-03-18 · Updated: 2025-03-27
- Authors: NVIDIA; Johan Bjorck; Fernando Castañeda; Nikita Cherniadev; Xingye Da; Runyu Ding; Linxi "Jim" Fan; Yu Fang; Dieter Fox; Fengyuan Hu; Spencer Huang; Joel Jang; Zhenyu Jiang; Jan Kautz; Kaushil Kundalia; Lawrence Lao; Zhiqi Li; Zongyu Lin; Kevin Lin; Guilin Liu; Edith Llontop; Loic Magne; Ajay Mandlekar; Avnish Narayan; Soroush Nasiriany; Scott Reed; You Liang Tan; Guanzhi Wang; Zu Wang; Jing Wang; Qi Wang; Jiannan Xiang; Yuqi Xie; Yinzhen Xu; Zhenjia Xu; Seonghyeon Ye; Zhiding Yu; Ao Zhang; Hao Zhang; Yizhou Zhao; Ruijie Zheng; Yuke Zhu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2503.14734) · [PDF](https://arxiv.org/pdf/2503.14734) · [Code](https://github.com/NVIDIA/Isaac-GR00T) · [Project](https://developer.nvidia.com/isaac/gr00t)
- Tags: GR00T-N1, humanoid, dual-system, flow-matching, synthetic-data
- Model size: 2B (GR00T-N1-2B checkpoint)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

ヒューマノイド向けの汎用VLA。視覚言語モジュールと拡散Transformer行動モジュールを密に結合し、実機・人間動画・合成データを混ぜて学習。異なる身体のシミュレーションと実機双腕操作でデータ効率を評価した。

**主な貢献**

意味解釈と連続運動生成のdual-system構成を、異種データの共同学習で汎用ヒューマノイド制御へ展開。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。コードApache-2.0。重みは別のNVIDIAライセンス: https://huggingface.co/nvidia/GR00T-N1-2B 。open\_source判定はコードのみ。 Code license: Apache-2.0; https://github.com/NVIDIA/Isaac-GR00T/blob/main/LICENSE.

### FAST: Efficient Action Tokenization for Vision-Language-Action Models

- ID: `VLA-0112`
- Published: 2025-01-16 · Updated: 2025-01-16
- Authors: Karl Pertsch; Kyle Stachowicz; Brian Ichter; Danny Driess; Suraj Nair; Quan Vuong; Oier Mees; Chelsea Finn; Sergey Levine
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2501.09747) · [PDF](https://arxiv.org/pdf/2501.09747) · [Code](https://huggingface.co/physical-intelligence/fast) · [Project](https://www.pi.website/research/fast)
- Tags: FAST, action-tokenization, discrete-cosine-transform, compression, autoregressive-VLA
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

動作を次元・時刻ごとにビン分割すると高周波で器用な動作が学びにくい問題を検討。離散コサイン変換と圧縮を使うFASTで動作列をトークン化し、100万動作列から学習した汎用tokenizer FAST+を公開した。

**主な貢献**

周波数空間で行動列を圧縮して自己回帰VLAの離散表現を効率化するFASTと汎用FAST+。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。Hugging Faceにprocessorのソースと学習済みtokenizer。Apache-2.0: https://huggingface.co/physical-intelligence/fast 。weights\_statusはtokenizer artifactの公開を示す。

### π0: A Vision-Language-Action Flow Model for General Robot Control

- ID: `VLA-0106`
- Published: 2024-10-31 · Updated: 2026-01-08
- Authors: Kevin Black; Noah Brown; Danny Driess; Adnan Esmail; Michael Equi; Chelsea Finn; Niccolo Fusai; Lachy Groom; Karol Hausman; Brian Ichter; Szymon Jakubczak; Tim Jones; Liyiming Ke; Sergey Levine; Adrian Li-Bell; Mohith Mothukuri; Suraj Nair; Karl Pertsch; Lucy Xiaoyang Shi; James Tanner; Quan Vuong; Anna Walling; Haohuan Wang; Ury Zhilinsky
- Venue: RSS 2025
- Links: [Paper](https://arxiv.org/abs/2410.24164) · [PDF](https://arxiv.org/pdf/2410.24164) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://physicalintelligence.company/blog/pi0)
- Tags: π0, flow-matching, generalist-policy, dexterous-manipulation, action-chunking
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

事前学習VLMへflow-matchingの行動生成器を接続し、複数の単腕・双腕・移動ロボットのデータで学習。ゼロショット制御、言語指示への追従、新スキルへの微調整を多様な器用さの必要なタスクで検証した。

**主な貢献**

Web由来の意味表現を維持するVLMと、高周波の連続行動チャンクを生成するflow expertの統合。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。arXiv v4コメントにRSS 2025。公式READMEにpi0\_baseと実機タスク別checkpoint。https://github.com/Physical-Intelligence/openpi\#model-checkpoints Code license: Apache-2.0; https://github.com/Physical-Intelligence/openpi/blob/main/LICENSE.

### RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

- ID: `VLA-0114`
- Published: 2024-10-10 · Updated: 2025-03-01
- Authors: Songming Liu; Lingxuan Wu; Bangguo Li; Hengkai Tan; Huayu Chen; Zhengyi Wang; Ke Xu; Hang Su; Jun Zhu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2410.07864) · [PDF](https://arxiv.org/pdf/2410.07864) · [Code](https://github.com/thu-ml/RoboticsDiffusionTransformer) · [Project](https://rdt-robotics.github.io/rdt-robotics/)
- Tags: RDT-1B, diffusion-transformer, bimanual, unified-action-space, cross-embodiment
- Model size: 1.2B (main diffusion model)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

双腕操作の多峰性とデータ不足に対応する大規模diffusion方策。物理的意味を維持する統一行動空間で異なるロボットのデータを混ぜ、双腕データで微調整して実機の器用さ・未知物体・少数デモ適応を検証した。

**主な貢献**

物理的に解釈可能な統一行動空間と、大規模Transformer拡散生成を組み合わせた双腕基盤方策。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。要旨・公式projectは1.2Bと記載。コード・重みMIT: https://github.com/thu-ml/RoboticsDiffusionTransformer\#license Code license: MIT; https://github.com/thu-ml/RoboticsDiffusionTransformer/blob/main/LICENSE.

### Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

- ID: `VLA-0110`
- Published: 2023-04-23 · Updated: 2023-04-23
- Authors: Tony Z. Zhao; Vikash Kumar; Sergey Levine; Chelsea Finn
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2304.13705) · [PDF](https://arxiv.org/pdf/2304.13705) · [Code](https://github.com/tonyzhaozh/act) · [Project](https://tonyzhaozh.github.io/aloha/)
- Tags: ACT, action-chunking, imitation-learning, bimanual, baseline, non-language-policy
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

低価格の双腕装置とテレオペレーションで集めたデモから、細かな実機操作を学ぶ。ACTは動作列をまとめて予測する生成モデルを使い、逐次模倣の誤差蓄積や人間デモの非定常性を抑える。

**主な貢献**

Action Chunking with Transformersによる動作列予測と時間的アンサンブル。VLAの比較基盤となる非言語条件付き方策。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。言語条件付きVLAではなく、ユーザー指定の主要action-policy先行研究として収録。 Code license: MIT; https://github.com/tonyzhaozh/act/blob/main/LICENSE.

### Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

- ID: `VLA-0111`
- Published: 2023-03-07 · Updated: 2024-03-14
- Authors: Cheng Chi; Zhenjia Xu; Siyuan Feng; Eric Cousineau; Yilun Du; Benjamin Burchfiel; Russ Tedrake; Shuran Song
- Venue: RSS 2023; journal extension
- Links: [Paper](https://arxiv.org/abs/2303.04137) · [PDF](https://arxiv.org/pdf/2303.04137) · [Code](https://github.com/real-stanford/diffusion_policy) · [Project](https://diffusion-policy.cs.columbia.edu/)
- Tags: Diffusion-Policy, action-diffusion, receding-horizon, visuomotor, baseline
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

視覚条件付き方策を行動分布のdenoising diffusionとして表し、複数の妥当な動作や高次元行動を扱う。receding-horizon制御と時系列diffusion Transformerを組み合わせ、複数の操作ベンチマークと実機で評価した。

**主な貢献**

画像生成ではなく行動列へ拡散モデルを適用し、視覚条件と閉ループ再計画を統合。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。初稿は2023-03-07。arXiv v5はRSS 2023論文の拡張版。公式READMEに公開training outputs/checkpoints。 Code license: MIT; https://github.com/real-stanford/diffusion\_policy/blob/main/LICENSE.

### RT-1: Robotics Transformer for Real-World Control at Scale

- ID: `VLA-0101`
- Published: 2022-12-13 · Updated: 2023-08-11
- Authors: Anthony Brohan; Noah Brown; Justice Carbajal; Yevgen Chebotar; Joseph Dabis; Chelsea Finn; Keerthana Gopalakrishnan; Karol Hausman; Alex Herzog; Jasmine Hsu; Julian Ibarz; Brian Ichter; Alex Irpan; Tomas Jackson; Sally Jesmonth; Nikhil J Joshi; Ryan Julian; Dmitry Kalashnikov; Yuheng Kuang; Isabel Leal; Kuang-Huei Lee; Sergey Levine; Yao Lu; Utsav Malla; Deeksha Manjunath; Igor Mordatch; Ofir Nachum; Carolina Parada; Jodilyn Peralta; Emily Perez; Karl Pertsch; Jornell Quiambao; Kanishka Rao; Michael Ryoo; Grecia Salazar; Pannag Sanketi; Kevin Sayed; Jaspiar Singh; Sumedh Sontakke; Austin Stone; Clayton Tan; Huong Tran; Vincent Vanhoucke; Steve Vega; Quan Vuong; Fei Xia; Ted Xiao; Peng Xu; Sichun Xu; Tianhe Yu; Brianna Zitkovich
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2212.06817) · [PDF](https://arxiv.org/pdf/2212.06817) · [Code](https://github.com/google-research/robotics_transformer) · [Project](https://robotics-transformer1.github.io/)
- Tags: RT-1, generalist-policy, action-tokenization, real-robot, language-conditioned
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

画像履歴と自然言語指示から離散行動を予測するRobotics Transformerを提案。多様な実機デモを用い、未知タスク・物体・背景への汎化と異なるロボットの経験からの転移を検証した。

**主な貢献**

言語条件付きEfficientNet、TokenLearner、Transformerを接続し、大規模多タスク模倣学習を実機閉ループ制御へ展開。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式READMEのtrained\_checkpointsに3種類のRT-1重み。https://github.com/google-research/robotics\_transformer\#using-trained-checkpoints Code license: Apache-2.0; https://github.com/google-research/robotics\_transformer/blob/master/LICENSE.
