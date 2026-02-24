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
from QpnSocketDataType import QpnSocketDataType, QpnDataType


# Class for holding the socket shape
class QpnSocketShape(QPainterPath):
    def __init__(self, shape=None, parent=None):
        super().__init__()
        self._shape = shape
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
    def Circle(cls, diameter: int):
        newShape = cls()
        newShape.addEllipse(-diameter/2.0, -diameter/2.0, diameter, diameter)
        return newShape


    @classmethod
    def Square(cls, width: int):
        newShape = cls()
        newShape.addRect(-width // 2, -width // 2, width, width)
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
        return newShape


    @classmethod
    def Rectangle(cls, width: int, height: int):
        newShape = cls()
        newShape.addRect(-width // 2, -height // 2, width, height)
        return newShape


    @classmethod
    def OblongCircle(cls, width: int, height: int):
        newShape = cls()
        # Use RoundedRect() and set the radius to 1/2 the width
        newShape.addRoundedRect(-width // 2, -height // 2, width, height, width // 2, width // 2)
        return newShape


    @classmethod
    def CustomShape(cls, path: QPainterPath):
        newShape = cls()
        newShape.addPath(path)
        return newShape


class QpnSocketSide(Enum):
    INPUT  = 1
    OUTPUT = 2


class QpnSocket(QGraphicsItem):
    def __init__(self, dataType: QpnSocketDataType = None, name: str = None, tooltip: str = None, side=QpnSocketSide.INPUT, parent=None):
        super().__init__(parent)
        self._dataType = dataType
        self._side = side
        self._shape = None
        self._name = name
        self._tooltip = tooltip

        self._shape = QpnSocketShape.Circle(12)

        # Rendering settings to be set later
        self._pen_default = QPen()
        self._pen_selected = QPen()
        self._brush = QBrush()
        self._brush.setStyle(Qt.SolidPattern)

        self.setRenderingSettings(2, QColor('#FF000000'), QColor('#FFFF0000'))

        # TODO: Fix the positioning
        # self._x_pos = 0.0 if side == QpnSocketSide.INPUT else parent.width
        # if side == QpnSocketSide.INPUT:
        #     self._y_pos = index * 30 + parent.title_height + (parent._padding * 2) + self._shape.boundingRect().height()
        # else:
        #     self._y_pos = parent.height - (index * 30) - (parent._padding * 2) - self._shape.boundingRect().height()

        # self.setPos(self._x_pos, self._y_pos)


        if dataType.atLeast(QpnDataType.VectorLayer):
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF62C662'))

        elif dataType.atLeast(QpnDataType.MultiVectorLayers):
            self._shape = QpnSocketShape.OblongCircle(12, 24)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF62C662'))

        elif dataType.atLeast(QpnDataType.VectorFeature):
            self._shape = QpnSocketShape.Square(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF62C662'))

        elif dataType.atLeast(QpnDataType.RasterLayer):
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFB53B31'))

        elif dataType.atLeast(QpnDataType.MultiRasterLayers):
            self._shape = QpnSocketShape.OblongCircle(12, 24)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFB53B31'))

        elif dataType.atLeast(QpnDataType.RasterBand):
            self._shape = QpnSocketShape.Square(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFB53B31'))

        elif dataType.atLeast(QpnDataType.MeshLayer):
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFC2781D'))

        elif dataType.atLeast(QpnDataType.PointCloudLayer):
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFFFFFFF'))

        elif dataType.atLeast(QpnDataType.Field):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF7474FF'))

        elif dataType.atLeast(QpnDataType.Extent):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF703E9A'))

        elif dataType.atLeast(QpnDataType.Expression):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF5B3565'))

        elif dataType.atLeast(QpnDataType.String):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF4F91F0'))

        elif dataType.atLeast(QpnDataType.Color):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFC6C628'))

        elif dataType.atLeast(QpnDataType.CoordinateSystem):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFFFFFFF'))

        elif dataType.atLeast(QpnDataType.Distance):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFFFFFFF'))

        elif dataType.atLeast(QpnDataType.Area):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFFFFFFF'))

        elif dataType.atLeast(QpnDataType.Enum):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFB9B9B9'))

        elif dataType.atLeast(QpnDataType.Boolean):
            self._shape = QpnSocketShape.Diamond(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFBE7DBB'))

        elif dataType.atLeast(QpnDataType.Numeric):
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FF828282'))

        elif dataType.atLeast(QpnDataType.AddWild):
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(2, QColor('#FF4C4C4C'), QColor('#FF1A1A1A'))

        else:
            self._shape = QpnSocketShape.Circle(12)
            self.setRenderingSettings(1, QColor('#FF000000'), QColor('#FFFF0000'))


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
