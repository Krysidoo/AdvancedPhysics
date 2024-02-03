import numpy as np
import sympy as sp

# Définition des symboles pour sympy
t = sp.symbols('t')
A = 0.100  # N
omega = sp.pi/3  # rad/s
m = 0.100  # kg

# Calcul de l'accélération
ax = (A / m) * sp.sin(omega * t)

# Intégration définie de l'accélération pour obtenir la vitesse
v_x = sp.integrate(ax, (t, 0, t))

# Intégration définie de la vitesse pour obtenir la position
x_t = sp.integrate(v_x, (t, 0, t))

# Simplification de l'expression de la position
x_t_simplified = x_t.simplify()

print(f"L'expression simplifiée de x(t) est : {x_t_simplified}")