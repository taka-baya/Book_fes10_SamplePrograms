import numpy as np

print("配列の範囲以外を参照して発生するエラー")

# パッケージnumpyを使って配列の作成
array_data = np.array([1, 2, 3, 4, 5])

print(f"変数array_dataのデータを表示：{array_data}")

# 変数array_dataの6番目の要素を表示
print(f"変数array_dataの範囲外のデータを表示：{array_data[6]}")