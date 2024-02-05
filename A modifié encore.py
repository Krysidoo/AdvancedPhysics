import sympy as sp

# Définition des symboles pour sympy

t = sp.symbols('t', positive=True)
A = sp.symbols('A',  positive=True)
m = sp.symbols('m',  positive=True)
omega = sp.symbols('omega',  positive=True)
# Calcul de l'accélération
ax = A * t * sp.sin(omega * t) / m

# Intégration définie de l'accélération pour obtenir la vitesse
v_x = sp.integrate(ax, (t, 0, t))

# Intégration définie de la vitesse pour obtenir la position
x_t = sp.integrate(v_x, (t, 0, t))

# Simplification de l'expression de la position
x_t_simplified = x_t.simplify()

print(f"L'expression simplifiée de x(t) est : {x_t_simplified}")