<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / action-coupling

[← wam](README.md) · [CSV master](../papers.csv)

29 records · Published date 降順（同日 ID 降順）

### LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC

- ID: `WAM-0101`
- Published: 2026-10-08
- Authors: Shashank Hegde; Alexander Popov; Elie Aljalbout; Nikolai Smolyanskiy
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12407)
- Tags: jepa, bidirectional-dynamics, diffusion-steering, mpc, decoder-free
- Model size: 41.0M trainable parameters
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

デコーダなしのJEPA潜在表現と共有Transformerで、順/逆時間ダイナミクス、逆ダイナミクス、方策の4モードを同時学習する。計画では生の行動でなく方策の拡散ノイズ空間を探索する。

**主な貢献**

4モード学習で制御に有用な潜在表現を得ることと、ノイズ空間MPCで世界モデルの誤差を突く行動を減らすことを分けて検証。41.0M学習パラメータで同規模方策と閉ループ性能を比較。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿・著者・題名、HTML3〜5節/6節/Appendix C,Dを確認: https://arxiv.org/html/2610.12407v1 。評価はPushT/robomimicのシミュレーション。計画が遅く、推論時のgoalを必要とし、実世界データ/実機への適用は今後の課題。本文リンクとLeWAM/著者を限定した検索で公式実装・独自重み・実装LICENSE未確認。各unknownで不存在とは断定しない。追補はreleaseと実機/速度評価。

### Unifying Policy Learning and State Prediction through Spatial Language Modeling

- ID: `WAM-0098`
- Published: 2026-10-08
- Authors: Minye Wu; Zehao Wang; Tinne Tuytelaars
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.12172)
- Tags: spatial-language-modeling, supporting-method, from-scratch, push-t, state-prediction
- Model size: 462M
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

場面輪郭、目標、行動座標、将来状態を共通の離散空間語彙で表し、一つの自己回帰Transformerで行動と状態遷移を学習する。raw画像VLAではなく、幾何入力を使うPush-Tの支援的world/action手法。

**主な貢献**

実機20episodeで成功0.80、episode最大coverage平均0.95。共同行動/状態学習とrandom-play事前学習の効果を分けて評価し、与えた行動列に沿う将来場面も予測した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.12172 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.12172v1 。§4/5、Table2選読。462M Qwen2構造をfrom scratch学習し、実機入力は較正済AprilTagと既知T字形状。40成功デモと20random-playを使い、比較方策はデモのみ。成功はcoverage≥0.95を300step以内に達成、coverage指標と成功率を区別。方策ごとの履歴/実行chunk差もあるため純粋な同一入力比較ではない。3D・他物体・raw sensor一般化は未検証。コード/重み/実装ライセンス未確認。 PDF未取得。

### UNITAS: A 3D-Native World Action Model for Embodied Manipulation

- ID: `WAM-0097`
- Published: 2026-10-08
- Authors: Ruixiang Wang; Yongyi Su; Wenlve Zhou; Bo Yue; Hengyan Liu; Dekun Lu; Yuxin Tian; Yihan Fang; Zerui Wu; Xing Hu; Jietao Chen; Yong Guo; Ziyan He; Junbin Yuan; Guiliang Liu; Xiaofen Xing; Kui Jia
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12099) · [Code](https://github.com/DexForce/UNITAS)
- Tags: 3d-native, metric-world-frame, scene-flow, action-flow, cross-embodiment
- Model size: 1.7B
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

観測、手/グリッパの3D点軌道、scene flowを同じmetric世界座標で表す3D-native WAM。身体や視点に依存しにくいmotion interfaceで、直接行動生成と行動条件付きscene予測を統合する。

**主な貢献**

world-aligned3D位置埋め込みとphysical-time trajectory tokenで行動/scene動態を結合。RoboTwinの点軌道予測とLIBERO/実機操作を評価し、RoboTwin Moving ADEは0.427cm（PointWorld0.656cm）。

**確認記録**

- Checked: 2026-10-09 · Review: needs-review
- v1初稿・著者・題名、HTML3節/4.4/5節/6節を確認: https://arxiv.org/html/2610.12099v1 。公式repoはREADME/assetsのみでinference/checkpoint/training release欄が未完了。要旨のcode availableとは区別し、実装は確認時点でunavailable、重み・LICENSE各unknown。READMEのproject http://unitas-wam.github.io/ は取得失敗でproject\_url空欄。scene-flow定量評価はsimulator groundtruthを用い、video baselineの3D化は初期GT depth校正を用いる。長期相互作用/広い実機deploymentは今後の課題。追補は実装とcheckpoint release。

### Humanoid World Action Model With Joint State--Action Generation

- ID: `WAM-0096`
- Published: 2026-10-08
- Authors: Yan Yang; Jikun Rong; Minzhao Zhu; Zheyi Zhao; Qirui Hu; Zihan Lan; Weixin Mao; Yinhao Li; Zhen Fu; Hua Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12026) · [Project](https://hwam.vercel.app/)
- Tags: humanoid, joint-state-action-generation, execution-gap, forward-inverse-dynamics, whole-body
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

人型のpolicy参照行動と、全身制御後に実現する身体状態のずれを、joint state-action生成で明示的に扱う。Policy/FDM/IDMの3条件経路で実現身体動作と視覚未来を結ぶ。

**主な貢献**

未来の固有受容状態をaction学習の教師targetに加える。LimX OLIの3実機課題を評価し、Candy Picking70.6%（Fast-WAM43.3%）など、action-onlyとの差を制御ablationで調べる。

**確認記録**

- Checked: 2026-10-09 · Review: needs-review
- v1初稿・著者・題名、HTML3節/4.2〜4.5を確認: https://arxiv.org/html/2610.12026v1 。HTMLのcode/dataset available記載に対し公式projectはCode/Dataset/Video Coming soonで、実装は確認時点でunavailable、重み・LICENSE各unknown。限界: OLI3課題中心のtask別データ/学習で身体間一般化保証ではない。未来video診断は12held-outepisodeで、predicted trajectory条件ではHWAMのPSNR優位なし。joint state-action単独のrecipeは必ず改善するわけではない。追補はreleaseと各試行分母/不確実性。

### Cross-Embodiment Robot Foundation World Models with Latent Actions

- ID: `WAM-0091`
- Published: 2026-10-07
- Authors: Huang Huang; Sriram Yenamandra; Arjun Majumdar; Elie Aljalbout; Tushar Nagarajan; Tsung-Yen Yang; Akshara Rai; Michael Rabbat; Li Fei-Fei; Jiajun Wu; Tingfan Wu; Franziska Meier
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10846) · [Project](https://lacwm.github.io/)
- Tags: latent-actions, cross-embodiment, inverse-forward-dynamics, motion-decoder, vla-proposal-ranking
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人と複数robotの連続画像から共通の潜在行動を学び、その行動で視覚世界モデルを条件づけるLAC-WM。未知身体の明示actionは新しいprojectorで事前学習済みlatentへ写像する。

**主な貢献**

IDM/FDMにmotion decoderとcross-augmentationを加え、身体ごとに分断したexplicit action表現との転移差を検証。5未見LIBEROvariant/125試行のVLA候補rankingでSR92.0%対EAC-WM82.4%。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿・著者・題名、HTML3節/6節/7節とprojectを確認: https://arxiv.org/html/2610.10846v1 。新身体にはprojector/モデルfine-tuningを行いzero-shot対応としない。事前学習にmotion labelを用い、label-free video学習は将来方向。dexterous絶対成功率は低く実機hardware検証は今後の課題。projectのCodeはbuttonのみで提供先未確認、実装・独自重み・LICENSE各unknown。追補はreleaseと実機評価。

### RealtimeWAM: How Fast Can I Run My World Action Model?

- ID: `WAM-0085`
- Published: 2026-10-07
- Authors: Huanan Liu; Ye Li; Kangye Ji; Xiaoyu Chen; Hanyun Cui; Yutian Shen; Yuan Meng; Chenglei Wu; Jingyan Jiang; Bo Li; Zhi Wang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10079) · [Project](https://anonymous.4open.science/w/realtimewam/)
- Tags: RealtimeWAM-training-free, dependency-aware-parallelism, token-reuse, motion-adaptive-refinement, inference-acceleration
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

WAMの観測処理と予測を層単位で重ね、視覚的に安定したtokenとTransformer残差を再利用する訓練不要の推論方式。予測された移動量に応じて追加計算を配分し、FastWAMとOpenWAMのシミュレーションおよび5つの実機操作で遅延と成功率を評価した。

**主な貢献**

並列実行とhardware-awareな計算再利用を協調させる。著者の改造48GiB RTX 4090測定で平均24.09/63.09 ms、native比8.90/10.67倍高速化。速度向上は複数最適化の合算で、sensor取得・通信・robot実行等を含まない。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・書誌: https://arxiv.org/abs/2610.10079 。HTML §§3–4、Appendix C.1/E.1–E.2を精読: https://arxiv.org/html/2610.10079v1 。公式projectは動画・結果を掲載するが実装/重み/実装ライセンスは確認できずunknown。2つのWAM backbone、5実機課題の範囲。motion gateはXYZ変位でrotation/gripperを使わず、10F予測との一致は真の行動正しさの保証ではない。2610.06617もRealtimeWAMを名乗るが、著者・arXiv・方式が異なる独立論文。PDFは未取得、URL欄は未検証のため空欄。

### ΔWAM: Distilling Action Tangent Fields into World Action Models

- ID: `WAM-0084`
- Published: 2026-10-07
- Authors: Ke Wu; Hanwen Huang; Bo Gu; Kaizhao Zhang; Xiangting Meng; Yupeng Zheng; Zijun Xu; Jieru Zhao; Wenchao Ding
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09734)
- Tags: DeltaWAM, action-tangent-fields, Residual-VAE, counterfactual-action-probes, robustness, single-pass-world-conditioning
- Model size: Wan VideoDiT 5B; ActionDiT size unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

観測からの残差として未来VAE latentを保持し、action-conditioned world modelへの局所行動摂動からAction Tangent Fieldsを抽出する。その方向の予測誤差を追加重み付けし、実デモの未来を学習するWAMへ行動依存性を蒸留する。推論は単一world passと行動flow生成を組み合わせる。

**主な貢献**

静的外観を捨てず、局所的な行動変化に応答する予測方向へ教師信号を集中。著者評価でLIBERO-Plus pooled成功87.8%。RoboTwin 2.0-Plusのcamera摂動19.1%が弱点で、局所近傍外の観測変化への限界が残る。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 書誌・初稿: https://arxiv.org/abs/2610.09734 。HTML §§3–4.4、Conclusionを精読: https://arxiv.org/html/2610.09734v1 。§3でWan VideoDiT-5Bを確認。論文・arXivに公式code/project/weightsリンクは確認できず、個別の実装ライセンスもunknown。制約: embodiment別ACWMへの依存、局所Taylor近似、camera/大きいlayout変化に弱い。実機は2platform/5task、task別訓練、各task-condition 3試行のprogress scoreで成功率と区別。HTMLが参照する一部appendixは表示されず未精読。PDFは未取得、URL欄は未検証のため空欄。

### RIWANav: Recursive World-Action Models with Self-Improvement for Urban Navigation

- ID: `WAM-0089`
- Published: 2026-10-06
- Authors: Jing Xie; Shouwei Ruan; Yubin Wang; Yuxiang Zhang; Haitao Yang; Songchang Jin; Dianxi Shi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08640)
- Tags: urban-navigation, recursive-self-improvement, grpo, cosmos, offline-training
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

都市ナビゲーション方策と行動条件付き動画世界モデルを交互に後学習する。想像された結果をGRPOの比較報酬に使い、改善した方策から専門家と整合する行動・動画対を選んで世界モデルを更新する。

**主な貢献**

行動の新規性と予測誤差で優先づけるgrounded self-curriculumにより、固定世界モデルとの比較を行う。UrbanNav test-unseenの3seed平均SRは88.25±0.43%、GRPO-WMは80.31±0.94%。実機試験は定量benchmarkと分けた定性的実証。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- arXiv v1初稿2026-10-06・著者・正式題名、HTML III手法/IV-A,C,D,E,Fを確認: https://arxiv.org/html/2610.08640v1 。今回初めて読み取り成功した retained lead。実装・独自重み・実装LICENSEの公式提供は本文リンクとRIWANav/著者を限定した検索で未確認。既存CosmosやUrbanNavの公開とは区別。限界: 固定offline dataset、記録expertに近い行動だけに未来動画を対応づけられ反実仮想探索が制限、4H200学習と大動画モデルの計算/メモリ負担、実機は定性的で都市/身体間一般化は未評価。専用releaseと広範な実機定量評価を追補。PDF未取得、正確なhref未抽出。

### AutodidactWAM: Cross-Modal Self-Distillation from Generated Video to Robot Actions

- ID: `WAM-0081`
- Published: 2026-10-06
- Authors: Sergei Kurchev; Iaroslav Kolomiets; Miguel Altamirano Cabrera; Artem Lykov; Dzmitry Tsetserukou
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08119)
- Tags: AutodidactWAM, cross-modal-self-distillation, generated-video, RoboHaMeR, inverse-kinematics, Flow-DPO, dexterous-humanoid
- Model size: Cosmos 3 Nano ~15.8B; 16.9M trainable adaptation parameters
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

embodiment適応済みCosmos 3の生成動画から、凍結hand-pose推定とIKで行動教師を復元し、同じ生成のnative行動と組にしてaction関連層を追加学習する。動画をteacher-forcingし、SFT・Flow-DPO・Cartesian軌道anchorを比較。自己蒸留段階では新しいtask別teleoperationを集めない。

**主な貢献**

生成動画と行動のずれを行動側の自己蒸留で部分修正。著者G1評価ではDPO+SFT+DTWがOreo/未見pink物体でfull-task 20/30%、plain DPOは0%。動画由来教師の直接実行より成功率が低く、preference accuracy 1.0は実機能力を保証しない。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 書誌・初稿: https://arxiv.org/abs/2610.08119 。HTML §§III、V–VIIIを精読: https://arxiv.org/html/2610.08119v1 。arXiv/本文の公式code・project・weights配布先は未確認、実装licenseもunknown。論文license CC BY-NC-NDと実装を混同しない。制約: 1embodiment/3objects、20試行/condition、Oreoのみ自己蒸留、extractor biasと生成artifact。先行G1 LoRA適応corpusは§V-Aで約90%Oreoと記載され、新規デモなしは自己蒸留段階に限る。matching video-side成功スコア未実施。104–137秒/chunkのregeneration latencyでreal-time性能とは区別。PDF未取得・URL未検証のためpdf\_url空欄。

### OpenWAM: An Open Framework for Composable World-Action Models

- ID: `WAM-0080`
- Published: 2026-10-06
- Authors: Heng Yu; David D. Yuan; Juze Zhang; Changan Chen; Yao Feng; Michelle Baldonado; Steve Cousins; Li Fei-Fei; Jiajun Wu; Ehsan Adeli
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.07922) · [PDF](https://arxiv.org/pdf/2610.07922) · [Code](https://github.com/OpenWAM/OpenWAM) · [Project](https://openwam.stanford.edu/)
- Tags: OpenWAM-Stanford, causal-robot-video, configurable-MoT, generation-order, local-context-dynamics, counterfactual-transitions, component-composition
- Model size: Wan2.2 5B video backbone; action expert size unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

共通の因果的ロボット動画backboneとMoTで、joint・video先行・action先行・decoupled生成を比較するframework。独立した局所contextのinverse/forward dynamicsも学習し、同一初期状態からsimulationで分岐させた反実仮想transitionを、予測器交換と行動条件付き未来識別に使う。

**主な貢献**

backboneと訓練interfaceを揃えたinteraction比較、および局所dynamicsの再利用を検証。著者評価でcounterfactual混合IDMは4target平均84.0%。target動画予測器は適応済みであり全model zero-shot転移とは区別。公開重みは動画事前学習部分。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 書誌・初稿: https://arxiv.org/abs/2610.07922 。HTML §§3–5を精読: https://arxiv.org/html/2610.07922v1 。初preprintは2026-10-06、code/projectの2026-06-04 releaseとは別（論文header明記）。実装AGPL-3.0-only: https://github.com/OpenWAM/OpenWAM/blob/main/LICENSE 。動画重みmodel\_state.pt一覧確認: https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining/tree/main ; 重みlicense表示なしでunknown、policy checkpoints/dataはREADMEで準備中。制約: dynamics再利用は主にsimulation/4targets、target動画model適応あり、短horizon FDM、単一multi-objective checkpointの全mode性能未確立。別研究OpenWAM (2609.07398, Wang et al.)と同名だが独立した著者/ID（§2.2/ref79）。PDF URLは公式README引用で確認、PDF自体未取得。

### RealtimeWAM: One-Step Asynchronous World Action Models

- ID: `WAM-0079`
- Published: 2026-10-05
- Authors: Chengtao Lv; Jinyang Du; Shuyi Feng; Yang Yong; Shiqiao Gu; Shunzi Yang; Ruihao Gong; Shen Ren; Tianwei Zhang; Wenya Wang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06617) · [Code](https://github.com/ModelTC/LightX2V/tree/main/examples/realtimewam)
- Tags: RealtimeWAM-one-step, teacher-anchored-consistency-distillation, cross-expert-wavefront-pipelining, MoT, inference-acceleration
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

MoT型WAMの行動expertを、局所consistency lossにteacherの多段rollout終端を加えるTACDで1stepへ蒸留する。動画KVをblock単位で共有するCEWPでexpert間待機を減らし、Fast-WAM/Faster-WAMの成功率と推論時間を比較した。

**主な貢献**

teacher終端の固定基準とblock-wise並列実行を組み合わせるpost-training高速化。著者H100測定で12.2/16.1 ms、native比24.55/13.56倍。CUDA Graph・kernel最適化込みで、VAEを含みtext encodingは除外。実機foldingは定性的例。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 書誌・初稿: https://arxiv.org/abs/2610.06617 。HTML §§4–5、Appendix E/F.5–F.6を精読: https://arxiv.org/html/2610.06617v1 。公式READMEにinference/evaluation codeとcheckpoint提供、training code未公開を確認。実装Apache-2.0: https://github.com/ModelTC/LightX2V/blob/main/LICENSE 。checkpoint先 https://huggingface.co/lightx2v/RealtimeWAM はread toolで取得できず、実ファイル・重み条件を独立確認できないためweights unknown。具体的追跡: HF files/model cardを確認しlicense/重みの提供範囲を更新。MoTの独立したvideo KV前提、H100中心のkernel、他GPUのgain差。2610.10079とは著者・ID・手法が異なるので別論文として保持。PDFは未取得、URL欄は未検証のため空欄。

### PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation

- ID: `WAM-0074`
- Published: 2026-10-02
- Authors: Chunghyun Park; Beomjun Kim; Seungcheol Park; Heeseung Kwon; Yashu Shukla; Seunghoon Sim; Jinwoo Shin; Minsu Cho
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.02840) · [Project](https://chrockey.github.io/PointWAM/)
- Tags: 3d-point-trajectory, dexterous-manipulation, human-video-pretraining, retargeting, scene-hand-factorization
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

場面と手を同じ時空間座標系の3D点軌跡として分離・共同予測し、予測した手の運動をロボット動作へretargetするWAM。物体やkeypointを課題ごとに指定せず、人とロボットに共通する軌跡表現を通じて人動画から事前学習できる。

**主な貢献**

人動画1.15Mepisodeの事前学習でDexJoCo平均成功率を12.1%から69.0%へ改善。場面軌跡の教師信号は手のみの予測より10.9ポイントを追加し、10課題で最強比較方策を11.7ポイント上回る。精密把持simulationとOpenArm実機2課題も評価。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- identity照合一致なし。v1初稿2026-10-02 05:31:01 UTC: https://arxiv.org/abs/2610.02840 、改訂なし。HTML §3/4/5選読: https://arxiv.org/html/2610.02840v1 、公式projectのmethodも照合。DexJoCoは元11課題のうちデモ再生42/100失敗のunlock iPadを除外し10課題、各3seed×50episode。実機2課題各24試行、OOD物体は一部PnP試行。点間隔以下の文字やdepthに映らない透明物体を捉えにくい。公式 https://chrockey.github.io/PointWAM/ はCode soon、code unavailable。公開重み・実装license未確認unknown。PDFファイル未保存。

### XGenAct: Geometry-Enhanced World Action Models through Cross-Task Generation

- ID: `WAM-0073`
- Published: 2026-10-02
- Authors: Tingting Du; Ziyao Wang; Guoheng Sun; Ang Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.03516)
- Tags: geometry, video-diffusion, depth, surface-normal, functional-segmentation, deterministic-codec
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

RGB、ロボット行動、metric depth、surface normal、機能役割segmentationを決定的codecでRGB動画へ変換し、同じ凍結VAE・動画diffusion Transformer・出力head・目的関数を共有するWAM。学習時に知覚空間と条件付けplanを変え、未来予測と行動をcross-taskに学ぶ。

**主な貢献**

保持したRLBench5課題の閉loop比較で52%成功（最強比較方策26%）を報告。構造化知覚の学習がRGBのみより制御を改善し、生成RGBを後処理する凍結expertと比べてdepth・segmentationの直接生成精度を高めた。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- identity照合一致なし。v1初稿2026-10-02 16:10:53 UTC: https://arxiv.org/abs/2610.03516 、改訂なし。HTML §3/4/5選読: https://arxiv.org/html/2610.03516v1 。外部比較は5課題各20試行、MolmoActはzero-shotで他手法とは学習条件が異なる。学習源はRLBench/ManiSkill3、検証はRLBench simulation。知覚menuはtask依存で追加modalityが単調に改善しない。将来知覚評価は各生成動作が達したsimulator状態を基準とし、動作乖離による除外規則あり。abs/HTML/手法名code検索で公式実装・重み・project・実装license未確認unknown。PDFファイル未保存。

### ActiveWAM: Evidence-Aware Active Vision for World-Action Models

- ID: `WAM-0066`
- Published: 2026-10-01
- Authors: Renjun Wu; Luzhou Ge; Xuesong Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01698) · [Project](https://icr-lab.github.io/ActiveWAM/)
- Tags: ActiveWAM, active-vision, pan-tilt, bimanual, training-time-inversion, view-aware-history
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unspecified

**概要（日本語）**

有限履歴の手掛かりを保持する学習と、新しい視点を得る頭部・双腕制御を統合する。動画priorの履歴inversionは訓練だけに使い、実行時は生の観測履歴から行動を生成する。

**主な貢献**

RoboTwin-AVの50課題で観測と操作を共同評価し、複合分布変化で53.3%成功を報告。実機の3料理課題・各20試行は全段階成功50.0%で、第一段階66.7%と区別する。段階切替は事前指定で、連続料理全体の自律性を保証しない。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.01698v1 の3節・4.1/4.2/4.4/4.5節を確認。操作失敗・早期終了・視野外・hardwareの失敗分類は因果分析ではない。公式 https://github.com/Soraruholic/Active-WAM はREADME/assetsのみ、訓練・評価コードとcheckpointsはTODO、ライセンスは初回releaseで指定予定。公開 https://github.com/Soraruholic/RoboTwin-AV の収集・評価実装をActiveWAM方策公開と混同しない。PDF未取得。

### SkeleWAM: Skeleton World-Action Modeling for Efficient Robotic Manipulation

- ID: `WAM-0065`
- Published: 2026-10-01
- Authors: Juyi Sheng; Hua Wang; Mengyuan Liu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02120) · [Project](https://skelewam-project.github.io/)
- Tags: SkeleWAM, sparse-3D-skeleton, RGB-D, auxiliary-future-prediction, medoid-action-consensus
- Model size: 57.1M observation-based; 51.4M privileged sim-state variant
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

RGB-Dと固有感覚から関節・物体中心・接触点の疎な3D骨格を構成し、行動と未来骨格を共同学習する。推論時は未来分岐を省き、MACで複数行動候補の代表軌道を選ぶ。

**主な貢献**

観測入力のLIBERO-Plusで85.9%成功、57.1M規模を報告。特権sim-state版を区別し、配置変化では66.6%に留まる。実機ARX R5の5課題・各20試行では平均89%で、任意の配置への保証ではない。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿日・著者、HTML https://arxiv.org/html/2610.02120v1 の3節・4節を確認。公式projectはデモと結果を掲載するが、研究実装・重み・実装ライセンスの提供先は未確認。論文ライセンスを実装へ転用しない。PDF未取得。

### Completion Aware Guidance for World Action Models

- ID: `WAM-0058`
- Published: 2026-10-01
- Authors: Seungyeon Kim; Junhoo Lee; Baekseung Kim; Minkyu Kim; Nojun Kwak
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01559)
- Tags: completion-guidance, training-free, cross-attention, short-horizon, sampling
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

短い映像・行動チャンクが把持解除などの完了遷移を先送りする失敗を分析し、関連する指示トークンの条件づけをサンプリング中に強めるCompletion Aware Guidanceを提案する。

**主な貢献**

クロスアテンションから得たトークン関連度でキー・値へ有界な介入を行う追加学習不要の方法。Fast-WAMの非飽和9課題で平均成功64.4%から70.0%、DreamZeroの3シミュレーション課題で69%から75%を報告する。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者・arXiv DOI、HTML https://arxiv.org/html/2610.01559v1 の3–4節と限界を確認。RoboTwinは成功率90%未満の選択9課題であり全ベンチマーク平均ではない。ワークショップ名は本文記載のみなのでvenue=arXiv。公式実装・重み・実装ライセンスは本文リンクとタイトル検索で未確認。論文CC BYはコード公開の証拠ではない。PDF未取得。

### CtrlWAM: Controllable World Action Models with Aligned Intent and Foresight

- ID: `WAM-0057`
- Published: 2026-10-01
- Authors: Chensheng Peng; Wenhao Ding; Ran Tian; Zewei Zhou; Jef Packer; Maximilian Igl; Peter Karkus; Yan Wang; Masayoshi Tomizuka; Boris Ivanovic; Marco Pavone; Yuxiao Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.00859) · [Project](https://ctrl-wam.github.io/)
- Tags: joint-video-action, aligned-noising, counterfactual-control, multi-agent, driving, bimanual
- Model size: Cosmos 3-Nano 16B backbone
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

摂動を加えた行動をシミュレータで実行し、その結果の映像と組にして世界行動モデルを学習する。映像と行動のノイズ時刻をずらし、周辺エージェントの将来を予測または指定できる入力へ拡張する。

**主な貢献**

行動意図と予測映像の物理的な対応を学習中から揃える方法を提示。運転の軌跡整合性とRoboTwin由来1000エピソードの映像品質・制御可能性を評価し、生成映像の改善を実機閉ループ成功率と混同しない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.00859v1 の3節・4.1–4.4節・付録Dを確認。公式projectのCode (under review)は https://github.com/anonymous/ctrlwam にリンクするが確認時404。実装公開・専用重み・実装ライセンスは未確認なのでunknown、code\_urlは空欄。multi-agentは場面内の行動ストリームでありLLM Agentとの結合と推測しない。PDF未取得。

### Magic-W0: A Structured World-Action Foundation Model for Physical Intelligence

- ID: `WAM-0070`
- Published: 2026-09-30 · Updated: 2026-10-03
- Authors: Xuhua Chen; Zhenhan Yin; Yuan Zhang; Lingfeng Zhang; He Zheng; Tong Mu; Shun Zuo; Dian Zhou; Di Wu; Xuan Zhou; Shaojie Wan; Rongtian Shen; Qiulong Xu; Yiduo Li; Yinglong Wang; Yanqian Wang; Kun Wang; Tao Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.39870) · [Code](https://github.com/MagiclabRobotics/Magic-W0) · [Project](https://embodied.magiclab.top/works/wam/magic-w0/index.html)
- Tags: 3d-geometry, structured-transition, cross-embodiment, flow-matching, future-semantics
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unavailable / open-source

**概要（日本語）**

現在の3D形状、行動が生む3D運動、将来のタスク意味をStructured World Transitionとして表現する基盤WAM。世界表現と連続行動の専門ストリームを複数層の共同attentionで双方向に結合し、人の一人称動画・UMI・実機・simulationを横断して事前学習する。

**主な貢献**

構造化された世界状態遷移と制御を共同学習し、行動置換・接続maskで予測が行動条件に依存することを調べた。v2本文ではRoboDojo-Sim平均Score 36.75/SR 30.36%、LIBERO 99.1%。5実機課題各100試行で94.6%（比較π0.5は91.8%）。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- canonical arXiv照合で既存WAM-0070を確認しID/初稿日を維持。https://arxiv.org/abs/2609.39870 のv1は2026-09-30 14:49:55 UTC、v2は2026-10-03 14:49:17 UTC、追加改訂なし。既存のv2 HTML https://arxiv.org/html/2609.39870v2 §3/5.2/6/7選読結果とTable 1のRoboDojo Score 36.75/SR 30.36%を維持。42課題・公式完走軌跡の集計でScoreとSRは別指標。abs要旨の27.10との差が残るためneeds-review、次回は改訂で整合するか確認。2026-10-08確認の同日付commit https://github.com/MagiclabRobotics/Magic-W0/commit/870051074695b5d22736223b01dda1d2e6607c5a のREADME、src/magic\_w0/modeling.py、configs/resources.json、docs/robodojo.mdを確認し、実装を伴うinference runtimeとRoboDojo adapterの公開をcode availableへ更新。READMEの更新欄はOct5だが確認したcommit日時はOct8、commit日時を初回公開日時とは同一視しない。学習/finetuning recipesは後日提供で、完全な学習再現releaseではない。同commitのLICENSEで独自実装MIT、NOTICEでrotation helperのApache-2.0と外部依存の別条件を確認しopen\_source=true。公式重みリンクは https://huggingface.co/XuhuaX/Magic-W0 にredirectしmodel cardはweights not yet available、FilesはREADME/.gitattributesのみ、weights unavailableを維持。HubのMIT表示はcheckpoint公開の証拠にしない。ローカル互換policy checkpointが必要なため公開codeだけで論文性能を再現できるとはしない。巧緻手/触力覚と追加演算の既存限界を保持。PDF/重み未取得。

### One from Infinity: Actualizing Futures from Pretrained World Models into Robot Actions

- ID: `WAM-0060`
- Published: 2026-09-29 · Updated: 2026-10-01
- Authors: Bang Du; Yichen Xie; Shuqi Zhao; Yuxin Chen; Menglin Wu; Masayoshi Tomizuka
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.36413) · [Code](https://github.com/7mare/RoboActualizer) · [Project](https://zhao-sq.github.io/RoboActualizer/)
- Tags: RoboActualizer, frozen-V-JEPA, latent-action-MoT, flow-matching, cached-features
- Model size: 60M trainable actualizer; frozen V-JEPA 2.1 300M encoder
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

凍結V-JEPA 2.1の動画表現を利用し、二つの軽量DiTが指示に沿った将来潜在と行動チャンクを共同予測するRoboActualizer。キャッシュ済み特徴でヘッドを学習し、展開時はエンコーダを一回だけ実行する。

**主な貢献**

60M学習パラメータの方策でLIBERO・LIBERO-Plus、選択RoboTwin課題と二実機の五課題を評価。表現事前学習の費用は別で、論文の比較は全RoboTwin課題を含まず、単なる画像表現と動画予測表現のアブレーションも行う。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1/v2の日付を区別。HTML https://arxiv.org/html/2609.36413v2 の3節、4.1–4.2節、4.5.2–4.5.3節と5節を確認。本文には採択後のcode release予定が残るが、公式project経由の現在のrepoにはsrcと学習/評価実装がある。root MITを確認: https://github.com/7mare/RoboActualizer/blob/main/LICENSE 。第三者コードは元条項。専用重みを https://huggingface.co/db12312607/RoboActualizer のmodel card、MIT表示、libero\_dits/step\_173580.ptのファイル一覧で独立確認。公開repoの拡張評価設定を論文の評価範囲に混ぜない。PDF未取得。

### Efficient World Action Model Inference with Adaptive Intermediate States

- ID: `WAM-0063`
- Published: 2026-09-28
- Authors: Zhinnan Liu; Haozhi Han; Ruge Zhang; Teng Ma; Tao Ma; Zheng Liu; Yifeng Chen; Yunquan Zhang; Ting Cao; Yunxin Liu; Kun Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.34608)
- Tags: WAMachine, supporting-inference, state-reuse, trajectory-remapping, observation-rebinding, residual-rescaling
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

再計画、拡散ステップ、Transformer層の三段階でWAM推論状態を保持・補正する学習不要のWAMachine。予測観測で先行計算し、実観測との整合性検査が失敗すると再初期化や全層計算へ戻る。

**主な貢献**

三WAMの同一checkpointでシミュレーションを比較し、観測から行動準備までの遅延を1.47–3.05倍高速化。GPU計算時間と制御ループに見える遅延を別々に測り、大標本での成功率低下も併記する。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2609.34608v1 の3節の状態再利用、4.1–4.3節の設定/表、5節/倫理声明の該当箇所を確認。時間比較は各モデル固定200episode、成功率はCosmos Policy/Fast-WAM-IDM各6000 LIBERO、Motus 2000 RoboTwin試行。A100 80GB使用、MotusのWAMachineは追加rendering GPUを使う。全てsimulationで実機安全検証は別。新規方策ではなくWAM推論の支援研究。専用実装・重み・実装ライセンスは本文リンクと題名検索で未確認。PDF未取得。

### InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data

- ID: `WAM-0062`
- Published: 2026-09-25
- Authors: Xingyu Miao; Zizun Li; Baole Fang; Kaiwen Song; Tenghui Wang; et al.
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.31394) · [Project](https://internrobotics.github.io/InternW0-Delta/)
- Tags: world-action-MoT, Causal-Imprint, 4D-distillation, sparse-memory, heterogeneous-pretraining
- Model size: Wan2.2-TI2V-5B video backbone; total parameters unknown
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

動画専門家と行動専門家を有向注意で結び、凍結VLMの場面意味と4D教師の幾何・運動情報を学習へ取り込むWAM。Causal Imprintは将来映像を訓練時の教師として使い、推論時の未来映像ロールアウトを省く。

**主な貢献**

ロボット・UMI・人の一人称データを共通状態行動形式へ揃えた20K時間超の事前学習を報告。複数シミュレーションと四実機で評価し、事前学習あり/なしの実機比較は二課題各20試行で行う。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。著者48名のうち先頭5名＋et al.を明示。HTML https://arxiv.org/html/2609.31394v1 の3.1/3.3–3.6節、7.3節、8節の限界と公式projectを確認。Source codeとModel checkpointsはForthcomingと明記され、確認時unavailable、実装ライセンスunknown。将来のopen source予定をopen\_source=trueやデータの現公開証拠と扱わない。Agent支援は限定的な補正実験であり汎用Agent統合の保証ではない。PDF未取得。

### I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?

- ID: `WAM-0011`
- Published: 2026-09-25 · Updated: 2026-09-25
- Authors: Yuhang Liu; Zhuo Huang; Javen Qinfeng Shi
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2609.31161v1) · [PDF](https://arxiv.org/pdf/2609.31161v1)
- Tags: Theory, Causal Representation, Action Conditioning, A-JEPA
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動条件を加えたJEPAが、単に未来を当てるだけでなく潜在的な因果状態を回復できる条件を調べる研究。介入の多様さが因果機構の学習にどう効くかを検証する。

**主な貢献**

遷移尤度と状態情報を保つエントロピー目的から識別条件を導き、行動で変調するガウス加法ノイズモデルとしてA-JEPAを具体化する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### An Action Is Worth One Patch: Unified World-Action Modeling with PatchWAM

- ID: `WAM-0064`
- Published: 2026-09-22
- Authors: Tianheng Wang; Zhou Xie; Heng Jia; Jianhua Xu; Tong Zhang; Kaicheng Yu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.25961)
- Tags: PatchWAM, Action-as-Patch, shared-transformer, joint-denoising, parameter-free-codec
- Model size: FLUX.2 klein 4B Base backbone; total parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動成分を繰返し・ゼロ埋めで画像パッチと同次元へ変換する固定codecを用い、未来画像と行動を一つのTransformerで共同denoiseするPatchWAM。専用行動専門家や学習可能な行動codecを追加しない。

**主な貢献**

データと最適化を揃えた間引きRoboTwin学習で二専門家構成との比較を実施。追加データを使う別条件でRoboTwin平均96.12%、LIBERO-Plus91.8%を報告し、条件差・独立seed不足・実機未評価を明示する。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2609.25961v1 の3.1–3.2節、4.2節と6–7節を確認。20step推論の時間は二専門家対照の1.87倍、評価用10stepは未計時。未来予測が行動選択を改善する因果機序や全ての専用head不要は未実証。主結果のデータ増強とmatched comparisonを混ぜない。専用実装・重み・実装ライセンスは本文リンク/題名検索で未確認、基礎FLUXやImageWAMの提供状態を転用しない。PDF未取得。

### On the Identifiability of Controlled World Models

- ID: `WAM-0010`
- Published: 2026-07-24 · Updated: 2026-07-27
- Authors: Xiangteng Zhang; Yang Guan; Bo Zhang; Hongyang Li; Ya-Qin Zhang; Shengbo Eben Li
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2607.22430v2) · [PDF](https://arxiv.org/pdf/2607.22430v2)
- Tags: Theory, Identifiability, Action Conditioning, Counterfactual Prediction
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

観測から状態を識別する問題と、候補行動の効果を識別する問題を分けた理論研究。行動条件付きJEPAが反実仮想の予測に使えるためのデータ条件を明らかにする。

**主な貢献**

表現側のスペクトル分離と、状態を条件にした行動の非退化な変動を組み合わせた識別条件および誤差限界を示す。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- ID: `WAM-0033`
- Published: 2025-06-11 · Updated: 2025-06-11
- Authors: Mido Assran; Adrien Bardes; David Fan; Quentin Garrido; Russell Howes; Mojtaba Komeili; Matthew Muckley; Ammar Rizvi; Claire Roberts; Koustuv Sinha; Artem Zholus; Sergio Arnaud; Abha Gejji; Ada Martin; Francois Robert Hogan; Daniel Dugas; Piotr Bojanowski; Vasil Khalidov; Patrick Labatut; Francisco Massa; Marc Szafraniec; Kapil Krishnakumar; Yong Li; Xiaodong Ma; Sarath Chandar; Franziska Meier; Yann LeCun; Michael Rabbat; Nicolas Ballas
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2506.09985v1) · [PDF](https://arxiv.org/pdf/2506.09985v1) · [Code](https://github.com/facebookresearch/vjepa2) · [Project](https://ai.meta.com/research/vjepa/)
- Tags: JEPA, Video Pretraining, Action Conditioning, Robot Planning, V-JEPA 2
- Model size: 300M–1B video encoder family
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

大規模な観察動画から学んだV-JEPA 2を、少量のロボット軌跡で行動条件付き世界モデルへ拡張する研究。画像目標の計画により、新しい実機環境での操作を検証する。

**主な貢献**

行動なしの動画JEPA事前学習の後にV-JEPA 2-ACを学習し、潜在空間で候補行動を予測・比較する二段階構成を取る。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT with Apache-2.0 components; source: https://github.com/facebookresearch/vjepa2. arXiv splits Mojtaba Komeili into two author records; corrected to the single name verified in the official V-JEPA 2 repository README.

### Learning Action-based Representations Using Invariance

- ID: `WAM-0017`
- Published: 2024-03-25 · Updated: 2024-06-24
- Authors: Max Rudolph; Caleb Chuck; Kevin Black; Misha Lvovsky; Scott Niekum; Amy Zhang
- Venue: Reinforcement Learning Conference 2024
- Links: [Paper](https://arxiv.org/abs/2403.16369v3) · [PDF](https://arxiv.org/pdf/2403.16369v3)
- Tags: Action Bisimulation, Reward-free, Controllability, Long Horizon
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

報酬を使わず、複数段先の行動に関係する状態差を表現へ残す研究。直前だけでなく、遠くの壁など後で制御へ影響する情報を捉えることを狙う。

**主な貢献**

単一ステップの逆動力学に再帰的な不変性制約を加えたaction-bisimulationにより、長期の制御可能性を距離として学ぶ。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Mastering Atari with Discrete World Models

- ID: `WAM-0105`
- Published: 2020-10-05 · Updated: 2022-02-12
- Authors: Danijar Hafner; Timothy Lillicrap; Mohammad Norouzi; Jimmy Ba
- Venue: ICLR 2021
- Links: [Paper](https://arxiv.org/abs/2010.02193) · [PDF](https://arxiv.org/pdf/2010.02193) · [Code](https://github.com/danijar/dreamerv2) · [Project](https://danijar.com/project/dreamerv2/)
- Tags: DreamerV2, supporting-foundation, categorical-latents, KL-balancing, RSSM, latent-imagination, Atari, simulated-humanoid
- Model size: 20M world model (actor/critic excluded)
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

Dreamerの世界モデルを離散潜在状態とKL balancingで改良し、想像内でactor-criticを訓練するDreamerV2。55のAtariゲームの単一タスク学習で性能を評価し、画像入力のシミュレーションhumanoid制御にも適用した。

**主な貢献**

離散RSSMとKL balancingの効果を分解し、別訓練の世界モデル内で学習する方策をsticky-action Atariへ拡張。人間基準の集約scoreと世界記録基準の集約を区別する。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv v1 2020-10-05/v4 2022-02-12、ICLR2021出版原稿を確認: https://openreview.net/pdf?id=0oabwyZbOu 。v4 HTML §§2–3/Discussionの関連部分を選読: https://arxiv.org/html/2010.02193v4 。Atari55ゲームは各ゲーム別agent、sticky actions・action repeat4・200M環境steps（repeat4で50M agent inputs、200Mの独立control decisionではない）。Table1 gamer-normalized median2.15で、全ゲームで人間超えという意味ではない。20Mは世界モデルのみ。実機ロボット評価ではない。公式project→公開TF2実装、MIT全文 https://github.com/danijar/dreamerv2/blob/main/LICENSE を確認。repoのscores JSONは学習曲線で重みではない。checkpoint公開を確認できずweights unknown、ダウンロード/実行なし。

### Dream to Control: Learning Behaviors by Latent Imagination

- ID: `WAM-0104`
- Published: 2019-12-03 · Updated: 2020-03-17
- Authors: Danijar Hafner; Timothy Lillicrap; Jimmy Ba; Mohammad Norouzi
- Venue: ICLR 2020 (author/project-reported)
- Links: [Paper](https://arxiv.org/abs/1912.01603) · [PDF](https://arxiv.org/pdf/1912.01603) · [Code](https://github.com/danijar/dreamer) · [Project](https://danijar.com/project/dreamer/)
- Tags: Dreamer, supporting-foundation, RSSM, latent-imagination, actor-critic, analytic-gradients, visual-control
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

経験から学ぶ潜在動力学モデル内でactorとvalueを訓練し、想像軌跡の価値勾配を行動生成へ逆伝播するDreamer。画像入力のDeepMind Control Suite 20タスクで、長期報酬を考慮した方策学習とデータ効率を検証した。

**主な貢献**

潜在想像の短いrolloutをvalue推定で長期報酬へ接続し、微分可能な世界モデルを通したactor-critic学習を実現。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv v1 2019-12-03/v3 2020-03-17を確認。v3 HTML §§2–4/6–7を選読: https://arxiv.org/html/1912.01603v3 。20シミュレーション制御タスク、固定action-repeat 2での結果で実機評価ではない。5M環境steps後の平均score 823とD4PGの100M steps後786は訓練予算が異なる比較。公式projectはICLR2020 oralと記載、出版者proceedingsは別途未確認。著者がprojectからリンクする簡略TF2実装とMIT全文を確認: https://github.com/danijar/dreamer/blob/master/LICENSE 。READMEは元のTF1実装を別リンクするため、論文実験とTF2再実装の厳密な同一性は保証しない。公開重みは選択したproject/READMEで確認できずunknown。

### Being-M0.7: A Latent World-Action Model for Humanoid Robots

- ID: `WAM-0108`
- Published: unknown / 未確認
- Authors: Junpeng Yue; Boyuan Li; Yuxuan Wang; Zepeng Wang; Yuhui Fu; Feiyang Xie; Yu Zhang; Jing Zhang; Xianqi Zhang; Weibo Li; Xiaofei Zheng; Yuming Fang; Jiangxing Wang; Zongqing Lu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.11283) · [Project](https://research.beingbeyond.com/being-m07)
- Tags: Being-M0.7, latent-world-action-model, humanoid, loco-manipulation, human-video-motion, future-conditioned-action-expert
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人間中心の動画のみ・動作のみ・動画と動作のペアを混合し、潜在視覚状態と全身動作の未来を学ぶ人型ロボット向けWAM。ロボット中間学習で予測事前分布を適応させ、凍結した未来表現と現在画像・自己受容情報をgate付きcross-attentionで接続するaction expertを後学習する。

**主な貢献**

対応のない人間動画・動作も利用できるvisual-motion priorと、未来文脈を使う全身command生成を接続。SIMPLEの6課題×3難度・計180試行では128/180で比較対象中最高の合計成功率。Unitree G1の3実機課題・計15試行では13/15でGR00T-N1.6と同率であり、一般的な優越性は主張しない。

**確認記録**

- Checked: 2026-10-10 · Review: needs-review
- arXiv v1は2026-10-08。公式projectは2026-07-14表記で同名Technical Reportと10名の著者を掲載し、arXivは14名・中間学習を明示。初稿同一性と最初の公開日を確定できずpublishedは空欄。https://arxiv.org/html/2610.11283v1 の§3、§4 Tables1–3、Appendix7.1–7.2を選択確認。10,000時間超はfilter前のraw corpus。code・weights・実装licenseは未確認。PDF未取得。
