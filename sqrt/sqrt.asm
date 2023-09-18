;nasm -felf64 sqrt.asm && gcc -no-pie -fno-pie sqrt.o && ./a.out

%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro

%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro

%macro print 1 
    pushd
    push rbp
    
    mov rdi, format
    mov rsi, %1
    call printf 

    pop rbp
    popd
%endmacro

section   .text
global    main

extern printf

main:   
    xor rdx, rdx
    mov rax, [num]
    mov rcx, 2 

    div rcx
    mov [x1], rax

    xor rdx, rdx
    mov rax, [num]
    mov rbx, [x1] 

    div rbx        ;(num / x1)
    xor rdx, rdx
    add rax, rbx   ;(x1 + (num / x1)
    div rcx        ;(x1 + (num / x1)) // 2
    mov [x2], rax

while:
    mov rax, [x1]
    sub rax, [x2] 
    cmp rax, 1
    jl end

    mov rax, [x2]
    mov [x1], rax  ;x1 = x2
    
    xor rax, rax
    xor rdx, rdx
    mov rax, [num]
    mov rbx, [x1] 

    div rbx        ;(num / x1)    
    xor rdx, rdx
    add rax, rbx   ;(x1 + (num / x1)
    div rcx        ;(x1 + (num / x1)) // 2
    
    mov [x2], rax
    jmp while
    
end:
    mov rax, [x2]
    print rax

    mov       rax, 60
    xor       rdi, rdi
    syscall

section   .data
    format db "Approximate square root: %d", 10, 0
    num dq 121
  
section .bss
    x1 resq 1
    x2 resq 1

    