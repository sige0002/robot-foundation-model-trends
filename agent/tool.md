<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / tool

[← agent](README.md) · [CSV master](../papers.csv)

7 records · Published date 降順（同日 ID 降順）

### RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments

- ID: `AGENT-0139`
- Published: 2026-10-07
- Authors: Zhiqin Yang; Chenxin Li; Xiaomeng Hu; et al.
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10409) · [Code](https://github.com/robotworldai/robotworld) · [Project](https://robotworldai.github.io/)
- Tags: RobotWorld, robot-use, cross-embodiment, benchmark, tool-use, execution-feedback, simulation-only
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

操作、移動操作、歩行、運転、飛行の84シミュレーションタスクで、汎用multimodal agentのrobot-use能力を評価する。観測と制御ツールを明示的な予算で与え、agent自身の完了宣言とは独立した実行可能checkerで採点し、状態保持・修正・回復の失敗をtraceから調べる。

**主な貢献**

異なる身体・simulatorの観測/動作契約、独立成功判定、interaction予算、実行traceを共通評価loopで結び、部分的な知覚・計算能力が安定したタスク完遂へ結び付かない箇所を可視化。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-07、v1のみ。本文§3–5、§7とAppendix B.6/H.4–5を選択読解: https://arxiv.org/html/2610.10409v1 。5モデル×84タスク各1episode; 最良16/84 (19.0%)。environment-side code controlはoff、推論中physics停止。non-action予算はAstra記録から調整して他モデルにも適用; 21件のretrospective adjudicationがあり後刻成功は境界内成功に含めない。単発・不均一controller支援・有限suite・training contamination・実機未検証が限界。公式公開実装READMEがRobotWorld-owned codeのtop-level license未選択と明記: https://github.com/robotworldai/robotworld\#-validation-and-provenance 。第三者licenseのみを根拠にopen\_source=trueとしない。新規重み配布未確認。PDF・assets未取得。

### Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI

- ID: `AGENT-0131`
- Published: 2026-10-05
- Authors: Christopher Leet; Achu Menon; Sravanthi Machcha; Sabrina Zou; Aayushya Patel; Aditya Kumar Singh; Anish Kr Singh; Galaba Vamsi; Javin Ahuja; Sai Asish Yamani; Tushar Anand; Vedang Alle; Zihan Jack Zhang; Tzu Kit Chan; Jay Chooi
- Venue: arXiv; submitted to SPAIS Workshop at CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2610.06306) · [Code](https://github.com/robocurve/inspect-robots) · [Project](https://docs.inspectrobots.org/)
- Tags: Inspect-Robots, evaluation-framework, physical-AI-safety, tool-use, action-guards, real-robot
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

ロボット評価のタスク、方策、身体、実行管理、記録・分析を交換可能なインターフェースで結ぶ評価基盤。LLMをロボット制御・終了ツールへ接続し、観測更新による方策再実行と動作guardを共通化する。実機の能力・危険指示拒否を別々の小規模評価で検証した。

**主な貢献**

能力だけでなく拒否・危害軽減も記述できる複数rubricと、動作前guard・再観測・監査可能な記録を評価スタック全体の再利用可能な部品へ分離。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-05、arXiv v1のみを確認。本文§3–4を選択読解: https://arxiv.org/html/2610.06306v1 。I2RT YAM双腕で能力4タスク・安全4タスク、各モデル各タスク20試行。安全評価6方策では3種類の非人型危険指示の拒否は各モデル5%以下。小規模guard付き評価であり一般的安全保証ではない。公式実装MIT: https://github.com/robocurve/inspect-robots/blob/main/LICENSE 。新しいモデル重みの配布は確認できずunknown。PDFは取得していない。

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
- Code / weights / license: available / unknown / unknown

**概要（日本語）**

汎用エージェントが観測の選択・処理とネイティブなロボット行動の合成を自ら行う、LIBEROベースのシミュレーション評価系。200タスクを統合し、知覚・短期操作・長期操作を各10タスクに分けた主要30タスクで7種類のモデルと実行環境の組を比較する。

**主な貢献**

高レベル技能を与えないMCPインターフェースと、3回すべての成功または最小段階完了率で測る安定性指標を導入。主要評価では最高スコアが45.0/100でも、難しい短期操作の安定成功率は40%、難しい長期操作の安定段階完了率は22%で、対象識別と確実な実行の隔たりを示した。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 書誌と履歴 https://arxiv.org/abs/2609.39507 : v1 2026-09-30 11:10:10 UTC、追加改訂なし。既存HTML https://arxiv.org/html/2609.39507v1 の3/4節・付録B.3の選読結果を維持。主要30課題は同一初期状態・seed100で各3回、1800秒制限のsimulationであり200課題全件/実機評価ではない。本文の公式Code先 https://github.com/dzj441/Libero-Agent が2026-10-08 commit https://github.com/dzj441/Libero-Agent/commit/0b9a282ec083f89d9c537dd17bda6a0edc56ec07 で30課題benchmarkを公開。README、CHANGELOG、benchmark manifest、libero/libero/agent\_env/runtime/control.pyとtreeを確認しcode availableへ更新。公開範囲は知覚/短期操作/長期操作各10課題、MCP native7D OSC、evaluator/schedulerで、広いtask catalog・著者実験結果・全開発testは含まれない。READMEはmain30課題90rolloutと操作観測ablation60rollout、同じseed100/no reset/no automatic retryを区別し、公開runtimeのnative Codex隔離と外部harnessの未強制隔離の差も明記する。独自作業のMITは同commit LICENSEとTHIRD\_PARTY\_NOTICES.mdで確認したが、同noticeはvendorしたRoboMemArena revisionにroot licenseがないと明記しMITの再許諾対象外とする。配布実装全体のライセンス範囲が確定していないためopen\_source/license\_status unknownとneeds-reviewを維持。次回はRoboMemArena由来部分の明示許諾/ライセンス整理を確認する。基盤モデル重みは別サービス、独自公開checkpointは未確認でweights unknown。PDF URLはabsリンクの確認のみ、PDF未取得。

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
