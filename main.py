from PyQt6.QtWidgets import QApplication
import sys
from camera_system import CameraSystem

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CameraSystem()
    ex.show()
    sys.exit(app.exec())
