from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
import random
import sys

class SayıTahminOyunu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sayı Tahmin Oyunu")
        self.resize(450, 220)

        # Tema
        style = """
        QWidget {
            background-color: #f0f4fb;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            color: #1a1a1a;
        }
        QLabel {
            font-weight: bold;
        }
        QLineEdit {
            border: 1.5px solid #6b08db;
            border-radius: 6px;
            padding: 6px;
            background-color: white;
            color: #333333;
            font-size: 14px;
        }
        QPushButton {
            background-color: #6b08db;
            border: none;
            color: white;
            padding: 10px 18px;
            font-weight: bold;
            border-radius: 8px;
            margin: 4px 2px;
        }
        QPushButton:hover {
            background-color: #5206a5;
        }
        """
        self.setStyleSheet(style)

        self.hedef_sayi = random.randint(1, 100)
        self.tahmin_sayisi = 0

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.info_label = QLabel("1 ile 100 arasında bir sayı tuttum. Tahminini gir ve ‘Tahmin Et’ butonuna bas!")
        self.layout.addWidget(self.info_label)

        input_layout = QHBoxLayout()
        self.tahmin_input = QLineEdit()
        self.tahmin_input.setPlaceholderText("Tahmininizi buraya yazın")
        self.tahmin_input.setMaxLength(3)
        self.tahmin_input.returnPressed.connect(self.tahmin_et)  # Enter tuşu ile de tahmin edilebilir
        input_layout.addWidget(self.tahmin_input)

        self.tahmin_button = QPushButton("Tahmin Et")
        self.tahmin_button.clicked.connect(self.tahmin_et)
        input_layout.addWidget(self.tahmin_button)

        self.layout.addLayout(input_layout)

        self.sonuc_label = QLabel("")
        self.layout.addWidget(self.sonuc_label)

        self.deneme_label = QLabel("Deneme sayısı: 0")
        self.layout.addWidget(self.deneme_label)

        self.yeniden_button = QPushButton("Yeniden Başlat")
        self.yeniden_button.clicked.connect(self.yeniden_baslat)
        self.yeniden_button.setVisible(False)
        self.layout.addWidget(self.yeniden_button)

    def tahmin_et(self):
        tahmin_metni = self.tahmin_input.text().strip()
        if not tahmin_metni.isdigit():
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı giriniz.")
            self.tahmin_input.clear()
            self.tahmin_input.setFocus()
            return

        tahmin = int(tahmin_metni)
        if tahmin < 1 or tahmin > 100:
            QMessageBox.warning(self, "Hata", "Lütfen 1 ile 100 arasında bir sayı giriniz.")
            self.tahmin_input.clear()
            self.tahmin_input.setFocus()
            return

        self.tahmin_sayisi += 1
        self.deneme_label.setText(f"Deneme sayısı: {self.tahmin_sayisi}")

        if tahmin < self.hedef_sayi:
            self.sonuc_label.setText("Daha büyük sayı deneyin.")
            self.sonuc_label.setStyleSheet("color: red; font-weight: bold;")
            self.tahmin_input.clear()
            self.tahmin_input.setFocus()
        elif tahmin > self.hedef_sayi:
            self.sonuc_label.setText("Daha küçük sayı deneyin.")
            self.sonuc_label.setStyleSheet("color: red; font-weight: bold;")
            self.tahmin_input.clear()
            self.tahmin_input.setFocus()
        else:
            self.sonuc_label.setText(f"Tebrikler! {self.tahmin_sayisi}. denemede buldunuz.")
            self.sonuc_label.setStyleSheet("color: green; font-weight: bold;")
            self.tahmin_button.setEnabled(False)
            self.tahmin_input.setEnabled(False)
            self.yeniden_button.setVisible(True)

    def yeniden_baslat(self):
        self.hedef_sayi = random.randint(1, 100)
        self.tahmin_sayisi = 0
        self.sonuc_label.setText("")
        self.sonuc_label.setStyleSheet("")
        self.deneme_label.setText("Deneme sayısı: 0")
        self.tahmin_input.setText("")
        self.tahmin_button.setEnabled(True)
        self.tahmin_input.setEnabled(True)
        self.yeniden_button.setVisible(False)
        self.tahmin_input.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = SayıTahminOyunu()
    pencere.show()
    sys.exit(app.exec())
