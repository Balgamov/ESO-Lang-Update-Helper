import tkinter as tk
from tkinter import filedialog

# Dosya seçme işlemi için bir GUI oluşturma
root = tk.Tk()
root.withdraw()

# Dosya seçme penceresini açma
file_path1 = filedialog.askopenfilename(title="Oyuna yeni eklenen satırların bulunduğu .txt")
file_path2 = filedialog.askopenfilename(title="Yeni satırların ekleneceği tb.lang.txt ya da tr.lang.txt")

# Dosyaları okuma
with open(file_path1, 'r', encoding='utf-8') as f:
    lines1 = f.readlines()

with open(file_path2, 'r', encoding='utf-8') as f:
    lines2 = f.readlines()

# Her iki dosyanın satırlarını birleştirme
all_lines = lines1 + lines2

# Her satırı kontrol etme ve ID'ye göre sıralama
try:
    sorted_lines = sorted(all_lines, key=lambda x: tuple(map(int, x.strip('{}\n').split(':')[0].split('-'))))
except ValueError as e:
    print(f"Hatalı format veya değer: {e}")

# Sonucu yeni bir dosyaya yazma
with open('sonuc.txt', 'w', encoding='utf-8') as f:
    for line in sorted_lines:
        f.write(line)