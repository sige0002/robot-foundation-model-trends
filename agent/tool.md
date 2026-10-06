<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / tool

[← agent](README.md) · [CSV master](../papers.csv)

5 records · Published date 降順（同日 ID 降順）

### RobotUse: Allocating Computation, Context, and Decisions

- ID: `AGENT-0130`
- Published: 2026-10-04
- Authors: Junhoo Lee; Injun Baek; Seungyeon Kim; Suhyun Jeon; Minkyu Kim; Baekseung Kim; Nojun Kwak
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.04929) · [Code](https://github.com/robotuse-team/RobotUse) · [Project](https://robotuse-team.github.io/)
- Tags: RobotUse, visual-action-interface, context-handoff, subagents, persistent-playbook, motion-planning, RoboLab
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

ロボットの標的・grasp候補・姿勢をエージェントが画像上で選び直し、geometry・motion planning・制御をbackendへ委ねる。subgoalの詳細履歴をsubagent内に保ち、結果を主agentへ返す。実行経験からpersistent playbookを改訂し、方策重みとbackendは固定する。

**主な貢献**

RoboLabの40課題120 episodeで54成功、45.0%となりCaP-Xより6.67ポイント高い。単一contextへの統合では成功率40.8%、token使用量4.9倍だった。実機Pandaの3課題は別の学習段階後にplaybookを凍結し各25試行成功を報告した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.04929 のv1は2026-10-04 04:15:33 UTC、改訂なし。 https://arxiv.org/html/2610.04929v1 §4–5、App.A.6/A.7と公式 https://robotuse-team.github.io/ を確認。language agentは各task3trial、direct-actionは10trialで停止規則も異なるsystem比較。改訂段階の19/40→22/40は別系列。実機3課題の初回成功まで学習後の25trialはzero-shot成功率ではない。RobotUseはCaP-XよりAPI費用/時間を多く使う。公式repoのsrc/agent/prime\_agent.py等と https://github.com/robotuse-team/RobotUse/blob/main/LICENSE のApache-2.0を独立確認。公開releaseはnative RoboLabでPanda adapter未包含、依存assetの非商用条件は別。HFリンクはpaperページであり重み配布ではない。専用重みunknown。PDF未取得。

### LIBERO-Agent: Evaluating General-Purpose Agents for Direct Embodied Manipulation

- ID: `AGENT-0120`
- Published: 2026-09-30
- Authors: Zijie Diao; Yitong Chen; Sicheng Xie; Tianyi Lu; Wujian Peng; Guojin Zhong; Houze Xu; Ziyi Ye; Zuxuan Wu; Yu-Gang Jiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39507) · [PDF](https://arxiv.org/pdf/2609.39507) · [Code](https://github.com/dzj441/Libero-Agent)
- Tags: LIBERO-Agent, benchmark, agent-native-control, MCP, embodied-manipulation, long-horizon
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

汎用エージェントが観測の選択・処理とネイティブなロボット行動の合成を自ら行う、LIBEROベースのシミュレーション評価系。200タスクを統合し、知覚・短期操作・長期操作を各10タスクに分けた主要30タスクで7種類のモデルと実行環境の組を比較する。

**主な貢献**

高レベル技能を与えないMCPインターフェースと、3回すべての成功または最小段階完了率で測る安定性指標を導入。主要評価では最高スコアが45.0/100でも、難しい短期操作の安定成功率は40%、難しい長期操作の安定段階完了率は22%で、対象識別と確実な実行の隔たりを示した。

**確認記録**

- Checked: 2026-10-04 · Review: needs-review
- 書誌と履歴: https://arxiv.org/abs/2609.39507 。v1は2026-09-30 11:10:10 UTC、改訂なし。方法・評価: https://arxiv.org/html/2609.39507v1 の3節・4節・付録B.3。主要30タスクは同一初期状態・seed=100で各3回、1,800秒制限のシミュレーションであり、200タスク全件や実機の検証ではない。HTML冒頭の公式\[Code\]は https://github.com/dzj441/Libero-Agent を指すが、確認時点ではREADME.mdとLICENSEのみでREADMEがコード公開予定と明記。MIT文面と著者の著作権表示を https://github.com/dzj441/Libero-Agent/blob/main/LICENSE で確認したが、未公開の実装に対してopen\_source=trueとはしない。コードリンクと公開実態の差をneeds-reviewに記録。独立した公式project・重みは未確認。PDF URLはabsページのリンクのみ確認し、PDFを取得していない。

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

### An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond

- ID: `AGENT-0122`
- Published: 2026-09-21
- Authors: Wenbo Zhang; Kaixuan Wang; Yutao Ouyang; Xiaoyu Huang; Liyang Li; Kailun Su; Weiyang Jin; Wenhao Chai; Haotian Liang; Zhiyang Dou; Yue Chen; Tianxing Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.24170) · [Code](https://github.com/RoboProbe/RoboProbe) · [Project](https://robodojo-benchmark.com/report/gpt-6-astra-eval)
- Tags: LLM-as-policy, direct-control, RoboDojo, supporting-evaluation, safety-limits, closed-weight-backbone
- Model size: GPT-6 Astra/GPT-5.5/DeepSeek-Flash; parameters unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

凍結LLMがRGB・ロボット状態・履歴から直接エンドエフェクタ目標を選ぶ制御を評価する。学習済み運動方策を介さず、非学習の目標検証・軌道変換を用いる。

**主な貢献**

RoboDojo全42課題でAstraは2,100試行、成功率22.48%。公開方策との入力情報は同一でなく、精密・動的制御は弱い。実機は危険動作と機器損傷で中止され、残る33試行は診断資料で安全性・一般信頼性の証明ではない。

**確認記録**

- Checked: 2026-10-04 · Review: needs-review
- arXiv v1初稿2026-09-21 06:39:47 UTC、改訂なし。HTML §3・5・App.H/I確認: https://arxiv.org/html/2609.24170v1 。公式harnessの公開実装・結果と現行Apache-2.0 LICENSEを確認: https://github.com/RoboProbe/RoboProbe/blob/main/LICENSE 。READMEは最終release licenseをTBDとするためneeds-review。open\_sourceはharnessのみで、閉鎖重みAstra等のモデル公開を意味しない。論文固有の公開重みは未確認。PDF未取得。

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
