#Variaveis globais
num1 = 0
num2 = 0

#Modulo
def calcularValor(): 
   global num1,num2
   num1 = int(input("Digite o primeiro numero: "))
   num2 = int(input("Digite o segundo numero: "))

   if num1 > num2: 
       num3 = num1 - num2
       print("O resultado da subtração é: ", num3)
   else:
       num3 = num2 - num1
   print("O resultado da subtração é: ", num3) 


def main(): 
    calcularValor() 
if __name__ == "__main__":
    main()  