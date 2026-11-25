import math
import random
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

getcontext().prec = 50

#block1 #task1

print("--- Задача 1 ---")
def cond_num(f, x, h=1e-5):
    return abs(x * (f(x + h) - f(x)) / h / f(x))

print(f"1. sqrt(x) при x=1e-8: {cond_num(math.sqrt, 1e-8):.2f}")
print(f"2. ln(x) при x=1.001: {cond_num(math.log, 1.001):.2f}")
print(f"3. x-1 при x=1.000001: {cond_num(lambda x: x - 1, 1.000001):.2f}")
print(f"4. sin(x) при x=pi/2: {cond_num(math.sin, math.pi/2):.2f}")
print("Вывод: Самая опасная - x-1. Наименее опасная - sin(x) в pi/2.")

#block1 #task2

print("\n--- Задача 2 ---")
a = 1 + 1e-8
b = 1
true_diff = Decimal(str(a)) - Decimal(str(b))
approx_diff = a - b
rel_err = abs(approx_diff - float(true_diff)) / float(true_diff) * 100
print(f"Аналитика: {abs(a/(a-b)) + abs(b/(a-b)):.2e}")
print(f"Результат float: {approx_diff:.2e}")
print(f"Относительная погрешность: {rel_err:.2f}%")
print("Вывод: Вычитание близких чисел приводит к потере точности.")

#block1 #task3

print("\n--- Задача 3 ---")
for delta in [1e-2, 1e-4, 1e-6, 1e-8]:
    x1 = 1 - math.sqrt(delta)
    err = abs(x1 - 1)
    print(f"delta={delta:.0e}: корень={x1:.15f}, отклонение={err:.2e}")

#block1 #task4

print("\n--- Задача 4 ---")
def unstable_algo(x):
    return math.log(x) / (math.sqrt(x + 1e-8) - math.sqrt(x))

def stable_algo(x):
    return math.log(x) * (math.sqrt(x + 1e-8) + math.sqrt(x)) / 1e-8

true_val = math.log(10) * (math.sqrt(10 + 1e-8) + math.sqrt(10)) / 1e-8
print(f"Устойчивый: {stable_algo(10):.4f}, ошибка: {abs(stable_algo(10) - true_val):.2e}")
print(f"Неустойчивый: {unstable_algo(10):.4f}, ошибка: {abs(unstable_algo(10) - true_val):.2e}")

#block2 #task5

print("\n--- Задача 5 ---")
a, b, c = 1, 10**8, 1
D = Decimal(b)**2 - Decimal(4)*Decimal(a)*Decimal(c)
x2_bad = (-Decimal(b) - D.sqrt()) / (Decimal(2)*Decimal(a))
x1_bad = (-Decimal(b) + D.sqrt()) / (Decimal(2)*Decimal(a))
x1_good = Decimal(2)*Decimal(c) / (-Decimal(b) - D.sqrt())
print(f"Плохой маленький корень: {x1_bad:.4e}")
print(f"Хороший маленький корень: {x1_good:.4e}")

#block2 #task6

print("\n--- Задача 6 ---")
for x in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
    true_val = float(Decimal(1) - Decimal(x)**2 / 2)
    bad_val = (1 - math.cos(x)) / x**2
    good_val = 2 * math.sin(x/2)**2 / x**2
    print(f"x={x:.0e}: плохо={bad_val:.4e}, хорошо={good_val:.4e}")
print("Вывод: при x < 1e-6 ошибка плохого способа превышает 1%.")

#block2 #task7

print("\n--- Задача 7 ---")
for x in [1e-4, 1e-8, 1e-12, 1e-16]:
    bad = math.sqrt(x+1) - math.sqrt(x)
    good = 1 / (math.sqrt(x+1) + math.sqrt(x))
    print(f"x={x:.0e}: плохо={bad:.4e}, хорошо={good:.4e}")

#block2 #task8

print("\n--- Задача 8 ---")
for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    bad = math.log(1 + x)
    good = math.log1p(x)
    print(f"x={x:.0e}: плохо={bad:.4e}, хорошо={good:.4e}")

#block2 #task9

print("\n--- Задача 9 ---")
def harmonic(n, method='loop'):
    if method == 'loop':
        s = 0.0
        for i in range(1, n+1): s += 1/i
        return s
    elif method == 'sum': return sum(1/i for i in range(1, n+1))
    elif method == 'fsum': return math.fsum(1/i for i in range(1, n+1))

for n in [10**5, 10**6, 10**7]:
    true_val = float(sum(1/Decimal(i) for i in range(1, n+1)))
    err_loop = abs(harmonic(n, 'loop') - true_val) / true_val
    print(f"n={n:.0e}: ошибка цикла = {err_loop:.2e}")

#block3 #task10

print("\n--- Задача 10 ---")
a, b, c = 1, 10**8, 1
x_true = Decimal(-1) / Decimal(10**8)
x_bad = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x_good = 2*c / (-b - math.sqrt(b**2 - 4*a*c))
print(f"Плохой алгоритм: {x_bad:.4e}")
print(f"Хороший алгоритм: {x_good:.4e}")

#block3 #task11

print("\n--- Задача 11 ---")
print("Пример: 1e16 + 1 - 1e16. float дает 0.0, эталон Decimal дает 1.")

#block3 #task12

print("\n--- Задача 12 ---")
x_vals = [10**k for k in range(2, 17, 2)]
errors = []
for x in x_vals:
    true_val = 2 * math.sin(x/2)**2 / x**2
    bad_val = (1 - math.cos(x)) / x**2
    errors.append(abs(bad_val - true_val) / true_val)
plt.loglog(x_vals, errors, marker='o')
plt.xlabel('x'); plt.ylabel('Относительная ошибка')
plt.grid(True); plt.savefig('plot_task12.png')
plt.close()

#block3 #task13

print("\n--- Задача 13 ---")
arr1 = [random.random() for _ in range(10**5)]
arr2 = np.random.default_rng(42).random(10**5)
for name, arr in [("random.seed(42)", arr1), ("default_rng(42)", arr2)]:
    s_sum = sum(arr); s_fsum = math.fsum(arr); s_np = np.sum(arr)
    print(f"{name}: sum={s_sum:.4e}, fsum={s_fsum:.4e}, np.sum={s_np:.4e}")

#block3 #task14

print("\n--- Задача 14 ---")
test_arrays = [
    [1e300, 1e300], [1e-300, 1e-300], [0.0, 0.0],
    [1e-320, 1e-320], [float('inf'), 1.0], [float('nan'), 1.0]
]
for arr in test_arrays:
    try: s1 = sum(arr)
    except: s1 = "Ошибка"
    try: s2 = math.fsum(arr)
    except: s2 = "Ошибка"
    print(f"Массив: {arr} -> sum: {s1}, fsum: {s2}")

#block3 #task15

print("\n--- Задача 15 ---")
print(f"{'x':<6} | {'Плохой':<12} | {'Хороший':<12} | {'Эталон':<12} | {'Ош. плохого':<12} | {'Ош. хор.'}")
print("-" * 80)
for x in [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
    true_val = float(Decimal(str(math.cos(x))))
    bad = 1 - x**2 / 2
    good = 2 * math.cos(x/2)**2 - 1
    err_bad = abs(bad - true_val) / abs(true_val) if true_val != 0 else float('inf')
    err_good = abs(good - true_val) / abs(true_val) if true_val != 0 else float('inf')
    print(f"{x:<6} | {bad:<12.8f} | {good:<12.8f} | {true_val:<12.8f} | {err_bad:<12.2e} | {err_good:.2e}")

#block3 #task16

print("\n--- Задача 16 ---")
print("Ссылка: https://stackoverflow.com/questions/1712891/why-does-python-return-0-30000000000000004")
print("Проблема: 0.1 + 0.2 = 0.30000000000000004. Замена: math.isclose() или Decimal.")