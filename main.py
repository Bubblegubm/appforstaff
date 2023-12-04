import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from widgets_classes import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('apple-icon-152x152.png'))
    window = Window()
    window.setWindowTitle('ServeSmart')
    window.show()

    sys.exit(app.exec())
