from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QWidget, QVBoxLayout, QGraphicsItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from QpnGraphicsView import QpnGraphicsView
from QpnNodeScene import QpnNodeScene
from QpnNode import QpnNode
from QpnSocket import QpnSocketSide

# from NodeSurface import NodesSurface, NodeSurfaceMode
# from Toolbox import Toolbox

class QpnMainWindow(QWidget):
    def __init__(self, parent=None):
        super(QpnMainWindow, self).__init__(parent)

        self.InitUI()

        # self.view = NodesSurface()
        # self.toolbox = Toolbox()

        # FIXME: temporary button to add something
        # self.tmpAddItemBtn = QPushButton()
        # self.tmpAddItemBtn.setText("Add Item")
        # self.tmpAddItemBtn.clicked.connect(self.TempAddItem)

        # FIXME: temporary layout for toolbox and temp button
        # self.temp_vbox = QVBoxLayout()
        # self.temp_vbox.addWidget(self.toolbox)
        # self.temp_vbox.addWidget(self.tmpAddItemBtn)

        # FIXME: temporary QWidget (acts like a group container)
        # self.temp_container = QWidget()
        # self.temp_container.setLayout(self.temp_vbox)

        # splitter = QSplitter()
        # splitter.addWidget(self.temp_container)
        # # splitter.addWidget(self.toolbox)
        # splitter.addWidget(self.view)

        # layout = QHBoxLayout()
        # layout.addWidget(splitter)

        # self.widget = QWidget()
        # self.widget.setLayout(layout)

        # self.setCentralWidget(self.widget)

    def InitUI(self):
        self.setGeometry(100, 100, 800, 500)

        # Create and set the layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create Graphic Scene
        self.nodeScene = QpnNodeScene()

        # Add nodes
        node1 = QpnNode("Test Node")
        node1.AddSocket(QpnSocketSide.INPUT)
        node1.AddSocket(QpnSocketSide.INPUT)
        node1.AddSocket(QpnSocketSide.INPUT)
        node1.AddSocket(QpnSocketSide.OUTPUT)
        node2 = QpnNode.fromAlgID('qgis:buffer')
        self.nodeScene.AddNode(node1)
        self.nodeScene.AddNode(node2)

        # Create Graphic View
        self.view = QpnGraphicsView(self.nodeScene.scene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("QGIS Processing Nodes Editor")
        self.show()
