from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QPixmap

class WeatherPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.back_label = QLabel(self)
        self.back_label.setFixedSize(50, 50)  # Taille de l'image du bouton Home
        self.back_label.setPixmap(QPixmap("home-button.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.back_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_label.mousePressEvent = lambda event: parent.go_home()

        button_layout_weather = QHBoxLayout()
        button_layout_weather.addWidget(self.back_label)

        layout_weather = QVBoxLayout(self)
        layout_weather.addLayout(button_layout_weather)

        self.weather_view = QWebEngineView(self)
        self.weather_view.setFixedSize(820, 580)
        self.weather_view.setUrl(QUrl("https://www.weather.com"))  # Utiliser un site de météo
        layout_weather.addWidget(self.weather_view)

        self.setLayout(layout_weather)
