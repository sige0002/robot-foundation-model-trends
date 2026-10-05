<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / planning

[← agent](README.md) · [CSV master](../papers.csv)

6 records · Published date 降順（同日 ID 降順）

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
