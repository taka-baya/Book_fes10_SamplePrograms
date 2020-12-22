# パッケージpandasをプログラム内で呼び出し、pdという名前でパッケージを使う
import pandas as pd

# kamoku.csvを変数「df」読み込む
df = pd.read_csv('kamoku.csv', encoding="shift-jis")

# 変数「df」に読み込んだ結果を表示
print(df)

print("")

# 列名「かんな」の情報を取得
print(df['かんな'])