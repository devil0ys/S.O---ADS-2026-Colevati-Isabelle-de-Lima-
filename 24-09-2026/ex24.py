#Variáveis Globais 
V1 = 0

def digitarValor():
    global V1
    V1 = int(input("Digite um valor: "))
    if V1 % 2 == 0 and V1 % 3 == 0:
        print("O valor é divisível por 2 e 3:" , V1)
    elif V1 % 3 == 0:
        print("O valor é divisível por 3:" , V1)
    elif V1 % 2 == 0 :
        print("O valor é divisível por 2:" , V1)
    elif V1 % 2 != 0 and V1 % 3 != 0:
        print("O valor não é divisível por 2 e nem por 3:" , V1)

def main():
    digitarValor() 

if __name__ == "__main__":
    main()
        