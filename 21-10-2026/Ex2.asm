
.data
    msg1: .asciiz "Quantidade de camisetas pequenas: "
    msg2: .asciiz "Quantidade de camisetas medias: "
    msg3: .asciiz "Quantidade de camisetas grandes: "
    resultado: .asciiz "Valor arrecadado: R$ "

.text
.globl main
main:
    li $v0, 4
    la $a0, msg1
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    li $v0, 4
    la $a0, msg2
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    li $v0, 4
    la $a0, msg3
    syscall

    li $v0, 5
    syscall
    move $t2, $v0

    mul $t3, $t0, 10
    mul $t4, $t1, 12
    mul $t5, $t2, 15

    add $t6, $t3, $t4
    add $t6, $t6, $t5

    li $v0, 4
    la $a0, resultado
    syscall

    li $v0, 1
    move $a0, $t6
    syscall

    li $v0, 10
    syscall
