"""
Exercício 25:
Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos,
sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
"""

def main():
    h_inicio = int(input("Hora de início (0-23): "))
    m_inicio = int(input("Minuto de início (0-59): "))
    h_fim = int(input("Hora de término (0-23): "))
    m_fim = int(input("Minuto de término (0-59): "))

    total_inicio = (h_inicio * 60) + m_inicio
    total_fim = (h_fim * 60) + m_fim

    if total_fim <= total_inicio:
        total_fim += 24 * 60

    duracao_minutos = total_fim - total_inicio
    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60

    print(f"Duração do jogo: {horas} hora(s) e {minutos} minuto(s).")
