.data 
                msg1: .asciiz "Digite o primeiro número: "
                msg2: .asciiz "Digite o segundo número: "
                msg3: .asciiz "Resultado: "
                
      .text 
      main: 
      li $v0, 4
      la $a0, msg1
      syscall 
      
      li $v0, 5
      syscall
       move $t0, $v0
      
        repetir:
         li $v0, 4
      la $a0, msg2
      syscall 
      
      li $v0, 5
      syscall
       move $t1, $v0
       beq $t1, $0, repetir
       
       div $t0, $t1
       mflo $t2
       
       li $v0, 4
       la $a0, msg3
       syscall 
       
       li $v0, 1
       move $a0, $t2
       syscall
       
       
       
     