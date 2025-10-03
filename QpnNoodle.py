from QpnSocket import QpnSocket
from PyQt5.QtWidgets import QGraphicsPathItem, QGraphicsItem
from PyQt5.QtGui import QPainter, QPen, QColor, QPainterPath
from PyQt5.QtCore import Qt, QPointF

class QpnNoodle(QGraphicsPathItem):
    def __init__(self, scene, start_socket: QpnSocket, end_socket: QpnSocket, parent=None):
        super().__init__(parent)
        self._scene = scene
        self._start_socket = start_socket
        self._end_socket = end_socket
        self._noodle_path = QPainterPath()
        
        self._pen = QPen(QColor('#FF0000FF'))
        self._pen.setWidth(2)

        self._pen_selected = QPen(QColor('#FF00FF00'))
        self._pen_selected.setWidth(2)

        self.setFlag(QGraphicsItem.ItemIsSelectable)

        # Set draw order to behind the nodes (which are at z-level 0)
        self.setZValue(-1)


    def updatePath(self):
        self._noodle_path.clear()
        self._noodle_path.moveTo(QPointF(0, 0))
        self._noodle_path.cubicTo(100, 0, 100, 100, 200, 100)
        self.setPath(self._noodle_path)


    def paint(self, painter, option, widget):
        self.updatePath()
        painter.setPen(self._pen_selected if self.isSelected() else self._pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(self.path())
