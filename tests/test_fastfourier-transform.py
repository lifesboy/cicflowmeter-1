from scipy.fft import fft


arr = [bytearray(100)]

y_arr = fft(arr)

print('y_arr=', y_arr[:10])
