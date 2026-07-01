SYS_WRITE = 1
STDOUT_FILENO = 1
SYS_EXIT = 60

.data
buffer: .string "X -> X\n"

.text

#def s(z,c,d):
# if z!=0:s(z-1,c,c^d);print(c,'->',d);s(z-1,c^d,d)
#s(9,1,3)

mov $9, %rdi # height
mov $1, %rsi # from-peg
mov $3, %rdx # to-peg
call hanoi
mov $SYS_EXIT, %eax
mov $0, %edi
syscall

hanoi:
    push %rdi # save
    push %rsi
    push %rdx
    cmp $0, %rdi # if height zero
    jz hanoi_end # then exit
    push %rdi
    push %rdx
    dec %rdi # minus one height
    xor %rsi, %rdx # unused peg
    call hanoi # recurse
    pop %rdx
    pop %rdi

    mov %rsi, %r8 # put peg numbers in ASCII
    add $48, %r8
    mov %rdx, %r9
    add $48, %r9

    push %rdi
    push %rsi
    push %rdx
    mov %r8b,(buffer) # write peg numbers to buffer
    mov %r9b, (buffer+5)
    mov $SYS_WRITE, %eax
    mov $STDOUT_FILENO, %edi
    mov $buffer, %esi
    mov $7, %edx
    syscall # print
    pop %rdx
    pop %rsi
    pop %rdi
    dec %rdi # reduce height
    xor %rdx, %rsi # new dest peg
    call hanoi # recurse
    hanoi_end:
       pop %rdx
       pop %rsi
       pop %rdi
       ret
