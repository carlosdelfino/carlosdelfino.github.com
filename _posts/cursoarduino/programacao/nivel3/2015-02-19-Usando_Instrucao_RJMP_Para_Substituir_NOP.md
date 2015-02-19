
Nada melhor que pequenos macetes para se ter um programa eficiente e pequeno.

Usamos muitas vezes a instrução "nop" para obter um passo de instrução no processador sem atividade alguma.

Tal instrução é muito usada para sincronizar códigos em especial com o mundo externo, por exemplo em instruções do tipo delay() ou em códigos onde precisa aguardar uma resposta precisa do sistema de tempos em tempos que sejam múltiplos baixos do clock do processador.

Porém acabei de aprender este novo macete usando a instrução "rjmp" no controlador da família ATMega:

""rjmp .+0" 

Tal instrução faz com que o controlador pule para um determinado endereço remoto de 8bits, como é preciso dois clocks para carregar tal instrução





RJMP- Relative Jump
Description:
Relative jump to an address within PC - 2K +1 and PC + 2K (words). In the assembler, labels are used instead of relative operands. For AVR microcontrollers with program memory not exceeding 4K words (8K bytes) this instruction can address the entire memory from every address location.
Operation:
(i)PC ← PC + k + 1
Syntax: Operands: Program Counter: Stack
(i) RJMP k -2K ≤ k < 2K PC ← PC + k + 1 Unchanged
16-bit Opcode:
1100
kkkk
kkkk
kkkk
Status Register (SREG) and Boolean Formula:
I
T
H
S
V
N
Z
C
-
-
-
-
-
-
-
-
Example:
cpi r16,$42 ; Compare r16 to $42
brne error ; Branch if r16 ⇔ $42
rjmpok ; Unconditional branch
error: addr16,r17 ; Add r17 to r16
incr16 ; Increment r16
ok: nop ; Destination for rjmp (do nothing)
Words: 1 (2 bytes)
Cycles: 2


## Fontes

 * [AVR Assembler Instructions - NOP - No OPeration](http://www.atmel.com/webdoc/avrassembler/avrassembler.wb_NOP.html)
 * [AVR Assembler Instructions - RJMP- Relative Jump](http://www.atmel.com/webdoc/avrassembler/avrassembler.wb_RJMP.html)