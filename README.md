# exe2c_sh
Converts PE executables into shellcode and loads it into usable C/C++ code, currently the default type is `unsigned char shellcode[]`.

It also has support for loader templates, the default output template is located at `/template/`. 

## Usage
`./exe2sh.py -i <path_to_bin> -o <output_folder>`


