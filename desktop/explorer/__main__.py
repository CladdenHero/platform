from Application import Application
from MainWindow import MainWindow
import sys


app = Application(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()
