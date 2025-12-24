import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integration_sum = f(a) + f(b)
    
    for i in range(1, n):
        k = a + i * h
        integration_sum += 2 * f(k)
        
    integration_sum = integration_sum * h / 2
    return integration_sum

# --- Simulasi Kasus Pengereman ---
# Fungsi Kecepatan: v(t) = v0 * exp(-kt)
# v0 = Kecepatan awal (m/s), k = konstanta pengereman
def velocity_profile(t):
    v0 = 30.0  # 30 m/s (sekitar 108 km/jam)
    k = 0.5    # Konstanta pengereman
    return v0 * np.exp(-k * t)

# Parameter Integrasi
a = 0.0      # Waktu mulai (detik)
b = 10.0     # Waktu berhenti (detik)
n = 100      # Jumlah segmen (grid)

# 1. Hitung Jarak (Integrasi Numerik)
distance_numeric = trapezoidal_rule(velocity_profile, a, b, n)

# 2. Hitung Solusi Eksak (Analitik) untuk perbandingan Error
# Integral dari v0*e^(-kt) adalah (-v0/k)*e^(-kt)
exact_val = (-30.0/0.5 * np.exp(-0.5 * 10.0)) - (-30.0/0.5 * np.exp(-0.5 * 0.0))

# 3. Output Hasil
print(f"--- Hasil Simulasi Pengereman ---")
print(f"Kecepatan Awal: 30 m/s")
print(f"Waktu Pengereman: {b} detik")
print(f"Jarak Tempuh (Numerik): {distance_numeric:.4f} meter")
print(f"Jarak Tempuh (Eksak)  : {exact_val:.4f} meter")
print(f"Galat Relatif (Error) : {abs((exact_val - distance_numeric)/exact_val)*100:.6f} %")

# 4. Visualisasi 
t_x = np.linspace(a, b, n+1)
t_y = velocity_profile(t_x)

plt.fill_between(t_x, t_y, alpha=0.4, label='Jarak Tempuh (Area)')
plt.plot(t_x, t_y, 'r', label='Profil Kecepatan v(t)')
plt.title('Estimasi Jarak Pengereman dg Aturan Trapesium')
plt.xlabel('Waktu (detik)')
plt.ylabel('Kecepatan (m/s)')
plt.legend()
plt.grid(True)
plt.savefig('grafik_pengereman.png')
plt.show()
