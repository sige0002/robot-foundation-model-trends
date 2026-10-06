<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Agent / memory

[← agent](README.md) · [CSV master](../papers.csv)

2 records · Published date 降順（同日 ID 降順）

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
