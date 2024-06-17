import re
import tkinter as tk
from tkinter import filedialog

# Grafiksel kullanıcı arayüzü oluşturun
root = tk.Tk()
root.withdraw()  # Ana pencereyi gizleyin

# Dosya seçme penceresini açın ve başlığını ayarlayın
file_path = filedialog.askopenfilename(title="Belgelere ayrılacak en.diff.txt dosyasını seçin")

# Dosyanızı açın
with open(file_path, 'r') as f:
    lines = f.readlines()

# Her durum için ayrı bir dosya oluşturun
files = {'Added': open('Added.txt', 'w'),
         'Deleted': open('Removed.txt', 'w'),
         'Changed': open('Changed.txt', 'w')}

# Her satırı işleyin
for line in lines:
    # Durumu belirleyin (Added, Deleted, Changed)
    for status in ['Added', 'Deleted', 'Changed']:
        if line.startswith('\t' + status):
            # ID'yi ve metni ayıklayın
            id, text = re.search(rf'\t{status} (\d+:\d+:\d+) = "(.*)"', line).groups()
            # ID'yi istediğiniz formata dönüştürün
            id = '{{' + id.replace(':', '-') + ':}}'
            # İstediğiniz formatta yeni bir satır oluşturun
            new_line = id + text + '\n'
            # Yeni satırı ilgili dosyaya yazın
            files[status].write(new_line)

# Tüm dosyaları kapatın
for file in files.values():
    file.close()
