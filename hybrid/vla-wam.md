<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-wam

[← hybrid](README.md) · [CSV master](../papers.csv)

3 records · Published date 降順（同日 ID 降順）

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
