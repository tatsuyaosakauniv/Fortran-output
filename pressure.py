import pandas as pd

# データを読み込む (例として'datafile.csv'を使用しています)
# 空白やカンマで区切られている場合は適宜変更してください。
df = pd.read_csv('pressure.dat', delim_whitespace=True, header=None)

# 2列目と3列目の平均をそれぞれ計算
col2_mean = df[1].mean()  # 2列目 (0ベースで1番目の列)
col4_mean = df[3].mean()  # 3列目 (0ベースで2番目の列)

# 結果を出力
print("2列目の平均:", col2_mean)
print("4列目の平均:", col4_mean)
