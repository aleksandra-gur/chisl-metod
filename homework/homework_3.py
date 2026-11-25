import numpy as np
from decimal import Decimal, getcontext

#block1 #task1
print("--- Задача 1 ---")
a = np.arange(60).reshape(3, 4, 5)
print("shape:", a.shape)
print("ndim:", a.ndim)
print("size:", a.size)
print("dtype:", a.dtype)
print("strides:", a.strides)
print("C_CONTIGUOUS:", a.flags['C_CONTIGUOUS'])
print("strides: шаг в байтах для перехода по индексам. size=60, так как 3*4*5.")

#block1 #task2
print("\n--- Задача 2 ---")
a = np.array([1, 2, 3, 4])
print("a/2:", a / 2, (a / 2).dtype)
print("a//2:", a // 2, (a // 2).dtype)
print("a/2.0:", a / 2.0, (a / 2.0).dtype)

b = np.array([1, 2, 3], dtype=np.int8)
print("b + 127:", b + 127, (b + 127).dtype)
print("a/2 не меняет a, создается новый массив. b+127 — переполнение int8 (127+1=-128), NumPy не падает, работает по модулю.")

#block1 #task3
print("\n--- Задача 3 ---")
getcontext().prec = 50
true_val = Decimal('0.1')

err32 = abs(Decimal(str(float(np.float32(0.1)))) - true_val)
err64 = abs(Decimal(str(float(np.float64(0.1)))) - true_val)
print("float32 ошибка:", f"{err32:.20e}")
print("float64 ошибка:", f"{err64:.20e}")

if err64 != 0:
    print("Отношение ошибок:", float(err32 / err64))
else:
    print("Ошибка float64 равна нулю, отношение не определено.")
print("float32 не подходит для задач с накоплением ошибки или высокой точностью.")

#block1 #task4
print("\n--- Задача 4 ---")
arrs = [
    np.zeros((2, 3), dtype=np.float64),
    np.zeros((2, 3), dtype=np.float32),
    np.ones((2, 3), dtype=np.int16),
    np.full((2, 3), 7, dtype=np.uint8)
]
for arr in arrs:
    print(f"dtype={arr.dtype}, nbytes={arr.nbytes}")
print("Экономия float32:", (1000*1000*8) - (1000*1000*4), "байт.")

#block2 #task5

print("\n--- Задача 5 ---")
a = np.arange(24)
cur = a
for shape in [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]:
    cur = cur.reshape(shape)
    print(f"shape={cur.shape}, equal={np.array_equal(a, cur.ravel())}")
print("reshape не копирует данные, если это возможно (меняются strides).")

#block2 #task6
print("\n--- Задача 6 ---")
M = np.arange(12).reshape(3, 4)
f = M.flatten()
r = M.ravel()
print("f.base is None:", f.base is None)
print("r.base is not None:", r.base is not None)
f[0] = 999
r[1] = 888
print("M:", M)
print("flatten — копия, ravel — view.")

#block2 #task7
print("\n--- Задача 7 ---")
v = np.arange(5)
print("v[:, None]:", v[:, None].shape)
print("v[None, :]:", v[None, :].shape)
print("squeeze:", np.squeeze(v[:, None]).shape)
T = np.arange(6).reshape(2, 3).T
print("T shape:", T.shape)

res = v[:, None] + v[None, :]
print("Сумма shape:", res.shape)
print(res)

#block2 #task8

print("\n--- Задача 8 ---")
A = np.arange(6).reshape(2, 3)
B = A.T
print("B.base is not None:", B.base is not None)
B[0, 1] = 999
print("A:", A)
print(".T — view, меняются только strides.")

#block3 #task9
print("\n--- Задача 9 ---")
A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)
print("A @ B shape:", (A @ B).shape)
print("A.T @ B.T shape:", (A.T @ B.T).shape)
print("A * A shape:", (A * A).shape)
print("* — поэлементное, @ — матричное. A * B даст ошибку из-за форм.")
D = np.diag([1, 2, 3])
print("D @ D == D * D:", np.array_equal(D @ D, D * D))

#block3 #task10

print("\n--- Задача 10 ---")
M = np.arange(12).reshape(3, 4)
print("sum(axis=0):", M.sum(axis=0))
print("sum(axis=1):", M.sum(axis=1))
print("argmax(axis=0):", M.argmax(axis=0))
print("argmax(axis=1):", M.argmax(axis=1))
print("axis=0 — по столбцам, axis=1 — по строкам.")

#block3 #task11
print("\n--- Задача 11 ---")
X = np.random.default_rng(42).normal(size=(5, 3))
m1 = X.mean(axis=0)
m2 = X.mean(axis=0, keepdims=True)
print("m1:", m1.shape, "m2:", m2.shape)
print("X - m1:", (X - m1).shape, "X - m2:", (X - m2).shape)

X_norm = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
print("mean(axis=1):", X_norm.mean(axis=1))
print("std(axis=1):", X_norm.std(axis=1))
print("keepdims сохраняет размерность для broadcasting.")

#block4 #task12

print("\n--- Задача 12 ---")
a = np.arange(10)
b = a[2:5]
b[0] = 999
print("a после b:", a)

c = a[2:5].copy()
c[0] = -1
print("a после c:", a)
print("Срез — view, copy — копия.")

#block4 #task13
print("\n--- Задача 13 ---")
a = np.random.default_rng(0).normal(size=20)
print("a[a>0]:", a[a > 0].size)
print("a[(a>-1)&(a<1)]:", a[(a > -1) & (a < 1)].size)
print("a[[0,5,10,15]]:", a[[0, 5, 10, 15]])
print("Выбросы:", a[np.abs(a) > 2])

a[a < 0] = 0
print("После зануления:", a)
print("a[a>0] & (a<1) — ошибка, нужны скобки из-за приоритета операций.")

#block4 #task14
print("\n--- Задача 14 ---")
X = np.random.default_rng(1).normal(size=(100, 3))
X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
print("mean:", X_norm.mean(axis=0))
print("std:", X_norm.std(axis=0))

D = np.sqrt(((X_norm[:, None, :] - X_norm[None, :, :]) ** 2).sum(axis=-1))
print("D shape:", D.shape, "diag:", np.diag(D)[:3], "sym:", np.allclose(D, D.T))

#block4 #task15
print("\n--- Задача 15 ---")
rng = np.random.default_rng(42)
raw = rng.normal(20, 2, size=(30, 4))
raw[7, 2] = 100

print("shape:", raw.shape, "dtype:", raw.dtype, "size:", raw.size)
mask = np.abs(raw - raw.mean(axis=0)) > 3 * raw.std(axis=0)
print("Выбросов:", mask.sum())

raw_nan = np.where(mask, np.nan, raw)
col_mean = np.nanmean(raw_nan, axis=0)
raw_clean = np.where(mask, col_mean, raw)
print("Заменен:", raw_clean[7, 2])

T = raw_clean.T
print("T.T equal:", np.array_equal(T.T, raw_clean))

flat = raw_clean.ravel()
print("flat restore equal:", np.array_equal(flat.reshape(30, 4), raw_clean))
print("Mean:", raw_clean.mean(axis=0))
print("Std:", raw_clean.std(axis=0))

norm = (raw_clean - raw_clean.mean(axis=0)) / raw_clean.std(axis=0)
print("norm mean:", norm.mean(axis=0))
print("norm std:", norm.std(axis=0))
print("copy: flatten. broadcasting: маска, нормировка. Ошибка формы: неверный axis.")

#block4 #task16
print("\n--- Задача 16 ---")
print("Ссылка: https://stackoverflow.com/questions/3890621/how-does-multiplication-differ-for-numpy-matrix-vs-array")
print("Ошибка: * вместо @. Исправление: заменить * на @.")