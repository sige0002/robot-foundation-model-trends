<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-wam-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

1 records · Published date 降順（同日 ID 降順）

### RoboCoach: World Models as Active Coaches for Compositional Robot Skills

- ID: `HYBRID-0104`
- Published: 2026-09-30
- Authors: Jiajun Liu; Yifan Chen; Yichao Liu; Jiayi Zhang; Ruoqu Chen; Shaoxuan Xie; Guocai Yao; Mengdi Xu; Sen Cui; Changshui Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39685) · [Code](https://github.com/RoboCoach-AI/CoachWorld) · [Project](https://robocoach-ai.github.io/)
- Tags: RoboCoach, CoachWorld, skill-routing, progress-judge, targeted-demonstrations, LoRA
- Model size: CoachWorld backbone: Wan2.2-TI2V-5B; full system total unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

VLAスキル専門家を行動条件付き世界モデル内で実行し、進捗判定器が最初の未完了サブタスクを特定する。その失敗を集約して、追加デモと更新対象の専門家を選ぶ。

**主な貢献**

Route–Imagine–Diagnose–Improveループで、計画・世界モデルの想像・スキル別LoRA更新を接続。長期タスク全体の追加デモではなく局所的な監督に予算を配分する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿とHTML本文3.1–3.4節の共有VLA backbone、router、judge、CoachWorldを確認。公式実装公開はCoachWorld部分であり全router/進捗判定/専門家更新パイプラインの公開とは区別。実装root MITを確認: https://github.com/RoboCoach-AI/CoachWorld/blob/main/LICENSE 。Wan2.2等の第三者コードは別条項。HF dit\_model.safetensorsを確認: https://huggingface.co/JEdward/CoachWorld/tree/main 。重み利用ライセンスは未確認。
