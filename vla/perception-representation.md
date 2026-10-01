<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / perception-representation

[← vla](README.md) · [CSV master](../papers.csv)

2 records · Published date 降順（同日 ID 降順）

### GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments

- ID: `VLA-0131`
- Published: 2026-09-18
- Authors: Yichen Liu; Puzhen Yuan; Xiang Zhu; Yanjiang Guo; Jianyu Chen
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.21948) · [Code](https://github.com/PuzhenYuan/GALA) · [Project](https://puzhenyuan.github.io/GALA-website/)
- Tags: latent-action, geometry, cross-embodiment, human-video
- Model size: 5B (RoboCasa-GR1 inference checkpoint)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

RGBの場面変化と3D末端形状の動きを同時に符号化し、機体をまたぐ細かな潜在行動を学習するGALA。人の手、器用なロボット手、平行グリッパーのデータをVLA事前学習へ接続する。

**主な貢献**

統一末端動作表現UEMRと視覚・幾何の二種類の潜在行動を導入。行動ラベルのない人の一人称動画も利用し、機体別ネイティブ行動ヘッドで操作を学習。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Official project directly links official implementation and checkpoint. https://github.com/PuzhenYuan/GALA/blob/main/LICENSE verified Apache 2.0. https://huggingface.co/ypz21/GALA\_robocasa\_gr1 and /tree/main expose a 5B F32 model and four safetensors shards (19.3GB total); only listing read, no model downloaded. README still describes repository as private, conflicting with public file listing; public listing supports available status but access not download-tested. Weight license is unspecified in checked model card and is not inferred from code Apache license. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

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
