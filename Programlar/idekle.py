import tkinter as tk
from tkinter import filedialog

# Dosya seçiciyi başlatıyoruz
root = tk.Tk()
root.withdraw()

# ID'lerin bulunduğu .txt uzantılı dosya
print("Lütfen ID'lerin bulunduğu .txt uzantılı dosyayı seçin.")
file_path1 = filedialog.askopenfilename(title="Lütfen ID'lerin bulunduğu .txt uzantılı dosyayı seçin.")
print(f"Seçilen dosya: {file_path1}")

# ID'siz satırların bulunduğu .txt uzantılı dosya
print("Lütfen ID'siz satırların bulunduğu .txt uzantılı dosyayı seçin.")
file_path2 = filedialog.askopenfilename(title="Lütfen ID'siz satırların bulunduğu .txt uzantılı dosyayı seçin.")
print(f"Seçilen dosya: {file_path2}")

# Dosyaları okuma modunda ve 'utf-8' kodlamasıyla açıyoruz
with open(file_path1, 'r', encoding='utf-8') as f1, open(file_path2, 'r', encoding='utf-8') as f2:
    # Her iki dosyanın satırlarını okuyoruz
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Yeni bir dosya oluşturuyoruz
with open('yeni_dosyaid.txt', 'w', encoding='utf-8') as f:
    # Her iki dosyanın satırlarını eşleştiriyoruz
    for line1, line2 in zip(lines1, lines2):
        # İlk dosyadan ID'yi alıyoruz
        id = line1.split('}}')[0] + '}}'
        # İkinci dosyadan stringi alıyoruz
        string = line2.strip()
        # Yeni dosyaya ID ve stringi yazıyoruz
        f.write(f'{id}{string}\n')