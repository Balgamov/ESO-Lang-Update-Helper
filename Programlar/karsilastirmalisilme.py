import tkinter as tk
from tkinter import filedialog

def remove_matching_lines(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f:
        lines1 = f.readlines()
    with open(file2, 'r', encoding='utf-8') as f:
        lines2 = f.readlines()

    lines1_ids = [line.split('}}')[0] + '}}' for line in lines1]
    lines2_new = [line for line in lines2 if line.split('}}')[0] + '}}' not in lines1_ids]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines2_new)

# Dosya seçiciyi başlatıyoruz
root = tk.Tk()
root.withdraw()

# Yeni Güncellemede Silinen Satırlar .txt
print("Lütfen 'Yeni Güncellemede Silinen Satırlar .txt' dosyasını seçin.")
file_path1 = filedialog.askopenfilename(title="Yeni Güncellemede Silinen Satırlar .txt")
print(f"Seçilen dosya: {file_path1}")

# Orjinal lang.txt dosyası
print("Lütfen 'Orjinal lang.txt dosyası' dosyasını seçin.")
file_path2 = filedialog.askopenfilename(title="Orjinal lang.txt dosyası")
print(f"Seçilen dosya: {file_path2}")

# Çıkış dosyası
output_file = "sonuc.txt"
remove_matching_lines(file_path1, file_path2, output_file)
print(f"İşlem tamamlandı. Sonuçlar '{output_file}' dosyasına kaydedildi.")
