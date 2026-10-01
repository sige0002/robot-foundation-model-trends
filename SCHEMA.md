# CSV schema

papers.csv が唯一の正本です。UTF-8、ヘッダーあり、標準 CSV 引用を使います。コンマ・引用符・改行を含むセルは csv.writer / DictWriter で正しく引用してください。authors と tags は | 区切りで、前後の空白や空項目は使いません。

## Required headings (ordered)

| Column | Meaning |
| --- | --- |
| id | 大文字小文字を区別する安定 ID。例 WAM-0001 / VLA-0101 / AGENT-0101 / HYBRID-0101。分類移動や改訂で変更しない |
| title | 一次情報の正式タイトル |
| published | 最初のプレプリント公開日 YYYY-MM-DD。正確な日付不明は空欄＋needs-review＋evidence_note |
| updated | 任意の改訂日 YYYY-MM-DD。published より前は不可 |
| authors | 著者名の | 区切り。省略する場合は et al. と明記し、完全なリストと誤認させない |
| venue | 会議・ジャーナル・ワークショップ・プレプリントなど。未確認は空欄 |
| main_category | vla / wam / agent / hybrid |
| subcategory | 下記の機械キー |
| tags | 横断属性を表す | 区切り |
| paper_url | 一次論文の絶対 http(s) URL。認証情報や空白を含めない |
| pdf_url | 公開 PDF の検証済み URL。不明なら空欄 |
| code_url | 公式公開コード URL。不明なら空欄 |
| project_url | 公式プロジェクト URL。不明なら空欄 |
| summary_ja | 日本語での研究概要 |
| key_contribution | 主な研究貢献。評価結果と推測を区別する |
| model_size | 公開されているモデル規模。未確認は空欄または unknown |
| open_source | true / false / unknown。true は公開された実装のオープンソースライセンスを確認済みの場合 |

必須は列の存在であり、すべてのセルが必須ではありません。id,title,authors,main_category,subcategory,paper_url,summary_ja,key_contribution,open_source は空欄不可。published の空欄はレビュー理由を伴う例外だけです。

## Optional review headings (after required headings)

| Column | Values / meaning |
| --- | --- |
| code_status | available / unavailable / unknown。available は code_url を必要とする |
| weights_status | available / unavailable / unknown。実装のライセンスとは別 |
| license_status | open-source / non-open-source / unspecified / unknown。ここでは実装コードのライセンスを指す。根拠を evidence_note に残す |
| source_checked | 一次情報を確認した日 YYYY-MM-DD |
| review_status | verified / needs-review。verified は source_checked を必要とする |
| evidence_note | 出典・不確実性・重みの提供先とライセンス・例外の説明 |

空欄の任意ステータスは生成ページで unknown と表示します。新規の取り込みでは unknown を明示することを推奨します。unavailable や false は積極的な否定を確認した場合であり、未調査を意味しません。公式 GitHub が存在してもライセンス未確認なら open_source=unknown です。重みがなくても実装が OSI 承認ライセンスなら open_source=true とできます。コード・重み・論文のライセンスを混ぜないでください。

## Category machine keys

| Main category | Subcategories |
| --- | --- |
| vla | perception-representation; reasoning-system2; action-system1; memory-temporal; adaptation |
| wam | world-representation; dynamics; action-coupling; planning; temporal-modeling |
| agent | planning; code; skill; tool; memory; replanning |
| hybrid | vla-agent; vla-wam; wam-agent; vla-wam-agent |

機械キーと英語表示名の対応は schema.json にあります。ID の接頭辞は初回付与の便宜にすぎず、現在の分類一致は要求しません。

## Identity and validation limits

同一 arXiv ID の abs/pdf、v1/v2、export.arxiv.org、および arXiv が発行する DOI（10.48550/arXiv.<id>）は同じ論文として扱います。DOI の doi:/doi.org 表記、エンコード、大文字小文字も正規化します。同一 ID・同一正規 ID はエラーです。タイトル完全一致（正規化後）や類似タイトル・サブタイトル差は候補警告で、人による確認が必要です。異なるタイトルでも arXiv/DOI が一致すれば重複として扱います。

検証はリンクの構文・スキーマ・整合性を確認し、リンク先の存在や研究内容の事実性は証明しません。一次情報の確認が別途必要です。--previous は共通の正規 ID を持つ行の ID 変更を検出します。正規 ID のない論文の継続性はレビューで確認してください。
