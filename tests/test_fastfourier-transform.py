import numpy as np
from scipy.fft import fft


arr = bytearray(0) + bytearray('12531526236236236', 'utf-8')

N = 100
y_arr = fft(arr)
freq = 2.0/N * np.abs(y_arr[0:N//2])
res = np.pad(freq, (0, N//2 - len(freq)), 'constant')
print('y_arr=', y_arr)
print('res=', res)
