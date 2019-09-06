#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # アプリケーション画面のためのオブジェクト作成
        grid = QGridLayout()
        self.setLayout(grid)

        # ボタンのラベル
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        # ボタンの位置設定
        positions = [(i,j) for i in range(5) for j in range(4)]

        # ボタンを画面に追加
        for position, name in zip(positions, names):

            # ボタンのラベルがない要素はとばす
            if name == '':
                continue
            # ボタンのラベルを設定
            button = QPushButton(name)
            # *positionの位置にボタンを配置
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
