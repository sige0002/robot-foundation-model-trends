<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / temporal-modeling

[← wam](README.md) · [CSV master](../papers.csv)

9 records · Published date 降順（同日 ID 降順）

### WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models

- ID: `WAM-0094`
- Published: 2026-10-08
- Authors: Kai Ding; Yang He; Ruijie Quan; Yi Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.11401) · [Code](https://github.com/DingKai0302/wam-cache) · [Project](https://dingkai0302.github.io/wam-cache/)
- Tags: training-free, kv-cache, staleness-bound, efficient-inference, fast-wam
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

WAMのvideo DiT prefillを毎chunk全再計算せず、KVを再利用する。action expertのcross-attentionと視覚surpriseで再計算tokenを選び、最大ageで古い特徴による誤差蓄積を抑える。

**主な貢献**

単なる視覚変化/KV driftだけでは足りないことを分析し、action-aware refreshとage boundを導入。Fast-WAMのprefill FLOPsを32〜42%削減し、RoboTwin/LIBERO/実機の成功率損失を評価。

**確認記録**

- Checked: 2026-10-09 · Review: needs-review
- v1初稿・著者・題名、HTML4節/5節/6節を確認: https://arxiv.org/html/2610.11401v1 。公式repoはREADME/docsのみでCode coming soonと明記し実装は確認時点でunavailable、重み・LICENSE各unknown。FLOPs削減はprefill段階でありpipeline全体の同比率高速化ではない。少token条件はGPU/kernel固定overheadで速度改善が小さく、phase移行で継承attentionが遅れる。実機はAIRBOT2課題各20試行。追補は実装公開とruntime計測条件。

### Long-WAM: Scaling the Context of World-Action Models

- ID: `WAM-0087`
- Published: 2026-10-07
- Authors: Wei Huang; Bohan Zhang; Chenzhi Liu; Isabella Liu; Shuai Yang; Weian Mao; Luozhou Wang; Yicheng Xiao; Weifeng Lin; Qixin Hu; Bryan Chu; Sifei Liu; Linxi Fan; Xiaojuan Qi; Song Han; Yukang Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10528) · [Code](https://github.com/NVlabs/LongLive/tree/main/Long-WAM) · [Project](https://nvlabs.github.io/LongLive/Long-WAM/)
- Tags: Long-WAM, autoregressive-video-pretraining, visual-history, streaming-VAE, asynchronous-control, edge-deployment
- Model size: unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

自己回帰のロボット動画事前学習を、因果的な動画・行動expert結合へ引き継ぎ、過去の観測と未来latentから行動chunkを生成する。履歴長を変えた操作評価と、streaming VAE・非同期実行・端末別高速化を検証し、実機の動的把持や長期操作に展開した。

**主な貢献**

履歴の追加効果を動画事前学習方式と合わせて分析。著者評価ではLIBERO-Long 99.5%、Unitree G1の動くカップ積み19/20成功。履歴長ごとに別モデルを訓練しており、可変長履歴の実機一般化は未検証。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿・著者: https://arxiv.org/abs/2610.10528 。HTML §§3–6、Appendix A/Gを選択精読: https://arxiv.org/html/2610.10528v1 。実装Apache-2.0: https://github.com/NVlabs/LongLive/blob/main/Long-WAM/LICENSE 。重み実ファイル一覧を確認: https://huggingface.co/Efficient-Large-Model/Long-WAM-LIBERO-IDM/tree/main (model.pt); cardはlicense=otherで重み条件の詳細は未確認。制約: 長い履歴はpaddingと計算費増加、38.4秒で性能低下、GPU/実機再現は未実施。要確認: GR-1の短履歴値がabstract=0秒63.3%、Table 4=2.4秒63.3%、§5.3=2.4秒66.3%で不一致。著者修正または評価記録で履歴条件を照合する。公開コードのGPU/benchmark再現も未検証。PDFは未取得、URL欄も未検証のため空欄。

### SpectralCache: Accelerating Diffusion-Based World Models via Spectral Feature Caching

- ID: `WAM-0088`
- Published: 2026-10-02
- Authors: Zhendong Mi; Pu Zhao; Ziyu Hu; Xiaodong Yu; Yanzhi Wang; Grace Li Zhang; Shaoyi Huang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02660)
- Tags: supporting-foundation, diffusion-world-model, spectral-cache, singular-subspace, training-free
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

拡散world modelの近接denoising stepで安定する特異部分空間を再利用し、少数の特異値を外挿/倍率補正するtraining-free高速化。繰り返すTransformer全計算を減らす。

**主な貢献**

SVD空間と特異値の時間構造を利用するcacheを設計し、HunyuanWorld-Voyager-13Bで5.22倍の生成高速化とWorldScoreを比較。rank/最大cache間隔/倍率の品質trade-offも分析。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- v1初稿2026-10-02・著者・題名、HTML3節/5.3〜5.4/6節を確認: https://arxiv.org/html/2610.02660v1 。Oct9cs.ROへのcross-listで発見した同一v1で、新改訂とは扱わない。13Bは評価対象の既存world generatorで新モデル規模ではない。評価は環境動画生成でrobot閉ループpolicyやaction followingの保証ではない。cache間隔増大は品質を悪化させる。本文リンク/題名著者検索で公式実装・独自重み・LICENSE未確認各unknown。追補は実装releaseとrobot制御評価。

### World Action Learning via Interaction-Centric Spectral Latent Guidance

- ID: `WAM-0071`
- Published: 2026-10-02
- Authors: Zhiming Liu; Yikun Miao; Ying Chen; Hongrui Yin; Fangqi Zhu; Xiaoyi Pang; Quanxin Shou; Zhengyang Yan; Haodong Wang; Song Guo
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.03607) · [Project](https://mikuz12.github.io/wing/)
- Tags: egocentric-video, latent-action, spectral-guidance, cross-embodiment
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

一人称動画の観察者運動と手・物体の相互作用を分離するWING-LAMを作り、人とロボットに共有されやすい低周波latent動作成分をDCTで抽出する。現在の観測・指示からこの高位動作priorを推定し、WAMのロボット固有の行動生成を条件付ける。

**主な貢献**

カメラ変動を抑えたlatent動作と周波数領域の共通構造を制御へ転用。LIBERO平均99.20%、RoboTwin 2.0平均93.80%、RoboCasa-GR1 57.7%を報告し、4実機課題の一般化も評価。直接latent動作を実行目標にする方法との差をablationした。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- identity照合一致なし。Oct5 announcementだがv1初稿は2026-10-02 17:08:12 UTC: https://arxiv.org/abs/2610.03607 、改訂なし。HTML §3/4/5選読: https://arxiv.org/html/2610.03607v1 。外部motion cuesと単一global affine warpに依存し、parallax/深度差/3Dcamera運動で教師noiseが増え得る。latent pretrainingとspectral guidanceは学習費用・pipeline複雑性を追加。公式 https://mikuz12.github.io/wing/ はCode COMING SOON、code unavailable。重みと実装licenseの公開は未確認unknown。PDFファイル未保存。

### FutureWorlds: Learning Robotic World Models from Alternative Futures

- ID: `WAM-0059`
- Published: 2026-10-01
- Authors: Hao Wu; Shengju Qian; Weiyan Wang; Fan Xu; Fan Zhang; Yuanpeng He; Qingsong Wen; Yuxuan Liang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01019) · [Code](https://github.com/Alexander-wu/FutureWorlds)
- Tags: alternative-futures, candidate-memory, MemSPO, autoregressive-video, RL-post-training
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unavailable / unspecified

**概要（日本語）**

同じ行動条件から多様な未来映像を探索し、候補ごとに初期状態と直近履歴を保持する自己回帰世界モデル。MemSPOは候補映像の相対的な品質を報酬にし、生成時と学習時の履歴を一致させて事後学習する。

**主な貢献**

三データセット各128軌跡の32フレーム予測で画質・運動・長期整合性を評価。候補履歴を有界に保つ設計と探索誘導学習を結びつけるが、実機制御や閉ループ計画での成功改善は未検証。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2610.01019v1 の3節、4.1節、5節を確認。公式repoのsrc実装とREADMEを独立確認。READMEは公開checkpoint/data配布と独自コードの最終ライセンスをpendingと明記し、weight manifestのハッシュ一覧を公開重みと扱わない。コードはavailable、重みはunavailable、実装ライセンスunspecified、open\_source=unknown。repoに示されたproject linkは今回取得できずproject\_urlは空欄。PDF未取得、正確なPDF href未抽出のためpdf\_urlは空欄。

### Linear Recurrent Memory Suffices to Distil a World-Model Policy for Robot Air Hockey

- ID: `WAM-0067`
- Published: 2026-09-30
- Authors: F. Olivia Fan; Oliver Obst
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39151) · [Code](https://github.com/unswei/airhockey-distillation)
- Tags: supporting-policy-distillation, DreamerV3-teacher, linear-recurrence, partial-observability, simulation-only, air-hockey
- Model size: 12,002 total / 2,304 recurrent-core parameters (linear k=0 student)
- Open-source: unknown
- Code / weights / license: available / unknown / unknown

**概要（日本語）**

追跡が一時途切れるシミュレーションのair-hockey守備で、DreamerV3教師を64次元の線形再帰学生へ蒸留する。非線形encoder/headは残し、学生軌跡の教師ラベルで分布ずれを補正する。

**主な貢献**

clean観測・400ms欠測・5seedで線形学生98.3%、GRU97.8%の守備成功を報告するが、差の区間は0を含み同等性の証明ではない。学生全体12,002対28,898 parametersの比較で、実機・長期反復遮蔽は未評価。

**確認記録**

- Checked: 2026-10-04 · Review: needs-review
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.39151v1 の3–6節を確認。要旨はtest splitを将来開くと記載する一方、本文3節とrepo STATUS.mdはgate後の48,600件評価完了を記載し、本文の実測値として限定。次回は改訂で要旨/READMEの未来表現が本文と整合するか確認。CPU p95はブロック平均の分位で個別呼出p95ではなく、実装も異なる。公式repoはsource/config/resultsを提供するが独自実装ライセンスと公開学習済み重みは未確認。上流MITから推定しない。PDF未取得。

### Round-Trip Consistency: Bidirectional Diffusion Models Can Predict Their Own Rollout Errors

- ID: `WAM-0045`
- Published: 2026-08-01 · Updated: 2026-08-13
- Authors: Alexander Scheinker
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2608.00675v2) · [PDF](https://arxiv.org/pdf/2608.00675v2) · [Code](https://github.com/alexscheinker/round-trip-consistency)
- Tags: Diffusion, Bidirectional Dynamics, Uncertainty, Error Calibration
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

正解の未来を観測できない推論時に、生成的な動力学モデルの長期予測誤差を推定する研究。物理シミュレーションと顔動画で評価し、ロボット制御は直接の実証対象ではない。

**主な貢献**

同じ拡散モデルを時間の順・逆両方向に学習し、往復ロールアウトで出発点に戻れない量を誤差の代理指標にする。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/alexscheinker/round-trip-consistency.

### Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning

- ID: `WAM-0014`
- Published: 2026-06-05 · Updated: 2026-06-05
- Authors: Paarth Gulati; Ilya Nemenman
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2606.07770v1) · [PDF](https://arxiv.org/pdf/2606.07770v1)
- Tags: Contrastive Learning, Slow Features, Distractors, Inductive Bias
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ゆっくり変化するノイズを動的状態と取り違える、対照的予測学習の弱点を調べる研究。軌跡ごとの背景差を使う近道を除くことで、物理的な動きの表現を改善する。

**主な貢献**

負例を軌跡間ではなく同じ軌跡内から選び、軌跡固有の静的ノイズがフレームを識別する手掛かりにならない目的へ変える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Joint Embedding Predictive Architectures Focus on Slow Features

- ID: `WAM-0013`
- Published: 2022-11-20 · Updated: 2022-11-20
- Authors: Vlad Sobal; Jyothir S; Siddhartha Jalagam; Nicolas Carion; Kyunghyun Cho; Yann LeCun
- Venue: NeurIPS 2022 SSL Theory and Practice Workshop
- Links: [Paper](https://arxiv.org/abs/2211.10831v1) · [PDF](https://arxiv.org/pdf/2211.10831v1) · [Code](https://github.com/vladisai/JEPA_SSL_NeurIPS_2022)
- Tags: JEPA, Slow Features, Distractors, Failure Analysis
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

潜在予測が、制御に必要な動きよりも予測しやすい背景情報を選ぶ失敗を分析。軌跡中に固定された外乱と毎時刻変わる外乱で、JEPAの表現の違いを比較する。

**主な貢献**

移動点と背景外乱を切り分けた実験および理論で、固定ノイズがVICReg・SimCLR型JEPAを支配する条件を示す。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/vladisai/JEPA\_SSL\_NeurIPS\_2022.
