<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / planning

[← agent](README.md) · [CSV master](../papers.csv)

15 records · Published date 降順（同日 ID 降順）

### AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- ID: `AGENT-0167`
- Published: 2026-10-20
- Authors: Xinxin Liu; Bingxin Xu; Wenrui Bao; Ming Li; Wentao Bao; Chen Chen; Yuzhang Shang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.28589) · [PDF](https://arxiv.org/pdf/2610.28589) · [Code](https://github.com/xinxinliu-ai/AgenticRoboRL)
- Tags: AgenticRoboRL, planner-post-training, SFT, multi-turn-RL, harness-adapter, frozen-VLA, control-code, LIBERO-PRO, LIBERO-Plus
- Model size: Qwen3.5-9B planner; total system unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

ロボットの実行基盤や低レベル方策を固定し、高レベルplannerだけを成功軌跡のSFTと複数turnの強化学習で改善する。VLAスキル呼出し型と制御コード生成型を、モデル呼出し記録と最終成否を結ぶadapterで扱う。

**主な貢献**

異なる実行方式を共通のplanner学習単位へ接続し、同じ実行器のまま判断能力を学習する。RPent上の9B plannerはLIBERO-PROで18.1%からSFT後65.1%、RL後71.0%へ改善し、LIBERO-Plusでも追加学習なしで72.2%を報告した。

**確認記録**

- Checked: 2026-10-21 · Review: verified
- arXiv absで全著者・初稿2026-10-20・改訂なしを確認。手法・評価は一次HTML v1 §§3–4.5を読んで確認し、PDF URLの取得も確認（https://arxiv.org/html/2610.28589v1 ）。評価はLIBERO系simulation。CaP-X側はprivileged stateを使う別学習で、RPentの学習済みplannerを直接転用した実験ではない。記憶付き大規模plannerとの値はsystem比較であり、SFT寄与の分離ではない。論文の公開予定表記とは別に、公式リンク先repoの実ファイルrl/train\_rl.py、LICENSE（Apache-2.0）、NOTICEを確認。旧L-CodingSpaceからxinxinliu-aiへの移動をGitHub repo ID 1422461340で確認。確認commit a4b4115dcc4890561a2f5b10d44a3c0264cb47ba（2026-10-21 22:30:25 UTC）。実装ライセンス: https://github.com/xinxinliu-ai/AgenticRoboRL/blob/a4b4115dcc4890561a2f5b10d44a3c0264cb47ba/LICENSE 。公式READMEが案内する重み https://huggingface.co/ciciciciliu/AgenticRoboRL-Qwen3.5-9B のsft/とrl-v006/に各18.8GBのmodel.safetensorsとXet/SHA256情報を確認（revision 996f98f32483277099e5448bbccc9fdc13677c0f、model card表示Apache-2.0）。重みの取得・実行は未実施。READMEはteacher軌跡未公開と明記。公式projectページは新旧URLともweb取得失敗のためproject\_urlは空欄。 2026-10-08〜21の分野別選択増分調査、本文前にcanonical IDと正規化/近似題名を照合。独立した実行・数値再現なし。

### Towards Agentic Robots: Model, Data, Environment, and Harness

- ID: `AGENT-0160`
- Published: 2026-10-14
- Authors: Chonghan Qin; Dongming Wu; Kaituo Feng; Jiaxu Wang; Xinlei Yu; Peiwen Sun; Yijia Fan; Xilin He; Bingao Chen; Weitong Lian; Ryan Ji; Wenqi Ren; Xiaobin Hu; Dahua Lin; Yu-Gang Jiang; Xiangyu Yue
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.20442) · [PDF](https://arxiv.org/pdf/2610.20442) · [Project](https://github.com/chonghanqin/Awesome-Agentic-Robots)
- Tags: survey, agentic-robotics, taxonomy, harness, data-lifecycle, environment-generation, VLA, world-model
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

目標達成に向けた計画・能力選択・実行監視・失敗回復を備えるagentic robotを整理するサーベイ。Model・Data・Environment・Harnessの4領域17分類で、方策学習からデータ収集、環境構築、実行基盤までを関連付ける。

**主な貢献**

エージェントが何を判断し、どの観測・実行器・フィードバックに依存するかを軸に研究を整理。公平な比較、実機展開、実行コスト、異なるロボットへの汎化を研究課題として提示する。

**確認記録**

- Checked: 2026-10-16 · Review: verified
- arXiv absの書誌・履歴を確認（v1: 2026-10-14、改訂なし）。HTML §§3,7,8で定義・分類・展望を確認: https://arxiv.org/html/2610.20442v1 。新規制御モデルや実験結果の提案ではなくsurveyとして収録。公式文献集リポジトリをproject\_urlに記録。GitHub上にMIT表示があるが文献集のライセンスであり、ロボット実装の公開・ライセンスや重みを意味しないため各状態はunknown。確認範囲は初稿2026-10-02〜10-15の選定候補、確認日はJST。

### Rendering-Free Lookahead for Question-Guided Active Vision

- ID: `AGENT-0150`
- Published: 2026-10-08
- Authors: Koya Sakamoto; Daichi Azuma; Shuhei Kurita; Naoya Chiba; Yusuke Iwasawa; Yutaka Matsuo; Taiki Miyanishi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.11039) · [Project](https://k0uya.github.io/rfl-proj/)
- Tags: RFL, active-vision, camera-control, answerability, privileged-value-distillation, E3VS-Bench
- Model size: Qwen3.6-27B teacher/student; 117M trainable LoRA parameters
- Open-source: unknown
- Code / weights / license: unavailable / unavailable / unknown

**概要（日本語）**

質問へ回答できる視点を探すため、候補camera motionの将来answerabilityをVLMで採点する。訓練時だけ3DGSで候補の1・2段先を描画し、その価値をLoRA学生へ蒸留することで、展開時は質問・最近の画像・候補動作だけで視点を選ぶ。

**主な貢献**

未実行の候補も含む価値supervisionを、描画不要のcamera制御へ移す。未知21scene・377episodeの平均judge scoreは同じVLMの直接制御2.14から3.05へ改善。これは1–5の回答品質指標で、操作成功率ではない。

**確認記録**

- Checked: 2026-10-11 · Review: verified
- abs履歴v1=2026-10-08、改訂なし。検索結果の7日表記より履歴を採用。https://arxiv.org/html/2610.11039v1 の§IV、V-A/B/F/Gを選択確認。実機は3質問×3method×各10試行、計90試行。stopはbase VLMへ委ね、実機では不可能動作を候補から除く。細部知覚・停止・可動範囲が制約。公式projectはCode/Weight Coming soonと明記、実装licenseはunknown。描画teacherを学習WAMとは扱わずagent/planningを提案。PDF未取得。

### SafeInferCom: Safe Inference-Time Compute via Verifier-Guided Mid-Generation Intervention for Robotic Task Planning

- ID: `AGENT-0147`
- Published: 2026-10-08
- Authors: Weizhe Xu; Jialiang Fan; Mengyu Liu; Fanxin Kong
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.11223)
- Tags: SafeInferCom, formal-verification, inference-time-compute, PDDL, mid-generation-intervention, robot-task-planning
- Model size: 7B\|14B\|32B（主評価のDeepSeek-R1-Distill-Qwen）
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

推論言語モデルの生成途中から行動計画を取り出し、外部形式検証器で検査するロボットタスク計画framework。元の復号状態を保存する監視器を使い、有効な途中計画の保持、違反への診断feedback、早期終了、持続する違反への再計画を生成中に制御する。

**主な貢献**

完了後の計画検証を生成途中へ移し、計画の上書きと訂正の遅れを抑える。5PDDL domain・各100問題の14B評価ではone-shot54.8%から78.2%へ改善。単独使用でtokenが常に減るわけではなく、形式的有効性は与えた仕様と検証器に相対的。VirtualHomeと実機armの定性的demoも扱う。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- absのsubmission historyでv1 2026-10-08確認、改訂なし。https://arxiv.org/html/2610.11223v1 の§III-A、§IV–V、§VI-A/F、§VIIを選択確認。500PDDL問題での数値、VirtualHomeの追加評価、実機Blocksworldは定性的demoを区別。安全保証はgrounding・知覚・物理実行の誤りを含まない。確認した一次資料に公式code/weights/実装licenseなし、unknown。公式videoはhttps://youtu.be/dbU7WskCNgY。PDF未取得。

### RoboQuest: Generalist Physical Agents that Search, Inspect and Test

- ID: `AGENT-0138`
- Published: 2026-10-07
- Authors: Liu Renhang; Navonil Majumder; Tej Deep Pala; Soujanya Poria
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.10388) · [Code](https://github.com/declare-lab/RoboQuest) · [Project](https://declare-lab.github.io/RoboQuest/)
- Tags: RoboQuest, goal-directed-exploration, active-perception, hidden-information, mobile-manipulation, benchmark, simulation-only
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

探索、操作を伴う観察、道具や機構の試験を必要とする10種類の移動操作タスクを設計する。開始時には必要情報を隠し、ロボットが物理的なSUBMITボタンを押す時点で採点することで、証拠収集と行動選択、いつ確信して終了するかをまとめて評価する。

**主な貢献**

物理動作による情報獲得を不可欠にしたbenchmarkと5,000探索demoを提供し、情報を与えた単独skill試験と失敗帰属を併用して、運動実行以外の探索・判断・状態回復の障害を分離。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-07、v1のみ。本文§3–5、結論を選択読解: https://arxiv.org/html/2610.10388v1 。RoboCasa365/MuJoCoでFranka mobile base、10タスク×50共通instance、5 frontier agents、最大200decision。最良23.2%; 情報を与えた8skillの単独成功72–81%。fine-tuned π0.5はPuzzle Box 2%、他9タスク0%; backboneや訓練条件の一般的優劣は示さない。失敗帰属の「観測済み」はcamera画像への可視性で注意/理解の証明ではなく、各失敗episodeの未達条件に決定的規則を適用する分析。実機評価なし。実装MIT: https://github.com/declare-lab/RoboQuest/blob/main/LICENSE 。公式README/projectにはdatasetとpolicy-server手順があるが、この論文のfine-tuned重みURLは確認できずunknown。PDF・dataset未取得。

### HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots

- ID: `AGENT-0135`
- Published: 2026-10-06
- Authors: Yurun Chen; Josh Qixuan Sun; Jason Qin; Chengtai Li; Tianyi Wang; Mark Crowley; Wentao Zhu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.08642) · [Project](https://euron-zc.github.io/HygieneRoboBench/)
- Tags: HygieneRoboBench, Hygiene-NSP, contact-history, neuro-symbolic-planning, CP-SAT, user-priorities, symbolic-evaluation
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

両gripperや共有物を介した汚染と処置の履歴を持つ624の家事planning instanceを構築する。Hygiene-NSPはLLMで依頼をgroundingし、接触履歴から衛生状態を再構成して、CP-SATで処置・作業・時間・資源を利用者の優先順に共同最適化する。

**主な貢献**

現在の配置だけでは分からない汚染履歴、接触event、資源優先順を制御した比較と独立plan replayで、安全な完了と安全かつcost最適な解決を分けて評価。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-06、v1。本文§III–V、§VIを選択読解: https://arxiv.org/html/2610.08642v1 。134task families/624instance、5LLM＋Rule-SAT＋Hygiene-NSP; NSPのgrounderはGPT-5.6 Sol。safe resolution94.4%/optimal safe resolution90.4%は実行不能の正しい拒否も含む。明示された接触/処置ruleと抽象time-unitに基づくsymbolic plan評価で実機衛生効果の実証ではない; OmniGibson図はstaged illustration。公式repository READMEはcode/dataを準備中と明記しrootは紹介資料のみ: https://github.com/Euron-ZC/HygieneRoboBench\#release-plan 。公開実装は現時点unavailable、実装licenseと重みはunknown。PDF・dataset未取得。

### OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning

- ID: `AGENT-0134`
- Published: 2026-10-06
- Authors: Hyeongwoo Nam; Woongje Cho; Juwon Kim; Jongeun Choi
- Venue: NeurIPS 2026
- Links: [Paper](https://arxiv.org/abs/2610.07649) · [Code](https://github.com/namhyeongwoo/OntoPlan) · [Project](https://namhyeongwoo.github.io/OntoPlan/)
- Tags: OntoPlan, ontology-PDDL-alignment, symbolic-scene-graph, selective-retrieval, tool-use, long-horizon-planning, fully-observable
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

物・空間・関係・状態を同じontologyとPDDL語彙へ揃え、四つのLLM役割が共有記憶上で依頼解釈・scene検索・目標形式化・計画修正を分担する。scene-query toolで必要な情報だけを取り出し、symbolic plannerが前提・状態遷移・達成済み目標の保持を扱う。

**主な貢献**

構造化sceneへの選択的アクセスと実行可能plan生成を同じ語彙で接続し、LLMへ全sceneのtext化やprimitive動作列の直接生成を課さないAgent planning pipeline。

**確認記録**

- Checked: 2026-10-08 · Review: verified
- 初稿2026-10-06、v1、arXiv commentsがNeurIPS 2026採択と明記。本文§3–6を選択読解: https://arxiv.org/html/2610.07649v1 。5室内環境×3scale/150general task、平均success0.89、18.1k tokens/task。scene-queryなしでtoken scalability悪化、integrated PDDL pathなしでsuccess0.31; 一個の部品だけの因果効果とはしない。world modelは完全観測されたRDF/OWL symbolic factsで学習WAMではなくAgent/planning。raw sensor/partial observability/実機自律性は未評価、新semanticsにはontologyとPDDL双方の改訂が必要。公式実装MIT: https://github.com/namhyeongwoo/OntoPlan/blob/main/LICENSE 。READMEはFast Downward GPLv3、3D Scene Graph由来dataは非商用研究限定と明記し、code licenseと区別。新規モデル重み配布未確認。PDF・data未取得。

### Mind the Refinement Gap: When Safe High-Level Robot Plans Produce Unsafe Executions

- ID: `AGENT-0129`
- Published: 2026-10-02
- Authors: Stabak Das; Priyesh Ranjan; Xiangfang Li; Lijun Qian
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.02662)
- Tags: refinement-gap, semantic-graph, LTL, trace-contract, RoboGuard, SPINE, safety-audit
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高水準計画が省く中間航行や暗黙的動作効果を、semantic graphと実行意味から展開したtraceで安全monitorへ渡す。RoboGuardで同じLTL仕様のsurface/refined判定を比較し、計画・接地・検証・interfaceの失敗を分離して抽象化境界を監査する。

**主な貢献**

制御監査28例のうち標的12例すべてでsurfaceは安全、refinedは危険となり、対照16例は期待どおりだった。SPINEとの14例ではfalse-safe 2件、明示的阻止2件、control pass 5件、interface error 5件。trace展開で監視の見落としを露出する軽量診断を示した。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.02662 のv1は2026-10-02 01:31:57 UTC、改訂なし。 https://arxiv.org/html/2610.02662v1 §1、§3–4を確認。RoboGuard e487f83／SPINE e776a8a、静的graph上のoffline auditで、各E2E例1trial。連続dynamics・知覚誤り・衝突・物理実行は扱わない。平均checker時間0.54→0.69msはplanning/grounding/graph構築を除く。inspect引数の5構文失敗は安全判定分母に混ぜない。正式題名/著者検索で本監査の公式コード・重み・実装ライセンス未確認、既存基盤のライセンスを継承して推定しない。PDF未取得。

### CORNAV: Construction-Aware Reasoning for Robot Navigation on Active Worksites

- ID: `AGENT-0125`
- Published: 2026-10-02
- Authors: Parastoo Ali Pour; Deepak Prakash Kumar; Tommy Zhou; Pramod Khargonekar; Mohammad Abdullah Al Faruque
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.03622)
- Tags: CORNAV, CAD, scene-graph, schedule-aware-navigation, LLM-safety-validation, classical-planner
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

2D CADの部屋配置と開放語彙3D scene graphを位置合わせし、施工予定を時間依存の航行制約へ変換する。GPT-4oが安全規則と危険記述を照合して注意領域を必要に応じて通行禁止に格上げし、A\*が制約下の経路を生成する。

**主な貢献**

事務所と施工現場の記録データを用いたオフライン評価で、図面groundingを含む計画のtask success rateは13.0%から72.2%へ改善。89の予定時刻条件のうち実行可能な74経路でhard-zone違反は0件。実機のlive動作は定性的デモであり、数値は現場での継続的な無事故運用を示さない。

**確認記録**

- Checked: 2026-10-05 · Review: verified
- 本文取得前にrevisionなしarXiv ID/DOIと正規化/類似タイトルをローカル比較し一致なし。https://arxiv.org/abs/2610.03622 で正式著者、v1 2026-10-02 17:19:05 UTC、改訂なしを確認。HTML https://arxiv.org/html/2610.03622v1 の§IIIと§IV-A/C/D/Eおよび結論を選択読解。量的評価はGo2で収集したRGB/depth/pose記録上のオフラインplanning。Go2/G1でのfull pipeline live deploymentは定性的実演のみ。89trial中15はstart/goalがhard-zone内のためinfeasible、違反0は74のfeasible経路に限定。hard-zoneの排除はA\* occupancy制約による。LLMはsoft-zoneを0.7閾値で格上げし、学習VLA/WAMではないのでagent/planningとした。soft-zoneには回避不能なら通過を許す。§IV-Eのmislabel safety評価と公開検索を確認、公式実装/project・専用重み・実装ライセンスは未確認のためunknown。PDF未取得。 App/Table VのTSRは対象grounding段階に依存し、schedule/safetyの有無で同値となる設計で、54requestに対するHOV-SG baselineは7.4%。13.0%はw/o Blueprint ablationであり、72.2%をend-to-end live-navigation成功率とは扱わない。LLM安全テストは8case各8callの限られた条件。

### Foundation-Model-Guided Topology-Aware Semantic Risk Fields for Manipulation

- ID: `AGENT-0127`
- Published: 2026-09-29
- Authors: Giung Lee; Weihang Guo; Lydia E. Kavraki
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.36640)
- Tags: semantic-risk, geodesic-field, topology-aware-shielding, LLM-prior, CHOMP, supporting-agent-planning
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

基盤モデルが物体対ごとの6方向risk重みと減衰距離を与え、3D占有形状の障害物を避けるgeodesic距離と遮蔽でrisk場を構成する。衝突制約を維持した従来plannerへ、意味的な曝露を抑える追加costとして組み込む。

**主な貢献**

静的な家庭simulation3場面で、人が定義した参照risk場に対する軌跡曝露を衝突回避のみより減らした。RTX4090の2cm解像度で20物体risk場56.9msを報告。曝露costと実際の損害・事故確率は別で、動的環境/実機安全性は未検証。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。本文前のcanonical arXiv/DOI・正規化/類似タイトル照合一致なし。https://arxiv.org/abs/2609.36640 : v1 2026-09-29 03:46:07 UTC、改訂なし。HTML https://arxiv.org/html/2609.36640v1 のIII/IV/V/VI節を選読。WAM/VLA方策ではなく基盤モデルpriorを従来CHOMP型plannerへgroundingする支援研究。表現とplanning比較はsimulator姿勢・手動ラベル・共有oracle risk重みを用いて知覚とprior生成を分離。別のprior比較は135物体対を各モデル1回生成、30対/180方向の人評価参照で検証。risk重みは確率ではなく、near-no-goも有限soft costで数学的禁止領域ではない。56.9msは知覚後のfield構成で知覚・表示・保存を除き、初回LLMfallback中央値2.11秒。静的近接場面・較正・固定frame方向への依存。一次論文/著者題名検索で公式実装・重み・project・実装license未確認unknown。PDF未取得。

### Risk-Aware Semantic Grounding for Trustworthy LLM-Based Robot Planning

- ID: `AGENT-0115`
- Published: 2026-09-29
- Authors: Łukasz Sobczak; Nur Keleşoğlu; Sławomir Piotr Nowak
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.37554) · [Code](https://github.com/iitis/Risk-Aware-Semantic-Grounding)
- Tags: RA-SGF, TRUST-NAV, semantic-grounding, clarification, risk-gating, navigation
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

指示の曖昧さ、存在しない対象、意味的矛盾を計画前に評価し、実行・確認質問・拒否を選ぶ。高レベルの屋内ナビゲーション計画とそのgroundingを対象にする。

**主な貢献**

リスク評価agentと規則ベースのdecision gateをplannerから分離し、TRUST-NAVで計画正解率とは別に判断の信頼性を評価する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿・著者とHTML本文3節・4–5節を確認。評価は単一の静的な意味環境で、知覚誤差や動的実機安全性の保証ではない。本文がリンクする公式repoのplanner/decision layer実装を確認。root MITを確認: https://github.com/iitis/Risk-Aware-Semantic-Grounding/blob/master/LICENSE 。学習済み重み提供は未確認。

### Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots

- ID: `AGENT-0117`
- Published: 2026-09-24
- Authors: Lucas Da Mota Bruno; Jiahao Sim; Yoshinobu Hagiwara
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.29043)
- Tags: LLM-chaining, GPSR, instruction-classification, task-schema, HSR, planning-execution-gap
- Model size: Qwen2.5-14B; Cogito-14B; hosted model size unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

生活支援ロボットの自然言語命令を28種類へ分類し、選ばれた課題のスキーマだけを使って行動関数列を生成する二段階LLM計画。巨大な単一promptを分け、観測・一手生成・実行・フィードバックを繰り返す。

**主な貢献**

100 GPSR命令で計画出力の整合性を比較し、HSR実機10試行では6課題が完了。分類の正解ラベルを与えた計画評価であり、上流分類込みの成功率や全課題の総token削減を実証したものではない。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.29043v1 のIII節、IV-A/B/C節とV節を確認。約45%削減はStage2の一回あたりprompt長で、分類callと総task tokenは別。三モデルと一命令分布、実機一施設10試行に限定。IEEE GCCE 2026採択はarXivコメントのみなのでvenue=arXiv。専用code・weight・実装licenseは本文リンク/題名検索で未確認。本論文は先行15課題研究の拡張と明記。既存DBとの正規ID・正規化題名照合に一致なし。PDF未取得。

### Text2Motion: From Natural Language Instructions to Feasible Plans

- ID: `AGENT-0110`
- Published: 2023-03-21 · Updated: 2023-11-26
- Authors: Kevin Lin; Christopher Agia; Toki Migimatsu; Marco Pavone; Jeannette Bohg
- Venue: Autonomous Robots 2023
- Links: [Paper](https://arxiv.org/abs/2303.12153) · [PDF](https://arxiv.org/pdf/2303.12153) · [Project](https://sites.google.com/stanford.edu/text2motion)
- Tags: Text2Motion, task-motion-planning, geometric-feasibility, skill-Q-functions, long-horizon
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

自然言語指示から象徴的な目標を推定し、到達可能なタスク・動作計画を検索する。スキルのQ関数で候補を導き、個々のスキルだけでなく動作列全体の幾何依存を検査して長期操作の実行可能性を高める。

**主な貢献**

LLMのタスク計画と、スキル列にまたがる幾何的実行可能性の探索を結合。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。最終arXiv版コメントが出版先を明記。公式projectで公開実装リンクを確認できず、code/licenseはunknown。

### PaLM-E: An Embodied Multimodal Language Model

- ID: `AGENT-0104`
- Published: 2023-03-06 · Updated: 2023-03-06
- Authors: Danny Driess; Fei Xia; Mehdi S. M. Sajjadi; Corey Lynch; Aakanksha Chowdhery; Brian Ichter; Ayzaan Wahid; Jonathan Tompson; Quan Vuong; Tianhe Yu; Wenlong Huang; Yevgen Chebotar; Pierre Sermanet; Daniel Duckworth; Sergey Levine; Vincent Vanhoucke; Karol Hausman; Marc Toussaint; Klaus Greff; Andy Zeng; Igor Mordatch; Pete Florence
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2303.03378) · [PDF](https://arxiv.org/pdf/2303.03378) · [Project](https://palm-e.github.io/)
- Tags: PaLM-E, embodied-multimodal-LM, sensor-grounding, task-planning, positive-transfer
- Model size: 562B (largest model)
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

画像、連続的な状態推定、テキストを交互に並べた入力で、身体性のある言語モデルを学習する。ロボットの逐次操作計画、VQA、captioningを共同学習し、異なるタスク・観測・身体間の正の転移を検証した。

**主な貢献**

連続センサーを言語トークン列へ直接組み込み、知覚と高レベル計画をマルチモーダルLMとして共同学習。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。要旨が最大モデル562Bと明記。Agent分類は高レベル操作計画を担うため。公開実装・重み・ライセンスはunknown。

### Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

- ID: `AGENT-0101`
- Published: 2022-04-04 · Updated: 2022-08-16
- Authors: Michael Ahn; Anthony Brohan; Noah Brown; Yevgen Chebotar; Omar Cortes; Byron David; Chelsea Finn; Chuyuan Fu; Keerthana Gopalakrishnan; Karol Hausman; Alex Herzog; Daniel Ho; Jasmine Hsu; Julian Ibarz; Brian Ichter; Alex Irpan; Eric Jang; Rosario Jauregui Ruano; Kyle Jeffrey; Sally Jesmonth; Nikhil J Joshi; Ryan Julian; Dmitry Kalashnikov; Yuheng Kuang; Kuang-Huei Lee; Sergey Levine; Yao Lu; Linda Luu; Carolina Parada; Peter Pastor; Jornell Quiambao; Kanishka Rao; Jarek Rettinghouse; Diego Reyes; Pierre Sermanet; Nicolas Sievers; Clayton Tan; Alexander Toshev; Vincent Vanhoucke; Fei Xia; Ted Xiao; Peng Xu; Sichun Xu; Mengyuan Yan; Andy Zeng
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2204.01691) · [PDF](https://arxiv.org/pdf/2204.01691) · [Code](https://github.com/google-research/google-research/tree/master/saycan) · [Project](https://say-can.github.io/)
- Tags: SayCan, affordance-grounding, skill-composition, language-planning, mobile-manipulation
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

LLMが持つタスク知識を、ロボットの学習済みスキルの実行可能性でgroundingする。言語モデルの有用性スコアとスキルのvalue/affordanceを組み合わせ、長期自然言語指示を実行可能なスキル列へ分解する。

**主な貢献**

「指示に役立つか」と「今の状態でできるか」の確率を掛け合わせる、言語計画とスキル価値の接続。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式projectがリンクするtabletop版コード。Apache-2.0: https://github.com/google-research/google-research/blob/master/LICENSE 。実機の全システム公開とは区別。
