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

QpnIteratorForEachFeature = QpnAlgorithm(
    'qpn:iteratorforeacheachfeature',
    'For-Each Feature',
    'Iterate over each feature in a vector layer'
)
QpnIteratorForEachFeature.help = "Iterate over each feature in a vector layer."
QpnIteratorForEachFeature.group = 'Iterator'
QpnIteratorForEachFeature.provider = 'QPN'
QpnIteratorForEachFeature.addInput(QpnAlgorithmInput(
    "INPUT",
    QpnDataType.VectorLayer,
    "Vector Layer",
    "Input vector layer to iterate over",
    False,
    False
))
QpnIteratorForEachFeature.addInput(QpnAlgorithmInput(
    "CONTEXT",
    QpnDataType.AddWild,
    "Add new context...",
    "Add item to pass as static context to the iterator.",
    False,
    False
))
QpnIteratorForEachFeature.addOutput(QpnAlgorithmOutput(
    "OUTPUT",
    QpnDataType.VectorLayer,
    "Vector Layer",
    "Output vector layer",
    True
))
QpnIteratorForEachFeature.addOutput(QpnAlgorithmOutput(
    "AGGREGATEOUTPUT",
    QpnDataType.Numeric,
    "Aggregate Value",
    "Aggregated value",
    True
))

QpnIteratorForEachVectorLayer = QpnAlgorithm(
    'qpn:iteratorforeachvectorlayer',
    'For-Each Vector Layer',
    'Iterate over each vector layer'
)

QpnIteratorForEachVectorLayer.help = "Iterate over each vector layer."
QpnIteratorForEachVectorLayer.group = 'Iterator'
QpnIteratorForEachVectorLayer.provider = 'QPN'
QpnIteratorForEachVectorLayer.addInput(QpnAlgorithmInput(
    "INPUT",
    QpnDataType.MultiVectorLayers,
    "Vector Layers",
    "Input layers to iterate over",
    False,
    False
))
QpnIteratorForEachVectorLayer.addInput(QpnAlgorithmInput(
    "CONTEXT",
    QpnDataType.AddWild,
    "Add new context...",
    "Add item to pass as static context to the iterator.",
    False,
    False
))
QpnIteratorForEachVectorLayer.addOutput(QpnAlgorithmOutput(
    "OUTPUT",
    QpnDataType.AddWild,
    "Output",
    "Output vector layer",
    True
))

QpnIteratorForEachRasterBand = QpnAlgorithm(
    'qpn:iteratorforeachrasterband',
    'For-Each Raster Band',
    'Iterate over each Raster Band'
)
QpnIteratorForEachRasterBand.help = "Iterate over each raster band."
QpnIteratorForEachRasterBand.group = 'Iterator'
QpnIteratorForEachRasterBand.provider = 'QPN'
QpnIteratorForEachRasterBand.addInput(QpnAlgorithmInput(
    "INPUT",
    QpnDataType.RasterLayer,
    "Raster Layer",
    "Input multi-band raster to iterate over",
    False,
    False
))
QpnIteratorForEachRasterBand.addInput(QpnAlgorithmInput(
    "CONTEXT",
    QpnDataType.AddWild,
    "Add new context...",
    "Add item to pass as static context to the iterator.",
    False,
    False
))
QpnIteratorForEachRasterBand.addOutput(QpnAlgorithmOutput(
    "OUTPUT",
    QpnDataType.AddWild,
    "Output",
    "Output vector layer",
    True
))

QpnConditionalIf = QpnAlgorithm(
    'qpn:conditionalif',
    'If - Branch Input',
    'Take an input and send it to different nodes depending on result of boolean expression.'
)
QpnConditionalIf.help = "Take an input and send it to different nodes depending on result of boolean expression."
QpnConditionalIf.group = 'Conditional'
QpnConditionalIf.provider = 'QPN'
QpnConditionalIf.addInput(QpnAlgorithmInput(
    "INPUT",
    QpnDataType.AddWild,
    'Input',
    'Input to send to different nodes',
    False,
    False
))
QpnConditionalIf.addInput(QpnAlgorithmInput(
    "CONDITION",
    QpnDataType.Expression,
    'Condition',
    'Conditional Expression',
    False,
    False
))
QpnConditionalIf.addOutput(QpnAlgorithmOutput(
    "TRUEOUTPUT",
    QpnDataType.AddWild,
    "True Output",
    'Input layer output if condition is TRUE',
    True
))
QpnConditionalIf.addOutput(QpnAlgorithmOutput(
    "FALSEOUTPUT",
    QpnDataType.AddWild,
    "False Output",
    'Input layer output if condition is FALSE',
    True
))
QpnConditionalIf.addOutput(QpnAlgorithmOutput(
    "EXPRESSIONRESULT",
    QpnDataType.Boolean,
    'Expression Result',
    "Result of the conditional expression",
    False
))

QpnBranchJoiner = QpnAlgorithm(
    'qpn:conditionalbranchjoiner',
    'Branch Joiner',
    'Take multiple inputs, and output the first not-null input.'
)

QpnBranchJoiner.help = "This node takes multiple inputs, usually from algorithms in different conditional or switch branches and outputs the first not-null input. All inputs must be the same type."
QpnBranchJoiner.group = 'Conditional'
QpnBranchJoiner.provider = 'QPN'
QpnBranchJoiner.addInput(QpnAlgorithmInput(
    "INPUT1",
    QpnDataType.VectorLayer,
    "Input 1",
    "Input 1 to test if null",
    False,
    False
))
QpnBranchJoiner.addInput(QpnAlgorithmInput(
    "INPUT2",
    QpnDataType.VectorLayer,
    "Input 2",
    "Input 2 to test if null",
    False,
    False
))
QpnBranchJoiner.addInput(QpnAlgorithmInput(
    "INPUT3",
    QpnDataType.AddWild,
    "Add new...",
    "Add new item to test if null",
    False,
    False
))
QpnBranchJoiner.addOutput(QpnAlgorithmOutput(
    "OUTPUT",
    QpnDataType.VectorLayer,
    "Output",
    "First input layer that was not null",
    True
))

SagaFlowAccumulationD8 = QpnAlgorithm(
    'qpn:sagaflowaccumulationd8',
    'Flow Accumulation (Top-Down) [D8]',
    'SAGA\'s Top-Down Flow Accumulation (Deterministic 8 Method)'
)
SagaFlowAccumulationD8.help = "SAGA Flow Accumulation (Deterministic 8 Method)"
SagaFlowAccumulationD8.group = 'SAGA Demo'
SagaFlowAccumulationD8.provider = 'QPN'
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "ELEVATION",
    QpnDataType.RasterLayer,
    "Elevation",
    "DEM Elevation Raster",
    False,
    False
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "SINKS",
    QpnDataType.RasterLayer,
    "Sink Routes",
    "Sink Routes",
    False,
    False
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "WEIGHTS",
    QpnDataType.RasterLayer,
    "Weights",
    "Weights",
    False,
    False
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "MEANCATCHMENT",
    QpnDataType.RasterLayer,
    "Input for Mean over Catchment",
    "Input for Mean over Catchment",
    False,
    False
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "MATERIAL",
    QpnDataType.RasterLayer,
    "Material for Accumulation",
    "Material for Accumulation",
    False,
    False
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "CHANNELDIRECTION",
    QpnDataType.RasterLayer,
    "Channel Direction",
    "Channel Direction",
    False,
    False
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "STEP",
    QpnDataType.Numeric,
    "Step",
    "Step",
    False,
    False,
    {
        'defaultValue': 1.0,
        'minValue': 1.0,
        'maxValue': 1000.0
    }
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "UNIT",
    QpnDataType.Enum,
    "Flow Accumulation Unit",
    "Flow Accumulation Unit",
    False,
    False,
    {
        'enumValues': [
            (0, 'number of cells'),
            (1, 'cell area')],
        'defaultValue': 1
    }
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "METHOD",
    QpnDataType.Enum,
    "Method",
    "Flow Accumulation Method",
    False,
    False,
    {'enumValues': [
        (0, 'Deterministic 8'),
        (1, 'Rho 8'),
        (2, 'Braunschweiger Reliefmodell'),
        (3, 'Deterministic Infinity'),
        (4, 'Multiple Flow Direction'),
        (5, 'Multiple Triangular Flow Direction'),
        (6, 'Multiple Maximum Downslope Gradient Based Flow Direction')],
    'defaultValue': 4
    }
))
SagaFlowAccumulationD8.addInput(QpnAlgorithmInput(
    "THRESHOLDED",
    QpnDataType.Boolean,
    "Thresholded Linear Flow",
    "Apply linear flow routing (D8) to all cells, having a flow accumulation greater than the specified threshold",
    False,
    False,
    {
        'defaultValue': False,
    }
))
SagaFlowAccumulationD8.addOutput(QpnAlgorithmOutput(
    "FLOW",
    QpnDataType.RasterLayer,
    "Flow Accumulation",
    "Calculated Flow Accumulation",
    False
))
SagaFlowAccumulationD8.addOutput(QpnAlgorithmOutput(
    "PATH",
    QpnDataType.RasterLayer,
    "Flow Path Length",
    "Average distance that a cell's accumulated flow travelled",
    False
))

SagaFlowAccumulationMFD = QpnAlgorithm(
    'qpn:sagaflowaccumulationmfd',
    'Flow Accumulation (Top-Down) [MFD]',
    'SAGA\'s Top-Down Flow Accumulation (Multi Flow Direction Method)'
)
SagaFlowAccumulationMFD.help = "SAGA Flow Accumulation (Multi Flow Direction Method)"
SagaFlowAccumulationMFD.group = 'SAGA Demo'
SagaFlowAccumulationMFD.provider = 'QPN'
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "ELEVATION",
    QpnDataType.RasterLayer,
    "Elevation",
    "DEM Elevation Raster",
    False,
    False
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "SINKS",
    QpnDataType.RasterLayer,
    "Sink Routes",
    "Sink Routes",
    False,
    False
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "WEIGHTS",
    QpnDataType.RasterLayer,
    "Weights",
    "Weights",
    False,
    False
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "MEANCATCHMENT",
    QpnDataType.RasterLayer,
    "Input for Mean over Catchment",
    "Input for Mean over Catchment",
    False,
    False
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "MATERIAL",
    QpnDataType.RasterLayer,
    "Material for Accumulation",
    "Material for Accumulation",
    False,
    False
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "CHANNELDIRECTION",
    QpnDataType.RasterLayer,
    "Channel Direction",
    "Channel Direction",
    False,
    False
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "STEP",
    QpnDataType.Numeric,
    "Step",
    "Step",
    False,
    False,
    {
        'defaultValue': 1.0,
        'minValue': 1.0,
        'maxValue': 1000.0
    }
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "UNIT",
    QpnDataType.Enum,
    "Flow Accumulation Unit",
    "Flow Accumulation Unit",
    False,
    False,
    {
        'enumValues': [
            (0, 'number of cells'),
            (1, 'cell area')],
        'defaultValue': 1
    }
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "METHOD",
    QpnDataType.Enum,
    "Method",
    "Flow Accumulation Method",
    False,
    False,
    {'enumValues': [
        (0, 'Deterministic 8'),
        (1, 'Rho 8'),
        (2, 'Braunschweiger Reliefmodell'),
        (3, 'Deterministic Infinity'),
        (4, 'Multiple Flow Direction'),
        (5, 'Multiple Triangular Flow Direction'),
        (6, 'Multiple Maximum Downslope Gradient Based Flow Direction')],
        'defaultValue': 4
    }
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "THRESHOLDED",
    QpnDataType.Boolean,
    "Thresholded Linear Flow",
    "Apply linear flow routing (D8) to all cells, having a flow accumulation greater than the specified threshold",
    False,
    False,
    {
        'defaultValue': False,
    }
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "CONVERGENCE",
    QpnDataType.Numeric,
    "Convergence factor",
    "Convergence factor",
    False,
    False,
    {
        'defaultValue': 1.10,
        'minValue': 0.001,
        'maxValue': 10.0
    }
))
SagaFlowAccumulationMFD.addInput(QpnAlgorithmInput(
    "MFDCONTOUR",
    QpnDataType.Boolean,
    "Contour Length",
    "Include (pseudo) contour length as additional weighing factor in multiple flow direction routing, reduces flow to diagonal neighbour cells by a factor of 0.71 (s. Quinn et al. 1991 for details).",
    False,
    False,
    {
        'defaultValue': False,
    }
))
SagaFlowAccumulationMFD.addOutput(QpnAlgorithmOutput(
    "FLOW",
    QpnDataType.RasterLayer,
    "Flow Accumulation",
    "Calculated Flow Accumulation",
    False
))
SagaFlowAccumulationMFD.addOutput(QpnAlgorithmOutput(
    "PATH",
    QpnDataType.RasterLayer,
    "Flow Path Length",
    "Average distance that a cell's accumulated flow travelled",
    False
))
