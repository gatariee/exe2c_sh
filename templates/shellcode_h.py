import textwrap
from dataclasses import dataclass

@dataclass
class shellcode_h:
    def generate(self):
        template = textwrap.dedent("""\
        #ifndef SHELLCODE_H
        #define SHELLCODE_H

        extern unsigned char shellcode[];

        #endif
        """)
        return template