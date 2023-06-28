#!/usr/bin/python3
import donut
import time
import os
import argparse
from templates.main_c import main_c
from templates.shellcode_h import shellcode_h

def exe_to_bin(path_to_bin: str, output_dir: str):
    """
    Uses `donut` to convert PE to binary shellcode

    WARNING: `donut.create()` performs IO operations!

    Args:
        path_to_bin (str): Path to the PE file.
        output_dir (str): Folder to store the parsed output.
    """
    outfile_name = os.path.join(output_dir, "shellcode.bin")
    donut.create(path_to_bin, output=outfile_name)

def to_code(file_path: str) -> str:
    """
    Converts a binary file to a parsable C char array.

    Args:
        file_path (str): Path to the binary file.

    Returns:
        str: C code for the char array.
    """
    with open(file_path, 'rb') as file:
        bytesread = file.read()
    bytes_array = [f"0x{byte:02X}" for byte in bytesread]
    bytes_string_final = ', '.join(bytes_array)
    ps_shellcode = f"unsigned char shellcode[] = {{ {bytes_string_final} }};"
    return ps_shellcode

def generate_template(shellcode_size) -> tuple[str, str]:
    """
    Generates the main.c and shellcode.h files.
    
    Args:
        shellcode_size (_type_): Size of the shellcode in bytes.

    Returns:
        tuple[str, str]: The string contents of the main.c and shellcode.h files.
    """
    main_template = main_c(shellcode_size)
    shellcode_template = shellcode_h()
    return main_template.generate(), shellcode_template.generate()

def write_file(file_path: str, contents: str):
    """
    Writes the contents to the file.

    Args:
        file_path (str): Path to the file.
        contents (str): Contents to write to the file.
    """
    with open(file_path, "w") as f:
        f.write(contents)

def main():
    parser = argparse.ArgumentParser(description="Convert an EXE file to shellcode.")
    parser.add_argument("-i", "--input", metavar="input_file", type=str, help="Path to the input EXE file.", required=True)
    parser.add_argument("-o", "--output", metavar="output_dir", type=str, help="Path to the output directory.", required=True)
    args = parser.parse_args()
    exe_path = args.input
    out_dir = args.output
    save_path = os.path.join(out_dir, time.strftime("%d_%m-%I_%M%p", time.localtime()))
    os.makedirs(save_path, exist_ok=True)
    print("[*] Input EXE file:", exe_path)
    print("[*] Output directory:", save_path)

    print("[*] Converting EXE to Shellcode...")
    exe_to_bin(exe_path, save_path)

    print("[*] Converting Shellcode to C code...")
    c_code = to_code(os.path.join(save_path, "shellcode.bin"))
    write_file(os.path.join(save_path, "shellcode.c"), c_code)

    print("[*] Generating template...")
    bin_size = os.path.getsize(os.path.join(save_path, "shellcode.bin"))
    main_c, shellcode_h = generate_template(bin_size)
    write_file(os.path.join(save_path, "main.c"), main_c)
    write_file(os.path.join(save_path, "shellcode.h"), shellcode_h)

    print("[+] All tasks completed successfully.")
    print(f"[+] Shellcode size: {bin_size} bytes.")

if __name__ == "__main__":
    main()
