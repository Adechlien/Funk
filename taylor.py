import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import *
x = sp.Symbol('x')
class Taylor:
    def __init__(self, f, a, n):
        self.f = f
        self.a = a
        self.n = n

    def taylor(self):
        modelo = 0
        for i in range(self.n+1):
            modelo = modelo + (self.f.diff(x,i).subs(x,self.a)*(x-self.a)**i)/factorial(i)
        return modelo

    def errores(self, equis):
        valor_teorico = self.f.subs(x,equis).evalf()
        valor_experimental = self.taylor().subs(x,equis).evalf()
        error_absoluto = abs(valor_teorico - valor_experimental)
        error_relativo = abs((valor_teorico - valor_experimental) / valor_teorico)*100
        return valor_teorico, valor_experimental, error_absoluto, error_relativo
    
    def valores(self):
        valores_x = np.linspace(self.a - 5, self.a + 5, 100)
        valores_fx = [self.f.subs(x,i) for i in valores_x]
        valores_y = [self.taylor().subs(x,i) for i in valores_x]
        tcOriginal = list(zip(valores_x, valores_fx))
        tcTaylor = list(zip(valores_x, valores_y))

        return tcOriginal, tcTaylor
    
    # def grafica(self,x_min,x_max):
    #     valores_x = np.linspace(x_min,x_max,100)
    #     valores_fx = [self.f.subs(x,i) for i in valores_x]
    #     plt.plot(valores_x, valores_fx)
    #     valores_y = [self.taylor().subs(x,i) for i in valores_x]
    #     plt.plot(valores_x, valores_y)
    #     plt.legend(['f(x)','Taylor'])
    #     plt.grid()
    #     plt.title('Taylor')
    #     plt.xlabel('x')
    #     plt.ylabel('f(x)')
    #     plt.show()

    # def grafica(self,intervalo):
    #     valores_x = np.linspace(min(intervalo),max(intervalo),100)
    #     valores_fx = [self.f.subs(x,i) for i in valores_x]
    #     plt.plot(valores_x, valores_fx)
    #     valores_y = sp.lambdify(x,self.taylor())(valores_x)
    #     plt.plot(valores_x, valores_y)
    #     plt.legend(['f(x)','Taylor'])
    #     plt.grid()
    #     plt.title('Taylor')
    #     plt.xlabel('x')
    #     plt.ylabel('f(x)')
    #     plt.show()

class Derivacion_Numerica:

    def __init__(self, f, h, xi):
        self.f = f
        self.h = h
        self.xi = xi

    def adelante(self, xi):
        return (-self.f.subs(x, xi+2*xi)+4*self.f.subs(x, xi+xi)-3*self.f.subs(x, xi))/(2*xi)

    def atras(self, xi):
        return (3*self.f.subs(x, xi)-4*self.f.subs(x, xi-xi)+self.f.subs(x, xi-2*xi))/(2*xi)

    def central(self, xi):
        return (-self.f.subs(x, xi+2*xi)+8*self.f.subs(x, xi+xi)-8*self.f.subs(x, xi-xi)+self.f.subs(x, xi-2*xi))/(12*xi)

    def derivada(self,xi):
        return self.f.diff(x).subs(x,xi)

    def errores(self):
        equis = self.xi
        valor_teorico = self.derivada(x).subs(x,equis).evalf()
        valor_adelante = self.adelante(equis)
        valor_atras = self.atras(equis)
        valor_central = self.central(equis)
        error_adelante = abs(valor_teorico - valor_adelante)
        error_atras = abs(valor_teorico - valor_atras)
        error_central = abs(valor_teorico - valor_central)
        return valor_teorico, valor_adelante, valor_atras, valor_central, error_adelante, error_atras, error_central

