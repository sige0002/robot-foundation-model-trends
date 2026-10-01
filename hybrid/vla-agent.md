<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

3 records · Published date 降順（同日 ID 降順）

### Where Memory Belongs: Ledger, an Object Ledger for Memory-Augmented VLAs

- ID: `HYBRID-0101`
- Published: 2026-09-28 · Updated: 2026-09-28
- Authors: Tanguy Dieudonné; Jack B. Jedlicki; Heng Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.34554) · [PDF](https://arxiv.org/pdf/2609.34554)
- Tags: Ledger, object-memory, temporal-memory, LLM-planner, π0.5, RoboMME
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

短期の知覚記憶をVLA内部、長期の物体状態・遮蔽・履歴を外部の読み取り可能なledgerへ分ける。SAM3の追跡とVLMのデモ説明をLLM plannerが参照し、実行ステップの境界で目標を決める単一π0.5方策を評価した。

**主な貢献**

記憶の種類に応じた配置分離と、ステップ境界での外部物体履歴groundingをVLAへ接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。一次HTMLで外部ledger・LLM planner・π0.5の構成を確認。公開実装・重み・ライセンスのリンクは未確認。https://arxiv.org/html/2609.34554v1

### SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation

- ID: `HYBRID-0106`
- Published: 2026-09-26
- Authors: Ziwen Li; Hanlue Zhang; Zhenyang Ren; Tianyu Huang; Runqi Lin; Haoyu Wang; Zhengqing Gao; Yandong Guo; Fakhri Karray; Tongliang Liu; Chris Russell; Mingming Gong
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.32698)
- Tags: failure-guided, online-rl, long-horizon, adapter
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

長期タスクを原子スキルに分解し、実行失敗から弱いスキルを特定する。LLMでシミュレーションの成功判定を生成し、同系統スキルが共有するVLAアダプターをオンラインRLで改善する。

**主な貢献**

追加の専門家デモを集めず、失敗状態の復元・タスク生成・共有アダプター更新を反復する自己改善システム。複数VLAと未知タスクへの転移を評価。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Relevant primary HTML https://arxiv.org/html/2609.32698v1 checked for author-owned project/code links; none verified. Referenced RLinf is upstream training infrastructure, not proof that SEES implementation or weights are released. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation

- ID: `HYBRID-0108`
- Published: 2026-09-22
- Authors: Junjie Xie; Chuxuan He; Angen Ye; Yujia Song; Dapeng Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.25756)
- Tags: medical-robotics, hierarchical, function-constrained, cot
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高水準の視覚言語推論を低水準の制約付き関数実行と組み合わせ、精密医療ロボットの閉ループ操作を行うMedVLA。複数エージェントでスキル志向CoT学習データを生成する。

**主な貢献**

連続行動だけでなく非行動のシステム関数も扱える階層的実行を導入。電極挿入100試行で95%成功を報告するが、臨床的安全性の実証とは扱わない。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.25756v1 and targeted title/code search checked; no official implementation/license, project, or weights verified. Classification as hybrid vla-agent is a curator interpretation of reasoning plus function-level execution. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.
