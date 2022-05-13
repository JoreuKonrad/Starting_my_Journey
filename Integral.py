#Calcular a integral da função f(x) = -2*x**3-4*x**2+13*x-1
from sympy import *
print('Exercicio 1:')
x,f = symbols('x f')
f = -2*x**3-4*x**2+13*x-1
print(integrate(f,x))



print('')
print('Exercicio 2:')
###########################
x,f = symbols('x f')
f = -2*x**3-4*x**2+13*x-1
resultado = integrate(f,(x,1,2))
print(resultado)

