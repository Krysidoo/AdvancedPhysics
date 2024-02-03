import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, sin, pi

# Définir les symboles
t = symbols('t')

# Constantes données
A = 0.100  # N
omega = pi/3  # rad/s
m = 0.100  # kg

# Définir Fx
Fx = A * sin(omega * t)

# Intégrer Fx deux fois pour obtenir le déplacement x(t)
# D'abord intégrer pour obtenir la vitesse (v = intégrale(Fx/m dt))
v = integrate(Fx/m, t)

# Ensuite, intégrer la vitesse pour obtenir le déplacement (x = intégrale(v dt))
x = integrate(v, t)

# Définir un tableau de temps
time = np.linspace(0, 6, 100)

# Convertir l'expression sympy en fonction numpy
x_func = np.vectorize(lambda t_val: x.subs(t, t_val).evalf())

# Calculer le déplacement pour chaque valeur de temps
displacement = x_func(time)

# Tracé
plt.figure(figsize=(10, 6))
plt.plot(time, displacement, label='Déplacement (x)')
plt.title('Déplacement du véhicule au fil du temps')
plt.xlabel('Temps (s)')
plt.ylabel('Déplacement (m)')
plt.legend()
plt.grid(True)
plt.show()
