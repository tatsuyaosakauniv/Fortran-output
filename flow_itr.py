import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

# データの読み込み
data = pd.read_csv("flow_check_top_1122.dat", delim_whitespace=True, header=None)

# 初期設定
output = []

# 各ブロック（1行目、6行目、11行目、...、86行目）を処理
for start_offset in range(0, 180, 10):
    for current_row in range(start_offset, len(data) - 200, 200):
        tmp = data.iloc[current_row, 1]  # 開始行の2列目の値
        for i in range(200):
            value = tmp * data.iloc[current_row + i, 1] * 1e30
            output.append([(i + 1) * 0.05, value])

# 集計処理：Indexごとの平均値を計算
output_df = pd.DataFrame(output, columns=["Index", "Value"])
output_avg = output_df.groupby("Index", as_index=False)["Value"].mean()

# 結果をファイルに保存
output_avg.to_csv("scalar.dat", index=False, header=False, float_format="%.7E")

# ファイルを再読み込みして合計処理
data = pd.read_csv("scalar.dat", delim_whitespace=True, header=None, names=["Index", "Value"])
summed_data = data.groupby("Index", as_index=False)["Value"].sum()

# 合計結果をファイルに保存
summed_data.to_csv("summed_data.dat", index=False, header=False, sep=' ')

# グラフの描画
plt.figure(figsize=(6, 6))
plt.plot(summed_data["Index"], summed_data["Value"], linestyle='-')
plt.xlabel("Time  ps")
plt.ylabel(r"$\langle J(t) \cdot J(0) \rangle \quad \mathrm{W/m^2}$")
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.axhline(0, color='gray', linestyle='--')  # 点線
plt.grid(False)
plt.savefig("ensemble3.png")
plt.show()

# スカラー値の積分計算
data = np.loadtxt("scalar.dat")
result = np.sum((data[:-1, 1] + data[1:, 1]) * 0.5 * 1e-13) / 2
print(f"計算結果: {result}")
