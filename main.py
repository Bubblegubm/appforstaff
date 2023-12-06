import os
import sys
import atexit
from PySide6.QtCore import QCoreApplication,QTimer
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from PySide6.QtWidgets import QApplication
from widgets_classes import Window
from connection import Data
from time import sleep


data = Data()

def update_database_on_exit():
    data.save_data_to_database()
    data.commit_and_close()

    # Создаем таймер для обработки событий
    timer = QTimer()
    timer.start(5000000)  # Устанавливаем интервал в 100 мс (можно настроить)

    # Определяем функцию, которая будет вызываться при каждом тике таймера
    def handle_events():
        QCoreApplication.sendPostedEvents()
        QCoreApplication.processEvents()

    # Подключаем функцию к сигналу таймера
    timer.timeout.connect(handle_events)

    # Запускаем таймер
    timer.start()

    # Проверка, завершились ли все запросы
    while data.db.isOpen() and data.db.transaction():
        QCoreApplication.processEvents()

    # Закрываем соединение
    data.db.removeDatabase('qt_sql_default_connection')

    # Останавливаем таймер
    timer.stop()


@atexit.register
def on_exit():
    update_database_on_exit()
    # Явно удаляем соединение с базой данных
    data.db.removeDatabase('qt_sql_default_connection')
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
    #db_path = os.path.join(exe_dir, 'app_db.db')

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(image_path))

    QFontDatabase.addApplicationFont(font_path)

    window = Window()
    window.setWindowTitle('ServeSmart')
    window.show()

    app.aboutToQuit.connect(update_database_on_exit)

    sys.exit(app.exec())
