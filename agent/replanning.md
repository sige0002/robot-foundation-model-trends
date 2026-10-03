<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / replanning

[← agent](README.md) · [CSV master](../papers.csv)

3 records · Published date 降順（同日 ID 降順）

### RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement

- ID: `AGENT-0119`
- Published: 2026-09-23
- Authors: Kailin Wang; Haoxiang Jie; Yaoyuan Yan; Zhiyou Heng; Zhaosong Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.27612)
- Tags: evidence-gated-runtime, role-isolated-context, versioned-memory, bounded-recovery, configuration-revision, supporting-system
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

計画提案、skill実行、独立検証、制限付き復旧を分け、証拠と版に結びつく状態更新だけを進捗として受理するロボットAgent runtime。履歴から構成変更候補を作り、固定回帰検査と版管理で採用する手順を定義する。

**主な貢献**

倉庫巡回・画像観察・報告・帰還の実機記録と、出発/経路進捗/帰還が必要な周回例で完了判定を具体化。RSIは構成改訂プロトコルで、統制比較の改善量や再帰的能力向上、オンライン重み更新の実証ではない。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.27612v1 の1節、6.2節の実機例、6.5–6.8節、7–8節を確認。HROSは先行runtimeで本稿のharness契約の基盤。6.8はfault injection・ablation・RSI評価手順を規定するが、その比較結果は記載されていない。VLA/world model/TAMPを接続できる契約と実機navigation/inspection実証を区別する。専用code・weight・実装licenseは本文リンク/題名検索で未確認。PDF未取得。

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
