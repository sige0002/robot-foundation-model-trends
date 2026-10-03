<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# WAM · World / Action Models / temporal-modeling

[← wam](README.md) · [CSV master](../papers.csv)

4 records · Published date 降順（同日 ID 降順）

### FutureWorlds: Learning Robotic World Models from Alternative Futures

- ID: `WAM-0059`
- Published: 2026-10-01
- Authors: Hao Wu; Shengju Qian; Weiyan Wang; Fan Xu; Fan Zhang; Yuanpeng He; Qingsong Wen; Yuxuan Liang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01019) · [Code](https://github.com/Alexander-wu/FutureWorlds)
- Tags: alternative-futures, candidate-memory, MemSPO, autoregressive-video, RL-post-training
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unavailable / unspecified

**概要（日本語）**

同じ行動条件から多様な未来映像を探索し、候補ごとに初期状態と直近履歴を保持する自己回帰世界モデル。MemSPOは候補映像の相対的な品質を報酬にし、生成時と学習時の履歴を一致させて事後学習する。

**主な貢献**

三データセット各128軌跡の32フレーム予測で画質・運動・長期整合性を評価。候補履歴を有界に保つ設計と探索誘導学習を結びつけるが、実機制御や閉ループ計画での成功改善は未検証。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2610.01019v1 の3節、4.1節、5節を確認。公式repoのsrc実装とREADMEを独立確認。READMEは公開checkpoint/data配布と独自コードの最終ライセンスをpendingと明記し、weight manifestのハッシュ一覧を公開重みと扱わない。コードはavailable、重みはunavailable、実装ライセンスunspecified、open\_source=unknown。repoに示されたproject linkは今回取得できずproject\_urlは空欄。PDF未取得、正確なPDF href未抽出のためpdf\_urlは空欄。

### Round-Trip Consistency: Bidirectional Diffusion Models Can Predict Their Own Rollout Errors

- ID: `WAM-0045`
- Published: 2026-08-01 · Updated: 2026-08-13
- Authors: Alexander Scheinker
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2608.00675v2) · [PDF](https://arxiv.org/pdf/2608.00675v2) · [Code](https://github.com/alexscheinker/round-trip-consistency)
- Tags: Diffusion, Bidirectional Dynamics, Uncertainty, Error Calibration
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

正解の未来を観測できない推論時に、生成的な動力学モデルの長期予測誤差を推定する研究。物理シミュレーションと顔動画で評価し、ロボット制御は直接の実証対象ではない。

**主な貢献**

同じ拡散モデルを時間の順・逆両方向に学習し、往復ロールアウトで出発点に戻れない量を誤差の代理指標にする。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/alexscheinker/round-trip-consistency.

### Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning

- ID: `WAM-0014`
- Published: 2026-06-05 · Updated: 2026-06-05
- Authors: Paarth Gulati; Ilya Nemenman
- Venue: unknown / 未確認
- Links: [Paper](https://arxiv.org/abs/2606.07770v1) · [PDF](https://arxiv.org/pdf/2606.07770v1)
- Tags: Contrastive Learning, Slow Features, Distractors, Inductive Bias
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ゆっくり変化するノイズを動的状態と取り違える、対照的予測学習の弱点を調べる研究。軌跡ごとの背景差を使う近道を除くことで、物理的な動きの表現を改善する。

**主な貢献**

負例を軌跡間ではなく同じ軌跡内から選び、軌跡固有の静的ノイズがフレームを識別する手掛かりにならない目的へ変える。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation/weights release and license not independently verified.

### Joint Embedding Predictive Architectures Focus on Slow Features

- ID: `WAM-0013`
- Published: 2022-11-20 · Updated: 2022-11-20
- Authors: Vlad Sobal; Jyothir S; Siddhartha Jalagam; Nicolas Carion; Kyunghyun Cho; Yann LeCun
- Venue: NeurIPS 2022 SSL Theory and Practice Workshop
- Links: [Paper](https://arxiv.org/abs/2211.10831v1) · [PDF](https://arxiv.org/pdf/2211.10831v1) · [Code](https://github.com/vladisai/JEPA_SSL_NeurIPS_2022)
- Tags: JEPA, Slow Features, Distractors, Failure Analysis
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

潜在予測が、制御に必要な動きよりも予測しやすい背景情報を選ぶ失敗を分析。軌跡中に固定された外乱と毎時刻変わる外乱で、JEPAの表現の違いを比較する。

**主な貢献**

移動点と背景外乱を切り分けた実験および理論で、固定ノイズがVICReg・SimCLR型JEPAを支配する条件を示す。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- Primary metadata and abstract checked via arXiv Atom API; first submission and latest revision are separate. Official implementation and MIT license license checked at https://github.com/vladisai/JEPA\_SSL\_NeurIPS\_2022.
