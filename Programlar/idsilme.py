import tkinter as tk
from tkinter import filedialog

def remove_ids(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # ':' karakterinden sonrasını al
        new_line = line.split(':}}')[-1].strip()
        new_lines.append(new_line)

    # Yeni satırları dosyaya yaz
    with open(filename, 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line + '\n')

# Dosya seçme penceresini aç
root = tk.Tk()
root.withdraw()  # Tkinter penceresini gizle

filename = filedialog.askopenfilename(title="ID'leri silinecek .txt belgesini seçin")  # Dosya seçme penceresini aç
remove_ids(filename)