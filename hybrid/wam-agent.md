<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / wam-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

1 records · Published date 降順（同日 ID 降順）

### Compositional Foundation Models for Hierarchical Planning

- ID: `HYBRID-0110`
- Published: 2023-09-15 · Updated: 2023-09-21
- Authors: Anurag Ajay; Seungwook Han; Yilun Du; Shuang Li; Abhi Gupta; Tommi Jaakkola; Josh Tenenbaum; Leslie Kaelbling; Akash Srivastava; Pulkit Agrawal
- Venue: NeurIPS 2023
- Links: [Paper](https://arxiv.org/abs/2309.08587) · [Code](https://github.com/anuragajay/hip) · [Project](https://hierarchical-planning-foundation-model.github.io/)
- Tags: HiP, foundational, hierarchical-planning, LLM, video-diffusion, inverse-dynamics, iterative-refinement
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

言語モデルのサブゴール、動画拡散モデルの視覚計画、逆動力学の行動を組み合わせるHiP。別々のデータで学習した専門モデル間を反復的な整合性評価でつなぎ、長期の操作計画を作る。

**主な貢献**

言語・映像・行動を単一モデルへ統合せず、下流の実行可能性を上流計画へ返す階層構成を示す。三つのシミュレーション操作環境で未知の物体・色・サブタスクの組合せを評価し、空だったWAM+Agent分類の基礎例を補う。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- 分類の空白hybrid/wam-agentを補うための限定的な基礎論文追加。arXiv v1/v2日付、HTML https://arxiv.org/html/2309.08587v2 の2–3節を確認。NeurIPS公式掲載で会議とDOI 10.52202/075280-0979を確認: https://proceedings.neurips.cc/paper\_files/paper/2023/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html 。公式project経由のinv\_dyn等の予備実装は存在するがroot LICENSEなし。第三者PVDMの条項を全実装へ推定せずopen\_source=unknown、専用重み未確認。PDF未取得。
