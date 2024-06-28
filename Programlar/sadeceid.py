import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    for line in lines:
        # ID kısmını parantezlerden ve iki nokta işaretinden temizle
        id_part = line.split(':')[0].replace('{{', '').replace('}}', '') + '\n'
        processed_lines.append(id_part)
    
    # Yeni dosya adı oluşturma
    directory = os.path.dirname(file_path)
    new_file_path = os.path.join(directory, 'sadeceid.txt')
    
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.writelines(processed_lines)
    
    print(f"İşlem tamamlandı. Yeni dosya: {new_file_path}")

# Tkinter kullanarak dosya seçici diyaloğu aç
def select_file():
    root = Tk()
    root.withdraw()  # Tkinter penceresini gizle
    file_path = askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

# Dosya seçimi
file_path = select_file()
if file_path:
    process_file(file_path)
else:
    print("Dosya seçilmedi.")
