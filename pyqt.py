import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUI = 'D:/pyqt/ui/text.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        self.lineEdit = QLineEdit(self)
        self.pushButton = QPushButton(self)
        self.pushButton.move(0,100)

app = QApplication(sys.argv)  # 여기서 부터 ~ app.exec_() 사이에 실제 실행(이벤트루프)될 코드가 나온다
main_dialog = MainDialog()
main_dialog.show()   
app.exec_() # 프로그램을 이벤트 루프로 집입 시키는 메소드 - window 프로그램 트징
            # 이벤트 루프 : 프로그램이 종료되지 않고 다음 명령(이벤트)를 대기하는 상태