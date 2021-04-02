# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/2 13:48
@Author  : zyj
'''

import os
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QFileDialog
from ForceBindIP import Ui_MainWindow



class ZSUI(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.pushButton_1.clicked.connect(self.get_guid)
        self.pushButton_3.clicked.connect(self.select_ForceBindIP)
        self.pushButton_4.clicked.connect(self.select_program)
        self.pushButton_2.clicked.connect(self.start)

    def get_guid(self):
        try:
            guid = os.popen("getmac /V /S 127.0.0.1").readlines()
            guid = [i.replace('\n', '') for i in guid][1:]
            guid = '\n'.join(guid)
            self.textBrowser.setText(guid)
        except Exception as e:
            print(e)

    def select_ForceBindIP(self):
        try:
            print('='*30+'加载数据文件'+'='*30)
            fname = QFileDialog.getOpenFileName(self, '选择文件', 'c:/')
            print(fname)
            self.lineEdit_1.setText(fname[0])
        except Exception as e:
            pass

    def select_program(self):
        try:
            print('='*30+'加载数据文件'+'='*30)
            fname = QFileDialog.getOpenFileName(self, '选择文件', 'c:/')
            print(fname)
            self.lineEdit_2.setText(fname[0])
        except Exception as e:
            pass

    def start(self):
        try:
            ForceBindIP_path = self.lineEdit_1.text()
            program = self.lineEdit_2.text()
            ip_guid = self.lineEdit_3.text()

            cmd = "{} {} {}".format(ForceBindIP_path, ip_guid, program)
            print(cmd)
            # os.popen(cmd).readlines()
            os.popen(cmd)

        except Exception as e:
            print(e)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = ZSUI(window)

    window.show()
    app.exit(app.exec_())
