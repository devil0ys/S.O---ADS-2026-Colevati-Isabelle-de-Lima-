#Váriaveis Globais
nota1 = 0
nota2 = 0  
nota3 = 0
nota4 = 0
media = 0

def LerNotas():
    global nota1,nota2,nota3,nota4 
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

def Calcular():
    global nota1,nota2,nota3,nota4
    global media
    media = (nota1 + nota2 + nota3 + nota4) / 4

def DefinirAprovacao():
    global media
    if media >= 6.0:
        print("Aluno APROVADO com média: ", media)
    elif media >=3.0 and media <6.0:
        print("Aluno para EXAME com média: ", media) 
    elif media < 3.0:
        print("Aluno RETIDO com média: ", media)

def main():
    LerNotas()
    Calcular()  
    DefinirAprovacao() 

if __name__ == "__main__":
    main()
