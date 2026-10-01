#Váriaveis Globais 
valor1 = 0
valor2 = 0

def LerValores():
    global valor1,valor2
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    if valor1 == valor2:
        print("Os valores são iguais: ", valor1)
def Ordem():
    global valor1,valor2
    if valor1 > valor2:
        print("A ordem decrescente é: ", valor1, " e ", valor2)
    elif valor1 < valor2:
        print("A ordem decrescente é: ", valor2, " e ", valor1)

def main():
    LerValores()
    Ordem() 

if __name__ == "__main__":
    main()