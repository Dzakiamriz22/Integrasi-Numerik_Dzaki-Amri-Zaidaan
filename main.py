import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi trapezoid
def trapezoid_integral(f, a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:N]) + y[N])
    return integral

# Menghitung galat RMS
def rms_error(estimated_pi, reference_pi):
    return np.sqrt(np.mean((estimated_pi - reference_pi)**2))

# Referensi nilai pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Testing
for N in N_values:
    start_time = time.time()
    estimated_pi = trapezoid_integral(f, 0, 1, N)
    execution_time = time.time() - start_time
    error = rms_error(estimated_pi, pi_ref)
    
    print(f"N = {N}")
    print(f"Estimated Pi: {estimated_pi}")
    print(f"RMS Error: {error}")
    print(f"Execution Time: {execution_time} seconds")
    print("-" * 30)
