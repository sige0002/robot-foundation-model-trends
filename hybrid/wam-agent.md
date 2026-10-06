<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / wam-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

3 records · Published date 降順（同日 ID 降順）

### Future Anchored Verification and Online Recovery for World Action Models

- ID: `HYBRID-0117`
- Published: 2026-10-05
- Authors: Zhibin Qin; Zhenxiong Tan; Xinchao Wang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.06280) · [PDF](https://arxiv.org/pdf/2610.06280)
- Tags: FAVOR, world-action-model, VLM-recovery, execution-verification, anchor-guided-recovery, closed-loop, simulation
- Model size: unknown (Qwen3-VL-2B-Instruct recovery VLM; total system size unverified)
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

WAMが実行前に予測した未来フレームを保持し、実観測とのずれを学習済み検証器で検出するFAVOR。逸脱時はVLMが未来アンカーから短い修正指示を作り、強めた言語CFGでWAMを復帰へ導いた後、元のタスクを再開する。世界モデルの予測と高レベル言語による復旧判断が実行中に連携する。

**主な貢献**

凍結Fast-WAM-IDMの未来予測を検証と復旧の両方へ再利用。全評価エピソードでのLIBERO成功率は97.85%から98.10%へ0.25ポイント、LIBERO-Plusは72.60%から72.98%へ表示値で0.38ポイント改善。LIBERO失敗率の相対11.6%減と、成功率の小さな絶対改善を区別する。評価はシミュレーションで実機検証は報告されていない。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。arXivの書誌・v1初稿日2026-10-05を確認、後続版なし。HTML https://arxiv.org/html/2610.06280v1 の§4-6、Table 1-2、Appendix A/Bを確認。DINOv2+spatial Transformer+GRUのAnchor Verifierと、Qwen3-VL-2B-Instructによる修正指示・復帰確認がWAMへ操作的に結合するためhybrid/wam-agent。LIBEROは40タスク各100rollout、LIBERO-Plusは1698rollout。Table 1のLIBERO-Plus gain欄は0.37ppだが、丸めた72.60→72.98の差は0.38ppなので表示値の差として記録。基底方策を変更しないとは検証器の追加学習がない意味ではない。公式論文・HTMLと論文名のコード検索で、本研究固有の公式実装・重み・実装ライセンス・projectの公開先は未確認、すべてunknown。基底Fast-WAMやQwenの公開をFAVORの公開と混同しない。PDFリンクを確認、ダウンロードなし。

### PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation

- ID: `HYBRID-0120`
- Published: 2026-10-04
- Authors: Jing Xie; Shouwei Ruan; Yubin Wang; Yuxiang Zhang; Junwei Yang; Songchang Jin; Dianxi Shi
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.04916)
- Tags: PreAct-Nav, navigation-memory, action-conditioned-world-model, predictive-sandbox, action-review, frozen-policy, VLA-compatible, OmniVLA
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

中期subgoalと実行履歴をNavigation Memoryに保持し、凍結航行方策の候補動作をVLMが実行前に評価する。必要時だけCosmos3-Nanoのaction-conditioned動画予測を呼び、候補を保持または修正する。実観測で期待と結果を照合してsubgoalと記憶を更新する。

**主な貢献**

UrbanNav test-unseenの4,634 episodeでQwen reasonerの成功率は78.14%から83.38%、SPLは74.73%から77.87%へ改善。CityWalkerの154 routeでは79.22%成功を報告。生成動画の誤りと費用が残り、H200上でsandbox平均11.37秒を要するため実時間航行を保証しない。

**確認記録**

- Checked: 2026-10-06 · Review: verified
- 2026-09-23〜2026-10-06の選択増分調査。本文取得前に既存165件とのrevisionなしarXiv/DOI・正規化/類似タイトル照合で一致なし。https://arxiv.org/abs/2610.04916 のv1は2026-10-04 03:50:39 UTC、改訂なし。 https://arxiv.org/html/2610.04916v1 §3–5、App.D/F/Gを選択確認。主系はUrbanNav方策＋Qwen3.8-27B＋Cosmos3-Nano、NoMaD/OmniVLAも比較。WAM toolとVLM agentが中心でwam-agent、VLAとの転移はtagで文脈化。UrbanNav seen4,179/unseen4,634はwatermark記述除外後、成功半径3m。定量評価は記録routeベース、outdoor実機は定性例。生成60frame・1,700rolloutの11.37秒はfastest complete run、VLM操作費用は別。予測整合ラベルはQwen判断で独立ground truthではない。正式題名/著者検索で専用実装/重み/ライセンスを未確認、unknown。PDF未取得。

### Compositional Foundation Models for Hierarchical Planning

- ID: `HYBRID-0110`
- Published: 2023-09-15 · Updated: 2023-09-21
- Authors: Anurag Ajay; Seungwook Han; Yilun Du; Shuang Li; Abhi Gupta; Tommi Jaakkola; Josh Tenenbaum; Leslie Kaelbling; Akash Srivastava; Pulkit Agrawal
- Venue: NeurIPS 2023
- Links: [Paper](https://arxiv.org/abs/2309.08587) · [Code](https://github.com/anuragajay/hip) · [Project](https://hierarchical-planning-foundation-model.github.io/)
- Tags: HiP, foundational, hierarchical-planning, LLM, video-diffusion, inverse-dynamics, iterative-refinement
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unknown / unspecified

**概要（日本語）**

言語モデルのサブゴール、動画拡散モデルの視覚計画、逆動力学の行動を組み合わせるHiP。別々のデータで学習した専門モデル間を反復的な整合性評価でつなぎ、長期の操作計画を作る。

**主な貢献**

言語・映像・行動を単一モデルへ統合せず、下流の実行可能性を上流計画へ返す階層構成を示す。三つのシミュレーション操作環境で未知の物体・色・サブタスクの組合せを評価し、空だったWAM+Agent分類の基礎例を補う。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- 分類の空白hybrid/wam-agentを補うための限定的な基礎論文追加。arXiv v1/v2日付、HTML https://arxiv.org/html/2309.08587v2 の2–3節を確認。NeurIPS公式掲載で会議とDOI 10.52202/075280-0979を確認: https://proceedings.neurips.cc/paper\_files/paper/2023/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html 。公式project経由のinv\_dyn等の予備実装は存在するがroot LICENSEなし。第三者PVDMの条項を全実装へ推定せずopen\_source=unknown、専用重み未確認。PDF未取得。
