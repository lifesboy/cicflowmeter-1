import numpy as np
from scipy.fft import fft


def get_payloads() -> bytearray:
    return bytearray(0)# + bytearray('12531526236236236', 'utf-8')


payloads = get_payloads()

N = 100
y_arr = fft(payloads if len(payloads) > 0 else bytearray(1))
freq = 2.0/N * np.abs(y_arr[0:N//2])
res = np.pad(freq, (0, N//2 - len(freq)), 'constant')
print('payloads=', len(payloads))
print('y_arr=', y_arr)
print('res=', res)
