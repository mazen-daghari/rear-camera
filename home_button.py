from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class HomeButton(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(50, 50)  # Taille de l'image du bouton Home
        self.setPixmap(QPixmap("home.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mousePressEvent = lambda event: parent.go_home()
