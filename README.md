# barusutaiki (バルス待機)

## 機能
ツイッターにて、TL上に「バルス！」というツイートが10秒間に4回以上出現したら、自分も「バルス！」とツイートします。

## 動作環境
pythonが必要です（動作確認は2.7.4）。ライブラリtweepyも必要です。

## 使い方
keysというファイルを同じディレクトリに用意してアクセスキーを書きます（フォーマットは同梱のkeys.sample）参照。そして、「python barusutaiki.py」と入力します。

## アクセスキーのとり方
http://tande.jp/lab/2011/01/638
を参考にしてください。
Read and Writeの許可が必要です。

大体以下のような流れになります。（メニュー名は英語版）
1. http://dev.twitter.com にアクセス
2. 右上のアイコンのプルダウンから「My applications」を選択
3. 「Create a new application」ボタンを押す
4. Name, Description, Websiteを適当に入れて、キャプチャを入れて、「Create your Twitter applicatioin」ボタンを押す。
5. 「Setting」タブを開いて「Application Type」で、Read and Writeを選び、「Update this Twitter application settings」ボタンを押す。
6. 「Details」タブに戻って、「Create my access token」ボタンを押す
7. これで必要な情報はすべて表示されています。Consumer key, Consumer secret, Access token, Access token secretをコピーしてください。

アクセスキーをとったら、keys.sampleを参考にして記入して、keysというファイル名で保存してください。

## 最後に
絶対同じ事やってる奴いるだろうと思って「バルス 自動ツイート」でググっても見つからなかった。