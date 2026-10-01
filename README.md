<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->
# Robot Foundation Model Trends

ロボット基盤モデルとその周辺技術の研究データベース。CSV を唯一の正本として、分類別の Markdown を自動生成します。VLA / WAM / Agent / Hybrid の技術地図を継続的に育てるための公開リサーチ基盤です。

- 正本: [papers.csv](papers.csv) · 85 records
- Last updated: 2026-10-01（source_checked の最大値。ビルド日時には依存しません）
- スキーマ: [schema.json](schema.json) · [フィールド定義](SCHEMA.md)
- 更新手順: [AGENTS.md](AGENTS.md)
- ソフトウェアのライセンスは未選定です。各論文・コード・PDF の権利は各権利者に帰属します

## 分類ごとの論文数

| 分類 | 論文数 |
| --- | ---: |
| [VLA · Vision–Language–Action](vla/README.md) | 21 |
| [WAM · World / Action Models](wam/README.md) | 48 |
| [Agent](agent/README.md) | 12 |
| [Hybrid](hybrid/README.md) | 4 |
| **合計** | **85** |

件数は実際の CSV 行から計算されます。分類は主な研究貢献に基づく整理で、論文の公式分類や能力保証ではありません。複数分類にまたがる性質は tags と説明に残し、重複登録を避けます。

## 技術マップ

### [VLA · Vision–Language–Action](vla/README.md)

- [perception-representation](vla/perception-representation.md) (1)
- [reasoning-system2](vla/reasoning-system2.md) (4)
- [action-system1](vla/action-system1.md) (12)
- [memory-temporal](vla/memory-temporal.md) (1)
- [adaptation](vla/adaptation.md) (3)

### [WAM · World / Action Models](wam/README.md)

- [world-representation](wam/world-representation.md) (24)
- [dynamics](wam/dynamics.md) (7)
- [action-coupling](wam/action-coupling.md) (4)
- [planning](wam/planning.md) (10)
- [temporal-modeling](wam/temporal-modeling.md) (3)

### [Agent](agent/README.md)

- [planning](agent/planning.md) (3)
- [code](agent/code.md) (4)
- [skill](agent/skill.md) (1)
- [tool](agent/tool.md) (1)
- [memory](agent/memory.md) (1)
- [replanning](agent/replanning.md) (2)

### [Hybrid](hybrid/README.md)

- [vla-agent](hybrid/vla-agent.md) (1)
- [vla-wam](hybrid/vla-wam.md) (3)
- [wam-agent](hybrid/wam-agent.md) (0)
- [vla-wam-agent](hybrid/vla-wam-agent.md) (0)

WAM の world-representation には、ロボットで使われる表現学習や動画基盤モデルなどの支援的研究も含められます。その場合は supporting-foundation などのタグと概要で位置づけを明記し、ロボット方策を直接学習した論文と混同しません。

## 使い方

Python 3.10 以上の標準ライブラリだけで動作します。追加パッケージは不要です。リポジトリのルートで実行してください。

```sh
python scripts/validate_csv.py
python scripts/build_markdown.py
python scripts/build_markdown.py --check
python -m unittest discover -s tests -v
```

公開前・更新時は検証、生成、テストをすべて通します。CI はネットワークを使わず、CSV と生成物の一致を確認します。README と分類別ページを手で変更せず、紹介文は docs/README.template.md を編集して再生成します。

### 重複候補をローカルで調べる

```sh
python scripts/validate_csv.py --title 'π0: A Vision-Language-Action Flow Model for General Robot Control'
python scripts/validate_csv.py --candidate candidates.json
python scripts/validate_csv.py --previous previous-papers.csv
```

候補ファイルは少量の JSON オブジェクト／配列か CSV です。title、id、paper_url、pdf_url のいずれかを指定します。ローカルのメタデータだけを照合し、本文や PDF を取得しません。arXiv ID はバージョンを除去し、DOI は表記ゆれを正規化します。NFKC、大文字小文字、句読点、π / pi などを比較し、曖昧な候補は人が確認します。警告で自動削除・統合しません。

### PDF は選択して任意取得

デフォルトは一覧表示のみで、ネットワーク通信は行いません。

```sh
python scripts/download_papers.py --category WAM --subcategory "Dynamics"
python scripts/download_papers.py --id WAM-0001 --download
python scripts/download_papers.py --category vla --download
```

category は大文字小文字を区別せず、subcategory は機械キーと schema.json の英語表示名を受け付けます。

全件取得は明示的な python scripts/download_papers.py --all --download のみです。サーバーの利用規約・レート制限・権利を尊重してください。リトライとバックオフ、PDF ヘッダー確認、一時ファイルからの原子的保存、容量上限があります。HTML やエラーページを PDF として保存しません。既存の正常な PDF は再取得しません。PDF ヘッダー検証は内容の安全性や完全性を保証するものではありません。

公開 HTTP(S) のみを対象にし、初期 URL と各リダイレクトの宛先を送信前に検証します。非公開・ループバック・リンクローカル等の IP、認証情報付き URL、解決不能なホストは拒否します。DNS の全候補を検証し、接続先を確認した公開 IP に固定して再解決の競合を避けます。環境のプロキシは使いません。TLS の証明書検証とホスト名は維持します。社内 URL やプロキシ必須環境はサポートしません。

標準の WAM-0001 等のファイル名は維持し、それ以外の ID は元 ID 全体の SHA-256 を加えて、句読点や大文字小文字の正規化による別論文の取り違えを避けます。

取得物は papers/ に保存し、Git には追加しません。PDF は CI・生成・研究更新のたびに自動ダウンロードしません。

## 品質と公開範囲

- 一次情報（論文、公式プロジェクト、著者の公開コード）を根拠にします
- published は最初のプレプリント公開日。arXiv 改訂日は updated に記録し、新しい論文として追加しません
- 正確な初出日が不明なら空欄とし、needs-review と理由を残します。推測の日付は使いません
- open_source は true / false / unknown。コード公開、重み公開、ライセンスを別々に記録します
- コードが読めることだけでオープンソースとは判断しません。unknown を false に変換しません
- 取り込み時点の source_checked と evidence_note を残します。ソースやライセンスは変わり得ます
- 公開可能な研究情報だけを扱い、秘密・個人情報・認証情報を追加しません

このデータベースは網羅性・性能順位・ライセンス助言を保証しません。各リンク先と原文を確認してください。
