#variaveis globais 
a = 0
b = 0 
c = 0
d = 0


def LerValores():
    global a,b,c,d, valido
    print('Digite 3 valores obrigatoriamente em ordem crescente')
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    if a == b or a == c or b == c:
        print("Os valores não podem ser iguais")
        exit()
    else:
        if a > b or b > c:
            print("Os valores não estão em ordem crescente")
            exit()


def CalcularOrdem():
    global a,b,c,d
    d = int(input("Digite o quarto valor: "))
    if d < a:
        print("A ordem crescente é: ", d, " , ", a, " , ", b, " , ", c)
    elif d > a and d < b:
        print("A ordem crescente é: ", a, " , ", d, " , ", b, " , ", c)
    elif d > b and d < c:
        print("A ordem crescente é: ", a, " , ", b, " , ", d, " , ", c)
    elif d > c:
        print("A ordem crescente é: ", a, " , ", b, " , ", c, " , ", d)

def main():  
   LerValores()
   CalcularOrdem()

if __name__ == "__main__":
    main()