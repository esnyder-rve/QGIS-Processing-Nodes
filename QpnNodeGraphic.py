from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem, QStyleOptionGraphicsItem
from PyQt5.QtGui import QColor, QFont, QPainter, QPainterPath, QPen, QBrush
from PyQt5.QtCore import Qt, QRectF

from QpnSettings import QpnSettings

class QpnNodeGraphic(QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)
        self.node = node

        # UI Elements
        self._title_item = QGraphicsTextItem(self)

        # TODO: make these dynamic
        self.width = 180
        self.height = 240
        self.title_height = 24

        self._padding = 5

        self._pen_default = QPen(QColor(QpnSettings.NodeOutlineColor))
        self._pen_default.setWidth(QpnSettings.NodeOutlineWidth)

        self._pen_selected = QPen(QColor(QpnSettings.NodeOutlineSelectionColor))
        self._pen_selected.setWidth(QpnSettings.NodeOutlineWidth)

        self._brush_title = QBrush(QColor(QpnSettings.NodeTitleBackgroundColor))
        self._brush_background = QBrush(QColor(QpnSettings.NodeContentBackgroundColor))

        # Initialize the UI
        self.InitUI(self.node.title)

    def InitUI(self, title):
        self.setFlag(QGraphicsTextItem.ItemIsSelectable)
        self.setFlag(QGraphicsTextItem.ItemIsMovable)
        self._title_item.setDefaultTextColor(QColor(QpnSettings.NodeTitleTextColor))
        self._title_item.setFont(QFont(QpnSettings.NodeTitleFont, QpnSettings.NodeTitleFontSize))
        self.title = title
        self._title_item.setPos(self._padding, 0)
        self._title_item.setTextWidth(self.width - 2 * self._padding)
    
    @property
    def title(self): return self._title
    @title.setter
    def title(self, value):
        self._title = value
        self._title_item.setPlainText(self._title)


    def boundingRect(self):
        return QRectF(0, 0, 2 * QpnSettings.NodeEdgeRoundness + self.width, 2 * QpnSettings.NodeEdgeRoundness + self.height).normalized()

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget=None):
        # Title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self.title_height, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_title.addRect(0, self.title_height - QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_title.addRect(self.width - QpnSettings.NodeEdgeRoundness, self.title_height - QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        # Content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.title_height, self.width, self.height - self.title_height, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_content.addRect(0, self.title_height, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_content.addRect(self.width - QpnSettings.NodeEdgeRoundness, self.title_height, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

        # Outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0, 0, self.width, self.height, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
