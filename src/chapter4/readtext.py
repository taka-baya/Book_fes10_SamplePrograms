import os

# openの中に書かれているファイルパスのファイルを開く
f = open("./textfile/textfile1.txt", "r") 

# ファイル「textfile1.txt」から読み込んだ情報を変数「s」に格納
s = f.read()

# 読み込んだ情報を表示
print(s)