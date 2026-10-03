<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / memory-temporal

[← vla](README.md) · [CSV master](../papers.csv)

4 records · Published date 降順（同日 ID 降順）

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
