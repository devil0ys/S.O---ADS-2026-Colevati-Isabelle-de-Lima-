.data 
            m1: .asciiz "Digite um número maior que 2 e menor que 20: "
            m2: .asciiz "\nEste número não entra no critério, tente novamente.\n\n"
            m3: .asciiz "Este é o resultado da multiplicação dos números de fibonacci: "
            
.text 
.globl main

main: 

   inicio:
     li $v0, 4
     la $a0, m1
     syscall 
     
     li $v0, 5 
     syscall
     move $t0, $v0
     
    ble $t0, 2, encerrar
    bge $t0, 20, encerrar
    
    j continua
    
    encerrar: 
    li $v0, 4
    la $a0, m2
    syscall 
    
    j inicio 
  
    #O 32bts não suporta, é necessário mudar para o 'double' 64 bits usando o mtc1 e cvt.d.w
    
    
    continua:
    
    li $t1, 1 #Primeiro Número ou A
    li $t2, 1 #Segundo número ou B
    li $t3, 2 #O $t3 é o que conta a quantidade de números de fibonacci já feitos
    li $t6, 1 #O $t6 é o multiplicador 
    mtc1 $t6, $f0
    cvt.d.w $f0, $f0
    
    
    
    repetir:
    
    beq $t3, $t0, fim_laco
    
    add $t5, $t1, $t2
    
    mtc1 $t5, $f2
    cvt.d.w $f2, $f2 
    
    mul.d $f0, $f0, $f2
    
    move $t1, $t2
    move $t2, $t5 
    
    addi $t3, $t3, 1
    
    j repetir
    
fim_laco:    
    li $v0, 4
    la $a0, m3
    syscall 
    
   li $v0, 3          
    mov.d $f12, $f0
    syscall
    
    
    
    
    
  