<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / skill

[← agent](README.md) · [CSV master](../papers.csv)

4 records · Published date 降順（同日 ID 降順）

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
