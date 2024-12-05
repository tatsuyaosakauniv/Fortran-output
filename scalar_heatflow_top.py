import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
data = pd.read_csv('flow_check_top_1104.dat', delim_whitespace=True, header=None)

# 一列目と二列目をそれぞれx, yとして取得
x = data[0]
y = data[1]

# グラフの作成 (点のみ)
plt.figure(figsize=(8, 6))
plt.plot(x,y,linestyle='-')
plt.xlabel('Time  ns')
plt.ylabel('Heat flow  $\mathrm{W/m^2}$')

# x, y軸の範囲をデータの最小値と最大値に設定
plt.xlim(0, 5)
plt.ylim(-5e-6, 5e-6)

# グラフの表示
plt.show()
