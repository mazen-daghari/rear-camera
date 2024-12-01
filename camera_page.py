from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QStackedLayout
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import cv2
import numpy as np
import threading
import winsound

class CameraPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(800, 600)  # Taille fixe de la caméra
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.home_image_label = QLabel(self)
        self.home_image_label.setFixedSize(50, 50)  # Taille de l'image du bouton Home
        self.home_image_label.setPixmap(QPixmap("home-button.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))  # Remplacer par le chemin de votre image
        self.home_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.home_image_label.mousePressEvent = lambda event: parent.go_home()

        self.warning_label = QLabel(self)
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setStyleSheet("color: red; font-size: 16px;")  # Style du message d'avertissement

        self.distance_label = QLabel(self)
        self.distance_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.distance_label.setStyleSheet("color: white; font-size: 16px;")  # Style du texte de la distance

        layout_camera = QStackedLayout()
        layout_camera.addWidget(self.image_label)
        layout_camera.addWidget(self.warning_label)
        layout_camera.addWidget(self.distance_label)
        layout_camera.setAlignment(self.warning_label, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout_camera.setAlignment(self.distance_label, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout_camera)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.home_image_label)
        bottom_layout.addStretch()
        bottom_layout.setAlignment(self.home_image_label, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def update_frame(self, frame, distance):
        screen_width = 800  # Largeur fixe de la caméra
        screen_height = 600  # Hauteur fixe de la caméra
        road_curvature = 1

        frame = cv2.resize(frame, (screen_width, screen_height))

        if distance < 50:
            line_color = (255, 0, 0)
            message = "Warning: Too Close!"
            frequency = 1000 + (50 - distance) * 20
            if not hasattr(self, 'beep_thread') or not self.beep_thread.is_alive():
                self.beep_thread = threading.Thread(target=self.play_beep, args=(frequency,))
                self.beep_thread.start()
        else:
            line_color = (0, 255, 0)
            message = ""
            if hasattr(self, 'beep_thread') and self.beep_thread.is_alive():
                self.beep_thread.do_run = False
                self.beep_thread.join()

        line_thickness = 2

        for i in range(1, 6):
            pts = np.array([
                [screen_width // 2 - i * 50 + road_curvature, screen_height],
                [screen_width // 2 - i * 25 + road_curvature, screen_height // 2],
                [screen_width // 2 + i * 25 + road_curvature, screen_height // 2],
                [screen_width // 2 + i * 50 + road_curvature, screen_height]
            ], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], isClosed=False, color=line_color, thickness=line_thickness)

        if message:
            self.warning_label.setText(message)
        else:
            self.warning_label.setText("")

        self.distance_label.setText(f"Distance: {distance} cm")

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)

        self.image_label.setPixmap(pixmap)

    def play_beep(self, frequency):
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            winsound.Beep(frequency, 100)
