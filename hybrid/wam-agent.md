<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Hybrid / wam-agent

[← hybrid](README.md) · [CSV master](../papers.csv)

5 records · Published date 降順（同日 ID 降順）

### Atomic-WAM: Execution-Grounded Atomic-Motion Reasoning for World Action Models

- ID: `WAM-0123`
- Published: 2026-10-14
- Authors: Shijun Shi; Zhe Liu; Zhi Hou; Yinan Chen; Tao Zhang; Kai Hu; Yong Liu; Jiangning Zhang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.20157) · [PDF](https://arxiv.org/pdf/2610.20157) · [Code](https://github.com/ssj9596/Atomic-WAM) · [Project](https://ssj9596.github.io/Atomic-WAM-project/)
- Tags: Atomic-WAM, atomic-motion-reasoning, execution-grounded-GRPO, joint-video-action, DROID, RoboLab, hierarchical-control
- Model size: unknown
- Open-source: unknown
- Code / weights / license: available / unknown / unknown

**概要（日本語）**

視覚言語reasonerが観測履歴と課題指示から次の局所動作を言語化し、WAMが未来動画と行動chunkを生成する。実行後の観測で動作記述を更新し、曖昧な指示の接地を助ける。

**主な貢献**

接触情報を含むDROIDの原子動作教師を作成し、凍結WAMで候補動作を実行した結果をEG-GRPOの報酬へ使ってreasonerだけを適応させる。

**確認記録**

- Checked: 2026-10-16 · Review: verified
- arXiv absの履歴でv1初稿2026-10-14（後続改訂なし）、全著者、PDFリンクを確認。HTML v1のIII–IV節で手法と限界を確認: https://arxiv.org/html/2610.20157v1 。EG-GRPOの実行成功報酬は現状で人手判定を使用。高levelの動作選択とWAM実行の閉loopに基づきhybrid/wam-agentに分類、安定IDを維持。公式projectがリンクするrepoで推論・RoboLab評価コードを確認（training/data公開とは区別）。repoはWAM/Reasoner LoRA公開を表明するが、各checkpointの実ファイルとimmutable tree/blob metadataを未確認のためweights\_statusはunknown。公式に案内された重み配布先: https://huggingface.co/datasets/MochunniaN1/Atomic-WAM\_Robolab （metadataはApache-2.0、README空、全重みへの適用範囲未確認）。実装はファイル別でCosmos由来OpenMDW-1.1とRoboLab由来Apache-2.0を保持: https://github.com/ssj9596/Atomic-WAM/blob/main/licenses/OpenMDW-1.1.txt 。新規scriptsを含む実装全体の明確なlicense適用を確定できずopen\_source/license\_statusはunknown。

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

### AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation

- ID: `HYBRID-0142`
- Published: 2026-09-20 · Updated: 2026-10-02
- Authors: Yicheng Jiang; Zesen Gan; Xiaobo Wang; Tianlun He; Chenxu Zhao; Minghui Wu; Xinyue Wang; Jiaxu Wang; Junhao He; Jianan Wang; Qiming Shao
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.23578) · [PDF](https://arxiv.org/pdf/2609.23578) · [Code](https://github.com/AR-WAM/AR-WAM) · [Project](https://ar-wam.github.io/)
- Tags: AR-WAM, visual-prompt, agent-policy-interface, latent-foresight
- Model size: 0.5B
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

上位エージェントが対象bounding boxと原子的操作tokenを指定する視覚条件付きWAM。言語encoderを使わず、教師ありの意図出力と視覚・意味の将来潜在表現を行動生成と共同学習する。detect・execute・query interfaceで外部VLM/LLMと接続し、長期記憶と失敗復旧を上位側に担当させる。

**主な貢献**

空間groundingと操作選択を明示的なagent-policy interfaceにし、共有transformer上で意図推論と二段の未来整合を学習する。方策を小型に保ちながら、上位エージェントによる記憶・再試行と接続する。

**確認記録**

- Checked: 2026-10-17 · Review: needs-review
- 直近窓より前の欠落補充。arXiv v2の書誌・履歴、本文III-A～III-EとIVの選択確認。初稿2026-09-20、改訂2026-10-02。公式repoのmodels・dataloader・configs・train.py・train\_rla.pyを確認。GitHub APIのLICENSE全文（1076 bytes、標準MIT、copyright AR-WAM contributors、blob f68537c3d3d8606adea65fa388e12232fa62188f）を確認。継承部分と事前学習assetはupstream条件。AR-WAM方策重みの公開file tree未確認（DINOv3の重みと区別）。公式code HEAD:085d435b366755512ea078ea500a97da8ed2e9ed（GitHub API確認）。限定的選択確認で実行再現なし。 本文: https://arxiv.org/html/2609.23578v2 。本文前にcanonical arXivと正規化/近似題名を既存347件と照合し一致なし、version/DOI aliasも同一性なしを再確認。needs-review: 公式方策checkpointの公開fileと適用licenseを個別再確認。

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
