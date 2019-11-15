import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


# .py 직접 실행하면 실행됨 / 다른 인터프리터에서 import 하는 경우에는 실행되지 않음
# __name__ : 현재 모듈 이름을 저장 (프로그램이 직접 실행되는지 모듈을 통해 실행되는지 확인)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())