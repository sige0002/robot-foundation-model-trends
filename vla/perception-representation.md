<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / perception-representation

[← vla](README.md) · [CSV master](../papers.csv)

26 records · Published date 降順（同日 ID 降順）

### What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning

- ID: `VLA-0223`
- Published: 2026-10-15
- Authors: Haitao Shen; Hanyu Liu; Yihan Lin; Huiping Liu; Junbo Cui; Daoheng Li; Yang Li; Jing Zhang; Wenxin Li; Yuan Yao
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.21915) · [PDF](https://arxiv.org/pdf/2610.21915)
- Tags: supervision-allocation, latent-action, future-vision, sample-level-routing, MMDiT
- Model size: 約2B（本文Table 1の実験モデル）
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

二流MMDiTとサンプル単位routerを用い、固定した学習サンプル予算を行動予測・潜在行動予測・未来視覚表現予測へ配分して比較する。LIBERO・CALVIN・実機4課題で、適切な補助予測は直接行動予測への配分が半分以下でも行動のみの学習を上回ったと報告する。

**主な貢献**

VLAの予測対象と教師信号の配分を明示的な設計変数として比較する。予算一致は学習サンプルの延べ利用回数であり、FLOPsや実時間の一致ではない。

**確認記録**

- Checked: 2026-10-18 · Review: verified
- 2026-10-05〜2026-10-18の選択増分調査。本文前にcanonical arXiv・正規化/近似題名を既存351件と照合し一致なし。arXiv DOI/version aliasも別論文として扱わない。arXiv一次資料で書誌・初稿日2026-10-15・v1のみの履歴・PDFリンクを確認。本文 https://arxiv.org/html/2610.21915v1 で予算定義とTable 1の約2B表記を選択確認。公式実装・重み・project・実装ライセンスは未確認のためunknown。未来表現は学習用教師信号で、推論時は行動出力を実行するためvlaに分類。実行再現なし。

### VLA-Δ: Learning Physical State Transition for Vision-Language-Action Models

- ID: `VLA-0221`
- Published: 2026-10-15
- Authors: Qi Lu; Jiarun Li; Ce Zhang; Miao Pan; Yi Pan; Xu Wang; Wenqi Zhang; Xuhong Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.21306) · [PDF](https://arxiv.org/pdf/2610.21306) · [Code](https://github.com/ZJU-OmniAI/VLA-Delta) · [Project](https://zju-omniai.github.io/VLA-Delta/)
- Tags: VLA-Delta, physical-state-transition, structured-slots, optical-flow, difference-text, flow-matching, LIBERO, RoboTwin, GR00T, Qwen3-VL
- Model size: Qwen3-VL-2B-Instruct backbone + 9-layer action DiT (total not reported)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

現在・未来間の物理状態変化を、構造化slot、dense optical flow、差分textの三種の教師信号で学習するVLA。Physical State Difference Queriesで得た遷移表現をflow-matching行動expertへ渡す。補助教師信号は事前学習で使い、下流fine-tuningは行動損失のみ、推論は補助出力を復号しない。

**主な貢献**

物体位置・接触・タスク進行の意味情報と画像内運動をquery表現に統合する事前学習、および約484時間・2,400万frameの遷移annotation pipeline。LIBERO平均98.4%、RoboTwin Clean/Random 90.06/89.74%は原著比較条件での結果。

**確認記録**

- Checked: 2026-10-17 · Review: verified
- arXiv v1 2026-10-15 05:54:21 UTC、改訂なし。本文前にcanonical arXiv・DOI alias・正規化/近似題名を既存347件と照合し一致なし。一次HTML https://arxiv.org/html/2610.21306v1 Sec.2–3とTable 1–2を選読。主貢献が学習時の遷移表現supervisionであるためvla/perception-representation。公式GitHubにmodel/policies/train\_vla.pyと3-stage pretraining・benchmark評価手順を確認。GitHub APIでLICENSE本文11,357 bytesを取得しApache-2.0を確認: https://github.com/ZJU-OmniAI/VLA-Delta/blob/main/LICENSE 。READMEからリンクされたbase重み https://huggingface.co/t0rn0d0/VLA-Delta-base のimmutable commit c9821c22a2e83f3578732da45a5289a5925dece8でaction\_expert.safetensors・difference\_query.safetensors・3 model shards等の実file名、size、LFS hashをtree APIで確認。model cardはapache-2.0。重みのdownload・実行・数値再現は未実施。上流componentの条件は別、2Bはbackboneの表示で総規模ではない。

### FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs

- ID: `VLA-0218`
- Published: 2026-10-14
- Authors: Bingao Chen; Lihan Zha; C. Karen Liu; Guy Tevet
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.20064) · [PDF](https://arxiv.org/pdf/2610.20064) · [Code](https://github.com/Stanford-TML/FoveaVLA) · [Project](https://tml.stanford.edu/FoveaVLA/)
- Tags: foveation, active-perception, RGB-D, pi0.5, DROID, real-robot
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

FoveaVLAは手首カメラの代わりに、外部画像のどの領域を次に拡大観測するかを学習するπ0.5ベースの方策。全景と元解像度からの局所crop、整合した深度を入力し、外部ステレオカメラ1台または2台で操作する。

**主な貢献**

動作chunkと次回観測の相互作用領域を別headで予測し、動作実行中にboxを復号して次画像のcropを準備。DROIDのRoboInter注釈から将来boxを教師化し、flow-matching動作損失と共同学習する。

**確認記録**

- Checked: 2026-10-16 · Review: verified
- v1初出2026-10-14、改訂なし: https://arxiv.org/abs/2610.20064 。canonical arXiv/DOI・正規化/近似題名を本文前に照合し一致なし。HTML https://arxiv.org/html/2610.20064v1 §IV、§V-A、Appendix B/Cを選読。実機4suite計48共通試行。MolmoSpaces公開baselineとはカメラ・深度等が異なり統制比較ではない。公式projectとrepoの相互linkを確認。実装LICENSE本文とREADMEでApache-2.0: https://github.com/Stanford-TML/FoveaVLA/blob/main/LICENSE 。公式model cardはApache-2.0、root/params treeは12.4GB・OCDBT manifest/\_METADATAを表示: https://huggingface.co/bingaochen/FoveaVLA-Single/tree/main ; https://huggingface.co/bingaochen/FoveaVLA-Dual/tree/main 。ただし下位data file・immutable commitの取得はCache missとなり、checkpoint実fileの確認未完のため重みunknown。Gemma等の由来noticeはcodeの許諾と区別。PDF応答を確認、ファイル・重み・data未download、再現実験なし。

### Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision

- ID: `VLA-0220`
- Published: 2026-10-09
- Authors: Zile Zhong; Yuxin Du; Tao Lin; Haoxiao Wang; Wei Dai; Binhua Zuo; Bo Zhao
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.12936) · [PDF](https://arxiv.org/pdf/2610.12936) · [Code](https://github.com/MINT-SJTU/Evo-World)
- Tags: Evo-World, future-motion, optical-flow-supervision, latent-prediction, FiLM, flow-matching, lightweight, Meta-World, RoboTwin, bimanual
- Model size: 0.87B total (paper-reported, includes predictive branch)
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

現在画像と指示から未来の2D運動潜在表現を予測し、FiLMを通じてflow-matching行動生成を条件付ける軽量VLA。訓練時のみ実演動画のoptical flowを教師信号とし、推論時に未来画像やflow推定器は不要。Meta-World、RoboTwinとAgileX実機3課題で評価した。

**主な貢献**

静的外観を含む未来RGB再構成の代わりに運動表現を学習し、SIGRegと行動勾配の遮断で予測表現を維持する。報告値はMeta-Worldの難易度tier等重み平均91.1%、実機3課題各20試行の平均63.3%であり、全課題等重み平均や広範な汎化保証とは区別する。

**確認記録**

- Checked: 2026-10-17 · Review: verified
- arXiv v1 2026-10-09 03:38:02 UTC、改訂なし。Sec.3–5、Table 1–2を選読。予測は候補行動に条件付けず画像と指示から運動表現を生成するためvla/perception-representationに分類。公式GitHubにmodel/scripts/launch/evalの実装と訓練・評価手順を確認。READMEはMINT-SJTU/Evo-World-MetaworldとEvo-World-Robotwin重みを案内するが配布先が取得不能でweights unknown。リポジトリroot表示にLICENSEなく、コードlicenseはunspecified。論文CC BY 4.0をコードlicenseへ流用しない。再現未実施。 本文前にcanonical arXiv・DOI alias・正規化/近似題名を既存347件と照合し一致なし。一次本文: https://arxiv.org/html/2610.12936v1 。 公式code HEAD 17191f90990de9cc6d3a15fbfab2b62c31368b74、GitHub license APIは404。

### LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos

- ID: `VLA-0204`
- Published: 2026-10-09
- Authors: Zhiyuan Xiang; Peidong Liu; Mingyang Li; Jiawei Li; Wenhow Li; Wenbo Ding; Xiang Deng
- Venue: CoRL 2026 (accepted; arXiv metadata)
- Links: [Paper](https://arxiv.org/abs/2610.13732) · [PDF](https://arxiv.org/pdf/2610.13732)
- Tags: latent-action-pretraining, continuous-LAM, human-video, egocentric, embodiment-alignment, optical-flow-supervision, flow-matching, AgiBot-G1, RoboTwin
- Model size: LAM: 24 encoder + 24 decoder blocks, width 1024, 32-dimensional latent; policy parameter count unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

一人称の人間動画の隣接frame変化を説明する連続latent actionを学び、VLAの事前学習教師へ変換する。知覚・意味・optical flowを合わせてLAMを学習し、人動画のlatent-action事前学習、対象ロボットへの整列、task別post-trainingを同じaction expertで行う。

**主な貢献**

離散codeや画素再構成だけに頼らない人動画の潜在行動教師と、3段階のVLA学習recipeを提示する。ロボットdataを固定した1K→5K時間の人動画scalingで、3実機taskの平均成功63.3→85.0%を報告する。

**確認記録**

- Checked: 2026-10-13 · Review: verified
- abs履歴v1=2026-10-09 15:29:20 UTC、改訂なし。absにCoRL2026 acceptedと記載。HTML §§3–5, Appendix Bを選読: https://arxiv.org/html/2610.13732v1 。PDF24頁のfetchを確認。LAM corpus23.3K時間とpolicy用clean subset5.1K時間を区別。対象ロボット250時間のembodiment alignmentを要し、latentが独立制御可能な自由度へ一致する保証はない。実機評価はAgiBot G1一機種・7task、各条件20試行でdeployment robustnessの一般保証ではない。正式なproject/実装repository/専用重み/実装licenseを論文と題名限定検索で独立確認できずunknown。

### VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

- ID: `VLA-0188`
- Published: 2026-10-08
- Authors: Boyao Han; Chen Shi; Jingjing Qian; ZhuoTan Tian; Li Jiang
- Venue: NeurIPS 2026
- Links: [Paper](https://arxiv.org/abs/2610.12451) · [Code](https://github.com/BoyaoHan/VersaCamVLA) · [Project](https://boyaohan.github.io/VersaCamVLA.github.io/)
- Tags: camera-configurable, scene-tokens, wrist-pose-sampling, calibrated-rgb
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

較正済み複数RGB viewを固定サイズscene tokenへ写像し、カメラ数・poseの違いを行動学習から切り離すVersaCamVLA。自然な手首運動を追加pose教師として利用する。

**主な貢献**

training-only多信号view predictionでscene encoderを作り、凍結encoderと軽量spatial encoderから192追加tokenをπ0.5へ供給。RoboTwinの未知pose評価は52.63%（π0.5は32.88%）。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.12451 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.12451v1 。v1 HTMLと https://boyaohan.github.io/VersaCamVLA.github.io/ Method/Tables1–3選読。RGB viewのpose/ray較正を要し、raw未較正カメラ対応とはしない。未知pose比較はRoboTwin Clean、nominal学習条件。https://github.com/BoyaoHan/VersaCamVLA READMEはCode coming soon、rootはREADME/demosのみでcode unavailable、weights/license unknown。公開demoを実装releaseと見なさない。 PDF未取得。

### WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models

- ID: `VLA-0180`
- Published: 2026-10-08
- Authors: Junmyeong Lee; Dongmin Shin; Min-Gyu Park; Wooseok Jeon; Inho Chang; Hae-Gon Jeon
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.11508)
- Tags: wrist-camera-adaptation, mixture-of-experts, view-robustness, frozen-policy
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

手首カメラの視点差をMoE feature adapterでcanonical表現へ近づけるWARP-VLA。暗黙の視点情報でexpertを混合し、推論時のカメラ外部較正値を不要にする。

**主な貢献**

LIBEROの手首視点摂動でπ0.5の平均成功39.2%→78.3%。simulation学習adapterの実機視点差への転移を評価し、wrist-view benchmarkを提案した。

**確認記録**

- Checked: 2026-10-09 · Review: needs-review
- 初稿・著者: https://arxiv.org/abs/2610.11508 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.11508v1 。§I/III選読。canonicalデモの視覚特徴平均をanchorとして使うため、元設定の学習dataから独立した完全無準備適応ではない。absはbenchmark/実装releaseを述べるが選読本文と公式著者名検索では取得先/実装LICENSEを確定できずcode/weights/license unknown。needs-review: 次回は著者が結び付けた公式repoと実装file/LICENSEを確認しrelease主張を解消。外部較正不要は推論adapter入力についての限定。 PDF未取得。

### When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs

- ID: `VLA-0177`
- Published: 2026-10-07
- Authors: Jasper Gerigk; Kenzo Aspuru-Takata; Chin-Hsuan Wu; Mohammad Mohammadi; Shuhong Zheng; Igor Gilitschenski
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.10912)
- Tags: shortcut-learning, task-scrubbing, language-grounding, representation-diagnostics
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

視点や背景とタスクの偶然の相関にVLAが依存する仕組みを調べ、視覚タスク識別器への勾配反転で言語指示の利用を促すtask scrubbingを提案する。

**主な貢献**

action marginとattention knockoutで視覚shortcutの入り方とモデルごとの差を分析。LIBERO、RoboTwin、実機の対課題設定でOOD頑健性を改善し、視覚情報の完全除去とは区別した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.10912 (v1=2026-10-07、改訂なし)。選択精読: https://arxiv.org/html/2610.10912v1 。§III–VII選読。実験は二つの対課題に限定され、multi-task一般化は未検証。タスクlabelと学習可能な視覚経路が必要、凍結系はadapterを追加。補助損失scaleは1seedでSC/OOD性能を参照して選択し、ID-only較正の確立ではない。ID性能低下やshortcutを残すseedもある。コード/重み/実装ライセンス未確認。 PDF未取得。

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

### VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models

- ID: `VLA-0198`
- Published: 2026-10-06 · Updated: 2026-10-08
- Authors: Owen Du; Yang Yue; Jie Zhang; Jiaqi Pi; Chi Bene Chen; Gao Huang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08133) · [Code](https://github.com/du-owen/VLA-ACL)
- Tags: VLA-ACL, action-consistency, visual-token-pruning, frozen-VLA, soft-top-k, OpenVLA-OFT
- Model size: unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

VLAを凍結したまま、全視覚contextのteacher動作とdemonstration動作への整合性で軽量patch scorerだけを学ぶ。訓練時はsoft Top-K gateを使い、推論時はcameraごとに上位K tokenをlanguage backboneへ渡す。

**主な貢献**

視覚tokenの選択を間接的attention指標から動作出力への影響へ結び付ける。LIBEROでK32は平均成功96.8%→95.4%、LLM遅延63.49→42.30ms、FLOPs4.013→0.991TFLOPs。K64は97.0%で、速度と性能のtrade-offを示す。

**確認記録**

- Checked: 2026-10-12 · Review: verified
- abs履歴v1=2026-10-06、v2=2026-10-08。同じ正規ID。https://arxiv.org/html/2610.08133v2 の§III、IV-A–Cを選択確認。速度はA100上のLLM部分、全robot loopの1.5倍とは扱わない。比較baseline成功は各論文から引用、実機4taskは各methodに40/20/20/40試行の計120試行で、73.75%→72.5%はtaskを等重みとした平均でありpooled成功率ではない。公式train\_scorer.pyをGitHub connectorで取得、root LICENSEのApache2.0を確認: https://github.com/du-owen/VLA-ACL/blob/main/LICENSE 。公式https://huggingface.co/owendudu/VLA-ACL のcardは8 scorer checkpointを記載。2026-10-12に固定revision e8d30096b49184d2d4bb259240319a4f1c55919bの公式HF tree APIで8つのscorer .pt（各130,452,786 bytes、LFS metadata）を確認したためweights\_status=available。公開重みはscorerのみでbase VLA全体の重みではない。https://huggingface.co/owendudu/VLA-ACL/tree/e8d30096b49184d2d4bb259240319a4f1c55919b 。weight license未確認。PDF未取得。

### MIM-VLA: Learning Physical Interaction Representations from Gripper Motor Feedback

- ID: `VLA-0196`
- Published: 2026-10-06
- Authors: Jaeyoung Lee; Jiyeon Koo; Taehwa Kim; Yerin Cha; Andrew Jaeyong Choi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08425)
- Tags: MIM-VLA, motor-telemetry, contact-phase-pretraining, gripper-conditioning, interaction-memory, SmolVLA
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

gripperの電流・位置・速度・信号有効性の因果履歴を、接触とinteraction phaseの教師で128次元tokenへ符号化する。tokenはSmolVLAのgripper経路へ接続し、物体ごとの記憶をMEM selector VLMの比較・説明にも使う。出力は位置commandを維持する。

**主な貢献**

追加触覚sensorなしで既存motor feedbackを時間的interaction表現へ変換し、制御と物体比較で再利用する。実機13物体pair×各20試行の抵抗が大きい物体の選択は195/260=75.0%、SmolVLAは127/260=48.8%。校正済みの材質硬度測定とは区別する。

**確認記録**

- Checked: 2026-10-11 · Review: verified
- abs履歴v1=2026-10-06、改訂なし。https://arxiv.org/html/2610.08425v1 の§III、IV-A/B/C、Vを選択確認。VLM backboneは凍結するが両action expertは後学習するためarm方策全体の凍結とは記さない。優しい把持はarm固定・cameraなしのgripper-only評価。単一gripper、未校正force、mask誤差、未知breakable物体の低成功が制約。論文と題名限定検索で公式code/weights/実装licenseは確認できずunknown。PDF未取得。

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

### NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- ID: `VLA-0200`
- Published: 2026-10-01
- Authors: Shota Kobayashi; Koki Seno; Daichi Yashima; Komei Sugiura
- Venue: ACCV 2026 (accepted; arXiv)
- Links: [Paper](https://arxiv.org/abs/2610.00981) · [PDF](https://arxiv.org/pdf/2610.00981) · [Project](https://shota0520.github.io/NarrativeFlow-project-page/)
- Tags: NarrativeFlow, robot-flow, velocity-field, flow-matching, Narrative-Delta, cross-embodiment-data, HSR, motion-interface
- Model size: 487M trainable parameters (paper Sec.4.1)
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

言語と初期画像から連続速度場を積分して2D robot flowを生成する。Fractal・Bridge V2でflow予測を評価し、生成flowを別のflow-conditioned policyへ渡してHSRの移動操作3 taskを検証した。画像平面の運動を言語と制御の中間表現に用いる。

**主な貢献**

初期・goal画像間のtask-relevant変化を複数の文章埋め込みへ変換するNarrative Delta lossで視覚言語表現を補助学習する。flow生成と補助lossに別々のsubtask tokenを設け、goal画像不要の言語条件付きvelocity-field生成へ拡張する。

**確認記録**

- Checked: 2026-10-11 · Review: verified
- arXiv v1 2026-10-01書誌・ACCV 2026 accepted表記、Sec.3–5とsupplement implementationを選読。Fractal/Bridge V2 ADE 21.68/30.59はend-effector領域のpoint-tracking errorで全sceneの物理整合性評価ではない。CoTracker3由来targetと一部生成instructionを用いる。HSRは3 task各20 trial、平均成功率55%（Im2Flow2Act 42%）、各task平均30 demonstrationでfine-tuneし一つのhardwareに限定。固定camera・初期end-effector可視を仮定し、2D flowではdepth方向運動を捉えにくい。独立した世界の未来状態予測モデルとは分類しない。公式project pageの全linkとauthor-name限定code検索に公式実装・weights提供先を確認できずunknown、unavailable/closedとは判断しない。website-template CC-BY-SAを実装licenseと混同しない。モデル規模はtrainableのみ、total size未確認。

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

### CLIPort: What and Where Pathways for Robotic Manipulation

- ID: `VLA-0189`
- Published: 2021-09-24
- Authors: Mohit Shridhar; Lucas Manuelli; Dieter Fox
- Venue: CoRL 2021
- Links: [Paper](https://arxiv.org/abs/2109.12098) · [PDF](https://arxiv.org/pdf/2109.12098) · [Code](https://github.com/cliport/cliport) · [Project](https://cliport.github.io/)
- Tags: CLIPort, supporting-foundation, VLA-predecessor, CLIP, TransporterNets, language-conditioned-policy, pick-and-place, SE2
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

CLIPの視覚言語的な意味表現とTransporterの空間的な操作表現を二つのstreamで結ぶ、言語条件付き模倣学習方策。物体認識を明示的に挟まずpick/place affordanceを予測し、10シミュレーション課題と9実機課題の多タスク学習を検証した。

**主な貢献**

Web事前学習の意味的priorを精密な空間行動予測に結合する、後のVLA研究につながる基礎的な知覚・行動接続。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv v1 2021-09-24、PMLR書誌 https://proceedings.mlr.press/v164/shridhar22a.html を確認（会議2021、proceedings公開2022を初稿日へ代用しない）。HTML §§3–4/AppendixIを選読: https://arxiv.org/html/2109.12098v1 。広範なロボット基盤モデル事前学習ではなくVLA前史の言語条件付き方策。SE(2) pick/placeのprimitive実行はopen-loop、主に準静的課題で、実機終了は利用者が指示。CLIPのzero-shot物体認識とzero-shot操作を混同しない。公式repo実装/Apache-2.0全文、v1.0.0 releaseのuploaded cliport\_quickstart.zip checkpoint assetを別々に確認: https://github.com/cliport/cliport/blob/master/LICENSE ; https://github.com/cliport/cliport/releases/tag/v1.0.0 。重み未ダウンロード、重みの独立ライセンスは未確認。

### BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

- ID: `VLA-0195`
- Published: unknown / 未確認
- Authors: Eric Jang; Alex Irpan; Mohi Khansari; Daniel Kappler; Frederik Ebert; Corey Lynch; Sergey Levine; Chelsea Finn
- Venue: CoRL 2021 / PMLR 2022
- Links: [Paper](https://arxiv.org/abs/2202.02005) · [Code](https://github.com/google-research/tensor2robot/tree/master/research/bcz) · [Project](https://sites.google.com/view/bc-z/home)
- Tags: BC-Z, supporting-foundation, language-video-task-embedding, FiLM, HG-DAgger, zero-shot-task-generalization
- Model size: ResNet18 policy; 512-dimensional task embedding
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

自然言語や人間task動画をtask埋め込みへ写し、FiLMで画像ベース方策を条件付ける模倣学習。デモと人の途中介入を集約し、未学習の動詞・物体の組合せに対するロボット操作の一般化を調べる。

**主な貢献**

言語・動画task表現と閉ループ行動学習を接続したVLAの基礎。ResNet18方策、HG-DAggerの反復データ収集、適応的状態差分actionを組み合わせ、課題デモなしでの新しい指示への転移を検査する。

**確認記録**

- Checked: 2026-10-11 · Review: needs-review
- arXiv v1は2022-02-04だがCoRL2021/OpenReview版が先行し、最初の公開preprint日を確定できずpublished空欄。OpenReviewの公開日取得はbrowser verification/API取得失敗で未解決。https://arxiv.org/html/2202.02005v1 §3–5を選読。公式projectは未学習21task、arXiv要旨は24taskを示すため44%を統一denominatorの成果として採用しない。公式projectから参照されたTensor2Robot bcz/model.py/config/READMEとroot LICENSEのApache2.0全文、model.pyの同license headerを別確認。READMEの公開TFRecordsはdatasetであり方策重みの証拠ではなくweights unknown。追補は初公開日と評価task数の版差。PDF未取得。
