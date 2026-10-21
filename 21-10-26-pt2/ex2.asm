.data 
                         msg1: .asciiz "Digite o valor do raio da circuferencia: "
                         msg2: .asciiz "Este é o comprimento da circuferencia: "
                         
.text 
       li $v0, 4
       la $a0, msg1 
       syscall 
 
       li $v0, 5
       syscall
       move $t0, $v0 
       
       mul $t1, $t0, 6 
       
       li $v0, 4
       la $a0, msg2 
       syscall
       
       li  $v0, 1 
       move $a0, $t1
       syscall
       
 
 