<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / vla-wam-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

2 records · Published date 降順（同日 ID 降順）

### Agentic World Action Models

- ID: `HYBRID-0146`
- Published: 2026-10-21
- Authors: Zhuoyang Liu; Dantong Niu; Botong Zhang; Boning Shao; Jing Wang; Ruijie Zheng; Yuvan Sharma; Runyu Lu; Jiaming Liu; Renrui Zhang; Roei Herzig; Yutong Bai; Ken Goldberg; Danfei Xu; Yuke Zhu; Guanzhi Wang; Linxi "Jim" Fan; Trevor Darrell
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.30136) · [PDF](https://arxiv.org/pdf/2610.30136) · [Code](https://github.com/ZhuoyangLiu2005/agentic-wam) · [Project](https://agentic-wam.github.io/)
- Tags: AW-0, joint-code-video-action, mixture-of-transformers, skill-library, masked-code-diffusion, hybrid-execution, bimanual
- Model size: SDAR-1.7B code body + Cosmos-Predict2.5-2B video expert + action DiT; frozen Qwen3-VL-2B vision tower; total unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

視覚と言語に接地したskillコード、未来動画、低レベル行動を三専門家の共同denoisingで生成するAW-0。実演からskillライブラリと時刻整合したプログラムを自動抽出し、通常はコードを予測の文脈として使い、任意の実行モードではコード呼出しと行動chunkを切り替える。

**主な貢献**

RoboTwin 2.0の50課題でclean/random平均成功率50.7%、2機体8実機課題で平均rubric score 71.1%を報告。後者は二値成功率ではない。コードを世界予測と制御に接続する構造を示すが、視覚的分布変化への弱さとskill引数の接地誤りは残る。

**確認記録**

- Checked: 2026-10-22 · Review: verified
- 2026-10-09〜22の選択増分調査。本文前にcanonical arXiv/DOI aliasと正規化・近似題名を既存376件へ照合し一致なし。arXiv absで全著者・v1初稿10-21・改訂なしを確認。読解範囲は https://arxiv.org/html/2610.30136v1 §§2–3、Appendix A・Lの構造的選読。実機は各課題3学習seed×16試行。simulation hybridは別収集CaP実演を使い、defaultとの純粋な実行方式だけの比較ではない（clean63.1/random29.2、default80.8/20.6）。実機hybridはYAMの1課題のみ、オンライン自己学習の実証なし。公式project→repoの実モデル実装を確認、commit 7ad228bebb897bf01705cc10171e1d88cf5e9b22。実装BSD-2-Clause: https://github.com/ZhuoyangLiu2005/agentic-wam/blob/7ad228bebb897bf01705cc10171e1d88cf5e9b22/LICENSE 。公式配布 https://huggingface.co/miniFranka/agentic-wam-pretrain-yamego3k-soup-e1 のagenticwam\_pretrain.pt（9,959,836,973 bytes、revision 603c59fd434774a269978e704730ba60740b1c17）とmodel cardのBSD-2-Clauseを独立確認。外部凍結モデルは各自の条件、事前学習corpusと初期Cosmos動画checkpointはこのreleaseに含まれない。総parameter数は未確認。重み取得・実行・数値再現なし。 PDF URLはabsの実リンクをHEADでHTTP 200/application/pdf確認（本文bytes未取得）。

### RoboCoach: World Models as Active Coaches for Compositional Robot Skills

- ID: `HYBRID-0104`
- Published: 2026-09-30
- Authors: Jiajun Liu; Yifan Chen; Yichao Liu; Jiayi Zhang; Ruoqu Chen; Shaoxuan Xie; Guocai Yao; Mengdi Xu; Sen Cui; Changshui Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39685) · [Code](https://github.com/RoboCoach-AI/CoachWorld) · [Project](https://robocoach-ai.github.io/)
- Tags: RoboCoach, CoachWorld, skill-routing, progress-judge, targeted-demonstrations, LoRA
- Model size: CoachWorld backbone: Wan2.2-TI2V-5B; full system total unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

VLAスキル専門家を行動条件付き世界モデル内で実行し、進捗判定器が最初の未完了サブタスクを特定する。その失敗を集約して、追加デモと更新対象の専門家を選ぶ。

**主な貢献**

Route–Imagine–Diagnose–Improveループで、計画・世界モデルの想像・スキル別LoRA更新を接続。長期タスク全体の追加デモではなく局所的な監督に予算を配分する。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv初稿とHTML本文3.1–3.4節の共有VLA backbone、router、judge、CoachWorldを確認。公式実装公開はCoachWorld部分であり全router/進捗判定/専門家更新パイプラインの公開とは区別。実装root MITを確認: https://github.com/RoboCoach-AI/CoachWorld/blob/main/LICENSE 。Wan2.2等の第三者コードは別条項。HF dit\_model.safetensorsを確認: https://huggingface.co/JEdward/CoachWorld/tree/main 。重み利用ライセンスは未確認。
