from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from functools import partial

class LoginForm(QDialog):
    def __init__(self, parent, ipaddr):
        super(LoginForm, self).__init__(parent)
        self.setWindowTitle('device ip adress is '+ipaddr)
        self.resize(300, 120)
        self.setLayout(QVBoxLayout())

        self.label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter the device username')
        self.layout().addWidget(self.label_name)
        self.layout().addWidget(self.lineEdit_username)
        self.label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter the devic password')
        self.layout().addWidget(self.label_password)
        self.layout().addWidget(self.lineEdit_password)

        button = QPushButton(self)
        button.setText('Confirm')
        button.clicked.connect(partial(self.confirm, parent)) #using partial to make a slot alog with parameters
        self.layout().addWidget(button)
        self.setModal(True)
        self.exec_()  #  Use exec if you want to really want to create modal dialog

    def confirm(self,parent):
        self.accept() #instead of close use its accept feature
        self.user = self.lineEdit_username.text()
        self.password = self.lineEdit_password.text()
        self.boolean = True
        #parent.label.setText(user)  # acessing DialogClass object that you passed  while calling show modal
        #print('entered value: %s' % password)


