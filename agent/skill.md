<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / skill

[← agent](README.md) · [CSV master](../papers.csv)

2 records · Published date 降順（同日 ID 降順）

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
