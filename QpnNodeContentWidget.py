from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QColor

from QpnSettings import QpnSettings

class QpnNodeContentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(QpnSettings.NodeContentBackgroundColor))
        self.setPalette(palette)
        self._count = 0
        self.setFixedSize(0, 0)


    def AddWidget(self, widget: QWidget, newWidth: int):
        widget.setUpdatesEnabled(True)
        self.layout.addWidget(widget)
        # self.setFixedSize(int(newWidth), int(self.height() + widget.height()))
        self.setFixedSize(int(newWidth), int(self.height() + widget.sizeHint().height()))
        self._count += 1
        return self.height() - (widget.sizeHint().height()/2)


    def getMinWidth(self):
        minWidth = 0
        for i in range(self._count):
            pass


    def count(self) -> int:
        return self._count
