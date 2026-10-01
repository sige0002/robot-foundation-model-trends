<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / skill

[← agent](README.md) · [CSV master](../papers.csv)

1 records · Published date 降順（同日 ID 降順）

### Voyager: An Open-Ended Embodied Agent with Large Language Models

- ID: `AGENT-0108`
- Published: 2023-05-25 · Updated: 2023-10-19
- Authors: Guanzhi Wang; Yuqi Xie; Yunfan Jiang; Ajay Mandlekar; Chaowei Xiao; Yuke Zhu; Linxi Fan; Anima Anandkumar
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2305.16291) · [PDF](https://arxiv.org/pdf/2305.16291) · [Code](https://github.com/MineDojo/Voyager) · [Project](https://voyager.minedojo.org/)
- Tags: Voyager, skill-library, lifelong-learning, code-generation, Minecraft, not-physical-robot
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

Minecraftで探索とスキル獲得を継続するLLMエージェント。自動カリキュラム、検索可能な実行コードのスキルライブラリ、環境feedback・エラー・自己検証による反復修正を使う。実機ロボット制御の評価ではない。

**主な貢献**

実行可能コードの蓄積・検索と自動探索を組み合わせ、再利用可能スキルを継続獲得する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公開実装MIT。仮想embodied agentであり、物理ロボットへの直接評価ではない。 Code license: MIT; https://github.com/MineDojo/Voyager/blob/main/LICENSE.
