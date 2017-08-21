# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\PyGeoIp.ui'
#
# Created: Sun Jun 18 14:40:39 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import pygeoip, socket

appStyle = """
    #search_btn {
        background-color: rgb(25, 181, 254); 
        color: #fff;
        outline: none;
    }
    #PyGeoIP_Window {
        background-color: rgb(34, 49, 63);
        color: #fff;
    }
    #ip_textbox, #search_list {
        border: 2px solid rgb(25, 181, 254);
        border-radius: 5px;
    }
    #search_list, #ip_textbox {
        background-color: rgb(191, 191, 191);
        color: black;
    }
    #ip_label, #info_bar {
        color: #fff;
        
    }
    #search_list {
        padding-top: 20px;
    }
"""

class Ui_PyGeoIP_Window(object):
    def setupUi(self, PyGeoIP_Window):
        PyGeoIP_Window.setObjectName("PyGeoIP_Window")
        PyGeoIP_Window.resize(429, 471)
        self.centralwidget = QtGui.QWidget(PyGeoIP_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 411, 71))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ip_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.ip_label.setObjectName("ip_label")
        self.horizontalLayout.addWidget(self.ip_label)
        self.ip_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.ip_textbox.setObjectName("ip_textbox")
        self.horizontalLayout.addWidget(self.ip_textbox)
        self.search_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 80, 411, 41))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 0, 271, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.info_bar = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.info_bar.setObjectName("info_bar")
        self.horizontalLayout_2.addWidget(self.info_bar)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 130, 411, 281))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.search_list = QtGui.QListWidget(self.frame_3)
        self.search_list.setGeometry(QtCore.QRect(10, 10, 391, 261))
        self.search_list.setObjectName("search_list")
        PyGeoIP_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyGeoIP_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menubar.setObjectName("menubar")
        PyGeoIP_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyGeoIP_Window)
        self.statusbar.setObjectName("statusbar")
        PyGeoIP_Window.setStatusBar(self.statusbar)

        self.retranslateUi(PyGeoIP_Window)
        QtCore.QMetaObject.connectSlotsByName(PyGeoIP_Window)

        #clicked function
        self.search_btn.clicked.connect(self.search)


    def retranslateUi(self, PyGeoIP_Window):
        PyGeoIP_Window.setWindowTitle(QtGui.QApplication.translate("PyGeoIP_Window", "PyGeoIP", None, QtGui.QApplication.UnicodeUTF8))
        self.ip_label.setText(QtGui.QApplication.translate("PyGeoIP_Window", "IP Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.search_btn.setText(QtGui.QApplication.translate("PyGeoIP_Window", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.info_bar.setText(QtGui.QApplication.translate("PyGeoIP_Window", "Tip: Enter An Address In The TextBox And Click Search", None, QtGui.QApplication.UnicodeUTF8))

    def search(self):
        message = ''
        result_count = 0
        gip = pygeoip.GeoIP("data\\GeoLiteCity.dat")
        ip = self.ip_textbox.text()
        try:
            ip = socket.gethostbyname(str(ip))
            message = "Host: %s is Currently Available" % (str(ip))
        except socket.error as e:
            message = "Host: %s is Currently Unavailable" % (str(ip))

        self.info_bar.setText(message)
        self.search_list.clear()

        try:
            rec = gip.record_by_addr(str(ip))
            for key, val in rec.items():
                self.update_search_list("[*] %s => %s" % (key, val))
                result_count +=1
            self.msg_box("Search Complete", "%d Result Were Found For %s" % (result_count, str(ip)))
        except Exception as e:
            self.msg_box("", str(e))
            self.msg_box("Search Complete", "No Results Were Found For %s" % (str(ip)))
            return

    def msg_box(self, title, message):
        w = QtGui.QWidget()
        QtGui.QMessageBox.information(w, title, message)

    def update_search_list(self, data):
        self.search_list.addItem(data)


if __name__ == "__main__":
    import sys
    import os
    app = QtGui.QApplication(sys.argv)
    PyGeoIP_Window = QtGui.QMainWindow()
    ui = Ui_PyGeoIP_Window()
    ui.setupUi(PyGeoIP_Window)
    PyGeoIP_Window.setStyleSheet(appStyle)
    PyGeoIP_Window.show()
    sys.exit(app.exec_())

