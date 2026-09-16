h_inicio = int(input("Hora inicial: "))
m_inicio = int(input("Minuto inicial: "))
h_fim = int(input("Hora final: "))
m_fim = int(input("Minuto final: "))

inicio = h_inicio * 60 + m_inicio
fim = h_fim * 60 + m_fim

if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio
print("Duração:", duracao // 60, "hora(s) e", duracao % 60, "minuto(s)")