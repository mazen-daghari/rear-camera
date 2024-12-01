from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QPixmap

class SpotifyPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.back_label = QLabel(self)
        self.back_label.setFixedSize(50, 50)  # Taille de l'image du bouton Home
        self.back_label.setPixmap(QPixmap("home-button.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.back_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_label.mousePressEvent = lambda event: parent.go_home()

        button_layout_spotify = QHBoxLayout()
        button_layout_spotify.addWidget(self.back_label)

        layout_spotify = QVBoxLayout(self)
        layout_spotify.addLayout(button_layout_spotify)

        self.spotify_view = QWebEngineView(self)
        self.spotify_view.setFixedSize(820, 580)
        self.spotify_view.setUrl(QUrl("https://open.spotify.com"))
        layout_spotify.addWidget(self.spotify_view)

        self.setLayout(layout_spotify)
