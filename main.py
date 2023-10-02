import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow

from entrance import Ui_MainWindow

class ServeSmart(QMainWindow):
    def __init__(self):
        super(ServeSmart, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServeSmart()
    window.show()

    sys.exit(app.exec())