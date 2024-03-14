
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#Nora Lode, 07.03.24 - Løsningen av Varmelikningen med Euler eksplisitt i 2 romlige dimensjoner.

# Lengde x og t
L_x = 4
L_t = 0.1 

# Antall punkt i x og tid
N_x = 10
N_t = 40

# Steglengde
h = L_x / (N_x - 1)
k = L_t / (N_t - 1)

# Gitterpunkter
x = np.linspace(0, L_x, N_x)
t = np.linspace(0, L_t, N_t)

gamma = k / h**2

# En funksjon som representerer initialverdiene
def func(x):
    return np.cos(x)

# Setter initialverdi krav
matrise = np.zeros([N_x, N_t])
func_verdier = func(x)
matrise[:, 0] = func_verdier

# Løsning av varmeligningen med Euler-eksplisitt metode
def varmelikningen():
    A = (1 - 2*gamma) * np.eye(N_x-2) + gamma * np.eye(N_x-2, k=-1) + gamma * np.eye(N_x-2, k=1)

    for j in range(N_t - 1):
        matrise[1:-1, j+1] = A @ matrise[1:-1, j] # Matrisemultiplikasjon 
    return matrise

varmelikningen()

# Plotting av resultatene
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
meshX, meshT = np.meshgrid(x, t)
ax.plot_surface(meshX, meshT, np.flip(np.rot90(matrise), axis=0), cmap=cm.coolwarm)

ax.set_xlabel("Posisjon")
ax.set_ylabel("Tid")
ax.set_zlabel("Temperatur")
plt.title("Løsning av varmeligningen med Euler-eksplisitt metode")
plt.show()
