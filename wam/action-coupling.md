<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / action-coupling

[← wam](README.md) · [CSV master](../papers.csv)

55 records · Published date 降順（同日 ID 降順）

### LoopedWAM: Looped World Action Models for Elastic Inference

- ID: `WAM-0159`
- Published: 2026-11-19
- Authors: Anh Dao; Xinxin Liu; Hang Yu; Jeffrey A Chan Santiago; Yuzhang Shang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2611.25595) · [PDF](https://arxiv.org/pdf/2611.25595) · [Code](https://github.com/anhdao69/LoopedWAM) · [Project](https://anhdao69.github.io/LoopedWAM/)
- Tags: weight-sharing, elastic-inference, distillation, inference-efficiency
- Model size: 0.58B policy parameters
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

動画と行動の各エキスパートでコアブロックを反復利用する小型WAM。動画特徴はクエリごとに一度、行動計算はサンプリングステップごとに実行されるため、深さを別々に調整する。

**主な貢献**

行動側の反復深さとサンプリング回数を変えられる単一チェックポイントを自己蒸留で学習。LIBEROではH100で96.0%・27.6 msまたは95.2%・24.7 msを論文で報告。実機ではAgileX PiPERの4タスク80試行で通常版71.3%。

**確認記録**

- Checked: 2026-11-23 · Review: verified
- arXiv v1・公式実装を確認。実装MIT: https://github.com/anhdao69/LoopedWAM/blob/main/LICENSE 。https://huggingface.co/anhdao69/LoopedWAM のApache-2.0表記と、3ベンチマークの通常版・可変版計6個のpolicy.ptの公開を別に確認。

### MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation

- ID: `WAM-0158`
- Published: 2026-11-18
- Authors: Xianzhe Fan; Chi-Pin Huang; Fu-En Yang; Jing Wang; Yecheng Wu; Yu-Cheng Chou; Johan Bjorck; Linxi "Jim" Fan; Jan Kautz; Yu-Chiang Frank Wang; Zhiding Yu; Hengshuang Zhao; Zhiqi Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2611.25105) · [PDF](https://arxiv.org/pdf/2611.25105) · [Project](https://research.nvidia.com/labs/lpr/mawam/)
- Tags: multi-robot, coordinated-manipulation, cross-agent-attention, joint-denoising
- Model size: 2.76B trainable modules
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

複数ロボットの将来視点と行動チャンクを一度に生成し、ロボットごとに独立した制御インターフェースを通じて同期実行する。

**主な貢献**

単体WAMを初期値とし、ロボット間注意で各機の行動と将来視点を結び付ける。Galaxea R1 Pro 2台の実機3課題・各30試行で平均成功率67.8%、同じ実演と視点を使うMA-VLAは48.9%、ロボット間注意なしは52.2%と報告。

**確認記録**

- Checked: 2026-11-22 · Review: verified
- v1のみ。https://arxiv.org/html/2611.25105v1 §3・表1を確認。学習対象のDiT 2.06Bと状態・行動モジュール0.70Bの合計を記載。凍結モジュールは含まない。公式プロジェクトで本研究の実装・重み・ライセンスは未確認。同名に近い別研究のコードを除外。

### WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation

- ID: `WAM-0155`
- Published: 2026-11-18 · Updated: 2026-11-18
- Authors: Junlin Long; Xu Deng; Yiran Wang; Yue Yang; Yang Zhao; Zeyu Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2611.24011) · [PDF](https://arxiv.org/pdf/2611.24011) · [Code](https://github.com/AIGeeksGroup/WAM-Policy) · [Project](https://aigeeksgroup.github.io/WAM-Policy/)
- Tags: quadruped, loco-manipulation, on-policy-distillation, multi-teacher
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

操作用のLingBot-VAを四脚の移動操作へ移植し、生徒の生成軌跡上で動画と行動の生成を少ステップ化する。タスク別に強化学習した複数の教師も単一生徒に統合する。

**主な貢献**

QLM-Benchでは転移教師77.0%、少ステップ生徒76.7%でサンプリング14倍高速、専門教師統合後85.0%。実機Go2 Airは統合前の蒸留版を評価し、閉ループで0.66秒/チャンク。

**確認記録**

- Checked: 2026-11-20 · Review: verified
- arXiv v1書誌・本文の蒸留と評価を確認。コア実装Apache-2.0、deploy/とベンチマークはCC BY-NC 4.0。公開重みと配布条件は https://huggingface.co/AIGeeksGroup/WAM-Policy で別途確認。

### LaST1.0: A Unified Latent World-Action Model with Control-Centric SpatioTemporal Reasoning

- ID: `WAM-0153`
- Published: 2026-11-18 · Updated: 2026-11-18
- Authors: Hao Chen; Xuheng Zhang; Zhuangzhe Wu; Jiaming Liu; Shaobo Zhang; Jialin Gao; Zhonghao Yan; Di Wu; Sixiang Chen; Peng Jia; Chi-Wing Fu; Shanghang Zhang; Pheng-Ann Heng
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2611.23974) · [PDF](https://arxiv.org/pdf/2611.23974)
- Tags: latent-future, wrist-camera, geometry, spatiotemporal-attention
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

未来の手首カメラから得る幾何特徴を予測目標とし、ロボットと物体の相対運動を重視する。操作方策と潜在未来予測を一つのモデルで学ぶ。

**主な貢献**

現在画像は軽量なパッチ埋め込みで入力し、時空間構造を持つ注意機構で視覚・言語・行動を結合する。描画可能な動画全体の再構成ではなく、操作に関わる未来表現へ監督を絞る。

**確認記録**

- Checked: 2026-11-20 · Review: verified
- arXiv v1書誌・§3と評価の概要を確認。幾何ターゲット用エンコーダと入力側のパッチ埋め込みを区別。公式実装・重み・実装ライセンス未確認。

### JEPA Dots: Dual-Latent World Model for Language-Guided Robot Control

- ID: `WAM-0152`
- Published: 2026-11-18
- Authors: Xianhao Pan; Chi Li; Hanchao Li; Yunxin Liu; Jiankai Sun; Luhui Hu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2611.24062)
- Tags: JEPA, language-conditioned-control, masked-attention, subspace-Gaussian-regularization, LIBERO
- Model size: 16.4M; 39.1M with frozen language encoder
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

画像から、言語を受けない運動・環境変化用の表現と、言語で変調するタスク用の表現を分ける。前者と既知の行動で未来潜在を予測し、行動生成にはタスク用の表現も与える。

**主な貢献**

同じ観測と行動に対して指示だけを変えても、世界予測が変わらないよう注意マスクで制約。指示の切替実験で、世界予測を保ちながら方策出力が変わることを検証した。

**確認記録**

- Checked: 2026-11-19 · Review: verified
- arXiv v1初稿2026-11-18。論文HTMLの方式・実験概要・パラメータ計上を確認。学習対象LIBERO 40タスクで84.9%、著者らのタスクID条件付き参照実験76.0%。他論文の公表値とは評価条件が異なるため直接比較せず、実機・同一ハードの遅延は未確認。コード・重み・実装ライセンスはunknown。

### ResWAM: Learning What Changes, Not What Stays, for World-Action Models

- ID: `WAM-0157`
- Published: 2026-11-14
- Authors: Chongyu Fan; Gaowen Liu; Ramana Rao Kompella; Jason Corso; Sijia Liu
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2611.19559) · [PDF](https://arxiv.org/pdf/2611.19559) · [Code](https://github.com/OPTML-Group/ResWAM) · [Project](https://chongyu-fan.netlify.app/posts/reswam/)
- Tags: visual-residual, DINOv3, flow-matching, RoboTwin, LIBERO-Plus
- Model size: 2.3B total; 0.5B dual-branch DiT
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

凍結したDINOv3の現在と未来の特徴差分を教師にして、視覚の変化とロボット行動チャンクを同じモデルで学習する。背景など、変化しない特徴の再現に学習が偏ることを抑える狙い。

**主な貢献**

行動と視覚の差分を予測する二枝DiTを条件付きフローマッチングで共同学習。RoboTwin 2.0の50課題で平均成功率93.8%、未来特徴全体の予測に置換すると90.9%、視覚差分枝を除くと89.9%と報告。

**確認記録**

- Checked: 2026-11-22 · Review: verified
- v1のみ。https://arxiv.org/html/2611.19559v1 §4・表2・図7を確認。RoboTwin 2.0は50課題・各条件100試行/課題（clean 93.6%、random 94.0%）。公式評価はp32e16、シミュレータbf44be5。実装MIT: https://github.com/OPTML-Group/ResWAM/blob/main/LICENSE 。LIBEROに加え、RoboTwin 2.0 https://huggingface.co/OPTML-Group/ResWAM-RoboTwin2/tree/1b5f499e0cab45beafba2ac1c43b5fba08451497 とRoboDojo https://huggingface.co/OPTML-Group/ResWAM-RoboDojo/tree/b334326cedd24a43dfeb0765210b77df41640eec のmodel.pt・正規化統計・設定を配布APIで確認。両配布カードはMIT表記。重み取得や独立再現は未実施。

### Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models

- ID: `WAM-0150`
- Published: 2026-11-04 · Updated: 2026-11-10
- Authors: Juncheng Ma; et al.
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2611.06817) · [Code](https://github.com/DAGroup-PKU/HumanNet/tree/Open-HumanWAM) · [Project](https://dagroup-pku.github.io/open-humanwam/)
- Tags: Open-HumanWAM, HumanWAM, egocentric-pretraining, human-robot-data, visual-goal
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / available / unknown

**概要（日本語）**

50,000時間の人間一人称動画と手の動き・言語を利用してworld-action modelを事前学習し、ロボットへの転移を調べる。HumanWAM-Vanillaと、人間・robot混合学習および画像goal条件を持つHumanWAM-Goalを提示する。

**主な貢献**

人間データ時間だけでなくtask・sceneの多様性を分離して調べ、領域外転移との関係を分析。Goal版の画像条件による転移と、robot post-training後の評価をゼロショット評価から区別する。

**確認記録**

- Checked: 2026-11-16 · Review: verified
- 2026-11-02〜2026-11-15の14日間を対象とする選択増分調査。VLA/native policy、WAM/test-time selection、agent/belief-space planning、hybrid/world-model-agentの分野別検索。網羅調査ではなく、前回2026-10-23以降の全期間を補完したものではない。本文取得前に既存410件とrevisionなしarXiv/DOI・NFKC/Greek正規化・類似タイトルを既存checkerで照合し候補一致なし。初稿11月4日、v3改訂11月10日。旧題Open-HumanScaleと同一arXiv identityで別登録しない。https://arxiv.org/html/2611.06817v3 の結論と公式projectを確認。公式READMEとルート https://github.com/DAGroup-PKU/HumanNet/blob/Open-HumanWAM/Apache-2.0.txt はApache-2.0を提示する一方、humanwam\_goal/LICENSEはNVIDIA OpenMDW-1.1であり適用範囲・OSI承認状況を解決していないため実装license\_status/open\_sourceはunknown。Goal推論・評価・post-training実装を確認、Vanillaの一部reproductionは作業中と明記。公式 https://huggingface.co/DAGroup-PKU/HumanWAM-Goal-Base に公開safetensorsを確認したが重みのlicense metadataは未指定で実装licenseと別。READMEと論文では評価protocol/数値の差があるためここでは数値を混在させない。PDF実体は未取得。

### UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry

- ID: `WAM-0144`
- Published: 2026-10-22
- Authors: Jialin Tian; Zhuofan Li; Xinkai Wang; Bokai Lin; Chenyi Wang; Xinyu Zhan; Cewu Lu; Lixin Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.30991) · [PDF](https://arxiv.org/pdf/2610.30991) · [Project](https://kksham111.github.io/UniFlowWAM_ProjectPage/)
- Tags: scene-flow, 4D-geometry, multimodal-diffusion, role-conditioned-objectives, forward-inverse-dynamics
- Model size: Qwen3-VL-4B conditioning; LDA-initialized three-expert model, total unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

未来視覚特徴・3D scene flow・行動を対等な3モダリティとして共同学習するWorld-Action Model。各専門家のjoint attentionと10通りのtarget/condition/absent目的で方策と順逆動力学を統合し、直接方策の推論にはflow抽出を要しない。

**主な貢献**

RoboCasa-GR1の24課題を共有11評価seed・各課題/seed50episodeで比較し、平均56.38%対公開LDA52.11%。LIBERO学習からLIBERO-Plusへzero-shot87.7%（評価したcheckpoint中のbest）。実機は4課題を各50demoで別々に学習し各50試行、完遂成功率87.0%対π0.5の68.5%を報告。

**確認記録**

- Checked: 2026-10-23 · Review: verified
- arXiv v1=2026-10-22、改訂なし。本文前のcanonical arXiv/DOI・正規化/近似題名照合は一致なし。https://arxiv.org/html/2610.30991v1 §§3–5選読。3D flowはTrack4Worldの擬似教師と凍結4D VAEで準備し、雑音・表現shift・約1200時間の限定的flow mid-trainingを明記。RoboCasa58.9%は11評価seedのbestで平均56.38%と区別。実機は固定開始条件を同一policy間で共有したtask別学習で、87.0%は完遂率、92.3は別の部分点process score。公式projectはCode coming soon、公開実装unavailable。重みと実装licenseは未確認unknown、基礎LDAの公開状態を転用しない。PDF href検証のみ、PDF/重み保存・独立再現なし。

### Self-Distilling Future Video Representations for World Action Models

- ID: `WAM-0145`
- Published: 2026-10-21
- Authors: Huiwon Jang; Suhyeok Jang; Hyeonmo Kang; Seungku Kim; Jinwoo Shin; Sihyun Yu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.30320) · [PDF](https://arxiv.org/pdf/2610.30320) · [Code](https://github.com/suhyeok-jang/FRED) · [Project](https://huiwon-jang.github.io/FRED/)
- Tags: FRED, future-representation, self-distillation, EMA-teacher, observation-history, single-video-step, human-robot-co-training
- Model size: Wan2.2-TI2V-5B / Wan2.1-I2V-14B video backbone + 16 / 24-layer action DiT; total unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

動画モデルの1回のforwardから行動decoderへ渡す未来表現を改善するFRED。ノイズから得た表現を、未来観測を見るEMA教師へ自己蒸留し、過去4枚と現在画像で条件付ける。動画側は動画予測と蒸留で学び、行動損失の勾配は渡さない。

**主な貢献**

DROID学習後の未見環境で14B版のOOD平均scoreは52.1%（DreamZero 10.4%）。OpenArmの人間動画だけにある技能では50.0%（DiT4DiT 19.4%）。各課題12試行で部分点を認める評価であり、二値完遂率とは区別する。

**確認記録**

- Checked: 2026-10-23 · Review: verified
- 2026-10-10〜23の選択増分調査。本文前に既存392件へcanonical arXiv・DOI aliasと正規化/近似題名をvalidate\_csv.py --candidateで照合し一致なし。arXiv absで全著者・v1初稿10-21 18:33:13 UTC・改訂なしを確認（Oct23掲載日と区別）。読解範囲 https://arxiv.org/html/2610.30320v1 §3–4、Appendix A/B/F/G。zero-shotは環境固有fine-tuneなし。人間転移は553 robot実演と1,187 human動画の同環境co-trainingで、対応付けは暗黙的。言語接地の制限が残る。公式repoの実装・学習経路、LICENSE Apache-2.0、NOTICEの外部コード条件をcommit 57ddd3d70c1f6066d65e06eaf81e5c5022b7906dで確認: https://github.com/suhyeok-jang/FRED/blob/57ddd3d70c1f6066d65e06eaf81e5c5022b7906d/LICENSE 。公式重み https://huggingface.co/FRED-AGI-LAB/fred-wan22-5b-droid revision 1d6fd1f363e38819273e6935389e97b993e547d0、5 safetensors shard計22,536,424,208 bytesとmodel card Apache-2.0を独立確認。14B-DROIDと5B-RoboCasaも実shard掲載確認。外部backbone等の条件は別。absの実PDF hrefを抽出・絶対URL化し、本体は取得せず。実行・数値再現なし。

### Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation

- ID: `WAM-0140`
- Published: 2026-10-21
- Authors: Chun Gu; Xiaofei Wei; Yiming Chen; Bozhou Zhang; Juntong Zhang; Xiatian Zhu; Li Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.29264) · [PDF](https://arxiv.org/pdf/2610.29264) · [Project](https://logosroboticsgroup.github.io/TIDE/)
- Tags: TIDE, online-post-training, human-in-the-loop, provenance-conditioning, video-action, world-action-policy, bimanual-manipulation
- Model size: 3B（本文のworld-action policy）
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

人間介入と方策実行の出所を区別するchunkで、動画世界backboneと行動expertを同じ配備session中に教師あり更新するTIDE。criticや報酬modelを学ばず、実行・記録・学習を非同期化しepisode境界で更新checkpointへ切り替える。

**主な貢献**

出所条件を動画・行動両系のflow時刻埋め込みへ加え、両方の実行経験を活用。実機4課題の各20自律rolloutでwarm-startと追加offlineデモを上回り、固定方策で収集後に学ぶ比較系とは同程度の最終性能で、更新を配備中に利用可能にした。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absで全著者とv1初稿2026-10-21 06:15:00 UTC、改訂なしを確認。本文前に既存376件とcanonical arXiv/DOI alias・正規化/近似題名をvalidate\_csv.py --candidateで照合し一致なし。https://arxiv.org/html/2610.29264v1 §III–VIと公式projectを選択精読。未来動画と行動を共同予測・最適化するworld-action policyなのでwam/action-coupling。1双腕UR5e・4課題・1backboneのみ。人間が成功確認したepisodeだけを学習に保持しselection biasがあり、反復session間変動や長期保持は未評価。milestone部分点とbinary完了率を分離。介入率低下は自律性能や学習の因果効果そのものではない。1時間未満は8 H100による配備rollout開始から最終checkpoint利用可能までで、初期setup・最終評価を含まない。公式GitHub https://github.com/LogosRoboticsGroup/TIDE commit ee65dcc6e2d1b34e07a0c8b60fb3d06f1d161ffc の全recursive tree・READMEはproject用HTML/CSS/JS/画像/動画のみで方策訓練/推論実装なし。従ってcode unavailable、重み/実装license unknown。公式repoはproject-site sourceのみなのでcode\_urlは空欄とし、実装releaseと誤認させない。サイトCC-BY-SAは実装licenseに流用しない。PDF/重みdownload・実行再現なし。 arXiv absの生HTMLで実在するPDF相対href /pdf/2610.29264 を抽出し絶対URLへ解決。PDF本体は取得しない。

### Relational Geometry Forcing for World Action Models

- ID: `WAM-0139`
- Published: 2026-10-21
- Authors: Yuan Xu; Yixiang Chen; Qisen Ma; Jiabing Yang; Peiyan Li; Kai Wang; Jianhua Yang; Jianlou Si; Jun Huang; Jing Liu; Nianfeng Liu; Yan Huang; Liang Wang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.29282) · [PDF](https://arxiv.org/pdf/2610.29282)
- Tags: RGF-WAM, relational-alignment, 3D-geometric-prior, video-action-model, training-time-supervision
- Model size: Wan2.2-TI2V-5B backbone + 1B Action DiT; frozen VGGT-1B teacher (training only)
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結3D基盤モデルの幾何知識を、特徴そのものの回帰ではなく特徴間の関係としてWAMへ転移する。フレーム内・視点間・行動時間方向の3つの整合損失を学習時だけ加え、推論時の幾何予測branchを追加しない。

**主な貢献**

点ごとの幾何特徴整合が行動学習を妨げる問題を関係整合で緩和。LIBERO、RoboTwin 2.0とFranka実機7設定で評価し、実機平均成功率はFast-WAMの57.14%に対し65.71%（各設定20試行）を報告した。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absのv1履歴・全著者、HTML https://arxiv.org/html/2610.29282v1 §3–5・実験表・実装設定を確認。LIBERO平均98.65%、RoboTwin 2.0平均92.71%は著者報告。実機は各課題50実演でfine-tuneし4基本課題とBowl-to-Rackの3汎化条件を評価。pairwise cosine関係が中心で、絶対的なmetric scaleと接触構造は未検討。abs/HTMLに公式project・実装・重みの公開先を確認できず、それぞれunknown。

### CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation

- ID: `WAM-0138`
- Published: 2026-10-21
- Authors: Houzhu Ding; Xinda Qi; Luqi Wang; Ming Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.30117) · [PDF](https://arxiv.org/pdf/2610.30117) · [Project](https://cw-wam-project.github.io/)
- Tags: CW-WAM, contact-wrench, force-sensitive-manipulation, paired-causal-attention, admittance-control, slow-fast-control
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

映像・動作・接触wrenchを共同予測するWAM。動作と力の履歴を対にして扱う注意機構と長期wrench記憶から同期した制御参照を生成し、予測力を20Hzのadmittance制御へ渡してモデル照会間の接触を調整する。

**主な貢献**

450実演・実機4課題で構造化した動作–wrench学習を評価。wrenchなしWAMに対して角柱挿入25%→70%、電源アダプタ挿入40%→95%。admittance追加は成功率を変えず、成功試行の力参照RMSEを角柱で4.8→2.7Nに低減した。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absのv1履歴・全著者、HTML https://arxiv.org/html/2610.30117v1 §III–VIの手法・実験・discussion、公式projectを確認。各接触課題20試行、荷重ごと10試行。評価は実演分布内の4課題で、feedback gainとcompliant方向は手動設定。新物体・新課題への汎化は今後の課題。projectのCodeはリンクのない表示で、公開実装・重み・実装ライセンスは確認できずunknown。論文ライセンスとは区別。

### Complementary Future Token Pruning for World Action Models

- ID: `WAM-0124`
- Published: 2026-10-14
- Authors: Baekseung Kim; Junhoo Lee; Sohyeon Hong; Suhyun Jeon; Minkyu Kim; Seungyeon Kim; Donghoon Han; Nojun Kwak
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.19957) · [PDF](https://arxiv.org/pdf/2610.19957)
- Tags: CF-Prune, future-token-pruning, training-free, attention-entropy, inference-acceleration, joint-video-action, Cosmos3
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

事前学習済みWAMの未来フレームtokenを推論時だけ間引くCF-Prune。動画の見た目をすべて復元する代わりに、行動生成に必要な領域を残して計算量を減らす。

**主な貢献**

最初のdenoising passで指示attentionと行動attentionから相補的なtoken集合を選ぶ。視点間・行動時刻間のattention entropy差で精密操作phaseを検出し、その間はdense計算へ戻す。

**確認記録**

- Checked: 2026-10-16 · Review: verified
- arXiv absの履歴でv1初稿2026-10-14（後続改訂なし）、全著者、PDFリンクを確認。PDFはweb取得上限を超えたため、一次HTML v1の3–4節とAppendix A.1を読んで手法・設定を検証: https://arxiv.org/html/2610.19957v1 。評価はCosmos3系checkpointを用いたRoboLab、RoboCasa、Franka実機3課題。追加学習不要はpruning処理についてであり、RoboCasa/実機用base policyはfine-tuneされている。精密phase判定の閾値は評価環境別。abs/HTMLに公式project・実装・重みの公開先を確認できず、タイトル/CF-Pruneによる限定検索でも公式配布先未確認のためURL空欄・各statusはunknown。arXiv論文ライセンスを実装ライセンスと混同しない。

### Box-WAM: Box Trajectories as Compact State Representations for World Action Models

- ID: `WAM-0129`
- Published: 2026-10-13
- Authors: Qinxi Yu; Wenzhou Ding; Gloria X. Wang; Albert J. Zhai; Shenlong Wang
- Venue: CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2610.17526) · [PDF](https://arxiv.org/pdf/2610.17526) · [Code](https://github.com/quincy-u/box-wam) · [Project](https://box-wam.github.io/)
- Tags: BoxWAM, object-centric-futures, oriented-bounding-box, rectified-flow, state-guided-attention, pi0.5-integration
- Model size: 3.35B (pi0.5 + BoxWAM, 27,500-demo setting); standalone unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

未来動画全体の代わりに、操作対象の3D有向boxの8頂点を画像平面へ投影した軌跡と行動を共同生成する。状態から行動への一方向attentionで物体の未来運動を方策へ渡し、単一課題モデルとπ0.5への追加を検証する。

**主な貢献**

2,500実演のRoboTwin多課題比較で、π0.5への追加によりclean成功52.6→61.5%、randomized成功26.9→34.0%、遅延55.3→57.7 msを報告。学習用box注釈は追跡・RGB-D・既知mesh等に依存し、強い遮蔽や変形物体への適用は未確立。

**確認記録**

- Checked: 2026-10-19 · Review: verified
- 2026-10-06〜19の選択増分調査。本文前にcanonical arXiv/version/DOI alias・正規化/近似題名を既存355件と照合し一致なし。初稿・著者・v1のみの履歴はarXiv abs、方法§3・評価§4・制約§6は https://arxiv.org/html/2610.17526v1 で確認。CoRL 2026はPDF headerと公式projectに明記。実装とMIT LICENSEを確認: https://github.com/quincy-u/box-wam/blob/main/LICENSE 。code release 2026-10-11、最新確認commit 7afa9c62884e7d23851034200628bc69cdd60731 (10-15)。READMEの重み候補 https://huggingface.co/quincyu/pi05\_robotwin\_obb\_eef と https://huggingface.co/quincyu/box-wam-standalone はAPIが双方401で実ファイルmetadataを確認できずweights=unknown。第三者noticeはπ0.5派生重みにGemma条項、別取得DINOv3重みに専用条項を明記し、実装MITと区別する。 実行・数値再現なし。 遅延はRTX Pro 6000 Blackwell・既定10 denoising stepの条件。

### Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence

- ID: `WAM-0126`
- Published: 2026-10-13 · Updated: 2026-10-14
- Authors: Thinker Team Ubtech; Peng Gao; Jichao Jiao; Chen Liao; Daqin Luo; Yiming Ma; Baiyu Pan; Hailin Shi; Jiyuan Wang; Xiangming Xu; Xiongwei Zhao
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18447) · [PDF](https://arxiv.org/pdf/2610.18447) · [Code](https://github.com/UBTECH-Robot/Thinker-WM) · [Project](https://thinkercosmos.ubtrobot.com/thinker-wm/)
- Tags: world-action-model, depth, flow-matching, multi-embodiment, language-conditioned
- Model size: unknown
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

RGB・深度・ロボット行動を共通の動的表現で生成する世界行動モデル。言語は凍結VLMによる条件として使い、同じ重みで未来予測と行動推論を切り替える。

**主な貢献**

モダリティ別の入出力と共有Transformerを組み合わせ、深度を補助損失だけでなく生成対象にする。共通の相対手先行動表現で異種ロボットを接続し、選択された生成評価とRoboTwinの単一タスクで幾何情報の効果を検証する。

**確認記録**

- Checked: 2026-10-17 · Review: needs-review
- arXiv history confirms v1 2026-10-13 and v2 2026-10-14; selected v2 architecture and evaluation sections read, not numerical reproduction. Official inference repository at 44cdb519d73c16bb63738e5dd66f84ede21dae12 contains main.py and model modules; root LICENSE is CC-BY-NC-SA-4.0 (noncommercial), not an open-source implementation license. README links https://huggingface.co/UBTECH-Robotics/Thinker-WM/tree/main but weight-file access failed; weights remain unknown. README retains a placeholder download command and inconsistent BibTeX eprint; paper identity follows arXiv, not that eprint. Total parameter count unverified. Project page rendered poorly; official repository cross-links it. No benchmark-wide superiority or unseen-task guarantee is asserted.

### UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models

- ID: `WAM-0120`
- Published: 2026-10-13
- Authors: Jingbo Xu; Jianjie Fang; Zhuohang Li; Zihao Song; Zhaolu Wang; Xvyuan Liu; Xin Zhang; Haisheng Su; Yinzhou Tang; Chen Gao; Wei Wu; Yong Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18697) · [PDF](https://arxiv.org/pdf/2610.18697)
- Tags: mixture-of-experts, world-action-model, action-conditioned-world-model, adaptive-routing, diffusion-transformer, real-robot
- Model size: ~16.2B parameters for MoE (external encoders/VAE excluded)
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

行動条件付き世界モデルと4種類の世界行動モデルを、動画・行動の可視性マスクで区別しながら、共有Transformerと能力別expertで共同学習する。配備時には凍結した基盤モデルの4つの行動生成インターフェースから、課題に応じて各実行チャンクで選ぶ。

**主な貢献**

共有ダイナミクス、能力整合トークンルーティング（CATR）、チャンク単位の選択器PAIRを組み合わせる。著者らの3実機課題では最良のインターフェースで平均成功率88.3%（比較対象の最良76.7%）を報告し、世界予測との共同学習が各行動インターフェースに寄与するアブレーションを示す。インターフェース間の比較はすべて同一計算量条件とは限らない。

**確認記録**

- Checked: 2026-10-15 · Review: verified
- https://arxiv.org/abs/2610.18697 v1 only, submitted 2026-10-13 UTC; “under review at ICLR 2027” is not acceptance. https://arxiv.org/html/2610.18697v1 §§3-5 and App. G.4 verify five interfaces, PAIR, reported real-robot results and approximate 16.2B MoE parameter count excluding external encoders/VAE; not a parameter-matched dense baseline. ArXiv HTML supplies PDF href; PDF web parser errored. No official paper-specific implementation, weights or implementation license verified in arXiv HTML/abstract and exact-title searches; statuses unknown, not unavailable. Recheck release later.

### GreenWAM: A World Foundation Model for Robotics

- ID: `WAM-0119`
- Published: 2026-10-13
- Authors: Gennady Sidorov; Valerii Kornilov; Denis Grankin; Polina Fedotova; Aleksey Postnikov
- Venue: Technical report / arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18774) · [PDF](https://arxiv.org/pdf/2610.18774) · [Code](https://github.com/greenvla/GreenWAM) · [Project](https://greenvla.github.io/GreenWAM/)
- Tags: world-foundation-model, cross-embodiment, shared-action-space, video-action-model, humanoid, real-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / available / unknown

**概要（日本語）**

20種類のロボット群の関節動作を共通の解剖学的行動空間に写し、視覚予測・行動条件付き世界予測・世界行動生成を共同学習する基盤モデル。Cosmos 3 Edgeを適応し、世界モデルとしての予測と、行動専門家を分離した方策への転用を検証する。

**主な貢献**

ロボットごとに別の行動投影パラメータを持たせない共通表現と、動画生成器から分岐する行動expertを提示。著者らはWorldArena 1.0、RoboTwin 2.0、LIBERO、CALVIN、および実機ヒューマノイドで評価。ただし課題幾何の変化に敏感で、実機検証は1種のヒューマノイドの梱包課題に限られる。

**確認記録**

- Checked: 2026-10-15 · Review: verified
- https://arxiv.org/abs/2610.18774 v1 only, submitted 2026-10-13 UTC; https://arxiv.org/pdf/2610.18774 §§4-8 supports recipe, evaluations and limitations. Official project links https://github.com/greenvla/GreenWAM with public evaluator/source tree; repo README says training recipes/data and robotics-stage base checkpoint are not released. https://huggingface.co/SberRoboticsCenter/GreenWAM/tree/main/robotwin directly lists two .safetensors files; other task folders listed. Code/weights declared OpenMDW-1.1 in repo/HF card. OpenMDW-1.1 was submitted for OSI approval in 2026-08 (https://lists.opensource.org/pipermail/license-review\_lists.opensource.org/2026-August/006125.html), but OSI-approved implementation status not verified; under schema open\_source stays unknown, not true. PDF URL opened. No independent benchmark reproduction.

### ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation

- ID: `WAM-0117`
- Published: 2026-10-13
- Authors: Zijun Xu; Wendi Chen; Xinkai Wang; Jiachen Zou; Hongjin Chen; Hairuo Liu; Bokai Lin; Shihao Ma; Ke Ma; Zhiwei Zhang; Zhuohao Yan; Ke Wu; Haoming Song; Xueqi Li; Chuan Wen; Jieru Zhao; Wenchao Ding; Cewu Lu; Lixin Yang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18852) · [PDF](https://arxiv.org/pdf/2610.18852) · [Project](https://force-wam.github.io/)
- Tags: world-action-model, force-feedback, inverse-dynamics, play-data, contact-rich-manipulation, real-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

成功実演から手首画像と6軸の力・トルクの将来系列を予測する世界モデルと、実演・目的なしのplayデータから行動を学ぶ逆動力学モデルを分ける。実行時には予測した視覚・力の将来を目標に、最新の力覚を使って行動を逐次補正する。

**主な貢献**

課題の望ましい接触結果と局所的な行動―力応答を別のデータ源から学習する構成を提案。著者らの実機4条件（各20試行）で成功率85–95%を報告し、playデータ追加で課題のみのモデルより15–45ポイント上昇。ただしこの結果は特定4条件での比較。

**確認記録**

- Checked: 2026-10-15 · Review: needs-review
- https://arxiv.org/abs/2610.18852 v1 only, submitted 2026-10-13 UTC; https://arxiv.org/html/2610.18852v1 §§3-4 and Table 1 verify model factorization, play ablation, four real-robot conditions and 20 trials per condition. Official https://force-wam.github.io/ says “Code coming soon” and contains no code-release link, despite arXiv abstract saying code available; no implementation/checkpoint file or implementation license verified. Recheck project for release. The PDF href is supplied by arXiv; web PDF parser errored, HTML full text was read instead. Paper CC BY is not an implementation license.

### LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts

- ID: `WAM-0116`
- Published: 2026-10-13
- Authors: Wenxuan Guo; Yingping Liang; Zhaoguo Wang; Ziyuan Li; Angyuan Ma; Zhenyu Wu; Chengkun Wang; Bingyao Yu; Ze Chen; Borui Zhang; Xiuwei Xu; Meng Zhang; Erjin Zhou; Jiwen Lu
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.18873) · [PDF](https://arxiv.org/pdf/2610.18873) · [Code](https://github.com/loop-wam/LoopWAM) · [Project](https://loop-wam.github.io/)
- Tags: world-action-model, closed-loop-learning, deployment-rollouts, mixed-quality-data, video-action-generation, real-robot
- Model size: Wan2.2-TI2V-5B video backbone; total model size unverified
- Open-source: unknown
- Code / weights / license: available / unknown / unknown

**概要（日本語）**

実演と配備後の成功・不十分・失敗ロールアウトを合わせ、動画と行動を並列に生成する世界行動モデル。ロールアウトの質に応じて行動模倣を弱めつつ、結果動画による世界モデルの学習は全品質で維持し、収集・再学習・再配備を繰り返す。

**主な貢献**

動画・行動の双方向注意、データ源別のノイズ付与、品質条件付けと品質加重の行動損失を統合。著者らのRoboChallenge Table30-V2実機評価では3回の配備・再学習で成功率23.67%から43.33%へ上昇。RoboTwin 2.0とRoboCasa365の報告値はそれぞれ94.5%と49.5%で、後者2件はシミュレーション評価。

**確認記録**

- Checked: 2026-10-15 · Review: verified
- https://arxiv.org/abs/2610.18873 v1 only, submitted 2026-10-13 UTC; https://arxiv.org/html/2610.18873v1 §§3-4 verifies method, setup and author-reported results. Official https://loop-wam.github.io/ links public https://github.com/loop-wam/LoopWAM with training/evaluation source files. Repo root has no observed LICENSE; implementation OSI license unverified (paper CC license is separate). Repo README claims checkpoints; https://huggingface.co/datasets/loop-wam/loopwam/tree/main lists checkpoint-named folders but nested checkpoint files could not be opened, so weights\_status remains unknown; recheck exact .pt files. arXiv PDF link was opened. No independent reproduction of benchmark metrics.

### RAP-WAM: Learning World-Action Models through Predictive Rehearsal and Action Perturbations

- ID: `WAM-0130`
- Published: 2026-10-12 · Updated: 2026-10-15
- Authors: Yuanpeng He; Ceyao Zhang; Fangjing Li; Kefei Zhu; Lijian Li; Yueheng Li; Tianjia He; Wenpin Jiao; Zhi Jin; Yaodong Yang; Yuanpei Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.16443) · [PDF](https://arxiv.org/pdf/2610.16443v2) · [Code](https://github.com/heyuanpengpku/RAP-WAM) · [Project](https://rapwam.github.io/)
- Tags: RAP-WAM, predictive-rehearsal, action-response-credit, future-supervised-queries, coupled-action-projection, agent-guided-post-training, task-policy-selection
- Model size: Wan2.2-TI2V-5B backbone; total unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

動画事前学習backboneで未来観測と行動を学び、生成観測で次区間を練習しつつ実演の正解を維持する。行動摂動への予測応答・誤差・過去の誤差priorから時空間の教師重みを作り、未来教師queryとCAPで行動へ接続する。

**主な貢献**

42 RoboDojo課題で固定base成功12.85%、agent精緻化と課題別checkpoint選択を含む系15.62%を報告。15実機課題の89.00%は課題macro平均で試行数・不確実性は未提示。応答重みの因果的有効性や独立testでのpolicy選択は未確立。

**確認記録**

- Checked: 2026-10-19 · Review: verified
- 2026-10-06〜19の選択増分調査。本文前にcanonical arXiv/version/DOI alias・正規化/近似題名を既存355件と照合し一致なし。初稿10-12、v2改訂10-15はarXiv abs。方法§3、評価§4、Appendix A/Hを確認: https://arxiv.org/html/2610.16443v2 。PDF linkはarXivが12,648,248 bytesを返したが取得上限超過、HTMLを精読。公式MIT実装を10-18公開、確認commit cd32fba405b26f8c3e4ee29120ffc7432a126f47: https://github.com/heyuanpengpku/RAP-WAM/blob/main/LICENSE 。公開範囲はbase学習と28D実機training workflowで、robot制御・sim評価・agent介入・課題別policy保持・学習済みtask checkpointを含まない: https://github.com/heyuanpengpku/RAP-WAM/blob/main/docs/REPRODUCIBILITY.md 。公開recipeは論文のbatch/split/cache/選択法と差があり再現実証ではない。task重みの実metadata未確認、外部Wan重みを代用せずunknown。 実行・数値再現なし。 RoboDojoの12.85/15.62%は5能力群の平均を等重み平均した値で、全episodeのpooled成功率ではない。

### Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding

- ID: `WAM-0142`
- Published: 2026-10-09
- Authors: Feng Jiang; Shu Chen; Yuanfei Wang; Yuan Li; Zhenhao Shen; Jiaqi Liang; Yang Chen; Lei Wei; Chen Xie; Ruihai Wu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.13164) · [PDF](https://arxiv.org/pdf/2610.13164) · [Project](https://fffstrong.github.io/Grounded-Dreamer/)
- Tags: Grounded-Dreamer, synthetic-robot-data, inverse-dynamics, simulation-replay, physical-grounding, VLA-training
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

少数の実画像から操作対象・カメラをシミュレーションへ再構成し、物理的に有効な軌跡で動画モデルと逆動力学モデルを調整する。生成動画から復元した行動をシミュレーションで再実行し、成功軌跡だけをロボット方策の合成学習データとして用いる。

**主な貢献**

interaction-aware maskingと物理replay検証で、teleoperation実演なしの合成データを構成。Franka実機7課題でDiffusion Policyとπ0.5を評価し、π0.5のボタン押しは合成50軌跡と実演50軌跡の双方で75%（各20試行）を報告した。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- arXiv absのv1履歴・全著者、HTML https://arxiv.org/html/2610.13164v1 §3–4、データ条件・mask/replay ablation・scalingを確認。合成のみと少数実演co-trainingは別条件。7課題中ボタン以外では合成のみが実演のみを必ずしも上回らず、2課題のscalingは約150軌跡で飽和傾向。実画像由来の再構成・task記述・物理simulatorを要し、全工程が実データ不要ではない。公式projectにCode Coming soonと明記されるためcode\_status=unavailable。重み・実装ライセンスは未確認。

### LeapBot-JAC: Joint Action Chains for World Action Models

- ID: `WAM-0113`
- Published: 2026-10-09
- Authors: Chenhao Zhu; Baibing Liu; Pei Liu; Rui Yang; Lang Zhang; Mingyue Feng; Yaonong Wang; Jun Ma
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12886) · [Code](https://github.com/LeapWM/leapbot-jac)
- Tags: LeapBot-JAC, joint-action-chains, fixed-token-budget, physical-time-alignment, directed-attention, FastWAM, LeapBot-WA, LIBERO-Plus
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unspecified

**概要（日本語）**

固定の行動token予算を疎な未来参照chainと密な実行chainへ分け、同じaction expertで物理時間を揃えて共同denoisingする。実行側が参照側を読む有向attentionを加え、実行chainのprefixだけをロボットへ送る。

**主な貢献**

WAMの世界予測処理とparameter/token数を維持し、予測行動に参照・実行の役割を付ける。FastWAMとLeapBot-WAに組み込み、特にzero-shot摂動下の頑健性を検証。

**確認記録**

- Checked: 2026-10-12 · Review: verified
- arXiv初稿v1=2026-10-09 02:21:19 UTC、改訂なし。一次HTMLの公式codeリンクを検証。公開repoの唯一のmain branch/treeは13-byte READMEのみで実装・LICENSEなし: https://github.com/LeapWM/leapbot-jac 。重みの公開を独立確認できずunknown。LIBEROは両host98.3%、LIBERO-PlusはFastWAM53.5→70.4%、LeapBot-WA73.1→77.3%。同一学習seedの比較で、98.3%の再掲は独立再現実験ではない。疎な参照はsemantic subgoalではなく予測control、strideとsupervision等の効果分離に限界。実機2課題各model200試行。PDFリンクはarXiv absで確認したがfetchがcache missのためpdf\_url空欄。https://arxiv.org/html/2610.12886v1

### Forward Dynamics Models

- ID: `WAM-0112`
- Published: 2026-10-09
- Authors: Zipei Ma; Junzhe Jiang; Jiahui Zhang; Juntong Zhang; Chun Gu; Bozhou Zhang; Jiankang Deng; Xiatian Zhu; Li Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.13117) · [Code](https://github.com/LogosRoboticsGroup/FDM) · [Project](https://logosroboticsgroup.github.io/FDM/)
- Tags: FDM, action-to-future, asymmetric-attention, future-supervision, action-only-inference, VLM, VGM, LIBERO, RoboTwin
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / unavailable / unknown

**概要（日本語）**

行動featureを入力に未来状態を予測し、その損失を行動featureへ逆伝播させるaction-to-future学習。非対称attentionで予測未来から行動への依存を遮断し、π0.5系とWan2.2系の両方で、推論時は未来生成を省く。

**主な貢献**

未来を行動条件にする向きを反転し、観測された結果を方策の訓練信号として活用。future headの誤差伝播を構造的に避けるaction-only推論を、VLM/VGMの双方へ実装。

**確認記録**

- Checked: 2026-10-12 · Review: verified
- arXiv初稿v1=2026-10-09 07:12:16 UTC、改訂なし。一次HTML・公式project・Pi05\_causal.py/WanMoT\_causal.pyの実装を確認。LICENSEはMIT見出しだがupstream commit履歴維持の追加条件があり、標準MIT/OSI扱いを未確定としてunknown: https://github.com/LogosRoboticsGroup/FDM/blob/FDM/LICENSE 。公式READMEはtrained FDM checkpointの公開download link未提供と明記: https://github.com/LogosRoboticsGroup/FDM 。LIBERO平均はVLM版99.4%、VGM版98.1%。実機は双腕ARX-X5の5課題各20試行、平均96%/83%、VGM推論253.45ms/chunk対FastWAM-Joint446.55ms。sim学習seed42、公開configと論文runの差に注意。PDFリンクはarXiv absで確認したがfetchがcache missのためpdf\_url空欄。https://arxiv.org/html/2610.13117v1

### SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices

- ID: `WAM-0111`
- Published: 2026-10-09 · Updated: 2026-11-07
- Authors: Timi Owolabi; Hikmah Olawore; Frances Adelakun; Ayotomiwa Oyewumi
- Venue: NeurIPS 2026 Workshop on Robot Learning with World Models
- Links: [Paper](https://arxiv.org/abs/2610.13740) · [PDF](https://arxiv.org/pdf/2610.13740v2) · [Code](https://github.com/iitimii/SmolWAM) · [Project](https://smolwam.vercel.app/)
- Tags: SmolWAM, Cosmos-Policy, distillation, model-compression, single-step-flow, latent-future, LIBERO, edge-inference
- Model size: 0.88B network; excludes 54M VAE encoder and BERT-base
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

Cosmos Policyの動画拡散trunkを剪定・蒸留し、単画像潜在、attention sinkを保つ言語キャッシュ、状態条件付きqueryから16ステップの行動と両カメラの未来潜在を1回のforwardで予測する軽量WAM。

**主な貢献**

剪定とトークン圧縮で1回推論を実現。v2で、将来潜在などの世界予測側の教師信号を外した場合の対照実験と、単ステップ教師・複数GPUとの効率比較を追加した。

**確認記録**

- Checked: 2026-11-19 · Review: verified
- arXiv v1=2026-10-09、v2=2026-11-07。https://arxiv.org/html/2610.13740v2 の評価・効率分析を確認。LIBERO 400エピソードで95.5%、世界側の教師信号なし89.3%。単一評価シードで、未来画像損失だけの効果を分離した比較ではない。テキストキャッシュ・batch 1の16行動チャンクでA100 57ms、L4 83ms、T4 188ms。単ステップ・単フレーム教師は各126/243/552ms。Jetsonや実機は未評価。実装Apache-2.0 https://github.com/iitimii/SmolWAM/blob/main/LICENSE 。公式重み https://huggingface.co/timiiowolabi/SmolWAM/tree/main はNVIDIA One-Way Noncommercial Licenseで別条件。2026-11-06〜2026-11-19 UTCの選択差分調査。arXiv cs.ROのrecent・月別一覧と分野別検索（VLA適応、WAM/潜在予測、Agent実行監視、Hybrid）、採用候補の公式実装・重みを確認。全件・全改訂を網羅せず。

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
- Links: [Paper](https://arxiv.org/abs/2610.12099) · [Code](https://github.com/DexForce/UNITAS) · [Project](https://unitas-wam.github.io/)
- Tags: 3d-native, metric-world-frame, scene-flow, action-flow, cross-embodiment
- Model size: 1.7B
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

観測、手/グリッパの3D点軌道、scene flowを同じmetric世界座標で表す3D-native WAM。身体や視点に依存しにくいmotion interfaceで、直接行動生成と行動条件付きscene予測を統合する。

**主な貢献**

world-aligned3D位置埋め込みとphysical-time trajectory tokenで行動/scene動態を結合。RoboTwinの点軌道予測とLIBERO/実機操作を評価し、RoboTwin Moving ADEは0.427cm（PointWorld0.656cm）。

**確認記録**

- Checked: 2026-10-15 · Review: needs-review
- arXiv v1初稿・著者・題名を維持: https://arxiv.org/abs/2610.12099 (2026-10-08、2026-10-15時点でv2なし)。HTML§3/4.4/5/6は2026-10-09に選読: https://arxiv.org/html/2610.12099v1 。scene-flow定量評価はsimulator groundtruthを用い、video baselineの3D化は初期GT depth校正を用いる。長期相互作用/広い実機deploymentは今後の課題。2026-10-13公式release commit https://github.com/DexForce/UNITAS/commit/8c480eed6bfa06461313360045512ae7c62a06a8 のinference/evaluation実装、model、scene-flow処理、およびroot LICENSE Apache-2.0を確認済み。2026-10-15追補: 公式GitHub README https://github.com/DexForce/UNITAS のcheckpointリンク先HF https://huggingface.co/RobbinWang123/Unitas/tree/main に7個の実ファイル(.pt; RoboTwin/LIBERO/VLABench各scratch/finetunedとscene\_flow、各約6.96GB)を独立確認しweights\_status=availableへ更新。個別ファイル https://huggingface.co/RobbinWang123/Unitas/blob/main/unitas\_robotwin\_scratch.pt と https://huggingface.co/RobbinWang123/Unitas/blob/main/unitas\_scene\_flow.pt にXet pointer size/SHA256とdownload linkがある。model repoのMIT表示はcheckpoint配布情報であり、GitHub実装のApache-2.0とは別。公式project https://unitas-wam.github.io/ の論文identity/公式codeリンクを確認したためproject\_url追加。同projectのCheckpoint Coming soonはHF実ファイルと不整合で更新遅れと思われるが、動作/論文性能再現は未検証。training code/datasetは未公開、Florence-2-largeとsimulator資産は別途必要。needs-review: training code/datasetの正式公開、checkpoint条件の詳細と再現範囲、projectの表記整合を次回確認。PDF/weights/data未download、GPU再現なし。

### HWAM: Humanoid World Action Model With Joint State--Action Generation

- ID: `WAM-0096`
- Published: 2026-10-08 · Updated: 2026-10-12
- Authors: Yan Yang; Jikun Rong; Minzhao Zhu; Zheyi Zhao; Qirui Hu; Zihan Lan; Weixin Mao; Yinhao Li; Zhen Fu; Hua Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12026) · [Project](https://hwam.vercel.app/)
- Tags: humanoid, joint-state-action-generation, execution-gap, forward-inverse-dynamics, whole-body
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

高水準の運動参照と低水準制御後に実現する身体状態のずれを扱う人型World Action Model。行動と時間整列した実行後の固有受容状態を共同生成し、Policy/FDM/IDMの3経路で身体動作と視覚未来を結ぶ。推論時は未来動画を生成せず、行動だけを制御器へ渡す。

**主な貢献**

実行後状態を行動と同じdenoise対象にした設計を検証。OLIのCandy Pickingは84/119成功（70.6%、Fast-WAM52/120）で、共同状態targetの効果が視覚学習recipeに依存することをablationで示す。ALOHA衣服折りも課題別学習で評価する。

**確認記録**

- Checked: 2026-10-22 · Review: needs-review
- arXiv履歴（初稿2026-10-08、v2改訂2026-10-12）、v2 HTML §§3–5/Appendix C–Dを選読: https://arxiv.org/html/2610.12026v2 。取得できたv1/v2 HTML本文の比較では版表示以外のテキスト差を確認できず、原TeX/PDF差分は未監査。Candy PickingのHWAM 95% Wilson区間は61.9–78.0%、訓練seed分散ではない。Plush-Toyの状態共同targetはVGM/Policy下60.0→45.5%、FDM/IDM/Policy下55.0→73.3%で単独効果とは断定しない。未来video診断12episodeの予測軌道条件ではPSNR優位なし。ALOHAは640demoで課題別学習し、86.0は部分点付き0–100 scoreで成功率でもOLIからのzero-shot転移でもない。OLIも3課題のtask別学習で身体間一般化保証ではない。公式 https://hwam.vercel.app/ は依然Code/Dataset Coming soonで、本文のavailable記述と整合せずneeds-review。実装unavailable、重み/実装license unknownを維持。独立再現・PDF保存なし。

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

### KineWorld: Action-Induced Transport Fields for Embodied World Modeling

- ID: `WAM-0110`
- Published: 2026-10-05
- Authors: Ziying Song; Yuchen Liu; Zhuoran Xu; Ziyang Liu; Jian Jin; Jiangtao Su; Haibao Yu; Lei Yang; Yuanpei Chen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06349) · [PDF](https://arxiv.org/pdf/2610.06349) · [Code](https://github.com/modaxiansheng/KineWorld) · [Project](https://modaxiansheng.github.io/KineWorld/)
- Tags: KineWorld, kinematic-transport, action-conditioned-video, flow-matching, RoboTwin-2.0, Wan2.2, reproduction-gap
- Model size: 5.001B active denoiser; VAE/text encoder/optional action expert excluded (paper A.6)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

初期画像・言語・候補行動から未来RGBを生成する世界モデル。KTLがロボットのみのレンダリングとRAFTからカメラ整列transportを作り、TAWDがその領域へ未来RGBの学習損失を配分する。RoboTwin 2.0のALOHA–AgileX双腕データで動画予測を評価した。

**主な貢献**

行動由来の運動情報を生成条件だけでなく学習時の空間的監督配分に利用する。uniformとtransport-focused分布を混合し総token重みを保持するTAWDは、推論時の追加パラメータやdenoising stepを要しない。

**確認記録**

- Checked: 2026-10-12 · Review: needs-review
- arXiv v1 2026-10-05の書誌とSec.4–5、Appendix A.3/A.5–A.10を選読。EWMScore-PとTWB-Scoreは別プロトコルの動画集約指標で、実機closed-loop成功率ではない。retained profileと50-update matched continuationを区別。transportはロボット支持領域に限定し物体運動・接触を直接表現せず、FPSはoffline transport準備を除く。公式公開READMEはuniform future-RGB学習でTAWD未提供と明記し、論文再現は未確立: https://github.com/modaxiansheng/KineWorld/blob/main/README.md 。LICENSE全文Apache-2.0とNOTICEをGitHub APIで確認: https://github.com/modaxiansheng/KineWorld/blob/main/LICENSE 。公式HF https://huggingface.co/pumpkin601/KineWorld のmodel cardと公開READMEがstep-500 release、固定revision・SHA256とApache-2.0を宣言することを確認。2026-10-12に固定revision 37e8f86c6c3cf45cde743162bf9b6de583cf1b73の公式HF tree APIを再確認し、step-500.safetensors（13,113,498,528 bytes、LFS SHA256 86294739c54073c836a0dcb3f9114c6cf2bf83d1a8698423b71698e5f88460a3）とaction\_norm\_stats.npzの公開file metadataを確認したためweights\_status=available。https://huggingface.co/pumpkin601/KineWorld/tree/37e8f86c6c3cf45cde743162bf9b6de583cf1b73 。論文結果再現なし、外部Wan等は別条件。重み未download/実行。公開実装と論文の差をneeds-reviewとして保持。

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

### WSA₁: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control

- ID: `WAM-0127`
- Published: 2026-07-04 · Updated: 2026-10-13
- Authors: Jiahao Jiang; Jianing Zhang; Xuanhan Wang; Duo Peng; Ruidong Chen; Zhenhan Yin; Sen Wang; Zhaoshu Yu; Pengpeng Zeng; Xiaofeng Cao; Jingkuan Song; Heng Tao Shen
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2607.03941) · [PDF](https://arxiv.org/pdf/2607.03941) · [Code](https://github.com/zaleni/WSA)
- Tags: WSA1, 3D-world-model, bidirectional-dynamics, mixture-of-transformers
- Model size: 3B / 6B (paper-reported)
- Open-source: unknown
- Code / weights / license: available / available / unknown

**概要（日本語）**

行動条件付き3D潜在状態予測、3Dに接地した将来視覚表現、3D逆動力学による行動生成を共同学習するWorld-Spatial-Actionモデル。実機1,000時間を含む計6,000時間のデモで事前学習し、シミュレーション・実機・未学習機体への転移を評価した。

**主な貢献**

共有3D表現と双方向attentionを介し、行動が世界を変える順動力学と、目標世界から行動を得る逆動力学を3専門器のMoTで統合する。

**確認記録**

- Checked: 2026-10-17 · Review: needs-review
- arXiv v2の書誌・履歴、本文 https://arxiv.org/html/2607.03941v2 3.2–3.4、4.1–4.2を選択確認。初稿2026-07-04、改訂2026-10-13。本文前にcanonical arXivと正規化/近似題名を既存347件と照合し一致なし、version/DOI aliasも同一性なしを再確認。公式repoにsrc/lerobot・launch・evaluationを確認。GitHub APIでcode HEAD 32211e42399bddb48382585639f79ea749f253f2、license APIは404。公式重み https://huggingface.co/zaleni/WSA-Base/tree/8760ce6703076a6ec8f0bdeda808e6fb9797804c のmodel.safetensorsは6,608,313,224 bytes、LFS hash付き実file metadataを確認。モデルcardのlicense欄なし、実装/重みの明示ライセンス未確認で論文CC BY-NC-NDとは区別。needs-review: 許諾範囲とrepo BibTeXの著者相違を再確認、著者はarXiv一覧を採用。重みdownloadや実行再現は未実施。

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
