#!/usr/bin/python3
import donut
import time
import os
import argparse
from templates.main_c import main_c
from templates.shellcode_h import shellcode_h



def exe_to_bin(path_to_bin: str, output_dir: str):
    current_time = time.strftime("%I_%M%p", time.localtime())
    folder_name = time.strftime("%d_%m-", time.localtime()) + current_time
    folder_path = os.path.join(output_dir, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    outfile_name = os.path.join(folder_path, "shellcode.bin")
    donut.create(path_to_bin, output=outfile_name)
    return folder_name

def to_code(file_path):
    with open(file_path, 'rb') as file:
        bytesread = file.read()
    bytes_array = [f"0x{byte:02X}" for byte in bytesread]
    bytes_string_final = ', '.join(bytes_array)
    ps_shellcode = f"unsigned char shellcode[] = {{ {bytes_string_final} }};"
    return ps_shellcode

def generate_template(shellcode_size):
    main_template = main_c(shellcode_size = shellcode_size)
    shellcode_template = shellcode_h()
    return main_template.generate(), shellcode_template.generate()

def main():
    parser = argparse.ArgumentParser(description="Convert an EXE file to shellcode.")
    parser.add_argument("-i", "--input", metavar="input_file", type=str, help="Path to the input EXE file.", required=True)
    parser.add_argument("-o", "--output", metavar="output_dir", type=str, help="Path to the output directory.", required=True)
    args = parser.parse_args()

    exe_path = args.input
    out_dir = args.output
    print("[*] Converting EXE to Shellcode...")
    bin_path = exe_to_bin(exe_path, out_dir)

    print("[*] Converting Shellcode to C code...")
    c_code = to_code(os.path.join(out_dir, bin_path, "shellcode.bin"))
    with open(os.path.join(out_dir, bin_path, "shellcode.c"), "w") as f:
        f.write(c_code)
    print("[+] All tasks completed successfully.")
    bin_size = os.path.getsize(os.path.join(out_dir, bin_path, "shellcode.bin"))
    print(f"[+] Shellcode size: {bin_size} bytes.")
    
    main_c, shellcode_h = generate_template(bin_size)
    with open(os.path.join(out_dir, bin_path, "main.c"), "w") as f:
        f.write(main_c)
    with open(os.path.join(out_dir, bin_path, "shellcode.h"), "w") as f:
        f.write(shellcode_h)
if __name__ == "__main__":
    main()
