<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-wam

[← hybrid](README.md) · [CSV master](../papers.csv)

12 records · Published date 降順（同日 ID 降順）

### Juno: Taming Predictive Latents for Vision-Language-Action Models

- ID: `HYBRID-0126`
- Published: 2026-10-07
- Authors: Yuchen Zhu; Chenyi Xu; Yulin Zhang; Gang Xu; Wentao Zhu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.09940) · [Code](https://github.com/ZhuYuChenNO1/Juno) · [Project](https://juno-policy.github.io/)
- Tags: JEPA, predictive-latents, world-model, test-time-adaptation, failure-data
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unavailable / unknown

**概要（日本語）**

行動条件付きJEPAを、VLAの表現学習・未来状態の教師・配備後の動力学適応で共用する。局所運動をCLS状態へ移す損失と分離した予測枝を使い、失敗を含む遷移で世界モデルを先に適応させてから成功した実行で方策を再整合する。

**主な貢献**

世界モデルの誤較正と方策誤りを分ける二段階適応。SimplerEnv60.9→68.5%、追加rolloutによるoffline TTT後72.7%。実機の凍結方策は背景・高さ・物体変化で70〜75%；別のnoise/lighting条件のoffline TTT後は65%/70%。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿・著者・正式題名をarXiv v1で確認。選読: https://arxiv.org/html/2610.09940v1 （3.2〜3.4手法、4.1〜4.5比較・実機、Appendix C.3/D適応手順）。限界: 実機は右PiPER腕の物体をボウルへ入れる課題で各条件20試行。TTTは実行中の即時更新ではなく、追加40ロールアウト等を収集したオフラインプロトコル。 公式repoはBridge/Fractal方策学習のみ公開と明記し、JEPA訓練・RoboCasa・TTTコードとcheckpoint releaseはTODO。 https://github.com/ZhuYuChenNO1/Juno/blob/main/LICENSE はMIT標題ながらrebaseとupstream commit維持の追加文を含み、標準OSI MITと同一か未確定。具体的追補: 追加条項の位置付け・適用範囲を確認し、full-paper手法と公開実装の差を再確認。実装ライセンスunknown、open\_source=unknown。

### World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models

- ID: `HYBRID-0119`
- Published: 2026-10-01
- Authors: Jie He; Wei Li; Junwen Tong; Rui Shao; Wei-Shi Zheng; Liqiang Nie
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02323) · [Code](https://github.com/JiuTian-VL/ProAct) · [Project](https://github.com/JiuTian-VL/ProAct-page)
- Tags: ProAct, motion-proposal, prospective-latents, world-calibration, anisotropic-flow-source, pi0.5
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

直近動作をProposal Expertでscene-awareな仮説へ変換し、World Expertが所望の未来latentと仮説との適合を予測する。その適合からproposal中心の異方的生成源の大きさと低rank形状を調整し、Action Expertがflow refinementで行動chunkを生成する。

**主な貢献**

LIBERO平均98.4%でπ0.5より1.5ポイント、RoboTwin 2.0の50課題・hard条件で60.3%と31.7ポイント改善。実機6課題各25試行でも改善し、LIBEROでモデル推論latencyを121.26から89.98msへ削減した。誤proposalの反実仮想結果を直接学習しているわけではない。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.02323 のv1は2026-10-01 18:00:11 UTC、改訂なし。 https://arxiv.org/html/2610.02323v1 §2–3、App.C/Fを確認。LIBERO各suite500、RoboTwin各task100 rollout、実機GALAXEA/AgileX計6課題各25trial。World Expertはfactual expert未来で監督され、代替/誤動作の結果とdesired futureを直接比較しない。固定chunk horizonも制約。latencyはA800/RTX5090上のモデル推論で全robot周期ではない。論文project https://github.com/JiuTian-VL/ProAct-page のindexから公式実装を確認。 https://github.com/JiuTian-VL/ProAct/blob/main/src/openpi/models\_pytorch/proact\_pytorch.py と https://github.com/JiuTian-VL/ProAct/blob/main/LICENSE のApache-2.0を確認。GemmaとV-JEPA基盤は別条件、READMEのpi05初期化を調整済みProAct重みと混同しない。専用重みは未確認。Pages URLは取得失敗のため検証済みproject repoを採用。PDF未取得。

### UniWAM: Unified World-Action Model

- ID: `HYBRID-0112`
- Published: 2026-10-01
- Authors: Jiayi Chen; Wenxuan Song; Jingbo Wang; Shuai Zhou; Xicheng Gong; Zehua Fan; Ziyang Zhou; Junwu E; Haodong Yan; Fuhao Li; Qize Yu; Xu Huang; Pengwei Wang; Wen Chen; Shunbo Zhou; Haoang Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02054) · [Code](https://github.com/UniWAM/UniWAM) · [Project](https://uniwam.github.io/)
- Tags: UniWAM, physical-language-supervision, mixture-of-transformers, human-robot-co-training, history-conditioned-flow
- Model size: 8B (official README); Qwen3-VL-2B + Wan2.2-TI2V-5B + action predictor
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

VLM物理reasoner・動画世界生成器・行動予測器を共同attentionで統合する。VQA・人間動画・ロボットデータに相補的な教師信号を割り当て、未来画像noiseと行動履歴初期化で後学習を補助する。

**主な貢献**

LIBEROとRoboTwinのID/OOD評価に加え、実機の言語追従と完了成功を分けて測る。4実機課題の平均成功67.5%、指示追従82.5%を報告。長期課題の進捗5.0/6は完了成功率ではなく、学習済み課題・条件下の結果である。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.02054v1 の3–5節・Appendix Gを確認。公式repoにmodel/train/inference実装、Apache-2.0 LICENSEとMotus由来NOTICEを確認: https://github.com/UniWAM/UniWAM/blob/main/LICENSE 。READMEはBridge/DROID/Fractalと実機inferenceをrelease対象外と明記。READMEが専用base/robotwin checkpointを示す https://www.modelscope.cn/collections/Kosmos524/UniWAM は取得テキストが空でファイルと重みライセンスを独立確認できずweights=unknown。backboneの重みから推定しない。PDF未取得。

### ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection

- ID: `HYBRID-0111`
- Published: 2026-10-01
- Authors: Yijie Zhu; Rui Shao; Jie He; Wei Li; Bo Zhao; Yelin Wang; Xiaochen Yuan; Tao Tan; Miao Zhang; Xiaojiang Peng; Zitong Yu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01741) · [Project](https://jiutian-vl.github.io/ATI-VLA-page/)
- Tags: predictive-VLA, shared-codebook, actionable-alignment, adaptive-injection, bimanual
- Model size: OpenVLA-7B backbone; total parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

観測と行動を共有離散コードブックへ揃えて将来を予測し、その潜在表現をVLAの行動デコーダへ適応的に注入する二段階学習。整合モジュールを凍結後、行動目的だけで方策と軽量側路を最適化する。

**主な貢献**

予測表現のモダリティ差と共同最適化の競合を分けて扱う。LIBERO、RoboTwin 2.0と二種類の実機による五つの長期課題で評価し、予測潜在を使うVLA+WAMの例として整理する。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.01741v1 の2節・3.1–3.2節・付録A.1を確認。NeurIPS 2026採択は著者/公式projectの記載で、主催者確認はしていないためvenue=arXiv。projectのCodeリンクはproject内に戻り、研究実装・重み・実装ライセンスを確認できずunknown。hybrid/vla-wamは予測潜在と行動方策の結合による編集上の分類で、独立汎用世界モデルの公開を意味しない。PDF未取得。

### V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents

- ID: `WAM-0034`
- Published: 2026-09-29 · Updated: 2026-09-29
- Authors: Yang Zhang; Jiangyuan Zhao; Chenyou Fan; Jiayu Hu; Xiu Yuan; Chenjia Bai; Xiu Li
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2609.37250v1) · [PDF](https://arxiv.org/pdf/2609.37250v1) · [Code](https://github.com/breez3young/VJEPA-Policy)
- Tags: Language-conditioned, Latent Prediction, Flow Matching, Robot Policy, V-JEPA Policy
- Model size: 0.9B total; 0.6B trainable
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

固定V-JEPA 2.1の潜在空間で、指示に応じた未来予測とロボット行動生成を結び付ける研究。動画の生成器全体を継承せず、予測表現を方策の基盤として使う。

**主な貢献**

将来潜在を予測するネットワークの文脈キー・値をflow-matching行動expertへ渡し、両者を下流の一段階で共同学習する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/breez3young/VJEPA-Policy. Repository contains source only; no policy checkpoint distribution independently verified. Upstream encoders and assets have their own terms.

### WorldGuide: Learning Success-Failure Boundaries in Latent World Models for Vision-Language-Action Policies

- ID: `HYBRID-0121`
- Published: 2026-09-28
- Authors: Lin Liu; Lu Zhang; Ziying Song; Wu Yang; Yuzheng Zhuang; Yunzhi Zhuge; Shuai Tao; Wulong Liu; Huchuan Lu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.34206)
- Tags: WorldGuide, training-only-world-model, failure-rich-pretraining, matched-contrastive-learning, differentiable-reward, LIBERO
- Model size: 配備VLA 4B; 学習時world predictor 0.5B
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

成功・失敗の両軌跡でlatent dynamicsを事前学習し、同一課題の進捗を揃えた類似segmentをcontrastive学習で分離する。凍結した予測器を微分可能な報酬としてVLAの視覚/行動部を更新し、配備時は予測器を捨ててVLA単体を動かす。

**主な貢献**

LIBERO-100で96.8%、LIBERO全体98.4%、SimplerEnv Google Robotで72.0%を報告。ARX LIFT2の狭許容度3課題各20試行ではπ0.5の11.7%から18.3%へ改善したが、成功率は依然低く失敗後の同じ動作の反復が残る。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2609.34206 のv1は2026-09-28 03:13:43 UTC、改訂なし。 https://arxiv.org/html/2609.34206v1 §3–4、App.A/B/Cを確認。学習時のVLA/WAM結合としてhybrid/vla-wamで、推論時rollout/agentはない。table1は配備4B＋学習時predictor0.5B、225ms/chunkはWebSocket配備経路。基盤/実行周波数の異なるWAM比較の2.2–19.9倍をWM除去だけの因果効果としない。SimplerEnv72.0%はGoogle平均でWidowX64.8%。実機300demo、3課題各20trialで11/60成功、評価interleaved。失敗時刻はQwen推定に手動sample検証。2026-10-06再確認の現要旨は「Code will be publicly available.」と将来公開を明記（abs最終文／HTML abstract）。著者による公開保留の一次記述に基づきcode\_status=unavailableとした。正式題名/著者検索でも公式配布先は未確認。実装ライセンス・専用重みは公開保留から推測せずunknown。PDF未取得。

### SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models

- ID: `HYBRID-0105`
- Published: 2026-09-27
- Authors: Tianfu Li; Haoxuan Xu; Wenbo Chen; Haitian Li; Changchuan Yang; Xinhu Zheng; Jun Ma; Yuan Liu; Lujia Wang; Haoang Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.33575) · [Project](https://haoxuanxu1024.github.io/SLIP_VLA/)
- Tags: latent-imagination, single-step, future-prediction, manipulation
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

1回のノイズ除去で将来の潜在表現を生成し、幾何・意味・行動の整合性を学習してVLAの操作方策に供給する。シミュレーションと実機で将来予測の有効性を評価した。

**主な貢献**

多段の動画生成を用いず、知覚教師・順動力学・逆動力学で制御に有用な潜在未来を整形。未来想像は12msだが、公式ページの全体推論時間は181ms。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv submission history: v1 only. Official project https://haoxuanxu1024.github.io/SLIP\_VLA/ links https://github.com/HaoxuanXU1024/SLIP\_VLA; repository contains website assets and explicitly says code will be released soon, so it is not counted as a released research implementation. Implementation license and weights unverified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Towards VLA-Dreamer: Refining VLA Behavior Using World Models

- ID: `HYBRID-0107`
- Published: 2026-09-25
- Authors: Parsa Mastouri Kashani; Jan-Gerrit Habekost; Stefan Wermter
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.31313)
- Tags: concept-paper, latent-world-model, planning, sample-efficiency
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VLAの視覚埋め込み空間で行動条件付き世界モデルを学習し、データ効率改善や短期計画に利用する構想論文。視覚埋め込みが未来予測と制御に十分かを検証する研究計画を述べる。

**主な貢献**

画素再構成ではなくVLAの視覚埋め込みを予測対象にするVLA-Dreamer構想。提案・仮説であり、実証済み性能改善として扱わない。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.31313v1 explicitly describes a concept/proposed architecture, not a completed empirical system. No official project, implementation/license, or weights verified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution

- ID: `HYBRID-0109`
- Published: 2026-09-23
- Authors: Shuai Zeng; Yuxuan Liang; Hangmiao Hu; Fobao Zhou; Zixiang Wang; Wenxi Hong; Hang Zhao
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.27468)
- Tags: residual-control, consequence-model, governor, frozen-vla
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結VLAの行動チャンクを軽量な残差で補正し、予測される結果が不利な補正を抑制するCereVLA。再帰状態空間モデルと履歴分類器で短期・区間単位の結果を評価する。

**主な貢献**

残差生成を参照行動との一致だけで評価せず、予測結果に基づく実行ガバナーを導入。SO-101で成功率57.5%から90%への改善を報告。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.27468v1 checked for project/code/release evidence; no author-owned release verified. Hybrid vla-wam classification reflects predictive consequence modeling coupled to VLA control, not a separately released general world model. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies

- ID: `HYBRID-0103`
- Published: 2026-09-21 · Updated: 2026-09-22
- Authors: Trung Dao; Sankalp Yamsani; Jaden Park; Joohyung Kim; Yong Jae Lee
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.24682) · [Code](https://github.com/trungdt880/THAW-VLA) · [Project](https://thaw-vla.trung-dt.com/)
- Tags: THAW-VLA, representation-distillation, compact-policy, world-model-teacher, flow-matching
- Model size: 0.8B student; 4B variants
- Open-source: unknown
- Code / weights / license: available / available / unknown

**概要（日本語）**

凍結世界モデルの内部特徴を事前計算し、小型VLAの画像特徴へ蒸留する。推論時には教師と投影器を使わず、行動方策の構造を維持したまま表現学習を補助する。

**主な貢献**

行動模倣損失に特徴整合損失を加え、教師の行動表現への依存を避ける。LIBERO・RoboCasaと実機で同一学生の非蒸留対照を検証する。

**確認記録**

- Checked: 2026-10-04 · Review: needs-review
- 初稿2026-09-21、v2改訂2026-09-22をarXivで確認。HTML本文III節と評価条件を確認。公式projectがリンクする実装とHF LIBERO/RoboCasa-GR1のfinal\_model.ptを再確認。両モデルカードはMITを宣言する: https://huggingface.co/termanteus/THAW-VLA-Qwen3.5-0.8B-LIBERO ; https://huggingface.co/termanteus/THAW-VLA-Qwen3.5-0.8B-Robocasa-GR1 。カード更新は2026-09-29で今回差分期間の新規releaseではない。実装 https://github.com/trungdt880/THAW-VLA/blob/main/LICENSE はMIT表記に追加のupstream commit保持条項を含むためopen\_source/license\_status=unknownを維持し、重みのMIT宣言と混同しない。次回は実装LICENSEの明確化/変更を確認する。Oct3–4 UTCの新GitHub commit/releaseなし。

### Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model

- ID: `HYBRID-0102`
- Published: 2026-09-11 · Updated: 2026-09-11
- Authors: Hoeun Lee; Jaeik Kim; Jusang Oh; Jinhyeok Kim; Geon Choi; Hyeonggeun Kim; Jaeyoung Do
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.13053) · [PDF](https://arxiv.org/pdf/2609.13053) · [Code](https://github.com/AIDASLab/Dynin-Robotics) · [Project](https://dynin.ai/robotics/)
- Tags: Dynin-Robotics, masked-diffusion, world-action-model, goal-state-prediction, candidate-reranking
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

言語・観測・目標・行動を共通の離散トークン列として学ぶomnimodal masked-diffusionモデル。条件と予測領域を変え、方策、次状態、終端目標、指示再構成を共同学習し、目標生成や未来予測を動作生成・候補選択へ使う。

**主な貢献**

共有trajectory modelの複数条件付き予測を、目標誘導・行動と次状態の共同denoising・候補再ランキングに再構成。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式repoはREADME/assetsのみ、公式model cardもCode and model will be released soon。MIT badgeはあるが実装・重み未公開なのでopen\_sourceはunknown。https://huggingface.co/snu-aidas/Dynin-Robotics

### LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

- ID: `WAM-0035`
- Published: 2026-06-14 · Updated: 2026-06-14
- Authors: Jialei Chen; Kai Wang; Kang Chen; Shuaihang Chen; Feng Gao; Wenhao Tang; Zhiyuan Li; Weilin Liu; Zhuyu Yao; Boxun Li; Yuanbo Xu; Chao Yu
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2606.15768v1) · [PDF](https://arxiv.org/pdf/2606.15768v1) · [Code](https://github.com/RLinf/LaWAM)
- Tags: Language-conditioned, Latent Subgoal, Latent Action, Robot Policy, LaWAM
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

未来の画像を生成する代わりに、潜在的な視覚サブゴールを方策へ渡すLaWAMを提案。世界モデルによる先読みを、低遅延の言語条件付きロボット操作へ取り込む。

**主な貢献**

視覚基盤の潜在空間で行動表現を学び、その順方向デコーダを未来特徴の予測器へ転用して行動生成に条件付ける。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Implementation license checked: MIT implementation; DINOv3 component has separate terms; source: https://github.com/RLinf/LaWAM.
