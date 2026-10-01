<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / adaptation

[← vla](README.md) · [CSV master](../papers.csv)

7 records · Published date 降順（同日 ID 降順）

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
