import math
import numpy as np
from decimal import Decimal, getcontext

#block1 #task1

pairs = [(3.14, math.pi), (2.718, math.e), (9.8, 9.81), (0.333, 1/3)]
for x, x_star in pairs:
    delta = abs(x - x_star)
    rel = (delta / abs(x_star)) * 100
    print(f"x={x}: абс={delta:.4f}, отн={rel:.4f}%")

#block1 #task2

m_abs, m_val = 2, 1247
b_abs, b_val = 0.2, 9.7
print(f"Мост: отн={m_abs/m_val*100:.4f}%")
print(f"Болт: отн={b_abs/b_val*100:.4f}%")

#block1 #task3

def relative_error(approx, exact):
    if exact == 0:
        return float('inf')
    return abs(approx - exact) / abs(exact)
for x, x_star in pairs:
    print(f"x={x}: {relative_error(x, x_star):.6f}")

#block1 #task4

d_max = 47.3 * 0.001
print(f"[{47.3 - d_max:.3f}, {47.3 + d_max:.3f}]")

#block2 #task5

err_A = 0.3
err_B = 25 * 0.005
print(f"Абс. погрешность А: {err_A}, Б: {err_B}")

#block2 #task6

def count_sig_figs(num_str):
    s = num_str.replace('.', '').lstrip('0')
    return len(s) if s else 0

nums = ["0.004520", "1200", "1200", "10.03", "0.03050", "250000"]
for n in nums:
    sig = count_sig_figs(n)
    print(f"{n}: {sig} зн. цифр, эксп. форма: {float(n):.4e}")

#block2 #task7

print("4.74 ± 0.02, 3 значащие цифры")

#block2 #task8

print(round(0.5), round(1.5), round(2.5), round(3.5), round(-0.5), round(-1.5))

#block3 #task9

N = 100000
sum_a = sum([1/k for k in range(1, N+1)])
sum_b = sum([1/k for k in range(N, 0, -1)])
sum_std = math.fsum([1/k for k in range(1, N+1)])
print(f"а: {abs(sum_a - sum_std):.2e}, б: {abs(sum_b - sum_std):.2e}")

#block3 #task10

a = 0.1 + 0.2
print(a, a == 0.3, math.isclose(a, 0.3), a - 0.3)

#block3 #task11

a, b = 1 + 1e-15, 1
print(f"a - b = {a - b}")
a_q, b_q, c_q = 1, 1e5, 1
D = b_q**2 - 4*a_q*c_q
x1 = (-b_q + math.sqrt(D)) / (2*a_q)
x1_improved = c_q / x1 if x1 != 0 else 0
print(f"x1 = {x1}")
print(f"Улучшенный x1 = {x1_improved}")

#block3 #task12

arr = [0.1] * 1_000_000
s_loop = 0.0
for v in arr: s_loop += v
print(f"Цикл: {abs(s_loop - 1e5):.2e}, sum: {abs(sum(arr) - 1e5):.2e}, fsum: {abs(math.fsum(arr) - 1e5):.2e}")

#block3 #task13

arr2 = [1e-10, 1e6, 1e-10, 1e6, 1e-10, 1e6, 1e-10]
sa = sum(sorted(arr2, key=abs))
sb = sum(sorted(arr2, key=abs, reverse=True))
print(f"а: {sa}, б: {sb}, fsum: {math.fsum(arr2)}")

#block3 #task14

x = 1.0
for _ in range(10000): x *= 1.0001
true_exp = math.exp(10000 * math.log(1.0001))
print(f"Отн. погрешность: {abs(x - true_exp) / true_exp:.2e}")

#block3 #task15

getcontext().prec = 28
f_sum = 0.0
for _ in range(10000): f_sum += 0.01
d_sum = Decimal('0.0')
for _ in range(10000): d_sum += Decimal('0.01')
print(f"Float: {f_sum}, Decimal: {d_sum}, Расхождение: {abs(float(d_sum) - f_sum):.4e}")

#block4 #task16

np.random.seed(42)
arr_rand = np.random.rand(10**6)
s_loop = 0.0
for val in arr_rand: s_loop += val
s_sum = sum(arr_rand)
s_np = np.mean(arr_rand) * len(arr_rand)
s_fsum = math.fsum(arr_rand)
s_npsum = np.sum(arr_rand)
print(f"Цикл: {s_loop}, sum: {s_sum}, np.mean*len: {s_np}, fsum: {s_fsum}, np.sum: {s_npsum}")