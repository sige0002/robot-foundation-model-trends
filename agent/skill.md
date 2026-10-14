<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / skill

[← agent](README.md) · [CSV master](../papers.csv)

6 records · Published date 降順（同日 ID 降順）

### ChunkAct: Action Chunking for Agentic Robotics

- ID: `AGENT-0155`
- Published: 2026-10-13
- Authors: Bingxin Xu; Wenrui Bao; Xinxin Liu; Jiawei Zhou; Yuzhang Shang; Emilio Ferrara
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.18874) · [PDF](https://arxiv.org/pdf/2610.18874)
- Tags: action-chunking, procedural-memory, LLM-planning, VLA-tools, robot-manipulation
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

LLMエージェントが知覚・制御・VLAツールを一手ずつ呼ぶ負荷を減らす。オフラインで手続き記憶を実行可能な動作チャンクに編成し、オンラインでは一回の呼び出しで連鎖実行し、失敗時だけ構造化されたエラーをプランナーへ返す。

**主な貢献**

エージェントの記憶を複数プリミティブの実行手順へ事前コンパイルし、LLM呼び出しを個々の動作から意思決定単位へ移す。LIBERO-Proで既存エージェント系比較より成功率5.0ポイント増、LLM呼び出し2.9分の1と著者報告。

**確認記録**

- Checked: 2026-10-15 · Review: verified
- arXiv v1・著者・要旨・本文の方法/実験・PDFリンク確認: https://arxiv.org/abs/2610.18874 ; https://arxiv.org/html/2610.18874v1 。本文に公式実装・重みの公開先を確認できず、公開状況はunknown。VLAは呼び出されるツールであり本研究の主貢献はエージェントのスキル実行効率。実機汎用性は未検証。後日著者の公開先を再確認。

### BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation

- ID: `AGENT-0151`
- Published: 2026-10-09
- Authors: Fabio Hübel; Adam Lilja; Yue Yin; Siming He; Claire Tomlin; Shankar Sastry; Jonas Frey; Marco Pavone
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.13862) · [PDF](https://arxiv.org/pdf/2610.13862) · [Code](https://github.com/fabiohuebel/bt-agent)
- Tags: behavior-tree, onboard-inference, structured-failure-feedback, runtime-guards, multi-fidelity-evaluation, real-robot, Spot
- Model size: Qwen3.5 NVFP4 4B/9B/27B/122B-A10B; onboard 9B
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

LLMが事前定義のbehavior-tree技能を選択し、技能内の局所guardが実行条件と中断を管理するonboard robot agent。161タスクのtext評価、39タスクのHabitat評価、SpotとJetson Thor上の9Bモデルによる実機試験を接続する。

**主な貢献**

モデル判断を待たずに技能を停止させ、構造化した失敗診断で再試行・再計画を支える実行interfaceを設計。共通161タスクで最良Act/ReAct比の成功率差は4Bで10.1、9Bで5.0percentage points、実機は11/15成功。

**確認記録**

- Checked: 2026-10-12 · Review: verified
- abs履歴v1=2026-10-09、改訂なし。Oct12 cs.RO announcementから発見しcanonical arXiv/DOIとnormalized/fuzzy/subtitle title matcherで既存一致なし。HTML §§III,V,VIを選択確認: https://arxiv.org/html/2610.13862v1 。text成功の57.3%のみHabitatでも成功、10.9倍throughputはtimeout除外。固定技能・scene prior・人のmotion承認に依存し、guardの19msはcommanded velocityで物理停止保証ではない。公式repo READMEが論文を明示し実装runtime.pyとApache-2.0全文を確認。public commit f90990ea9e842c07e4844ff59eebe33b1ea2185a=2026-10-12。https://github.com/fabiohuebel/bt-agent/blob/main/docs/RELEASE\_READINESS.md とLICENSE-SCOPE.mdではcompanion benchmarkは再配布許可待ち、weights/assets/recordings未同梱、release自体のlive robot検証未実施。コードlicenseはデータ・重みへ拡張されず、専用重み配布未確認。project URLはREADMEにあるが取得失敗で空欄。PDF未保存。

### Skill-SLM: Agent Skill-driven Small Language Models for Reliable Robot Operation

- ID: `AGENT-0141`
- Published: 2026-10-07
- Authors: Wenhao Wang; Yanyan Li; Jiawei Yuan
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10812)
- Tags: small-language-model, context-free-grammar, skill-composition, progressive-orchestration, onboard-uav
- Model size: Llama 3B/8B; Qwen3 4B/8B with LoRA; onboard Q4\_K\_M
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

小型言語モデルのrobot操作を、課題の丸ごと模倣からtask分解/skill合成へ組み替える。robot操作意味を反映するCFGでskillを抽出し、LLM教師から分解と段階的code合成を学ぶ。

**主な貢献**

skill-aware CFG、技能document、分解/合成の別LoRA adapter、progressive orchestrationを統合。Jetson Orin NX搭載UAV/地上車で、既知pattern・新組合せ・新能力の課題群を評価。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿・著者・題名、HTML III-B,C,D/IV-A,Cを確認: https://arxiv.org/html/2610.10812v1 。各skillのrobot APIへのgroundingはhuman expertが行い、300training instruction由来の教師データで学習。3/4/8Bは再利用SLMbackboneで研究独自total規模/公開重みではない。未知能力は準備されたskill/APIとCFG範囲であり自由な新技能獲得と区別。本文リンクと題名/著者検索で実装・独自重み・LICENSE未確認、各unknown。追補は専用release/データとskill外指示評価。

### SharedKV-BT: Node-Local Typed Decisions for Behavior-Tree Agents

- ID: `AGENT-0146`
- Published: 2026-10-05
- Authors: Naoki Wake; Justin Wagle
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.07327)
- Tags: behavior-tree, typed-decision, shared-kv, node-local-candidates, external-postconditions
- Model size: Qwen2.5-3B-Instruct; additional Qwen3-4B check
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

事前定義behavior treeの現在ノードに必要な技能・引数候補だけを提示し、共通prefixのKVを再利用して候補を並列採点する。独立した実行系と外部postconditionが動作順序と達成確認を管理する。

**主な貢献**

prefix再利用の速度、ノード局所interfaceの選択精度、実行gateの役割を分離評価。promptを揃えた自己回帰decodeより意思決定が2.36–4.15倍速く、Adaptive PickPlaceの完了率は局所候補で18/30、全候補で0/30。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv履歴v1=2026-10-05、改訂なし（commentsのlast updatedも同日）。HTML §§III,IV-B,IV-C,VIを選択読解: https://arxiv.org/html/2610.07327v1 。Robosuite Stack/PickPlace/NutAssemblySquare/Door、RoboCasa NavigateKitchen、WindowsAgentArena固定3taskで評価。実機/未知taskへの一般化は未検証。手作業structured state/事前BT/候補/技能/一部sim内部postconditionに依存し、候補なし時の信頼できる棄権や任意のfield互換性保証は未解決。18/30は公開candidate順のみ、順序を変えた閉ループ頑健性は未評価。公式実装/専用重み/実装licenseをHTML/absと題名限定検索で確認できずunknown、base modelの公開と区別。PDFは取得していない。

### Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation

- ID: `AGENT-0124`
- Published: 2026-10-02
- Authors: Xincheng He; Siyu Ma; Chang Yu; Yunuo Chen; Yanjia Huang; Ying Nian Wu; Yin Yang; Chenfanfu Jiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02788)
- Tags: Skill2Real, executable-skills, hierarchical-memory, sim-to-real, PVG, validation-gated-learning
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

Proposer・Verifier・Governorの役割を分け、シミュレータの評価情報を用いて実行可能な技能を検証・蓄積する。まず局所操作のCerebellumを学習・凍結し、その技能を組み合わせるBrainを学習する。凍結した二階層の技能記憶を共通API経由で実機へ移す。

**主な貢献**

LIBERO-90でSolが学習した凍結技能をAstraで評価すると、未学習のLIBERO-Pro Longで成功率2.0%から56.3%へ改善。UR5eの実機4課題では平均78.75%を報告。Verifier/Governor除去でPro Longが各17.3/13.3ポイント低下し、検証を伴う技能記憶更新の効果を調べた。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 本文取得前にrevisionなしarXiv ID/DOIと正規化/類似タイトルをローカル比較し一致なし。https://arxiv.org/abs/2610.02788 で正式著者・v1 2026-10-02 04:25:12 UTC・改訂なしを確認。HTML https://arxiv.org/html/2610.02788v1 の§3、§4、§5.1/5.2/5.3/5.4、§6およびApp.B.4〜B.6を選択読解。転移対象はモデルparameterではなく凍結したコード/API技能の知識でありagent/skillと分類。LIBERO-Pro Long checkpoint系列は20task各10seedで、別の固定C3/B3比較は10task各20trialの独立記録なので数値を混在させない。実機4task各20trial。Verifierはsimulation trainingでprivileged evidenceを使うがtarget evaluationには参加せず、実機転移はtask-policy fine-tuneや技能記憶更新なし。特権の効果だけを切り分けるにはpublic-only Verifier対照が必要とApp.B.6に記載。本文の公開リンクと正式タイトル/著者による公開検索で公式実装・専用重み・実装ライセンスは未確認、すべてunknown。PDF未取得。 §6では現状はpure code-as-policyで、end-to-end policyをcallable toolとして組み込むのは将来課題。VLM推論遅延と狭い場所のreactive controlが残る。

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
