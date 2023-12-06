import os
import sys
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from PySide6.QtWidgets import QApplication
from widgets_classes import Window
from connection import Data

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":

    image_path = resource_path('apple-icon-152x152.png')

    font_path = resource_path('Fonts/ljk_Ambient-Medium.ttf')

    exe_path = sys.executable
    exe_dir = os.path.dirname(exe_path)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(image_path))

    QFontDatabase.addApplicationFont(font_path)

    window = Window()
    window.setWindowTitle('ServeSmart')
    window.show()

    sys.exit(app.exec())
