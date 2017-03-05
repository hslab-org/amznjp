##【　注意　】　pricecheckというサイトがなくなったので動作しません。##

prigiza(ver 0.002)
 
prigizaはamazonjapanの商品が売れているかどうかを気軽に調べるツールです。

プライスチェック（ http://so-bank.jp/ ）というサイトを参照します。

ウェブブラウザ使ってサイトにわざわざ行かなくても、コマンド一発で調べられます。

一ヶ月に何回ランキングが上がったか。現在の価格はいくらかを調べます。

ASINコードを一行一行リスト化したテキストファイルを読み込ませると、

複数の商品を順番にしらべられます。

インストール方法

　0. PythonとGitをインストール（LinuxやMacの場合最初から入っている確率が高い）

　1. $ git clone https://github.com/nextaacs/amznjp.git

　2. $ cd amznjp

　3. $ su

　4. # cp ./prigiza.py /usr/bin/prigiza

　5. # prigiza
