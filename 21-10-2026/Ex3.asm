
.data
    msg1: .asciiz "Horas normais trabalhadas: "
    msg2: .asciiz "Horas extras trabalhadas: "
    msg3: .asciiz "Valor do desconto: "
    msg4: .asciiz "\nSalario bruto: R$ "
    msg5: .asciiz "\nSalario liquido: R$ "

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
    mul $t4, $t1, 15
    add $t5, $t3, $t4

    sub $t6, $t5, $t2

    li $v0, 4
    la $a0, msg4
    syscall

    li $v0, 1
    move $a0, $t5
    syscall

    li $v0, 4
    la $a0, msg5
    syscall

    li $v0, 1
    move $a0, $t6
    syscall

    li $v0, 10
    syscall
