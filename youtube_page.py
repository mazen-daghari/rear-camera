from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class YouTubePage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.back_button = QPushButton('Back to Home', self)
        self.back_button.setFixedSize(100, 20)
        self.back_button.clicked.connect(parent.go_home)

        button_layout_youtube = QHBoxLayout()
        button_layout_youtube.addWidget(self.back_button)

        layout_youtube = QVBoxLayout(self)
        layout_youtube.addLayout(button_layout_youtube)

        self.youtube_view = QWebEngineView(self)
        self.youtube_view.setFixedSize(820, 580)
        self.youtube_view.setUrl(QUrl("https://www.youtube.com"))
        layout_youtube.addWidget(self.youtube_view)
