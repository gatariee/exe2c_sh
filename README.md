# exe2c_sh
Converts PE executables into shellcode and loads it into usable C code, the default type is `unsigned char shellcode[]`.

It also has support for loader templates, the default output template is located at `/template/`. 




## Installation

```git
git clone https://github.com/gatariee/exe2c_sh.git
pip install -r requirements.txt
```

## Usage
`./exe2sh.py -i <path_to_bin> -o <output_folder>`

## Templates
Shellcode generated will also automatically be passed into a loader template, located at `/template/`. These should be edited to your liking, the default template is a simple loader that will load the shellcode into memory and execute it.

* [main.c](./templates/main_c.py)
  * The main loader template, this is where the shellcode will be loaded into.
* shellcode.c
  * This is where the shellcode is generated and parsed to.
* [shellcode.h](./templates/shellcode_h.py)
  * The shellcode header template, this is where the shellcode will be defined.

## Example
main.c
```c
#include <windows.h>
#include "shellcode.h"

int main(int argc, char *argv[]) {
    size_t shellcode_size = 42965; // auto-generated based on size of bin
    void *exec = VirtualAlloc(0, shellcode_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    memcpy(exec, shellcode, shellcode_size);
    ((void(*)())exec)();
    return 0;
}
```

shellcode.c
```c
unsigned char shellcode[] = { 0xE8, 0xC0, 0x45, 0x00, 0x00, 0xC0, 0x45 ... };
```

shellcode.h
```c
#ifndef SHELLCODE_H
#define SHELLCODE_H

extern unsigned char shellcode[];

#endif
```

## Donut
You may face AV issues when installing the [donut-shellcode](https://github.com/TheWover/donut) library, add an exclusion to the folder before installing.



