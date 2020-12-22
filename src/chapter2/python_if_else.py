import os

# 変数switchに真偽値のTrueとFalseの情報を格納
# True : カレールーがあるのでカレーを作る。
# False: カレールーが無いので肉じゃがを作る
switch = True # ここの部分を手動で変更

print(f"変数switchの真偽値を表示：{switch}")

if switch == True:
    print("カレーを作る")
else:
    print("肉じゃがを作る")