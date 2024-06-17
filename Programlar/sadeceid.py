import tkinter as tk
from tkinter import filedialog
import os

def extract_ids():
    root = tk.Tk()
    root.withdraw()

    input_file_path = filedialog.askopenfilename(title="Sadece ID'lerinin kalmasını istediğiniz .txt belgesini seçin")
    base_name = os.path.splitext(input_file_path)[0]
    output_file_path = base_name + "_ID.txt"

    with open(input_file_path, 'r') as f_in, open(output_file_path, 'w') as f_out:
        for line in f_in:
            if line.startswith('{{') and ':' in line:
                id = line.split(':')[0].replace('{{', '') + '\n'
                f_out.write(id)

# Kullanımı
extract_ids()