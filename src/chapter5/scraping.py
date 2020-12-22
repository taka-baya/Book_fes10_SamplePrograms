# ライブラリBeautifulSoupを読み込み、bs4として定義
from bs4 import BeautifulSoup as bs4

# 保存したhtmlファイルのファイルパス
file_path ="./html/open-data.html"

# BeautifulSoupを使って保存したhtmlファイルを読み込み
soup = bs4(open(file_path), "html.parser", from_encoding="utf-8")

# タグ「ol」、class「m-listMarker m-txtS」の要素の情報を変数「get_ol」に格納
get_ol = soup.find_all("ol", class_="m-listMarker m-txtS")

# for文を使って取得した要素の情報を一つ一つ変数「get_ol」から取り出して、変数「li_tag」に格納
for li_tag in get_ol:
    # 変数li_tagから指定した不要な情報を削除し、変数「data」に格納
    data = str(li_tag).replace('<li><span class="m-listMarker__marker">','').replace('</span>','').replace('</li>','').replace('<ol class="m-listMarker m-txtS">','').replace('</ol>','')
    
    # 変数「data」を表示
    print(f"data : {data}")

