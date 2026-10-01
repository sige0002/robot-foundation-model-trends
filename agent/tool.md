<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / tool

[← agent](README.md) · [CSV master](../papers.csv)

1 records · Published date 降順（同日 ID 降順）

### ReAct: Synergizing Reasoning and Acting in Language Models

- ID: `AGENT-0107`
- Published: 2022-10-06 · Updated: 2023-03-10
- Authors: Shunyu Yao; Jeffrey Zhao; Dian Yu; Nan Du; Izhak Shafran; Karthik Narasimhan; Yuan Cao
- Venue: ICLR 2023
- Links: [Paper](https://arxiv.org/abs/2210.03629) · [PDF](https://arxiv.org/pdf/2210.03629) · [Code](https://github.com/ysymyth/ReAct) · [Project](https://react-lm.github.io/)
- Tags: ReAct, reasoning-action-loop, tool-use, environment-feedback, transferable-agent, not-physical-robot
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

推論記述と外部ツール・環境への行動を交互に生成し、取得した情報で計画を修正するLLMエージェント。QA、事実検証、ALFWorld、WebShopで評価され、実機ロボット制御の実証ではない。

**主な貢献**

推論と行動の反復を一つのprompt形式へ統合する、robot-agent設計にも転用される汎用エージェント基盤。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。実機ロボット論文ではなく、要求されたAgent基盤の先行研究として収録。 Code license: MIT; https://github.com/ysymyth/ReAct/blob/master/LICENSE.
