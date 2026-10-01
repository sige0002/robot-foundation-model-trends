<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# VLA · Vision–Language–Action / reasoning-system2

[← vla](README.md) · [CSV master](../papers.csv)

4 records · Published date 降順（同日 ID 降順）

### π0.5: a Vision-Language-Action Model with Open-World Generalization

- ID: `VLA-0107`
- Published: 2025-04-22 · Updated: 2025-04-22
- Authors: Physical Intelligence; Kevin Black; Noah Brown; James Darpinian; Karan Dhabalia; Danny Driess; Adnan Esmail; Michael Equi; Chelsea Finn; Niccolo Fusai; Manuel Y. Galliker; Dibya Ghosh; Lachy Groom; Karol Hausman; Brian Ichter; Szymon Jakubczak; Tim Jones; Liyiming Ke; Devin LeBlanc; Sergey Levine; Adrian Li-Bell; Mohith Mothukuri; Suraj Nair; Karl Pertsch; Allen Z. Ren; Lucy Xiaoyang Shi; Laura Smith; Jost Tobias Springenberg; Kyle Stachowicz; James Tanner; Quan Vuong; Homer Walke; Anna Walling; Haohuan Wang; Lili Yu; Ury Zhilinsky
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2504.16054) · [PDF](https://arxiv.org/pdf/2504.16054) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.physicalintelligence.company/blog/pi05)
- Tags: π0.5, open-world-generalization, co-training, semantic-subtasks, long-horizon
- Model size: unknown / 未確認
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

π0を基に、複数ロボット、Webデータ、高レベル意味予測などの異種タスクを共同学習。画像・言語・物体検出・サブタスク・低レベル行動を混ぜ、未経験の家庭環境で長期かつ器用な操作を評価した。

**主な貢献**

高レベル意味知識と低レベル行動の異種共同学習を使い、実世界の未経験環境への汎化を拡張。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式openpi READMEにpi05\_baseとLIBERO/DROID checkpoint。公開実装はflow-matching headの訓練・推論をサポート。 Code license: Apache-2.0; https://github.com/Physical-Intelligence/openpi/blob/main/LICENSE.

### CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

- ID: `VLA-0115`
- Published: 2024-11-29 · Updated: 2024-11-29
- Authors: Qixiu Li; Yaobo Liang; Zeyu Wang; Lin Luo; Xi Chen; Mozheng Liao; Fangyun Wei; Yu Deng; Sicheng Xu; Yizhong Zhang; Xiaofan Wang; Bei Liu; Jianlong Fu; Jianmin Bao; Dong Chen; Yuanchun Shi; Jiaolong Yang; Baining Guo
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2411.19650) · [PDF](https://arxiv.org/pdf/2411.19650) · [Code](https://github.com/microsoft/CogACT) · [Project](https://cogact.github.io/)
- Tags: CogACT, cognition-action, diffusion-transformer, action-ensemble, componentized-VLA
- Model size: 7B VLM + up to 300M action module
- Open-source: true
- Code / weights / license: available / available / open-source

**概要（日本語）**

VLMを単純な離散動作予測器へ変える代わりに、その認知特徴で専用diffusion action Transformerを条件付けする。行動モジュールの規模と設計を比較し、新ロボットへの適応・未知物体や背景への汎化を評価した。

**主な貢献**

VLMの認知表現と連続行動生成をモジュール分離し、類似度に基づく適応的行動アンサンブルを導入。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式projectにVLMとaction module規模。コード・重みMIT: https://github.com/microsoft/CogACT\#license Code license: MIT; https://github.com/microsoft/CogACT/blob/main/LICENSE.

### RT-H: Action Hierarchies Using Language

- ID: `VLA-0113`
- Published: 2024-03-04 · Updated: 2024-06-01
- Authors: Suneel Belkhale; Tianli Ding; Ted Xiao; Pierre Sermanet; Quon Vuong; Jonathan Tompson; Yevgen Chebotar; Debidatta Dwibedi; Dorsa Sadigh
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2403.01823) · [PDF](https://arxiv.org/pdf/2403.01823) · [Project](https://rt-hierarchy.github.io/)
- Tags: RT-H, language-action-hierarchy, human-intervention, semantic-sharing, hierarchical-policy
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

高レベルタスクから直接動作へ写像せず、「腕を前へ動かす」などの言語的動作を中間段階に置く。異なるタスク間で低レベル構造を共有し、人間の言語介入に応じた修正と、その介入からの学習を評価した。

**主な貢献**

タスク→言語動作→ロボット行動という階層を学び、言語介入可能な低レベル制御を構成。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公開実装・重み・実装ライセンスは確認できずunknown。

### RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

- ID: `VLA-0102`
- Published: 2023-07-28 · Updated: 2023-07-28
- Authors: Anthony Brohan; Noah Brown; Justice Carbajal; Yevgen Chebotar; Xi Chen; Krzysztof Choromanski; Tianli Ding; Danny Driess; Avinava Dubey; Chelsea Finn; Pete Florence; Chuyuan Fu; Montse Gonzalez Arenas; Keerthana Gopalakrishnan; Kehang Han; Karol Hausman; Alexander Herzog; Jasmine Hsu; Brian Ichter; Alex Irpan; Nikhil Joshi; Ryan Julian; Dmitry Kalashnikov; Yuheng Kuang; Isabel Leal; Lisa Lee; Tsang-Wei Edward Lee; Sergey Levine; Yao Lu; Henryk Michalewski; Igor Mordatch; Karl Pertsch; Kanishka Rao; Krista Reymann; Michael Ryoo; Grecia Salazar; Pannag Sanketi; Pierre Sermanet; Jaspiar Singh; Anikait Singh; Radu Soricut; Huong Tran; Vincent Vanhoucke; Quan Vuong; Ayzaan Wahid; Stefan Welker; Paul Wohlhart; Jialin Wu; Fei Xia; Ted Xiao; Peng Xu; Sichun Xu; Tianhe Yu; Brianna Zitkovich
- Venue: arXiv
- Links: [Paper](https://arxiv.org/abs/2307.15818) · [PDF](https://arxiv.org/pdf/2307.15818) · [Project](https://robotics-transformer.github.io/)
- Tags: RT-2, VLM-transfer, web-knowledge, action-tokenization, semantic-generalization
- Model size: unknown / 未確認
- Open-source: unknown
- Code / weights / license: unknown / unknown / unknown

**概要（日本語）**

Web規模の視覚言語モデルをロボット軌跡と視覚言語タスクで共同微調整し、動作をテキストトークンとして出力するRT-2を提案。物体・指示の汎化に加え、ロボットデータに直接ない意味的判断を評価した。

**主な貢献**

言語出力と離散ロボット行動を同じトークン空間で学び、Web知識を低レベル制御へ直接転移。

**確認記録**

- Checked: 2026-10-01 · Review: verified
- 書誌・初稿日・最終改訂日・要旨をarXiv一次資料で確認。公式論文・プロジェクトを確認。公開実装と実装ライセンスを確認できず、open\_sourceはunknown。
