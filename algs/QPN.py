# from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QComboBox, QLineEdit, QVBoxLayout
from QpnAlgorithm import QpnAlgorithm, QpnAlgorithmInput, QpnAlgorithmOutput
from QpnSocketDataType import QpnDataType
# from QpnNode import QpnNode


QpnAlgTestNode = QpnAlgorithm('qpn:testnode', 'Test', 'Algorithm for testing purposes')
QpnAlgTestNode.help = """Testing Algorithm
    This algorithm does absolutely nothing. It is purely for the purposes of seeing all the socket types
    Inputs: Yes
    Outputs: Pass-through from inputs
"""

QpnAlgTestNode.group = 'Testing'
QpnAlgTestNode.provider = 'QPN'

QpnAlgTestNode.addInput(QpnAlgorithmInput('VECTORLAYER', QpnDataType.VectorLayer, 'Vector Layer', "Sample vector layer", False, False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('VECTORLAYERS', QpnDataType.MultiVectorLayers, 'Vector Layers', "Sample multi-vector layers", False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('VECTORFEATURES', QpnDataType.VectorFeature, 'Vector Features', "Sample vector features", False,
                      False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('RASTERLAYER', QpnDataType.RasterLayer, 'Raster Layer', "Sample raster layer", False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('RASTERLAYERS', QpnDataType.MultiRasterLayers, 'Raster Layers', "Sample multi-raster layers",
                      False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('RASTERBAND', QpnDataType.RasterBand, 'Raster Layers', "Sample multi-raster layers", False,
                      False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('MESHLAYER', QpnDataType.MeshLayer, 'Mesh Layer', "Sample mesh layer", False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('POINTCLOUD', QpnDataType.PointCloudLayer, 'Point Cloud', "Sample point cloud", False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('ATTRIBUTEFIELD', QpnDataType.Field, 'Attribute Field', "Sample attribute field", False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('GEOGRAPHICEXTENT', QpnDataType.Extent, 'Extent', "Sample geographic extent", False, False))
QpnAlgTestNode.addInput(
    QpnAlgorithmInput('EXPRESSION', QpnDataType.Expression, 'Expression', "Sample QGIS expression", False, False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('STRING', QpnDataType.String, 'String', "Sample string value", False, False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('COLOR', QpnDataType.Color, 'Color', "Sample color value", False, False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('OPTION', QpnDataType.Enum, 'Enum', "Sample enumerated option", False, False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('CHECKBOX', QpnDataType.Boolean, 'Yes/No', "Sample boolean option", False, False))
QpnAlgTestNode.addInput(QpnAlgorithmInput('ADDNEW', QpnDataType.AddWild, 'Add new...', "Add another input...", False, False))

QpnAlgTestNode.addOutput(
    QpnAlgorithmOutput('VECTOROUT', QpnDataType.VectorLayer, 'Vector layer output', "Output vector layer", True))
QpnAlgTestNode.addOutput(
    QpnAlgorithmOutput('RASTEROUT', QpnDataType.RasterLayer, 'Raster layer output', "Output raster layer", True))

QpnAlgTestNode.executionFunction = lambda: print('This is a test node')

QpnAlgModelInput = QpnAlgorithm('qpn:modelinput', 'Model Input', 'Input parameters for the model')
QpnAlgModelInput.help = "Input parameters for the model. To add a new parameter, check the properties panel, or drag an algorithm's input here."
QpnAlgModelInput.group = 'Modeller'
QpnAlgModelInput.provider = 'QPN'
QpnAlgModelInput.addOutput(QpnAlgorithmOutput('ADDNEW', QpnDataType.AddWild, 'Add new model input parameter', 'Add new input parameter', False))

QpnAlgModelInput.executionFunction = lambda: print('Starting model...')

QpnAlgModelOutput = QpnAlgorithm('qpn:modeloutput', 'Model Output', 'Output for the model')
QpnAlgModelOutput.help = "Outputs for the model. To add a new output, check the properties panel, or drag an algorithm's output here."
QpnAlgModelOutput.group = 'Modeller'
QpnAlgModelOutput.provider = 'QPN'
QpnAlgModelOutput.addInput(QpnAlgorithmInput('ADDNEW', QpnDataType.AddWild, 'Add new model output', 'Add new output parameter', True, False))

QpnAlgModelOutput.executionFunction = lambda: print('Finishing model...')

QpnRasterBandSelector = QpnAlgorithm('qpn:rasterbandselector', 'Raster Band Selector', 'Select a single band from a multi-band raster.')
QpnRasterBandSelector.help = "Select a single band from a multi-band raster."
QpnRasterBandSelector.group = 'Raster Utilities'
QpnRasterBandSelector.provider = 'QPN'
QpnRasterBandSelector.addInput(QpnAlgorithmInput('RASTER', QpnDataType.RasterLayer, 'Raster Layer', "Input raster layer", False, False))
QpnRasterBandSelector.addInput(QpnAlgorithmInput('BANDNUM', QpnDataType.Numeric, 'Band Number', "Raster band number", False, False))
QpnRasterBandSelector.addOutput(QpnAlgorithmOutput('RASTERBAND', QpnDataType.RasterBand, 'Raster Band', "Selected raster band", True))

QpnRasterBandSelector.executionFunction = lambda: print('Selecting raster band...')

# class QpnAlgTestNode(QpnAlgorithm):
#
#     def __init__(self):
#         super().__init__('qpn:testnode', 'Test', 'Algorithm for testing purposes')
#         self.help = """Testing Algorithm
#             This algorithm does absolutely nothing. It is purely for the purposes of seeing all the socket types
#             Inputs: Yes
#             Outputs: Pass-through from inputs
#         """
#
#         self.group = 'Testing'
#         self.provider = 'QPN'
#
#         self.addInput(QpnAlgorithmInput('VECTORLAYER', QpnDataType.VectorLayer, 'Vector Layer', "Sample vector layer", False, False))
#         self.addInput(QpnAlgorithmInput('VECTORLAYERS', QpnDataType.MultiVectorLayers, 'Vector Layers', "Sample multi-vector layers", False, False))
#         self.addInput(QpnAlgorithmInput('VECTORFEATURES', QpnDataType.VectorFeature, 'Vector Features', "Sample vector features", False, False))
#         self.addInput(QpnAlgorithmInput('RASTERLAYER', QpnDataType.RasterLayer, 'Raster Layer', "Sample raster layer", False, False))
#         self.addInput(QpnAlgorithmInput('RASTERLAYERS', QpnDataType.MultiRasterLayers, 'Raster Layers', "Sample multi-raster layers", False, False))
#         self.addInput(QpnAlgorithmInput('RASTERBAND', QpnDataType.RasterBand, 'Raster Layers', "Sample multi-raster layers", False, False))
#         self.addInput(QpnAlgorithmInput('MESHLAYER', QpnDataType.MeshLayer, 'Mesh Layer', "Sample mesh layer", False, False))
#         self.addInput(QpnAlgorithmInput('POINTCLOUD', QpnDataType.PointCloudLayer, 'Point Cloud', "Sample point cloud", False, False))
#         self.addInput(QpnAlgorithmInput('ATTRIBUTEFIELD', QpnDataType.Field, 'Attribute Field', "Sample attribute field", False, False))
#         self.addInput(QpnAlgorithmInput('GEOGRAPHICEXTENT', QpnDataType.Extent, 'Extent', "Sample geographic extent", False, False))
#         self.addInput(QpnAlgorithmInput('EXPRESSION', QpnDataType.Expression, 'Expression', "Sample QGIS expression", False, False))
#         self.addInput(QpnAlgorithmInput('STRING', QpnDataType.String, 'String', "Sample string value", False, False))
#         self.addInput(QpnAlgorithmInput('COLOR', QpnDataType.Color, 'Color', "Sample color value", False, False))
#         self.addInput(QpnAlgorithmInput('OPTION', QpnDataType.Enum, 'Enum', "Sample enumerated option", False, False))
#         self.addInput(QpnAlgorithmInput('CHECKBOX', QpnDataType.Boolean, 'Yes/No', "Sample boolean option", False, False))
#         self.addInput(QpnAlgorithmInput('ADDNEW', QpnDataType.AddWild, 'Add new...', "Add another input...", False, False))
#
#         self.addOutput(QpnAlgorithmOutput('VECTOROUT', QpnDataType.VectorLayer, 'Vector layer output', "Output vector layer", True))
#         self.addOutput(QpnAlgorithmOutput('RASTEROUT', QpnDataType.RasterLayer, 'Raster layer output', "Output raster layer", True))
#
#
#     def execute(self, input):
#         print("I'm executing absolutely nothing!!")

#
# class QpnAlgModelInput(QpnAlgorithm):
#     def __init__(self):
#         super().__init__('qpn:modelinput', 'Model Input', 'Input parameters for the model')
#         self.help = "Input parameters for the model. To add a new parameter, check the properties panel, or drag an algorithm's input here."
#         self.group = 'Modeller'
#         self.provider = 'QPN'
#         self.addOutput(QpnAlgorithmOutput('ADDNEW', QpnDataType.AddWild, 'Add new model input parameter', 'Add new input parameter', False))
#
#     def execute(self, input):
#         print("Starting model...")
#
#
# class QpnAlgModelOutput(QpnAlgorithm):
#     def __init__(self):
#         super().__init__('qpn:modeloutput', 'Model Output', 'Output for the model')
#         self.help = "Outputs for the model. To add a new output, check the properties panel, or drag an algorithm's output here."
#         self.group = 'Modeller'
#         self.provider = 'QPN'
#         self.addInput(QpnAlgorithmInput('ADDNEW', QpnDataType.AddWild, 'Add new model output', 'Add new output parameter', True, False))
#
#     def execute(self, input):
#         print("Exporting data...")
#
#
# class QpnRasterBandSelector(QpnAlgorithm):
#     def __init__(self):
#         super().__init__('qpn:rasterbandselector', 'Raster Band Selector', 'Select a single band from a multi-band raster.')
#         self.help = "Select a single band from a multi-band raster."
#         self.group = 'Raster Utilities'
#         self.provider = 'QPN'
#         self.addInput(QpnAlgorithmInput('RASTER', QpnDataType.RasterLayer, 'Raster Layer', "Input raster layer", False, False))
#         self.addInput(QpnAlgorithmInput('BANDNUM', QpnDataType.Numeric, 'Band Number', "Raster band number", False, False))
#         self.addOutput(QpnAlgorithmOutput('RASTERBAND', QpnDataType.RasterBand, 'Raster Band', "Selected raster band", True))
#
#     def execute(self, input):
#         print("Selecting raster band...")