import pandas as pd
import matplotlib.pyplot as plt

# データファイルの読み込み
data = pd.read_csv('heatflux_1205.dat', sep='\s+', header=None, low_memory=False)  # 空白区切りの場合

# 1列目を新しいx軸データで置き換える（数値型に変換）
x = pd.to_numeric(data[0], errors='coerce')

# y軸のデータ（2～5列目）
y1 = pd.to_numeric(data[1], errors='coerce')
y2 = pd.to_numeric(data[2], errors='coerce')
y3 = pd.to_numeric(data[3], errors='coerce')
y4 = pd.to_numeric(data[4], errors='coerce')

# グラフを作成
plt.figure(figsize=(6, 6))  # 正方形のサイズに設定
plt.plot(x, y2, label='Phantom Top', color='red')
plt.plot(x, y1, label='Phantom Bottom', color='blue')
plt.plot(x, y4, label='Interface Top', color='yellow')
plt.plot(x, y3, label='Interface Bottom', color='cyan')

# 軸の範囲を自動設定
plt.xlim([min(x), max(x)])
plt.xlim([0, 10])
plt.ylim([min(y1.min(), y2.min(), y3.min(), y4.min()), max(y1.max(), y2.max(), y3.max(), y4.max())])

# アスペクト比を正方形に設定
ax = plt.gca()
ax.set_aspect(abs((max(x) - min(x)) / (max(y1.max(), y2.max(), y3.max(), y4.max()) - min(y1.min(), y2.min(), y3.min(), y4.min()))), adjustable='box')

# ラベルとタイトルの設定
plt.xlabel('Time  $\mathrm{ns}$')
plt.ylabel('Heat  $\mathrm{J/m^2}$')
plt.legend()
plt.grid(False)

# グラフを表示
plt.show()
