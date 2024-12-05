import pandas as pd

# ファイルの読み込み
data = pd.read_csv("tempe_Layer_0.10_1107.dat", delim_whitespace=True, header=None)

# 2列目のデータを1000倍して12.1で割る
data[1] = (data[1] * 1000) / 12.1

# 指定のフォーマットに変換して保存
formatted_data = data.copy()
formatted_data[0] = formatted_data[0].apply(lambda x: f"{x:.7E}")  # 1列目も指定フォーマットに変換
formatted_data[1] = formatted_data[1].apply(lambda x: f"{x:.7E}")  # 2列目も指定フォーマットに変換

# 新しいファイルに書き出し
formatted_data.to_csv("tempe_Layer_0.10.dat", sep=" ", header=False, index=False)
