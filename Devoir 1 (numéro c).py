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

# Intégrer Fx/m pour obtenir l'expression de la vitesse vx
vx = sp.integrate(Fx/m, t)

# Tracer la vitesse vx en fonction du temps de 0 à 6 secondes
p = plot(vx, (t, 0, 6), title='La vitesse Vx en fonction du temps',
         xlabel='Temps (s)', ylabel='Vitesse (m/s)', show=True)
