import tkinter as tk
from tkinter import filedialog

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = {}
    for line in lines:
        id_part, string_part = line.split("}}")
        id_part += "}}"
        data[id_part] = string_part.strip()
    return data

def compare_files(file1_path, file2_path, output_file_path):
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)
    
    differences = []
    
    for id_part in data1:
        if id_part in data2 and data1[id_part] != data2[id_part]:
            differences.append(f"{id_part}{data1[id_part]}\n")
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(differences)

def select_files():
    root = tk.Tk()
    root.withdraw()  # Tkinter penceresini gizle
    
    file1_path = filedialog.askopenfilename(title="İlk dosyayı seçin")
    file2_path = filedialog.askopenfilename(title="İkinci dosyayı seçin")
    output_file_path = filedialog.asksaveasfilename(title="Kaydedilecek dosya adını girin", defaultextension=".txt")
    
    if file1_path and file2_path and output_file_path:
        compare_files(file1_path, file2_path, output_file_path)
        print(f"Farklar {output_file_path} dosyasına kaydedildi.")

# Kullanım
select_files()
