# Text Editor

#### 使用技術
<p style="display: inline">
<img src="https://img.shields.io/badge/-Linux-212121.svg?logo=linux&style=popout">
<img src="https://img.shields.io/badge/-Python-FFC107.svg?logo=python&style=popout">
</p>

&nbsp;

## 概要

テキストベースのファイルの内容を反転・コピー・複製・文字の置き換えした新しいファイルを作成するプログラムです．

&nbsp;

#### 操作方法
- **copy**<br>inputfile_pathにあるファイルを受け取り，outputfile_pathにinputfile_pathの内容を反転させた新しいファイルを作成<br>
`python main.py reverse inputfile_path outputfile_path`

- **copy**<br>inputfile_pathにあるファイルのコピーを作成し，outputfile_pathとして保存<br>
`python main.py copy inputfile_path outputfile_path`

- **duplicate-contents**<br>inputpathにあるファイルの内容を読み込み，その内容を複製し，複製された内容をinputfile_pathにn回複製<br>
`python main.py duplicate-contents inputfile_path n`

- **replace-string**<br>inputfile_pathにあるファイルの内容から文字列'hogehoge'を検索し，'hogehoge'の全てを'fugafuga'に置換<br>
`python main.py repalce-string inputpath hogehoge fugafuga`

&nbsp;

## 環境構築
### 開発環境
| OS・言語・ライブラリ | バージョン |
| :------- | :------ |
| Ubuntu | 22.04.4 LTS |
| Python | 3.10.12 |

&nbsp;