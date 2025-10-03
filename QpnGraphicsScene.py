import math

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import QRectF, QLine, QEvent

from QpnNode import QpnNode
from QpnNoodle import QpnNoodle

from QpnSettings import QpnSettings

class QpnGraphicsScene(QGraphicsScene):
    # def __init__(self, scene, parent=None):
    def __init__(self, parent=None):
        super(QpnGraphicsScene, self).__init__(parent)
        self._nodes = []
        self._edges = []

        self._scene_height = self._scene_width = QpnSettings.GridSceneSize
        self.SetScene(self._scene_width, self._scene_height)

        # self.scene = scene

        self.minorLinePen = QPen(QColor(QpnSettings.GridColorMinor))
        self.minorLinePen.setWidth(QpnSettings.GridLineWidthMinor)
        self.majorLinePen = QPen(QColor(QpnSettings.GridColorMajor))
        self.majorLinePen.setWidth(QpnSettings.GridLineWidthMajor)

        if QpnSettings.GridColorBackground is not None:
            self.setBackgroundBrush(QColor(QpnSettings.GridColorBackground))


    def SetScene(self, width: int, height: int):
        self.setSceneRect(-width // 2, -height // 2, width, height)


    def drawBackground(self, painter: QPainter, rect: QRectF):
        super(QpnGraphicsScene, self).drawBackground(painter, rect)
        
        if not QpnSettings.GridLinesEnabled:
            return

        viewLeft   = int(math.floor(rect.left()))
        viewRight  = int(math.ceil(rect.right()))
        viewTop    = int(math.floor(rect.top()))
        viewBottom = int(math.ceil(rect.bottom()))

        if QpnSettings.GridLinesMinorEnabled:
            first_left = viewLeft - (viewLeft % QpnSettings.GridSizeMinor)
            first_top = viewTop - (viewTop % QpnSettings.GridSizeMinor)

            lines_minor = []
            
            for x in range(first_left, viewRight, QpnSettings.GridSizeMinor):
                lines_minor.append(QLine(x, viewTop, x, viewBottom))

            for y in range(first_top, viewBottom, QpnSettings.GridSizeMinor):
                lines_minor.append(QLine(viewLeft, y, viewRight, y))

            painter.setPen(self.minorLinePen)
            painter.drawLines(*lines_minor)

        if QpnSettings.GridLinesMajorEnabled:
            first_left = viewLeft - (viewLeft % (QpnSettings.GridSizeMajor * QpnSettings.GridSizeMinor))
            first_top = viewTop - (viewTop % (QpnSettings.GridSizeMajor * QpnSettings.GridSizeMinor))

            lines_major = []
            
            for x in range(first_left, viewRight, QpnSettings.GridSizeMajor * QpnSettings.GridSizeMinor):
                lines_major.append(QLine(x, viewTop, x, viewBottom))

            for y in range(first_top, viewBottom, QpnSettings.GridSizeMajor * QpnSettings.GridSizeMinor):
                lines_major.append(QLine(viewLeft, y, viewRight, y))

            painter.setPen(self.majorLinePen)
            painter.drawLines(*lines_major)


    def contextMenuEvent(self, event:QEvent):
        pass
    

    def AddNode(self, node: QpnNode):
        self._nodes.append(node)
        self.addItem(node)


    def RemoveNode(self, node: QpnNode):
        self._nodes.remove(node)
        self.removeItem(node)


    def AddEdge(self, edge: QpnNoodle):
        self._edges.append(edge)


    def RemoveEdge(self, edge: QpnNoodle):
        self._edges.remove(edge)
