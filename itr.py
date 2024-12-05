import numpy as np

data = np.loadtxt('ACF_top_1128.dat')

integration = 0
area = 39.2*39.2*10**-20
boltz = 1.3806662*10**(-23)
temp = 100

num_rows = len(data)

for i in range(num_rows - 1):
    integration += (data[i,1] + data[i+1,1]) * 0.05 * 10**(-12) / 2

result = boltz*temp**2/area/integration
print(f"計算結果: {result}")