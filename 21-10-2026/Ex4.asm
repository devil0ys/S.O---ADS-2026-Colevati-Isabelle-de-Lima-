.data 
   ladomenor: .asciiz "Digite o valor do lado menor: " 
   ladomaior: .asciiz "Digite o valor do lado maior: "
   alturatra: .asciiz "Digite o valor da altura: "
   resultado: .asciiz "Area do trapézio: "
   

.text 
 main:
  li $v0, 4
  la $a0, ladomenor
  syscall
  
  li $v0, 5 
  syscall
  move $t0, $v0 
  
  li $v0, 4
  la $a0, ladomaior
  syscall
  
  li $v0, 5 
  syscall
  move $t1, $v0
  
    li $v0, 4
  la $a0, alturatra
  syscall
  
  li $v0, 5 
  syscall
  move $t2, $v0
  
  
  add $t3, $t0, $t1
  mul $t4, $t2, $t3
  div $t4, $t4, 2
  
  li $v0, 4
  la $a0, resultado 
  syscall
  
 li $v0, 1
 move $a0, $t4
  syscall
  