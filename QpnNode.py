from PyQt5.QtGui import QColor, QFont, QPainter, QPainterPath, QPen, QBrush
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem, QStyleOptionGraphicsItem, QGraphicsProxyWidget, QSizePolicy

# FIXME: Temp for testing
from PyQt5.QtWidgets import QLabel, QTextEdit

from QpnNodeGraphic import QpnNodeGraphic
from QpnNodeContentWidget import QpnNodeContentWidget
from QpnSocket import QpnSocket, QpnSocketSide, QpnSocketShape
from QpnAlgorithmsDB import *
from QpnSettings import QpnSettings

class QpnNode(QGraphicsItem):
    """
    QpnNode: A class for representing a processing algorithm.

    ...

    Attributes
    ----------
    _title : str
        a string of the user friendly name of the node

    inputs : QpnSocket[]
        an array of sockets which represent the algorithm's inputs

    outputs : QpnSocket[]
        an array of sockets which represent the algorithm's outputs
    
    Methods
    -------
    InitUI()
        a function called during the construction to initialize the node's user interface
    """
    # def __init__(self, scene, title="Undefined Node", parent=None):
    def __init__(self, title="Undefined Node", parent=None):
        super().__init__(parent)

        self._title = title

        self.inputs = []
        self.outputs = []
        
        # UI Elements
        self.titleBar = QGraphicsTextItem()
        self.nodeContent = QpnNodeContentWidget()
        self.nodeContentProxy = QGraphicsProxyWidget(self)


        # TODO: make these dynamic
        self.width = 180
        self.height = 300
        self.title_height = 24

        self._padding = 5

        self._pen_default = QPen(QColor(QpnSettings.NodeOutlineColor))
        self._pen_default.setWidth(QpnSettings.NodeOutlineWidth)

        self._pen_selected = QPen(QColor(QpnSettings.NodeOutlineSelectionColor))
        self._pen_selected.setWidth(QpnSettings.NodeOutlineWidth)

        self._brush_title = QBrush(QColor(QpnSettings.NodeTitleBackgroundColor))
        self._brush_background = QBrush(QColor(QpnSettings.NodeContentBackgroundColor))

        self.InitUI()


    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
        self.titleBar.setPlainText(self._title)


    def InitUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.titleBar = QGraphicsTextItem(self)
        self.titleBar.setDefaultTextColor(QColor(QpnSettings.NodeTitleTextColor))
        self.titleBar.setFont(QFont(QpnSettings.NodeTitleFont, QpnSettings.NodeTitleFontSize))
        self.titleBar.setPos(self._padding, 0)
        self.titleBar.setTextWidth(self.width - 2 * self._padding)
        self.titleBar.setPlainText(self._title)
        
        tempLabel = QLabel("Foo Bar")
        self.nodeContent.AddWidget(tempLabel)
        tempTextEdit = QTextEdit("Lorem ipsum...")
        self.nodeContent.AddWidget(tempTextEdit)

        self.nodeContent.setGeometry(QpnSettings.NodeEdgeRoundness, self.title_height + QpnSettings.NodeEdgeRoundness, self.width - 2 * QpnSettings.NodeEdgeRoundness, self.height - 2 * QpnSettings.NodeEdgeRoundness - self.title_height)
        self.nodeContentProxy.setWidget(self.nodeContent)


    def AddSocket(self, side: QpnSocketSide, dataType: str = None):
        socket = QpnSocket(side=side, parent=self)

        # Set the socket depending on the data type
        if dataType is None:
            socket.SetShape(QpnSocketShape.Circle(6))
            socket.setRenderingSettings(2, QColor('#FF000000'), QColor('#FFFF0000'))
        elif dataType == 'QgsVectorLayer':
            socket.SetShape(QpnSocketShape.Circle(6))
            socket.setRenderingSettings(2, QColor('#FF000000'), QColor('#FF00AA00'))
        elif dataType == 'Integer':
            socket.SetShape(QpnSocketShape.Square(12))
            socket.setRenderingSettings(2, QColor('#FF000000'), QColor('#FF4D4D4D'))
        elif dataType == 'Float':
            socket.SetShape(QpnSocketShape.Square(12))
            socket.setRenderingSettings(2, QColor('#FF000000'), QColor('#FF4D4D4D'))
        elif dataType == 'Boolean':
            socket.SetShape(QpnSocketShape.Diamond(12))
            socket.setRenderingSettings(2, QColor('#FF000000'), QColor('#FFFC78D1'))
        else:
            socket.SetShape(QpnSocketShape.Circle(6))
            socket.setRenderingSettings(2, QColor('#FF000000'), QColor('#FFFF0000'))

        # TODO: Fix the positioning, and make it more dynamic
        _x_pos = 0.0 if side == QpnSocketSide.INPUT else self.width
        _y_pos = 0.0
        index = len(self.inputs) if side == QpnSocketSide.INPUT else len(self.outputs)

        if side == QpnSocketSide.INPUT:
            _y_pos = index * 30 + self.title_height + (self._padding * 2) + socket._shape.boundingRect().height()
        else:
            _y_pos = self.height - (index * 30) - (self._padding * 2) - socket._shape.boundingRect().height()

        socket.setPos(_x_pos, _y_pos)


        # Add the socket to the node
        if side == QpnSocketSide.INPUT:
            self.inputs.append(socket)
        elif side == QpnSocketSide.OUTPUT:
            self.outputs.append(socket)
        else:
            # We have an error
            print('Error, socket is neither INPUT or OUTPUT')
            return


    def RemoveSocket():
        pass


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

        
    @classmethod
    def fromAlgID(cls, algID: str):
        newNode = cls()
        newNode.title = QpnAlgorithmDB.getAlgName(algID)
        algInputs = QpnAlgorithmDB.getAlgInputs(algID)
        for i in algInputs:
            newNode.AddSocket(QpnSocketSide.INPUT, i['Type'][0])

        algOutputs = QpnAlgorithmDB.getAlgOutputs(algID)
        for i in algOutputs:
            newNode.AddSocket(QpnSocketSide.OUTPUT, i['Type'][0])


        return newNode
