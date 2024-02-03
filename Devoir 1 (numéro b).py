from sympy import symbols, sin, pi, integrate

# Définir les symboles
t, A, omega = symbols('t A omega')

# Définir les valeurs des constantes
A_val = 0.100  # N
omega_val = pi / 3.00  # rad/s

# Définir l'expression de la force Fx
Fx = A * sin(omega * t)

# Intégrer Fx par rapport au temps pour obtenir l'expression de la vitesse (v = intégrale de F/m dt)
m = 0.100  # kg
v = integrate(Fx/m, t).subs({A: A_val, omega: omega_val})

# Intégrer v par rapport au temps pour obtenir l'expression de la position x (x = intégrale de v dt)
x = integrate(v, t)

# Calculer la position du véhicule à t = 6.00 s
x_val = x.subs(t, 6.00)

# Utiliser print pour afficher la réponse
print(x_val.evalf())

