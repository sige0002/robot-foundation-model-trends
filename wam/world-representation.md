<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / world-representation

[← wam](README.md) · [CSV master](../papers.csv)

24 records · Published date 降順（同日 ID 降順）

### Adaptive Latent Capacity for World Models

- ID: `WAM-0012`
- Published: 2026-09-26 · Updated: 2026-09-26
- Authors: Idan Achituve; Lior Dikstein; Idit Diamant; Arnon Netzer; Hai Victor Habi
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2609.32921v1) · [PDF](https://arxiv.org/pdf/2609.32921v1)
- Tags: JEPA, Adaptive Capacity, Compression, MixSIGReg, ALeWM
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

環境や目標に応じて必要な潜在容量を減らすALeWMを提案。予測に重要な情報を先頭の座標へ集め、画像目標への計画で固定幅モデルとの効率差を調べる。

**主な貢献**

短い潜在接頭辞から全幅の次状態を予測し、MixSIGRegで有効なガウス接頭辞と残りのゼロ座標の混合分布を正則化する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Object-centric LeJEPA

- ID: `WAM-0031`
- Published: 2026-07-02 · Updated: 2026-07-02
- Authors: Jakob Geusen; Ender Konukoglu
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2607.02404v1) · [PDF](https://arxiv.org/pdf/2607.02404v1)
- Tags: Foundation, Encoder, Object-centric, SAM Masks, LeJEPA
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

画像全体でなく物体単位の特徴を整合させ、少ないデータでLeJEPA表現を改善する研究。学習時には外部の物体マスクを使うため、完全な教師なし物体発見とは区別される。

**主な貢献**

SAMによる物体候補で整合を取り、可変長の物体集合にSIGRegを適用し、同じ画像の別物体を分離する損失を追加する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### When Does LeJEPA Learn a World Model?

- ID: `WAM-0009`
- Published: 2026-05-25 · Updated: 2026-05-25
- Authors: David Klindt; Yann LeCun; Randall Balestriero
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2605.26379v1) · [PDF](https://arxiv.org/pdf/2605.26379v1)
- Tags: Theory, Identifiability, JEPA, Latent State
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

LeJEPAの表現が、非線形な観測の背後にある状態をいつ回復できるかを調べる理論研究。識別可能性の保証は、仮定を満たす潜在分布と遷移に限られる。

**主な貢献**

定常な加法ノイズ遷移のスペクトル構造を用い、ガウス潜在状態の線形・直交識別と近似条件を解析する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

- ID: `WAM-0008`
- Published: 2026-03-15 · Updated: 2026-06-11
- Authors: Lorenzo Mur-Labadia; Matthew Muckley; Amir Bar; Mido Assran; Koustuv Sinha; Mike Rabbat; Yann LeCun; Nicolas Ballas; Adrien Bardes
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2603.14482v3) · [PDF](https://arxiv.org/pdf/2603.14482v3) · [Code](https://github.com/facebookresearch/vjepa2)
- Tags: Foundation, Encoder, Video, Dense Features, V-JEPA
- Model size: 80M–2B encoder family
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

V-JEPAの動画表現を、全体認識に加えて局所的な空間・時間情報が使えるよう改善した研究。密な特徴を世界モデルやロボット知覚へ転用する視覚基盤として位置付けられる。

**主な貢献**

可視・マスク済み双方のトークンに予測損失を与え、中間層への自己教師あり監督と画像・動画を統合するトークナイザを組み合わせる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT with Apache-2.0 components; source: https://github.com/facebookresearch/vjepa2.

### Learning Invariant Visual Representations for Planning with Joint-Embedding Predictive World Models

- ID: `WAM-0018`
- Published: 2026-02-20 · Updated: 2026-02-20
- Authors: Leonardo F. Toso; Davit Shadunts; Yunyang Lu; Nihal Sharma; Donglin Zhan; Nam H. Nguyen; James Anderson
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2602.18639v1) · [PDF](https://arxiv.org/pdf/2602.18639v1)
- Tags: Bisimulation, Invariance, JEPA, DINO-Bisim
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

固定視覚特徴を使うJEPA世界モデルが背景変化に弱い問題を、追加の状態抽象化で改善する研究。簡単なナビゲーション課題で頑健性と潜在次元削減を評価する。

**主な貢献**

DINO-WM型の予測目的にbisimulationエンコーダを加え、似た遷移を持つ状態を近づけて遅い外乱の寄与を抑える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics

- ID: `WAM-0002`
- Published: 2025-11-11 · Updated: 2025-11-14
- Authors: Randall Balestriero; Yann LeCun
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2511.08544v3) · [PDF](https://arxiv.org/pdf/2511.08544v3) · [Code](https://github.com/galilai-group/lejepa)
- Tags: Foundation, Encoder, JEPA, Anti-collapse, SIGReg
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

JEPAの自己教師あり学習を、表現分布の設計から整理する基礎研究。画像の表現学習が中心であり、この手法単体が行動条件付きの世界モデルを構成するわけではない。

**主な貢献**

ランダム射影を使うSIGRegで潜在分布を等方ガウスへ近づけ、予測・整合損失と組み合わせた簡潔な学習目的を導く。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: CC-BY-NC 4.0; source: https://github.com/galilai-group/lejepa.

### Diffusion Transformers with Representation Autoencoders

- ID: `WAM-0023`
- Published: 2025-10-13 · Updated: 2025-10-13
- Authors: Boyang Zheng; Nanye Ma; Shengbang Tong; Saining Xie
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2510.11690v1) · [PDF](https://arxiv.org/pdf/2510.11690v1) · [Code](https://github.com/bytetriper/RAE) · [Project](https://rae-dit.github.io/)
- Tags: Foundation, Encoder, Image Generation, RAE, Diffusion
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

生成モデルの潜在空間を、再構成だけで学ぶVAEから意味的な視覚特徴へ置き換えるRAEを提案。画像生成用の表現設計であり、ロボット行動の世界モデルではない。

**主な貢献**

固定DINO・SigLIP・MAEなどの表現エンコーダに学習済みデコーダを組み合わせ、高次元潜在に対応した拡散Transformerを設計する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/bytetriper/RAE.

### DINOv3

- ID: `WAM-0020`
- Published: 2025-08-13 · Updated: 2025-08-13
- Authors: Oriane Siméoni; Huy V. Vo; Maximilian Seitzer; Federico Baldassarre; Maxime Oquab; Cijo Jose; Vasil Khalidov; Marc Szafraniec; Seungeun Yi; Michaël Ramamonjisoa; Francisco Massa; Daniel Haziza; Luca Wehrstedt; Jianyuan Wang; Timothée Darcet; Théo Moutakanni; Leonel Sentana; Claire Roberts; Andrea Vedaldi; Jamie Tolan; John Brandt; Camille Couprie; Julien Mairal; Hervé Jégou; Patrick Labatut; Piotr Bojanowski
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2508.10104v1) · [PDF](https://arxiv.org/pdf/2508.10104v1) · [Code](https://github.com/facebookresearch/dinov3)
- Tags: Foundation, Encoder, DINOv3, Dense Features, Gram Anchoring
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / available / non-open-source

**概要（日本語）**

長期の自己教師あり学習でも密な局所特徴を保つDINOv3を提案。幾何や物体の細部を使う世界モデルの視覚基盤として重要だが、単体では未来の行動結果を予測しない。

**主な貢献**

Gram anchoringで長時間学習中の密な特徴劣化を抑え、解像度・モデル規模・言語との整合に対する後処理を加える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: DINOv3 custom license; source: https://github.com/facebookresearch/dinov3.

### Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think

- ID: `WAM-0022`
- Published: 2024-10-09 · Updated: 2025-06-18
- Authors: Sihyun Yu; Sangkyung Kwak; Huiwon Jang; Jongheon Jeong; Jonathan Huang; Jinwoo Shin; Saining Xie
- Venue: ICLR 2025
- Links: [Paper](https://arxiv.org/abs/2410.06940v4) · [PDF](https://arxiv.org/pdf/2410.06940v4) · [Code](https://github.com/sihyun-yu/REPA) · [Project](https://sihyun.me/REPA)
- Tags: Foundation, Encoder Alignment, Image Generation, Diffusion, REPA
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

拡散Transformerの学習を、既存の視覚表現を教師として使うことで効率化するREPAを提案。画像生成の研究であり、ロボットの計画性能は直接検証していない。

**主な貢献**

ノイズ付き画像を処理する生成ネットワークの中間特徴を、クリーン画像から得た固定エンコーダの特徴へ整合させる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/sihyun-yu/REPA.

### Revisiting Feature Prediction for Learning Visual Representations from Video

- ID: `WAM-0007`
- Published: 2024-02-15 · Updated: 2024-02-15
- Authors: Adrien Bardes; Quentin Garrido; Jean Ponce; Xinlei Chen; Michael Rabbat; Yann LeCun; Mahmoud Assran; Nicolas Ballas
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2404.08471v1) · [PDF](https://arxiv.org/pdf/2404.08471v1) · [Code](https://github.com/facebookresearch/jepa)
- Tags: Foundation, Encoder, Video, JEPA, V-JEPA
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

観察動画の欠けた部分の特徴を予測し、動きと見た目の両方を捉えるV-JEPAを学習する研究。ロボット行動の介入結果を直接学ぶモデルとは区別が必要。

**主な貢献**

事前学習済み画像エンコーダ、言語、負例、画素再構成を使わず、動画の時空間特徴予測だけで表現を学ぶ。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: CC-BY-NC 4.0; source: https://github.com/facebookresearch/jepa.

### Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities

- ID: `WAM-0030`
- Published: 2023-06-07 · Updated: 2023-12-08
- Authors: Andrii Zadaianchuk; Maximilian Seitzer; Georg Martius
- Venue: NeurIPS 2023
- Links: [Paper](https://arxiv.org/abs/2306.04829v2) · [PDF](https://arxiv.org/pdf/2306.04829v2) · [Code](https://github.com/martius-lab/videosaur) · [Project](https://martius-lab.github.io/videosaur)
- Tags: Foundation, Encoder, Object-centric, Video, VideoSAUR
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

事前学習済み画像特徴から、実世界動画の物体を教師なしで分けて追うVideoSAURを提案。物体中心の動画表現が主題であり、ロボット行動への条件付けはない。

**主な貢献**

特徴再構成に時間的なパッチ類似度の予測損失を加え、動きの手掛かりを物体発見へ与える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/martius-lab/videosaur.

### DINOv2: Learning Robust Visual Features without Supervision

- ID: `WAM-0019`
- Published: 2023-04-14 · Updated: 2024-02-02
- Authors: Maxime Oquab; Timothée Darcet; Théo Moutakanni; Huy Vo; Marc Szafraniec; Vasil Khalidov; Pierre Fernandez; Daniel Haziza; Francisco Massa; Alaaeldin El-Nouby; Mahmoud Assran; Nicolas Ballas; Wojciech Galuba; Russell Howes; Po-Yao Huang; Shang-Wen Li; Ishan Misra; Michael Rabbat; Vasu Sharma; Gabriel Synnaeve; Hu Xu; Hervé Jegou; Julien Mairal; Patrick Labatut; Armand Joulin; Piotr Bojanowski
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2304.07193v2) · [PDF](https://arxiv.org/pdf/2304.07193v2) · [Code](https://github.com/facebookresearch/dinov2)
- Tags: Foundation, Encoder, DINOv2, Dense Features
- Model size: 1B teacher; distilled encoder family
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

多様な画像から汎用的な全体・局所特徴を学ぶ視覚エンコーダ。世界モデルで固定パッチ表現を使う際の基盤だが、DINOv2単体は行動条件付きの遷移モデルではない。

**主な貢献**

自動データ選別と大規模な自己教師あり学習を組み合わせ、大きなViTから小型エンコーダ群へ特徴を蒸留する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: Apache-2.0 for original DINOv2 code and weights; later X-ray variant has separate terms; source: https://github.com/facebookresearch/dinov2.

### Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

- ID: `WAM-0025`
- Published: 2023-03-31 · Updated: 2024-02-01
- Authors: Arjun Majumdar; Karmesh Yadav; Sergio Arnaud; Yecheng Jason Ma; Claire Chen; Sneha Silwal; Aryan Jain; Vincent-Pierre Berges; Pieter Abbeel; Jitendra Malik; Dhruv Batra; Yixin Lin; Oleksandr Maksymets; Aravind Rajeswaran; Franziska Meier
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2303.18240v2) · [PDF](https://arxiv.org/pdf/2303.18240v2) · [Code](https://github.com/facebookresearch/eai-vc) · [Project](https://eai-vc.github.io/)
- Tags: Foundation, Encoder, Benchmark, CortexBench, VC-1
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / available / non-open-source

**概要（日本語）**

身体性AI向けの視覚表現を、移動・操作など17課題のCortexBenchで系統的に比較する研究。VC-1を公開し、事前学習の規模だけでは全課題で最良にならないことを示す。

**主な貢献**

多源の自己中心動画とImageNetでMAE表現を学び、データ構成・モデル規模・下流への適応の効果を同じ評価基盤で分離する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and CC-BY-NC, with separately licensed components license checked at https://github.com/facebookresearch/eai-vc.

### Language-Driven Representation Learning for Robotics

- ID: `WAM-0027`
- Published: 2023-02-24 · Updated: 2023-02-24
- Authors: Siddharth Karamcheti; Suraj Nair; Annie S. Chen; Thomas Kollar; Chelsea Finn; Dorsa Sadigh; Percy Liang
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2302.12766v1) · [PDF](https://arxiv.org/pdf/2302.12766v1) · [Code](https://github.com/siddk/voltron-robotics)
- Tags: Foundation, Encoder, Language-conditioned, Voltron, Robot Manipulation
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

低水準の形状と高水準の意味を両方扱うロボット向け視覚表現Voltronを提案。操作以外の把持や意図推定まで比較する、表現の汎用性を調べる研究。

**主な貢献**

言語条件付きの視覚再構成と、視覚に基づく言語生成のバランスを取り、五種類のロボット学習課題で評価する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/siddk/voltron-robotics.

### Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

- ID: `WAM-0006`
- Published: 2023-01-19 · Updated: 2023-04-13
- Authors: Mahmoud Assran; Quentin Duval; Ishan Misra; Piotr Bojanowski; Pascal Vincent; Michael Rabbat; Yann LeCun; Nicolas Ballas
- Venue: CVPR 2023
- Links: [Paper](https://arxiv.org/abs/2301.08243v3) · [PDF](https://arxiv.org/pdf/2301.08243v3) · [Code](https://github.com/facebookresearch/ijepa)
- Tags: Foundation, Encoder, JEPA, Masked Prediction, I-JEPA
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

画像の一部から別領域の意味的な特徴を推定するI-JEPAを提案。画素の再構成をせずに視覚エンコーダを育てる設計であり、ロボットの行動遷移学習は対象外。

**主な貢献**

広い目標領域と空間的に分散した文脈を使うマスク設計により、画素ではなく潜在特徴の予測へ学習を集中させる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: CC-BY-NC 4.0; source: https://github.com/facebookresearch/ijepa. arXiv comment lists ICCV, but the official repository identifies the original paper as CVPR; venue follows official repository.

### Real-World Robot Learning with Masked Visual Pre-training

- ID: `WAM-0026`
- Published: 2022-10-06 · Updated: 2022-10-06
- Authors: Ilija Radosavovic; Tete Xiao; Stephen James; Pieter Abbeel; Jitendra Malik; Trevor Darrell
- Venue: CoRL 2022
- Links: [Paper](https://arxiv.org/abs/2210.03109v1) · [PDF](https://arxiv.org/pdf/2210.03109v1) · [Code](https://github.com/ir413/mvp) · [Project](https://tetexiao.com/projects/real-mvp)
- Tags: Foundation, Encoder, Human Video, Robot Manipulation, MVP
- Model size: 307M visual encoder
- Open-source: unknown
- Code / weights / license: available / available / unspecified

**概要（日本語）**

自然動画から学んだ固定視覚表現を、多様な実機ロボットの制御へ使うMVPの研究。人手ラベルに頼らない事前学習の有用性を調べるエンコーダ研究で、未来遷移モデルではない。

**主な貢献**

MAEで事前学習した視覚Transformerを固定し、学習可能な制御モジュールへ接続して画像データ量とモデル規模の効果を比較する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official project links ir413/mvp, whose README lists encoder downloads; no implementation license statement found in the checked repository page.

### VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training

- ID: `WAM-0028`
- Published: 2022-09-30 · Updated: 2023-03-07
- Authors: Yecheng Jason Ma; Shagun Sodhani; Dinesh Jayaraman; Osbert Bastani; Vikash Kumar; Amy Zhang
- Venue: ICLR 2023
- Links: [Paper](https://arxiv.org/abs/2210.00030v2) · [PDF](https://arxiv.org/pdf/2210.00030v2) · [Code](https://github.com/facebookresearch/vip) · [Project](https://sites.google.com/view/vip-rl)
- Tags: Foundation, Encoder, Visual Reward, Human Video, VIP
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / available / non-open-source

**概要（日本語）**

人の動画から、画像目標への進み具合を距離として表すVIPを学ぶ研究。固定表現で密な視覚報酬を作る設計であり、行動条件付きの動力学モデルとは異なる。

**主な貢献**

行動ラベルを必要としない目標条件付き価値関数の双対目的を導き、時間的に滑らかな潜在距離を報酬として利用する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and CC-BY-NC 4.0 license checked at https://github.com/facebookresearch/vip.

### R3M: A Universal Visual Representation for Robot Manipulation

- ID: `WAM-0024`
- Published: 2022-03-23 · Updated: 2022-11-18
- Authors: Suraj Nair; Aravind Rajeswaran; Vikash Kumar; Chelsea Finn; Abhinav Gupta
- Venue: CoRL 2022
- Links: [Paper](https://arxiv.org/abs/2203.12601v3) · [PDF](https://arxiv.org/pdf/2203.12601v3) · [Code](https://github.com/facebookresearch/r3m)
- Tags: Foundation, Encoder, Human Video, Robot Manipulation, R3M
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

人の操作動画から、少数のロボット実演でも使えるR3Mの視覚表現を学ぶ研究。固定の知覚モジュールとして方策へ転用する方式で、行動条件付きの未来モデルは学ばない。

**主な貢献**

時間対照学習、動画と言語の整合、L1正則化による疎な表現を同時に学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/facebookresearch/r3m.

### Masked Autoencoders Are Scalable Vision Learners

- ID: `WAM-0021`
- Published: 2021-11-11 · Updated: 2021-12-19
- Authors: Kaiming He; Xinlei Chen; Saining Xie; Yanghao Li; Piotr Dollár; Ross Girshick
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2111.06377v3) · [PDF](https://arxiv.org/pdf/2111.06377v3) · [Code](https://github.com/facebookresearch/mae)
- Tags: Foundation, Encoder, MAE, Masked Reconstruction
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / available / non-open-source

**概要（日本語）**

大部分を隠した画像を再構成するMAEを提案した視覚事前学習の基礎。再構成型の表現を潜在予測型と比較するための土台であり、行動条件付き世界モデルではない。

**主な貢献**

見えるパッチだけを重いエンコーダへ入れ、軽いデコーダで高率にマスクした画素を再構成する非対称構造を採用する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: CC-BY-NC 4.0; source: https://github.com/facebookresearch/mae.

### VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

- ID: `WAM-0003`
- Published: 2021-05-11 · Updated: 2022-01-28
- Authors: Adrien Bardes; Jean Ponce; Yann LeCun
- Venue: ICLR 2022
- Links: [Paper](https://arxiv.org/abs/2105.04906v3) · [PDF](https://arxiv.org/pdf/2105.04906v3) · [Code](https://github.com/facebookresearch/vicreg)
- Tags: Foundation, Encoder, Anti-collapse, VICReg
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

異なる画像ビューを近い特徴へ写しつつ、定数表現への崩壊を防ぐ自己教師ありエンコーダの基礎。世界モデルの表現正則化を比較する土台であり、時間や行動の遷移は学ばない。

**主な貢献**

ビュー間の一致、各次元の分散下限、次元間共分散の抑制を別々の損失として明示する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT; source: https://github.com/facebookresearch/vicreg.

### Barlow Twins: Self-Supervised Learning via Redundancy Reduction

- ID: `WAM-0004`
- Published: 2021-03-04 · Updated: 2021-06-14
- Authors: Jure Zbontar; Li Jing; Ishan Misra; Yann LeCun; Stéphane Deny
- Venue: ICML 2021
- Links: [Paper](https://arxiv.org/abs/2103.03230v3) · [PDF](https://arxiv.org/pdf/2103.03230v3) · [Code](https://github.com/facebookresearch/barlowtwins)
- Tags: Foundation, Encoder, Anti-collapse, Redundancy Reduction
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

同じ画像から作った二つのビューを用い、冗長性の少ない視覚特徴を学習する基礎手法。負例を必要としない表現学習の比較対象だが、行動による未来予測のモデルではない。

**主な貢献**

二つの出力の交差相関行列を単位行列へ近づけ、不変性と次元間の冗長性削減を同じ目的で扱う。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT; source: https://github.com/facebookresearch/barlowtwins.

### Object-Centric Learning with Slot Attention

- ID: `WAM-0029`
- Published: 2020-06-26 · Updated: 2020-10-14
- Authors: Francesco Locatello; Dirk Weissenborn; Thomas Unterthiner; Aravindh Mahendran; Georg Heigold; Jakob Uszkoreit; Alexey Dosovitskiy; Thomas Kipf
- Venue: NeurIPS 2020
- Links: [Paper](https://arxiv.org/abs/2006.15055v2) · [PDF](https://arxiv.org/pdf/2006.15055v2) · [Code](https://github.com/google-research/google-research/tree/master/slot_attention)
- Tags: Foundation, Encoder, Object-centric, Slot Attention
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

画像特徴を複数の物体単位へまとめるSlot Attentionの基礎研究。構造化した世界表現の構成要素だが、単体では時間変化や行動結果をモデル化しない。

**主な貢献**

交換可能なスロットが反復的な競合注意を通じて別々の物体へ結び付く、入力集合に対応した表現モジュールを提案する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official reference implementation and checkpoint links checked. model.py has an Apache-2.0 header: https://github.com/google-research/google-research/blob/master/slot\_attention/model.py.

### Learning Invariant Representations for Reinforcement Learning without Reconstruction

- ID: `WAM-0015`
- Published: 2020-06-18 · Updated: 2021-04-07
- Authors: Amy Zhang; Rowan McAllister; Roberto Calandra; Yarin Gal; Sergey Levine
- Venue: ICLR 2021
- Links: [Paper](https://arxiv.org/abs/2006.10742v2) · [PDF](https://arxiv.org/pdf/2006.10742v2)
- Tags: Bisimulation, Reward-conditioned, Invariance, DBC
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

報酬と将来の挙動が似た状態を近づけ、背景の変動に強い制御表現を学ぶDBCを提案。画素再構成を使わない抽象化だが、どの情報を残すかは対象タスクの報酬に依存する。

**主な貢献**

報酬差と遷移分布の差から定義するbisimulation距離を、エンコーダの潜在距離へ対応付ける。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Bootstrap your own latent: A new approach to self-supervised Learning

- ID: `WAM-0005`
- Published: 2020-06-13 · Updated: 2020-09-10
- Authors: Jean-Bastien Grill; Florian Strub; Florent Altché; Corentin Tallec; Pierre H. Richemond; Elena Buchatskaya; Carl Doersch; Bernardo Avila Pires; Zhaohan Daniel Guo; Mohammad Gheshlaghi Azar; Bilal Piot; Koray Kavukcuoglu; Rémi Munos; Michal Valko
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2006.07733v3) · [PDF](https://arxiv.org/pdf/2006.07733v3) · [Code](https://github.com/google-deepmind/deepmind-research/tree/master/byol)
- Tags: Foundation, Encoder, Anti-collapse, EMA, BYOL
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

負例を使わずに画像特徴を学ぶBYOLを提案した研究。オンライン側と目標側の非対称な更新は、後続の潜在予測学習の安定化を考える基礎になる。行動条件付き世界モデルではない。

**主な貢献**

オンライン予測器に別ビューの目標表現を予測させ、目標ネットワークをオンライン重みの移動平均で更新する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: Apache-2.0 code; weights CC-BY-NC 4.0; source: https://github.com/google-deepmind/deepmind-research/tree/master/byol.
