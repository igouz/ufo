import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__();
        self.initUI()

    def initUI(self):
        self.resize(480,320)
        self.center()
        self.setWindowTitle("测试Pyqt5")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        reply = QMessageBox.question(self,
                                     "message","are you sure to quit"
                                     ,QMessageBox.Yes | QMessageBox.No,QMessageBox.No);
        if (reply == QMessageBox.Yes):
            event.accept();
        else:
            event.ignore()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example();

    sys.exit(app.exec_())