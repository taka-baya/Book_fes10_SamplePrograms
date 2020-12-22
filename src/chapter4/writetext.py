import os

# 書き込みたい内容を変数「s」に格納
s = "書き込みたい内容！"

# openの中に書かれているファイルパスのファイルを書き込みとして開く
f = open("./textfile/textfile2.txt", "w") 

# ファイル「textfile2.txt」に書き込みたい内容(変数sの情報)を書き込み
f.write(s)
