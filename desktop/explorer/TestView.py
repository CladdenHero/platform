from PySide6.QtWidgets import QListView, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QModelIndex
import os
import sqlite3


class TestView(QWidget):
    def __init__(self):
        super().__init__()

        conn = sqlite3.connect('D:/1WORK/platform/learning_platform/db.sqlite3')
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM tests_true_test')

        self.listView = QListView(self)
        self.listView.setEditTriggers(QListView.NoEditTriggers)

        self.model = QStandardItemModel()

        values = ['ich', 'ni', 'san']
        for i in values:
            self.model.appendRow(QStandardItem(i))

        self.listView.setModel(self.model)
        self.listView.setObjectName('tests')
