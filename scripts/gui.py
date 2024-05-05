import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QFrame, QVBoxLayout, QApplication, QGridLayout
from PyQt5.QtCore import Qt


class Windows(QWidget):

    def __init__(self):
        super(Windows, self).__init__()
        self.setObjectName('MainWindow')
        self.setWindowTitle('tic-tac-toe')
        self.setMinimumSize(0, 0)
        self.setMinimumSize(500, 500)
        self.setStyleSheet('#MainWindow {background-color: rgb(0, 100, 200); } \n '
                           '* {color: rgb(0, 0, 0);}')

        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setBold(True)
        font.setPointSize(15)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(self)
        self.frameHeader.setObjectName('frameHeader')

        self.hlayout_header = QVBoxLayout(self.frameHeader)

        self.label_title = QLabel(self.frameHeader)
        self.label_title.setObjectName('lblTitle')
        self.label_title.setFont(font)
        self.label_title.setText('Player 1 Turn!')

        self.hlayout_header.addWidget(self.label_title)

        self.layout.addWidget(self.frameHeader, alignment=Qt.AlignmentFlag.AlignCenter)

        self.frameMain = QFrame(self)
        self.frameMain.setObjectName('frameMain')

        self.layout_main = QGridLayout(self.frameMain)
        self.layout_main.setSpacing(0)
        self.layout_main.setContentsMargins(0, 0, 0, 0)


        for i in range(3):
            for j in range(3):
                btn = QPushButton(self.frameMain)
                btn.setObjectName(f'btn_{i}_{j}')
                font1 = QtGui.QFont()
                font1.setFamily('Arial')
                font1.setBold(True)
                font1.setPointSize(30)
                btn.setFont(font1)
                btn.setText(str(i + j))
                self.layout_main.addWidget(btn, i, j, alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.frameMain)
        self.frameMain.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Windows()
    windows.show()
    sys.exit(app.exec_())
