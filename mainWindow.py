import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import cv2
import configparser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setMinimumSize(QtCore.QSize(1035, 726))
        self.mainWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainWidget.setObjectName("mainWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameLeftBar = QtWidgets.QFrame(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameLeftBar.sizePolicy().hasHeightForWidth())
        self.frameLeftBar.setSizePolicy(sizePolicy)
        self.frameLeftBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLeftBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLeftBar.setObjectName("frameLeftBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameLeftBar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frameLeftBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableParams = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tableParams.sizePolicy().hasHeightForWidth())
        #参数表;
        self.tableParams.setSizePolicy(sizePolicy)
        self.tableParams.setGridStyle(QtCore.Qt.DashLine)
        self.tableParams.setObjectName("tableParams")
        self.verticalLayout_4.addWidget(self.tableParams)
        self.btnExecute = QtWidgets.QPushButton(self.groupBox_3)
        self.btnExecute.setObjectName("btnExecute")
        self.btnExecute.clicked.connect(self.doActionExecute)

        self.verticalLayout_4.addWidget(self.btnExecute)
        self.lb_result = QtWidgets.QLabel(self.groupBox_3)
        self.lb_result.setObjectName("lb_result")

        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frameLeftBar)
        self.frameMain = QtWidgets.QFrame(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameMain.sizePolicy().hasHeightForWidth())
        self.frameMain.setSizePolicy(sizePolicy)
        self.frameMain.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameMain)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.frameMain)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frameMain)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        img = cv2.imread("org.png")  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图


        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)

        img = cv2.imread("deal.png")  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView_2.setScene(self.scene)  # 将场景添加至视图

        self.lbDealPic = QtWidgets.QLabel(self.groupBox_2)
        self.lbDealPic.setText("")
        self.lbDealPic.setObjectName("lbDealPic")
        self.horizontalLayout_3.addWidget(self.lbDealPic)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addWidget(self.frameMain)
        MainWindow.setCentralWidget(self.mainWidget)
        #菜单
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)

        self.menuAbout.setObjectName("menuAbout")
        self.menuAlogi = QtWidgets.QMenu(self.menubar)
        self.menuAlogi.setObjectName("menuAlogi")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("程序已加载完成，请选择一个算法", 0)

        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionalgority = QtWidgets.QAction(MainWindow)
        self.actionalgority.setObjectName("actionalgority")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlogi.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.loadAlgorithmList(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UFOv1.0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "当前算法"))
        self.btnExecute.setText(_translate("MainWindow", "执行算法"))
        self.lb_result.setText(_translate("MainWindow", "-"))
        self.groupBox.setTitle(_translate("MainWindow", "原始图"))
        self.groupBox_2.setTitle(_translate("MainWindow", "结果图"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于"))
        self.menuAlogi.setTitle(_translate("MainWindow", "算法"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionalgority.setText(_translate("MainWindow", "algority"))

    ###读取配置文件的算法;
    def loadAlgorithmList(self,mainWindow):
        path = os.path.abspath(os.curdir)+"\config.ini" #当前目录下的配置文件
        self.config = configparser.ConfigParser()
        self.config.read(path, encoding="utf-8-sig")
        algorithmList = self.config.sections()
        _translate = QtCore.QCoreApplication.translate
        for alg in algorithmList:
            #params = config.items(alg)
            self.algorighmItem = QtWidgets.QAction(mainWindow)
            self.algorighmItem.setText(_translate("MainWindow",alg))
            self.menuAlogi.addAction(self.algorighmItem)


        self.menuAlogi.triggered[QAction].connect(self.addAlgorithParam)

    ###添加参数到参数列表
    def addAlgorithParam(self,q):
        self.alogiName = q.text()
        self.statusbar.showMessage("当前算法："+self.alogiName, 0)
        params = self.config.items(self.alogiName)
        self.tableParams.setColumnCount(2)
        self.tableParams.setRowCount(len(params))
        self.tableParams.setHorizontalHeaderLabels(['参数', '值'])
        index = 0
        for param_item in params:
            newItem = QTableWidgetItem(param_item[0])
            self.tableParams.setItem(index, 0, newItem)
            newItem = QTableWidgetItem(param_item[1])
            self.tableParams.setItem(index, 1, newItem)
            index = index + 1

    def doActionExecute(self):
        print(self.alogiName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    w = Ui_MainWindow()
    w.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())