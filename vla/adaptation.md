<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / adaptation

[← vla](README.md) · [CSV master](../papers.csv)

12 records · Published date 降順（同日 ID 降順）

### Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks

- ID: `VLA-0137`
- Published: 2026-10-01
- Authors: Sophie Higham; Riccardo Andrea Izzo; Matteo Matteucci; Alessandro Suglia
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01351) · [Project](https://github.com/esgi-research-group/vla-reliability)
- Tags: supporting-evaluation, behavioural-robustness, input-perturbations, trajectory-metrics, reliability
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unavailable / unknown / unknown

**概要（日本語）**

成功したVLA軌跡に限定して、入力摂動による滑らかさ・移動距離・グリッパ挙動とそのばらつきを測る評価手法。成功率だけでは隠れる行動変化をLIBEROとLIBERO-Plusで調べる。

**主な貢献**

軌跡指標の典型値変化とMADによるばらつきを区別し、統計検定とFDR補正を適用。π0.5とVLANeXtは四スイート、OpenVLA-OFTはSpatialだけを評価し、実機での効果と失敗軌跡は検証範囲外。

**確認記録**

- Checked: 2026-10-02 · Review: needs-review
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2610.01351v1 のIII–IV節・VI節を確認。本文はfull code availableと記載するが公式repo default branch initial-setupはREADMEのみで、READMEは公開を論文出版後と明記。確認時の研究実装はunavailableとしcode\_urlは空欄、公開状態の不整合をneeds-reviewに保持。重み・実装ライセンスはunknown。新規VLA方策ではなく評価の支援研究。PDF未取得。

### ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing

- ID: `VLA-0135`
- Published: 2026-10-01
- Authors: Zhugang Liu; Kaichuang Zhang; Jinman Zhang; Pu Sun; Martha Asare; Jose Hernandez; Maxim Ermolinsky; Efren Saenz; Qi Lu; Jinghao Yang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2610.01856)
- Tags: embodiment-adaptation, action-chunking, manufacturing, LoRA, cloud-edge
- Model size: OpenVLA-OFT 7B backbone
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

OpenVLA-OFTをFAIRINO FR3の固定製造セルへ適応させるデータ変換・LoRA・実行パイプライン。単眼デモをTFDS/RLDSへ揃え、遠隔推論で得た8ステップの行動チャンクを実行後に再観測する。

**主な貢献**

座標系・行動正規化・チャンク実行の整合を具体化し、実機の対象物移送42試行で39成功を報告。並列ホスト推論は実機評価に使われず、適応とチャンク長の効果は単独で分離されていない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXivのv1初稿・著者・arXiv DOIを確認。HTML https://arxiv.org/html/2610.01856v1 のIV節、V節の実機・照明評価を読んだ。固定セルの赤/青ブロック移送は汎用製造能力の実証と区別。実装・専用重み・実装ライセンスの公式提供先は本文リンクとタイトル検索で未確認。PDF未取得、正確なPDF href未抽出のためpdf\_urlは空欄。

### Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

- ID: `VLA-0138`
- Published: 2026-09-30
- Authors: Mingyue Cui; Zheyuan Liu; Yihan Zhu; Zheyuan Zhang; Meng Jiang
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.39820) · [Code](https://github.com/Mingyuee88/FailBank) · [Project](https://mingyuee88.github.io/FailBank/)
- Tags: FailBank, self-evolution, failure-bank, observe-only-teacher, guarded-LoRA, safety
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

方策が実行した行動へ観察専用CBF教師の反事実的補正を記録し、結果で選別した失敗バンクと成功行動のアンカーからLoRAを更新するFailBank。検証損失と行動ドリフトのガードを満たす更新だけを採用する。

**主な貢献**

一時的なランタイム制約を永続的な方策学習信号へ変える四段階手順。VLA-Arenaの静的障害物二難度・π0/π0.5で成功率と方策由来接触コストを併記し、平均改善を全課題や動的障害物の安全保証とは扱わない。

**確認記録**

- Checked: 2026-10-02 · Review: verified
- arXiv v1初稿・著者、HTML https://arxiv.org/html/2609.39820v1 の4節・5.2節・6.3節を確認。収集教師は特権シミュレータ形状を使い、展開方策には不要。公式project経由のsrc実装・READMEとroot Apache-2.0を確認: https://github.com/Mingyuee88/FailBank/blob/main/LICENSE 。第三者成分は別条項。READMEのVLA-Arena重みは基礎方策でありFailBank専用adapterの提供を確認できずweights\_status=unknown。PDF未取得。

### Self-Adaptive VLA for Robust Robot Deployment

- ID: `VLA-0123`
- Published: 2026-09-24
- Authors: Hongxin Zhang; Chunru Lin; Tsun-Hsuan Wang; Zhenjia Xu; Chuang Gan
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.30092) · [Project](https://icefoxzhx.github.io/self-adaptive-vla/)
- Tags: test-time-adaptation, hardware-shift, context, bimanual
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

駆動バイアスや関節エンコーダーのずれに対し、自身の試行履歴を文脈トークンへ圧縮してVLAを補償する事後学習法。複数試行のトークンを統合し、配備先で反復的に補正する。

**主な貢献**

既存の専門家デモを既知の機器ずれに事前補償し、軽量文脈エンコーダーとAdaLNを学習。精密な双腕・器用操作4タスクで性能回復を報告。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Official project videos/method and primary HTML https://arxiv.org/html/2609.30092v1 checked; no research code repository, implementation license, or trained weight download verified. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### Dissecting Advantage-Guided Post-Training for Vision-Language-Action Policies

- ID: `VLA-0128`
- Published: 2026-09-23
- Authors: Jiahang Cao; Hanye Zhao; Hang Lai; Shenyu Zhang; Xiaoshen Han; Xinghang Li; Futeng Liu; Wanli Peng; Heyun Wang; Yunhong Wang; Jason Li; Yong Yu; Weinan Zhang
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.28161) · [Project](https://dissectvla.github.io/)
- Tags: post-training, advantage-weighting, offline-diagnostics, bimanual
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

VLAの優位度に基づく事後学習を、優位度構成・尺度校正・方策利用の3段階に分解する制御比較。実機評価の前に候補を選べる段階別オフライン診断を導入する。

**主な貢献**

TD優位度、グループ別校正、連続重み付けの組合せを識別。固定データ・方策・予算による4双腕タスクの比較で診断と実機性能の整合性を調べる。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.28161v1 directly links verified project https://dissectvla.github.io/. Project contains videos and study details, no verified research code or trained weight release; website template/website CC license is not an implementation license. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

- ID: `VLA-0143`
- Published: 2026-09-22
- Authors: Zeyu Lou; Tianran Zhang; Xinquan Yue; Ya Jing; Chenyang Si
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.26313) · [Code](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop)
- Tags: execution-safety, hazard-prediction, rollback, safe-waypoint-memory, frozen-VLA, asymmetric-PPO
- Model size: Qwen2.5-VL-3B predictor backbone; total parameters unknown
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

凍結VLAへ外付けの危険予測と復帰制御を加える。身体・物体の危険確率と発生までの時間を推定し、低頻度PPO制御器が続行・安全地点記録・関節空間rollbackを選ぶ。

**主な貢献**

24 LIBERO課題×16seed、実機三課題×25試行で安全性と成功率を比較。実機は予測器を適応しdeciderをそのまま移す。安全地点は予測閾値に基づき形式保証ではなく、不可逆な物体変化は戻せない。公開releaseはPi0向けで訓練データは含まれない。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿2026-09-22 12:22:44 UTC、改訂なし。arXiv commentsはIROS 2026受理を記載するが、会議側では独立確認していない。HTML §III–V確認: https://arxiv.org/html/2609.26313v1 。公式release/safeloop実装とApache-2.0 LICENSE確認: https://github.com/Loule0-0/SafeLoop/blob/release/safeloop/LICENSE 。HF公開head重み・Apache-2.0カード確認: https://huggingface.co/Jaqen0-0/SafeLoop/tree/main/decision\_heads 。pi0-v1の8ファイルmanifest: https://github.com/Loule0-0/SafeLoop/blob/release/safeloop/configs/release/artifacts\_pi0\_v1.json 。重み未ダウンロードでchecksum自体は未検証。基盤モデルは別ライセンス。PDF未取得。

### RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy

- ID: `VLA-0142`
- Published: 2026-09-22
- Authors: Chongyu Zhu; Jaden Hinds; Hyegang Kim; Juan Sebastian Rojas; Ramy Elmallah; Chi-Guhn Lee
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2609.26467)
- Tags: RL-specialist, controller-routing, SmolVLA, action-chunk, precision-control, operator-aligned-handoff
- Model size: SmolVLA backbone; total router/specialist parameters unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

凍結SmolVLAの潜在表現から担当制御器を推定し、精密段階だけRL専門方策へ切り替える。ヒステリシス等で切替を安定化し、担当変更時に古いaction chunkの未実行部分を破棄する。

**主な貢献**

LIBERO Object三課題・60保持試行・三学習seedで全課題成功85.00%から92.22%。実機挿入は6.7%から35.0%だが、挿入開始前に操作者が位置合わせする。大規模専門方策群・完全自律の多専門方策合成・他の幾何形状は未検証。

**確認記録**

- Checked: 2026-10-04 · Review: verified
- arXiv v1初稿2026-09-22 14:15:28 UTC、改訂なし。arXiv commentsはIROS 2026 IARL Workshop受理を記載するが、会議側では独立確認していない。HTML §III・IV・Vで手法・評価・制約を確認: https://arxiv.org/html/2609.26467v1 。実機はRouteRLT20試行、対照30試行。phaseラベル・専門方策学習にはprivileged境界を使用し、実行時router入力には使わない。本文と著者/手法名検索で公式公開実装・重み・実装ライセンス・独立project未確認。PDF未取得。

### Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

- ID: `VLA-0122`
- Published: 2026-09-20
- Authors: Shuaijun Liu; Feiyang You; Chengyu Wu; Shuyang Hao; Chenglong Zhang; Jingyao Cai; Xingwei Chen; Ningxin Su
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.23650) · [Code](https://github.com/NEBULIS-Lab/Beyond-Appearance-Shifts) · [Project](https://nebulis-lab.com/Beyond-Appearance-Shifts/)
- Tags: semantic-calibration, frozen-vla, robustness, residual
- Model size: unknown
- Open-source: true
- Code / weights / license: available / unknown / open-source

**概要（日本語）**

見た目だけが変わる条件と、対象物や制約が変わる条件を区別し、凍結VLAの出力行動を補正するBAS-VLA。意味変更後に旧タスクを続ける失敗を抑え、外観変動への頑健性も評価する。

**主な貢献**

意味変更を中心とした残差キャリブレーターと、意味の一貫性を確認した場合だけ有効化する補助経路を統合。旧タスク抑制と新タスク達成を別指標として評価。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Official project links official GitHub. Actual bas\_vla implementation, training/evaluation scripts and LICENSE are present; GitHub identifies MIT license. Root LICENSE content independently read via GitHub connector and confirmed standard MIT: https://github.com/NEBULIS-Lab/Beyond-Appearance-Shifts/blob/main/LICENSE . README requires separately supplied carrier and adapter weights; public adapter download unverified. Project/repository claim NeurIPS 2026, but organizer acceptance not independently checked. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models

- ID: `VLA-0133`
- Published: 2026-09-18
- Authors: Kaiwen Zhu; Dongfang Liu; Liangkai Liu
- Venue: arXiv preprint
- Links: [Paper](https://arxiv.org/abs/2609.21246)
- Tags: failure-prediction, ood, execution-history, reliability
- Model size: unknown
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

入力の分布外変化を検出・分類し、行動履歴と実行進捗を組み合わせてVLAの失敗確率を更新するVLA-Scope。OpenVLAのLIBERO-Spatial10タスクで評価する。

**主な貢献**

分布外入力と実行失敗を同一視せず、共有ロジスティック回帰で履歴依存の失敗予測を行う。1400分布外試行で進捗特徴の効果を比較。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- arXiv v1 only. Primary HTML https://arxiv.org/html/2609.21246v1 checked for author-owned implementation/license or weight links; none verified. CC Zero shown on arXiv is the paper license, not evidence of released implementation. This is a reliability framework rather than a new generalist action backbone. Paper URL and arXiv-issued DOI verified on abstract page. PDF linked by arXiv but exact href not extracted and PDF not fetched; pdf\_url left blank. Unknown means unverified, not a closed-source claim.

### OpenVLA: An Open-Source Vision-Language-Action Model

- ID: `VLA-0104`
- Published: 2024-06-13 · Updated: 2024-09-05
- Authors: Moo Jin Kim; Karl Pertsch; Siddharth Karamcheti; Ted Xiao; Ashwin Balakrishna; Suraj Nair; Rafael Rafailov; Ethan Foster; Grace Lam; Pannag Sanketi; Quan Vuong; Thomas Kollar; Benjamin Burchfiel; Russ Tedrake; Dorsa Sadigh; Sergey Levine; Percy Liang; Chelsea Finn
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2406.09246) · [PDF](https://arxiv.org/pdf/2406.09246) · [Code](https://github.com/openvla/openvla) · [Project](https://openvla.github.io/)
- Tags: OpenVLA, generalist-policy, parameter-efficient-finetuning, quantization, cross-embodiment
- Model size: 7B
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

97万件の実機軌跡で学習した7BのVLAを公開。DINOv2とSigLIPの視覚特徴をLlama 2へ接続し、複数ロボット制御と新環境への微調整を評価した。LoRAと量子化による利用コスト削減も検証した。

**主な貢献**

公開の汎用VLAと、消費者向けGPUでの効率的な適応・推論手順を一体化。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。重み: https://huggingface.co/openvla/openvla-7b 。コードMITと基盤Llama 2の利用条件は別。 Code license: MIT; https://github.com/openvla/openvla/blob/main/LICENSE.

### Octo: An Open-Source Generalist Robot Policy

- ID: `VLA-0105`
- Published: 2024-05-20 · Updated: 2024-05-26
- Authors: Octo Model Team; Dibya Ghosh; Homer Walke; Karl Pertsch; Kevin Black; Oier Mees; Sudeep Dasari; Joey Hejna; Tobias Kreiman; Charles Xu; Jianlan Luo; You Liang Tan; Lawrence Yunliang Chen; Pannag Sanketi; Quan Vuong; Ted Xiao; Dorsa Sadigh; Chelsea Finn; Sergey Levine
- Venue: RSS 2024
- Links: [Paper](https://arxiv.org/abs/2405.12213) · [PDF](https://arxiv.org/pdf/2405.12213) · [Code](https://github.com/octo-models/octo) · [Project](https://octo-models.github.io/)
- Tags: Octo, generalist-policy, diffusion-policy, goal-conditioning, cross-embodiment
- Model size: 27M (Small); 93M (Base)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

80万軌跡から事前学習したTransformerベースの汎用ロボット方策。言語または目標画像で指示し、新しいセンサー入力や行動空間へ少量データで適応できる設計を9種類のロボット環境で評価した。

**主な貢献**

柔軟な観測・タスクトークン化と拡散行動ヘッドにより、ロボットごとの入出力変更へ効率的に適応。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式プロジェクトにモデル規模とRSS 2024書誌、Hugging Face重みへのリンク。 Code license: MIT; https://github.com/octo-models/octo/blob/main/LICENSE.

### Open X-Embodiment: Robotic Learning Datasets and RT-X Models

- ID: `VLA-0103`
- Published: 2023-10-13 · Updated: 2025-05-14
- Authors: Open X-Embodiment Collaboration; Abby O'Neill; Abdul Rehman; Abhinav Gupta; Abhiram Maddukuri; Abhishek Gupta; Abhishek Padalkar; Abraham Lee; Acorn Pooley; Agrim Gupta; Ajay Mandlekar; Ajinkya Jain; Albert Tung; Alex Bewley; Alex Herzog; Alex Irpan; Alexander Khazatsky; Anant Rai; Anchit Gupta; Andrew Wang; Andrey Kolobov; Anikait Singh; Animesh Garg; Aniruddha Kembhavi; Annie Xie; Anthony Brohan; Antonin Raffin; Archit Sharma; Arefeh Yavary; Arhan Jain; Ashwin Balakrishna; Ayzaan Wahid; Ben Burgess-Limerick; Beomjoon Kim; Bernhard Schölkopf; Blake Wulfe; Brian Ichter; Cewu Lu; Charles Xu; Charlotte Le; Chelsea Finn; Chen Wang; Chenfeng Xu; Cheng Chi; Chenguang Huang; Christine Chan; Christopher Agia; Chuer Pan; Chuyuan Fu; Coline Devin; Danfei Xu; Daniel Morton; Danny Driess; Daphne Chen; Deepak Pathak; Dhruv Shah; Dieter Büchler; Dinesh Jayaraman; Dmitry Kalashnikov; Dorsa Sadigh; Edward Johns; Ethan Foster; Fangchen Liu; Federico Ceola; Fei Xia; Feiyu Zhao; Felipe Vieira Frujeri; Freek Stulp; Gaoyue Zhou; Gaurav S. Sukhatme; Gautam Salhotra; Ge Yan; Gilbert Feng; Giulio Schiavi; Glen Berseth; Gregory Kahn; Guangwen Yang; Guanzhi Wang; Hao Su; Hao-Shu Fang; Haochen Shi; Henghui Bao; Heni Ben Amor; Henrik I Christensen; Hiroki Furuta; Homanga Bharadhwaj; Homer Walke; Hongjie Fang; Huy Ha; Igor Mordatch; Ilija Radosavovic; Isabel Leal; Jacky Liang; Jad Abou-Chakra; Jaehyung Kim; Jaimyn Drake; Jan Peters; Jan Schneider; Jasmine Hsu; Jay Vakil; Jeannette Bohg; Jeffrey Bingham; Jeffrey Wu; Jensen Gao; Jiaheng Hu; Jiajun Wu; Jialin Wu; Jiankai Sun; Jianlan Luo; Jiayuan Gu; Jie Tan; Jihoon Oh; Jimmy Wu; Jingpei Lu; Jingyun Yang; Jitendra Malik; João Silvério; Joey Hejna; Jonathan Booher; Jonathan Tompson; Jonathan Yang; Jordi Salvador; Joseph J. Lim; Junhyek Han; Kaiyuan Wang; Kanishka Rao; Karl Pertsch; Karol Hausman; Keegan Go; Keerthana Gopalakrishnan; Ken Goldberg; Kendra Byrne; Kenneth Oslund; Kento Kawaharazuka; Kevin Black; Kevin Lin; Kevin Zhang; Kiana Ehsani; Kiran Lekkala; Kirsty Ellis; Krishan Rana; Krishnan Srinivasan; Kuan Fang; Kunal Pratap Singh; Kuo-Hao Zeng; Kyle Hatch; Kyle Hsu; Laurent Itti; Lawrence Yunliang Chen; Lerrel Pinto; Li Fei-Fei; Liam Tan; Linxi "Jim" Fan; Lionel Ott; Lisa Lee; Luca Weihs; Magnum Chen; Marion Lepert; Marius Memmel; Masayoshi Tomizuka; Masha Itkina; Mateo Guaman Castro; Max Spero; Maximilian Du; Michael Ahn; Michael C. Yip; Mingtong Zhang; Mingyu Ding; Minho Heo; Mohan Kumar Srirama; Mohit Sharma; Moo Jin Kim; Muhammad Zubair Irshad; Naoaki Kanazawa; Nicklas Hansen; Nicolas Heess; Nikhil J Joshi; Niko Suenderhauf; Ning Liu; Norman Di Palo; Nur Muhammad Mahi Shafiullah; Oier Mees; Oliver Kroemer; Osbert Bastani; Pannag R Sanketi; Patrick "Tree" Miller; Patrick Yin; Paul Wohlhart; Peng Xu; Peter David Fagan; Peter Mitrano; Pierre Sermanet; Pieter Abbeel; Priya Sundaresan; Qiuyu Chen; Quan Vuong; Rafael Rafailov; Ran Tian; Ria Doshi; Roberto Martín-Martín; Rohan Baijal; Rosario Scalise; Rose Hendrix; Roy Lin; Runjia Qian; Ruohan Zhang; Russell Mendonca; Rutav Shah; Ryan Hoque; Ryan Julian; Samuel Bustamante; Sean Kirmani; Sergey Levine; Shan Lin; Sherry Moore; Shikhar Bahl; Shivin Dass; Shubham Sonawani; Shubham Tulsiani; Shuran Song; Sichun Xu; Siddhant Haldar; Siddharth Karamcheti; Simeon Adebola; Simon Guist; Soroush Nasiriany; Stefan Schaal; Stefan Welker; Stephen Tian; Subramanian Ramamoorthy; Sudeep Dasari; Suneel Belkhale; Sungjae Park; Suraj Nair; Suvir Mirchandani; Takayuki Osa; Tanmay Gupta; Tatsuya Harada; Tatsuya Matsushima; Ted Xiao; Thomas Kollar; Tianhe Yu; Tianli Ding; Todor Davchev; Tony Z. Zhao; Travis Armstrong; Trevor Darrell; Trinity Chung; Vidhi Jain; Vikash Kumar; Vincent Vanhoucke; Vitor Guizilini; Wei Zhan; Wenxuan Zhou; Wolfram Burgard; Xi Chen; Xiangyu Chen; Xiaolong Wang; Xinghao Zhu; Xinyang Geng; Xiyuan Liu; Xu Liangwei; Xuanlin Li; Yansong Pang; Yao Lu; Yecheng Jason Ma; Yejin Kim; Yevgen Chebotar; Yifan Zhou; Yifeng Zhu; Yilin Wu; Ying Xu; Yixuan Wang; Yonatan Bisk; Yongqiang Dou; Yoonyoung Cho; Youngwoon Lee; Yuchen Cui; Yue Cao; Yueh-Hua Wu; Yujin Tang; Yuke Zhu; Yunchu Zhang; Yunfan Jiang; Yunshuang Li; Yunzhu Li; Yusuke Iwasawa; Yutaka Matsuo; Zehan Ma; Zhuo Xu; Zichen Jeff Cui; Zichen Zhang; Zipeng Fu; Zipeng Lin
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2310.08864) · [PDF](https://arxiv.org/pdf/2310.08864) · [Code](https://github.com/google-deepmind/open_x_embodiment) · [Project](https://robotics-transformer-x.github.io/)
- Tags: Open-X-Embodiment, RT-X, cross-embodiment, dataset-mixture, transfer
- Model size: 55B (RT-2-X)
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

複数機関・22種類のロボットのデータを統一形式で集約し、RT-1-XとRT-2-Xを訓練。異なる身体の経験を混ぜることで、各ロボットの単独学習より有利になる正の転移を示した。

**主な貢献**

異種ロボットデータの標準化とクロスエンボディメント方策学習を、共有データとモデルで検証。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。open\_sourceは公開リポジトリの実装に対する判定。RT-1-Xの公開checkpointと非公開RT-2-Xを区別。https://github.com/google-deepmind/open\_x\_embodiment Code license: Apache-2.0; https://github.com/google-deepmind/open\_x\_embodiment/blob/main/LICENSE.
