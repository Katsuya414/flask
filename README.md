## 作ったもの
 https://folio-sec.com/theme/<テーマ名>というURLになっているが
 そのテーマ名を入力として受け取り指定したテーマの銘柄一覧を見れるようにするサーバーアプリケーション

## 選択言語
Python

## 実際に構築した環境について
OS macOS ver 10.13.6

python version Python 3.7.2

追加ライブラリー requests, bs4,json,flask

## 環境構築方法
Homebrewのインストール

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

pipのインストール
```
brew install python
```

追加ライブラリーのインストール
```
pip3 install requests
pip3 install bs4

```

## サーバアプリケーションを動かす方法
```
python3 run2.py
```
