from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QColor

from QpnSettings import QpnSettings

class QpnNodeContentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.InitUI()


    def InitUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(QpnSettings.NodeContentBackgroundColor))
        self.setPalette(palette)

    
    def AddWidget(self, widget: QWidget):
        self.layout.addWidget(widget)
