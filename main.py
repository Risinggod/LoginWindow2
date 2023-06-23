from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

# All you need is https://doc.qt.io/qtforpython-6/

# line edits, https://github.com/chey00/lineedits/ , https://doc.qt.io/qt-6/qlineedit.html#inputMask-prop

# Login_fenster https://github.com/chey00/login/

#Taschenrechner  https://github.com/chey00/calc/

#drawing https://github.com/chey00/drawing/




if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    application.exec()