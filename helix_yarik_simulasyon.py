import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# PARAMETRELER
# -----------------------
N_theta = 2000                  # Heliks için açı adımı
theta = np.linspace(0, 2*np.pi, N_theta)
r = 1.0                         # Heliks yarıçapı
d = 0.8                         # Yarıktan geçiş genişliği
m = 1                           # Topolojik sayı (heliks)
k = 12                          # Dalga sayısı
alpha = 0.8                     # EM saptırma katsayısı (max)
beta = 10                        # Saptırmanın keskinliği

# -----------------------
# YARIK + EM ETKİSİ
# -----------------------
T = (np.abs(np.cos(theta)) < d/(2*r)).astype(float)   # Yarıktan geçiş
f_EM = 1 - alpha*np.exp(-beta*(np.cos(theta)/(d/2))**2)  # EM alan etkisi

# Toplam geçiş fonksiyonu
T_total = T * f_EM

# -----------------------
# EKRAN DÜZLEMİ
# -----------------------
grid_size = 300
x = np.linspace(-3, 3, grid_size)
y = np.linspace(-3, 3, grid_size)
X, Y = np.meshgrid(x, y)
Psi = np.zeros_like(X, dtype=complex)

# -----------------------
# TOPLAM KATKI
# -----------------------
for th, t in zip(theta, T_total):
    if t > 0:
        Psi += np.exp(1j*m*th) * np.exp(1j*k*(X*np.cos(th) + Y*np.sin(th)))

# -----------------------
# YOĞUNLUK
# -----------------------
I = np.abs(Psi)**2
I /= I.max()  # Normalize

# -----------------------
# GRAFİK
# -----------------------
plt.figure(figsize=(6,6))
plt.imshow(I, extent=[-3,3,-3,3], origin='lower', cmap='inferno')
plt.colorbar(label="Yoğunluk")
plt.title(f"Heliks + Yarıktan Geçiş + EM Alan (m={m}, d={d})")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()