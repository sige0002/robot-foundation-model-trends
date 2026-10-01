<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / planning

[← wam](README.md) · [CSV master](../papers.csv)

10 records · Published date 降順（同日 ID 降順）

### Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving

- ID: `WAM-0037`
- Published: 2026-03-25 · Updated: 2026-03-25
- Authors: Linbo Wang; Yupeng Zheng; Qiang Chen; Shiwei Li; Yichen Zhang; Zebin Xing; Qichao Zhang; Xiang Li; Deheng Qian; Pengxuan Yang; Yihang Dong; Ce Hao; Xiaoqing Ye; Junyu han; Yifeng Pan; Dongbin Zhao
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2603.24581v1) · [PDF](https://arxiv.org/pdf/2603.24581v1)
- Tags: Autonomous Driving, Geometry Distillation, Latent Dynamics, Latent-WAM
- Model size: 104M
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

複数カメラ画像を圧縮した世界表現と将来予測を、自動運転の軌跡計画へ使うLatent-WAMを提案。ロボット操作とは異なる運転領域で、限られた計算とデータを評価する。

**主な貢献**

幾何知識を蒸留する学習可能なシーンクエリと、視覚・運動履歴に条件付けた因果Transformerの潜在予測を組み合わせる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

- ID: `WAM-0032`
- Published: 2024-11-07 · Updated: 2025-02-01
- Authors: Gaoyue Zhou; Hengkai Pan; Yann LeCun; Lerrel Pinto
- Venue: ICML 2025
- Links: [Paper](https://arxiv.org/abs/2411.04983v2) · [PDF](https://arxiv.org/pdf/2411.04983v2) · [Code](https://github.com/gaoyuezhou/dino_wm)
- Tags: JEPA, DINOv2, Image-goal Planning, Offline Learning, DINO-WM
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

オフラインの行動軌跡から視覚的な動力学を学び、初めての画像目標へ行動系列を最適化するDINO-WMを提案。報酬モデルや事前の方策を必要としない計画を評価する。

**主な貢献**

固定DINOv2の空間パッチ特徴を行動条件付きに予測し、候補系列の未来特徴と目標特徴の距離で探索する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT; source: https://github.com/gaoyuezhou/dino\_wm.

### OGBench: Benchmarking Offline Goal-Conditioned RL

- ID: `WAM-0050`
- Published: 2024-10-26 · Updated: 2025-02-13
- Authors: Seohong Park; Kevin Frans; Benjamin Eysenbach; Sergey Levine
- Venue: ICLR 2025
- Links: [Paper](https://arxiv.org/abs/2410.20092v2) · [PDF](https://arxiv.org/pdf/2410.20092v2) · [Code](https://github.com/seohongpark/ogbench) · [Project](https://seohong.me/projects/ogbench)
- Tags: Benchmark, Offline RL, Goal-conditioned, Stitching, OGBench
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

報酬のないオフライン軌跡から、任意の目標へ行く能力を比較するOGBenchを提案。世界モデルや目標条件付き方策に必要な能力を、単一の成功率だけにまとめず測れる評価基盤。

**主な貢献**

環境とデータセットを設計して、軌跡のつなぎ合わせ、長期推論、高次元入力、確率性を個別に調べる標準実装と評価を提供する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/seohongpark/ogbench.

### TD-MPC2: Scalable, Robust World Models for Continuous Control

- ID: `WAM-0039`
- Published: 2023-10-25 · Updated: 2024-03-21
- Authors: Nicklas Hansen; Hao Su; Xiaolong Wang
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2310.16828v2) · [PDF](https://arxiv.org/pdf/2310.16828v2) · [Code](https://github.com/nicklashansen/tdmpc2) · [Project](https://tdmpc2.com)
- Tags: Model-based RL, Continuous Control, Scaling, TD-MPC2
- Model size: 1M–317M family; 5M default
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

画素の再構成をせずに制御用の潜在モデルを学ぶTD-MPCを、広い連続制御へ拡張した研究。共通の設定で多様な課題を扱い、モデルとデータの規模効果を調べる。

**主な貢献**

SimNormで潜在状態を小さな単体の集合へ正規化し、対数空間の報酬・価値回帰とQアンサンブルで学習を安定させ、方策事前分布を使うMPCへ接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/nicklashansen/tdmpc2. SimNorm and model-size family checked in https://arxiv.org/html/2310.16828v2.

### LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning

- ID: `WAM-0049`
- Published: 2023-06-05 · Updated: 2023-10-14
- Authors: Bo Liu; Yifeng Zhu; Chongkai Gao; Yihao Feng; Qiang Liu; Yuke Zhu; Peter Stone
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2306.03310v2) · [PDF](https://arxiv.org/pdf/2306.03310v2) · [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) · [Project](https://libero-project.github.io/)
- Tags: Benchmark, Lifelong Learning, Language-conditioned, LIBERO
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

ロボット操作の継続学習で、物体・配置・目標などの知識移転を比べるLIBEROを提案。世界モデルそのものではなく、言語条件付き操作の評価基盤と実演データを提供する。

**主な貢献**

手続き的なタスク生成と四つの評価スイートを用意し、課題順序・事前学習・知覚表現が継続学習に与える影響を測る。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/Lifelong-Robot-Learning/LIBERO.

### Mastering Diverse Domains through World Models

- ID: `WAM-0041`
- Published: 2023-01-10 · Updated: 2024-04-17
- Authors: Danijar Hafner; Jurgis Pasukonis; Jimmy Ba; Timothy Lillicrap
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2301.04104v2) · [PDF](https://arxiv.org/pdf/2301.04104v2) · [Code](https://github.com/danijar/dreamerv3) · [Project](https://danijar.com/dreamerv3)
- Tags: Model-based RL, Imagination, Actor Critic, DreamerV3
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

世界モデル内で未来を想像して方策を学ぶDreamerV3を提案。ドメインごとの大幅な設定調整を減らし、画素と疎な報酬から多様な制御課題を学ぶことを狙う。

**主な貢献**

想像した潜在軌跡でactorとcriticを学習し、正規化・損失のバランス・値の変換で複数領域に共通する学習安定性を高める。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/danijar/dreamerv3.

### The Value Equivalence Principle for Model-Based Reinforcement Learning

- ID: `WAM-0043`
- Published: 2020-11-06 · Updated: 2020-11-06
- Authors: Christopher Grimm; André Barreto; Satinder Singh; David Silver
- Venue: NeurIPS 2020
- Links: [Paper](https://arxiv.org/abs/2011.03506v1) · [PDF](https://arxiv.org/pdf/2011.03506v1)
- Tags: Theory, Value Equivalence, Bellman Updates, Model-based RL
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

環境の遷移が違っても、特定の方策と価値関数に対して同じ計画ができるモデルを理論化した研究。表現やモデルへ何を残すべきかを、価値更新の等価性から考える。

**主な貢献**

対象とする関数と方策の集合でBellman更新が一致するvalue equivalenceを定義し、集合を増やしたときのモデルの識別範囲を解析する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

- ID: `WAM-0042`
- Published: 2019-11-19 · Updated: 2020-02-21
- Authors: Julian Schrittwieser; Ioannis Antonoglou; Thomas Hubert; Karen Simonyan; Laurent Sifre; Simon Schmitt; Arthur Guez; Edward Lockhart; Demis Hassabis; Thore Graepel; Timothy Lillicrap; David Silver
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/1911.08265v2) · [PDF](https://arxiv.org/pdf/1911.08265v2)
- Tags: Model-based RL, Tree Search, Reward Value Policy, MuZero
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ゲーム規則や完全なシミュレータを与えず、学習したモデルと木探索で行動を選ぶMuZeroを提案。観測を忠実に再構成する代わりに、判断に必要な量を予測する。

**主な貢献**

反復可能な潜在動力学に報酬・方策・価値の予測を学習させ、そのモデルで探索を行う。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Hierarchical Foresight: Self-Supervised Learning of Long-Horizon Tasks via Visual Subgoal Generation

- ID: `WAM-0047`
- Published: 2019-09-12 · Updated: 2019-09-12
- Authors: Suraj Nair; Chelsea Finn
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/1909.05829v1) · [PDF](https://arxiv.org/pdf/1909.05829v1) · [Project](https://sites.google.com/stanford.edu/hvf)
- Tags: Hierarchical Planning, Visual Subgoal, Video Prediction, HVF
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

遠い画像目標への計画を、途中の視覚サブゴールで分解するHierarchical Visual Foresightを提案。長期の動画予測誤差とサンプリング探索の負担を減らすことを狙う。

**主な貢献**

目標に条件付けて生成する中間画像を直接最適化し、動画予測に基づく短区間の計画を階層的に接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Hidden Failure Modes in Latent World-Model Planning from Offline Data

- ID: `WAM-0046`
- Published: unknown / 未確認
- Authors: Kanpat Vesessook; Kevin Yang
- Venue: ICML 2026 Workshop on Decision-Making from Offline Datasets to Online Adaptation
- Links: [Paper](https://openreview.net/forum?id=kS01rTyQ9s) · [PDF](https://portfolio-rho-flame-83.vercel.app/projects/assets/lewmro/paper.pdf) · [Code](https://github.com/24GUNV/LeWMRO) · [Project](https://portfolio-rho-flame-83.vercel.app/projects/lewmro)
- Tags: Offline Learning, Receding Horizon, Failure Analysis, Workshop, LeWMRO
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

オフライン学習した潜在世界モデルの失敗を、計画の評価時刻と実際の実行区間の不一致から分析する研究。迂回が必要な課題では、目標への距離だけで制御可能性を表せない点も調べる。

**主な貢献**

計画長Hと実行接頭辞Kを分離し、prefix・running costおよびwaypointと局所actuatorの対照実験で二種類の計画インターフェースの失敗を切り分ける。

**確認記録**

- Checked: 2026-10-01 · Review: needs-review
- Publication year 2026 verified from authors and official workshop reference; exact first-publication/submission date unverified because OpenReview requires browser verification and public API returned403. Checkpoints/datasets are not included in the official release. Implementation license checked: MIT; source: https://github.com/24GUNV/LeWMRO.
