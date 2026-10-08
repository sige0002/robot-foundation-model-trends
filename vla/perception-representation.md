<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / perception-representation

[← vla](README.md) · [CSV master](../papers.csv)

13 records · Published date 降順（同日 ID 降順）

### Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding

- ID: `VLA-0174`
- Published: 2026-10-07
- Authors: Theodor Wulff; Angelo Cangelosi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10178)
- Tags: mechanistic-interpretability, language-grounding, activation-patching, CKA, LIBERO
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

π0.5とGR00T N1.7に対し、同義語・上位概念・方向語・不存在物体・空指示による内部変化を調べる。LIBERO-10の1万オフライン試料でattribution patching、activation patching、CKAを組み合わせ、言語が行動計算に影響する層と表現変化を分析した。

**主な貢献**

内部の言語感度と行動への因果寄与を分離し、attribution patchingの近似精度がモデル依存であることを検証。activation patchingとのPearson相関はGR00Tで0.946、π0.5で0.089。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.10178v1 （4摂動とpatching、5実験設計、6.3比較、7議論、8今後の課題）。限界: 合成的で短いLIBERO指示のオフライン評価。意味を変えた指示も元の実演に対する誤差で評価するため、指示を適切に使ったかは閉ループ反実仮想試験が必要。 論文が挙げるHFモデルは分析対象の既存方策で、研究独自の重み公開とは扱わない。研究の実装・独自重み・実装ライセンス提供は未確認。

### YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding

- ID: `VLA-0172`
- Published: 2026-10-07
- Authors: Masatoshi Tateno; Takehiko Ohkawa; Yueh-Hua Wu; Hanlong Li; Tatsuya Matsushima; Yoichi Sato; Kei Ota
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09718) · [Project](https://yubi-stag.airoa.io/)
- Tags: video-language-grounding, contact-awareness, annotation, bimanual, language-steerability
- Model size: YUBI-VLM: Qwen3.6-27B backbone（VLA全体は未確認）
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

双腕操作動画の粗い課題ラベルを、接触対象マスク・接触区間・左右グリッパーの行動・物体属性や空間関係を含む注釈へ拡張する。多段処理をYUBI-VLMへ蒸留し、手首動画だけから注釈を生成する。その注釈をVLA後学習に使い、細かな言語指示への追従を調べた。

**主な貢献**

触覚センサーなしで接触を視覚推定し、時間・空間・意味の注釈を統合するデータ中心のVLA整合。実機部品sortingの各条件20試行で、handednessのみのfull success25%をcontact追加で60%へ改善。言語評価では操作完遂と完遂試行内のbin/gripper追従を区別する。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09718v1 （3.1接触対象分割・3.2蒸留、4ベンチマーク・5方策訓練、6.1注釈評価・6.2〜6.4実機・言語追従）。限界: 注釈の色混同や左右反転が方策誤りへ残る。相対位置・順序選択は完全には解けず、未知の長期構成評価はBUSの10試行など限定的。 公式projectを確認。掲載リンク内で実装・重みの配布先や実装ライセンスを確認できず各unknown。27Bは注釈用VLMのbackboneであり下流VLA規模とは区別。 分母再確認: https://arxiv.org/html/2610.09718v1\#S6.SS3 の本文はbin/gripper accuracyにcompleted trials条件を明示する一方、色accuracy82.9%対46.4%の分母は閲覧できた本文・captionでは明示されていないため、その数値はkey\_contributionから除外した。代わりに6.2/Fig.4の全20試行に対するfull successを掲載。

### DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies

- ID: `VLA-0167`
- Published: 2026-10-06
- Authors: Kaixi Feng; Guoheng Sun; Ziyao Wang; Yexiao He; Zheyu Shen; Ang Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09144)
- Tags: visual-grounding, soft-attenuation, intent-aware, OOD-robustness, OpenVLA-OFT
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

指示の意図と局所的な視覚証拠からパッチごとの関連度を推定し、入力の視覚tokenとバックボーン内部の視覚状態の双方を弱めたり保ったりする。tokenを削除せず全体文脈を残す構成で、OpenVLA-OFTの通常操作と視覚摂動下の頑健性を評価した。

**主な貢献**

外部grounding教師なしの関連度推定と、入力・内部状態の二重soft attenuation。LIBERO平均96.6→98.0%、zero-shot LIBERO-Plus69.6→72.6、UF850実機で各課題条件25試行。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09144v1 （MethodのGTP・relevance anchoring・dual-space attenuation、Experiments・実機・ablation、Conclusion限界）。限界: 固定した関連度予算は物体の大きさや散らかり具合、必要な領域の広さに適応できず、観測ごとの最適設定にはならない。検証はOpenVLA-OFT中心。 一次arXiv本文の提供リンクと題名・著者を限定した公開検索では、公式実装・独自checkpoint・実装LICENSEの提供を確認できず、別々にunknownとした。存在しないと断定したものではない。

### PAIR: Bridging Perception and Action in Vision-Language-Action Models

- ID: `VLA-0166`
- Published: 2026-10-06
- Authors: Kaixi Feng; Guoheng Sun; Ang li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09016)
- Tags: perception-action-alignment, action-latents, bridge-tokens, LIBERO, CALVIN
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

観測・指示から行動への中間表現を明示的に学ぶ。実演行動をmasked autoencoderで時系列latentへ変換し、視覚言語特徴から抽出したBridge Tokensをこれに整合する。行動expertの入口へ注入し、推論では行動autoencoderを外す。2つのVLA基盤と実機7課題で評価した。

**主な貢献**

課題意味と実行可能な行動構造を共有する、知覚由来の中間interface。VLA-AdapterのLIBERO-Plus59.1→64.2%、CALVIN平均完遂長4.42→4.53、実機OpenVLA-OFT51.4→65.0%。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09016v1 （3.1〜3.4手法、4.2〜4.5実機・表現probe・ablation、5結論）。限界: 実機はUF850、293実演から課題ごとに別方策を訓練し、各20試行。線形probeが示す行動情報の可読性は一般的な因果説明や未知身体への汎化を証明しない（評価範囲からの留保）。 一次arXiv本文の提供リンクと題名・著者を限定した公開検索では、公式実装・独自checkpoint・実装LICENSEの提供を確認できず、別々にunknownとした。存在しないと断定したものではない。

### Encoded but Not in Control: Revealing the Grounding Gap in Vision-Language Robot Policies

- ID: `VLA-0157`
- Published: 2026-10-05
- Authors: Shaohan Jiang; Jiahang Cao; Qiduo He; Fengting Deng; Kun Wu; Jingkai Sun; Jiaxu Wang; Qiang Zhang; Qihao Zheng; Chunfeng Song; Ping Luo; Andrew F. Luo
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06235)
- Tags: instruction-grounding, scene-prior, target-replacement, linear-probe, action-lens, VLA-WAM-evaluation
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

同一場面で有効な対象物だけを指示変更し、VLA/WAMが場面から推測した動作に従うか言語意図に従うかを診断する。行動lens・probe・attention・表現分解で、対象情報の符号化と実際の制御を分けて調べる。

**主な貢献**

LIBERO-Objectの変更対象成功率はπ0.5 11.5%、GR00T N1.7 0.5%、FastWAM 0%、LingBot-VA 1.3%。実機2 VLAでも新しい指示対象は5.8%・3.3%に留まり、probeで読める対象情報が選択を制御するとは限らないことを示す。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-10-05 12:37:55 UTC、改訂なし。本文 https://arxiv.org/html/2610.06235v1 の§3–7とAppendix Aを選択読解。4モデルをsimulation、2 VLAを6実機sceneで評価。代替対象が可視・到達可能な設定に限定し、attention/probeは因果機構の証明とは扱わない。WAMも評価するが統合modelを提案しないためvla/perception-representation、横断tagを付与。公式専用実装・重み・ライセンスは未確認。

### What the Guard Misses, the Robot Executes: Implied Harm in VLA Instructions

- ID: `VLA-0155`
- Published: 2026-10-05
- Authors: Sripad Karne; Arjun Balaji
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.05818)
- Tags: semantic-safety, implied-harm, text-guard, linear-probe, instruction-evaluation, π0.5
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ロボットの動作・物体・場面を固定し、指示された理由の有害性と明示度だけを変える安全性評価。text guardと内部表現probeを同じ指示に適用し、有害な目的の検出と実行の関係を調べる。

**主な貢献**

π0.5は有害性の明示度を変えても約95–97%で動作を完遂し、暗示された害を多くのguardが見逃した。2系列のモデルでは、言語/VLMからロボット後学習後に有害意図のprobe識別性能が低下した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-10-05 05:11:58 UTC、改訂なし。本文 https://arxiv.org/html/2610.05818v1 の§3–6とTable 1を選択読解。1つの模擬kitchen、5タスク、51理由、2 VLAに限定。OpenVLA-OFTは無害理由付きでも失敗し、拒否能力とは解釈しない。probeの語彙依存と少数negativeによる閾値不安定性あり。SPAIS 2026 workshop審査中。公式実装・専用重み・ライセンスは未確認。

### Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models

- ID: `VLA-0148`
- Published: 2026-10-02
- Authors: Yukiya Horiba; Koshiro Aoki; Shunsuke Yasuki; Bum Jun Kim; Taiki Miyanishi
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.03498) · [PDF](https://arxiv.org/pdf/2610.03498)
- Tags: adversarial-defense, sparse-autoencoder, linear-probe, conditional-intervention, robustness
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

Sparse autoencoderで敵対patchの存在と関連するVLA内部特徴を特定し、linear probeが攻撃を検知した時だけその特徴方向を推論中に抑制する。VLAの追加fine-tuningなしで、攻撃への対処と正常時の制御阻害のtrade-offを調べる。

**主な貢献**

LIBERO-10でπ0.5とSmolVLAへの断続的UADA攻撃を評価し、条件付き抑制が全4設定の成功率を改善。π0.5・10回攻撃では26.0%→32.4%。常時抑制の大きな性能低下を示し、介入する時点と強度の制御が重要と検証した。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- identity照合一致なし。v1初稿2026-10-02 15:57:04 UTC: https://arxiv.org/abs/2610.03498 、改訂なし。HTML §3/4/5選読: https://arxiv.org/html/2610.03498v1 。主評価は各条件10task×50初期状態=500rollout、攻撃は各victim用universal UADA patch。未知攻撃と実機は未評価。SmolVLAでは正常時41.4%→36.6%に低下し、ロバスト化が無害とはいえない。論文/手法名github検索で公式実装・重み・project・実装license未確認unknown。PDFファイル未保存。

### SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?

- ID: `VLA-0146`
- Published: 2026-10-02
- Authors: Chen Yang; Linzhe Shi; Changjie Wu; Hang Zhang; Ronghan Chen; Lingjun Zhang; Xu Hu; Mu Xu; Jiansheng Fan; Chen Wang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.02784) · [Project](https://simpletouch-robot.github.io/)
- Tags: tactile, contact-rich, future-latent-prediction, task-finetuning
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結したT3触覚encoderの全tokenを独立した触覚expertへ入力し、π0.5の行動expertと層ごとに接続する。行動教師信号と複数時点の将来触覚latent予測から、追加の触覚方策事前学習や別の視触覚整合段階を使わず課題単位に学習する。

**主な貢献**

各課題50デモでUniVTAC6課題の平均成功率77.5%を報告し、FTP-1の66.7%を10.8ポイント上回る。4実機課題では71.3%でFTP-1より8.8ポイント高い。将来触覚は学習用教師信号であり、実行時の未来触覚生成を必須にはしない。

**確認記録**

- Checked: 2026-10-05 · Review: needs-review
- identity照合一致なし。v1: https://arxiv.org/abs/2610.02784 (2026-10-02 04:19:13 UTC、改訂なし)。HTML §3/4/App.F選読: https://arxiv.org/html/2610.02784v1 。100simulation/20実機episode per task、各50demo。実機USB挿入は30%でFTP-1と同率。実機対象は視覚型触覚sensor付き平行jawのみで、巧緻手・別sensor・高周波触覚・力制御は未評価。著者リンク https://simpletouch-robot.github.io/ はweb readで2度取得失敗し、直接の公開GETでも2026-10-05時点HTTP 404、実際の公開実装/重み/ライセンスを独立確認できずunknown、project到達性をneeds-review。論文ライセンスと実装を分ける。PDFファイル未保存。

### SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation

- ID: `VLA-0164`
- Published: 2026-10-01
- Authors: Sofya Konstantinova; Miguel Altamirano Cabrera; Artem Lykov; Dzmitry Tsetserukou
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02360)
- Tags: SocialVLA, human-reaction, runtime-intervention, audio-video-fusion, VLA-hold, participant-directed-recovery
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人間の発声・表情・明示停止語を局所検出し、ロボットへの関連性を加えた非同期first-event融合でVLAを停止する。停止後の訂正発話を記録し、人間の明示要求で継続・再試行・指示変更を行う、方策非依存の社会知覚gatewayを提案する。

**主な貢献**

G1実機の15参加者・238反応episodeの凍結offline replayでrecall 54.6%、precision 69.5%。未見参加者1名では59.5%／91.7%、反応開始から物理holdまで中央値1.021秒。検出対象は人間が感じた介入必要性であり、全物理故障や認証済み安全性を評価したものではない。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.02360 のv1は2026-10-01 18:36:35 UTC、改訂なし。 https://arxiv.org/html/2610.02360v1 §III、IV/V、VIIを確認。III-Hで再開は参加者の明示操作、post-stop transcriptはmotion発行不可。自律planner/WAMを持たないためvla/perception-representation。prospectiveは22TP/2FP/15FN、hold latencyは反応検出とgate後の物理遅延を区別し、反応→holdの標本は14。false-stop率は非介入344.18秒に基づき不確実性が大きい。文化・年齢等の一般化は未確立、独立emergency stopを要する。正式題名/著者検索で公式実装、専用重み、実装ライセンスを未確認、unknown。PDF未取得。

### Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors

- ID: `VLA-0136`
- Published: 2026-10-01
- Authors: Edward W. Staley; Connor O. Pyles; Rahul Hingorani; Frank Camargo; Griffin Milsap; Jared Markowitz; Matthew S. Fifer; Michael Wolmetz
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01794)
- Tags: multimodal-conditioning, EMG, visual-annotation, human-in-the-loop, clutter
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

筋電の連続信号を固有感覚へ加えるEC-VLAと、対象物・置き場所の画像注釈を使うVA-VLAを比較する。詳細な言語指示を固定の曖昧な指示と追加モダリティへ置き換え、散らかった場面での意図伝達を調べる。

**主な貢献**

SO-101の実機で三参加者別SmolVLAを評価し、RoboCasaの16課題ではπ0.5へ視覚注釈を加えて比較。非言語の課題条件づけの効果を示す予備実証で、未知参加者への転移や汎用性は未検証。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.01794v1 のIII–IV節・付録VI-Aを確認。実機筋電条件とシミュレーション視覚注釈を区別。IROS WORLDS Workshop 2026発表はarXivコメントの記載のみなのでvenue=arXiv。本文リンクで専用実装・重み・実装ライセンス未確認。LeRobot/VLAbの利用を本研究の公開状態へ転用しない。PDF未取得。

### Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics

- ID: `VLA-0163`
- Published: 2026-09-30
- Authors: Songhua Yang; Ziyu Liu; Yuanwei Liu; Xuetao Li; Xuanye Fei; He Huang; Zheng Wang; Miao Li
- Venue: ICRA 2026
- Links: [Paper](https://arxiv.org/abs/2609.39178)
- Tags: adversarial-robustness, physical-object, security-evaluation, sim-to-real, RoboTwin, Pi0, RDT
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

物理的な視覚攪乱物体に対するVLAの脆弱性をsimulationと実機で評価する。軌跡・タスク遂行・動作制御への影響を測り、複数cameraでの見え方とsim-to-realの効果保持を比較した。

**主な貢献**

Pi0/RDTのRoboTwin 13選択課題で成功率が31.2–39.9ポイント低下。実機Aloha 5課題ではRDTが43.2%から17.6%、Pi0が60.2%から28.4%。実機に保持された攻撃効果比は81.4%・82.2%。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。初稿 2026-09-30 07:34:24 UTC、改訂なし。ICRA 2026採択はarXiv著者commentで確認し、publisher proceedingsは未確認。本文 https://arxiv.org/html/2609.39178v1 の§III、IV-A/FとTable I/IVを選択読解。simulationは50中13選択課題、各10seed。81.4–82.2%はsimulationの効果に対する保持率で、成功率の絶対低下ではない。2モデルと指定環境への評価で普遍的な安全性結論とは扱わない。公式実装・重み・実装ライセンスは未確認。

### GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments

- ID: `VLA-0131`
- Published: 2026-09-18
- Authors: Yichen Liu; Puzhen Yuan; Xiang Zhu; Yanjiang Guo; Jianyu Chen
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.21948) · [Code](https://github.com/PuzhenYuan/GALA) · [Project](https://puzhenyuan.github.io/GALA-website/)
- Tags: latent-action, geometry, cross-embodiment, human-video
- Model size: 5B (RoboCasa-GR1 inference checkpoint)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

RGBの場面変化と3D末端形状の動きを同時に符号化し、機体をまたぐ細かな潜在行動を学習するGALA。人の手、器用なロボット手、平行グリッパーのデータをVLA事前学習へ接続する。

**主な貢献**

統一末端動作表現UEMRと視覚・幾何の二種類の潜在行動を導入。行動ラベルのない人の一人称動画も利用し、機体別ネイティブ行動ヘッドで操作を学習。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Official project directly links official implementation and checkpoint. https://github.com/PuzhenYuan/GALA/blob/main/LICENSE verified Apache 2.0. https://huggingface.co/ypz21/GALA\_robocasa\_gr1 and /tree/main expose a 5B F32 model and four safetensors shards (19.3GB total); only listing read, no model downloaded. README still describes repository as private, conflicting with public file listing; public listing supports available status but access not download-tested. Weight license is unspecified in checked model card and is not inferred from code Apache license. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### UniVLA: Learning to Act Anywhere with Task-centric Latent Actions

- ID: `VLA-0117`
- Published: 2025-05-09 · Updated: 2025-11-03
- Authors: Qingwen Bu; Yanting Yang; Jisong Cai; Shenyuan Gao; Guanghui Ren; Maoqing Yao; Ping Luo; Hongyang Li
- Venue: RSS 2025
- Links: [Paper](https://arxiv.org/abs/2505.06111) · [PDF](https://arxiv.org/pdf/2505.06111) · [Code](https://github.com/OpenDriveLab/UniVLA)
- Tags: UniVLA, latent-actions, human-video, cross-embodiment, task-centric-representation
- Model size: 7B (univla-7b)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

ロボット・人間動画から、身体や視点の違いを越えて共有できるtask-centricな潜在行動を学ぶ。言語とDINO特徴でタスク無関係な変化を抑え、潜在行動を介して汎用VLAを事前学習して各身体へ適応する。

**主な貢献**

言語条件付きの潜在行動表現によって、行動ラベルのない異種動画をVLA学習へ取り込む。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式READMEに公開モデルzoo、訓練コード、7B backboneとRSS 2025。https://github.com/OpenDriveLab/UniVLA\#-model-zoo Code license: Apache-2.0; https://github.com/OpenDriveLab/UniVLA/blob/main/LICENSE.
