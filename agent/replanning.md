<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / replanning

[← agent](README.md) · [CSV master](../papers.csv)

5 records · Published date 降順（同日 ID 降順）

### CIRRA: Dual-Level Continual Instruction Reconciliation with Ongoing Execution for Embodied Robot Agents in Interactive Household Tasks

- ID: `AGENT-0133`
- Published: 2026-10-05
- Authors: Ci Zhang; Enfu Nan; Arman Akbari; Lin Zhao; Li Wang; Chen Wang; Weiwei Chen; Yanzhi Wang; Geng Yuan
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08862)
- Tags: CIRRA, continual-instruction-reconciliation, execution-aligned-planning, interruptibility, CHIRP, humanoid, real-robot
- Model size: Qwen3-8B compiler/judge; 4B and 32B ablations
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

進行中の家事へ新しい依頼が来た時、元のsubtask順序を維持したまま曖昧な指示をskill・場所へgroundingする。場所が一致する区間だけへ新subtaskを挿入し、LLMが依存関係と衝突を判定して融合・待機・中断・確認を選ぶ。

**主な貢献**

rule制約で既存の実行backboneと安全な中断境界を守り、LLMの自由な全体再計画を局所的なinstruction reconciliationへ限定。CHIRP benchmarkで言語compilerの誤りとschedule統合を分離。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-05、primary arXivはv1のみ。本文§3–5を選択読解: https://arxiv.org/html/2610.08862v1 。CHIRP text120episodeで8B DA74.2%; oracle仕様で100%。実機G1は2table/8 ImageWAM-fine-tuned skills、5combination×25trialでDA95.6%、中断compliance100%; grasp失敗trialは除外。改善は高level指示統合が主貢献なのでAgent/replanning、低level既存ImageWAM使用をHybrid化の根拠にしない。限定環境とcompiler/judge誤りが限界。公式著者homepage https://brankozz.github.io/ のGitHub/HF欄はplaceholderで実装・重みURLの証拠にならず、code/license/weightsはunknown。PDF未取得。

### CAPEX: Efficiently Distilling Foundation Model Behavior into Deployable Robot Policies through Experience-Adaptive Reasoning

- ID: `AGENT-0126`
- Published: 2026-09-26
- Authors: Shivam Aarya; Zhang Xi-Jia; Chengyue Huang; Junhyun Kim; Huishu Xue; Hrishit Leen; Roman Yakunin; Animesh Garg; Zsolt Kira
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.33007) · [Project](https://capex-paper.github.io/)
- Tags: CAPEX, autonomous-demonstrator, confidence-calibration, bounded-memory, waypoint-planning, supporting-data-generation
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結VLMが複数waypointと到達確率を提案し、過去の実行結果で確率を較正して信頼できる先頭部分だけを実行する。少数の成功例と段階別の信頼度を次の収集に渡し、成功軌跡をDiffusion Policy/ACTの教師データにする。

**主な貢献**

RoboCasa18課題360開始状態で収集成功12.5→53.6%、成功demo当たりの論文時点API費用を80%削減。実機YAMは40/42成功。学生方策は人demoに近づくが、20k学習stepの平均は人demo未満で、事前学習DPの差も残る。

**確認記録**

- Checked: 2026-10-06 · Review: needs-review
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。本文前のcanonical arXiv/DOI・正規化/類似タイトル照合一致なし。初稿 https://arxiv.org/abs/2609.33007 : v1 2026-09-26 23:05:46 UTC、改訂なし。HTML https://arxiv.org/html/2609.33007v1 の§3/4/5を選読。較正は同じ課題の過去waypoint成否、少なくとも1waypointを実行する。後続学生はDP/ACTでVLA/世界モデルの推論時融合ではなくagent/replanningに分類。収集性能は基盤モデル依存、Qwen+CAPEXは5/350。記憶の改善は成功例取得後に集中し、失敗履歴のみでは改善しない。学生simulationは選択6課題、3seed各50rollout、実機Frankaは3課題各方策10trialで絶対成功は低い。実機resetと成功判定は人手、完全無人収集の証拠ではない。費用は2026-09-22のlist-price評価。公式projectリンクはwebで2度取得失敗し到達性未確認のためneeds-review。著者/題名code検索でも公式実装・重み・実装license未確認unknown。PDF未取得。

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
