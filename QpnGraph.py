class QpnGraphEdge():
    def __init__(self):
        self._edge_id : str | None = None
        self._input_node_id : str | None = None
        self._input_node_socket_index : int | None = None

        self._output_node_id : str | None = None
        self._output_node_socket_index: int | None = None


class QpnGraphNode():
    def __init__(self, nodeID: str):
        self._node_id : str = nodeID


class QpnGraph():
    def __init__(self):
        # self.inputs: list[QpnSocket] = []
        self._nodes : dict[str, QpnGraphNode] = {}
        self._edges : dict[str, QpnGraphEdge] = {}
        pass

    def addNode(self, node):

        pass

    def removeNode(self, node):
        pass

    def addEdge(self, nodeA, socketA, nodeB, socketB):
        pass

    def removeEdge(self, edgeID):
        pass
