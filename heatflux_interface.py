import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# データファイルの読み込み
data = pd.read_csv('heatflux_1207.dat', sep='\s+', header=None, low_memory=False)

x = data[0]

# y軸のデータ（2～5列目）
y1 = pd.to_numeric(data[1], errors='coerce')
y2 = pd.to_numeric(data[2], errors='coerce')
y3 = pd.to_numeric(data[3], errors='coerce')
y4 = pd.to_numeric(data[4], errors='coerce')

# 外れ値を除去する関数
def remove_outliers(y, threshold=1.5):
    median = np.median(y)
    std_dev = np.std(y)
    return y[(y > median - threshold * std_dev) & (y < median + threshold * std_dev)]

# y3とy4の外れ値を除去
y3_filtered = remove_outliers(y3)
x_filtered = x[y3.notnull() & (np.abs(y3 - np.median(y3)) < 1.5 * np.std(y3))]

y4_filtered = remove_outliers(y4)
x_filtered_y4 = x[y4.notnull() & (np.abs(y4 - np.median(y4)) < 1.5 * np.std(y4))]

# y3とy4に対して近似直線を計算
slope_y3, intercept_y3 = np.polyfit(x_filtered, y3_filtered, 1)
slope_y4, intercept_y4 = np.polyfit(x_filtered_y4, y4_filtered, 1)

# 傾きと切片を表示
print(f"傾き top: {slope_y3}")
print(f"切片 top: {intercept_y3}")
print(f"傾き bottom: {slope_y4}")
print(f"切片 bottom: {intercept_y4}")

# グラフを作成
plt.figure(figsize=(6, 6))  # 正方形のサイズに設定
plt.plot(x, y4, label='Interface Top', color='red')
plt.plot(x, y3, label='Interface Bottom', color='blue')
plt.plot(x, slope_y4 * np.array(x) + intercept_y4, label='Linear Fit Top', color='orange', linestyle='--')
plt.plot(x, slope_y3 * np.array(x) + intercept_y3, label='Linear Fit Bottom', color='cyan', linestyle='--')

# テキストを右端より少し左に表示
text_x = 0.78 * max(x)  # x座標を右端より少し左寄りに固定
text_y_center = (y3.max() + y4.min()) / 2  # y3とy4の値の間の中央位置に設定

# 傾きと切片をグラフ上に表示（y3）
plt.text(text_x, text_y_center + 0.1 * (y3.max() - y3.min()), 
         f'Slope Bottom: {slope_y3:.2e}\nIntercept Bottom: {intercept_y3:.2e}', 
         color='cyan', fontsize=10, ha='center', va='center')

# 傾きと切片をグラフ上に表示（y4）
plt.text(text_x, text_y_center - 0.1 * (y3.max() - y3.min()), 
         f'Slope Top: {slope_y4:.2e}\nIntercept Top: {intercept_y4:.2e}', 
         color='orange', fontsize=10, ha='center', va='center')

# 軸の範囲を自動設定
plt.xlim([0,10])
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
