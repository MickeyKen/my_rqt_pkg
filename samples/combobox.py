#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # ラベル作成、初期の名前をUbuntuにする
        self.lbl = QLabel("Motion", self)

        # QComboBoxオブジェクトの作成
        combo = QComboBox(self)
        # アイテムの名前設定
        combo.addItem("acceleration")
        combo.addItem("forward")
        combo.addItem("rotation")
        combo.addItem("turning")
        combo.addItem("pause")
        combo.addItem("stop")
        combo.addItem("slowstop")
        combo.addItem("detect")
        combo.addItem("e")
        combo.addItem("end")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        # アイテムが選択されたらonActivated関数の呼び出し
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()


    def onActivated(self, text):

        # ラベルに選択されたアイテムの名前を設定
        self.lbl.setText(text)
        # ラベルの長さを調整
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
