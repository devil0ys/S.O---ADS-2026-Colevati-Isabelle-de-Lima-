
.data
msg1: .asciiz "Valor da compra em centavos (100000 a 999999): "
msg2: .asciiz "Valor da parcela em centavos (10000 a 50000): "
msg3: .asciiz "Quantidade de parcelas: "
msg4: .asciiz "\nValor invalido! Digite novamente.\n"

.text

main:
ler_compra:
    li $v0, 4
    la $a0, msg1
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    blt $t0, 100000, erro_compra
    bgt $t0, 999999, erro_compra
    j ler_parcela

erro_compra:
    li $v0, 4
    la $a0, msg4
    syscall
    j ler_compra

ler_parcela:
    li $v0, 4
    la $a0, msg2
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    blt $t1, 10000, erro_parcela
    bgt $t1, 50000, erro_parcela
    j calcular

erro_parcela:
    li $v0, 4
    la $a0, msg4
    syscall
    j ler_parcela

calcular:
    addi $t2, $t1, -1
    add $t3, $t0, $t2
    div $t3, $t1
    mflo $t4

    li $v0, 4
    la $a0, msg3
    syscall

    li $v0, 1
    move $a0, $t4
    syscall

   
