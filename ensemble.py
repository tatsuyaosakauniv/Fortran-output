import matplotlib.pyplot as plt
import pandas as pd

# データを読み込む
data = pd.read_csv('ACF_top_1128.dat', delim_whitespace=True, header=None)

# x, yにそれぞれの列を代入
x = data[0]  # 1列目
y = data[1]  # 2列目

# グラフを作成
plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Column 2", linestyle='-', markersize=3)

# x軸とy軸の範囲をデータの最小値と最大値に設定
plt.xlim([x.min(), x.max()])
plt.ylim([y.min(), y.max()])  # データに応じた動的な範囲

# ラベルやタイトル、凡例を設定
plt.xlabel("Column 1 (X-axis)")
plt.ylabel("Column 2 (Y-axis)")

plt.axhline(0, color='gray', linestyle='--')

plt.legend()

# グラフを表示
plt.show()