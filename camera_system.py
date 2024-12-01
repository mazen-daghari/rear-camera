import sys
import cv2
import numpy as np
import winsound
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QTimer
from home_page import HomePage
from camera_page import CameraPage
from spotify_page import SpotifyPage
from radio_page import RadioPage
from dashboard_page import DashboardPage
from weather_page import WeatherPage
from popup import Popup  # Importer la fenêtre contextuelle

class CameraSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mazenkovic')
        self.setGeometry(100, 100, 820, 580)

        self.stacked_widget = QStackedWidget(self)

        self.home_page = HomePage(self)
        self.camera_page = CameraPage(self)
        self.spotify_page = SpotifyPage(self)
        self.radio_page = RadioPage(self)
        self.dashboard_page = DashboardPage(self)
        self.weather_page = WeatherPage(self)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.camera_page)
        self.stacked_widget.addWidget(self.spotify_page)
        self.stacked_widget.addWidget(self.radio_page)
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.weather_page)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

        self.system_on = False
        self.cap = None
        self.beep_thread = None
        self.distance = 100  # Initialiser la valeur de distance

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.go_home()

    def start_system(self):
        self.system_on = True
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        self.stacked_widget.setCurrentWidget(self.camera_page)
        self.timer.start(30)  # Limiter la fréquence d'images à ~33 FPS

    def update_frame(self):
        if not self.system_on:
            return

        ret, frame = self.cap.read()

        if not ret:
            print("Error: Could not read frame.")
            return

        frame = cv2.resize(frame, (640, 480))  # Taille de cadre réduite

        # Traiter le cadre (par exemple, dessiner des lignes directrices, ajouter des messages)
        self.camera_page.update_frame(frame, self.distance)

        # Simuler la modification de la distance
        self.distance -= 1
        if self.distance < 0:
            self.distance = 100

    def play_beep(self, frequency):
        while self.system_on:
            winsound.Beep(frequency, 100)

    def go_home(self):
        self.system_on = False
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.camera_page.image_label.clear()
        self.stacked_widget.setCurrentWidget(self.home_page)

    def go_spotify(self):
        self.system_on = False
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.camera_page.image_label.clear()
        self.stacked_widget.setCurrentWidget(self.spotify_page)

    def go_radio(self):
        self.system_on = False
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.camera_page.image_label.clear()
        self.stacked_widget.setCurrentWidget(self.radio_page)

    def go_dashboard(self):
        self.system_on = False
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.camera_page.image_label.clear()
        self.stacked_widget.setCurrentWidget(self.dashboard_page)

    def go_weather(self):
        self.system_on = False
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.camera_page.image_label.clear()
        self.stacked_widget.setCurrentWidget(self.weather_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Afficher la fenêtre contextuelle au démarrage
    popup = Popup()
    if popup.exec() == QDialog.Accepted:
        QTimer.singleShot(10000, lambda: start_camera_system(app))

def start_camera_system(app):
    ex = CameraSystem()
    ex.show()
    sys.exit(app.exec())
