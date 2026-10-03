<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / tool

[← agent](README.md) · [CSV master](../papers.csv)

2 records · Published date 降順（同日 ID 降順）

### CognitiveReality: Robot-Agnostic Semantic Gaussian Mapping with an LLM Agent for Immersive Collaborative VR Teleoperation

- ID: `AGENT-0118`
- Published: 2026-09-25
- Authors: Timofei Kozlov; Dmitrii Maliukov; Andrey Marchenko; Dmitrii Plotnikov; Miguel Altamirano Cabrera; Dzmitry Tsetserukou
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.31418)
- Tags: semantic-Gaussian-TSDF, typed-tools, VR-teleoperation, persistent-object-ID, operator-confirmation, supporting-system
- Model size: Qwen3-VL-8B router; system total unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

RGB-Dから作るオンラインGaussian-TSDF地図を、VR操作者と型付きtoolを使う言語Agentで共有する。物体の永続ID・意味・再構成品質を記録し、指差しや発話をscene参照へ接地してロボット操作を確認付きで実行する。

**主な貢献**

二四足実機でnavigation26/30件と再観測20/20件を完了し、tool選択・引数・地図参照を分けて評価。地図ラベルへの高い同意を独立認識精度と扱わず、提案後のmap更新に対する確認時再検証は残課題。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.31418v1 のIII-A/C/D節、IV-D/E節、V節を確認。制御Agentは外部GPU、移動はNav2等既存backendで操作者確認を要求。sandboxのunsafe proposalなしは実機安全保証ではない。主分類agent/tool、地図は支援的表現で学習済み予測世界モデルとの統合を推定しない。専用実装・重み・実装ライセンスは本文リンク/題名検索で未確認。PDF未取得。

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
