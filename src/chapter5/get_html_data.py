# ライブラリrequestsを読み込み
import requests

# 今回スクレイピングするサイト
url ="https://www.mhlw.go.jp/stf/covid-19/open-data.html"

# 対象のwebサイトに対してGETリクエストを行う。
response = requests.get(url)

# 文字化を修正
response.encoding = response.apparent_encoding

# ./html/open-data.htmlにhtmlファイルを書き込み
with open("./html/open-data.html",'w') as f:
    f.write(response.text)