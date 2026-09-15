"""
Exercício 21:
Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética.
Mostre a mensagem de acordo com a média:
a. Se a média for >= 6,0 exibir "APROVADO";
b. Se a média for >= 3,0 ou < 6,0 exibir "EXAME";
c. Se a média for < 3,0 exibir "RETIDO".
"""

def main():
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    n4 = float(input("Digite a 4ª nota: "))

    media = (n1 + n2 + n3 + n4) / 4
    print(f"Média: {media:.2f}")

    if media >= 6.0:
        print("APROVADO")
    elif media >= 3.0:
        print("EXAME")
    else:
        print("RETIDO")

if __name__ == "__main__":
    main()
