import tkinter as tk
from tkinter import filedialog
import os

def replace_lines(file1_path, file2_path, output_path):
    # Dosya 1'i oku ve satırları bir sözlükte depola (ID: Satır)
    with open(file1_path, 'r', encoding='utf-8') as file1:
        lines1 = {line.split(':')[0]: line for line in file1}

    # Dosya 2'yi oku ve satırları bir sözlükte depola (ID: Satır)
    with open(file2_path, 'r', encoding='utf-8') as file2:
        lines2 = {line.split(':')[0]: line for line in file2}

    # Ortak ID'leri bul ve birinci dosyadaki satırları ikinci dosyadakiyle değiştir
    for common_id in set(lines1.keys()) & set(lines2.keys()):
        lines1[common_id] = lines2[common_id]

    # Değiştirilmiş satırları yeni bir dosyaya yaz
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines1.values())

    print(f"Değiştirilmiş satırlar {output_path} dosyasına kaydedildi.")

# Klasör seçme penceresini aç
root = tk.Tk()
root.withdraw()
file1_path = filedialog.askopenfilename(title=".lang dosyasını seçin")
file2_path = filedialog.askopenfilename(title="Changed.txt dosyasını seçin")

if file1_path and file2_path:
    folder_path = os.path.dirname(file1_path)
    output_path = os.path.join(folder_path, "changed_done.txt")
    replace_lines(file1_path, file2_path, output_path)
else:
    print("Dosya seçimi iptal edildi.")
