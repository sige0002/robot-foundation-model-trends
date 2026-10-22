<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / dynamics

[← wam](README.md) · [CSV master](../papers.csv)

20 records · Published date 降順（同日 ID 降順）

### PhysiCalWorld: In-Context Physics Calibration for World Models

- ID: `WAM-0137`
- Published: 2026-10-21
- Authors: Yunhao Luo; Wentao He; Yinpei Dai; Hyelin Nam; Hongze Fu; Joyce Chai; Nima Fazeli; Jeong Joon Park
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.30125) · [PDF](https://arxiv.org/pdf/2610.30125) · [Code](https://github.com/physical-world/physical-world-release) · [Project](https://physical-world.github.io/)
- Tags: PhysiCalWorld, in-context-physics-calibration, latent-world-model, physics-descriptor, visual-planning
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

テスト環境での短い観測・行動クリップから物理特性を表す単一tokenを抽出し、行動条件付き潜在世界モデルの予測を校正する。物理ラベルやテスト時の重み更新を使わず、同じ環境のrolloutと視覚計画で記述子を再利用する。

**主な貢献**

DINO-WMとLeWMに軽量なcontext encoderを接続。物理条件を変える4つのシミュレーション環境で予測・計画を評価し、DINO-WMのPush-T計画成功率を53.3%から62.7%へ改善した。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absのv1履歴・全著者、HTML https://arxiv.org/html/2610.30125v1 §3–5と実験表、公式projectを確認。評価はPush-T/Reacher/BeerPong/FetchSlideのシミュレーション。物理条件別の軌跡group化、情報を含む探索prompt、episode内で定常な物理条件が必要。公式実装MIT: https://github.com/physical-world/physical-world-release/blob/main/LICENSE （GitHub file APIで本文確認）。重み: https://huggingface.co/physical-world/physical-world-checkpoints-release のmodel cardと14GB file treeを確認、重みライセンスはmodel cardのMIT表示のみ（別のLICENSE本文は未確認）。重み未ダウンロード、コード未実行。

### Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- ID: `WAM-0135`
- Published: 2026-10-20
- Authors: Zebin Xing; Yuhang Zheng; Yupeng Zheng; Yichen Zhang; Zichen Li; Shangqing Zhou; Yujie Zang; Yuchen Liu; Zhongpu Xia; Haoran Li; Qichao Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.28613) · [Project](https://zebinx.github.io/PhysCanvas_HomePage/)
- Tags: PhysCanvas, visuo-tactile, multimodal-canvas, action-conditioned-simulator, policy-evaluation, imagined-GRPO, contact-rich
- Model size: Wan2.2-TI2V-5B backbone; total unknown
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

多視点RGB・触覚画像・marker変位・task状態を共通canvasへ描き、同じvideo VAE/生成backboneで予測するPhysCanvas。ロボット関節指令を投影したmotion画像で条件付け、閉ループpolicy評価と想像内学習に使う。

**主な貢献**

scene・modality・stateの凍結reward modelで生成の整合性を追加学習。4実機taskの評価batch間成功率相関と、想像内GRPO後のpolicy成功を別々に検査し、π0.5平均59.1%→70.8%を報告する。

**確認記録**

- Checked: 2026-10-21 · Review: verified
- 初稿・題名・著者・版履歴をarXiv absで確認（v1=2026-10-20、改訂なし）。https://arxiv.org/html/2610.28613v1 の§3/4、Appendix C/Gと公式projectを選読。ARX AC One双腕・Xense触覚による4taskに限定。相関0.602→0.885はtask別Pearsonの算術平均で、全試行pooled相関ではない。追加整合学習は全低レベル指標や全taskを一律改善せず、FMは2taskで成功0のまま。行動を生成するpolicyと観測を生成するWMは別で、WM/RMを固定してpolicyを更新する。公式projectがCode/Model Coming Soonを明記し各unavailable。実装licenseはunknown、論文licenseとは別。PDF未取得。 2026-10-08〜21の選択増分調査（基礎文献は分類補完の例外）。独立した実行・数値再現なし。

### Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

- ID: `WAM-0132`
- Published: 2026-10-19
- Authors: Tianqi Liu; Hanfei Zhao; Qifeng Liang; Hui En Pang; Jiarui Xu; Sayang Mu; Penghao Qiu; YingSheng Zhang; Jun Wang; Ziang Cao; Mingze Sun; Yukang Cao; Fangzhou Hong; Zhaoxi Chen; Ziwei Liu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.26855) · [Code](https://github.com/Ropedia/ropedia-w0) · [Project](https://ropedia.github.io/ropedia-w0/)
- Tags: cross-embodiment, egocentric-video, loco-manipulation, kinematic-conditioning, human-video, policy-evaluation
- Model size: 5B dense; A14B MoE (approximately 27B total / 14B active)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

カメラ姿勢と投影骨格を共通の運動条件にし、人間と異なるロボット身体の一人称移動・操作映像を予測する。人間10k時間とロボット3k時間を統一注釈し、Xp-Teleop評価と方策評価・候補行動選択・WAM初期化を検証した。

**主な貢献**

身体別の数値行動を共通の幾何条件へ写像。著者実験ではFastWAMの動画backbone初期化を置換するとLIBERO-Plus成功率50.06%→56.82%。世界モデルによる実機候補選択はtask progress55%で、完全成功率とは区別する。

**確認記録**

- Checked: 2026-10-20 · Review: verified
- arXiv v1初稿日・全著者、HTML §4/§6.4/Appendix Fを確認: https://arxiv.org/html/2610.26855v1 。公式5B推論実装とApache-2.0 LICENSE: https://github.com/Ropedia/ropedia-w0/blob/main/LICENSE 。重み2種の実在とCC BY-NC 4.0を別確認: https://huggingface.co/ropedia-ai/Ropedia-W0/tree/main 。A14B・post-training/evaluation codeは公開予定で、全recipe公開とはしない。運動条件は接触・物体物理を直接記述しない。PDFリンク取得は取得エラー、HTMLで本文確認しpdf\_urlは空欄。

### From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction

- ID: `WAM-0141`
- Published: 2026-10-13
- Authors: Ruo Chen; Jiahua Pang; Yingjie Niu; Hongyi Lin; Jun Tian; Yang Zhu; Chao Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.17630) · [PDF](https://arxiv.org/pdf/2610.17630)
- Tags: DR-WM, behavior-grounded-physics, quadruped-navigation, terrain-contact, action-consequence-prediction, VLM-action-selection
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

画像から再構成した地形に、実機の行動応答で校正した接触特性を与え、Genesisの物理rolloutで四脚ロボットの動きと将来カメラ軌跡を推定する。その軌跡と幾何情報で動画世界モデルを条件付け、生成画像による地形更新と予測を反復する。

**主な貢献**

地形接触を空間的に変える予測と、行動結果の視覚生成を接続。未見22シーン34clipの物理ablationで、幾何のみのbaselineに対してbase ATEを18.0%低減。90の行動選択シーンではDR-WM付き8B VLMが単独32Bを6指標中5指標で上回った。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absのv1履歴・全著者、HTML https://arxiv.org/html/2610.17630v1 §3–5、Appendix Bと比較・ablation表を確認。初期実画像と行動からの因果rolloutで、校正mappingはtest時固定。生成画像を再構成へ戻すため誤差伝播の可能性があり、行動応答に合う有効接触値は真の物性値を一意に同定するものではない。Appendix Aはdata/code releaseを予定と記すが公式公開実装・重み・ライセンスは未確認。検索で見つかった同名展示用GitHubは著者との対応が未検証のためURL不採用。

### Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

- ID: `WAM-0143`
- Published: 2026-10-09
- Authors: Peiyan Tu; Cong Wang; Hanxin Zhu; Xin Jin; Zhibo Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.13522) · [PDF](https://arxiv.org/pdf/2610.13522) · [Project](https://peiyantu.github.io/HF-WM/)
- Tags: HF-WM, failure-dynamics, human-robot-transfer, stabilized-pointflow, GRPO, policy-evaluation, test-time-action-selection
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人間とロボットの相互作用を、カメラ運動を補正したpointflowの補助予測で結ぶ行動条件付き世界モデルHF-WM。成功実演の行動に摂動を加え、行動整合性と物理妥当性の報酬によるGRPOで、対応する正解動画なしに失敗時のダイナミクスも学習する。

**主な貢献**

100成功・100失敗の実機軌跡で動画生成と行動追従を検証。6方策×90の対応sessionでは予測成功率と実機成績のPearson相関0.983を報告。LIBERO-90のπ0.5候補選択では、HF-WMとRoboMeterにより成功率27.8%→30.0%を報告した。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absのv1履歴・全著者、HTML https://arxiv.org/html/2610.13522v1 §3–5とAppendix B/Cの学習・評価設定、論文からリンクされた公式projectを確認。Cosmos 3 Nanoを約45Kロボット・83K人間軌跡で調整。補助pointflowは学習時のみ、物理妥当性報酬はVLM評価。相関は6方策の集計成功率で、540独立方策の相関ではない。LIBERO候補選択には同domain fine-tuneと別のscorerが必要。公式project/論文で実装・重み・実装ライセンス公開先は確認できずunknown。

### DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

- ID: `WAM-0102`
- Published: 2026-10-08
- Authors: Junyan Li; Ruizhi Li; Yu Liu; Xiangshuo Liu; Mingchao Sun; Hongyu Pan; Mu Xu; Lue Fan; Zhaoxiang Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12468) · [Code](https://github.com/brave-eai/DreamTrue)
- Tags: cross-embodiment, multi-view, counterfactual-post-training, video-reward, geometric-calibration
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

複数身体・複数視点の行動条件付き動画世界モデル。既存データの幾何校正を直し、反実仮想行動で生成した動画を、人の欠陥注釈から学ぶ報酬モデルで後学習する。

**主な貢献**

行動軌道の画像条件への統一、オフライン校正、相互作用欠陥の報酬学習を組み合わせる。AgiBotの160反実仮想条件で、人評価の相互作用欠陥率をStage Iの48.12%から6.25%へ低減。

**確認記録**

- Checked: 2026-10-09 · Review: needs-review
- v1初稿・著者・題名、HTML3節/4.1/4.2/5節を確認: https://arxiv.org/html/2610.12468v1 。公式repoのcalibration/wmvideo/rewardに実コードあり。rootと各pyprojectに新規実装ライセンスを確認できずunspecified。READMEの配布先 https://modelscope.cn/datasets/huoxingdawang/DreamTrue はdatasetリンクでありリンク自体はcheckpoint公開の証拠ではない。本確認で配布ファイルにアクセス不能なのでweightsはunknown。project https://brave-eai.github.io/DreamTrue/ も再確認で取得失敗。限界: 画像空間の生成/報酬は遮蔽下で見かけが自然でも物理的に誤った相互作用を許す。追補は配布ファイルと利用条項・実装LICENSE。

### VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving

- ID: `WAM-0092`
- Published: 2026-10-08
- Authors: Zhaoyang Liu; Kun Jiang; Ziying Song; Diange Yang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.11161)
- Tags: 3d-world-prediction, driving-intent, vla-semantic-features, navsim, supporting-method
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VGGT-Worldの将来3D幾何へ走行maneuver、trajectory/速度、VLA由来の意味tokenを条件付けするVGGTWorld-VLA。同じ場面でも行動による異なる将来形状を表現する。

**主な貢献**

NAVSIMの3,000clip motion subsetで行動をzero/shuffle/wrongに変える介入と、意味token追加ablationを実施。正しい行動条件で予測を改善するが、raw geometry全指標での一律改善ではない。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.11161 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.11161v1 。§4.3–5/Tables1–4選読。主評価はfuture geometryでdepthはVGGT pseudo ground truth、閉ループ運転成功や衝突安全性の評価ではない。baselineよりRMSE/thresholdは改善するがAbsRelは悪化する指標trade-offがある。VLA moduleは予測条件の供給で、実行robot policyを共同学習するHybridとは分けた。semantic追加は小幅で追加computeの限界。コード/重み/実装ライセンス未確認。 PDF未取得。

### RoboJEPA: Scaling Robotic Latent World Models

- ID: `WAM-0086`
- Published: 2026-10-07
- Authors: Artem Zholus; Nicolas Beltran-Velez; Jianhao Yuan; Sarath Chandar; Tushar Nagarajan; Daniel Severo; Koustuv Sinha; Michal Drozdzal; Adriana Romero Soriano; Jeannette Bohg; Nicolas Ballas; Mahmoud Assran
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10515) · [Code](https://github.com/facebookresearch/robo_jepa) · [Project](https://robojepa.github.io/)
- Tags: RoboJEPA, JEPA, multi-embodiment, latent-dynamics, scaling-laws, image-goal-CEM, fixed-encoder
- Model size: 22M–8B predictor; frozen V-JEPA 2.1 encoder
- Open-source: false
- Code / weights / license: available / available / non-open-source

**概要（日本語）**

凍結V-JEPA 2.1表現上で、行動・状態・複数視点を入力するlatent予測器を22Mから8Bまで拡張する。23公開データセット・12embodimentを統合し、rollout誤差の計算量依存と画像目標CEM計画の性能を、DROID/RoboCasaとFranka操作で調べた。

**主な貢献**

小規模22M–2Bのfitから4B/8Bを外挿する比較で二次power lawが良好。固定表現上の予測誤差と計画能力の関係を実測。encoder共同scaleやテキスト目標は扱わず、大規模CEMは複数GPUで数秒を要する。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- 初稿2026-10-07/v1、改訂なしをabsで再確認: https://arxiv.org/abs/2610.10515 。前回のHTML §2,§3.1–3.4,§5,Appendix G.7確認による制約は継続: 固定encoder/corpus、image-goalのみ、複数GPUの大規模CEM、VLAと目標仕様/訓練/controllerが異なる。2026-10-10に公式project→repoの公開を再確認、Oct8の404/coming soon状態は解消。READMEの訓練/eval/Franka・RoboCasa deployment構成とworld\_model.py実装を確認: https://github.com/facebookresearch/robo\_jepa/blob/main/app/robo\_jepa/world\_model.py 。実装root LICENSE全文はCC BY-NC-SA 4.0で非商用制限、したがってopen\_source=false: https://github.com/facebookresearch/robo\_jepa/blob/main/LICENSE ; upstream codeは個別license。READMEに22M–8B/8B DROID720p checkpointの公式dl.fbaipublicfiles.com配布リンク一覧、例 https://dl.fbaipublicfiles.com/robojepa/wm/wm-50m/cooldown\_50m\_120k.pth.tar 。独立した重み利用条件は未確認、実装licenseと区別。CHANGELOGの初release2026-08-08はpreprint初稿日でなく実際のpublic化日も特定せず。公開dataset converterはDROID/AgiBotのみ、他datasetは今後。PDF/weights/dataは取得していない。

### DepthWorld: 3D World Model for Robot Manipulation

- ID: `WAM-0109`
- Published: 2026-10-06
- Authors: Jai Bardhan; Josef Šivic; Vladimír Petrík
- Venue: CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2610.08780) · [Code](https://github.com/Jai2500/depthworld) · [Project](https://jaibardhan.com/depthworld/)
- Tags: DepthWorld, multi-view-rgb-depth, DROID-3D, spatial-latent-tiling, action-conditioned-video, geometric-supervision
- Model size: unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

DROIDの複数視点映像を、ロボットごとに共有する運動学パラメータと場面ごとの外部校正を同時最適化して3D教師信号にする。既存VAEを変えずRGBと深度の潜在表現を空間配置し、行動条件付きで未来の両者を予測する。

**主な貢献**

DROID-3Dの幾何校正と、点地図補助損失を備えた動画世界モデルを接続。256保留軌道・10連続rolloutの予測評価で、RGBのみの同一backboneに対し外部視点PSNRを1.48dB改善。ロボット方策の成功率改善を直接評価した値ではない。

**確認記録**

- Checked: 2026-10-11 · Review: verified
- arXiv v1日付・書誌、https://arxiv.org/html/2610.08780v1 §3–5と限界を選読。深度評価の参照はDROID-3D推定深度をVAEでencode/decodeしたもので、手首視点の精度低下と自己回帰誤差蓄積を記載。公式repoのtrain/eval実装とLICENSE.txtの完全なMIT本文を別確認: https://github.com/Jai2500/depthworld/blob/main/LICENSE.txt 。重みは https://huggingface.co/jaibrdhn/depthworld/tree/main のhoriz\_90k\_ema.pt/horiz\_dpt\_vggt\_90k\_ema.pt実ファイルを確認。model cardは前者Stability AI Community、後者は追加CC-BY-NC4.0で非商用と区別。root MITは重み・外部backboneへの包括許可ではない。PDF/重み未取得。

### World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models

- ID: `WAM-0082`
- Published: 2026-10-06
- Authors: Jiuyi Xu; Xiao Hu; Meida Chen; Peng Gao; Yang Ye; Yangming Shi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09134) · [Code](https://github.com/jiuyixu25/CureWM)
- Tags: CureWM, failure-insensitivity, execution-verified-counterfactuals, world-model-repair, success-failure-discrimination
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unavailable / open-source

**概要（日本語）**

成功デモの行動を重症度別に変え、simulationまたは実機で成否を検証したreplayを既存world modelの追加学習へ使うCureWM。architectureやlossを変えず、失敗への楽観的予測と成功・失敗の識別を、Cosmos PolicyとCtrl-World系列で診断・修復する。

**主な貢献**

検証済み反実仮想replayを、同予算のon-policy失敗と比較。LIBERO-Goalの例で楽観率79.55%→30.17%、AUROC 0.495→0.743だが、成功の誤警報率も31→38%に増加。予測修復を操作性能向上と同一視しない評価を提示。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・書誌: https://arxiv.org/abs/2610.09134 。HTML §3、§4.1/§5、§6を精読: https://arxiv.org/html/2610.09134v1 。実装MITを本文確認: https://github.com/jiuyixu25/CureWM/blob/main/LICENSE 。公式READMEはmodel weights/fine-tuned checkpoints/datasetsを再配布しないと明記: https://github.com/jiuyixu25/CureWM\#what-is-not-here 。制約: 484 LIBERO failures中未見元デモは53、転移不均一、短い予測horizon、1robot/2objectsの小規模実機。RoboCasaのrepair-control tradeoff、best-of-N制御改善に統計的証拠なし。weights unavailableは著者の積極的な非配布表明に基づく。PDFは未取得、URL欄は未検証のため空欄。

### SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

- ID: `WAM-0076`
- Published: 2026-10-05
- Authors: Xiaodong Wang; Tianle Li; Chuanxin Song; Junliang Xie; Zhanmi Zhong; Suiying Wu; Peixi Peng
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06598) · [PDF](https://arxiv.org/pdf/2610.06598) · [Code](https://github.com/Wang-Xiaodong1899/SimForcing) · [Project](https://wang-xiaodong1899.github.io/SimForcing/)
- Tags: action-conditioned-video, sim-to-real, latent-motion-distillation, simulation-conditioning, policy-pretraining
- Model size: Wan2.2-TI2V-5B video backbone + 1B Action DiT
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

シミュレーション教師の隣接潜在状態の差分を実映像の生徒へ蒸留し、行動に応じた運動知識を移すロボット世界モデル。複数ブロックへの条件付けとdropoutで不正確なシミュレーション予測への依存を抑え、推論時は同一の生徒がシミュレーション条件と実領域映像を生成する。Bridge、InternData-A1、下流LIBERO方策学習で検証。

**主な貢献**

外見の差を避ける潜在運動蒸留と、シミュレーション条件のCFGを統合。Bridgeでは身体性事前学習を使わない比較群内でPSNR・SSIM・LPIPS・FVDが最良だがFIDは最良ではない。下流のaction-only学習で平均LIBERO成功率が82.6%から89.2%へ改善。推論時に別の教師モデルは不要だが、運動条件の生成と実映像生成は必要。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。arXiv書誌とv1初稿日2026-10-05を確認、後続版なし。HTML https://arxiv.org/html/2610.06598v1 の§3-5、Table 1/5、Appendix A.3/A.5を確認。研究の主対象は行動条件付き映像予測で、事前学習中に行動を生成するモデルではないためWAM/dynamics。教師の合成データはロボット運動に集中し、物体相互作用と背景を除く。標準設定は初期腕領域のsegmentationを要し、計測条件による遅延の制約も記載。論文からリンクされた公式実装、projectを確認。実装MIT: https://github.com/Wang-Xiaodong1899/SimForcing/blob/main/LICENSE 。READMEは第三者コードの元ライセンスを保持しWanのApache-2.0も同梱と明記。READMEの重み・学習手順とprojectを別に確認したが、学習済みSimForcing重みの公開配布先は未確認でunknown。コードにはsimulation renderingが含まれないと明記。PDFリンクを確認、ダウンロードなし。

### LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models

- ID: `WAM-0036`
- Published: 2026-08-06 · Updated: 2026-08-06
- Authors: Jiarui Yang; Jiale Zhange; Jiawei Li; Hang Guo; Wen Huang; Jinpeng Wang; Peidong Liu; Shu-Tao Xia
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2608.05706v1) · [PDF](https://arxiv.org/pdf/2608.05706v1)
- Tags: Latent Action, Human Video, Multi-view, 3D Geometry, RGB-D
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動ラベルのない人の動画から、視点をまたいで使える三次元的な潜在行動を学ぶ研究。動画を複数視点に増やすだけでは残る、見た目による近道を扱う。

**主な貢献**

複数視点で共有する行動トークン、三次元基盤特徴との幾何整合、RGB-D共同再構成を結合して未来フレームの外観漏洩を抑える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning

- ID: `WAM-0038`
- Published: 2026-07-27 · Updated: 2026-07-27
- Authors: Wenxuan Ma; Chaofan Zhang; Chao Xue; Yinghao Cai; Guocai Yao; Shaowei Cui; Shuo Wang
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2607.24267v1) · [PDF](https://arxiv.org/pdf/2607.24267v1)
- Tags: Visuo-tactile, Contact, Slip Prediction, CEM, FeelWorld
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

見た目だけでは捉えにくい接触と滑りを、視覚・触覚の未来予測へ組み込むFeelWorldを提案。接触を伴う把持や挿入で、予測と候補行動の計画を評価する。

**主な貢献**

接触状態、力を含む三次元触覚潜在、滑り状態を階層的に予測し、接触前後で注意経路を切り替えるcontact gatingを使う。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

- ID: `WAM-0001`
- Published: 2026-03-13 · Updated: 2026-06-03
- Authors: Lucas Maes; Quentin Le Lidec; Damien Scieur; Yann LeCun; Randall Balestriero
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2603.19312v3) · [PDF](https://arxiv.org/pdf/2603.19312v3) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)
- Tags: JEPA, Latent Dynamics, Pixel Control, SIGReg
- Model size: ~15M
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

画素から小さな潜在状態と行動条件付き予測を同時に学び、画像目標への計画に使う世界モデル。大規模な固定視覚エンコーダを使う方式に対し、学習と候補行動の探索を軽くする設計を検証した。

**主な貢献**

次状態の潜在予測誤差とSIGRegの二項だけで表現崩壊を抑え、エンコーダと予測器を一体学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT; source: https://github.com/lucas-maes/le-wm.

### Learning Interactive Real-World Simulators

- ID: `WAM-0131`
- Published: 2023-10-09 · Updated: 2024-09-26
- Authors: Sherry Yang; Yilun Du; Kamyar Ghasemipour; Jonathan Tompson; Leslie Kaelbling; Dale Schuurmans; Pieter Abbeel
- Venue: ICLR 2024
- Links: [Paper](https://arxiv.org/abs/2310.06114) · [PDF](https://arxiv.org/pdf/2310.06114) · [Project](https://universal-simulator.github.io/unisim/)
- Tags: UniSim, action-conditioned-video, generative-simulator, sim-to-real, supporting-foundation
- Model size: 5.6B (UniSim simulator; policy sizes are separate)
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

画像・動画・ロボット操作などの異種データを統合し、言語指示や低レベル制御に対する未来の観測動画を生成するUniSim。生成した経験を上位VLM方策の学習や低レベル方策の強化学習に用い、実機への転移を検証する。

**主な貢献**

異なる形式の行動を共通の条件表現へ変換し、有限の観測履歴から動画を予測する拡散モデルを自己回帰的に接続する。生成環境内の方策改善を示す基礎研究であり、物理的正確性や未知機体への一般化を保証しない。

**確認記録**

- Checked: 2026-10-19 · Review: verified
- 直近窓より前の選択的基礎研究補充。本文前にcanonical arXiv、version/10.48550/arXiv DOI alias、正規化/近似題名を既存355件と照合し一致なし。arXiv履歴v1 2023-10-09、v3 2024-09-26。本文 https://arxiv.org/html/2310.06114v3 の2節・4.1–4.2節・6節を選読。主な限界は不可能な指示への幻覚、有限履歴、未知機体、視覚以外の力等の未表現。Table 3の81%は生成動画を定性的に判定したシミュレーション48課題で実機成功率ではない。公式projectのリンク先を確認。専用実装・checkpoint実file・実装LICENSEは個別に未確認のため各unknown。論文/サイトのlicenseを実装に流用しない。PDF hrefのみ確認、PDF/weights/data未download、実行再現なし。

### Denoised MDPs: Learning World Models Better Than the World Itself

- ID: `WAM-0016`
- Published: 2022-06-30 · Updated: 2023-04-06
- Authors: Tongzhou Wang; Simon S. Du; Antonio Torralba; Phillip Isola; Amy Zhang; Yuandong Tian
- Venue: ICML 2022
- Links: [Paper](https://arxiv.org/abs/2206.15477v6) · [PDF](https://arxiv.org/pdf/2206.15477v6) · [Code](https://github.com/facebookresearch/denoised_mdp) · [Project](https://ssnl.github.io/denoised_mdp/)
- Tags: Factorized State, Controllability, Reward-conditioned, Denoised MDP
- Model size: unknown / 未確認
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

外界の情報を、制御できるか・報酬に関係するかで分けて世界モデルを学ぶ研究。背景などの外乱を明示的に分離し、制御に使う潜在状態を絞る。

**主な貢献**

制御可能性と報酬関連性による四種類の潜在因子を設け、制御可能かつ報酬関連な状態へ方策学習を集中させる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Venue and author list cross-checked against https://proceedings.mlr.press/v162/wang22c.html. Official implementation and CC-BY-NC 4.0 license checked at https://github.com/facebookresearch/denoised\_mdp.

### Contrastive Learning of Structured World Models

- ID: `WAM-0048`
- Published: 2019-11-27 · Updated: 2020-01-05
- Authors: Thomas Kipf; Elise van der Pol; Max Welling
- Venue: ICLR 2020
- Links: [Paper](https://arxiv.org/abs/1911.12247v2) · [PDF](https://arxiv.org/pdf/1911.12247v2) · [Code](https://github.com/tkipf/c-swm)
- Tags: Object-centric, Graph Dynamics, Contrastive Learning, C-SWM
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

画素から物体と関係を分けて学び、構造化した潜在空間で行動後の状態を予測するC-SWMを提案。複数物体が独立に操作される環境で、再構成型モデルとの違いを評価する。

**主な貢献**

物体単位の状態埋め込みとグラフニューラルネットワークによる遷移を、対照的な予測目的で学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/tkipf/c-swm.

### Learning Latent Dynamics for Planning from Pixels

- ID: `WAM-0040`
- Published: 2018-11-12 · Updated: 2019-06-04
- Authors: Danijar Hafner; Timothy Lillicrap; Ian Fischer; Ruben Villegas; David Ha; Honglak Lee; James Davidson
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/1811.04551v5) · [PDF](https://arxiv.org/pdf/1811.04551v5) · [Code](https://github.com/google-research/planet) · [Project](https://danijar.com/project/planet/)
- Tags: Model-based RL, Stochastic Dynamics, Latent Overshooting, PlaNet
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

画像から環境の動力学を学び、潜在空間内のオンライン計画だけで行動を選ぶPlaNetを提案。部分観測や接触、疎な報酬を含む連続制御でモデルの長期予測を評価する。

**主な貢献**

決定論的な再帰状態と確率的な潜在状態を組み合わせ、複数段先の整合を学ぶlatent overshooting目的を加える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and Apache-2.0 license license checked at https://github.com/google-research/planet.

### Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models

- ID: `WAM-0044`
- Published: 2018-05-30 · Updated: 2018-11-02
- Authors: Kurtland Chua; Roberto Calandra; Rowan McAllister; Sergey Levine
- Venue: NeurIPS 2018
- Links: [Paper](https://arxiv.org/abs/1805.12114v2) · [PDF](https://arxiv.org/pdf/1805.12114v2) · [Code](https://github.com/kchua/handful-of-trials) · [Project](https://sites.google.com/view/drl-in-a-handful-of-trials/)
- Tags: Probabilistic Dynamics, Ensemble, Uncertainty, Model-based RL, PETS
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

少数の実環境試行から使える動力学モデルPETSを提案。モデル予測の不確実性を候補軌跡へ伝え、モデルベース制御のデータ効率と最終性能を両立させる。

**主な貢献**

確率的ニューラル動力学のアンサンブルと、粒子を使うtrajectory samplingによる不確実性伝播を結合する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/kchua/handful-of-trials.

### World Models

- ID: `WAM-0103`
- Published: 2018-03-27 · Updated: 2018-05-09
- Authors: David Ha; Jürgen Schmidhuber
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/1803.10122) · [PDF](https://arxiv.org/pdf/1803.10122) · [Code](https://github.com/hardmaru/WorldModelsExperiments) · [Project](https://worldmodels.github.io/)
- Tags: World-Models, supporting-foundation, VAE, MDN-RNN, latent-imagination, evolution-strategies, not-physical-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / available / unknown

**概要（日本語）**

画像をVAEで圧縮し、行動条件付きMDN-RNNで潜在状態の推移を学ぶ。小さな線形controllerを進化戦略で最適化し、CarRacingとVizDoomで評価した。VizDoomではモデルが生成した環境内で学んだ方策を元のゲームへ移す。

**主な貢献**

知覚・再帰的世界モデル・制御器を分離し、学習した潜在環境での方策訓練と元環境への転移を実証した世界モデル研究の基礎。

**確認記録**

- Checked: 2026-10-10 · Review: needs-review
- arXiv書誌/v1 2018-03-27/v4 2018-05-09と公式記事のAgent Model・両ゲーム実験・Discussionを選読。実機ロボットや一般的sim-to-realの実証ではない。CarRacingのcontroller訓練は元環境、VizDoomは夢環境であり区別。モデル誤差の悪用と温度調整の限界も記載。公式記事→著者の実験解説→参照実装を確認: https://blog.otoro.net/2018/06/09/world-models-experiments/ 。公開tf\_modelsのvae/rnn JSONとcontrollerの使用手順を確認、重み未ダウンロード。READMEはMITと宣言するが完全な実装ライセンス本文を未確認のためlicense/open\_sourceはunknown・要再確認。記事のCC-BYと混同しない。公式サイトは後の会議版タイトルRecurrent World Models Facilitate Policy Evolutionを引用するが、本行の正式タイトル/日付はarXiv原稿を維持。
