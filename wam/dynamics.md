<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / dynamics

[← wam](README.md) · [CSV master](../papers.csv)

7 records · Published date 降順（同日 ID 降順）

### LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models

- ID: `WAM-0036`
- Published: 2026-08-06 · Updated: 2026-08-06
- Authors: Jiarui Yang; Jiale Zhange; Jiawei Li; Hang Guo; Wen Huang; Jinpeng Wang; Peidong Liu; Shu-Tao Xia
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2608.05706v1) · [PDF](https://arxiv.org/pdf/2608.05706v1)
- Tags: Latent Action, Human Video, Multi-view, 3D Geometry, RGB-D
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動ラベルのない人の動画から、視点をまたいで使える三次元的な潜在行動を学ぶ研究。動画を複数視点に増やすだけでは残る、見た目による近道を扱う。

**主な貢献**

複数視点で共有する行動トークン、三次元基盤特徴との幾何整合、RGB-D共同再構成を結合して未来フレームの外観漏洩を抑える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning

- ID: `WAM-0038`
- Published: 2026-07-27 · Updated: 2026-07-27
- Authors: Wenxuan Ma; Chaofan Zhang; Chao Xue; Yinghao Cai; Guocai Yao; Shaowei Cui; Shuo Wang
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2607.24267v1) · [PDF](https://arxiv.org/pdf/2607.24267v1)
- Tags: Visuo-tactile, Contact, Slip Prediction, CEM, FeelWorld
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

見た目だけでは捉えにくい接触と滑りを、視覚・触覚の未来予測へ組み込むFeelWorldを提案。接触を伴う把持や挿入で、予測と候補行動の計画を評価する。

**主な貢献**

接触状態、力を含む三次元触覚潜在、滑り状態を階層的に予測し、接触前後で注意経路を切り替えるcontact gatingを使う。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

- ID: `WAM-0001`
- Published: 2026-03-13 · Updated: 2026-06-03
- Authors: Lucas Maes; Quentin Le Lidec; Damien Scieur; Yann LeCun; Randall Balestriero
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2603.19312v3) · [PDF](https://arxiv.org/pdf/2603.19312v3) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)
- Tags: JEPA, Latent Dynamics, Pixel Control, SIGReg
- Model size: ~15M
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

画素から小さな潜在状態と行動条件付き予測を同時に学び、画像目標への計画に使う世界モデル。大規模な固定視覚エンコーダを使う方式に対し、学習と候補行動の探索を軽くする設計を検証した。

**主な貢献**

次状態の潜在予測誤差とSIGRegの二項だけで表現崩壊を抑え、エンコーダと予測器を一体学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT; source: https://github.com/lucas-maes/le-wm.

### Denoised MDPs: Learning World Models Better Than the World Itself

- ID: `WAM-0016`
- Published: 2022-06-30 · Updated: 2023-04-06
- Authors: Tongzhou Wang; Simon S. Du; Antonio Torralba; Phillip Isola; Amy Zhang; Yuandong Tian
- Venue: ICML 2022
- Links: [Paper](https://arxiv.org/abs/2206.15477v6) · [PDF](https://arxiv.org/pdf/2206.15477v6) · [Code](https://github.com/facebookresearch/denoised_mdp) · [Project](https://ssnl.github.io/denoised_mdp/)
- Tags: Factorized State, Controllability, Reward-conditioned, Denoised MDP
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

外界の情報を、制御できるか・報酬に関係するかで分けて世界モデルを学ぶ研究。背景などの外乱を明示的に分離し、制御に使う潜在状態を絞る。

**主な貢献**

制御可能性と報酬関連性による四種類の潜在因子を設け、制御可能かつ報酬関連な状態へ方策学習を集中させる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Venue and author list cross-checked against https://proceedings.mlr.press/v162/wang22c.html. Official implementation and CC-BY-NC 4.0 license checked at https://github.com/facebookresearch/denoised\_mdp.

### Contrastive Learning of Structured World Models

- ID: `WAM-0048`
- Published: 2019-11-27 · Updated: 2020-01-05
- Authors: Thomas Kipf; Elise van der Pol; Max Welling
- Venue: ICLR 2020
- Links: [Paper](https://arxiv.org/abs/1911.12247v2) · [PDF](https://arxiv.org/pdf/1911.12247v2) · [Code](https://github.com/tkipf/c-swm)
- Tags: Object-centric, Graph Dynamics, Contrastive Learning, C-SWM
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

画素から物体と関係を分けて学び、構造化した潜在空間で行動後の状態を予測するC-SWMを提案。複数物体が独立に操作される環境で、再構成型モデルとの違いを評価する。

**主な貢献**

物体単位の状態埋め込みとグラフニューラルネットワークによる遷移を、対照的な予測目的で学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/tkipf/c-swm.

### Learning Latent Dynamics for Planning from Pixels

- ID: `WAM-0040`
- Published: 2018-11-12 · Updated: 2019-06-04
- Authors: Danijar Hafner; Timothy Lillicrap; Ian Fischer; Ruben Villegas; David Ha; Honglak Lee; James Davidson
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/1811.04551v5) · [PDF](https://arxiv.org/pdf/1811.04551v5) · [Code](https://github.com/google-research/planet) · [Project](https://danijar.com/project/planet/)
- Tags: Model-based RL, Stochastic Dynamics, Latent Overshooting, PlaNet
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

画像から環境の動力学を学び、潜在空間内のオンライン計画だけで行動を選ぶPlaNetを提案。部分観測や接触、疎な報酬を含む連続制御でモデルの長期予測を評価する。

**主な貢献**

決定論的な再帰状態と確率的な潜在状態を組み合わせ、複数段先の整合を学ぶlatent overshooting目的を加える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and Apache-2.0 license license checked at https://github.com/google-research/planet.

### Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models

- ID: `WAM-0044`
- Published: 2018-05-30 · Updated: 2018-11-02
- Authors: Kurtland Chua; Roberto Calandra; Rowan McAllister; Sergey Levine
- Venue: NeurIPS 2018
- Links: [Paper](https://arxiv.org/abs/1805.12114v2) · [PDF](https://arxiv.org/pdf/1805.12114v2) · [Code](https://github.com/kchua/handful-of-trials) · [Project](https://sites.google.com/view/drl-in-a-handful-of-trials/)
- Tags: Probabilistic Dynamics, Ensemble, Uncertainty, Model-based RL, PETS
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

少数の実環境試行から使える動力学モデルPETSを提案。モデル予測の不確実性を候補軌跡へ伝え、モデルベース制御のデータ効率と最終性能を両立させる。

**主な貢献**

確率的ニューラル動力学のアンサンブルと、粒子を使うtrajectory samplingによる不確実性伝播を結合する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/kchua/handful-of-trials.
