#Calcular a area e fazer o grafico entre uma função e o intervalo. Seja f = x**2 e [0,2] o seu periodo.
print('Exericio 1')
from sympy import *
f,x = symbols('f x')
f = x**2
print('O valor da área é:',integrate(f,(x,0,2)))

print('Exercicio 2: O grafico a seguir.')
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,3,1000)
f = x**2
plt.plot(x,f,color='blue')
plt.axhline(color='blue')
plt.fill_between(x,f,where = [(x>0) and (x<2) for x in x],color = 'green')
plt.plot()

#Calcule a area entre as funções y=2*x e y=1/x com x variando entre 1 a 4.
print('Exericio 3:')
import matplotlib.pyplot as plt
from sympy import *
x,f,g = symbols('x f g')
f = 2*x
g = 1/x
A = integrate((f-g),(x,1,4))
x = np.linspace(0.5,4.5,1000)
f = 2*x
g = 1/x
plt.plot(x,f,color='blue')
plt.plot(x,g,color='red')
plt.axhline(color='black')
plt.fill_between(x,f,g,where=[(x>1) and (x<4) for x in x],color='magenta')
plt.show()
print('Area:',A)









