<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-wam

[← hybrid](README.md) · [CSV master](../papers.csv)

7 records · Published date 降順（同日 ID 降順）

### V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents

- ID: `WAM-0034`
- Published: 2026-09-29 · Updated: 2026-09-29
- Authors: Yang Zhang; Jiangyuan Zhao; Chenyou Fan; Jiayu Hu; Xiu Yuan; Chenjia Bai; Xiu Li
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2609.37250v1) · [PDF](https://arxiv.org/pdf/2609.37250v1) · [Code](https://github.com/breez3young/VJEPA-Policy)
- Tags: Language-conditioned, Latent Prediction, Flow Matching, Robot Policy, V-JEPA Policy
- Model size: 0.9B total; 0.6B trainable
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

固定V-JEPA 2.1の潜在空間で、指示に応じた未来予測とロボット行動生成を結び付ける研究。動画の生成器全体を継承せず、予測表現を方策の基盤として使う。

**主な貢献**

将来潜在を予測するネットワークの文脈キー・値をflow-matching行動expertへ渡し、両者を下流の一段階で共同学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/breez3young/VJEPA-Policy. Repository contains source only; no policy checkpoint distribution independently verified. Upstream encoders and assets have their own terms.

### SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models

- ID: `HYBRID-0105`
- Published: 2026-09-27
- Authors: Tianfu Li; Haoxuan Xu; Wenbo Chen; Haitian Li; Changchuan Yang; Xinhu Zheng; Jun Ma; Yuan Liu; Lujia Wang; Haoang Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.33575) · [Project](https://haoxuanxu1024.github.io/SLIP_VLA/)
- Tags: latent-imagination, single-step, future-prediction, manipulation
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

1回のノイズ除去で将来の潜在表現を生成し、幾何・意味・行動の整合性を学習してVLAの操作方策に供給する。シミュレーションと実機で将来予測の有効性を評価した。

**主な貢献**

多段の動画生成を用いず、知覚教師・順動力学・逆動力学で制御に有用な潜在未来を整形。未来想像は12msだが、公式ページの全体推論時間は181ms。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv submission history: v1 only. Official project https://haoxuanxu1024.github.io/SLIP\_VLA/ links https://github.com/HaoxuanXU1024/SLIP\_VLA; repository contains website assets and explicitly says code will be released soon, so it is not counted as a released research implementation. Implementation license and weights unverified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Towards VLA-Dreamer: Refining VLA Behavior Using World Models

- ID: `HYBRID-0107`
- Published: 2026-09-25
- Authors: Parsa Mastouri Kashani; Jan-Gerrit Habekost; Stefan Wermter
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.31313)
- Tags: concept-paper, latent-world-model, planning, sample-efficiency
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VLAの視覚埋め込み空間で行動条件付き世界モデルを学習し、データ効率改善や短期計画に利用する構想論文。視覚埋め込みが未来予測と制御に十分かを検証する研究計画を述べる。

**主な貢献**

画素再構成ではなくVLAの視覚埋め込みを予測対象にするVLA-Dreamer構想。提案・仮説であり、実証済み性能改善として扱わない。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.31313v1 explicitly describes a concept/proposed architecture, not a completed empirical system. No official project, implementation/license, or weights verified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution

- ID: `HYBRID-0109`
- Published: 2026-09-23
- Authors: Shuai Zeng; Yuxuan Liang; Hangmiao Hu; Fobao Zhou; Zixiang Wang; Wenxi Hong; Hang Zhao
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.27468)
- Tags: residual-control, consequence-model, governor, frozen-vla
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結VLAの行動チャンクを軽量な残差で補正し、予測される結果が不利な補正を抑制するCereVLA。再帰状態空間モデルと履歴分類器で短期・区間単位の結果を評価する。

**主な貢献**

残差生成を参照行動との一致だけで評価せず、予測結果に基づく実行ガバナーを導入。SO-101で成功率57.5%から90%への改善を報告。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.27468v1 checked for project/code/release evidence; no author-owned release verified. Hybrid vla-wam classification reflects predictive consequence modeling coupled to VLA control, not a separately released general world model. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies

- ID: `HYBRID-0103`
- Published: 2026-09-21 · Updated: 2026-09-22
- Authors: Trung Dao; Sankalp Yamsani; Jaden Park; Joohyung Kim; Yong Jae Lee
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.24682) · [Code](https://github.com/trungdt880/THAW-VLA) · [Project](https://thaw-vla.trung-dt.com/)
- Tags: THAW-VLA, representation-distillation, compact-policy, world-model-teacher, flow-matching
- Model size: 0.8B student; 4B variants
- Open-source: unknown
- Code / weights / license: available / available / unknown

**概要（日本語）**

凍結世界モデルの内部特徴を事前計算し、小型VLAの画像特徴へ蒸留する。推論時には教師と投影器を使わず、行動方策の構造を維持したまま表現学習を補助する。

**主な貢献**

行動模倣損失に特徴整合損失を加え、教師の行動表現への依存を避ける。LIBERO・RoboCasaと実機で同一学生の非蒸留対照を検証する。

**確認記録**

- Checked: 2026-10-01 · Review: needs-review
- 初稿2026-09-21、v2改訂2026-09-22をarXivで確認。HTML本文III節と評価条件を確認。公式projectがリンクする実装とHF final\_model.ptを確認: https://huggingface.co/termanteus/THAW-VLA-Qwen3.5-0.8B-LIBERO/tree/main 。重みのモデルカード・ライセンスは未確認。実装LICENSEはMIT表記に加えコミット保持等の条項を含むためOSI承認MITと同一と断定せずopen\_source/license\_statusをunknown: https://github.com/trungdt880/THAW-VLA/blob/main/LICENSE 。

### Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model

- ID: `HYBRID-0102`
- Published: 2026-09-11 · Updated: 2026-09-11
- Authors: Hoeun Lee; Jaeik Kim; Jusang Oh; Jinhyeok Kim; Geon Choi; Hyeonggeun Kim; Jaeyoung Do
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.13053) · [PDF](https://arxiv.org/pdf/2609.13053) · [Code](https://github.com/AIDASLab/Dynin-Robotics) · [Project](https://dynin.ai/robotics/)
- Tags: Dynin-Robotics, masked-diffusion, world-action-model, goal-state-prediction, candidate-reranking
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

言語・観測・目標・行動を共通の離散トークン列として学ぶomnimodal masked-diffusionモデル。条件と予測領域を変え、方策、次状態、終端目標、指示再構成を共同学習し、目標生成や未来予測を動作生成・候補選択へ使う。

**主な貢献**

共有trajectory modelの複数条件付き予測を、目標誘導・行動と次状態の共同denoising・候補再ランキングに再構成。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式repoはREADME/assetsのみ、公式model cardもCode and model will be released soon。MIT badgeはあるが実装・重み未公開なのでopen\_sourceはunknown。https://huggingface.co/snu-aidas/Dynin-Robotics

### LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

- ID: `WAM-0035`
- Published: 2026-06-14 · Updated: 2026-06-14
- Authors: Jialei Chen; Kai Wang; Kang Chen; Shuaihang Chen; Feng Gao; Wenhao Tang; Zhiyuan Li; Weilin Liu; Zhuyu Yao; Boxun Li; Yuanbo Xu; Chao Yu
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2606.15768v1) · [PDF](https://arxiv.org/pdf/2606.15768v1) · [Code](https://github.com/RLinf/LaWAM)
- Tags: Language-conditioned, Latent Subgoal, Latent Action, Robot Policy, LaWAM
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

未来の画像を生成する代わりに、潜在的な視覚サブゴールを方策へ渡すLaWAMを提案。世界モデルによる先読みを、低遅延の言語条件付きロボット操作へ取り込む。

**主な貢献**

視覚基盤の潜在空間で行動表現を学び、その順方向デコーダを未来特徴の予測器へ転用して行動生成に条件付ける。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT implementation; DINOv3 component has separate terms; source: https://github.com/RLinf/LaWAM.
