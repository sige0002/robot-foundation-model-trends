<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / memory

[← agent](README.md) · [CSV master](../papers.csv)

3 records · Published date 降順（同日 ID 降順）

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
