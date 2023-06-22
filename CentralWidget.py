from PyQt6.QtWidgets import QWidget, QTextBrowser, QGridLayout, QPushButton, QApplication, QLabel, QLineEdit, \
    QMessageBox
from PyQt6.QtCore import pyqtSlot, Qt


class CentralWidget(QWidget):
    def __init__(self, parent=None, QT=None):
        super(CentralWidget, self).__init__(parent)

        #the labels are getting created
        self.user_name_label= QLabel("UserName", self)
        self.passwort_label=QLabel("Passwort", self)


        #the line edits are geting created
        self.user_name_edit = QLineEdit(self)
        self.user_name_edit.setInputMask("A"*6)
        self.passwort_edit = QLineEdit(self)
        self.passwort_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwort_edit.setInputMask("9"*6)

        #the bottens
        self.cancel_button = QPushButton("cancel")
        self.login_button = QPushButton("login")

        self.login_button.clicked.connect(self.the_logic)

        self.cancel_button.clicked.connect(QApplication.instance().quit)



        layout = QGridLayout(self)

        layout.addWidget(self.user_name_label,1,1)
        layout.addWidget(self.user_name_edit,1, 2)
        layout.addWidget(self.passwort_label,2,1)
        layout.addWidget(self.passwort_edit,2, 2)
        layout.addWidget(self.login_button,3, 1)
        layout.addWidget(self.cancel_button, 3, 4)

    @pyqtSlot()
    def the_logic(self):
        if self.user_name_edit.text()=="freddy" and self.passwort_edit.text()=="123456":
            QMessageBox.information(self, "Ergebnis", "Erfolgreicher login"), QApplication.instance().quit()
        else:
           QMessageBox.information(self, "Ergebnis", "Falsche login daten")






