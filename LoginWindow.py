from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class LoginWindow(QWidget):
    """A Login Window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Please Login")
        self.MainLayout()
        self.setFixedSize(425,225)
        

    def MainLayout(self):
        self.horizontal1 = QHBoxLayout()
        self.horizontal2 = QHBoxLayout()
        self.horizontal3 = QHBoxLayout()
        self.horizontal4 = QHBoxLayout()
        self.horizontal5 = QHBoxLayout()
        self.verticle = QVBoxLayout()

        LoginLbl = QLabel("~ PLEASE LOG IN ~")
        LoginLbl.setFont(QFont("Georgia",18))

        username = QLineEdit()
        username.setPlaceholderText("Username")
        username.setValidator(QIntValidator(0,99999))
        username.setFixedWidth(250)
        username.setFixedHeight(30)

        username.textChanged.connect(self.UsernameValidation)
        
        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)
        password.setFixedWidth(250)
        password.setFixedHeight(30)
        
        LoginBtn = QPushButton("Log In")
        LoginBtn.setStyleSheet('QPushButton {background-color: #A787FF; color: black; border: 2px solid black}'
                               'QPushButton {border-radius: 4px}'
                               'QPushButton:pressed{background-color: #D0BFFF; border: 2px solid grey}')
        LoginBtn.setFixedWidth(100)
        LoginBtn.setFixedHeight(30)

        self.ValidationLbl = QLabel("Your username should be 5 digits long")

        self.tick = QLabel()
        self.pixmap = QPixmap("Valid.png")
        self.tick.setPixmap(self.pixmap)
        self.tick.setVisible(False)

        self.blanklbl = QLabel("     ")
        self.blanklbl.setVisible(False)

        self.horizontal1.addStretch(1)
        self.horizontal1.addWidget(LoginLbl)
        self.horizontal1.addStretch(1)

        self.horizontal2.addStretch(1)
        self.horizontal2.addWidget(self.blanklbl)
        self.horizontal2.addWidget(username)
        self.horizontal2.addWidget(self.tick)
        self.horizontal2.addStretch(1)
        
        self.horizontal3.addStretch(1)
        self.horizontal3.addWidget(password)
        self.horizontal3.addStretch(1)
        
        self.horizontal4.addStretch(1)
        self.horizontal4.addWidget(LoginBtn)
        self.horizontal4.addStretch(1)

        self.horizontal5.addStretch(1)
        self.horizontal5.addWidget(self.ValidationLbl)
        self.ValidationLbl.setVisible(False)
        self.horizontal5.addStretch(1)
        
        self.verticle.addLayout(self.horizontal1)
        self.verticle.addStretch(1)
        self.verticle.addLayout(self.horizontal5)
        self.verticle.addLayout(self.horizontal2)
        self.verticle.addLayout(self.horizontal3)
        self.verticle.addStretch(1)
        self.verticle.addLayout(self.horizontal4)

        self.setLayout(self.verticle)

    def UsernameValidation(self,text):
        if len(text) != 5:
            self.ValidationLbl.setVisible(True)
            self.tick.setVisible(False)
            self.blanklbl.setVisible(False)
        else:
            self.ValidationLbl.setVisible(False)
            self.tick.setVisible(True)
            self.blanklbl.setVisible(True)

    def PasswordValidation(self,text):
        pass
        
def main():
    App = QApplication(sys.argv)
    launcher = LoginWindow()
    launcher.show()
    launcher.raise_()
    App.exec_()

if __name__ == "__main__":
    main()
