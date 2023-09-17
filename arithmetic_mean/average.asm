;nasm -felf64 average.asm && gcc -no-pie -fno-pie average.o && ./a.out

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
    mov ebx, [len] 
    mov ecx, dword 0
subtract:  
    sub ebx, dword 4  

    mov eax, [x+ebx]
    sub eax, [y+ebx]

    add [sum], eax
    inc ecx

    xor rax, rax
    test ebx, ebx   
    jnz subtract

    mov eax, [sum]
    xor edx, edx
    mov ebx, ecx
    
    cdq
    idiv ebx

    print rax

    mov       rax, 60
    xor       rdi, rdi
    syscall


section   .data
    format db "Average is: %d", 10, 0

    x dd 5, 3, 2, 6, 1, 7, 4
    len dd $ - x
    y dd 0, 10, 1, 9, 2, 8, 5
    
    sum dd 0
    