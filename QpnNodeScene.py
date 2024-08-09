from QpnGraphicsScene import QpnGraphicsScene
from QpnNode import QpnNode
from QpnNoodle import QpnNoodle

from QpnSettings import QpnSettings

class QpnNodeScene:
    def __init__(self):
        self.nodes = []
        self.edges = []

        self._scene_height = self._scene_width = QpnSettings.GridSceneSize
        
        self.InitUi()


    def InitUi(self):
        self.scene = QpnGraphicsScene(self)
        self.scene.SetScene(self._scene_width, self._scene_height)


    def AddNode(self, node: QpnNode):
        self.nodes.append(node)
        self.scene.addItem(node)


    def RemoveNode(self, node: QpnNode):
        self.nodes.remove(node)
        self.scene.removeItem(node)


    def AddEdge(self, edge: QpnNoodle):
        self.edges.append(edge)


    def RemoveEdge(self, edge: QpnNoodle):
        self.edges.remove(edge)
