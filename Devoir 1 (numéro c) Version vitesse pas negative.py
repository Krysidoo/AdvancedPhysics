import numpy as np
import sympy as sp
from sympy.plotting import plot

# Définir les constantes et les symboles
A = 0.100  # N
omega = np.pi / 3  # rad/s
m = 0.100  # kg
t = sp.symbols('t')

# Définir l'expression de la force
Fx = A * sp.sin(omega * t)

# Calcul de l'accélération a_x = Fx/m
a_x = Fx / m

# Intégration de l'accélération pour obtenir la vitesse, avec la condition initiale v(0) = 0
vx = sp.integrate(a_x, t) + sp.symbols('C')

# Résolution pour C en utilisant la condition initiale
C_value = sp.solve(vx.subs(t, 0), sp.symbols('C'))[0]

# Mise à jour de vx avec la valeur correcte de C
vx_corrected = vx.subs(sp.symbols('C'), C_value)

# Tracer la vitesse vx en fonction du temps de 0 à 6 secondes
p = plot(vx_corrected, (t, 0, 6), title='Vitesse fonction du temps',
         xlabel='Temps (s)', ylabel='Vitesse (m/s)', show=True)