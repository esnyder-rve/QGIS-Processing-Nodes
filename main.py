from PyQt5.QtWidgets import QApplication
from QpnMainWindow import QpnMainWindow
import sys

def main(argv):
    app = QApplication(argv)
    mw = QpnMainWindow()
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)
