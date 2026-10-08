<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / code

[← agent](README.md) · [CSV master](../papers.csv)

12 records · Published date 降順（同日 ID 降順）

### Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies

- ID: `AGENT-0140`
- Published: 2026-10-07
- Authors: Yihan Li; Yating Feng; Shengjiu Sun; Jianing Chen; Hao Ren; Bowen Yang; Weisheng Xu; Qiwei Wu; Hui Cheng; Renjing Xu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10479)
- Tags: Agentic-RSR, real-to-sim-to-real, scene-reconstruction, programmatic-policy, execution-feedback, experience-memory, real-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

作業空間の動画と既知のロボット形状から、タスクに必要な接触を再現するシミュレーションを構築する。coding agentは真値利用、画像観測のみ、摂動付き条件へと段階的に方策コードを改良し、実行feedbackと経験記録を実機での再観測・回復へ引き継ぐ。

**主な貢献**

scene再構築と生成方策を同じ操作タスクで結び、実行可能性の検査、段階的な観測制約、実機への方策・経験移送を一つのagentic開発loopへ統合。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-07、v1のみ。本文§3–5を選択読解: https://arxiv.org/html/2610.10479v1 。Piper/Franka計18タスク、主agentはGPT-6 Astra high。Sim成功10/18、実機成功8/18 (44.4%); 80%はsimulation成功タスクからのpaired transferで全実機成功率ではない。baselineのconversionは非pairedで比較は記述的。閉鎖model serviceのinterface/時点による未統制変動を限界として明記。MuJoCoは再構築・試験環境で学習WAMは提案しておらずAgent/code。要旨はcode/scene dataの今後公開を予告するが公式URLを確認できず、コード・重み・実装ライセンスはunknown。論文CC BY 4.0は実装ライセンスと区別。PDF未取得。

### PhysEvo: Astra Can Act, Let It

- ID: `AGENT-0136`
- Published: 2026-10-06
- Authors: Wenqing Tian; Zeyu Zhang; Zhaocheng Liu; Fengwei Liu; Qiang Liu; Liang Wang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08995)
- Tags: PhysEvo, physical-recursive-self-improvement, harness-evolution, frozen-model, joint-control, skill-reuse, real-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

同じ凍結multimodal modelを実行agentとmeta-agentの二つの役割で使い、ロボット軌跡から失敗を診断して操作ツール・skill・診断ツール自体を改良する。モデル重みの更新や別学習action policyなしに、検証済み変更を以後の行動と改善に再利用する。

**主な貢献**

実行feedbackを次の動作修正に留めず、関節姿勢の制御、証拠を保つ視点取得、後続改善で使える診断機能という二つの永続harnessの変更へ変換。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-06、v1。本文§3–5、§6を選択読解: https://arxiv.org/html/2610.08995v1 。42 RoboDojoタスク、task固有deployment版を各5held-out layoutで固定評価; five-dimension等重みSR62.00%、task等重み58.57%を区別。実機PiPERの5タスク×5trialはskill改訂を継続する適応過程でSR84%、凍結ゼロショット転移の数字ではない。baselineは公開referenceで広い平均比較は厳密なmatched ablationではない; 関節tool比較は別の限定6episode。追加学習VLA/WAMを導入せずAgent/code。公式論文・検索で当該実装repository・license・重み配布を確認できずunknown。PDF未取得。

### ArtifactArena: Evaluating Models by What They Build in the Physical World

- ID: `AGENT-0132`
- Published: 2026-10-05
- Authors: Kushagra Tiwary; David Mayo; Nikhil Behari; Xiangzhou Sun; Abdulrahman Alabdulkareem; Isaac Galatzer-Levy; Boris Katz; Brian Cheung
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06511) · [Code](https://github.com/ArtifactArena/harness-public) · [Project](https://artifactarena.ai)
- Tags: ArtifactArena, hardware-software-co-design, code-generation, verifier-feedback, MuJoCo, simulation-only, benchmark
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

基盤モデルがMuJoCo用ロボット形状とPython制御器を同時生成し、競技内で動作する成果物を評価する。独立sampling、verifier・試合feedbackによる改良、自由な設計labの3方式を同じAPI呼出予算で比較し、成果物同士の対戦からEloを算出する。

**主な貢献**

固定の答えを採点する代わりに、物理制約・機能検査・対戦を用いてモデルのロボット設計コードを評価する継続拡張型testbed。より自由なagent loopが常に強い成果物を生むわけではないことも検証。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-05、arXiv v1のみ。本文§2、§3.1、§3.5と公開harness READMEを選択読解: https://arxiv.org/html/2610.06511v1 。21モデル、各harness10 API呼出×3独立run。整合した予算はAPI呼出数のみでtoken数・wall time・計算量は同一とは限らない。VGHは15/21モデルで最高Elo、自由なDLHはtop-7成果物なし。MuJoCo内の設計・制御評価で実機能力ではない; bootstrap区間は候補内選抜の不確実性を含まず下限。公式SH/VGH実装MIT: https://github.com/ArtifactArena/harness-public/blob/main/LICENSE ; DLHもMIT: https://github.com/ArtifactArena/design-lab-harness/blob/main/LICENSE 。生成XML/制御コードはモデル重みではなくweights\_status=unknown。公式projectリンクは本文から確認したがweb取得は失敗。PDF・dataset未取得。

### OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies

- ID: `AGENT-0123`
- Published: 2026-10-01
- Authors: Zhaoyang Chu; Earl T. Barr; Claire Le Goues; Peter O'Hearn; Mark Harman; Federica Sarro; He Ye
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02459) · [Code](https://github.com/terminalworld/OpenRUA)
- Tags: OpenRUA, ROS2, code-as-policy, workspace-memory, zero-shot, simulation
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

汎用コーディングエージェントにROS 2への端末アクセスと作業ディレクトリを与え、観測の保存・解析と制御コードの作成を自律的に行わせる。専用の技能ライブラリやロボット方策の追加学習を使わず、ファイルと実行結果を再参照して操作を修正する。

**主な貢献**

Claude CodeとOpus 5の組合せでCaP-Bench成功率99.0%、LIBERO-PRO 87.0%、未見RoboCasa365複合タスク28.1%を報告。結果はシミュレーション評価であり、思考中の物理時間停止を含むため実機での遅延・安全性・センサ雑音への頑健性を保証しない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 2026-09-22〜2026-10-05のRobot Agent/Hybrid増分調査。本文取得前にscripts/validate\_csv.py --candidateでrevisionなしarXiv ID、DOI表記、正規化/類似タイトルを比較し一致なし。書誌と初稿履歴を https://arxiv.org/abs/2610.02459 で確認: v1 2026-10-01 20:32:41 UTC、改訂なし。HTML https://arxiv.org/html/2610.02459v1 の§3、§4.1/4.2、§4.7、§5を選択読解。CaP-Benchは7タスク各100試行、LIBERO-PROは各10試行、RoboCasa365は50対象タスク各10試行。実機評価は未実施と§5に明記。公式リンク先のREADME、openrua/、tests/等の公開実装と https://github.com/terminalworld/OpenRUA/blob/main/LICENSE のApache-2.0文面を独立確認。学習済み専用重みの配布は未確認、基盤モデルのAPIは実装ライセンスとは別。PDFはリンク表示のみで取得せず、検証済みの完全URLを保持できなかったためpdf\_urlは空欄。 公開実装はconnectorのcontents一覧と https://github.com/terminalworld/OpenRUA/blob/main/openrua/artifacts.py の選択コード読解でも確認。

### Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens

- ID: `AGENT-0116`
- Published: 2026-10-01
- Authors: Ruiyang Si; Jianxin Bi; Shunyu Yang; Rui Ni; Wenbo Huang; Qiang Wang; Shulong Jiang; Duomin Wang; Xiuyu Li; Haiwen Feng; Zhen Dong; Daquan Zhou
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01939) · [Code](https://github.com/DAGroup-PKU/PyRUA-Lean) · [Project](https://dagroup-pku.github.io/PyRUA-Lean/)
- Tags: PyRUA-Lean, interactive-code, selective-observation, primitive-composition, VLA-tool
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

ロボットの古典的プリミティブと凍結VLAをPythonオブジェクトへ公開し、分岐・再試行を一つのセルで実行するPyRUA-Lean。エピソード内の変数を保持し、要求した画像や状態だけを計画モデルへ返す。

**主な貢献**

同一の凍結計画モデル・ロボットプリミティブ・呼出予算で700シミュレーション試行を比較し、成功率63.1%から71.7%を報告。入力トークン65%削減は両方式が成功した共通部分での比較で、エピソード間記憶は用いない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.01939v1 の3節・4節の設定/費用/限界を確認。公式projectがリンクするsrc実装・README・NOTICEとroot Apache-2.0を独立確認: https://github.com/DAGroup-PKU/PyRUA-Lean/blob/main/LICENSE 。第三者RPent/VLA/知覚モデルは別配布であり専用学習済み重みの公開は未確認。主貢献は実行インターフェースなのでagent/codeとしVLAはtagに保持。PDF未取得。

### Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools

- ID: `AGENT-0121`
- Published: 2026-09-30
- Authors: Shijia Ge; Alex Zhou; Jianshu Zeng; Yexing Wan; Di Wu; Zelin Zheng; Yazhe Wang; Zhiqi Jia; Xuan Shangguan; Jay Zhu; Yijun Liu; Lingyu He; Sihang Wu; Xiao He; Hongcheng Gao
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39018) · [PDF](https://arxiv.org/pdf/2609.39018)
- Tags: URAI, Code-as-Policy, tool-synthesis, feedback-driven-selection, persistent-tools, bimanual-manipulation
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

URAIは、ロボット用の再利用可能なツールを作成・検証するプログラミングエージェントと、観測からツールを選択・引数指定する実行エージェントを接続する。ツール内部の多段階運動はローカルで実行し、呼び出し間の判断はモデルに戻す。検証済みのコード改訂をエピソード間に保存し、基盤モデルの重みは変更しない。

**主な貢献**

RoboDojoの5タスク・4実行エージェント・各5seedの比較で、直接制御に対する集計成功率を18.0%から53.0%へ改善。同じツールを使う2エージェントの対照では、事前生成プログラムの24%に対し呼び出しごとのモデル判断が56%となり、ツール集合と判断タイミングを分けて評価した。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- 書誌と履歴: https://arxiv.org/abs/2609.39018 。v1は2026-09-30 05:23:25 UTC、改訂なし。方法・評価・限界: https://arxiv.org/html/2609.39018v1 の3節・4節・5節・付録C。シミュレーション評価時のツールと実行モデルは固定し、ツール作成と人間の指示に要する時間・tokenは未計測。実機はAgileX双腕の7タスクで、既報比較は別ハードウェア・異なる呼び出し計数規則を含むため、因果的な高速化率とは扱わない。abs/HTMLとタイトル・URAI・著者所属を用いた公開検索では公式コード・project・重みの提供先を確認できず、公開状況と実装ライセンスはunknown。論文のCC BY 4.0を実装ライセンスに流用しない。PDF URLはabsページのリンクのみ確認し、PDFを取得していない。

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
