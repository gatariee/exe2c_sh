# exe2c_sh
Converts PE executables into shellcode and loads it into usable C code, the default type is `unsigned char shellcode[]`.

It also has support for loader templates, the default output template is located at `/template/`. 




## Installation

```git
git clone https://github.com/gatariee/exe2c_sh.git
pip install -r requirements.txt
```

## Donut
You may face AV issues when installing the [donut-shellcode](https://github.com/TheWover/donut) library, add an exclusion to the folder before installing.

## Usage
`./exe2sh.py -i <path_to_bin> -o <output_folder>`

## Example Output 



