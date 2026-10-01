<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / replanning

[← agent](README.md) · [CSV master](../papers.csv)

2 records · Published date 降順（同日 ID 降順）

### SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

- ID: `AGENT-0112`
- Published: 2023-07-12 · Updated: 2023-09-27
- Authors: Krishan Rana; Jesse Haviland; Sourav Garg; Jad Abou-Chakra; Ian Reid; Niko Suenderhauf
- Venue: CoRL 2023
- Links: [Paper](https://arxiv.org/abs/2307.06135) · [PDF](https://arxiv.org/pdf/2307.06135) · [Project](https://sayplan.github.io/)
- Tags: SayPlan, 3D-scene-graph, semantic-search, classical-path-planning, simulator-feedback
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

大規模な階層3D scene graphを意味検索で絞り、LLMが長期ロボットタスクを計画する。古典的経路計画でLLMの負担を減らし、scene graph simulatorのfeedbackから不可能な動作を修正して反復再計画する。

**主な貢献**

階層scene graphの検索・古典計画・実行可能性feedbackを組み合わせ、複数階・部屋の環境へLLM計画を拡張。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。arXivコメントと公式projectがCoRL 2023 oralと明記。公開実装とライセンスは未確認。

### Inner Monologue: Embodied Reasoning through Planning with Language Models

- ID: `AGENT-0103`
- Published: 2022-07-12 · Updated: 2022-07-12
- Authors: Wenlong Huang; Fei Xia; Ted Xiao; Harris Chan; Jacky Liang; Pete Florence; Andy Zeng; Jonathan Tompson; Igor Mordatch; Yevgen Chebotar; Pierre Sermanet; Noah Brown; Tomas Jackson; Linda Luu; Sergey Levine; Karol Hausman; Brian Ichter
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2207.05608) · [PDF](https://arxiv.org/pdf/2207.05608) · [Project](https://innermonologue.github.io/)
- Tags: Inner-Monologue, closed-loop-planning, execution-feedback, scene-description, human-feedback
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

成功判定・シーン記述・人間とのやり取りを言語feedbackとしてLLMへ戻し、ロボットの高レベル計画を更新する。追加のLLM訓練なしに、卓上配置と実世界の長期移動操作で閉ループfeedbackの効果を検証した。

**主な貢献**

実行結果と環境変化を自然言語にまとめ、LLMの次のスキル選択・再計画へ連続的に反映。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式論文・projectを確認。公開実装・重み・実装ライセンスはunknown。
