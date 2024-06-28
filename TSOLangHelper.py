from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider, QDesktopWidget, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QSize
import sys
import os
import subprocess
import pygame

# Pygame'i başlat
pygame.mixer.init()

# Get the directory of the current script
def resource_path(folder, relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, folder, relative_path)
    return os.path.join(os.path.abspath(folder), relative_path)

# Python dosyasını çalıştırma fonksiyonu
def run_python_file(file_path):
    subprocess.call(["python", file_path])

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.language = "English"
        self.initUI()

        # Dosya adı ile Example pencerelerini tutacak bir sözlük
        self.example_windows = {}

    def set_volume(self, value):
        pygame.mixer.music.set_volume(value / 100.0)
    
    def initUI(self):
        self.setWindowTitle('Turkish Scrolls Online - Güncelleme Yardımcısı by Balgamov')
        self.setWindowIcon(QIcon(resource_path('SS', 'tso.ico')))

        # Arka plan resmi için QPalette kullan ve resmi genişlet
        palette = QPalette()
        pixmap = QPixmap(resource_path("SS", "arka.png"))
        scaled_pixmap = pixmap.scaled(750, 750, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette.setBrush(QPalette.Background, QBrush(scaled_pixmap))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.music_player_hbox = QHBoxLayout()
        
        # Müzik Çal/Durdur düğmeleri ve şarkı adı etiketi
        self.play_button = QPushButton("Çal", self)
        self.play_button.setFont(QFont('Arial', 10))
        self.play_button.setStyleSheet("background-color: green; color: white;")
        self.play_button.setFixedSize(50, 30)
        self.play_button.clicked.connect(self.play_music)
        self.music_player_hbox.addWidget(self.play_button)

        self.stop_button = QPushButton("Durdur", self)
        self.stop_button.setFont(QFont('Arial', 10))
        self.stop_button.setStyleSheet("background-color: red; color: white;")
        self.stop_button.setFixedSize(50, 30)
        self.stop_button.clicked.connect(self.stop_music)
        self.music_player_hbox.addWidget(self.stop_button)

        self.song_label = QLabel("Şarkı: Secunda - Jeremy Soule (Cover by Rihards Lībietis)", self)
        self.song_label.setFont(QFont('Arial', 10))
        self.song_label.setStyleSheet("color: white;")
        self.music_player_hbox.addWidget(self.song_label)

        # Ses kontrol sliderı
        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setFixedSize(100, 20)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.music_player_hbox.addWidget(self.volume_slider)

        vbox.addLayout(self.music_player_hbox)

        self.files = {
            "English": {
                "ayirma.py": ("en.diff.txt Ayırma", "en.diff.txt dosyasında oyundaki eklenen,silinen ve değiştirilen satırları ayrı dosyalara ayırır ve ID formatını düzenler.", "ayirma.png"),
                "karsilastirmalisilme.py": ("Deleted Silme", "en.diff.txt dosyasında silinen satırları tb.lang.txt ile kıyaslayarak siler.", "karsilassil.png"),
                "changed.py": ("Changed Satır Değiştirme", "Oluşturulan Changed.txt dosyasını kullanımdaki lang.txt dosyası ile karşılaştırarak satırları değiştirir.", "changed.png"),
                "idekle.py": ("ID Ekle", "ID'si bulunmayan, çevirisi yapılmış satırların başına tekrar ID eklemek için kullanılır.", "idekle.png"),
                "Idsilme.py": ("ID Silme", "Satırların başındaki ID'leri siler.", "idsil.png"),
                "sadeceid.py": ("Sadece ID Kaydetme", "Sadece satırların başındaki ID'leri kaydeder. Devamını siler.", "sadeceid.png"),
                "birlestir.py": ("Yeni Satırları Ekle", "en.diff.txt'de belirtilmiş, güncelleme ile oyuna yeni eklenen satırları tb.lang.txt ile birleştirir ve sıralar.", "yeniekle.png"),
                "clientpre.py": ("Client ve Pregame", "Client ve pregame .lua dosyalarındaki yeni eklenmiş satırları .str dosyası ile karşılaştırır ve yeni dosyalar oluşturur.", "clipre.png")
            },
            "Türkçe": {
                "ayirma.py": ("Separate en.diff.txt", "Separates the added, deleted and changed lines in the en.diff.txt file into separate files and adjusts the ID format.", "ayirmaEN.png"),
                "karsilastirmalisilme.py": ("Remove from Original", "Compares the lines deleted in the en.diff.txt file with tb.lang.txt and deletes them.", "karsilassilEN.png"),
                "changed.py": ("Changed Line Replacement", "Replaces lines by comparing the generated Changed.txt file with the lang.txt file in use.", "changedEN.png"),
                "idekle.py": ("Add ID", "Used to re-add the ID to the beginning of the translated lines that do not have an ID.", "idekleEN.png"),
                "Idsilme.py": ("Remove ID", "Deletes the IDs at the beginning of the lines.", "idsilEN.png"),
                "sadeceid.py": ("Save Only ID", "Only saves the IDs at the beginning of the lines. Deletes the rest.", "sadeceidEN.png"),
                "birlestir.py": ("Add New Lines", "Combines and sorts the new lines added to the game with the update, specified in en.diff.txt, with tb.lang.txt.", "yeniekleEN.png"),
                "clientpre.py": ("Client ve Pregame", "It compares the newly added lines in the client and pregame .lua files with the .str file and creates new files.", "clipreEN.png")
            }
        }

        self.language_button = QPushButton(self.language, self)
        self.language_button.setFixedSize(70, 40)
        self.language_button.setStyleSheet("background-color: lightblue; color: darkred;")
        self.language_button.clicked.connect(self.switch_language)
        vbox.addWidget(self.language_button)

        self.file_buttons = []
        self.file_labels = []
        self.example_buttons = []
        button_width = 180
        button_height = 35

        for i, (file, (title, description, image)) in enumerate(self.files[self.language].items()):
            full_path = resource_path("Programlar", file)
            hbox = QHBoxLayout()

            button = QPushButton(title, self)
            button.setFont(QFont('Arial', 10, QFont.Bold))
            button.setStyleSheet("background-color: darkred; color: white;")
            button.setFixedSize(button_width, button_height)
            button.clicked.connect(lambda checked, full_path=full_path: run_python_file(full_path))
            hbox.addWidget(button)
            self.file_buttons.append(button)

            label = QLabel(description, self)
            label.setFont(QFont('Arial', 10))
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("QLabel { background-color : rgba(255, 255, 255, 100); border-radius: 10px; padding: 5px; }")
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hbox.addWidget(label)
            self.file_labels.append(label)

            example_button = QPushButton("Örnek" if self.language == "English" else "Example", self)
            example_button.setFont(QFont('Arial', 10))
            example_button.setStyleSheet("color: darkred;")
            example_button.setFixedSize(button_width, button_height)
            example_button.clicked.connect(lambda checked, image=resource_path("SS", image): self.show_example(image))
            hbox.addWidget(example_button)
            self.example_buttons.append(example_button)

            vbox.addLayout(hbox)

        self.resize(750, 750)
        self.center()

        self.show()

        self.play_music()

    def resizeEvent(self, event):
        pixmap = QPixmap(resource_path("SS", "arka.png"))
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Background, QBrush(scaled_pixmap))
        self.setPalette(palette)

    def switch_language(self):
        self.language = "Türkçe" if self.language == "English" else "English"
        self.language_button.setText(self.language)
        self.play_button.setText("Çal" if self.language == "English" else "Play")
        self.stop_button.setText("Durdur" if self.language == "English" else "Stop")
        
        # Dosya listesini güncelle
        files = self.files[self.language]
        for i, (file, (title, description, image)) in enumerate(files.items()):
            self.file_buttons[i].setText(title)
            self.file_labels[i].setText(description)
            self.example_buttons[i].setText("Örnek" if self.language == "English" else "Example")

            # Dil değiştiğinde Example penceresini güncelle
            if file in self.example_windows:
                self.example_windows[file].update_image(resource_path("SS", image))

    def show_example(self, image_path):
        file_name = os.path.basename(image_path)

        # Eğer Example penceresi zaten açıksa kapatın
        if file_name in self.example_windows:
            self.example_windows[file_name].close()

        # Yeni bir Example penceresi oluşturun ve sözlüğe ekleyin
        self.example_windows[file_name] = Example(image_path, self.language)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    

    def play_music(self):
        pygame.mixer.music.load(resource_path("SS", "sarki.mp3"))
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

class Example(QWidget):
    def __init__(self, image_path, language):
        super().__init__()
        self.language = language
        self.initUI(image_path)

    def initUI(self, image_path):
        hbox = QVBoxLayout(self)
        pixmap_path = f"{os.path.splitext(image_path)[0]}{'' if self.language == 'English' else 'EN'}.png"
        pixmap = QPixmap(resource_path("SS", pixmap_path))

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Örnek')
        self.show()

    def update_image(self, image_path):
        pixmap_path = f"{os.path.splitext(image_path)[0]}{'' if self.language == 'English' else 'EN'}.png"
        pixmap = QPixmap(resource_path("SS", pixmap_path))
        lbl = self.findChild(QLabel)  # Var olan QLabel'i bulun
        if lbl:
            lbl.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
