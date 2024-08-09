# TODO:
# * Fix the positioning of the socket (mainly height)
# * Fix socket constructor to add information such as:
#    * Type
#    * Colors
#    * Shape

from enum import Enum
from PyQt5.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem
from PyQt5.QtGui import QPainterPath, QColor, QPainter, QPen, QBrush, QPolygonF
from PyQt5.QtCore import Qt, QRectF, QPointF


class QpnSocketShapeEnum(Enum):
    INVALID   = 0
    CIRCLE    = 1
    SQUARE    = 2
    DIAMOND   = 3
    RECTANGLE = 4
    OBLONG    = 5
    CUSTOM    = 6


# Class for holding the socket shape
class QpnSocketShape(QPainterPath):
    def __init__(self, parent=None):
        super().__init__()
        self.currentShape = QpnSocketShapeEnum.INVALID
        self.setFillRule(Qt.WindingFill)


    @property
    def outlineWidth(self):
        """The outlineWidth property."""
        return self._outlineWidth
    @outlineWidth.setter
    def outlineWidth(self, value: float):
        if value >= 0:
            self._outlineWidth = value


    @classmethod
    def Circle(cls, radius: int):
        newShape = cls()
        newShape.addEllipse(-radius, -radius, 2 * radius, 2 * radius)
        newShape.currentShape = QpnSocketShapeEnum.CIRCLE
        return newShape


    @classmethod
    def Square(cls, width: int):
        newShape = cls()
        newShape.addRect(-width // 2, -width // 2, width, width)
        newShape.currentShape = QpnSocketShapeEnum.SQUARE
        return newShape


    @classmethod
    def Diamond(cls, width: int):
        newShape = cls()
        # Need to make custom shape, as paths cannot be rotated :(
        newShape.addPolygon(QPolygonF([
            QPointF(-width // 2, 0), 
            QPointF(0, -width // 2), 
            QPointF(width // 2, 0),
            QPointF(0, width // 2),
            QPointF(-width // 2, 0)]))
        newShape.currentShape = QpnSocketShapeEnum.DIAMOND
        return newShape


    @classmethod
    def Rectangle(cls, width: int, height: int):
        newShape = cls()
        newShape.addRect(-width // 2, -height // 2, width, height)
        newShape.currentShape = QpnSocketShapeEnum.RECTANGLE
        return newShape


    @classmethod
    def OblongCircle(cls, width: int, height: int):
        newShape = cls()
        # Use RoundedRect() and set the radius to 1/2 the width
        newShape.addRoundedRect(-width // 2, -height // 2, width, height, width // 2, width // 2)
        newShape.currentShape = QpnSocketShapeEnum.OBLONG
        return newShape


    @classmethod
    def CustomShape(cls, path: QPainterPath):
        newShape = cls()
        newShape.addPath(path)
        newShape.currentShape = QpnSocketShapeEnum.CUSTOM
        return newShape


class QpnSocketSide(Enum):
    INPUT = 1
    OUTPUT = 2


class QpnSocket(QGraphicsItem):
    def __init__(self, shape: QpnSocketShape = None, side=QpnSocketSide.INPUT, parent=None):
        super().__init__(parent)
        self._side = side
        self._shape = shape

        # Rendering settings to be set later
        self._pen_default = QPen()
        self._pen_selected = QPen()
        self._brush = QBrush()
        self._brush.setStyle(Qt.SolidPattern)

        # TODO: Fix the positioning
        # self._x_pos = 0.0 if side == QpnSocketSide.INPUT else parent.width
        # if side == QpnSocketSide.INPUT:
        #     self._y_pos = index * 30 + parent.title_height + (parent._padding * 2) + self._shape.boundingRect().height()
        # else:
        #     self._y_pos = parent.height - (index * 30) - (parent._padding * 2) - self._shape.boundingRect().height()

        # self.setPos(self._x_pos, self._y_pos)


    # Function to set all rendering settings (outline colors, fill color, outline width)
    def setRenderingSettings(self, outlineWidth: int, outlineColor: QColor, fillColor: QColor, outlineSelectedColor: QColor = None):
        self.setOutlineWidth(outlineWidth)
        self.setOutlineColor(outlineColor)
        self.setFillColor(fillColor)
        self.setSelectedOutlineColor(outlineColor if outlineSelectedColor is None else outlineSelectedColor)


    def setOutlineColor(self, color: QColor):
        self._pen_default.setColor(color)


    def setOutlineWidth(self, width: int):
        self._pen_default.setWidth(width)
        self._pen_selected.setWidth(width)


    def setSelectedOutlineColor(self, color: QColor):
        self._pen_selected.setColor(color)


    def setFillColor(self, color: QColor):
        self._brush.setStyle(Qt.SolidPattern)
        self._brush.setColor(color)


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget=None):
        painter.setPen(self._pen_default)
        painter.setBrush(self._brush)
        painter.drawPath(self._shape.simplified())
        pass
    

    def SetShape(self, shape: QpnSocketShape):
        self._shape = shape


    def boundingRect(self):
        return self._shape.boundingRect()
