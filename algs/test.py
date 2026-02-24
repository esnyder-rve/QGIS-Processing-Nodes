from PyQt5.QtWidgets import QLabel, QCheckBox, QComboBox
from ..QpnAlgorithm import QpnAlgorithm

class TestNodeAlg(QpnAlgorithm):
    self._name = "Testing Algorithm"
    self._description = "Algorithm for testing purposes"
    self._help = """Testing Algorothm
This algorithm does absolutely nothing. It is purely for the purposes of seeing all the sockets.
Inputs: Yes
Outputs: Pass-through from inputs"""
    self._qgisAlgID = 'qpn:testnode'

    def __init__(self, qpnID):
        self._qpnID = qpnID

        self._node = None

        self._createNode()


    def _createNode(self):
        self._node = QpnNode(self._name)
        self._node.addInput(QpnDataType.VectorLayer, "Vector Layer", "Sample Vector Layer")
        self._node.addInput(QpnDataType.MultiVectorLayers, "Vector Layers", "Sample Multi-Vector Layers")
        self._node.addInput(QpnDataType.VectorFeature, "Vector Features", "Sample Vector Features")
        self._node.addInput(QpnDataType.RasterLayer, "Raster Layer", "Sample Raster Layer")
        self._node.addInput(QpnDataType.RasterBand, "Raster Band", "Sample Raster Band")
        self._node.addInput(QpnDataType.MeshLayer, "Mesh Layer", "Sample Mesh Layer")
        self._node.addInput(QpnDataType.PointCloudLayer, "Point Cloud", "Sample Point Cloud")
        self._node.addInput(QpnDataType.Field, "Attribute Field", "Sample Attribute Field")
        self._node.addInput(QpnDataType.Extent, "Geographic Extent", "Sample Geographic Extent")
        self._node.addInput(QpnDataType.Expression, "Expression", "Sample Expression")
        self._node.addInput(QpnDataType.String, "String Value", "Sample String Value")
        self._node.addInput(QpnDataType.Color, "Color Value", "Sample Color Value")
        self._node.addInput(QpnDataType.CoordinateSystem, "Coordinate System", "Sample Input Coordinate System")
        self._node.addInput(QpnDataType.Distance, "Distance Value", "Sample Distance Value")

        enumValueWidget = QComboBox()
        enumValueWidget.addItem("Option A", 1)
        enumValueWidget.addItem("Option B", 2)
        enumValueWidget.addItem("Option C", 3)
        enumValueWidget.addItem("Option D", 4)
        self._node.addInput(QpnDataType.Enum, "Some Enum", "Sample Enum input", enumValueWidget)

        boolValueWidget = QCheckBox("Sample Boolean Value")
        boolValueWidget.setChecked(False)
        self._node.addInput(QpnDataType.Boolean, "Boolean Value", "Sample Boolean Value", boolValueWidget)

        self._node.addInput(QpnDataType.AddWild, "Add new...", "Sample add new socket")

        self._node.addOutput(QpnDataType.VectorLayer, "Vector Output", "Vector Layer")
        self._node.addOutput(QpnDataType.RasterLayer, "Raster Output", "Raster Layer")

