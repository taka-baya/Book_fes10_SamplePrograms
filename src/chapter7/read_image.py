import cv2

# 画像の読み込みのファイルパス
filename = "./inputs/testimage1.png"

# 変数「img」に読み込んだ画像を保存
img = cv2.imread(filename, 1)

# 読み込んだ画像を表示
cv2.imshow('image',img)

# キーボード入力されるまで画像を表示
# キーボード入力(Enterなど)押されたら画像を閉じてプログラム終了
cv2.waitKey(0)