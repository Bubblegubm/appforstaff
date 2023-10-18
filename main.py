import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from widgets_classes import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec())
