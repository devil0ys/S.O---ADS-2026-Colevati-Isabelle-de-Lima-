notas = []
for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))
media = sum(notas) / 4
print("Média:", media)
if media >= 6:
    print("APROVADO")
elif media >= 3:
    print("EXAME")
else:
    print("RETIDO")