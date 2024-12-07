import numpy as np

# heatflux_1205.datのデータを読み込む
data_heatflux = np.loadtxt('heatflux_1207.dat')

# 1列目を横軸、各列を縦軸として回帰分析
# 切片をゼロに固定して傾きを計算
def calculate_slope(x, y):
    return np.sum(x * y) / np.sum(x ** 2)

x = data_heatflux[:, 0]
slope_phantom_top = calculate_slope(x, data_heatflux[:, 1]) * 10**9
slope_phantom_bottom = calculate_slope(x, data_heatflux[:, 2]) * 10**9
slope_interface_top = calculate_slope(x, data_heatflux[:, 3]) * 10**9
slope_interface_bottom = calculate_slope(x, data_heatflux[:, 4]) * 10**9

# tempe_Layer.datのデータを読み込む
data_tempe_layer = np.loadtxt('tempe_Layer_1207.dat')

# 2列目の差を計算
dT_bottom = data_tempe_layer[5, 1] - data_tempe_layer[4, 1]
dT_top = data_tempe_layer[20, 1] - data_tempe_layer[19, 1]

# 結果の計算
dT_top_over_slope_phantom_top = dT_top / slope_phantom_top
dT_bottom_over_slope_phantom_bottom = dT_bottom / slope_phantom_bottom
dT_top_over_slope_interface_top = dT_top / slope_interface_top
dT_bottom_over_slope_interface_bottom = dT_bottom / slope_interface_bottom

# 結果を出力
print("itr_phantom_top:", dT_top_over_slope_phantom_top)
print("itr_phantom_bottom:", dT_bottom_over_slope_phantom_bottom)
print("itr_interface_top:", dT_top_over_slope_interface_top)
print("itr_interface_bottom:", dT_bottom_over_slope_interface_bottom)