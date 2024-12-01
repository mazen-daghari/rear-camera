from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView

class HomePage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.start_label = QLabel(self)
        self.start_label.setFixedSize(50, 50)
        self.start_label.setPixmap(QPixmap("camera (1).png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.start_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_label.mousePressEvent = lambda event: parent.start_system()

        self.spotify_label = QLabel(self)
        self.spotify_label.setFixedSize(50, 50)
        self.spotify_label.setPixmap(QPixmap("spotify.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.spotify_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spotify_label.mousePressEvent = lambda event: parent.go_spotify()

        self.radio_label = QLabel(self)
        self.radio_label.setFixedSize(50, 50)
        self.radio_label.setPixmap(QPixmap("radio.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.radio_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.radio_label.mousePressEvent = lambda event: parent.go_radio()

        self.dashboard_label = QLabel(self)
        self.dashboard_label.setFixedSize(50, 50)
        self.dashboard_label.setPixmap(QPixmap("dashboard.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.dashboard_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dashboard_label.mousePressEvent = lambda event: parent.go_dashboard()

        self.weather_label = QLabel(self)
        self.weather_label.setFixedSize(50, 50)
        self.weather_label.setPixmap(QPixmap("cloudy.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.weather_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weather_label.mousePressEvent = lambda event: parent.go_weather()

        button_layout_home = QHBoxLayout()
        button_layout_home.addWidget(self.start_label)
        button_layout_home.addWidget(self.spotify_label)
        button_layout_home.addWidget(self.radio_label)
        button_layout_home.addWidget(self.dashboard_label)
        button_layout_home.addWidget(self.weather_label)

        layout_home = QVBoxLayout(self)
        layout_home.addLayout(button_layout_home)

        self.map_view = QWebEngineView(self)
        self.map_view.setFixedSize(820, 580)
        self.map_view.setUrl(QUrl("https://www.google.com/maps"))
        layout_home.addWidget(self.map_view)
