<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

16 records · Published date 降順（同日 ID 降順）

### ARC: A Reasoning Recipe for Robot Foundation Models

- ID: `HYBRID-0131`
- Published: 2026-10-08
- Authors: Gokul Puthumanaillam; Tao Sun; Elie Aljalbout; Moritz Reuss; Zhaoshuo Li; Fabio Ramos; Ankit Goyal; Jenai Xuning Yang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.12386) · [Project](https://arc-robot-reasoning.github.io/)
- Tags: action-grounded-reasoning, external-vlm, causal-traces, wam-compatible, droid
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

既存DROIDデモから行動の理由と効果を示すcausal traceを自動生成し、既存RFMをtrace条件付き制御へ微調整するARC。実行時には外部VLMが観察からtraceを更新する。

**主な貢献**

VLAとWAMへの別々の適応recipeを示し、RoboLab-120のdefault指示でπ0.5は28.0%→45.3%、Cosmos3-Nanoは36.8%→48.8%。追加の新規ロボットデモなしで推論教師を構築した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.12386 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.12386v1 。§4.2–5.1選読。約75K DROID episode/1.2M frameを再labelし、既存デモでfine-tuneするためtraining-freeではない。外部reasoner条件付きVLAを主分類vla-agent、WAM variantはtags/説明に保持し三要素同時融合としない。hardwareの91.7%は28再現課題の集計で一般成功保証ではない。https://arc-robot-reasoning.github.io/ はCode/Model/Dataset Coming soonとreview後releaseを明記し、code/weights unavailable、実装ライセンスunknown。 PDF未取得。

### RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes

- ID: `HYBRID-0129`
- Published: 2026-10-08
- Authors: Bohan Zhou; Xingbei Chen; Emily Huang; Weilin Ruan; Haojian Huang; Yehang Zhang; Zexi Li; Wenqian Li; Qize Yu; Zetian Song; Leyi Wu; Jinghao Li; Mingxuan Song; Xinrun Xu; Zongyang Qiu; Yangkai Wei; Tianyi Zhang; Kaiwen Zhou; Yinchuan Li; James Cheng
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.11480)
- Tags: skill-orchestration, counterfactual-branching, policy-family-coordinator, q-learning, mcts
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結coding agentとmodular skill/VLA系policyを組み合わせ、現在状態に適したpolicy familyの責任を学習する。P5段階構造と同一状態からの反実仮想実行で、選ばれなかった枝の結果も収集する。

**主な貢献**

State-Locked Counterfactual BranchingとMCTS/Q-learningでfamily-conditioned価値を学び、推論時は観測文脈だけでfamilyを選ぶ。100simulation課題のsingle-episode評価で77.0%overall成功を報告。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿・著者・題名、HTML3節/SCB-EAL/5節を確認: https://arxiv.org/html/2610.11480v1 。trainではsimulator snapshot復元・oracle mask・GT object poseとreward evaluatorを用い、deploymentでprivileged signal/online searchを使わない主張とは分ける。policy switchingはP5境界に限られ、atomic end-to-end呼出中の一時失敗の細粒度割込は未解決。本文リンク/題名検索で公式実装・独自重み・LICENSE未確認（同名旧IRF repoは別研究）。追補は専用releaseと実機評価。

### NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

- ID: `HYBRID-0127`
- Published: 2026-10-07
- Authors: Gengze Zhou; Yicong Hong; Jiazhao Zhang; Xunyi Zhao; Jian Zhou; Zixing Lei; Zun Wang; Chongyang Zhao; Xionghui Chen; Stephen Gould; Anton van den Hengel; Qi Wu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10787) · [Code](https://github.com/metacognitionai/NavGPT-3) · [Project](https://metacognitionai.github.io/NavGPT3/)
- Tags: navigation, hierarchical-runtime, motion-authority, context-allocation, route-repair
- Model size: NavGPT VLA variants: 4.44B and 8.77B (4B/8B names); Planner size varies
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

言語モデルPlannerとナビゲーションVLAを、状態/文脈管理・空間tool・route修復harnessで結ぶ。上位runtimeが推論、行動、監視のthreadとmotion authorityを管理し、割込後の再検証を行う。

**主な貢献**

harness/runtime/VLAを共同設計し、scene変化に応じたvisual token配分も学習。full-split R2R-CE/RxR-CEで評価し、8B単独のRxR-CE SR78.19%からcomplete harness90.43%へ改善。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿・著者・題名、HTML3節/4.8/5節とprojectを確認: https://arxiv.org/html/2610.10787v1 。公式sourceはVLA inference/harness/simulation evalでApache-2.0全文確認: https://github.com/metacognitionai/NavGPT-3/blob/main/LICENSE 。HF両variantにsafetensors shard/indexを独立確認: https://huggingface.co/Metacognition-AI/NavGPT3-4B/tree/main ; https://huggingface.co/Metacognition-AI/NavGPT3-8B/tree/main 。モデルカードはAGPL-3.0でsourceと別条項。UnitreeのZEOS deployment/thread実装は別repoで後日予定。19.28Mは再利用/augmentationを含むeffective recordでunique trajectory数ではない。human参考値はdiscrete研究でcontinuous RxR-CEと条件が異なる。

### Co-Evolving Robot Orchestrators and Policies through Deployment

- ID: `HYBRID-0125`
- Published: 2026-10-06
- Authors: Xilun Zhang; Maggie Wang; Erik Bauer; Hong-Xing Yu; Huang Huang; Jiajun Wu; Marco Pavone
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09228) · [Project](https://robo-cop.pages.dev/)
- Tags: Robo-COP, deployment-time-learning, VLA-orchestration, skill-demonstration-curation, policy-verification, episodic-memory, real-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VLM orchestratorがVLAとscripted skillを組み合わせて実行し、失敗episode内の成功skillも学習例として抽出する。更新を必要と判断した時だけVLAをfine-tuneし、期待skillの改善を検証して採用・巻き戻しを決め、古い方策に依存する記憶を更新する。

**主な貢献**

単に固定VLAへ回復動作を追加するだけでなく、実行データのskill単位選別、訓練開始判断、candidate policyの検証、orchestrator記憶の改訂を連結してVLAとAgentを共進化。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿2026-10-06、v1。本文§3–5を選択読解: https://arxiv.org/html/2610.09228v1 。DROID π0.5＋Gemini 3.8 Flash orchestrator、RoboLab10タスク各100deployment trial後に50held-out初期化へ凍結評価; 平均73.8%対fixed-policy64.8%、実機3タスク38.3→50.0%。単一learning runで、自己実行で部分成功できるskillのみを学習; 実機resetは人手、訓練・curation・検証costが増える。orchestratorの推論・judge・scripted skill自体は固定。VLA呼出とAgent判断が実行時にも中心なのでHybrid/vla-agent。要旨の公式projectはcode提供を宣言するがweb取得失敗; 実装URL/license/checkpointを独立確認できずunknown。Follow-up: 公式projectから公開実装を辿りLICENSEとfine-tuned policy重みを確認する。PDF未取得。

### Recursive Video In-Context Learning for Agentic Robot

- ID: `HYBRID-0118`
- Published: 2026-10-05
- Authors: Wenrui Bao; Xinxin Liu; Bingxin Xu; Yuzhang Shang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06843) · [Code](https://github.com/BWR-hhh/rvicl) · [Project](https://bwr-hhh.github.io/rvicl/)
- Tags: RV-ICL, hierarchical-video-memory, in-context-learning, frozen-VLA, read-only-tools, LIBERO-PRO
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

一つのデモ動画を全体keyframe・phase・moment・短いclipの四階層へ変換し、LLMエージェントが計画時と接触動作時で必要な粒度だけ参照する。HarnessVLA上で凍結π0.5を操作ツールとして使い、重み更新を行わず実行中にデモへ再アクセスする。

**主な貢献**

LIBERO-PROで成功率92.6%から96.5%、LIBERO-Plusの層化抽出120変種で86.7%から95.8%へ改善。長期課題では同じ動画の全提示やkeyframeだけより階層アクセスが有効だった。評価はシミュレーションのみで、デモの状態情報と単一ロボットに依存する。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.06843 のv1は2026-10-05 17:59:11 UTC、改訂なし。Oct 6告知日とは区別。 https://arxiv.org/html/2610.06843v1 §3–5、Limitationsを選択読解。PROは8セル各50試行で既報baseline各100試行と別run、Plusは公式全10,030件ではない。gripper/fixture状態から事象を切り出し、phaseに物体状態も使用する。clip再読込はcontextと費用を増やす。本文リンク先の https://github.com/BWR-hhh/rvicl でpatch/scriptsとscripts/run\_sweep.pyを確認、 https://github.com/BWR-hhh/rvicl/blob/main/LICENSE のApache-2.0を独立確認。デモと外部基盤重みは別ライセンスで、専用重み配布は未確認。PDF未取得。

### ProactiveVLA: Augmenting Embodied Memory through Proactive Environment Exploration

- ID: `HYBRID-0132`
- Published: 2026-10-04
- Authors: Shizuo Tian; Haodong Luo; Yutong Li; Yuebing Song; Yunxin Liu; Yuanchun Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06999)
- Tags: ProactiveVLA, proactive-exploration, deployment-time-adaptation, embodied-memory, frozen-VLA, affordance, LIBERO-Pro
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高level agentと凍結VLAを組み合わせ、初期task完了後の残りのinteraction budgetを環境の自主探索に使う。物体affordance、状態変更、interactionの組合せを自己提案し、結果の視覚検証と独立した証拠reviewを通して経験をglobal memoryへ統合し、次の計画と制御を助ける。

**主な貢献**

VLA自体の更新をせず、限られた環境経験の取り方と記憶の整理によって適応する。LIBERO-Pro Goal-TのVLA呼出し最多1回の再評価で48%成功、Harness VLA19%。この上限はVLA callだけで、知覚・解析的制御toolは利用可能。実験はLIBERO-ProとRoboCasa365 Composite-Seenのsimulationで単一実行stack。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- abs history v1 2026-10-04、改訂なし。https://arxiv.org/html/2610.06999v1 の§3.1–3.3、§4.1、§5–6を選択確認。Harness VLA上の同じCodex planner比較、評価時のVLAとglobal memoryは凍結。real-world transfer未評価。選択確認した一次資料に当該研究の公式code/weights/実装licenseへのリンクなし、unknown。PDF未取得。

### RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer

- ID: `HYBRID-0123`
- Published: 2026-10-02
- Authors: Chenxi Li; Zhangrui Zhao; Rui Li; Yuan Gao; Kehui Liu; Jiarui Li; Dong Wang; Tong Si; Minting Pan; Wanli Ouyang; Dongzhan Zhou
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02717)
- Tags: RoboBridge, sim-to-real, procedural-skills, skill-evolution, validation-gating, inference-time-guidance, frozen-VLA, LIBERO-PRO
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結したVLAを行動ツールとして用いるエージェントが、観測・操作・結果検証を結ぶ手続き的スキルを実行フィードバックで修正する。候補スキルを検証してから保存し、仮想環境で得た手続きを共通インターフェース経由で実機へ移し、方策を再学習せず継続適応させる。

**主な貢献**

検証付きスキル改訂と、エージェントが設定する推論時の報酬誘導を統合した手続き的sim-to-real。LIBERO-PROの800テストで成功率74.4%（Harness VLA 72.1%）を報告し、実機3タスクでも移行後のスキル適応を評価した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。書誌・初稿日は https://arxiv.org/abs/2610.02717 の履歴v1（2026-10-02 02:53:57 UTC）で確認、改訂なし。 https://arxiv.org/html/2610.02717v1 §3、§4、§5、付録C–Eを確認。Codex/GPT-5.5と凍結π0.5を使用し、仮想環境はRLinf LIBERO、実機はOpenPI DROIDの異なるチェックポイント。実機は共通のタスク意味・観測／操作インターフェースを整えた3タスク、各15評価試行であり、一般的な未整備環境への転移を示すものではない。§5は他の基盤モデル／ハーネスへの拡張を未検証とする。本文・要旨と限定検索では公式コード、プロジェクト、重み配布先・実装ライセンスを未確認。既存基盤の公開性を本実装の公開性に転用しない。PDFの取得・エンドポイント確認は行わず空欄。

### Bridging Frontier Reasoning and Robot Execution: From Autonomous Demonstration Generation to Dense Language Supervision

- ID: `HYBRID-0115`
- Published: 2026-10-02
- Authors: Bosung Kim; Alexander Trevithick; Ruiyi Wang; Prithviraj Ammanabrolu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.03615)
- Tags: frontier-reasoning, autonomous-demonstrations, dense-language-supervision, hierarchical-instructions, local-VLA, latency
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高遅延のfrontier modelによる推論を高速なローカル方策へ接続する二つの方法を検討する。補正デモを参照した自律軌跡生成をVLAの学習データへ加え、primitive・atomic・compositeの三階層と多面的な言語記述で方策の指示追従を学習する。

**主な貢献**

SO-101の4課題で、人間20本と生成20本を混ぜた方策と人間40本のみの方策は各80試行中41成功。RoboCasa365とBEHAVIOR-1Kでは階層的かつ多面的な言語監督の併用が比較条件中で最良となった。生成デモだけの学習や統計的同等性、系全体の実時間性は示していない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 本文取得前にrevisionなしarXiv/DOIと正規化/類似タイトルをローカル照合し一致なし。https://arxiv.org/abs/2610.03615 で正式著者・v1 2026-10-02 17:12:29 UTC・改訂なしを確認。HTML https://arxiv.org/html/2610.03615v1 の§3、§4の方法/評価設定、App.A、App.C.4/C.6を選択読解。物理方策はOpenPI π0.5をfine-tuneし、PaliGemma gemma\_2bとgemma\_300m action expertを用いるとApp.C.4に記載、系全体のparameter数は未確認。四課題の混合デモ比較は20人間のみの対照がなく、生成デモ追加の独立効果や統計的同等性は主張しない。言語監督比較は2組のtrain/eval seedで、評価taskは学習に含まれ、物理crosswordは5ゲーム。30Hzは目標であり一律の達成値ではなく、frontier API待ちが残る。生成の時間/費用は成功episodeのみ、失敗試行や一部hardware修正時間を含めない。abs/HTMLの公開リンクと正式タイトル・著者名による検索で公式実装、専用重み、実装ライセンスは確認できず各unknown。PDF未取得。

### MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation

- ID: `HYBRID-0114`
- Published: 2026-10-02
- Authors: Chenzhi Liu; Yue Zhang; Jiehong Lin; Jianan Wang; Bo Wang; Zhongrui Wang; Xiaojuan Qi
- Venue: CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2610.03476) · [Project](https://kaiknower.github.io/mobiagent/)
- Tags: MobiAgent, mobile-manipulation, skill-experts, visual-critic, recursive-improvement, replanning
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

実行時はVLMが原子的技能を逐次計画し、π0.5由来の共有VLMと技能別flow-matching expertが動作を生成する。視覚criticが再試行と再計画を選び、別の学習ループが収集軌跡を分割・検証して技能方策を更新する。

**主な貢献**

BEHAVIOR-1Kの選択した4タスクでは平均65.0%で、タスク別π0.5-TAの42.5%を上回る。RoboCasaの16複合タスクで基礎方策7.50%から最高27.50%、Astribot S1では32.5%から57.5%へ改善。技能干渉、姿勢補正の反復、遮蔽下のcritic誤判定が残る。

**確認記録**

- Checked: 2026-10-05 · Review: needs-review
- 本文取得前にrevisionなしarXiv ID/DOIと正規化/類似タイトルをローカル照合し一致なし。https://arxiv.org/abs/2610.03476 の正式著者、CoRL 2026採択コメント、v1 2026-10-02 15:48:23 UTC、改訂なしを確認。https://arxiv.org/html/2610.03476v1 の§3.1/3.2、§4.1、§5と選択した補足設定を読解。BEHAVIOR-1K全件ではなく4タスクで各10試行、RoboCasa365 Composite-Seenは16タスクで対象scene各5試行。後半更新roundは25.00〜27.50%に飽和。π0.5 VLA executorとVLM planner/criticの統合なのでhybrid/vla-agentに分類。公式projectのCodeとCheckpointを独立確認。Codeは https://github.com/kaiknower/MobiAgent を指すがweb取得失敗、GitHub connectorも404のため公開実装とライセンスを確認できず、code\_urlは空欄、各statusはunknown。公式checkpoint https://huggingface.co/Liukaikai/MobiAgent は25,000-stepの共有backbone/6 expertsを説明するが手動審査のアクセス申請が必要。未承認でファイル内容・重みライセンス未確認なのでweights\_status=unknown。アクセス申請・ダウンロードは行わず、この配布確認の残件をneeds-reviewに記録。PDF未取得。

### DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication

- ID: `HYBRID-0124`
- Published: 2026-10-01
- Authors: Hanchu Zhou; Dechen Gao; Hang Wang; Brendan Lynch; Boqi Zhao; Qiyao Ma; Raman Goyal; Junshan Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02161) · [Code](https://github.com/ucd-dare/DuoMind) · [Project](https://hanchuzhou.github.io/duomind_project_page/)
- Tags: DuoMind, multi-robot-coordination, semantic-communication, hierarchical-control, distributed-control, Qwen3-VL, pi0.5, RoboPoly, RoboTwin
- Model size: VLM: Qwen3-VL-4B-Instruct; VLA: π0.5（総パラメータ数未確認）
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

各ロボットのVLMが局所観測と相手からの意味的メッセージを使って短期指示を生成し、VLAが低レベル動作を実行する分散階層型システム。意図・サブゴール・タスク信念・任意の不確実性を自然言語で共有し、長期の協調操作を閉ループで進める。

**主な貢献**

VLMの意味推論とVLA制御を各ロボットで組み合わせ、構造化自然言語通信による協調を実現。7タスクのRoboPolyを構築し、RoboTwinの8タスクと各タスク400ロールアウトで比較。RoboPoly Cook Potは成功率39.25%（π0.5単体1.00%）を報告した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。書誌・初稿日は https://arxiv.org/abs/2610.02161 の履歴v1（2026-10-01 17:53:09 UTC）で確認、改訂なし。 https://arxiv.org/html/2610.02161v1 §2–4、付録B–Dを確認。評価は二エージェントのシミュレーションで、実機と大規模チームは未検証。VLAはタスク別LoRA調整、VLM指示を許容例へ制限し停滞時に段階進行する。全タスクで優越するわけではなくRoboTwin Put Object Cabinetは43.25%対π0.5単体46.50%。論文リンクの公式projectから公開repoを確認。実装LICENSEは https://github.com/ucd-dare/DuoMind/blob/main/LICENSE のApache-2.0（第三者MIT/BSD通知併記）、論文CC BY-NC-SAとは別。公開コードはRoboPoly、データ生成、評価、policyテンプレートを確認（ https://github.com/ucd-dare/DuoMind/blob/main/policy/custom/my\_policy.py は未実装ロード部）。DuoMind本体の完全な再現実装・調整済み重みは未確認。 https://huggingface.co/datasets/ucd-dare/robopoly\_demo はデモデータで、重みと区別。PDFは未取得・未確認で空欄。

### Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation

- ID: `HYBRID-0113`
- Published: 2026-10-01
- Authors: Isabella Liu; An-Chieh Cheng; Johan Bjorck; Zhiding Yu; Hongxu Yin; Jan Kautz; Linxi Fan; Yuke Zhu; Sifei Liu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01178) · [Project](https://www.liuisabella.com/Recova/)
- Tags: failure-recovery, digital-twin, code-as-policy, DAgger, human-intervention, parallel-workstations
- Model size: π0.5 task/recovery policies; total parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

エージェントが再構成MuJoCo digital twinで失敗復帰コードと軌跡を開発し、課題方策と復帰方策を別々に学習する。実行時は進捗監視・復帰・場面復元確認を行い、解決できない失敗の人間デモを対応する方策へ追加する。

**主な貢献**

LIBERO-Pro六条件とMolmoSpaces四分類で平均成功78.8%・64.9%。実機四課題各20試行でDAgger後77.5%、復帰追加87.5%。人間介入0%は一課題の第四収集round七episodeの観測で、無人運用や一般安全性を保証しない。対照は既報値で同時再実験ではない。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- canonical arXiv IDと正規化/類似タイトルのローカル重複確認後に本文を確認し一致なし。arXiv v1初稿2026-10-01 06:52:05 UTC、改訂なし。HTML §3・4・App.A/C確認: https://arxiv.org/html/2610.01178v1 。twinは再構成MuJoCoシミュレータで学習型WAMとは数えずvla-agentに分類。simulationはMolmoAct2+復帰プログラム、実機はπ0.5課題/復帰方策+Gemini 3.8 Flash監視。復帰は時間上限付きで未登録/失敗時は操作者に交代。公式projectと著者/手法名検索で公開実装・重み・実装ライセンス未確認。PDF未取得。

### RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance

- ID: `HYBRID-0116`
- Published: 2026-09-30
- Authors: Jingwei Jia; Keyu Zhou; Jiewei Wang; Peisen Xu; Xingyuan Zhou; Liang Wang; Jiming Chen; Gaofeng Li; Jin Wang; Shunlei Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39384) · [Project](https://roboassist.github.io/)
- Tags: RoboAssist, residual-replanning, workflow-memory, human-robot-handover, runtime-safety, GR00T
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人間の作業進行と実行可能なロボット課題列を分けて保持し、要求変更時には影響を受けた未完了部分だけを再計画する。LLMの課題判断、GR00T由来の操作expert、航行・受渡し・全身runtime監視を統合し、G1の模擬手術補助環境で評価する。

**主な貢献**

要求順序変更の16試行では成功率81.25%で、全未完了課題を再計画するFullReplanの68.75%を上回る。10ログ試行の平均再計画時間は3.62秒から1.20秒、変更後の計画tokenは20.02kから11.41kへ減少。臨床での安全性や一般的な実時間保証を示す評価ではない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 本文取得前にrevisionなしarXiv ID/DOIと正規化/類似タイトルをローカル比較し一致なし。https://arxiv.org/abs/2609.39384 で正式著者、v1 2026-09-30 09:34:17 UTC、改訂なしを確認。HTML https://arxiv.org/html/2609.39384v1 の§III、§IV-A/B/C、§Vを読解。shared GR00T N1.7 backboneと物体別grasp/shared placement-handover action expertsをLLM task agentが実行するためhybrid/vla-agentとした。G1ハードウェアを使う模擬手術補助場面であり臨床試験ではない。FullReplan比較のlatency/tokenはspeech recognitionとphysical execution、初期planning/perceptionを除いた計画コスト。効率別実験は各methodで成功5runのみ。force-feedback 20.11msとVLM 4.833sは異なるhazard triggerに対する応答で厳密に揃えたend-to-end比較ではない。最終subtaskでの失敗原因はplanningかphysical executionか分離されていない。公式projectはPaper/Code/TODO表示の雛形で、公開実装・専用重み・実装ライセンスは未確認のためunknown。PDF未取得。

### Where Memory Belongs: Ledger, an Object Ledger for Memory-Augmented VLAs

- ID: `HYBRID-0101`
- Published: 2026-09-28 · Updated: 2026-09-28
- Authors: Tanguy Dieudonné; Jack B. Jedlicki; Heng Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.34554) · [PDF](https://arxiv.org/pdf/2609.34554)
- Tags: Ledger, object-memory, temporal-memory, LLM-planner, π0.5, RoboMME
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

短期の知覚記憶をVLA内部、長期の物体状態・遮蔽・履歴を外部の読み取り可能なledgerへ分ける。SAM3の追跡とVLMのデモ説明をLLM plannerが参照し、実行ステップの境界で目標を決める単一π0.5方策を評価した。

**主な貢献**

記憶の種類に応じた配置分離と、ステップ境界での外部物体履歴groundingをVLAへ接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。一次HTMLで外部ledger・LLM planner・π0.5の構成を確認。公開実装・重み・ライセンスのリンクは未確認。https://arxiv.org/html/2609.34554v1

### SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation

- ID: `HYBRID-0106`
- Published: 2026-09-26
- Authors: Ziwen Li; Hanlue Zhang; Zhenyang Ren; Tianyu Huang; Runqi Lin; Haoyu Wang; Zhengqing Gao; Yandong Guo; Fakhri Karray; Tongliang Liu; Chris Russell; Mingming Gong
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.32698)
- Tags: failure-guided, online-rl, long-horizon, adapter
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

長期タスクを原子スキルに分解し、実行失敗から弱いスキルを特定する。LLMでシミュレーションの成功判定を生成し、同系統スキルが共有するVLAアダプターをオンラインRLで改善する。

**主な貢献**

追加の専門家デモを集めず、失敗状態の復元・タスク生成・共有アダプター更新を反復する自己改善システム。複数VLAと未知タスクへの転移を評価。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Relevant primary HTML https://arxiv.org/html/2609.32698v1 checked for author-owned project/code links; none verified. Referenced RLinf is upstream training infrastructure, not proof that SEES implementation or weights are released. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution

- ID: `HYBRID-0122`
- Published: 2026-09-24
- Authors: Junyi Tang; Jie Peng; Zezhen Ding; Yuan Shen; Tianlong Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.29204) · [Code](https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA)
- Tags: AdaHVLA, adaptive-harness, code-revision, revision-graph, behavioral-assessment, frozen-VLA, long-horizon
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

実行履歴・指示・進捗・回復・完了判定を管理するcode harnessを、rollout間で改訂する。証拠分析・code修正・行動評価を別agent contextへ分け、事前の検証可能な仮説と改訂後の挙動をrevision graphへ結びつける。保持したharnessと適応記憶を次課題へ継承する。

**主な貢献**

NaVILA-LH held-out40課題の3適応restart平均で初期harness22.5%から31.7–57.5%へ改善。π0.5操作L1では25.0%から55.8%、L2では10.0%から38.3%へ改善し、VLA重みを変えず調整規則の適応を示した。実機結果は例示的なtrajectoryである。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2609.29204 のv1は2026-09-24 08:14:03 UTC、改訂なし。 https://arxiv.org/html/2609.29204v1 §III–Vを確認。50instanceは10適応/40test、各run最大16candidate、held-out証拠で選択しない。test値は120評価で120別taskではない。SR-only selection/flat-history消融は同予算だが各機構の単独因果効果を証明しない。共有基盤モデルの視覚/空間誤りは分割contextでも残る。論文のCodeリンクと https://github.com/Haaareally のJunyi Tang本人表示から公式repoを確認、src/adahvla/adaptation.py等と https://github.com/Haaareally/AdaHVLA-Adaptive\_Harness\_VLA/blob/main/LICENSE のApache-2.0を独立確認。公開releaseはGo2 simulationのsample harnessで、全manipulation/実機adapterを含むと主張しない。専用調整重み未確認、unknown。PDF未取得。

### MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation

- ID: `HYBRID-0108`
- Published: 2026-09-22
- Authors: Junjie Xie; Chuxuan He; Angen Ye; Yujia Song; Dapeng Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.25756)
- Tags: medical-robotics, hierarchical, function-constrained, cot
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高水準の視覚言語推論を低水準の制約付き関数実行と組み合わせ、精密医療ロボットの閉ループ操作を行うMedVLA。複数エージェントでスキル志向CoT学習データを生成する。

**主な貢献**

連続行動だけでなく非行動のシステム関数も扱える階層的実行を導入。電極挿入100試行で95%成功を報告するが、臨床的安全性の実証とは扱わない。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.25756v1 and targeted title/code search checked; no official implementation/license, project, or weights verified. Classification as hybrid vla-agent is a curator interpretation of reasoning plus function-level execution. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.
