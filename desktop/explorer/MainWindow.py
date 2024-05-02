from PySide6.QtWidgets import QMainWindow
from FileExplorer import FileExplorer
from TestView import TestView


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(100, 100, 600, 600)

        fe = FileExplorer()
        tv = TestView()

        self.setCentralWidget(tv)
