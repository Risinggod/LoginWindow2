from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Text für die Titelleiste des QMainWinows
        self.setWindowTitle("Einführung ins QMainWindow")

        # Setzt die Größe des Fensters auf feste Werte
        # self.setFixedWidth(800)
        # self.setFixedHeight(600)

       # self.setMinimumWidth(200)
        #self.setMinimumHeight(200)

       # self.setMaximumWidth(200)
       # self.setMaximumHeight(200)

        central_widget = CentralWidget(self)
        self.setCentralWidget(central_widget)
