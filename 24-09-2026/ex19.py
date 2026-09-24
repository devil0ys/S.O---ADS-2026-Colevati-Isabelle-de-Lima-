#Variaveis globais
num1 = 0
num2 = 0

#Modulo
def MaiorValor(): 
   global num1,num2
   num1 = int(input("Digite o primeiro numero: "))
   num2 = int(input("Digite o segundo numero: "))

   if num1 > num2: 
       print("O maior valor é: ", num1)
   elif num1 < num2:
       print("O maior valor é: ", num2)       
   else:
       print("Os valores são iguais: ", num1)
   


def main(): 
    MaiorValor() 
if __name__ == "__main__":
    main()  