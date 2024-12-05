import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# データファイルの読み込み
data = pd.read_csv('heatflux_1122.dat', sep=r'\s+', header=None, low_memory=False)

# 一列目のデータを数値型に変換
x = pd.to_numeric(data[0], errors='coerce')

# y軸のデータ（2～5列目）
y1 = pd.to_numeric(data[1], errors='coerce')
y2 = pd.to_numeric(data[2], errors='coerce')
y3 = pd.to_numeric(data[3], errors='coerce')
y4 = pd.to_numeric(data[4], errors='coerce')

# 外れ値を除去する関数
def remove_outliers(x, y, threshold=1.5):
    median = np.median(y)
    std_dev = np.std(y)
    mask = (y > median - threshold * std_dev) & (y < median + threshold * std_dev)
    return x[mask], y[mask]

# y1とy2の外れ値を除去
x_filtered, y1_filtered = remove_outliers(x, y1)
x_filtered_y2, y2_filtered = remove_outliers(x, y2)

# y1とy2に対して近似直線を計算
slope_y1, intercept_y1 = np.polyfit(x_filtered, y1_filtered, 1)
slope_y2, intercept_y2 = np.polyfit(x_filtered_y2, y2_filtered, 1)

# 傾きと切片を表示
print(f"傾き top: {slope_y1}")
print(f"切片 top: {intercept_y1}")
print(f"傾き bottom: {slope_y2}")
print(f"切片 bottom: {intercept_y2}")

# グラフを作成
plt.figure(figsize=(6, 6))  # 正方形のサイズに設定
plt.plot(x, y2, label='Phantom Top', color='red')
plt.plot(x, y1, label='Phantom Bottom', color='blue')
plt.plot(x_filtered_y2, slope_y2 * np.array(x_filtered_y2) + intercept_y2, label='Linear Fit Top', color='orange', linestyle='--')
plt.plot(x_filtered, slope_y1 * np.array(x_filtered) + intercept_y1, label='Linear Fit Bottom', color='cyan', linestyle='--')

# テキストを右端より少し左に表示
text_x = 0.78 * max(x)  # x座標を右端より少し左寄りに固定
text_y_center = (y1.max() + y2.min()) / 2  # y1とy2の値の間の中央位置に設定

# 傾きと切片をグラフ上に表示（y1）
plt.text(text_x, text_y_center + 0.1 * (y1.max() - y1.min()), 
         f'Slope Bottom: {slope_y1:.2e}\nIntercept Bottom: {intercept_y1:.2e}', 
         color='cyan', fontsize=10, ha='center', va='center')

# 傾きと切片をグラフ上に表示（y2）
plt.text(text_x, text_y_center - 0.1 * (y1.max() - y1.min()), 
         f'Slope Top: {slope_y2:.2e}\nIntercept Top: {intercept_y2:.2e}', 
         color='orange', fontsize=10, ha='center', va='center')

# 軸の範囲を自動設定
plt.xlim([0, 10])
plt.ylim([min(y1.min(), y2.min()), max(y1.max(), y2.max())])

# アスペクト比を正方形に設定
ax = plt.gca()
ax.set_aspect(abs((max(x) - min(x)) / (max(y1.max(), y2.max()) - min(y1.min(), y2.min()))), adjustable='box')

# ラベルとタイトルの設定
plt.xlabel(r'Time  $\mathrm{ns}$')
plt.ylabel(r'Heat  $\mathrm{J/m^2}$')
plt.legend()
plt.grid(False)

# グラフを表示
plt.show()
