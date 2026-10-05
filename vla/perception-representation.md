<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / perception-representation

[← vla](README.md) · [CSV master](../papers.csv)

5 records · Published date 降順（同日 ID 降順）

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
