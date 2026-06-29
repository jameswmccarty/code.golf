SYS_WRITE = 1
SYS_EXIT = 60
STDOUT_FILENO = 1
SEGSIZE = 3
ROWSIZE = 30

# Printing
.data
newline: .string "\n"
buffer: .ascii " _     _  _     _  _  _  _  _ | |  | _| _||_||_ |_   ||_||_||_|  ||_  _|  | _||_|  ||_| _|"

.text
# Accessing arguments
pop %rbx
pop %rax
pop %rsi

mov %rsi, %rdi

mov $-1, %ecx
xor %al, %al
repnz scasb

not %ecx # length of input
dec %ecx
mov %ecx, %r12d # 
xor %r13, %r13 # idx = 0
xor %r14, %r14 # row = 0

argLoop:
    cmp $3, %r14 # if row > 3, exit
    jz end
    cmp %r13, %r12 # if idx > len(input)
    jz nextRow 
    # get the digit at the input buffer at current index
    push %rsi
    xor %eax, %eax
    movb (%rsi,%r13), %al
    sub $48, %al
    mov %rax, %rdi
    mov %r14, %rsi
    call printSeg
    inc %r13
    pop %rsi
    jmp argLoop

printSeg:
    #%rdi - digit number
    #%rsi - row number (0. 1, 2)
    imul $ROWSIZE, %rsi, %rsi
    imul $SEGSIZE, %rdi, %rdi
    add %rsi, %rdi

    lea buffer(%rdi), %rsi      # write() buffer pointer

    mov $SEGSIZE, %edx          # count
    mov $SYS_WRITE, %eax        # syscall number
    mov $STDOUT_FILENO, %edi    # fd
    syscall
    ret

nextRow:
    push %rsi # avoid clobber on write
    mov $newline, %esi
    mov $1, %edx          # count
    mov $SYS_WRITE, %eax        # syscall number
    mov $STDOUT_FILENO, %edi    # fd
    syscall
    xor %r13, %r13 # idx = 0
    inc %r14 # row += 1
    pop %rsi
    jmp argLoop

end:
mov $SYS_EXIT, %eax
mov $0, %edi
syscall
