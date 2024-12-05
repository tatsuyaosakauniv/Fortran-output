import numpy as np
import matplotlib.pyplot as plt

# データの読み込み
data = np.loadtxt('tempe_Layer_1125.dat')

# x軸とy軸のデータ
x = data[:, 0]
y = data[:, 1]

# y軸の範囲を設定
y_min, y_max = 85, 115

# x軸の範囲を設定
x_min, x_max = 0, 87.2

# 正方形のプロット（点のみ）
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='blue')  # 点をプロット
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('z Length nm')
plt.ylabel('Temperature K')

# x軸の範囲とy軸の範囲を同じ比率に設定
plt.gca().set_aspect((x_max - x_min) / (y_max - y_min), adjustable='box')

plt.show()
