import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
from widgets_classes import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec())
