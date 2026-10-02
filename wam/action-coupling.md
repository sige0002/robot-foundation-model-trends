<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / action-coupling

[← wam](README.md) · [CSV master](../papers.csv)

6 records · Published date 降順（同日 ID 降順）

### Completion Aware Guidance for World Action Models

- ID: `WAM-0058`
- Published: 2026-10-01
- Authors: Seungyeon Kim; Junhoo Lee; Baekseung Kim; Minkyu Kim; Nojun Kwak
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01559)
- Tags: completion-guidance, training-free, cross-attention, short-horizon, sampling
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

短い映像・行動チャンクが把持解除などの完了遷移を先送りする失敗を分析し、関連する指示トークンの条件づけをサンプリング中に強めるCompletion Aware Guidanceを提案する。

**主な貢献**

クロスアテンションから得たトークン関連度でキー・値へ有界な介入を行う追加学習不要の方法。Fast-WAMの非飽和9課題で平均成功64.4%から70.0%、DreamZeroの3シミュレーション課題で69%から75%を報告する。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者・arXiv DOI、HTML https://arxiv.org/html/2610.01559v1 の3–4節と限界を確認。RoboTwinは成功率90%未満の選択9課題であり全ベンチマーク平均ではない。ワークショップ名は本文記載のみなのでvenue=arXiv。公式実装・重み・実装ライセンスは本文リンクとタイトル検索で未確認。論文CC BYはコード公開の証拠ではない。PDF未取得。

### CtrlWAM: Controllable World Action Models with Aligned Intent and Foresight

- ID: `WAM-0057`
- Published: 2026-10-01
- Authors: Chensheng Peng; Wenhao Ding; Ran Tian; Zewei Zhou; Jef Packer; Maximilian Igl; Peter Karkus; Yan Wang; Masayoshi Tomizuka; Boris Ivanovic; Marco Pavone; Yuxiao Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.00859) · [Project](https://ctrl-wam.github.io/)
- Tags: joint-video-action, aligned-noising, counterfactual-control, multi-agent, driving, bimanual
- Model size: Cosmos 3-Nano 16B backbone
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

摂動を加えた行動をシミュレータで実行し、その結果の映像と組にして世界行動モデルを学習する。映像と行動のノイズ時刻をずらし、周辺エージェントの将来を予測または指定できる入力へ拡張する。

**主な貢献**

行動意図と予測映像の物理的な対応を学習中から揃える方法を提示。運転の軌跡整合性とRoboTwin由来1000エピソードの映像品質・制御可能性を評価し、生成映像の改善を実機閉ループ成功率と混同しない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.00859v1 の3節・4.1–4.4節・付録Dを確認。公式projectのCode (under review)は https://github.com/anonymous/ctrlwam にリンクするが確認時404。実装公開・専用重み・実装ライセンスは未確認なのでunknown、code\_urlは空欄。multi-agentは場面内の行動ストリームでありLLM Agentとの結合と推測しない。PDF未取得。

### I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?

- ID: `WAM-0011`
- Published: 2026-09-25 · Updated: 2026-09-25
- Authors: Yuhang Liu; Zhuo Huang; Javen Qinfeng Shi
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2609.31161v1) · [PDF](https://arxiv.org/pdf/2609.31161v1)
- Tags: Theory, Causal Representation, Action Conditioning, A-JEPA
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動条件を加えたJEPAが、単に未来を当てるだけでなく潜在的な因果状態を回復できる条件を調べる研究。介入の多様さが因果機構の学習にどう効くかを検証する。

**主な貢献**

遷移尤度と状態情報を保つエントロピー目的から識別条件を導き、行動で変調するガウス加法ノイズモデルとしてA-JEPAを具体化する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### On the Identifiability of Controlled World Models

- ID: `WAM-0010`
- Published: 2026-07-24 · Updated: 2026-07-27
- Authors: Xiangteng Zhang; Yang Guan; Bo Zhang; Hongyang Li; Ya-Qin Zhang; Shengbo Eben Li
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2607.22430v2) · [PDF](https://arxiv.org/pdf/2607.22430v2)
- Tags: Theory, Identifiability, Action Conditioning, Counterfactual Prediction
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

観測から状態を識別する問題と、候補行動の効果を識別する問題を分けた理論研究。行動条件付きJEPAが反実仮想の予測に使えるためのデータ条件を明らかにする。

**主な貢献**

表現側のスペクトル分離と、状態を条件にした行動の非退化な変動を組み合わせた識別条件および誤差限界を示す。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- ID: `WAM-0033`
- Published: 2025-06-11 · Updated: 2025-06-11
- Authors: Mido Assran; Adrien Bardes; David Fan; Quentin Garrido; Russell Howes; Mojtaba Komeili; Matthew Muckley; Ammar Rizvi; Claire Roberts; Koustuv Sinha; Artem Zholus; Sergio Arnaud; Abha Gejji; Ada Martin; Francois Robert Hogan; Daniel Dugas; Piotr Bojanowski; Vasil Khalidov; Patrick Labatut; Francisco Massa; Marc Szafraniec; Kapil Krishnakumar; Yong Li; Xiaodong Ma; Sarath Chandar; Franziska Meier; Yann LeCun; Michael Rabbat; Nicolas Ballas
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2506.09985v1) · [PDF](https://arxiv.org/pdf/2506.09985v1) · [Code](https://github.com/facebookresearch/vjepa2) · [Project](https://ai.meta.com/research/vjepa/)
- Tags: JEPA, Video Pretraining, Action Conditioning, Robot Planning, V-JEPA 2
- Model size: 300M–1B video encoder family
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

大規模な観察動画から学んだV-JEPA 2を、少量のロボット軌跡で行動条件付き世界モデルへ拡張する研究。画像目標の計画により、新しい実機環境での操作を検証する。

**主な貢献**

行動なしの動画JEPA事前学習の後にV-JEPA 2-ACを学習し、潜在空間で候補行動を予測・比較する二段階構成を取る。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT with Apache-2.0 components; source: https://github.com/facebookresearch/vjepa2. arXiv splits Mojtaba Komeili into two author records; corrected to the single name verified in the official V-JEPA 2 repository README.

### Learning Action-based Representations Using Invariance

- ID: `WAM-0017`
- Published: 2024-03-25 · Updated: 2024-06-24
- Authors: Max Rudolph; Caleb Chuck; Kevin Black; Misha Lvovsky; Scott Niekum; Amy Zhang
- Venue: Reinforcement Learning Conference 2024
- Links: [Paper](https://arxiv.org/abs/2403.16369v3) · [PDF](https://arxiv.org/pdf/2403.16369v3)
- Tags: Action Bisimulation, Reward-free, Controllability, Long Horizon
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

報酬を使わず、複数段先の行動に関係する状態差を表現へ残す研究。直前だけでなく、遠くの壁など後で制御へ影響する情報を捉えることを狙う。

**主な貢献**

単一ステップの逆動力学に再帰的な不変性制約を加えたaction-bisimulationにより、長期の制御可能性を距離として学ぶ。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.
