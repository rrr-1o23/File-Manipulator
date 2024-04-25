### File-Manipulator

テキストベースのファイルの内容を反転・コピー・複製・文字の置き換えなどをするプログラムです．

#### reverse
- inputpathにあるファイルを受け取り，outputpathにinputpathの内容を逆にした新しいファイルを作成します．
```bash
$python main.py reverse inputpath outputpath
```

#### copy
- inputpathにあるファイルのコピーを作成し，outputpathとして保存．
```bash
$python main.py copy inputpath outputpath
```

#### duplicate-contents
- inputpathにあるファイルの内容を読み込み，その内容を複製し，複製された内容をinputpathにn回複製します．
```bash
$python main.py duplicate-contents inputpath n
```

#### replace-string
- inputpathにあるファイルの内容から文字列'hogehoge'を検索し，'hogehoge'の全てを'fugafuga'に置き換えます．
```bash
$python main.py repalce-string inputpath hogehoge fugafuga
```
