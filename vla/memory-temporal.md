<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / memory-temporal

[← vla](README.md) · [CSV master](../papers.csv)

8 records · Published date 降順（同日 ID 降順）

### Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models

- ID: `VLA-0185`
- Published: 2026-10-08
- Authors: Hongyu Shi; Sen Zhao; Zuyu Zhang; Lifeng Shen; Ding Zou; Xinyu He; Xu Zhang; Qinghua Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.12090)
- Tags: latent-reasoning, reasoning-reuse, multi-episode-memory, zero-shot-robustness
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

成功した潜在推論の流れを保存し、現在の状況に合う断片を複数エピソードから再構成・修正して行動expertへ渡すFlowMem。観察の蓄積だけでなく、再利用可能な推論過程を記憶する。

**主な貢献**

RoboMME Full-16で48.0%（記憶なしLaST₀は46.3%）、標準LIBERO学習後のLIBERO-Plusで77.3%（73.2%）。互換性・順序・進捗に関する記憶介入も検査した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.12090 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.12090v1 。§3.3–3.6/4.1–4.3とTables1–2選読。RoboMMEは16課題各50固定episodeの課題macro平均、LIBERO-Plusは10,030 instanceのpooled平均。学習・記憶供給・評価episodeは分離。コード/重み/実装ライセンスの公式releaseは未確認でunknown。 PDF未取得。

### PMTRM: Pseudo-Memory Temporal Re-encoding Module for Embodied Policy Learning

- ID: `VLA-0178`
- Published: 2026-10-08
- Authors: Changchuan Yang; Haoxuan Xu; Wenbo Chen; Shuai Ren; Jianlong Zheng; Huarui Zhang; Tianfu Li; Guanzhong Tian
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2610.11168)
- Tags: phase-ambiguity, executed-history, supporting-method, temporal-reencoding
- Model size: 追加module: 訓練7.61M / 推論3.81M
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

実行済みstate/actionの有界履歴を再encodeし、似た観察でも異なる操作phaseを区別するPMTRM。時間的heterogeneityと再構成教師を使い、既存のACT・DP・VLAのaction headを保つ。

**主な貢献**

訓練用decoderを捨て、推論時は3.81M encoderだけを使う。T=128のACT判断でRTX4090上0.42ms追加という条件付き測定と、反復操作での履歴効果を報告した。

**確認記録**

- Checked: 2026-10-09 · Review: verified
- 初稿・著者: https://arxiv.org/abs/2610.11168 (v1=2026-10-08、改訂なし)。選択精読: https://arxiv.org/html/2610.11168v1 。§III-F–G/IV-A–BとTABLE V選読。総訓練module7.61Mと推論encoder3.81Mを区別。0.42msは6.8ms base ACTに対する6.2%増で、全VLA共通latencyではない。preceding executed actionのみqueueに入れ将来chunkは含めない。実機は各10rolloutでconfidence幅が広く、simulation multi-seedと証拠強度を分ける。MemoryVLAへの追加結果はaligned action stream不足で省略。コード/重み/実装ライセンス未確認。 PDF未取得。

### MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation

- ID: `VLA-0192`
- Published: 2026-09-30
- Authors: Egor Cherepanov; Nikita Kachaev; Aleksandr I. Panov; Alexey K. Kovalev
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.00604) · [Code](https://github.com/CognitiveAISystems/MIKASA-Robo) · [Project](https://mikasarobo.github.io/)
- Tags: MIKASA-Robo-VLA, memory-benchmark, language-conditioned, partial-observability, information-gap, ManiSkill, RLDS, LeRobot
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

行動に必要な手掛かりが消えた後の記憶を測る、90言語条件付き操作task・10memory typeのbenchmark。80taskは記憶を必要とし、10taskは手掛かりが見えるreactive control。情報が確実に見えないintervalとepisode horizonを区別し、22,500 oracle trajectoryをRLDS/LeRobot形式で提供する。

**主な貢献**

記憶内容、遅延、観測interface、seed、成功基準を明示してVLA評価を標準化。現時点のpi0.5参照baselineはhistory/明示memoryなしの14task subset・各20episodeで平均成功0.211±0.044。全90taskの代表成績とは扱わず、Long-split低下はopen-loop chunkとmemory type構成が交絡する。

**確認記録**

- Checked: 2026-10-10 · Review: verified
- arXiv IDは2610だがsubmission history v1は2026-09-30、改訂なし。https://arxiv.org/html/2610.00604v1 の§3、§5.2、Datasheet Distributionを選択確認。公式docs/repoにVLA suiteと評価code、MIT licenseはhttps://github.com/CognitiveAISystems/MIKASA-Robo/blob/main/LICENSE で確認。weightsは未確認でunknown。dataset releaseとmodel weightsを混同しない。projectのICLR2026引用は前身MIKASA-Robo論文であり、このVLA論文のvenueとは扱わない。PDF未取得。

### Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

- ID: `VLA-0141`
- Published: 2026-09-29
- Authors: Yaxin Zhao; Dianye Huang; Chenwei Wang; Chenguang Yang; Zhongliang Jiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.37307) · [PDF](https://arxiv.org/pdf/2609.37307)
- Tags: ActMem-VLA, action-history, Mamba-2, dual-expert-denoising, frozen-base-policy, LIBERO-Mem
- Model size: 追加パラメータは基盤VLAの3.45%（総パラメータ数は未確認）
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

ActMem-VLAは、実行済み行動の履歴をMamba-2で記憶し、軽量PreAction Expertが高ノイズ側の生成を担当した後、凍結した元のAction Expertへ途中状態を引き継ぐ。調整済み基盤VLAのVLMとAction Expertを固定し、記憶モジュールとPreAction Expertだけを学習して、観測が似る異なる作業段階の混同を抑える。

**主な貢献**

行動履歴による初期デノイジングと凍結方策による後段精密化を分離し、追加パラメータ3.45%で時間的適応を行う。シミュレーションではデモ長に基づくタスク別ステップ制限下のLIBERO-Mem 10タスクで80.8%（π0.5:65.2%、MemoryVLA:49.5%）。DOBOT Novaの4タスク各20試行ではπ0.5の35.0%から63.75%へ改善した。

**確認記録**

- Checked: 2026-10-04 · Review: needs-review
- 書誌と履歴: https://arxiv.org/abs/2609.37307 。v1は2026-09-29 11:43:19 UTC、改訂なし。方法・評価: https://arxiv.org/html/2609.37307v1 のIII節・IV-B・IV-C・IV-D。80.8%は標準600step制限の数値ではなく、デモ長95分位から作るタスク別期限での平均。標準条件では循環動作で成功でき、記憶利用を識別しにくい限界を本文が明記。実機の28.8%表記はIV-Dの35.0%→63.75%から28.8 percentage pointsと解釈し、相対改善率にはしない。部品除去の効果はタスク依存。abs/HTMLに公式公開先はない。検索で https://github.com/hit-my/PhaseVLA と https://huggingface.co/HITdongdong/ActMem-VLA を確認したが、論文著者による公式提供との結び付きを検証できないため正式URL/statusには採用せずneeds-review。候補repoの https://github.com/hit-my/PhaseVLA/blob/main/LICENSE はApache-2.0だが、本文との公式関係は未確認。候補の https://github.com/hit-my/PhaseVLA/blob/main/releases/2026-09-28/README.md とモデルカードは、修正前後の履歴勾配・タスク別plugin・探索的checkpoint選択を区別し、matching baseの公開downloadを示していない。論文CC BY-SA 4.0とコード・重みのライセンスは別。PDF URLはabsページのリンクのみ確認し、PDFを取得していない。

### Vision-Language-Action Autonomous Driving Agent with Language-based Memory

- ID: `VLA-0140`
- Published: 2026-09-29
- Authors: Kai Yan; Xiangyu Chen; Yulong Cao; Alex Naumann; Peter Karkus; Yan Wang; Jef Packer; Alex Schwing; Yuxiong Wang; Boris Ivanovic; Wenjie Luo; Marco Pavone
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.38641) · [Project](https://kaiyan289.github.io/projects/ad-memo/)
- Tags: AD-Memo, driving, language-memory, Da-Capo, semi-closed-loop-RL, supporting-foundation
- Model size: Alpamayo 2 2B VLA backbone; 8B SFT ablation
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

運転に重要な周辺物体を言語メモとして書き、後の軌跡予測と質問応答に再利用するAD-Memo。Da Capoは運転トークンへ時点別、メモへ将来依存の学習信号を割り当てる。

**主な貢献**

四方停止と一般運転の実映像クリップで軌跡品質・記憶質問応答・他モデルへのメモ移植を評価。制御入力は正解履歴を再生し、記憶だけを閉ループ化するため、実車の閉ループ走行成功や安全性能を実証した結果ではない。

**確認記録**

- Checked: 2026-10-03 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.38641v1 の3節、4節のbaseline設定、付録D.2/Fと公式projectの評価を確認。主実験は約10秒の言語メモと2B VLA backboneで、Alpamayoのaction expertは含まない。8BはSFT追加評価。本文/公式projectに専用code・weight・実装license提供先を確認できずunknown。運転分野の支援研究として扱い、マニピュレーションへの効果は未検証。PDF未取得。

### D²-VLA: Dual-Memory Dual-Frequency Vision-Language-Action Model For Long Dynamic Manipulation

- ID: `VLA-0124`
- Published: 2026-09-28 · Updated: 2026-09-30
- Authors: Zijian Ye; Chengqi Wei; Wei Huang; Anlin Zheng; Chunyu Zou; Liangyu Wu; Zikang Zhao; Zhenjie Peng; Yushuo Yang; Shuman Zhao; Zhongrui Wang; Xiaojuan Qi
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.34792)
- Tags: dual-memory, kv-cache, multi-rate, dynamic-manipulation
- Model size: PaliGemma-3B backbone; total unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

過去の視覚情報を保持しながら動く物体へ素早く反応するD²-VLA。VLMと行動専門家に別々の履歴KV参照を持たせ、低頻度VLM更新の間は新しい視覚特徴で行動条件を補正する。

**主な貢献**

ブロック単位の因果KV再利用と非対称な二重記憶、異なる更新周期の制御を統合。過去の視覚手掛かりと動的操作を要するDOMINO-Longを導入。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 and v2 exact dates verified; one identity, not two additions. Primary HTML https://arxiv.org/html/2609.34792v2 links https://github.com/CVMI-Lab/DMDF-VLA; repository currently shows Readme.md and images only, so actual implementation, code license and weights remain unknown. Linked project on zijianyy.github.io failed to fetch; exact project path not recorded. Backbone stated in §5.1; total parameters not verified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### MemBodied: Recurrent Associative Memory for Vision-Language-Action Models

- ID: `VLA-0130`
- Published: 2026-09-23
- Authors: Tej Deep Pala; Navonil Majumder; Bryce Goh; Raphael Yee; Jianfei Yang; Liming Chen; Soujanya Poria
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.28256) · [Code](https://github.com/declare-lab/MemBodied) · [Project](https://declare-lab.github.io/MemBodied/)
- Tags: associative-memory, episodic-anchor, recurrent, partial-observability
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

エピソードの初期場面を保持するアンカーと、行動後の結果を書き込む連想記憶をVLAへ追加するMemBodied。過去画像列を無制限に入力せず、固定サイズの状態から行動を生成する。

**主な貢献**

層別の連想読み出しと遅延した遷移条件付き書き込みにより、履歴依存の操作を支援。5RMBenchタスクで平均成功率50%を報告し、記憶の構成を比較。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv submission history shows v1 only on 2026-09-23, despite secondary indexing timestamps on Sep 24; do not treat indexing as revision. Official project and implementation verified. https://github.com/declare-lab/MemBodied/blob/main/LICENSE is Apache 2.0; vendored components retain their licenses. README explicitly says trained checkpoints are not bundled; no public weight download verified, so weights unknown. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

- ID: `VLA-0116`
- Published: 2025-08-26 · Updated: 2026-01-30
- Authors: Hao Shi; Bin Xie; Yingfei Liu; Lin Sun; Fengrong Liu; Tiancai Wang; Erjin Zhou; Haoqiang Fan; Xiangyu Zhang; Gao Huang
- Venue: ICLR 2026
- Links: [Paper](https://arxiv.org/abs/2508.19236) · [PDF](https://arxiv.org/pdf/2508.19236) · [Code](https://github.com/shihao1895/MemoryVLA) · [Project](https://shihao1895.github.io/MemoryVLA)
- Tags: MemoryVLA, working-memory, episodic-memory, temporal-context, long-horizon
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: available / available / unspecified

**概要（日本語）**

現在観測の知覚・認知トークンをworking memoryとし、過去の低レベル詳細と意味情報をmemory bankへ保持するVLA。必要な記憶の検索・融合・重複統合を行い、記憶条件付き拡散行動生成で長期操作を評価した。

**主な貢献**

Perceptual-Cognitive Memory Bankとworking-memory検索を接続し、現在フレームだけでは解けない時間依存操作へ対応。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。実装とモデルcollectionを確認。2026-10-01時点で公開リポジトリrootにLICENSEなし、GitHub license=null。ライセンス未指定のためopen\_sourceはunknown。https://huggingface.co/collections/shihao1895/memoryvla
