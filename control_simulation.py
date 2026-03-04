import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
K = 1
tau = 5
dt = 0.1
tiempo = 50

# Inicialización
t = np.arange(0, tiempo, dt)
y = np.zeros(len(t))
u = np.ones(len(t))  # Entrada escalón

# Simulación sistema sin control
for i in range(len(t)-1):
    y[i+1] = y[i] + (dt/tau) * (-y[i] + K*u[i])

plt.figure()
plt.plot(t, y)
plt.title("Sistema de Primer Orden - Respuesta al Escalón")
plt.xlabel("Tiempo")
plt.ylabel("Salida")
plt.grid()
plt.show()
