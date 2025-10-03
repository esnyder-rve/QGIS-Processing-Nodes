import uuid

from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QWidget, QVBoxLayout, QGraphicsItem
from PyQt5.QtWidgets import QSplitter, QPushButton, QHBoxLayout
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from QpnGraphicsView import QpnGraphicsView
from QpnGraphicsScene import QpnGraphicsScene
from QpnNode import QpnNode
from QpnNoodle import QpnNoodle
from QpnSocket import QpnSocketSide
from QpnAlgorithmsDB import QpnAlgorithmsDB
from QpnGraph import QpnGraph

# from NodeSurface import NodesSurface, NodeSurfaceMode
# from Toolbox import Toolbox

class QpnMainWindow(QWidget):
    def __init__(self, parent=None):
        super(QpnMainWindow, self).__init__(parent)

        self._graph = QpnGraph()

        self.InitUI()


    def InitUI(self):
        self.setGeometry(100, 100, 800, 500)

        # Get the AlgorithmDB instance
        algDB = QpnAlgorithmsDB()

        # Create widgets
        self.toolbox = algDB.getAlgorithmToolbox()
        self.toolbox.itemDoubleClicked.connect(self.toolboxItemDoubleClick)
        self.btnAddNode = QPushButton("Add Node to Model")
        self.btnAddNode.clicked.connect(self.btnAddNodeClicked)
        self.mainNodeScene = QpnGraphicsScene()
        self.graphicsView = QpnGraphicsView(self.mainNodeScene, self)
        
        # Create views/containers
        self.toolboxView = QVBoxLayout()
        self.toolboxView.addWidget(self.toolbox)
        self.toolboxView.addWidget(self.btnAddNode)

        self.toolboxContainer = QWidget()
        self.toolboxContainer.setLayout(self.toolboxView)

        # Splitter widget for the algorithm toolbox on the side (splitter allows to resize)
        self.splitter = QSplitter()
        self.splitter.addWidget(self.toolboxContainer)
        self.splitter.addWidget(self.graphicsView)

        # Create and set the layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create Graphic View
        self.layout.addWidget(self.splitter)

        self.setWindowTitle("QGIS Processing Nodes Editor")
        self.show()


    def btnAddNodeClicked(self):
        self.addNode(self.toolbox.currentItem().text(1))


    def toolboxItemDoubleClick(self, item, column):
        if item.childCount() == 0:
            self.addNode(self.toolbox.currentItem().text(1))


    def addNode(self, algID):
        newNode = QpnNode(QpnAlgorithmsDB().instance().getAlgorithm(algID), nodeUUID=uuid.uuid4())
        self.mainNodeScene.AddNode(newNode)
        # self._graph.addNode(newNode)
