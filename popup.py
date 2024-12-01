from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap

class Popup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.text_label = QLabel("Welcome to the Rear Camera System!", self)
        layout.addWidget(self.text_label)

        self.image_label = QLabel(self)
        pixmap = QPixmap("Mazenkovic.png")  # Remplacer par le chemin de votre image
        pixmap = pixmap.scaled(270, 236)
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)
