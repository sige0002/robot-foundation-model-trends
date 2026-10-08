<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / adaptation

[← vla](README.md) · [CSV master](../papers.csv)

27 records · Published date 降順（同日 ID 降順）

### RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input

- ID: `VLA-0176`
- Published: 2026-10-07
- Authors: Yanwen Zou; Chenyang Shi; Guoxuan Xu; Wenye Yu; Wendi Chen; Ye Pan; Cewu Lu; Chuan Wen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10534) · [Code](https://github.com/yanwen-zou/Roboprompt) · [Project](https://yanwen-zou.github.io/Roboprompt-Website/)
- Tags: human-in-the-loop, policy-steering, sparse-prompt, diffusion, DAgger
- Model size: 0.77B（Phase I steering model；下流方策は別）
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

人が画像上の点・軌跡や粗い方向を示すと、補助VLAが行動案へ変換し、既存のdiffusion/flow方策がnoise空間で修正する。基盤方策にsteerability訓練を加えず、人の意図と方策priorを調整する。介入付き成功軌跡を時間重み付き最適輸送で選び、DAggerによる方策改善にも使う。

**主な貢献**

同じsteering moduleをDiffusion Policy・π0.5・FastWAMに接続。3課題のπ0.5ではDAgger後の平均課題進捗80.0→95.5%と平均介入2.86→1.60を報告し、自律的zero-shot成功とは区別する。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.10534v1 （III-A〜C補助module訓練・noise制御・TOT、IV実機とDAgger、V限界）。限界: Phase Iは同一robotの500 play-data軌跡で訓練しており、補助モデルまで訓練不要ではない。エンドエフェクタ姿勢のsteering中心で多指handは未対応。人の介入を含む課題進捗指標。 公式projectからrepoを確認。steering/Web UI/Phase I実装が公開、root一覧とpyproject.tomlで新規実装LICENSEは確認できずunspecified。READMEは https://huggingface.co/datasets/ywzou/Roboprompt\_Play\_Data のckpt/evo1\_fullとckpt/pi05\_toasterを示すが、HF本体・tree/APIは本確認でアクセス不能、weight存在と配布条件を独立確認できずunknown。具体的追補: HF checkpoint一覧・model/dataカードと新規steering実装LICENSEを確認する。

### Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models

- ID: `VLA-0175`
- Published: 2026-10-07
- Authors: Mikey Watts; Yuchen Cui
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10526) · [Code](https://github.com/sttawm/phrase-rl) · [Project](https://sttawm.github.io/rephrase-before-you-act/)
- Tags: language-sensitivity, instruction-rephrasing, frozen-policy, SIMPLER, LIBERO
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

指示の単語や表記の小さな変更がVLAの成功率を大きく変える現象を調べ、複数課題の実行結果からLLMで言い換え規則を抽出する。推論前に指示を一度だけ書き換え、方策の重みを変えずに未使用課題へ適用する。SIMPLERの12課題とLIBEROで評価した。

**主な貢献**

実行証拠を10〜20の明示的な言い換え規則に圧縮する訓練不要の入力適応。π0の改善16〜27%は相対値で、π0.5のLIBERO内分布成功率93.6→97.8%とは別の評価。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.10526v1 （IV-B統計と曖昧性除外、V手法、VI-D〜F評価、VII結論）。限界: 2種類のVLA・シミュレーションのみ。単語差の検定には多重比較補正がなく、非実行課題ではgripper誤差を代理指標に使う。開始前の2モデル呼び出し時間も必要。 公式projectがリンクするコードrepoを確認し、src/phrase\_rlとscriptsが公開。root一覧・READMEで実装ライセンス表記を確認できずunspecified、open\_source=unknown。論文がリンクする再利用資料repo https://github.com/sttawm/vla-rephrasing-artifacts とは区別。新規モデル重みは未確認。

### Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization

- ID: `VLA-0173`
- Published: 2026-10-07
- Authors: Haoru Li; Jinmei Liu; Zhiyong Wang; Xiaoming Li; Zhenhong Sun; Daoyi Dong; Chunlin Chen; Zhi Wang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09943)
- Tags: DRIVE, reinforcement-learning, behavioral-diversity, OOD-generalization, bimanual
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

RLによるVLA後学習で成功軌跡の多様性を増やすDRIVEを提案する。同じ課題・初期条件の軌跡をVLM特徴と時間整列で比較し、成功した軌跡だけに相対的な多様性報酬を加える。3つのシミュレーション系と双腕実機の2課題で分布外条件を評価した。

**主な貢献**

失敗の多様化を報酬化せず、成功モードの被覆を後学習目的にする。通常RL後学習に対するOOD平均改善はπ0で5.3ポイント、π0.5で2.0ポイント、実機のOOD条件平均は64.1→73.3%。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09943v1 （4.1〜4.3手法、5.1分布分割と比較、5.3実機、6限界）。限界: 組内の軌跡対GAK比較に追加計算が必要で、VLM特徴が意味のある戦略差を捉えることに依存する。実機はClick BellとPress Stapler、各条件20試行。長期課題・多様な身体・実機オンライン学習は未検証。 一次arXiv本文の提供リンクと題名・著者を限定した公開検索では、公式実装・独自checkpoint・実装LICENSEの提供を確認できず、別々にunknownとした。存在しないと断定したものではない。

### Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models

- ID: `VLA-0170`
- Published: 2026-10-07
- Authors: Jiho Lee; Jeongeun Park; Heayoun Choi; Taekyung Kim; Eunwoo Kim
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09496)
- Tags: SOUL, state-hallucination, sparse-autoencoder, policy-unlearning, LoRA
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

掴めていない物体を運ぶなど、未達状態を達成済みとして動くVLAのstate hallucinationを分析する。SAEで視覚領域別の内部特徴を分解し、hallucinationに関連する特徴を抑え、成功に関連する特徴を残すSOULを提案する。OpenVLAとπ0.5、シミュレーションとFranka実機で評価した。

**主な貢献**

失敗分析で得たsparse featureをpolicy unlearningの忘却・保持対象にする。選んだLIBERO-Plus課題のhallucination failure60→38%、overall success26→58%、RoboCasaも改善を報告。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09496v1 （III定義・領域別SAE分析、IV忘却/保持loss、V-A〜C評価・実機・ablation、VI結論）。限界: 選定したpick-and-placeに限定。simulation maskと実機の手動領域注釈、成功/幻覚失敗rollout分類が必要で、長期・多様な操作にそのまま適用できるとは未検証（評価範囲からの留保）。 一次arXiv本文の提供リンクと題名・著者を限定した公開検索では、公式実装・独自checkpoint・実装LICENSEの提供を確認できず、別々にunknownとした。存在しないと断定したものではない。

### TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks

- ID: `VLA-0169`
- Published: 2026-10-07
- Authors: Zirun Zhou; Jingfeng Zhang; HaoChuan Xu; Xizhe Zhang; Elliott Wen; Jing Sun; Hong Jia
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09462)
- Tags: backdoor-defense, runtime-detection, latent-transitions, unseen-tasks, security
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

良性rolloutでinput tokenの分布と隣接層のlatent遷移を学ぶTMTを提案する。既知課題で統計基準により確認したincidentから固定監視遷移を選び、その後の未知課題でbackdoor発動を検出する。3種のbackdoorと既存検出器、WidowX実機で評価し、良性入力の行動を教師とするpolicy自己蒸留も探索した。

**主な貢献**

input分布異常と層間遷移誤差を組み合わせ、detector学習にtrigger例やclean reference policyを使わず、既知課題でのscore-confirmed incidentから監視遷移を選ぶ。その選択後の実機GoBA評価はTDR100%・FRR0%（RNDも同値）、未知DropVLAはTDR73.6%。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09462v1 （3脅威/defender前提、4 detector、5自己蒸留、6.1〜6.5評価・実機・ablation、Appendix F）。段階条件を再確認: https://arxiv.org/html/2610.09462v1\#S4.SS3 と https://arxiv.org/html/2610.09462v1\#A6 。detector predictorはverified benign rolloutで学習するが、訓練/referenceに含まれる既知課題で追加rolloutを実行し、token-manifold scoreとrollout-wide latent-deviation基準で確認したincidentから最大standardized excessの遷移を選ぶ。score-confirmedとは外部のmalicious labelではなく統計基準による確認。選択後にheld-out benign rolloutで監視閾値を較正し、固定遷移を未知課題で監視する。未知課題の結果はincident-driven selection後の評価であり、incident不要の初期cold-start保証ではない。限界: 内部activationと信頼できる良性referenceが必要。実機は4課題中2課題で学習・2課題でGoBA評価。誤検出ゼロは評価標本内の結果で一般保証ではなく、purificationは予備評価。公式project https://zzr42.github.io/tmt/ はHTTP404、project\_urlを空欄とし独自コード・重み・LICENSEはunknown。具体的追補: 著者の公式公開先で移転/公開状況を確認し、正しいproject URL・実装・checkpoint配布条件を補う。

### Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models

- ID: `VLA-0156`
- Published: 2026-10-05
- Authors: Zaibin Zhang; Binghao Ran; Yuhan Wu; Zhongbo Zhang; Yifan Wang; Junwei Jiang; Junlan Xiao; Wangcheng Shi; Li Kang; Yiran Qin; Zhenfei Yin; Lijun Wang; Huchuan Lu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06184)
- Tags: ACG-Bench, AE-VLA, bimanual, compositional-generalization, SkillLoRA, arm-wise-attention
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

双腕の既知原子スキルを新しい順序・同期・タスクの組合せで再利用するACG-Benchを導入。共通π0.5に腕別token、SkillLoRA、腕別attentionを追加したAE-VLAを、同じデータ・指示で比較する。

**主な貢献**

17未見条件の制約順守成功率はAE-VLAが21.53%、独立Dual π0.5が5.53%。実機SO101の5未見条件では39.00%対10.00%。成功には目標達成に加えて順序・同期・milestoneを満たす必要がある。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-10-05 12:03:04 UTC、改訂なし。本文 https://arxiv.org/html/2610.06184v1 の§3–6とAppendix Bを選択読解。評価は供給されたper-arm原子prompt/skill構造下の実行で、novel-task plannerは提案していない。純同期とin-domain性能は課題。SkillLoRAは追加重みとrouter supervision、AWAは腕間と時間attentionの両方を変える。公式実装・重み・ライセンスは未確認。

### VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models

- ID: `VLA-0154`
- Published: 2026-10-05
- Authors: Jaemin Kim; Jiahn Kim; Taesik Gong
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06271)
- Tags: VLA-ZO, zeroth-order-optimization, one-shot-adaptation, prefix-cache, prefetch, camera-shift
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

forward計算だけのzeroth-order適応を、VLAの計算構造に合わせて高速化する。行動側だけを更新し、凍結した視覚言語prefixの条件状態を摂動query・更新step間で再利用し、prefetchで転送を隠す。

**主な貢献**

π0.5のLIBERO視点変化で、cold cacheを含む適応時間を同じquery数のbaseline ZOに対しq=16で25.59倍、q=64で32.54倍短縮。未適応の48.27%に対し成功率は58.17%・63.58%。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-10-05 13:05:34 UTC、改訂なし。本文 https://arxiv.org/html/2610.06271v1 の§3–5、Appendix Aを選択読解。π0.5とOpenVLA-OFT、LIBERO 40タスク、sceneごとに1デモの計5デモで適応。seed=0、実機検証は未確認。比較のFLA/DARTは著者のZO-SGD置換実装であり元の一階法との同等比較ではない。公式実装・専用重み・ライセンスURLは未確認。

### How (and How Not) to Use Data Augmentation in VLA Post-Training

- ID: `VLA-0152`
- Published: 2026-10-05
- Authors: Bram Grooten; Joaquin Vanschoren
- Venue: NeurIPS 2026 RoboPAD workshop
- Links: [Paper](https://arxiv.org/abs/2610.05994) · [Code](https://github.com/bramgrooten/vla-augm) · [Project](https://bramgrooten.nl/vla-augm/)
- Tags: RL-post-training, critic-only-augmentation, visual-OOD, PPO, π0.5, GR00T-N1.5
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

VLAのPPO後学習で、画像拡張をactor・criticのどこへ入れるべきかを比較する。rollout時は元の画像を使い、更新時のcriticだけにoverlayまたはshiftを与える構成が視覚分布外への汎化を改善した。

**主な貢献**

LIBERO-Plusの5視覚軸の非加重平均で、π0.5はoverlayにより73.9%から81.7%、GR00T N1.5はshiftにより66.0%から76.0%へ改善。actorの拡張は両モデルで学習を崩した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-10-05 08:48:13 UTC、改訂なしをarXivで確認。NeurIPS 2026 RoboPAD workshop採択はarXiv著者commentと公式author projectの記載で確認し、publisher proceedingsは未確認。本文 https://arxiv.org/html/2610.05994v1 の§3–6を選択読解。シミュレーション、LIBERO-Spatial/PPO、各構成1学習seedに限定。公式projectから実装を確認し、augmentation.pyとApache-2.0 LICENSEを別々に確認: https://github.com/bramgrooten/vla-augm/blob/main/LICENSE 。専用重みの配布先は未確認。

### ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation

- ID: `VLA-0150`
- Published: 2026-10-02
- Authors: Sangwu Park; Yeonjun In; Wonjoong Kim; Sungwon Kim; Sein Kim; Chanyoung Park
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02802) · [PDF](https://arxiv.org/pdf/2610.02802) · [Code](https://github.com/sangwu99/ManiPhysicsBench_Arxiv)
- Tags: supporting-evaluation, object-preservation, physics-assessment, gripper-supervision, FEM, simulation
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / unknown / unknown

**概要（日本語）**

文献に基づく材料特性と形状をまとめたManiPhysicsZooと、把持位置・接触力から損傷閾値を求める物理solver評価を提案。LIBEROとSimplerEnvの剛体rollout後に、タスク達成と物体保持を分けて評価する。VLAの把持指令分析と連続gripper教師による再学習を通じ、成功しても物体を守れない問題を調べる。

**主な貢献**

3種類の物理応答と3難度の評価を、把持ごとの材料・形状依存損傷判定へ接続。SimplerEnvの高・中難度では公開checkpoint平均の成功48.3%に対しSafe SRは13.5%。連続教師による再学習ではSafe SRが改善する一方でタスク成功が低下し、材質差への一般化は限定的。損傷はシミュレーション後の予測で、実機安全を実証した結果ではない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- arXiv v1初稿2026-10-02 04:49:46 UTC・著者・履歴を確認。HTML https://arxiv.org/html/2610.02802v1 の3–7節とreproducibility statement、App.F.2を確認。各model/objectは12 episodes、平均数値は3軸のHigh/Mid対象。再学習はBridge-only/LoRAで公開Bridge–RT-1 checkpointと訓練条件が異なり、教師ラベル差の単独因果比較ではない。把持のみのoffline損傷予測で、落下/衝突や変形後feedbackは含まず、実機による直接検証は今後。本文がリンクする公式README、targets.py、pyproject.tomlとmodels.jsonを確認。実装は公開、確認head db717ec0 の414-file treeはtruncated=falseで、見つかったlicenseはthird\_party/vendor用のみ。root LICENSEは404かつpyprojectにlicense指定なし。上流依存のライセンスから推定せず実装license/open\_sourceはunknown、専用再学習重みの公開も未確認。PDF URLはabsリンクのみ確認、PDF未取得。

### MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models

- ID: `VLA-0147`
- Published: 2026-10-02
- Authors: Pingrui Zhang; Yu Zhang; Pengyuan Wu; Bin Wang; Haoming Song; Xianqiang Gao; ZhaxiZhuoma; Zhigang Wang; Dong Wang; Bin Zhao; Xuelong Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.02898) · [PDF](https://arxiv.org/pdf/2610.02898)
- Tags: ood-generalization, invariant-representation, feature-mixing, information-bottleneck
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

情報bottleneckで不変表現を学び、重み差から得た非不変表現を確率的に混合して行動予測へ再統合するモデル非依存の学習法。環境特有の手掛かりを全て捨てず、予測に有用な情報を残しつつ相関への過依存を抑える。

**主な貢献**

OpenVLA-OFTとπ0.5に適用し、追加OOD学習データなしでLIBERO-Plusの全体成功率76.2%（比較OpenVLA-OFT 69.6%）を報告。RoboTwinのclean-to-randomized評価と実機照明変動も検証し、単一学習履歴を再利用するSelf-MixVLAを探索した。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- identity照合一致なし。v1: https://arxiv.org/abs/2610.02898 (2026-10-02 06:44:43 UTC、改訂なし)。HTML §3/4/App.D選読: https://arxiv.org/html/2610.02898v1 。camera変動では49.6%と比較OpenVLA-OFT 56.4%を下回り、全変動で優位ではない。App.Dは大きな幾何変動への限界を明記。実機Frankaの照明変動定量は1課題2条件各5試行で60%対20%、広範な実機一般化と断定しない。abs/HTMLと手法名github検索では公式実装・重み・project・実装ライセンス未確認、unknown。論文CC BY-NC-SAを実装に転用しない。PDFファイル未保存。

### FastOPD: On-Policy Distillation for Lightweight VLA Deployment

- ID: `VLA-0145`
- Published: 2026-10-02
- Authors: Yoojin Oh; Jeongsol Kim; Yeonwoo Seo; Jangho Park; Seonghyun Jin; Sunwoo Park; Youngmin Kim; Youngjun Jun; Kyumin Choi; Jong Chul Ye
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.02832) · [Project](https://fastopd.github.io/)
- Tags: on-policy-distillation, flow-map, few-step, efficient-inference, wam-teacher
- Model size: 451M (student)
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

大規模VLAから小さなfew-step方策へ知識を移すon-policy蒸留。学生が到達した一つの状態だけで教師の速度場を照会し、自己整合性損失で有限時間のflow mapに伝播する。視覚言語backboneを凍結し行動expertなどを調整する。

**主な貢献**

451M学生がLIBEROで2step・平均81.8%を達成し、π0.5教師97.5%の約84%を保持しながら推論latencyを78.1%短縮。LingBot-VLA教師ではRoboTwin 2.0の1step成功率が初期学生から15.9ポイント改善。WAM教師とMolmoAct2からの実機蒸留も検証。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- identity照合一致なし。v1: https://arxiv.org/abs/2610.02832 (2026-10-02 05:24:20 UTC、改訂なし)。HTML §3/4/5選読: https://arxiv.org/html/2610.02832v1 。教師依存の蒸留で、81.8%は教師と同じ成功率ではない。simulationはLIBERO/RoboTwin各task50試行、実機は1課題。損失重みが小さ過ぎると性能崩壊。公式 https://fastopd.github.io/ はCode (TBA)と表示、code unavailable。論文固有の重み公開・実装ライセンスは未確認でunknown、基盤学生/教師の公開とは分ける。451Mはtime projectionを追加した学生規模。PDFファイル未保存。

### eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing

- ID: `VLA-0149`
- Published: 2026-10-01
- Authors: Dehao Huang; Jianbang Liu; Jianpan Gao; Chao Tang; Zilang Cen; Zedong Dan; Jiaheng Wang; Tingguang Li; Yue Wang; Hong Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.00913) · [PDF](https://arxiv.org/pdf/2610.00913)
- Tags: frozen-VLA, online-RL, action-relevant-token, layer-routing, sample-efficiency, human-assisted-insertion
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結したVLAの複数層から行動に必要な特徴を学習済みrouting tokenで取り出し、軽量actor/criticへ渡すeRLT。実演の行動予測で初期化し、オンラインRLのcritic損失で表現を更新する。LIBERO・RoboTwinの7課題とRB-Y1実機の2挿入課題で、固定予算内の学習効率を評価した。

**主な貢献**

観測ごとのtoken集約とタスク内で共有する層重みを分離し、VLA本体を変えずにRL状態表現を適応する。7シミュレーション課題の平均正規化学習曲線AUCは0.626で、固定圧縮RLTの0.506、独立encoderの0.585を上回る。これは最終成功率の差ではない。実機のAUC改善は人手支援を含む収集条件に限定され、試行間変動と介入頻度の影響は未解決。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- arXiv v1初稿2026-10-01 01:43:42 UTC・著者・履歴を確認。HTML https://arxiv.org/html/2610.00913v1 の4–6節、App.C.3/C.4/C.6とD.1/D.2を確認。実機は80/90収集軌跡にwarm-upと5連続失敗後の人手支援を含み、支援数は方策成績に依存。USB 108.9%とribbon 46.7%はAUCの相対改善で成功率percentage pointsではない。本文のRLinfリンクは上流であり専用公開実装と扱わない。題名・著者名・code検索と本文で専用実装・重み・実装ライセンス未確認。PDF URLはabsリンクのみ確認、PDF未取得。

### Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks

- ID: `VLA-0137`
- Published: 2026-10-01
- Authors: Sophie Higham; Riccardo Andrea Izzo; Matteo Matteucci; Alessandro Suglia
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01351) · [Project](https://github.com/esgi-research-group/vla-reliability)
- Tags: supporting-evaluation, behavioural-robustness, input-perturbations, trajectory-metrics, reliability
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

成功したVLA軌跡に限定して、入力摂動による滑らかさ・移動距離・グリッパ挙動とそのばらつきを測る評価手法。成功率だけでは隠れる行動変化をLIBEROとLIBERO-Plusで調べる。

**主な貢献**

軌跡指標の典型値変化とMADによるばらつきを区別し、統計検定とFDR補正を適用。π0.5とVLANeXtは四スイート、OpenVLA-OFTはSpatialだけを評価し、実機での効果と失敗軌跡は検証範囲外。

**確認記録**

- Checked: 2026-10-02 · Review: needs-review
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.01351v1 のIII–IV節・VI節を確認。本文はfull code availableと記載するが公式repo default branch initial-setupはREADMEのみで、READMEは公開を論文出版後と明記。確認時の研究実装はunavailableとしcode\_urlは空欄、公開状態の不整合をneeds-reviewに保持。重み・実装ライセンスはunknown。新規VLA方策ではなく評価の支援研究。PDF未取得。

### ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing

- ID: `VLA-0135`
- Published: 2026-10-01
- Authors: Zhugang Liu; Kaichuang Zhang; Jinman Zhang; Pu Sun; Martha Asare; Jose Hernandez; Maxim Ermolinsky; Efren Saenz; Qi Lu; Jinghao Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01856)
- Tags: embodiment-adaptation, action-chunking, manufacturing, LoRA, cloud-edge
- Model size: OpenVLA-OFT 7B backbone
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

OpenVLA-OFTをFAIRINO FR3の固定製造セルへ適応させるデータ変換・LoRA・実行パイプライン。単眼デモをTFDS/RLDSへ揃え、遠隔推論で得た8ステップの行動チャンクを実行後に再観測する。

**主な貢献**

座標系・行動正規化・チャンク実行の整合を具体化し、実機の対象物移送42試行で39成功を報告。並列ホスト推論は実機評価に使われず、適応とチャンク長の効果は単独で分離されていない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXivのv1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2610.01856v1 のIV節、V節の実機・照明評価を読んだ。固定セルの赤/青ブロック移送は汎用製造能力の実証と区別。実装・専用重み・実装ライセンスの公式提供先は本文リンクとタイトル検索で未確認。PDF未取得、正確なPDF href未抽出のためpdf\_urlは空欄。

### Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

- ID: `VLA-0138`
- Published: 2026-09-30
- Authors: Mingyue Cui; Zheyuan Liu; Yihan Zhu; Zheyuan Zhang; Meng Jiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39820) · [Code](https://github.com/Mingyuee88/FailBank) · [Project](https://mingyuee88.github.io/FailBank/)
- Tags: FailBank, self-evolution, failure-bank, observe-only-teacher, guarded-LoRA, safety
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

方策が実行した行動へ観察専用CBF教師の反事実的補正を記録し、結果で選別した失敗バンクと成功行動のアンカーからLoRAを更新するFailBank。検証損失と行動ドリフトのガードを満たす更新だけを採用する。

**主な貢献**

一時的なランタイム制約を永続的な方策学習信号へ変える四段階手順。VLA-Arenaの静的障害物二難度・π0/π0.5で成功率と方策由来接触コストを併記し、平均改善を全課題や動的障害物の安全保証とは扱わない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.39820v1 の4節・5.2節・6.3節を確認。収集教師は特権シミュレータ形状を使い、展開方策には不要。公式project経由のsrc実装・READMEとroot Apache-2.0を確認: https://github.com/Mingyuee88/FailBank/blob/main/LICENSE 。第三者成分は別条項。READMEのVLA-Arena重みは基礎方策でありFailBank専用adapterの提供を確認できずweights\_status=unknown。PDF未取得。

### Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

- ID: `VLA-0162`
- Published: 2026-09-29
- Authors: Ruixiao Xu; Wong Lik Hang Kenny; Zhiqian Liu; Jianing Guo; Hanxiao Li; Kejian Shi; Shuning Zhang; Pu Feng; Yongjia Ma; Yuqing Ma; Kai Chen; Qi Dou; Yaodong Yang; Xianglong Liu; Simin Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.36588) · [Code](https://anonymous.4open.science/r/mavla_rft-2BC0/)
- Tags: cooperative-MARL, reinforced-finetuning, agent-wise-credit, latent-noise-RL, multi-robot, π0.5
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

失敗する初期配置で人間デモを補う収集、agent別advantageで軌跡を選ぶoffline微調整、凍結VLAのlatent noiseを学ぶonline RLの3段階で協調制御を後学習する。各ロボットは局所画像・状態と共通画像・指示を入力する。

**主な貢献**

π0/π0.5でRoboTwin 4課題、RoboFactory 4課題、実機Franka 3課題を評価。CHORUSのSFTに対する平均成功率増は各群で23.1・16.4・44ポイント。実機online段階は50rolloutのproof-of-concept。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-09-29 03:05:50 UTC、改訂なし。本文 https://arxiv.org/html/2609.36588v1 の§4–6とAppendix Aを選択読解。multi-agentは低レベルMARLの方策主体でLLM plannerではないためvla/adaptation。単調改善の命題は正確なadvantageとデータsupport等の仮定下のみ。公式anonymous repoリンクを開いたがreadable fileが返らず、実装・重み・ライセンスの実体は未確認でunknown。

### VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL

- ID: `VLA-0161`
- Published: 2026-09-25
- Authors: Namiko Saito; Kinam Kim; Heecheol Kim; Katsushi Ikeuchi; Yasuyuki Matsushita
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.30868)
- Tags: VLaRL, residual-RL, sim-to-real, latent-alignment, contact-rich, force-feedback
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

実機デモで微調整したVLAを凍結し、simulation latentを実機latentへ整合するmapperを学習する。mapped latent・VLA行動・固有感覚・力から残差RLをsimulationで学び、実機ではmapperなしで修正行動を出す。

**主な貢献**

Franka Research 3の接触4課題、FlowerとGR00T N1.7の全8組合せで実機成功率が改善。Flowerのbutton pressingは67.5%から100%、block pushingは22.5%から50%。実機でRLやonline適応を行わず転移を評価した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-09-25 06:18:40 UTC、改訂なし。本文 https://arxiv.org/html/2609.30868v1 の§III–VI-Cを選択読解。実機デモ32件/task、各実機条件40trial。task別digital twinと概ね対応するsim–real軌跡が必要で、実機データ不要ではない。mapperはbackbone別、残差方策はtask別。摩擦・contact dynamics差は直接補正せず、未知物体評価も限定的。検索で見つかったGuanxingLu/vlarlは著者・題名が違う別研究。公式専用実装・重み・ライセンスは未確認。

### Self-Adaptive VLA for Robust Robot Deployment

- ID: `VLA-0123`
- Published: 2026-09-24
- Authors: Hongxin Zhang; Chunru Lin; Tsun-Hsuan Wang; Zhenjia Xu; Chuang Gan
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.30092) · [Project](https://icefoxzhx.github.io/self-adaptive-vla/)
- Tags: test-time-adaptation, hardware-shift, context, bimanual
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

駆動バイアスや関節エンコーダーのずれに対し、自身の試行履歴を文脈トークンへ圧縮してVLAを補償する事後学習法。複数試行のトークンを統合し、配備先で反復的に補正する。

**主な貢献**

既存の専門家デモを既知の機器ずれに事前補償し、軽量文脈エンコーダーとAdaLNを学習。精密な双腕・器用操作4タスクで性能回復を報告。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Official project videos/method and primary HTML https://arxiv.org/html/2609.30092v1 checked; no research code repository, implementation license, or trained weight download verified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### BEE: Intervention-Adaptive Real-World Reinforcement Learning with Vision-Language-Action Models

- ID: `VLA-0160`
- Published: 2026-09-23
- Authors: Weihui Zhao; Xiaohan Yan; Zunian Wan; Xuan Du; Zhaozhan Chi; Jianbo Mao; Ruipu Wu; Rushuai Yang; Houlin Li; Shukai Yang; Jing Wu; Yuxiang Yan; Yongcheng Liu; Chuankang Li; Guanghui Ren; Wei Shan; Maoqing Yao
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.27450)
- Tags: BEE, human-intervention, residual-RL, correction-uncertainty, real-robot, π0.5
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結VLAの提案と人間の修正を対で保持し、修正の平均・分散を次元別に学ぶCorrection Modelを導入する。一貫した修正方向では方策を強く拘束し、ばらつく方向は緩めて残差RLを進める。

**主な貢献**

実機3課題とLIBERO-Pro 1課題の固定online-data予算で平均成功率91.2%、RLT 57.5%、DSRL 42.1%。この平均はphone charging・cloth aligningの精密段階の成功率と、残る2課題の全体成功率を混在させた値。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-09-23 07:14:20 UTC、改訂なし。本文 https://arxiv.org/html/2609.27450v1 の§IV–VとAppendix D/Eを選択読解。π0.5をtaskごとにBC微調整後凍結。3評価round各20trial。human intervention率は訓練control-step比率で、評価時介入なし。RLTは著者再実装、from-scratch比較は小予算に限定。学習制約は安全保証とは扱わない。公式実装・専用重み・ライセンスURLは未確認。

### Dissecting Advantage-Guided Post-Training for Vision-Language-Action Policies

- ID: `VLA-0128`
- Published: 2026-09-23
- Authors: Jiahang Cao; Hanye Zhao; Hang Lai; Shenyu Zhang; Xiaoshen Han; Xinghang Li; Futeng Liu; Wanli Peng; Heyun Wang; Yunhong Wang; Jason Li; Yong Yu; Weinan Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.28161) · [Project](https://dissectvla.github.io/)
- Tags: post-training, advantage-weighting, offline-diagnostics, bimanual
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VLAの優位度に基づく事後学習を、優位度構成・尺度校正・方策利用の3段階に分解する制御比較。実機評価の前に候補を選べる段階別オフライン診断を導入する。

**主な貢献**

TD優位度、グループ別校正、連続重み付けの組合せを識別。固定データ・方策・予算による4双腕タスクの比較で診断と実機性能の整合性を調べる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.28161v1 directly links verified project https://dissectvla.github.io/. Project contains videos and study details, no verified research code or trained weight release; website template/website CC license is not an implementation license. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

- ID: `VLA-0143`
- Published: 2026-09-22
- Authors: Zeyu Lou; Tianran Zhang; Xinquan Yue; Ya Jing; Chenyang Si
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.26313) · [Code](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop)
- Tags: execution-safety, hazard-prediction, rollback, safe-waypoint-memory, frozen-VLA, asymmetric-PPO
- Model size: Qwen2.5-VL-3B predictor backbone; total parameters unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

凍結VLAへ外付けの危険予測と復帰制御を加える。身体・物体の危険確率と発生までの時間を推定し、低頻度PPO制御器が続行・安全地点記録・関節空間rollbackを選ぶ。

**主な貢献**

24 LIBERO課題×16seed、実機三課題×25試行で安全性と成功率を比較。実機は予測器を適応しdeciderをそのまま移す。安全地点は予測閾値に基づき形式保証ではなく、不可逆な物体変化は戻せない。公開releaseはPi0向けで訓練データは含まれない。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿2026-09-22 12:22:44 UTC、改訂なし。arXiv commentsはIROS 2026受理を記載するが、会議側では独立確認していない。HTML §III–V確認: https://arxiv.org/html/2609.26313v1 。公式release/safeloop実装とApache-2.0 LICENSE確認: https://github.com/Loule0-0/SafeLoop/blob/release/safeloop/LICENSE 。HF公開head重み・Apache-2.0カード確認: https://huggingface.co/Jaqen0-0/SafeLoop/tree/main/decision\_heads 。pi0-v1の8ファイルmanifest: https://github.com/Loule0-0/SafeLoop/blob/release/safeloop/configs/release/artifacts\_pi0\_v1.json 。重み未ダウンロードでchecksum自体は未検証。基盤モデルは別ライセンス。PDF未取得。

### RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy

- ID: `VLA-0142`
- Published: 2026-09-22
- Authors: Chongyu Zhu; Jaden Hinds; Hyegang Kim; Juan Sebastian Rojas; Ramy Elmallah; Chi-Guhn Lee
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.26467)
- Tags: RL-specialist, controller-routing, SmolVLA, action-chunk, precision-control, operator-aligned-handoff
- Model size: SmolVLA backbone; total router/specialist parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結SmolVLAの潜在表現から担当制御器を推定し、精密段階だけRL専門方策へ切り替える。ヒステリシス等で切替を安定化し、担当変更時に古いaction chunkの未実行部分を破棄する。

**主な貢献**

LIBERO Object三課題・60保持試行・三学習seedで全課題成功85.00%から92.22%。実機挿入は6.7%から35.0%だが、挿入開始前に操作者が位置合わせする。大規模専門方策群・完全自律の多専門方策合成・他の幾何形状は未検証。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿2026-09-22 14:15:28 UTC、改訂なし。arXiv commentsはIROS 2026 IARL Workshop受理を記載するが、会議側では独立確認していない。HTML §III・IV・Vで手法・評価・制約を確認: https://arxiv.org/html/2609.26467v1 。実機はRouteRLT20試行、対照30試行。phaseラベル・専門方策学習にはprivileged境界を使用し、実行時router入力には使わない。本文と著者/手法名検索で公式公開実装・重み・実装ライセンス・独立project未確認。PDF未取得。

### Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

- ID: `VLA-0122`
- Published: 2026-09-20
- Authors: Shuaijun Liu; Feiyang You; Chengyu Wu; Shuyang Hao; Chenglong Zhang; Jingyao Cai; Xingwei Chen; Ningxin Su
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.23650) · [Code](https://github.com/NEBULIS-Lab/Beyond-Appearance-Shifts) · [Project](https://nebulis-lab.com/Beyond-Appearance-Shifts/)
- Tags: semantic-calibration, frozen-vla, robustness, residual
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

見た目だけが変わる条件と、対象物や制約が変わる条件を区別し、凍結VLAの出力行動を補正するBAS-VLA。意味変更後に旧タスクを続ける失敗を抑え、外観変動への頑健性も評価する。

**主な貢献**

意味変更を中心とした残差キャリブレーターと、意味の一貫性を確認した場合だけ有効化する補助経路を統合。旧タスク抑制と新タスク達成を別指標として評価。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Official project links official GitHub. Actual bas\_vla implementation, training/evaluation scripts and LICENSE are present; GitHub identifies MIT license. Root LICENSE content independently read via GitHub connector and confirmed standard MIT: https://github.com/NEBULIS-Lab/Beyond-Appearance-Shifts/blob/main/LICENSE . README requires separately supplied carrier and adapter weights; public adapter download unverified. Project/repository claim NeurIPS 2026, but organizer acceptance not independently checked. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models

- ID: `VLA-0133`
- Published: 2026-09-18
- Authors: Kaiwen Zhu; Dongfang Liu; Liangkai Liu
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.21246)
- Tags: failure-prediction, ood, execution-history, reliability
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

入力の分布外変化を検出・分類し、行動履歴と実行進捗を組み合わせてVLAの失敗確率を更新するVLA-Scope。OpenVLAのLIBERO-Spatial10タスクで評価する。

**主な貢献**

分布外入力と実行失敗を同一視せず、共有ロジスティック回帰で履歴依存の失敗予測を行う。1400分布外試行で進捗特徴の効果を比較。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.21246v1 checked for author-owned implementation/license or weight links; none verified. CC Zero shown on arXiv is the paper license, not evidence of released implementation. This is a reliability framework rather than a new generalist action backbone. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### OpenVLA: An Open-Source Vision-Language-Action Model

- ID: `VLA-0104`
- Published: 2024-06-13 · Updated: 2024-09-05
- Authors: Moo Jin Kim; Karl Pertsch; Siddharth Karamcheti; Ted Xiao; Ashwin Balakrishna; Suraj Nair; Rafael Rafailov; Ethan Foster; Grace Lam; Pannag Sanketi; Quan Vuong; Thomas Kollar; Benjamin Burchfiel; Russ Tedrake; Dorsa Sadigh; Sergey Levine; Percy Liang; Chelsea Finn
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2406.09246) · [PDF](https://arxiv.org/pdf/2406.09246) · [Code](https://github.com/openvla/openvla) · [Project](https://openvla.github.io/)
- Tags: OpenVLA, generalist-policy, parameter-efficient-finetuning, quantization, cross-embodiment
- Model size: 7B
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

97万件の実機軌跡で学習した7BのVLAを公開。DINOv2とSigLIPの視覚特徴をLlama 2へ接続し、複数ロボット制御と新環境への微調整を評価した。LoRAと量子化による利用コスト削減も検証した。

**主な貢献**

公開の汎用VLAと、消費者向けGPUでの効率的な適応・推論手順を一体化。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。重み: https://huggingface.co/openvla/openvla-7b 。コードMITと基盤Llama 2の利用条件は別。 Code license: MIT; https://github.com/openvla/openvla/blob/main/LICENSE.

### Octo: An Open-Source Generalist Robot Policy

- ID: `VLA-0105`
- Published: 2024-05-20 · Updated: 2024-05-26
- Authors: Octo Model Team; Dibya Ghosh; Homer Walke; Karl Pertsch; Kevin Black; Oier Mees; Sudeep Dasari; Joey Hejna; Tobias Kreiman; Charles Xu; Jianlan Luo; You Liang Tan; Lawrence Yunliang Chen; Pannag Sanketi; Quan Vuong; Ted Xiao; Dorsa Sadigh; Chelsea Finn; Sergey Levine
- Venue: RSS 2024
- Links: [Paper](https://arxiv.org/abs/2405.12213) · [PDF](https://arxiv.org/pdf/2405.12213) · [Code](https://github.com/octo-models/octo) · [Project](https://octo-models.github.io/)
- Tags: Octo, generalist-policy, diffusion-policy, goal-conditioning, cross-embodiment
- Model size: 27M (Small); 93M (Base)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

80万軌跡から事前学習したTransformerベースの汎用ロボット方策。言語または目標画像で指示し、新しいセンサー入力や行動空間へ少量データで適応できる設計を9種類のロボット環境で評価した。

**主な貢献**

柔軟な観測・タスクトークン化と拡散行動ヘッドにより、ロボットごとの入出力変更へ効率的に適応。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式プロジェクトにモデル規模とRSS 2024書誌、Hugging Face重みへのリンク。 Code license: MIT; https://github.com/octo-models/octo/blob/main/LICENSE.

### Open X-Embodiment: Robotic Learning Datasets and RT-X Models

- ID: `VLA-0103`
- Published: 2023-10-13 · Updated: 2025-05-14
- Authors: Open X-Embodiment Collaboration; Abby O'Neill; Abdul Rehman; Abhinav Gupta; Abhiram Maddukuri; Abhishek Gupta; Abhishek Padalkar; Abraham Lee; Acorn Pooley; Agrim Gupta; Ajay Mandlekar; Ajinkya Jain; Albert Tung; Alex Bewley; Alex Herzog; Alex Irpan; Alexander Khazatsky; Anant Rai; Anchit Gupta; Andrew Wang; Andrey Kolobov; Anikait Singh; Animesh Garg; Aniruddha Kembhavi; Annie Xie; Anthony Brohan; Antonin Raffin; Archit Sharma; Arefeh Yavary; Arhan Jain; Ashwin Balakrishna; Ayzaan Wahid; Ben Burgess-Limerick; Beomjoon Kim; Bernhard Schölkopf; Blake Wulfe; Brian Ichter; Cewu Lu; Charles Xu; Charlotte Le; Chelsea Finn; Chen Wang; Chenfeng Xu; Cheng Chi; Chenguang Huang; Christine Chan; Christopher Agia; Chuer Pan; Chuyuan Fu; Coline Devin; Danfei Xu; Daniel Morton; Danny Driess; Daphne Chen; Deepak Pathak; Dhruv Shah; Dieter Büchler; Dinesh Jayaraman; Dmitry Kalashnikov; Dorsa Sadigh; Edward Johns; Ethan Foster; Fangchen Liu; Federico Ceola; Fei Xia; Feiyu Zhao; Felipe Vieira Frujeri; Freek Stulp; Gaoyue Zhou; Gaurav S. Sukhatme; Gautam Salhotra; Ge Yan; Gilbert Feng; Giulio Schiavi; Glen Berseth; Gregory Kahn; Guangwen Yang; Guanzhi Wang; Hao Su; Hao-Shu Fang; Haochen Shi; Henghui Bao; Heni Ben Amor; Henrik I Christensen; Hiroki Furuta; Homanga Bharadhwaj; Homer Walke; Hongjie Fang; Huy Ha; Igor Mordatch; Ilija Radosavovic; Isabel Leal; Jacky Liang; Jad Abou-Chakra; Jaehyung Kim; Jaimyn Drake; Jan Peters; Jan Schneider; Jasmine Hsu; Jay Vakil; Jeannette Bohg; Jeffrey Bingham; Jeffrey Wu; Jensen Gao; Jiaheng Hu; Jiajun Wu; Jialin Wu; Jiankai Sun; Jianlan Luo; Jiayuan Gu; Jie Tan; Jihoon Oh; Jimmy Wu; Jingpei Lu; Jingyun Yang; Jitendra Malik; João Silvério; Joey Hejna; Jonathan Booher; Jonathan Tompson; Jonathan Yang; Jordi Salvador; Joseph J. Lim; Junhyek Han; Kaiyuan Wang; Kanishka Rao; Karl Pertsch; Karol Hausman; Keegan Go; Keerthana Gopalakrishnan; Ken Goldberg; Kendra Byrne; Kenneth Oslund; Kento Kawaharazuka; Kevin Black; Kevin Lin; Kevin Zhang; Kiana Ehsani; Kiran Lekkala; Kirsty Ellis; Krishan Rana; Krishnan Srinivasan; Kuan Fang; Kunal Pratap Singh; Kuo-Hao Zeng; Kyle Hatch; Kyle Hsu; Laurent Itti; Lawrence Yunliang Chen; Lerrel Pinto; Li Fei-Fei; Liam Tan; Linxi "Jim" Fan; Lionel Ott; Lisa Lee; Luca Weihs; Magnum Chen; Marion Lepert; Marius Memmel; Masayoshi Tomizuka; Masha Itkina; Mateo Guaman Castro; Max Spero; Maximilian Du; Michael Ahn; Michael C. Yip; Mingtong Zhang; Mingyu Ding; Minho Heo; Mohan Kumar Srirama; Mohit Sharma; Moo Jin Kim; Muhammad Zubair Irshad; Naoaki Kanazawa; Nicklas Hansen; Nicolas Heess; Nikhil J Joshi; Niko Suenderhauf; Ning Liu; Norman Di Palo; Nur Muhammad Mahi Shafiullah; Oier Mees; Oliver Kroemer; Osbert Bastani; Pannag R Sanketi; Patrick "Tree" Miller; Patrick Yin; Paul Wohlhart; Peng Xu; Peter David Fagan; Peter Mitrano; Pierre Sermanet; Pieter Abbeel; Priya Sundaresan; Qiuyu Chen; Quan Vuong; Rafael Rafailov; Ran Tian; Ria Doshi; Roberto Martín-Martín; Rohan Baijal; Rosario Scalise; Rose Hendrix; Roy Lin; Runjia Qian; Ruohan Zhang; Russell Mendonca; Rutav Shah; Ryan Hoque; Ryan Julian; Samuel Bustamante; Sean Kirmani; Sergey Levine; Shan Lin; Sherry Moore; Shikhar Bahl; Shivin Dass; Shubham Sonawani; Shubham Tulsiani; Shuran Song; Sichun Xu; Siddhant Haldar; Siddharth Karamcheti; Simeon Adebola; Simon Guist; Soroush Nasiriany; Stefan Schaal; Stefan Welker; Stephen Tian; Subramanian Ramamoorthy; Sudeep Dasari; Suneel Belkhale; Sungjae Park; Suraj Nair; Suvir Mirchandani; Takayuki Osa; Tanmay Gupta; Tatsuya Harada; Tatsuya Matsushima; Ted Xiao; Thomas Kollar; Tianhe Yu; Tianli Ding; Todor Davchev; Tony Z. Zhao; Travis Armstrong; Trevor Darrell; Trinity Chung; Vidhi Jain; Vikash Kumar; Vincent Vanhoucke; Vitor Guizilini; Wei Zhan; Wenxuan Zhou; Wolfram Burgard; Xi Chen; Xiangyu Chen; Xiaolong Wang; Xinghao Zhu; Xinyang Geng; Xiyuan Liu; Xu Liangwei; Xuanlin Li; Yansong Pang; Yao Lu; Yecheng Jason Ma; Yejin Kim; Yevgen Chebotar; Yifan Zhou; Yifeng Zhu; Yilin Wu; Ying Xu; Yixuan Wang; Yonatan Bisk; Yongqiang Dou; Yoonyoung Cho; Youngwoon Lee; Yuchen Cui; Yue Cao; Yueh-Hua Wu; Yujin Tang; Yuke Zhu; Yunchu Zhang; Yunfan Jiang; Yunshuang Li; Yunzhu Li; Yusuke Iwasawa; Yutaka Matsuo; Zehan Ma; Zhuo Xu; Zichen Jeff Cui; Zichen Zhang; Zipeng Fu; Zipeng Lin
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2310.08864) · [PDF](https://arxiv.org/pdf/2310.08864) · [Code](https://github.com/google-deepmind/open_x_embodiment) · [Project](https://robotics-transformer-x.github.io/)
- Tags: Open-X-Embodiment, RT-X, cross-embodiment, dataset-mixture, transfer
- Model size: 55B (RT-2-X)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

複数機関・22種類のロボットのデータを統一形式で集約し、RT-1-XとRT-2-Xを訓練。異なる身体の経験を混ぜることで、各ロボットの単独学習より有利になる正の転移を示した。

**主な貢献**

異種ロボットデータの標準化とクロスエンボディメント方策学習を、共有データとモデルで検証。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。open\_sourceは公開リポジトリの実装に対する判定。RT-1-Xの公開checkpointと非公開RT-2-Xを区別。https://github.com/google-deepmind/open\_x\_embodiment Code license: Apache-2.0; https://github.com/google-deepmind/open\_x\_embodiment/blob/main/LICENSE.
