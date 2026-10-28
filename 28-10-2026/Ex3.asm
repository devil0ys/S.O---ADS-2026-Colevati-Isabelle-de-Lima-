
.data
msg1: .asciiz "Mes de nascimento (1-12): "
msg2: .asciiz "Ano de nascimento: "
msg3: .asciiz "Mes atual (1-12): "
msg4: .asciiz "Ano atual: "
msg5: .asciiz "Idade em meses: "

.text
main:
ler_mes_nasc:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t0, $v0
    blt $t0, 1, ler_mes_nasc
    bgt $t0, 12, ler_mes_nasc

    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 5
    syscall
    move $t1, $v0

ler_mes_atual:
    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 5
    syscall
    move $t2, $v0
    blt $t2, 1, ler_mes_atual
    bgt $t2, 12, ler_mes_atual

    li $v0, 4
    la $a0, msg4
    syscall
    li $v0, 5
    syscall
    move $t3, $v0

    sub $t4, $t3, $t1
    li $t5, 12
    mul $t4, $t4, $t5
    sub $t6, $t2, $t0
    add $t7, $t4, $t6

    li $v0, 4
    la $a0, msg5
    syscall
    li $v0, 1
    move $a0, $t7
    syscall
