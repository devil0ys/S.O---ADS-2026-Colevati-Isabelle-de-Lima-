.data
       cat1: .asciiz "Digite o valor do cateto 1: "
       cat2: .asciiz "Digite o valor do cateto 2: "
       hip: .asciiz "Este é o valor da hipotenusa: "

 .text     

  main:
    li $v0, 4
    la $a0, cat1
    syscall
    
    li $v0, 6
    syscall
    mov.s  $f1, $f0
    
    
     li $v0, 4
    la $a0, cat2
    syscall
    
    li $v0, 6
    syscall
    mov.s  $f2, $f0
    
    mul.s $f1, $f1, $f1
    mul.s $f2, $f2, $f2
    add.s $f3, $f1, $f2
    sqrt.s $f4, $f3
    
    li $v0, 4
    la $a0, hip
    syscall
    
   li $v0, 2
  mov.s $f12, $f4
  syscall