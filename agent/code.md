<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / code

[← agent](README.md) · [CSV master](../papers.csv)

6 records · Published date 降順（同日 ID 降順）

### SimEX: Simulation-Integrated Robotics AutoResearch

- ID: `AGENT-0114`
- Published: 2026-09-30
- Authors: Jiaheng Hu; Roberto Martin-Martin; Peter Stone; Rocky Duan; Zhenyu Jiang; Guanya Shi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.38982) · [Project](https://robo-simex.github.io/)
- Tags: SimEX, simulation-autoresearch, toolbox-synthesis, few-trial-adaptation, sim-to-real
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

coding agentがシミュレーションの探索・改善を通じて操作用toolboxを作り、少数の実機試行を再現してシミュレータとtoolboxを修正する。修正候補を実機へ戻す前に仮想実験で比較する。

**主な貢献**

開放的な技能探索と、実機証拠に基づく仮説生成・修正案のスクリーニングを二段階で接続。デモ不要の方法を限定した操作タスク群で検証する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿・著者、HTML本文2.2–2.4節と3節、公式projectを確認。シミュレータ利用自体を学習世界モデルと同一視せずagent/codeに分類。実機5試行の適応条件と独立評価を区別。確認した一次資料に公式研究実装・重み・実装ライセンスの提供根拠なし。

### ASENA: Self-evolving Agents for Embodied Navigation

- ID: `AGENT-0113`
- Published: 2026-09-30
- Authors: An-Chieh Cheng; Isabella Liu; Edmund Bu; Johan Bjorck; Hongxu Yin; Zhengyi Luo; Jan Kautz; Linxi "Jim" Fan; Yuke Zhu; Sifei Liu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39207) · [Project](https://asena-bot.github.io/)
- Tags: ASENA, navigation, persistent-experience, skill-library, VLA-tool, humanoid
- Model size: ASENA-VLN: 4B; coding-agent size unspecified
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

coding agentを知覚・実行・記録のロボットインターフェースにつなぎ、失敗修正と再利用可能なコード・経験の蓄積を行う。単眼の言語誘導ナビゲーション方策ASENA-VLNを任意ツールとして組み込む。

**主な貢献**

モデル重みを固定したまま実行証拠からプログラムと永続経験を更新する系を提示。反復する同一課題群での改善と、教師付き実機デモを分けて評価する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿・著者、HTML本文3節・4.4節、公式projectを確認。主貢献はプログラム生成と永続経験のためagent/codeに分類し、任意のVLAツールはtagに保持。反復課題の改善は未知課題への一般化保証と区別。確認した公式ページでは研究実装・重み・実装ライセンスの提供先を確認できずunknown。

### Eureka: Human-Level Reward Design via Coding Large Language Models

- ID: `AGENT-0109`
- Published: 2023-10-19 · Updated: 2024-04-30
- Authors: Yecheng Jason Ma; William Liang; Guanzhi Wang; De-An Huang; Osbert Bastani; Dinesh Jayaraman; Yuke Zhu; Linxi Fan; Anima Anandkumar
- Venue: ICLR 2024
- Links: [Paper](https://arxiv.org/abs/2310.12931) · [PDF](https://arxiv.org/pdf/2310.12931) · [Code](https://github.com/eureka-research/Eureka) · [Project](https://eureka-research.github.io/)
- Tags: Eureka, reward-code-generation, evolutionary-search, reinforcement-learning, skill-acquisition
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

LLMで報酬コードを生成し、強化学習の訓練結果をもとに進化的に改善するEurekaを提案。タスク固有のテンプレートなしに多様なロボット形態のシミュレーションで報酬設計と器用なスキル獲得を評価した。

**主な貢献**

学習feedbackをLLMのin-context改善へ返し、報酬プログラムの探索で低レベルスキルを獲得。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公開コードMIT。LLM本体のパラメータ規模は非公開のためmodel\_size空欄。 Code license: MIT; https://github.com/eureka-research/Eureka/blob/main/LICENSE.

### VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

- ID: `AGENT-0105`
- Published: 2023-07-12 · Updated: 2023-11-02
- Authors: Wenlong Huang; Chen Wang; Ruohan Zhang; Yunzhu Li; Jiajun Wu; Li Fei-Fei
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2307.05973) · [PDF](https://arxiv.org/pdf/2307.05973) · [Code](https://github.com/huangwl18/VoxPoser) · [Project](https://voxposer.github.io/)
- Tags: VoxPoser, 3D-value-map, VLM-grounding, closed-loop-motion-planning, contact-dynamics
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

LLMがコードを介してVLMの知覚結果を3D value mapへ合成し、自然言語のaffordanceと制約を観測空間にgroundingする。value map上のモデルベース計画で動作軌道を生成し、動的摂動や接触を含む操作を評価した。

**主な貢献**

言語による制約を実行可能な3D value mapとして合成し、事前定義スキルだけに依存しない軌道生成へ接続。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公開コードMIT。学習された一般的WAMの論文ではなく、言語・知覚・動作計画を組むAgentとして分類。 Code license: MIT; https://github.com/huangwl18/VoxPoser/blob/main/LICENSE.

### ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

- ID: `AGENT-0106`
- Published: 2022-09-22 · Updated: 2022-09-22
- Authors: Ishika Singh; Valts Blukis; Arsalan Mousavian; Ankit Goyal; Danfei Xu; Jonathan Tremblay; Dieter Fox; Jesse Thomason; Animesh Garg
- Venue: ICRA 2023
- Links: [Paper](https://arxiv.org/abs/2209.11302) · [PDF](https://arxiv.org/pdf/2209.11302) · [Code](https://github.com/NVlabs/progprompt-vh) · [Project](https://progprompt.github.io/)
- Tags: ProgPrompt, programmatic-prompting, precondition-checking, recovery, situated-planning
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

利用可能な動作API、環境の物体、実行例をプログラム形式のpromptで与え、LLMが実行可能なタスク計画を生成する。assertionによる事前条件確認と回復動作を使い、VirtualHomeと実機卓上タスクを評価した。

**主な貢献**

環境・ロボット能力をpythonic promptへ構造化し、生成計画に実行前提の検査と回復処理を組み込む。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公開VirtualHome版コードのNVIDIA LICENSE §3.3は研究・評価用途の非商用限定。OSI open-sourceとは扱わない。https://github.com/NVlabs/progprompt-vh/blob/main/LICENSE

### Code as Policies: Language Model Programs for Embodied Control

- ID: `AGENT-0102`
- Published: 2022-09-16 · Updated: 2023-05-25
- Authors: Jacky Liang; Wenlong Huang; Fei Xia; Peng Xu; Karol Hausman; Brian Ichter; Pete Florence; Andy Zeng
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2209.07753) · [PDF](https://arxiv.org/pdf/2209.07753) · [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) · [Project](https://code-as-policies.github.io/)
- Tags: Code-as-Policies, program-synthesis, reactive-control, hierarchical-code-generation, robot-API
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

自然言語命令から、知覚結果を処理し制御APIを呼ぶロボット方策プログラムを生成する。ループ・条件分岐・外部ライブラリで空間幾何推論や反応的制御を記述し、未定義関数を再帰的に生成する階層化を検証した。

**主な貢献**

LLM生成コードを高レベル計画だけでなく、feedback loopや連続制御のパラメータ化を含む方策表現にする。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式projectリンクの実装。Apache-2.0: https://github.com/google-research/google-research/blob/master/LICENSE
