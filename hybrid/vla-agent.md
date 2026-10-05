<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

7 records · Published date 降順（同日 ID 降順）

### Bridging Frontier Reasoning and Robot Execution: From Autonomous Demonstration Generation to Dense Language Supervision

- ID: `HYBRID-0115`
- Published: 2026-10-02
- Authors: Bosung Kim; Alexander Trevithick; Ruiyi Wang; Prithviraj Ammanabrolu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.03615)
- Tags: frontier-reasoning, autonomous-demonstrations, dense-language-supervision, hierarchical-instructions, local-VLA, latency
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高遅延のfrontier modelによる推論を高速なローカル方策へ接続する二つの方法を検討する。補正デモを参照した自律軌跡生成をVLAの学習データへ加え、primitive・atomic・compositeの三階層と多面的な言語記述で方策の指示追従を学習する。

**主な貢献**

SO-101の4課題で、人間20本と生成20本を混ぜた方策と人間40本のみの方策は各80試行中41成功。RoboCasa365とBEHAVIOR-1Kでは階層的かつ多面的な言語監督の併用が比較条件中で最良となった。生成デモだけの学習や統計的同等性、系全体の実時間性は示していない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 本文取得前にrevisionなしarXiv/DOIと正規化/類似タイトルをローカル照合し一致なし。https://arxiv.org/abs/2610.03615 で正式著者・v1 2026-10-02 17:12:29 UTC・改訂なしを確認。HTML https://arxiv.org/html/2610.03615v1 の§3、§4の方法/評価設定、App.A、App.C.4/C.6を選択読解。物理方策はOpenPI π0.5をfine-tuneし、PaliGemma gemma\_2bとgemma\_300m action expertを用いるとApp.C.4に記載、系全体のparameter数は未確認。四課題の混合デモ比較は20人間のみの対照がなく、生成デモ追加の独立効果や統計的同等性は主張しない。言語監督比較は2組のtrain/eval seedで、評価taskは学習に含まれ、物理crosswordは5ゲーム。30Hzは目標であり一律の達成値ではなく、frontier API待ちが残る。生成の時間/費用は成功episodeのみ、失敗試行や一部hardware修正時間を含めない。abs/HTMLの公開リンクと正式タイトル・著者名による検索で公式実装、専用重み、実装ライセンスは確認できず各unknown。PDF未取得。

### MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation

- ID: `HYBRID-0114`
- Published: 2026-10-02
- Authors: Chenzhi Liu; Yue Zhang; Jiehong Lin; Jianan Wang; Bo Wang; Zhongrui Wang; Xiaojuan Qi
- Venue: CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2610.03476) · [Project](https://kaiknower.github.io/mobiagent/)
- Tags: MobiAgent, mobile-manipulation, skill-experts, visual-critic, recursive-improvement, replanning
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

実行時はVLMが原子的技能を逐次計画し、π0.5由来の共有VLMと技能別flow-matching expertが動作を生成する。視覚criticが再試行と再計画を選び、別の学習ループが収集軌跡を分割・検証して技能方策を更新する。

**主な貢献**

BEHAVIOR-1Kの選択した4タスクでは平均65.0%で、タスク別π0.5-TAの42.5%を上回る。RoboCasaの16複合タスクで基礎方策7.50%から最高27.50%、Astribot S1では32.5%から57.5%へ改善。技能干渉、姿勢補正の反復、遮蔽下のcritic誤判定が残る。

**確認記録**

- Checked: 2026-10-05 · Review: needs-review
- 本文取得前にrevisionなしarXiv ID/DOIと正規化/類似タイトルをローカル照合し一致なし。https://arxiv.org/abs/2610.03476 の正式著者、CoRL 2026採択コメント、v1 2026-10-02 15:48:23 UTC、改訂なしを確認。https://arxiv.org/html/2610.03476v1 の§3.1/3.2、§4.1、§5と選択した補足設定を読解。BEHAVIOR-1K全件ではなく4タスクで各10試行、RoboCasa365 Composite-Seenは16タスクで対象scene各5試行。後半更新roundは25.00〜27.50%に飽和。π0.5 VLA executorとVLM planner/criticの統合なのでhybrid/vla-agentに分類。公式projectのCodeとCheckpointを独立確認。Codeは https://github.com/kaiknower/MobiAgent を指すがweb取得失敗、GitHub connectorも404のため公開実装とライセンスを確認できず、code\_urlは空欄、各statusはunknown。公式checkpoint https://huggingface.co/Liukaikai/MobiAgent は25,000-stepの共有backbone/6 expertsを説明するが手動審査のアクセス申請が必要。未承認でファイル内容・重みライセンス未確認なのでweights\_status=unknown。アクセス申請・ダウンロードは行わず、この配布確認の残件をneeds-reviewに記録。PDF未取得。

### Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation

- ID: `HYBRID-0113`
- Published: 2026-10-01
- Authors: Isabella Liu; An-Chieh Cheng; Johan Bjorck; Zhiding Yu; Hongxu Yin; Jan Kautz; Linxi Fan; Yuke Zhu; Sifei Liu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01178) · [Project](https://www.liuisabella.com/Recova/)
- Tags: failure-recovery, digital-twin, code-as-policy, DAgger, human-intervention, parallel-workstations
- Model size: π0.5 task/recovery policies; total parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

エージェントが再構成MuJoCo digital twinで失敗復帰コードと軌跡を開発し、課題方策と復帰方策を別々に学習する。実行時は進捗監視・復帰・場面復元確認を行い、解決できない失敗の人間デモを対応する方策へ追加する。

**主な貢献**

LIBERO-Pro六条件とMolmoSpaces四分類で平均成功78.8%・64.9%。実機四課題各20試行でDAgger後77.5%、復帰追加87.5%。人間介入0%は一課題の第四収集round七episodeの観測で、無人運用や一般安全性を保証しない。対照は既報値で同時再実験ではない。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- canonical arXiv IDと正規化/類似タイトルのローカル重複確認後に本文を確認し一致なし。arXiv v1初稿2026-10-01 06:52:05 UTC、改訂なし。HTML §3・4・App.A/C確認: https://arxiv.org/html/2610.01178v1 。twinは再構成MuJoCoシミュレータで学習型WAMとは数えずvla-agentに分類。simulationはMolmoAct2+復帰プログラム、実機はπ0.5課題/復帰方策+Gemini 3.8 Flash監視。復帰は時間上限付きで未登録/失敗時は操作者に交代。公式projectと著者/手法名検索で公開実装・重み・実装ライセンス未確認。PDF未取得。

### RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance

- ID: `HYBRID-0116`
- Published: 2026-09-30
- Authors: Jingwei Jia; Keyu Zhou; Jiewei Wang; Peisen Xu; Xingyuan Zhou; Liang Wang; Jiming Chen; Gaofeng Li; Jin Wang; Shunlei Li
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39384) · [Project](https://roboassist.github.io/)
- Tags: RoboAssist, residual-replanning, workflow-memory, human-robot-handover, runtime-safety, GR00T
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人間の作業進行と実行可能なロボット課題列を分けて保持し、要求変更時には影響を受けた未完了部分だけを再計画する。LLMの課題判断、GR00T由来の操作expert、航行・受渡し・全身runtime監視を統合し、G1の模擬手術補助環境で評価する。

**主な貢献**

要求順序変更の16試行では成功率81.25%で、全未完了課題を再計画するFullReplanの68.75%を上回る。10ログ試行の平均再計画時間は3.62秒から1.20秒、変更後の計画tokenは20.02kから11.41kへ減少。臨床での安全性や一般的な実時間保証を示す評価ではない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 本文取得前にrevisionなしarXiv ID/DOIと正規化/類似タイトルをローカル比較し一致なし。https://arxiv.org/abs/2609.39384 で正式著者、v1 2026-09-30 09:34:17 UTC、改訂なしを確認。HTML https://arxiv.org/html/2609.39384v1 の§III、§IV-A/B/C、§Vを読解。shared GR00T N1.7 backboneと物体別grasp/shared placement-handover action expertsをLLM task agentが実行するためhybrid/vla-agentとした。G1ハードウェアを使う模擬手術補助場面であり臨床試験ではない。FullReplan比較のlatency/tokenはspeech recognitionとphysical execution、初期planning/perceptionを除いた計画コスト。効率別実験は各methodで成功5runのみ。force-feedback 20.11msとVLM 4.833sは異なるhazard triggerに対する応答で厳密に揃えたend-to-end比較ではない。最終subtaskでの失敗原因はplanningかphysical executionか分離されていない。公式projectはPaper/Code/TODO表示の雛形で、公開実装・専用重み・実装ライセンスは未確認のためunknown。PDF未取得。

### Where Memory Belongs: Ledger, an Object Ledger for Memory-Augmented VLAs

- ID: `HYBRID-0101`
- Published: 2026-09-28 · Updated: 2026-09-28
- Authors: Tanguy Dieudonné; Jack B. Jedlicki; Heng Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.34554) · [PDF](https://arxiv.org/pdf/2609.34554)
- Tags: Ledger, object-memory, temporal-memory, LLM-planner, π0.5, RoboMME
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

短期の知覚記憶をVLA内部、長期の物体状態・遮蔽・履歴を外部の読み取り可能なledgerへ分ける。SAM3の追跡とVLMのデモ説明をLLM plannerが参照し、実行ステップの境界で目標を決める単一π0.5方策を評価した。

**主な貢献**

記憶の種類に応じた配置分離と、ステップ境界での外部物体履歴groundingをVLAへ接続する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。一次HTMLで外部ledger・LLM planner・π0.5の構成を確認。公開実装・重み・ライセンスのリンクは未確認。https://arxiv.org/html/2609.34554v1

### SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation

- ID: `HYBRID-0106`
- Published: 2026-09-26
- Authors: Ziwen Li; Hanlue Zhang; Zhenyang Ren; Tianyu Huang; Runqi Lin; Haoyu Wang; Zhengqing Gao; Yandong Guo; Fakhri Karray; Tongliang Liu; Chris Russell; Mingming Gong
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.32698)
- Tags: failure-guided, online-rl, long-horizon, adapter
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

長期タスクを原子スキルに分解し、実行失敗から弱いスキルを特定する。LLMでシミュレーションの成功判定を生成し、同系統スキルが共有するVLAアダプターをオンラインRLで改善する。

**主な貢献**

追加の専門家デモを集めず、失敗状態の復元・タスク生成・共有アダプター更新を反復する自己改善システム。複数VLAと未知タスクへの転移を評価。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Relevant primary HTML https://arxiv.org/html/2609.32698v1 checked for author-owned project/code links; none verified. Referenced RLinf is upstream training infrastructure, not proof that SEES implementation or weights are released. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation

- ID: `HYBRID-0108`
- Published: 2026-09-22
- Authors: Junjie Xie; Chuxuan He; Angen Ye; Yujia Song; Dapeng Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.25756)
- Tags: medical-robotics, hierarchical, function-constrained, cot
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高水準の視覚言語推論を低水準の制約付き関数実行と組み合わせ、精密医療ロボットの閉ループ操作を行うMedVLA。複数エージェントでスキル志向CoT学習データを生成する。

**主な貢献**

連続行動だけでなく非行動のシステム関数も扱える階層的実行を導入。電極挿入100試行で95%成功を報告するが、臨床的安全性の実証とは扱わない。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.25756v1 and targeted title/code search checked; no official implementation/license, project, or weights verified. Classification as hybrid vla-agent is a curator interpretation of reasoning plus function-level execution. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.
