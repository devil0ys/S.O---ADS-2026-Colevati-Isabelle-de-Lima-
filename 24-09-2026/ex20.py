import math 

#Variaveis globais
A = 0
B = 0
C = 0
delta = 0

def LerValores(): 
   global A,B,C
   A = int(input("Digite o valor de A: "))
   B = int(input("Digite o valor de B: "))
   C = int(input("Digite o valor de C: "))

def CalcularDelta():
   global A,B,C,delta
   delta = (B**2) - (4*A*C)
   print("O valor de delta é: ", delta)

def CalcularRaizes():
   global A,B,C,delta
   if delta < 0:
       print("Não existem raizes reais")
   elif delta == 0:
       raiz = -B/(2*A)
       print("Existe apenas uma raiz real: ", raiz)
   else:
       raiz1 = (-B + math.sqrt(delta)) / (2*A)
       raiz2 = (-B - math.sqrt(delta)) / (2*A)
       print("As raizes reais são: ", raiz1, " e ", raiz2)

def main():
    LerValores()
    CalcularDelta()
    CalcularRaizes()

if __name__ == "__main__":
    main()  