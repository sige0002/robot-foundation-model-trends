<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / action-coupling

[← wam](README.md) · [CSV master](../papers.csv)

10 records · Published date 降順（同日 ID 降順）

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

### One from Infinity: Actualizing Futures from Pretrained World Models into Robot Actions

- ID: `WAM-0060`
- Published: 2026-09-29 · Updated: 2026-10-01
- Authors: Bang Du; Yichen Xie; Shuqi Zhao; Yuxin Chen; Menglin Wu; Masayoshi Tomizuka
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.36413) · [Code](https://github.com/7mare/RoboActualizer) · [Project](https://zhao-sq.github.io/RoboActualizer/)
- Tags: RoboActualizer, frozen-V-JEPA, latent-action-MoT, flow-matching, cached-features
- Model size: 60M trainable actualizer; frozen V-JEPA 2.1 300M encoder
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

凍結V-JEPA 2.1の動画表現を利用し、二つの軽量DiTが指示に沿った将来潜在と行動チャンクを共同予測するRoboActualizer。キャッシュ済み特徴でヘッドを学習し、展開時はエンコーダを一回だけ実行する。

**主な貢献**

60M学習パラメータの方策でLIBERO・LIBERO-Plus、選択RoboTwin課題と二実機の五課題を評価。表現事前学習の費用は別で、論文の比較は全RoboTwin課題を含まず、単なる画像表現と動画予測表現のアブレーションも行う。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1/v2の日付を区別。HTML https://arxiv.org/html/2609.36413v2 の3節、4.1–4.2節、4.5.2–4.5.3節と5節を確認。本文には採択後のcode release予定が残るが、公式project経由の現在のrepoにはsrcと学習/評価実装がある。root MITを確認: https://github.com/7mare/RoboActualizer/blob/main/LICENSE 。第三者コードは元条項。専用重みを https://huggingface.co/db12312607/RoboActualizer のmodel card、MIT表示、libero\_dits/step\_173580.ptのファイル一覧で独立確認。公開repoの拡張評価設定を論文の評価範囲に混ぜない。PDF未取得。

### Efficient World Action Model Inference with Adaptive Intermediate States

- ID: `WAM-0063`
- Published: 2026-09-28
- Authors: Zhinnan Liu; Haozhi Han; Ruge Zhang; Teng Ma; Tao Ma; Zheng Liu; Yifeng Chen; Yunquan Zhang; Ting Cao; Yunxin Liu; Kun Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.34608)
- Tags: WAMachine, supporting-inference, state-reuse, trajectory-remapping, observation-rebinding, residual-rescaling
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

再計画、拡散ステップ、Transformer層の三段階でWAM推論状態を保持・補正する学習不要のWAMachine。予測観測で先行計算し、実観測との整合性検査が失敗すると再初期化や全層計算へ戻る。

**主な貢献**

三WAMの同一checkpointでシミュレーションを比較し、観測から行動準備までの遅延を1.47–3.05倍高速化。GPU計算時間と制御ループに見える遅延を別々に測り、大標本での成功率低下も併記する。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2609.34608v1 の3節の状態再利用、4.1–4.3節の設定/表、5節/倫理声明の該当箇所を確認。時間比較は各モデル固定200episode、成功率はCosmos Policy/Fast-WAM-IDM各6000 LIBERO、Motus 2000 RoboTwin試行。A100 80GB使用、MotusのWAMachineは追加rendering GPUを使う。全てsimulationで実機安全検証は別。新規方策ではなくWAM推論の支援研究。専用実装・重み・実装ライセンスは本文リンクと題名検索で未確認。PDF未取得。

### InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data

- ID: `WAM-0062`
- Published: 2026-09-25
- Authors: Xingyu Miao; Zizun Li; Baole Fang; Kaiwen Song; Tenghui Wang; et al.
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.31394) · [Project](https://internrobotics.github.io/InternW0-Delta/)
- Tags: world-action-MoT, Causal-Imprint, 4D-distillation, sparse-memory, heterogeneous-pretraining
- Model size: Wan2.2-TI2V-5B video backbone; total parameters unknown
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

動画専門家と行動専門家を有向注意で結び、凍結VLMの場面意味と4D教師の幾何・運動情報を学習へ取り込むWAM。Causal Imprintは将来映像を訓練時の教師として使い、推論時の未来映像ロールアウトを省く。

**主な貢献**

ロボット・UMI・人の一人称データを共通状態行動形式へ揃えた20K時間超の事前学習を報告。複数シミュレーションと四実機で評価し、事前学習あり/なしの実機比較は二課題各20試行で行う。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。著者48名のうち先頭5名＋et al.を明示。HTML https://arxiv.org/html/2609.31394v1 の3.1/3.3–3.6節、7.3節、8節の限界と公式projectを確認。Source codeとModel checkpointsはForthcomingと明記され、確認時unavailable、実装ライセンスunknown。将来のopen source予定をopen\_source=trueやデータの現公開証拠と扱わない。Agent支援は限定的な補正実験であり汎用Agent統合の保証ではない。PDF未取得。

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

### An Action Is Worth One Patch: Unified World-Action Modeling with PatchWAM

- ID: `WAM-0064`
- Published: 2026-09-22
- Authors: Tianheng Wang; Zhou Xie; Heng Jia; Jianhua Xu; Tong Zhang; Kaicheng Yu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.25961)
- Tags: PatchWAM, Action-as-Patch, shared-transformer, joint-denoising, parameter-free-codec
- Model size: FLUX.2 klein 4B Base backbone; total parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動成分を繰返し・ゼロ埋めで画像パッチと同次元へ変換する固定codecを用い、未来画像と行動を一つのTransformerで共同denoiseするPatchWAM。専用行動専門家や学習可能な行動codecを追加しない。

**主な貢献**

データと最適化を揃えた間引きRoboTwin学習で二専門家構成との比較を実施。追加データを使う別条件でRoboTwin平均96.12%、LIBERO-Plus91.8%を報告し、条件差・独立seed不足・実機未評価を明示する。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2609.25961v1 の3.1–3.2節、4.2節と6–7節を確認。20step推論の時間は二専門家対照の1.87倍、評価用10stepは未計時。未来予測が行動選択を改善する因果機序や全ての専用head不要は未実証。主結果のデータ増強とmatched comparisonを混ぜない。専用実装・重み・実装ライセンスは本文リンク/題名検索で未確認、基礎FLUXやImageWAMの提供状態を転用しない。PDF未取得。

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
