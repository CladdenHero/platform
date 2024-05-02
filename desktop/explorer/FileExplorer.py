from PySide6.QtWidgets import QPushButton, QWidget, QTextEdit, QFileDialog


class FileExplorer(QWidget):

    def __init__(self):
        super().__init__()

        btn = QPushButton('Choose file', self)
        btn.setGeometry(150, 100, 250, 180)
        btn.clicked.connect(self.get_file_name)

        self.txt = QTextEdit(self)
        self.txt.setGeometry(130, 400, 280, 190)

    def get_file_name(self):
        file_filter = 'Data Filter (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select file',
            filter=file_filter
        )
        self.txt.setText(str(response))
