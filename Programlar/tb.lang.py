import tkinter as tk
from tkinter import filedialog

def dosya_sec():
    root = tk.Tk()
    root.withdraw()

    # İlk dosyanın seçimini yapın
    dosya1_adı = filedialog.askopenfilename(title="İlk dosyayı seçin", filetypes=[("Metin Dosyaları", "*.txt")])
    if not dosya1_adı:
        print("Dosya seçimi iptal edildi.")
        return

    # İkinci dosyanın seçimini yapın
    dosya2_adı = filedialog.askopenfilename(title="İkinci dosyayı seçin", filetypes=[("Metin Dosyaları", "*.txt")])
    if not dosya2_adı:
        print("Dosya seçimi iptal edildi.")
        return

    # İlk dosyadaki ID'leri bir küme (set) olarak alın
    idler_dosya1 = set()
    with open(dosya1_adı, "r", encoding="utf-8") as dosya1:
        for satır in dosya1:
            if ":" in satır:
                id_kısmı = satır.split(":")[0].strip()
                idler_dosya1.add(id_kısmı)

    # İkinci dosyadaki ID'leri bir küme (set) olarak alın
    idler_dosya2 = set()
    with open(dosya2_adı, "r", encoding="utf-8") as dosya2:
        for satır in dosya2:
            if ":" in satır:
                id_kısmı = satır.split(":")[0].strip()
                idler_dosya2.add(id_kısmı)

    # İkinci dosyada bulunup birinci dosyada bulunmayan ID'leri bulun
    eksik_idler = idler_dosya1 - idler_dosya2

    # Eksik ID'leri ve bulunduğu satırları yeni bir dosyaya kaydedin
    yeni_dosya_adı = "eksik_idler.txt"
    with open(yeni_dosya_adı, "w", encoding="utf-8") as yeni_dosya:
        with open(dosya1_adı, "r", encoding="utf-8") as dosya1:
            for satır in dosya1:
                if ":" in satır:
                    id_kısmı = satır.split(":")[0].strip()
                    if id_kısmı in eksik_idler:
                        yeni_dosya.write(satır)

    print(f"Eksik ID'ler {yeni_dosya_adı} dosyasına kaydedildi.")

if __name__ == "__main__":
    dosya_sec()
