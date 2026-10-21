<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / memory

[← agent](README.md) · [CSV master](../papers.csv)

8 records · Published date 降順（同日 ID 降順）

### Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets

- ID: `AGENT-0166`
- Published: 2026-10-20
- Authors: Jad Yammine; Malek Wahidi; Abrar Anwar; Yan Chang; Mihir Acharya; Anthony Rizk
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.28624)
- Tags: Industrial-ReMEmbR, fleet-memory, spatiotemporal-retrieval, edge-server-split, cached-vision-tokens, on-demand-captioning, semantic-traffic-map
- Model size: Nemotron-3-Nano-4B agent; total system unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

倉庫ロボット群の観測を、位置・時刻付きの共有記憶へ蓄積する。各機体で検索用埋め込み、説明用の視覚token、再構成用latentを一度作り、質問された場面だけサーバーで言語化する。

**主な貢献**

観測時の一律caption生成を省き、同じ表現を検索・通路状況分類・後日の説明へ再利用する構成。模擬倉庫914フレームの通路分類はbalanced accuracy 71.3%で、比較したcaption方式の最高値を6.0ポイント上回った。

**確認記録**

- Checked: 2026-10-21 · Review: verified
- arXiv absで全著者・初稿2026-10-20・改訂なしを確認。読了範囲は一次HTML v1 §§3–7（https://arxiv.org/html/2610.28624v1 ）で、手法・評価・運用上の範囲を確認。PDFリンクはabs/HTML双方から取得を試したがwebで失敗したためpdf\_urlは空欄。4Bはagent単体で総規模ではない。450回のcached-token一致は150フレーム×3質問のgreedy decodingでの結果。100台の計算量・通信量は測定値からの外挿で、100台実運用の実証とは区別。新規の制御方策ではなく共有記憶基盤としてagent/memory。一次論文と題名による限定検索で本研究固有の公式実装・重み・実装ライセンスを確認できずunknown。基盤モデルや原版ReMEmbRの公開状況を継承しない。 2026-10-08〜21の分野別選択増分調査、本文前にcanonical IDと正規化/近似題名を照合。独立した実行・数値再現なし。

### SEAR: Self-Evolving Agentic Robotics

- ID: `AGENT-0158`
- Published: 2026-10-13
- Authors: Xinyi Wang; Bangzheng Li; Hanyu Wang; Lin Zhang; Andrea Yaoyun Cui; Zhenggang Tang; Shyamal Buch; Dejia Xu
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.18792) · [PDF](https://arxiv.org/pdf/2610.18792) · [Project](https://sear.bot/)
- Tags: self-improvement, benchmark, code-as-policy, agent-as-policy, auto-research, skill-memory
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

ロボットエージェントの経験からの改善を調べる枠組み・ベンチマーク。コード方策、実行時エージェント、VLAを微調整する自動研究の三形態を比較し、反復試行、計算時間、記憶継承などを分離する対照評価を設ける。

**主な貢献**

単なる再試行と持続的なスキル・記憶の効果を切り分けるマッチした対照群と、タスク・シミュレータ・実機をまたぐ一般化段階を提示。330シミュレーション課題と5実機課題で、転移は共有手順に限定され、個別解や誤った記憶は一般化しにくいと報告。

**確認記録**

- Checked: 2026-10-15 · Review: needs-review
- arXiv v1・方法/結果: https://arxiv.org/abs/2610.18792 ; https://arxiv.org/html/2610.18792v1 。公式project: https://sear.bot/ 。論文はコード公開を記すが公式repo https://github.com/Self-Evolving-Agentic-Robotics/SEAR はREADME・assets・MIT LICENSEのみで「code is on its way」と明記。実装未公開なのでcode\_url空欄、MIT表示を未公開実装のライセンス証拠にしない。後日repoに実装/重みが入ったかと適用ライセンスを再確認。

### Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?

- ID: `AGENT-0163`
- Published: 2026-10-12 · Updated: 2026-10-16
- Authors: Jack B. Jedlicki; Amish Sethi; Heng Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.17350) · [PDF](https://arxiv.org/pdf/2610.17350) · [Code](https://github.com/jackbjed/embodied-astra-robomme) · [Project](https://embodied-astra.github.io/)
- Tags: frozen-VLM, full-context, waypoint-control, RoboMME, memory-evaluation
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

凍結したGPT-6-Astraに観測画像と過去の応答をエピソード全体で保持させ、手先ウェイポイントとグリッパ指令を直接生成する。RoboMMEの時間・空間・物体・手続き記憶を要する16課題で、専用学習なしの制御能力を検証する。

**主な貢献**

全800試行の単一実行で737成功（92.1%）という能力ベースラインと、全63失敗の監査を提示。人間参照値や既存方策とは実行インターフェースが異なり、記憶チャネルの寄与を分離していない。テスト分割を用いた設定調整があり、実機・実時間制御への一般化は未検証。

**確認記録**

- Checked: 2026-10-19 · Review: verified
- 2026-10-06〜19の選択増分調査。本文前にcanonical arXiv/version/DOI alias・正規化/近似題名を既存355件と照合し一致なし。arXiv履歴でv1=2026-10-12、v2=2026-10-16を確認。本文Setup・Protocol・Limitationsを確認: https://arxiv.org/html/2610.17350v2 。公式実装のharness/astra\_waypoint\_eval\_v3.pyと結果ログを確認。実装LICENSEはMIT: https://raw.githubusercontent.com/jackbjed/embodied-astra-robomme/main/LICENSE 。GPT-6-AstraはAPI利用で新規学習なし、公開チェックポイントは確認できず重みはunknown。APIの固定日付スナップショットはなく、シミュレータは推論中に停止する。 実行・数値再現なし。 確認時code commit 79dcc7f73f536948cb039103d3fc5e722d689207。

### What Should Embodied Agents Remember? Benchmarking and Evaluating Memory Modality for Embodied Agents

- ID: `AGENT-0154`
- Published: 2026-10-08
- Authors: Junxiang Wang; Yuchen Liu; Yi Wu; Guofei Chen; Nir Pechuk; Tao Chen; Zackory Erickson; Yuzhe Qin; Tianyu Li
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.12561) · [Code](https://github.com/jimwang418/MeMoREval)
- Tags: MeMoREval, memory-modality, embodied-benchmark, scene-graph, visual-memory, inference-cost, open-loop-plan
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

ロボットAgentが過去の経験を何の形式で保持すべきかを、観察段階と後続要求段階を分離したMeMoREvalで比較する。4室内環境・53課題で文章、画像説明、カメラframe、scene graphとその組合せの記憶を検査し、成功と書込・読出時の推論費用を別々に測る。要求時には新たな観察を許さず、動作要求は一括planのopen-loop実行として記憶欠落の探索による補償を防ぐ。

**主な貢献**

同一の観察・Agent条件で保持modalityを変える評価protocolと、履歴蓄積・frame選別・writer視覚入力の拡張を提示。frame＋scene graphは試した3モデルすべてで最良の集約成績だが、frame単独の説明文に対する優位はモデル依存。実機は手作業で注釈したmapを用いる2つの実演であり、広範な実機benchmark結果ではない。

**確認記録**

- Checked: 2026-10-13 · Review: verified
- 書誌/v1 2026-10-08: https://arxiv.org/abs/2610.12561 。HTML§3–5.3とAppendix Aの一部を選読: https://arxiv.org/html/2610.12561v1 。主要モデルは5backend×3seed、補助2モデルは3backend×1seed。費用はモデル内の価格重み付token比較で保存容量や全system費用を含めない。simulationの空間情報は観察物体に制限したsimulator stateから生成。公式repo READMEはsimulation/skills/memory/Agent/grading実装をpeer review後に公開予定と明記、現在はtask JSONとrobot assets等のみ: https://github.com/jimwang418/MeMoREval/blob/main/README.md 。root Apache-2.0全文とNOTICEは確認したが、未公開benchmark実装のlicenseを確認した意味ではなくimplementation license/open\_sourceはunknown。専用weight配布未確認、scene datasetリンクをweight公開と扱わない。本文の公式projectは2回取得失敗のためURL欄を空欄にした。PDF未取得、数値再現なし。

### COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance

- ID: `AGENT-0137`
- Published: 2026-10-07
- Authors: Samira Huber; Ruben Hammele; Sören Pirk
- Venue: CoRL 2026
- Links: [Paper](https://arxiv.org/abs/2610.09358) · [Project](https://samirahuber.github.io/cool)
- Tags: COOL, ownership-inference, persistent-spatial-memory, curiosity-driven-exploration, personalization, real-robot
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

人・物・場所・時刻と接触履歴を長期記憶へ結び、日常の観測から物の所有関係を推論する。利用者の依頼を解くlanguage agentと、古い観測を更新するため移動先を選ぶcuriosity agentを組み合わせ、所有者を条件にした物探しと移動を行う。

**主な貢献**

明示的な所有ラベルに依存せず、persistent identityと人–物相互作用の証拠を蓄積・検索し、能動的な記憶更新から個人化されたナビゲーションへ接続。

**確認記録**

- Checked: 2026-10-08 · Review: needs-review
- 初稿2026-10-07、v1; arXiv commentsがCoRL 2026採択と明記。本文§3、§4.3–4.4、§5を選択読解: https://arxiv.org/html/2610.09358v1 。単一officeで5navigationタスク各10run、成功条件は目標1m以内で停止し各90–100%。curiosityを15synthetic office logsと4.5時間実機runで評価。曖昧/借用/短い接触で所有推定は不確実; 長期人物観測の同意・最小化・保持期間が課題。本文はcode/prompts/data提供を公式projectへ案内するがweb取得に失敗し、実装URL・実装license・重みを独立確認できずunknown。Follow-up: 公式projectの公開repositoryへのリンクを確認し、実装とLICENSE、fine-tuned re-ID重みの配布を別々に調査する。PDF未取得。

### MarvisNav: Making Memory Visible on Route Choices for Zero-Shot Object Navigation

- ID: `AGENT-0128`
- Published: 2026-10-05
- Authors: Jincheng Wang; Chi Pui Chan; Wei Zeng; Shuyang Zhang; Jianhao Jiao; Dimitrios Kanoulas
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06510) · [Project](https://wangjincheng1998.github.io/MarvisNav/)
- Tags: MarvisNav, topological-memory, visual-route-choices, zero-shot-object-navigation, VLM, Go2
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

探索中のトポロジーグラフに端点・分岐の探索状態を保持し、候補経路とその状態を自我視点画像へ直接描画する。VLMが物体との関連性と探索進捗を同じ視覚候補上で判断し、低レベル航行へ渡すため、別段の履歴融合やrerankingを要しない。

**主な貢献**

HM3D v0.2の1,000 episodeで成功率81.2%、SPL 42.5%を報告。共有Gemini-2.5-Flash比較でもWMNav/OpenFrontierを上回り、VLM呼出数を削減した。MP3Dでは一律に首位ではなく、失敗の多数は標的誤検出である。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.06510 のv1は2026-10-05 15:28:25 UTC、改訂なし。 https://arxiv.org/html/2610.06510v1 §4–5、App.A/B/Fを確認。全3benchmarkは5,195 episode、主比較は既報値も含む。効率はruntimeではなく共有backboneで1,000 episodeのquery数。実機Go2は定性的な屋内外runで集計成功率なし。表現付きグラフとVLM route selectionをagent/memoryと分類し、グラフを学習WAMとは扱わない。公式 https://wangjincheng1998.github.io/MarvisNav/ を確認、現在Code Soon／公開予定の表示のみなのでcode\_status=unavailable、実装ライセンス・専用重みはunknown。PDF未取得。

### ReMEmbR: Building and Reasoning Over Long-Horizon Spatio-Temporal Memory for Robot Navigation

- ID: `AGENT-0168`
- Published: 2024-09-20
- Authors: Abrar Anwar; John Welsh; Joydeep Biswas; Soha Pouya; Yan Chang
- Venue: ICRA 2025
- Links: [Paper](https://arxiv.org/abs/2409.13682) · [PDF](https://arxiv.org/pdf/2409.13682) · [Code](https://github.com/NVIDIA-AI-IOT/remembr) · [Project](https://nvidia-ai-iot.github.io/remembr/)
- Tags: ReMEmbR, supporting-foundation, spatio-temporal-memory, retrieval-augmented, navigation, NaVQA
- Model size: VILA1.5-13B captioner; multiple LLM backends; deployment uses quantized VILA-3B
- Open-source: false
- Code / weights / license: available / unknown / non-open-source

**概要（日本語）**

移動ロボットの動画説明・位置・時刻を蓄積し、過去の出来事への質問や移動目標の生成に使う記憶システム。LLMが関連する経験を反復検索する構成で、長時間のロボット記憶を扱う基礎文献として補完する。

**主な貢献**

テキスト・空間・時間の検索をLLMの関数呼出しで組み合わせ、構造化された回答と目標座標を生成する。NaVQAの210問とNova Carterの定性的実演を示すが、caption誤認や反復情報の蓄積が限界。

**確認記録**

- Checked: 2026-10-21 · Review: verified
- agent/memoryの未収録基礎を選択追加。本文前にarXiv ID・正規化/近似題名を既存369件と照合し一致なし。初稿v1=2024-09-20、後続版なしをarXiv履歴で確認。https://arxiv.org/html/2409.13682v1 §IV–IXを選読。NaVQAは7動画由来、成功判定は空間15m/時間2分の閾値を含み、手法3seed対baseline1seed、テキスト回答はLLM判定。一般的な実機成功率や均等計算量比較とは扱わない。公式repoの実装を確認。https://github.com/NVIDIA-AI-IOT/remembr/blob/main/LICENSE.md §3.3は研究・評価の非商用限定（NVIDIA等の例外あり）のため、公開コードだがopen\_source=false。独自重みの配布未確認でunknown、外部VILA/LLMの提供条件を転用しない。実行・数値再現なし。 2026-10-08〜21の選択増分調査（基礎文献は分類補完の例外）。独立した実行・数値再現なし。 公式projectのICRA2025表記をvenueへ採用。

### TidyBot: Personalized Robot Assistance with Large Language Models

- ID: `AGENT-0111`
- Published: 2023-05-09 · Updated: 2023-10-11
- Authors: Jimmy Wu; Rika Antonova; Adam Kan; Marion Lepert; Andy Zeng; Shuran Song; Jeannette Bohg; Szymon Rusinkiewicz; Thomas Funkhouser
- Venue: Autonomous Robots 2023; IROS 2023
- Links: [Paper](https://arxiv.org/abs/2305.05658) · [PDF](https://arxiv.org/pdf/2305.05658) · [Code](https://github.com/jimmyyhwu/tidybot) · [Project](https://tidybot.cs.princeton.edu/)
- Tags: TidyBot, personalization, preference-summarization, household-cleanup, few-shot
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

少数の片付け例からLLMが利用者の一般的な収納好みを要約し、未経験物体にも適用する。言語計画と知覚を組み合わせた移動マニピュレータで、個人ごとに異なる片付け先への適応を検証した。

**主な貢献**

個別の例を再利用可能な言語的好みへまとめ、以降の家庭内物体配置判断へ反映する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式コードMIT。Memory分類は利用者の好みの要約・再利用に対するもの。 Code license: MIT; https://github.com/jimmyyhwu/tidybot/blob/main/LICENSE.
