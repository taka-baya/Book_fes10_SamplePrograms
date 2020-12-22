import csv

# kamoku.csvを
# 読み込みモード「r」として
# 文字コード「shift-jis」として開く
f = open("kamoku.csv", "r", encoding="shift-jis")
read = csv.reader(f)

# csvファイルの情報を保存するリスト配列の作成
csv_list = []

# ループ処理しながら変数「s」にread変数に格納されたcsvファイルの要素を格納
for s in read:
    # 変数csv_listに変数「s」が所持する情報を格納
    csv_list.append(s)

# 変数「csv_list」に格納された要素, 1行目を表示
print(csv_list[1])