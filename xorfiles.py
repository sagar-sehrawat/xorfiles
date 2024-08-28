#!/usr/bin/env python3

import os
import subprocess
import sys

def print_banner():
    banner = """
     _  __           ______ _ _
    | |/ /          |  ____(_) |
    | ' / ___  _ __ | |__   _| | _____ _ __
    |  < / _ \| '_ \|  __| | | |/ / _ \ '__|
    | . \ (_) | | | | |    | |   <  __/ |
    |_|\_\___/|_| |_|_|    |_|_|\_\___|_|

        Author: Sagar Sehrawat
    """
    print(banner)

def print_help():
    help_text = """
Usage: xorfiles.py [OPTIONS] FILE1 FILE2

Options:
  -h, --help        Display this help message.
  -o, --output      Specify the output file. Default is 'xor_output.bin'.
  -v, --version     Display version information.

Description:
  This script XORs the contents of two files byte by byte and outputs the result to a file.
  Both files must be of the same length. If they are not, the shorter file will be padded with null bytes.

Examples:
  python3 xorfiles.py 1st_file 2nd_file
  python3 xorfiles.py file1.bin file2.bin -o output.bin

    """
    print(help_text)

def xor_files(file1_path, file2_path, output_path):
    with open(file1_path, 'rb') as file1, open (file2_path, 'rb') as file2:
        file1_data = file1.read()
        file2_data = file2.read()

        max_length = max(len(file1_data), len(file2_data))
        file1_data = file1_data.ljust(max_length, b'\0')
        file2_data = file2_data.ljust(max_length, b'\0')

        xor_data = bytes(a ^ b for a, b in zip(file1_data, file2_data))

    with open(output_path, 'wb') as output_file:
        output_file.write(xor_data)

    print(f"XOR result saved to {output_path}")

    try:
        result = subprocess.run(['file', output_path], stdout=subprocess.PIPE)
        file_type = result.stdout.decode().strip()
        print(f"File type: {file_type}")
    except Exception as e:
        print(f"Could not identify file type: {e}")

def main():
    if len(sys.argv) < 3 or '-h' in sys.argv or '--help' in sys.argv:
        print_banner()
        print_help()
        sys.exit(0)

    if '-v' in sys.argv or '--version' in sys.argv:
        print("xorfiles.py version 1.0")
        sys.exit(0)

    if '-o' in sys.argv:
        output_index = sys.argv.index('-o') + 1
        output_path = sys.argv[output_index]
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
    elif '--output' in sys.argv:
        output_index = sys.argv.index('--output') + 1
        output_path = sys.argv[output_index]
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
    else:
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
        output_path = 'xor_output.bin'

    xor_files(file1_path, file2_path, output_path)

if __name__ == '__main__':
    # print_banner()
    main()
