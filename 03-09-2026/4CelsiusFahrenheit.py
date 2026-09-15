#Calcular uma equação de 2º grau
import math

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Não há raízes reais") 

else: 
#Calculo das raízes
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)


    print("X1 =", x1 )
    print("X2 =", x2 )