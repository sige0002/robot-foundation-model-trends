<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / dynamics

[← wam](README.md) · [CSV master](../papers.csv)

10 records · Published date 降順（同日 ID 降順）

### RoboJEPA: Scaling Robotic Latent World Models

- ID: `WAM-0086`
- Published: 2026-10-07
- Authors: Artem Zholus; Nicolas Beltran-Velez; Jianhao Yuan; Sarath Chandar; Tushar Nagarajan; Daniel Severo; Koustuv Sinha; Michal Drozdzal; Adriana Romero Soriano; Jeannette Bohg; Nicolas Ballas; Mahmoud Assran
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10515) · [Project](https://robojepa.github.io/)
- Tags: RoboJEPA, JEPA, multi-embodiment, latent-dynamics, scaling-laws, image-goal-CEM, fixed-encoder
- Model size: 22M–8B predictor; frozen V-JEPA 2.1 encoder
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結V-JEPA 2.1表現上で、行動・状態・複数視点を入力するlatent予測器を22Mから8Bまで拡張する。23公開データセット・12embodimentを統合し、rollout誤差の計算量依存と画像目標CEM計画の性能を、DROID/RoboCasaとFranka操作で調べた。

**主な貢献**

小規模22M–2Bのfitから4B/8Bを外挿する比較で二次power lawが良好。固定表現上の予測誤差と計画能力の関係を実測。encoder共同scaleやテキスト目標は扱わず、大規模CEMは複数GPUで数秒を要する。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿・書誌: https://arxiv.org/abs/2610.10515 。HTML §2、§3.1–3.4、§5、Appendix G.7を選択精読: https://arxiv.org/html/2610.10515v1 。制約: 固定encoder/固定corpusで飽和近傍、image-goalのみ、学習policy proposalなし。VLAとの比較は目標仕様・訓練・controllerが異なる。論文記載release先 https://github.com/facebookresearch/robo\_jepa はGitHub APIで404、projectはcoming soon。code/weights/licenseはunknown、code\_urlは空欄。具体的追跡: 公式repo公開後に実装ファイル・LICENSE・checkpoint配布先とmodel cardを再確認。PDFは未取得、URL欄は未検証のため空欄。

### World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models

- ID: `WAM-0082`
- Published: 2026-10-06
- Authors: Jiuyi Xu; Xiao Hu; Meida Chen; Peng Gao; Yang Ye; Yangming Shi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09134) · [Code](https://github.com/jiuyixu25/CureWM)
- Tags: CureWM, failure-insensitivity, execution-verified-counterfactuals, world-model-repair, success-failure-discrimination
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unavailable / open-source

**概要（日本語）**

成功デモの行動を重症度別に変え、simulationまたは実機で成否を検証したreplayを既存world modelの追加学習へ使うCureWM。architectureやlossを変えず、失敗への楽観的予測と成功・失敗の識別を、Cosmos PolicyとCtrl-World系列で診断・修復する。

**主な貢献**

検証済み反実仮想replayを、同予算のon-policy失敗と比較。LIBERO-Goalの例で楽観率79.55%→30.17%、AUROC 0.495→0.743だが、成功の誤警報率も31→38%に増加。予測修復を操作性能向上と同一視しない評価を提示。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・書誌: https://arxiv.org/abs/2610.09134 。HTML §3、§4.1/§5、§6を精読: https://arxiv.org/html/2610.09134v1 。実装MITを本文確認: https://github.com/jiuyixu25/CureWM/blob/main/LICENSE 。公式READMEはmodel weights/fine-tuned checkpoints/datasetsを再配布しないと明記: https://github.com/jiuyixu25/CureWM\#what-is-not-here 。制約: 484 LIBERO failures中未見元デモは53、転移不均一、短い予測horizon、1robot/2objectsの小規模実機。RoboCasaのrepair-control tradeoff、best-of-N制御改善に統計的証拠なし。weights unavailableは著者の積極的な非配布表明に基づく。PDFは未取得、URL欄は未検証のため空欄。

### SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

- ID: `WAM-0076`
- Published: 2026-10-05
- Authors: Xiaodong Wang; Tianle Li; Chuanxin Song; Junliang Xie; Zhanmi Zhong; Suiying Wu; Peixi Peng
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06598) · [PDF](https://arxiv.org/pdf/2610.06598) · [Code](https://github.com/Wang-Xiaodong1899/SimForcing) · [Project](https://wang-xiaodong1899.github.io/SimForcing/)
- Tags: action-conditioned-video, sim-to-real, latent-motion-distillation, simulation-conditioning, policy-pretraining
- Model size: Wan2.2-TI2V-5B video backbone + 1B Action DiT
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

シミュレーション教師の隣接潜在状態の差分を実映像の生徒へ蒸留し、行動に応じた運動知識を移すロボット世界モデル。複数ブロックへの条件付けとdropoutで不正確なシミュレーション予測への依存を抑え、推論時は同一の生徒がシミュレーション条件と実領域映像を生成する。Bridge、InternData-A1、下流LIBERO方策学習で検証。

**主な貢献**

外見の差を避ける潜在運動蒸留と、シミュレーション条件のCFGを統合。Bridgeでは身体性事前学習を使わない比較群内でPSNR・SSIM・LPIPS・FVDが最良だがFIDは最良ではない。下流のaction-only学習で平均LIBERO成功率が82.6%から89.2%へ改善。推論時に別の教師モデルは不要だが、運動条件の生成と実映像生成は必要。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。arXiv書誌とv1初稿日2026-10-05を確認、後続版なし。HTML https://arxiv.org/html/2610.06598v1 の§3-5、Table 1/5、Appendix A.3/A.5を確認。研究の主対象は行動条件付き映像予測で、事前学習中に行動を生成するモデルではないためWAM/dynamics。教師の合成データはロボット運動に集中し、物体相互作用と背景を除く。標準設定は初期腕領域のsegmentationを要し、計測条件による遅延の制約も記載。論文からリンクされた公式実装、projectを確認。実装MIT: https://github.com/Wang-Xiaodong1899/SimForcing/blob/main/LICENSE 。READMEは第三者コードの元ライセンスを保持しWanのApache-2.0も同梱と明記。READMEの重み・学習手順とprojectを別に確認したが、学習済みSimForcing重みの公開配布先は未確認でunknown。コードにはsimulation renderingが含まれないと明記。PDFリンクを確認、ダウンロードなし。

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
