<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / planning

[← wam](README.md) · [CSV master](../papers.csv)

27 records · Published date 降順（同日 ID 降順）

### Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future

- ID: `WAM-0136`
- Published: 2026-10-20
- Authors: Zhuohao Li; Jiawei He; Yuxuan Yan; Lang Zhou; Yinghao Li; Yanrui Li; Tianyu Zhang; Yi-Yang Song; Xirui Wu; Yi-Lin Wei; Fating Hong; Qing Zhang; Zhilin Zhao; Jingdong Wang; Wei-Shi Zheng
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.28431) · [Project](https://isee-laboratory.github.io/TaskWAM/)
- Tags: TaskWAM, stage-confusion, structured-task-state, mode-codebook, causal-state-tokens, residual-steering, StageBench
- Model size: FastWAM/Wan2.2-TI2V-5B or Cosmos Policy backbone; total unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

局所的に妥当な未来でも別task/段階へ逸れるstage confusionを扱うTaskWAM。指示の順序・時機・反復をMode Tokensに、実行済みactionと観測変化の因果履歴をState Tokensに整理する。

**主な貢献**

構造化task状態をattention/AdaLNと残差予測へ注入し、worldとaction生成を意図した次段階へ誘導。8task familyのStageBenchを整備し、FastWAM平均成功40.9%→69.4%を報告する。

**確認記録**

- Checked: 2026-10-21 · Review: verified
- 初稿・題名・著者・版履歴をarXiv absで確認（v1=2026-10-20、改訂なし）。https://arxiv.org/html/2610.28431v1 の§3/4/5、Appendix A/Bと公式projectを選読。ModeはT5指示にgroundし、Stateはaction/観測潜在/差分を集約するため、外部agent plannerとの接続ではない。StageBenchは重なる多段階軌道を意図的に構成した評価。4身体の実機評価は各task100–150実演で適応し、各variant10–20試行であり未学習身体へのzero-shot保証ではない。project/題名検索で公式公開実装・重み・LICENSEは確認できず各unknown。補足のimplementation記載だけで公開codeとは判定しない。PDF未取得。 2026-10-08〜21の選択増分調査（基礎文献は分類補完の例外）。独立した実行・数値再現なし。

### Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation

- ID: `WAM-0134`
- Published: 2026-10-19 · Updated: 2026-10-20
- Authors: Xuezhou Xu; Chung-Pang Wang; Zhenzhen Li; Benjamin Riviere
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.25600) · [PDF](https://arxiv.org/pdf/2610.25600)
- Tags: vector-quantization, latent-planning, feedback-control, controller-reachability, Tower-of-Hanoi, offline-play
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

潜在世界モデル内のcontroller rolloutから初到達時間を推定し、低レベル制御で到達可能な状態を離散codebookへまとめる。離散遷移上の幅優先探索で長期経路を求め、連続視覚feedback controllerで順に実行する。

**主な貢献**

Euclidean距離でなくcontroller依存の到達時間で計画抽象を構成。実機4枚Tower of Hanoiは短いplayから15手解へ合成し、non-expert設定でtask progress100%を報告。実験はepisodeごと1回の計画で、頻繁な再計画の効果は未検証。

**確認記録**

- Checked: 2026-10-23 · Review: needs-review
- arXiv v1初稿日・全著者、HTML §IV/§V-B/§VIと公開PDFを確認: https://arxiv.org/html/2610.25600v1 。本文は実機指標をtask progressと記すため、要旨の100% success rateをそのまま完全成功率として拡張しない。実機は6初期目標組×各3試行。公式code/project/weightsへのリンクはarXiv・HTMLで見つからず、タイトル+著者+codeの公開検索でも公式提供先を確認できないため各statusはunknown。未公開と断定しない。 2026-10-23増分確認: 本文前のcanonical arXiv/DOI照合でWAM-0134と一致。canonical absとv1/v2 absで初稿2026-10-19 00:06:44 UTC・v2改訂2026-10-20 20:08:37 UTC、題名・全著者の同一性を確認。https://arxiv.org/html/2610.25600v1 と https://arxiv.org/html/2610.25600v2 のarticleテキスト差分と§IV/§V–VIを選読。v2は要旨のsimulation改善幅の下限を13.3→8.0ポイントへ修正し、V-JEPA 2-AC\*の94±6% task progressがH1の値であることと、各disk移動の6段階subgoalを明確化。新手法・追加実験結果とは確認していない。数式/表のMathML alttext 200要素は両版で一致するが図の変更は未検査。canonical/v2 abs要旨は依然13.3–85.3ポイントでv2 HTMLの8.0–85.3と不一致のためneeds-review。既存の保守的summary/contributionは維持。今回PDF本体未取得、code/weights/licenseの新たな公開を示す専用リンクもabs/HTMLに確認できずunknownを維持（外部release先の網羅的再調査ではない）。

### SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation

- ID: `WAM-0122`
- Published: 2026-10-13
- Authors: Yifei Yang; Zehua Fan; Zike Yan; Zhongyu Li; Yan Wang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18135) · [PDF](https://arxiv.org/pdf/2610.18135)
- Tags: visual-navigation, latent-world-model, knowledge-distillation, coarse-to-fine-planning, efficient-inference
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

視覚ナビゲーションで候補行動列の将来状態を潜在空間で予測する。自己予測を次の入力に使う閉ループ学習、長い時間間隔を飛ばす生徒モデルへの蒸留、候補を粗選別して強い自己回帰モデルで再評価する二段階計画を組み合わせる。

**主な貢献**

Latent AutoRollで訓練と推論の履歴ずれを減らし、SkipDistillで教師の将来潜在状態を長いstrideで近似する。著者らのRECON・HuRoN・SCAND・TartanDrive評価では、NWM比で平均ATE 4.2%、RPE 2.7%減、計画時間62.4%減と報告。HuRoNは公開上の制約により低解像度subsetでの条件付き比較。

**確認記録**

- Checked: 2026-10-15 · Review: verified
- https://arxiv.org/abs/2610.18135 v1 only, submitted 2026-10-13 UTC; https://arxiv.org/html/2610.18135v1 §§3-4/Table 1 verifies method, reported comparison, and low-resolution HuRoN protocol. ArXiv HTML supplies PDF href; PDF web parser errored. No official paper-specific code, checkpoints or implementation license verified in paper/abstract and exact-title searches; statuses unknown. Metrics are author-reported, not independently reproduced.

### CAG-WAM: Causal Action-Gain World Action Models for Robot Manipulation

- ID: `WAM-0128`
- Published: 2026-10-10
- Authors: Peizheng Guo; Cheng Zhang; Xingyu Zhang; Changwen Zheng; Wenwen Qiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.14720) · [PDF](https://arxiv.org/pdf/2610.14720)
- Tags: CAG-WAM, causal-action-gain, paired-future-prediction, GRPO, action-revision
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

WAMの未来評価に混在する行動由来の変化と環境由来の変化を構造的因果モデルで分析する。同じ観測から行動条件付き未来と環境のみの未来を予測し、評価差をcausal action gainとしてGRPO学習と推論時の行動修正に利用する。

**主な貢献**

予測未来の総合評価だけに頼らず、環境の自然な変化に対して候補行動がもたらす改善量を対になった未来の差分で評価する。

**確認記録**

- Checked: 2026-10-18 · Review: verified
- 2026-10-05〜2026-10-18の選択増分調査。本文前にcanonical arXiv・正規化/近似題名を既存351件と照合し一致なし。arXiv DOI/version aliasも別論文として扱わない。arXiv一次資料で題名・全著者・初稿日2026-10-10・v1のみの履歴・要旨・PDFリンクを確認。本文 https://arxiv.org/html/2610.14720v1 を選択確認。HTMLと題名検索では公式実装・重み・project・実装ライセンスを確認できずunknown。論文公開ライセンスを実装ライセンスとは扱わない。独立した実行再現なし。

### CASTER: Formalizing Zero-Shot Manipulation from Synthetic Videos as Constrained Optimization

- ID: `WAM-0115`
- Published: 2026-10-08
- Authors: Yinlong Dai; Homanga Bharadhwaj; Dylan P. Losey
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12567) · [Code](https://github.com/VT-Collab/CASTER) · [Project](https://collab.me.vt.edu/CASTER/)
- Tags: synthetic-video-guidance, constrained-optimization, digital-twin, task-feature-alignment, frozen-video-generator, zero-shot, multi-video, open-loop, real-robot
- Model size: Frozen HunyuanVideo-1.5 480P-I2V generator; system total unspecified
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

生成した人間のtask動画から物体軌道を得て、意味整合と物理実行可能性を満たすrobot軌道探索の初期値にする。複数動画に共通するtask重要特徴を合わせ、RGB-Dから作るdigital twin内でcollision・関節制約を課した最適化を行う。

**主な貢献**

動画からrobot動作への変換を制約付き最適化として統一し、初期動画が意味的な局所修正域に入る条件を整理する。12実機taskの平均成功76.6%は最良baseline42.5%から+34.1 pointsで、動画をそのまま再生する方式ではない。

**確認記録**

- Checked: 2026-10-13 · Review: verified
- abs履歴v1=2026-10-08 18:00:55 UTC、改訂なし。HTML §§IV–VIIを選読: https://arxiv.org/html/2610.12567v1 。一般動画generatorを推論時に使うplanning研究で、robot-specific joint WAM学習ではない。各task20動画を生成しsemantic検証後7動画でCEMを初期化、CASTERとMimicは各task21実機軌道試行。open-loop実行で、sim-real物理差がkettle/handle taskの失敗要因。projectが指す公式repoのsrc/caster/pipeline.py (https://github.com/VT-Collab/CASTER/blob/main/src/caster/pipeline.py) とLICENSE全文MITをGitHub APIで確認: https://github.com/VT-Collab/CASTER/blob/main/LICENSE 。依存modelの提供と専用checkpointを区別しweights\_status unknown。PDF公式リンクのfetchはtool errorのためpdf\_url空欄。

### LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild

- ID: `WAM-0100`
- Published: 2026-10-08
- Authors: Linkai Liu; Yuntian Zhang; Zhenshan Bing; Chen Chen; Lingjuan Lyu; Shangguang Wang; Mengwei Xu; Dongqi Cai
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12368)
- Tags: latent-world-model, visual-navigation, candidate-ranking, shared-encoding, multi-horizon
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結ナビゲーション方策の候補軌道を、共有画像符号化と並列多時点の潜在未来予測で比較する世界モデル。RGB動画再構成を省き、学習した相対scorerで軌道を選択する。

**主な貢献**

候補ごとの画像rolloutを共有符号化と非自己回帰の未来潜在予測へ置き換える。RECON/SCAND/SACSoNと別proposerへの転移を評価。Go2の3scene各10試行ではSR83.3%、NoMaD43.3%。

**確認記録**

- Checked: 2026-10-09 · Review: needs-review
- v1初稿・著者・題名、HTML III/IV-E,F/Vを確認: https://arxiv.org/html/2610.12368v1 。実装・重み・LICENSEは本文リンクとLiteNWM検索で未確認。限界: image-goalの3scene/30試行、RTX5090上の速度、manipulation転移未検証。速度値に不整合: 要旨/IV-EはNWM-S16.86×/NWM-XL128.00×、結論は18.39×/132.02×。その比率は貢献欄から除外。追補はTable IVのtiming境界/比率訂正と専用release。

### Reliability-Aware Future Conditioning for Temporally Robust Robot Manipulation

- ID: `WAM-0095`
- Published: 2026-10-08
- Authors: Mohammad Khoshnazar; Mohammad Dehghani Tezerjani; Zhiyuan Gao; Deyuan Qu; Max Gandyra; Yanxiang Zhan; Mehreen Naeem; Andrew Melnik; Jeroen Schafer; Qing Yang; Michael Beetz
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.11956) · [Project](https://future-condition.github.io/)
- Tags: future-video-conditioning, temporal-misalignment, reliability-gating, residual-rl, supporting-method
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

一度生成した未来動画の時刻ずれを制御側で扱うRAFC。静的fallbackと近傍phase候補を凍結BCに通し、信頼度gateと有界residualで行動を混合する。

**主な貢献**

8 CALVIN課題のoff-grid shift平均で生成未来51.8%→RAFC73.7%、同じ候補の均等平均66.7%より7.0pp高い。自然な時刻差のFranka3課題各20trialは16/60→34/60成功。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.11956 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.11956v1 。§III-D/IVと https://future-condition.github.io/ を選読。GPT-4oのgoal grounding、robot-free digital-twin rollout、CogVideoX/VideoPainter系生成はtask開始時1回で、LLMは閉ループ低レベル行動を生成しない。BCはResNet18+TransformerでVLAとはしない。候補{-2,0,+2}に対し6非zero global shiftを評価、平均はzeroを除外。windowed GenFuture81.3%→54.8%とclipped69.8%→34.2%を混ぜない。codeは今後公開の記載でunavailable、重み/実装licenseはunknown。 PDF未取得。

### PlanWAM: Planning-Shaped Future Representations for End-to-End Autonomous Driving

- ID: `WAM-0093`
- Published: 2026-10-08
- Authors: Jinchang Xu; Hongda Yu; Fengwei Dong; Wenhui Huang; Xi Wei; Yongzhi Liu; Sunan Zhang; Jirao Wang; Chen Lv; Bingbing Li; Guodong Yin; Weichao Zhuang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.11382)
- Tags: autonomous-driving, planning-shaped-latent, privileged-posterior, hindsight-distillation, supporting-foundation
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

自動運転の未来潜在表現を、画像再構成の忠実度ではなくtrajectory planning目的で形づくる。未来を見たtraining-only posteriorから、履歴だけを使うpriorへ蒸留する。

**主な貢献**

Temporal Register Pyramidの履歴圧縮とHindsight-to-Foresight Distillationで、計画に役立つ未来情報をtrajectory生成/選択へ渡す。NAVSIM open-loopとHUGSIM zero-shot閉ループsimulationで評価。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿・著者・題名、HTML3節/4節を確認: https://arxiv.org/html/2610.11382v1 。posteriorは訓練のみでGT futureを使い、推論priorはhistoryのみ。評価は自動運転benchmarkで、実車安全性やmanipulationへの転移実証ではない（評価範囲からの留保）。本文リンクとPlanWAM検索で公式実装・独自重み・LICENSEを確認できず各unknown。追補はreleaseと実車/ロボット転移の検証。

### Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation

- ID: `WAM-0083`
- Published: 2026-10-07
- Authors: Tzu-Yu Chuang; Ching-Hsiang Chang; Yi-Hsiu Lee; Yi-Ting Chen; Min Sun; YuanFu Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09309) · [Code](https://github.com/Claire0730/executable-goals) · [Project](https://claire0730.github.io/executable-goals/)
- Tags: Entity-Level-Goal-Readout, 3D-trace-world-model, SE3-goal, prediction-to-execution, pose-feedback, reproducibility-caveat
- Model size: Planner 677.6M incl. frozen encoders; executor 0.8M
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

3D trace world modelの表現から、物体中心の回転予測と観測depthに基づく位置readoutでSE(3)の終端目標を明示的に学習する。episode開始時に固定した目標を小型Pose-Native Executorへ渡し、pose feedbackで20Hzの閉ループ操作を行う。

**主な貢献**

未来予測から制御用目標への学習interfaceを分離し、目標誤差・操作・位置摂動を評価。論文報告は5task平均79.69%とFranka転移。ただし公式公開記録は比較間のexecutor差、追加処理、simulation由来pose feedbackを開示しており、純粋なreadout効果としては未確定。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿: https://arxiv.org/abs/2610.09309 。HTML §§III–VIを精読: https://arxiv.org/html/2610.09309v1 。実装Apache-2.0: https://github.com/Claire0730/executable-goals/blob/main/LICENSE 。公式model card https://huggingface.co/Claire0730/executable-goals は縮小planner/student/teacher配布とApache-2.0を説明するが、public tree/APIおよびraw/resolve SHA256SUMSはいずれもread toolで取得できず、実配布ファイル・manifest・重み条件は独立確認できないためweights\_status=unknown。公開repoのevidence/01\_checkpoint\_registry.csvは元private-runのpath/size/hashであり、0.30GB releaseplannerの提供確認には使わない。追跡: public HF file一覧またはrelease SHA256SUMSで縮小plannerとstudent/teacherのfilename・size・SHA256を確認し、配布先の重みlicenseを別途照合する。公式 https://github.com/Claire0730/executable-goals/blob/main/docs/KNOWN\_ISSUES.md items15–19 とREPRODUCTION.mdを確認: Table IIに3executor、PickCube goal診断と実行は別bank/SAM2処理、psi token、simulator correspondence、1.27秒記録未配布。論文のshared-executor/追跡loop記述との不一致。追跡: 同一executor・同一readout/bank・非privileged pose条件の対照結果または著者訂正を照合。固定終端目標は軌道/contact制約やgoal更新を扱えない。PDF未取得・URL未検証のためpdf\_url空欄。

### EpicWorldModel: Exploration-driven Planning with Latent World Models

- ID: `WAM-0107`
- Published: 2026-10-05
- Authors: Bowen Feng; Julian Ost; May Mei; Anirudha Majumdar; Felix Heide
- Venue: NeurIPS 2026 (author-reported)
- Links: [Paper](https://arxiv.org/abs/2610.05996)
- Tags: stochastic-jepa, flow-matching, partial-observability, uncertainty-exploration, image-goal-cem
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

部分観測下で複数の未来があり得る状況を、flow matchingによる確率的JEPAで表現する。潜在予測の分散を探索の手掛かりにし、画像目標への接近と未知領域の探索をCEM計画で両立する。

**主な貢献**

決定論的潜在世界モデルへの不確実性導入と探索付き計画を統合。Visual PointMaze GiantでFMの成功率86.0%に対しLeWMは64.5%。高次元のAntMazeでは同等程度で、利益は環境に依存する。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv履歴v1=2026-10-05、改訂なし、commentsにNeurIPS2026採択。HTML §§3,4.1–4.6,5を選択読解: https://arxiv.org/html/2610.05996v1 。OGBench Visual PointMaze/AntMaze/Scene、Car Racing、LabMaze、RoboCasa NavigateKitchenの部分観測simulationで評価。画像goalは展開時にない特権情報を含む場合があり、言語goal未対応。探索係数/NFEの最適値は環境依存、自動調整は今後。HTML/absリンクと題名限定検索で公式code/専用weights/実装licenseは確認できずunknown、不存在は断定しない。PDFは取得していない。

### H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning

- ID: `WAM-0106`
- Published: 2026-10-05
- Authors: Wancong Zhang; Basile Terver; Michael Rabbat; Yann LeCun; Randall Balestriero
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06805) · [Code](https://github.com/kevinghst/H-JEPA) · [Project](https://h-jepa.com/)
- Tags: hierarchical-jepa, multi-timescale, latent-subgoals, inverse-dynamics, offline-droid
- Model size: unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

時間幅と潜在空間が異なる行動条件付きJEPAを階層化し、上位の未来予測を下位のサブゴールとして使う世界モデル。報酬や画像再構成なしで学び、多様なDROID動画では逆ダイナミクス損失で動作情報の消失を抑える。

**主な貢献**

時間分解と抽象的な目標距離の効果を分けて検証。Visual AntMazeでは3階層が平坦LeWMの18.0%に対し73.3%の成功率を示し、少ない計画計算量で改善した。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv履歴v1=2026-10-05、改訂なし。HTML §§2,3,4.1–4.3,6を選択読解: https://arxiv.org/html/2610.06805v1 。FourRoomDistractors/Visual AntMaze/Push-T/OGBench Cubeで評価、DROIDは実機成功率でなくoffline open-loop Fréchet trajectory fidelity。Push-Tは3階層以上で利用可能clipが減り性能低下、全環境で選択的抽象化が生じるとはしない。実装MIT全文: https://github.com/kevinghst/H-JEPA/blob/main/LICENSE 。独立した重みmodel cardとファイル一覧確認: https://huggingface.co/jepa-world-models/h-jepa/tree/main ; 84simulation+9DROID checkpoints、cardの重みlicenseはMIT。物理ロボット閉ループ検証は今後。PDF/重み/dataは取得していない。

### Keeping JEPA World Models Plannable When Little of the Frame Moves

- ID: `WAM-0077`
- Published: 2026-10-02
- Authors: Florian Strohm; Patrick Wagner; Jannik Schwab; Marco Huber
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.03137) · [PDF](https://arxiv.org/pdf/2610.03137)
- Tags: SLIM, JEPA, latent-planning, inverse-dynamics, action-sensitivity, language-goals, simulation
- Model size: ~18M trainable; 5.5M ViT-Tiny encoder; ~167K training-only inverse-dynamics head
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

小さな複数物体を押す合成2DベンチマークSLIMで、画面の行動応答が弱いとLeWMの潜在表現が物体・操作主体を捨て、計画に失敗する状況を診断。連続する符号化潜在と予測潜在へ共有逆動力学損失を加え、行動に必要な情報を保持する。修復後の潜在へ言語目標を写す小型ヘッドも評価した。

**主な貢献**

訓練時だけ使う逆動力学ヘッドにより、同一plannerでSLIM成功率を0.003から0.348±0.016へ改善。PushTの学習時の2倍の計画horizonでは0.53から0.83へ改善した。対照実験はencoderへの勾配の重要性を示す。一方、very-hard tierは両モデル0%、未知語彙を含む段階指示や大きなencoderへの計画転移には限界が残る。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。arXiv書誌とv1初稿日2026-10-02を確認、後続版なし。HTML https://arxiv.org/html/2610.03137v1 の§3-7、Table 1/4、Appendix C/J/Kを確認。3学習seedの平均±SEMで0.348±0.016、評価は合成2DとPushTで実機展開なし。action-sensitivityは経験的な必要条件で十分条件ではない。概要のscripted controllerが全tierを解く表現に対し、本文Table 1は既定budgetでvery-hard0.28、Appendix Eは60stepで1.00と区別する。§7のReproducibility statementはコードを将来公開予定（will be released）と明記するため、code\_status=unavailable。公開URLは空欄とし、重み・実装ライセンスは未確認でunknown。PDFリンクを確認、ダウンロードなし。

### Beyond Policy Alignment: Closing the Planning-Learning Loop for Robot Control with Learned World Models

- ID: `WAM-0054`
- Published: 2026-09-30
- Authors: Kowndinya Boyalakuntla; Yuhan Liu; Abdeslam Boularias
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39751) · [Code](https://github.com/Kowndinya2000/pl-mpc) · [Project](https://pl-mpc-humanoid.github.io/)
- Tags: PL-MPC, TD-MPC, multi-step-TD, critic-uncertainty, actor-distillation, sim-to-real
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

世界モデルを用いるMPCの計画と学習のフィードバックを、価値学習・終端評価・方策蒸留の三つの接点で改善する。世界モデルとMPPIの構成自体は維持する。

**主な貢献**

実観測報酬を多く使うTD目標、critic不一致に応じた終端推定、高リターンの計画行動を重視する蒸留を統合。性能改善は課題・seed依存として報告される。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿とHTML本文IV節・評価の課題依存性を確認。論文の公開予定表現より新しい公式projectリンクで実装を確認。root MIT: https://github.com/Kowndinya2000/pl-mpc/blob/main/LICENSE 。READMEは学習済み研究checkpointを同梱しないと明記するが、外部重み配布は未確認なのでweights\_status=unknown。第三者コード・SDKは別条項。

### Social-WM: Safety-Aware Latent World Models for Robot Social Navigation

- ID: `WAM-0053`
- Published: 2026-09-30
- Authors: Zhihao Zheng; Mooi Choo Chuah
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.40177)
- Tags: social-navigation, action-realizability, inverse-dynamics, safety-aware, latent-planning
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人や障害物がいる環境で、名目上の指令と実際に実行できる動作の差を潜在世界モデルへ学習させる。候補動作の将来予測と逆動力学を組み合わせ、目標への進行と実行可能性を評価する。

**主な貢献**

指令後に実際に観測された未来と実現動作を教師とし、名目動作との不一致を実行前の安全関連信号に使う。安全性の一般保証ではなくシミュレーション評価。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿・著者とHTML本文III節・評価を確認。ICRA 2027への投稿記載は採択と扱わずvenue=arXiv。確認した一次資料に公式実装・重み・実装ライセンスの根拠なし。PDF未取得。

### The Planning Limits of Latent World Models

- ID: `WAM-0052`
- Published: 2026-09-30
- Authors: Ali Alrasheed; Basim Azam; Naveed Akhtar
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39235)
- Tags: planning-horizon, latent-world-model, VLA-action-selection, Meta-World, BridgeData-V2
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結した視覚表現上の行動条件付き世界モデルが、どの距離の目標まで計画に役立つかを調べる。Meta-Worldと実機由来のオフラインデータを使い、予測誤差と想像区間の短さを切り分ける。

**主な貢献**

実シミュレータによる完全予測との対照で、目標とロールアウト長の不一致を診断。近いサブゴールとVLA候補の選択を、学習済みモデルの利用方法として比較する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXivのv1初稿日・著者とHTML本文3、5–7節・付録Bを確認。BridgeData V2はオフライン分析であり実機閉ループ成功の主張と区別。実装・重み・ライセンスの公式提供根拠は未確認。PDF未取得。

### What Must a World Model Distinguish for Planning?

- ID: `WAM-0051`
- Published: 2026-09-26
- Authors: Rongzhe Wei; Hans Hao-Hsun Hsu; Peizhi Niu; Yifan Li; Pan Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.33030)
- Tags: planning-sufficiency, query-conditioned, decision-representation, robotics
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

世界モデルが計画に保持すべき情報を、目的、候補行動、探索段階に応じて整理する。衝突系、非線形動力学、ロボット計画で、予測の細かさと意思決定に必要な細かさを比較する。

**主な貢献**

機構・応答・意思決定の十分性を区別し、目的依存の候補生成と再利用可能な行動条件付き予測を分離する設計を提示。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXivのv1初稿日・著者・要旨とHTML本文3–4節、計画実験の該当節を確認。確認した一次資料に公式実装・重み提供先を見つけられず、公開状態と実装ライセンスはunknown。PDFは取得していない。

### Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving

- ID: `WAM-0037`
- Published: 2026-03-25 · Updated: 2026-03-25
- Authors: Linbo Wang; Yupeng Zheng; Qiang Chen; Shiwei Li; Yichen Zhang; Zebin Xing; Qichao Zhang; Xiang Li; Deheng Qian; Pengxuan Yang; Yihang Dong; Ce Hao; Xiaoqing Ye; Junyu han; Yifeng Pan; Dongbin Zhao
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2603.24581v1) · [PDF](https://arxiv.org/pdf/2603.24581v1)
- Tags: Autonomous Driving, Geometry Distillation, Latent Dynamics, Latent-WAM
- Model size: 104M
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

複数カメラ画像を圧縮した世界表現と将来予測を、自動運転の軌跡計画へ使うLatent-WAMを提案。ロボット操作とは異なる運転領域で、限られた計算とデータを評価する。

**主な貢献**

幾何知識を蒸留する学習可能なシーンクエリと、視覚・運動履歴に条件付けた因果Transformerの潜在予測を組み合わせる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

- ID: `WAM-0032`
- Published: 2024-11-07 · Updated: 2025-02-01
- Authors: Gaoyue Zhou; Hengkai Pan; Yann LeCun; Lerrel Pinto
- Venue: ICML 2025
- Links: [Paper](https://arxiv.org/abs/2411.04983v2) · [PDF](https://arxiv.org/pdf/2411.04983v2) · [Code](https://github.com/gaoyuezhou/dino_wm)
- Tags: JEPA, DINOv2, Image-goal Planning, Offline Learning, DINO-WM
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

オフラインの行動軌跡から視覚的な動力学を学び、初めての画像目標へ行動系列を最適化するDINO-WMを提案。報酬モデルや事前の方策を必要としない計画を評価する。

**主な貢献**

固定DINOv2の空間パッチ特徴を行動条件付きに予測し、候補系列の未来特徴と目標特徴の距離で探索する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT; source: https://github.com/gaoyuezhou/dino\_wm.

### OGBench: Benchmarking Offline Goal-Conditioned RL

- ID: `WAM-0050`
- Published: 2024-10-26 · Updated: 2025-02-13
- Authors: Seohong Park; Kevin Frans; Benjamin Eysenbach; Sergey Levine
- Venue: ICLR 2025
- Links: [Paper](https://arxiv.org/abs/2410.20092v2) · [PDF](https://arxiv.org/pdf/2410.20092v2) · [Code](https://github.com/seohongpark/ogbench) · [Project](https://seohong.me/projects/ogbench)
- Tags: Benchmark, Offline RL, Goal-conditioned, Stitching, OGBench
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

報酬のないオフライン軌跡から、任意の目標へ行く能力を比較するOGBenchを提案。世界モデルや目標条件付き方策に必要な能力を、単一の成功率だけにまとめず測れる評価基盤。

**主な貢献**

環境とデータセットを設計して、軌跡のつなぎ合わせ、長期推論、高次元入力、確率性を個別に調べる標準実装と評価を提供する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/seohongpark/ogbench.

### TD-MPC2: Scalable, Robust World Models for Continuous Control

- ID: `WAM-0039`
- Published: 2023-10-25 · Updated: 2024-03-21
- Authors: Nicklas Hansen; Hao Su; Xiaolong Wang
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2310.16828v2) · [PDF](https://arxiv.org/pdf/2310.16828v2) · [Code](https://github.com/nicklashansen/tdmpc2) · [Project](https://tdmpc2.com)
- Tags: Model-based RL, Continuous Control, Scaling, TD-MPC2
- Model size: 1M–317M family; 5M default
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

画素の再構成をせずに制御用の潜在モデルを学ぶTD-MPCを、広い連続制御へ拡張した研究。共通の設定で多様な課題を扱い、モデルとデータの規模効果を調べる。

**主な貢献**

SimNormで潜在状態を小さな単体の集合へ正規化し、対数空間の報酬・価値回帰とQアンサンブルで学習を安定させ、方策事前分布を使うMPCへ接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/nicklashansen/tdmpc2. SimNorm and model-size family checked in https://arxiv.org/html/2310.16828v2.

### LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning

- ID: `WAM-0049`
- Published: 2023-06-05 · Updated: 2023-10-14
- Authors: Bo Liu; Yifeng Zhu; Chongkai Gao; Yihao Feng; Qiang Liu; Yuke Zhu; Peter Stone
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2306.03310v2) · [PDF](https://arxiv.org/pdf/2306.03310v2) · [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) · [Project](https://libero-project.github.io/)
- Tags: Benchmark, Lifelong Learning, Language-conditioned, LIBERO
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

ロボット操作の継続学習で、物体・配置・目標などの知識移転を比べるLIBEROを提案。世界モデルそのものではなく、言語条件付き操作の評価基盤と実演データを提供する。

**主な貢献**

手続き的なタスク生成と四つの評価スイートを用意し、課題順序・事前学習・知覚表現が継続学習に与える影響を測る。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/Lifelong-Robot-Learning/LIBERO.

### Mastering Diverse Domains through World Models

- ID: `WAM-0041`
- Published: 2023-01-10 · Updated: 2024-04-17
- Authors: Danijar Hafner; Jurgis Pasukonis; Jimmy Ba; Timothy Lillicrap
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2301.04104v2) · [PDF](https://arxiv.org/pdf/2301.04104v2) · [Code](https://github.com/danijar/dreamerv3) · [Project](https://danijar.com/dreamerv3)
- Tags: Model-based RL, Imagination, Actor Critic, DreamerV3
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

世界モデル内で未来を想像して方策を学ぶDreamerV3を提案。ドメインごとの大幅な設定調整を減らし、画素と疎な報酬から多様な制御課題を学ぶことを狙う。

**主な貢献**

想像した潜在軌跡でactorとcriticを学習し、正規化・損失のバランス・値の変換で複数領域に共通する学習安定性を高める。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/danijar/dreamerv3.

### The Value Equivalence Principle for Model-Based Reinforcement Learning

- ID: `WAM-0043`
- Published: 2020-11-06 · Updated: 2020-11-06
- Authors: Christopher Grimm; André Barreto; Satinder Singh; David Silver
- Venue: NeurIPS 2020
- Links: [Paper](https://arxiv.org/abs/2011.03506v1) · [PDF](https://arxiv.org/pdf/2011.03506v1)
- Tags: Theory, Value Equivalence, Bellman Updates, Model-based RL
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

環境の遷移が違っても、特定の方策と価値関数に対して同じ計画ができるモデルを理論化した研究。表現やモデルへ何を残すべきかを、価値更新の等価性から考える。

**主な貢献**

対象とする関数と方策の集合でBellman更新が一致するvalue equivalenceを定義し、集合を増やしたときのモデルの識別範囲を解析する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

- ID: `WAM-0042`
- Published: 2019-11-19 · Updated: 2020-02-21
- Authors: Julian Schrittwieser; Ioannis Antonoglou; Thomas Hubert; Karen Simonyan; Laurent Sifre; Simon Schmitt; Arthur Guez; Edward Lockhart; Demis Hassabis; Thore Graepel; Timothy Lillicrap; David Silver
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/1911.08265v2) · [PDF](https://arxiv.org/pdf/1911.08265v2)
- Tags: Model-based RL, Tree Search, Reward Value Policy, MuZero
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ゲーム規則や完全なシミュレータを与えず、学習したモデルと木探索で行動を選ぶMuZeroを提案。観測を忠実に再構成する代わりに、判断に必要な量を予測する。

**主な貢献**

反復可能な潜在動力学に報酬・方策・価値の予測を学習させ、そのモデルで探索を行う。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Hierarchical Foresight: Self-Supervised Learning of Long-Horizon Tasks via Visual Subgoal Generation

- ID: `WAM-0047`
- Published: 2019-09-12 · Updated: 2019-09-12
- Authors: Suraj Nair; Chelsea Finn
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/1909.05829v1) · [PDF](https://arxiv.org/pdf/1909.05829v1) · [Project](https://sites.google.com/stanford.edu/hvf)
- Tags: Hierarchical Planning, Visual Subgoal, Video Prediction, HVF
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

遠い画像目標への計画を、途中の視覚サブゴールで分解するHierarchical Visual Foresightを提案。長期の動画予測誤差とサンプリング探索の負担を減らすことを狙う。

**主な貢献**

目標に条件付けて生成する中間画像を直接最適化し、動画予測に基づく短区間の計画を階層的に接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Generalizable Robotic Insertion with World Models

- ID: `WAM-0061`
- Published: unknown / 未確認
- Authors: Nicklas Hansen; Iretiayo Akinola; Yijie Guo; Jie Xu; Bingjie Tang; Hao Su; Xiaolong Wang; Abhishek Gupta; Dieter Fox; Yashraj Narang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.28258)
- Tags: InsertionWM, TD-MPC2, contact-rich, depth-proprioception, zero-shot-assembly, earlier-workshop-version
- Model size: 5M learnable parameters
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

手首深度画像と固有感覚を融合した潜在世界モデルで挿入動作を計画するInsertionWM。TD-MPC2を基に、物体IDを入力せず複数組立形状から一般化するモデルベース強化学習を調べる。

**主な貢献**

90形状で学習し、同分布から保持した10形状のシミュレーションで平均56%のゼロショット成功を報告。視覚遮蔽とsim-to-realが限界であり、実機組立の実証や任意形状への保証ではない。

**確認記録**

- Checked: 2026-10-03 · Review: needs-review
- arXiv v1初稿は2026-09-23。HTML https://arxiv.org/html/2609.28258v1 のIII–V節、VI-A/B節、VII節を確認。著者の公開CV https://www.nicklashansen.com/files/cv.pdf は同題・同著者のRSS OOD workshop 2025版を記載し、一次OpenReview PDF検索 https://openreview.net/pdf?id=DR3n6IqGKI も題・著者が一致。最初の公開日の正確な年月日は未確認なのでpublishedは空欄、needs-review。OpenReview forumはブラウザ検証が必要で日付未取得。次回は公式workshop投稿履歴で初出日を解決し、このIDを維持する。IROS 2026はarXivコメント/著者ページのみのためvenue=arXiv。専用コード・重み・実装ライセンスは未確認、TD-MPC2本体から推定しない。PDF未取得。

### Hidden Failure Modes in Latent World-Model Planning from Offline Data

- ID: `WAM-0046`
- Published: unknown / 未確認
- Authors: Kanpat Vesessook; Kevin Yang
- Venue: ICML 2026 Workshop on Decision-Making from Offline Datasets to Online Adaptation
- Links: [Paper](https://openreview.net/forum?id=kS01rTyQ9s) · [PDF](https://portfolio-rho-flame-83.vercel.app/projects/assets/lewmro/paper.pdf) · [Code](https://github.com/24GUNV/LeWMRO) · [Project](https://portfolio-rho-flame-83.vercel.app/projects/lewmro)
- Tags: Offline Learning, Receding Horizon, Failure Analysis, Workshop, LeWMRO
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

オフライン学習した潜在世界モデルの失敗を、計画の評価時刻と実際の実行区間の不一致から分析する研究。迂回が必要な課題では、目標への距離だけで制御可能性を表せない点も調べる。

**主な貢献**

計画長Hと実行接頭辞Kを分離し、prefix・running costおよびwaypointと局所actuatorの対照実験で二種類の計画インターフェースの失敗を切り分ける。

**確認記録**

- Checked: 2026-10-01 · Review: needs-review
- Publication year 2026 verified from authors and official workshop reference; exact first-publication/submission date unverified because OpenReview requires browser verification and public API returned403. Checkpoints/datasets are not included in the official release. Implementation license checked: MIT; source: https://github.com/24GUNV/LeWMRO.
