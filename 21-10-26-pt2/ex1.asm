.data 
            msg1: .asciiz "Digite o valor do comprimento: "
            msg2: .asciiz "Digite o valor da largura: "
            msg3: .asciiz "Digite o valor da altura: "
            msg4: .asciiz "Este é o volume: "
            
   .text 
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
         move $t3, $v0 
         
   
     mul $t4, $t0, $t1
     mul $t4, $t3, $t4
     
     
     li $v0, 4 
     la $a0, msg4
     syscall
     
     li $v0, 1
     move $a0, $t4
     syscall 
     
      