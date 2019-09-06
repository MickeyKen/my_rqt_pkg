# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QTabWidget


class StartMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.button1 = QPushButton('Welcome', self)
        self.button1.move(230, 120)
        self.button1.clicked.connect(self.welcome)
        self.quitbutton1 = QPushButton('exit', self)
        self.quitbutton1.move (230, 200)
        self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    def welcome(self):
        # 0オリジン
        self.master.setCurrentIndex(1)


class WelcomeMenu(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.button2 = QPushButton('Hello', self)
        self.button2.move(230, 120)

        self.quitbutton2 = QPushButton('quit', self)
        self.quitbutton2.move(230, 200)
        self.quitbutton2.clicked.connect(self.quit)

    def quit(self):
        # 項目を引き継ぎたい時とか Sqlite3でも可能
        self.master.piyo_piyo("piyo_piyo")
        self.master.setCurrentIndex(0)


class App(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")
        # 1個1個のタブがメニューに対応
        self.tab1 = StartMenu(self)
        self.tab2 = WelcomeMenu(self)

        # タブページに追加
        self.addTab(self.tab1, "StartMenu")
        self.addTab(self.tab2, "WelcomeMenu")

        # タブパネルのボーダーを削除
        self.setStyleSheet("QTabWidget::pane { border: 0; }")
        # タブバーを非表示に(↓をコメントすると動きがわかりやすくなるかも)
        self.tabBar().hide()
        self.resize(500, 300)
        self.move(100, 0)

    def piyo_piyo(self, text):
        print(text)


def main():
    app = QApplication(sys.argv)
    ex1 = App()
    ex1.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
