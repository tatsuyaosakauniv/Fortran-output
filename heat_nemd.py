import matplotlib.pyplot as plt
import numpy as np

# データの読み込み
data = np.loadtxt('heatflux_1022.dat')

# x軸とy軸のデータ
x = data[:, 0]
y2 = data[:, 1]
y3 = data[:, 2]
y4 = data[:, 3]
y5 = data[:, 4]

# グラフの作成
plt.figure(figsize=(6, 6))  # 正方形のグラフ

plt.plot(x, y2, label='Column 2')
plt.plot(x, y3, label='Column 3')
plt.plot(x, y4, label='Column 4')
plt.plot(x, y5, label='Column 5')

# ラベルと凡例の追加
plt.xlabel('X Axis (Column 1)')
plt.ylabel('Y Axis (Columns 2-5)')
plt.legend()

# グラフの表示
plt.show()
