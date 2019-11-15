import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  # QApplication 인스턴스 생성
print(sys.argv)
label = QLabel("Hello PyQt")
label.show()

app.exec_()  # event loop (무한 루프)
