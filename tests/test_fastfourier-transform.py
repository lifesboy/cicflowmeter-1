import numpy as np
from scipy.fft import fft


arr = bytearray(0) + bytearray('12531526236236236', 'utf-8')

N = 100
y_arr = fft(arr)
res = 2.0/N * np.abs(y_arr[0:N//2])

print('y_arr=', y_arr)
print('res=', res)
