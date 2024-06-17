import re
import tkinter as tk
from tkinter import filedialog

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def parse_lua_file(lua_lines):
    lua_dict = {}
    for line in lua_lines:
        match = re.match(r'SafeAddString\((SI_[A-Z0-9_]+), "(.*)", \d+\)', line)
        if match:
            key = match.group(1)
            value = match.group(2)
            lua_dict[key] = value
    return lua_dict

def parse_str_file(str_lines):
    str_dict = {}
    for line in str_lines:
        match = re.match(r'\[(SI_[A-Z0-9_]+)\] = "(.*)"', line)
        if match:
            key = match.group(1)
            value = match.group(2)
            str_dict[key] = value
    return str_dict

def find_missing_and_removed_strings(lua_dict, str_dict):
    missing_strings = {}
    removed_strings = {}

    for key, value in lua_dict.items():
        if key not in str_dict:
            missing_strings[key] = value
    
    for key, value in str_dict.items():
        if key not in lua_dict:
            removed_strings[key] = value
    
    return missing_strings, removed_strings

def write_strings_to_file(strings_dict, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for key, value in strings_dict.items():
            file.write(f'[{key}] = "{value}"\n')

def main():
    root = tk.Tk()
    root.withdraw()

    lua_file_path = filedialog.askopenfilename(title="Select the .lua file", filetypes=[("LUA files", "*.lua"), ("All files", "*.*")])
    str_file_path = filedialog.askopenfilename(title="Select the .str file", filetypes=[("STR files", "*.str"), ("All files", "*.*")])

    if not lua_file_path or not str_file_path:
        print("Both files need to be selected.")
        return

    lua_lines = read_file(lua_file_path)
    str_lines = read_file(str_file_path)

    lua_dict = parse_lua_file(lua_lines)
    str_dict = parse_str_file(str_lines)

    missing_strings, removed_strings = find_missing_and_removed_strings(lua_dict, str_dict)

    if missing_strings:
        write_strings_to_file(missing_strings, "yeni_clipre.txt")
        print(f"Missing strings have been written to yeni_clipre.txt")

    if removed_strings:
        write_strings_to_file(removed_strings, "lua_silinmis.txt")
        print(f"Removed strings have been written to lua_silinmis.txt")

if __name__ == "__main__":
    main()