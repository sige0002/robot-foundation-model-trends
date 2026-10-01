<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / perception-representation

[← vla](README.md) · [CSV master](../papers.csv)

1 records · Published date 降順（同日 ID 降順）

### UniVLA: Learning to Act Anywhere with Task-centric Latent Actions

- ID: `VLA-0117`
- Published: 2025-05-09 · Updated: 2025-11-03
- Authors: Qingwen Bu; Yanting Yang; Jisong Cai; Shenyuan Gao; Guanghui Ren; Maoqing Yao; Ping Luo; Hongyang Li
- Venue: RSS 2025
- Links: [Paper](https://arxiv.org/abs/2505.06111) · [PDF](https://arxiv.org/pdf/2505.06111) · [Code](https://github.com/OpenDriveLab/UniVLA)
- Tags: UniVLA, latent-actions, human-video, cross-embodiment, task-centric-representation
- Model size: 7B (univla-7b)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

ロボット・人間動画から、身体や視点の違いを越えて共有できるtask-centricな潜在行動を学ぶ。言語とDINO特徴でタスク無関係な変化を抑え、潜在行動を介して汎用VLAを事前学習して各身体へ適応する。

**主な貢献**

言語条件付きの潜在行動表現によって、行動ラベルのない異種動画をVLA学習へ取り込む。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式READMEに公開モデルzoo、訓練コード、7B backboneとRSS 2025。https://github.com/OpenDriveLab/UniVLA\#-model-zoo Code license: Apache-2.0; https://github.com/OpenDriveLab/UniVLA/blob/main/LICENSE.
