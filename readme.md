# 仕様
行単位で重複を表示し、削除する

# 説明
unixのuniqコマンドだと前後の重複しか判断してくれないので製作した。  
ファイル内で重複している行がある場合、表示・削除する。

## 実行文
> python uniq-txt.py [ファイル名]

## 操作
1. 重複を削除したいファイルを同ディレクトリに移動
- uniq-txt.pyを起動（実行文を参照）
- 以下を聞かれるのでyを入力
> Are you sure you want to create a unique list to remove the above-mentioned? (y/n) >

- バックアップファイルが作成され、重複が削除される。
