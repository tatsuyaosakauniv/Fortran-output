# 必要なライブラリをインポート
import numpy as np
import matplotlib.pyplot as plt

# x軸のデータを生成（0から10までの範囲で100個の値）
x = np.linspace(0, 10, 100)

# y = sin(x)の関数を使ったy軸のデータを生成
y = np.sin(x)

# グラフをプロット
plt.plot(x, y, label='y = sin(x)', color='blue', linestyle='-', marker='o')

# グラフのタイトルとラベルを追加
plt.title('Sine Wave Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 凡例の表示
plt.legend()

# グリッドを表示
plt.grid(True)

# グラフを表示
plt.show()
