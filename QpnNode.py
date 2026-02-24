import uuid

from PyQt5.QtGui import QColor, QFont, QPainter, QPainterPath, QPen, QBrush, QTextItem
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsItem, QStyleOptionGraphicsItem, QGraphicsProxyWidget, QLabel, \
    QDoubleSpinBox, QLineEdit, QCheckBox, QComboBox

from QpnSocket import QpnSocket, QpnSocketSide
import QpnSocketDataType
from QpnSocketDataType import QpnSocketDataType, QpnDataType
from QpnSettings import QpnSettings
from QpnAlgorithmWrapper import QpnAlgorithmWrapper
from QpnAlgorithmsDB import QpnAlgorithmsDB
import QpnLog


class QpnNode(QGraphicsItem):
    """
    QpnNode: A class for representing a processing algorithm.
    ...

    Attributes
    ----------
    _title : str
        a string of the user-friendly name of the node

    inputs : QpnSocket[]
        an array of sockets which represent the algorithm's inputs

    outputs : QpnSocket[]
        an array of sockets which represent the algorithm's outputs
    
    Methods
    -------
    """

    def __init__(self, algorithm: QpnAlgorithmWrapper | None = None, autoGenerateUI : bool = True, nodeUUID : uuid.UUID | None = None, parent=None):
        """
        Description: Create a new QGIS Processing Node graphical node.
        Parameters
        ----------
            algorithm : QpnAlgorithmWrapper | None
                The processing algorithm that this graphical node is representing
            parent : any
                A parent widget for this node
        """
        super().__init__(parent)

        self._algorithm : QpnAlgorithmWrapper | None = algorithm

        self._uuid : uuid.UUID | None = nodeUUID

        self._nodeContent: QWidget = QWidget()
        self._titleBarHeight = 24

        self.height: int = QpnSettings.NodePadding * 2 + self._titleBarHeight
        self.width: int = QpnSettings.NodePadding * 2
        self._title: str = ''

        self.inputs: list[QpnSocket] = []
        self.outputs: list[QpnSocket] = []
        self.inputWidgets = []

        # Set Qt object properties to be selectable and movable
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

        # Outline pens
        # Regular (default) pen for the outline of the node
        self._pen_default = QPen(QColor(QpnSettings.NodeOutlineColor))
        self._pen_default.setWidth(QpnSettings.NodeOutlineWidth)

        # Pen style for when the node is selected
        self._pen_selected = QPen(QColor(QpnSettings.NodeOutlineSelectionColor))
        self._pen_selected.setWidth(QpnSettings.NodeOutlineWidth)

        # Background style
        self._brush_title = QBrush(QColor(QpnSettings.NodeTitleBackgroundColor))
        self._brush_background = QBrush(QColor(QpnSettings.NodeContentBackgroundColor))

        self._set_base_node_ui()

        if self._algorithm is not None and autoGenerateUI:
            self._load_ui()


    def _set_base_node_ui(self):
        """
        Description: This function sets up the basic node's UI. This should be run whether an algorithm is provided or not.
        This function sets up the node's widget container, the title text, and the starting size.
        Another function should be called to set up from an algorithm (which assumes this is done)
        """
        # Set up the node content widget
        self._nodeContentLayout = QVBoxLayout()
        self._nodeContentLayout.setContentsMargins(0, 0, 0, 0)
        self._nodeContentLayout.setSpacing(0)
        self._nodeContent.setLayout(self._nodeContentLayout)

        # Change the palette background so that the widgets look seamless
        palette = self._nodeContent.palette()
        palette.setColor(self._nodeContent.backgroundRole(), QColor(QpnSettings.NodeContentBackgroundColor))
        self._nodeContent.setPalette(palette)
        self._nodeContent.setFixedSize(0, 0)

        # Title Bar Text
        # QPainterPath has the ability to get the rendered width (used for determining if the node needs to be resized)
        self._path_title_text = QPainterPath()
        self._path_title_text.setFillRule(Qt.WindingFill)
        self._path_title_text.addText(QPointF(QpnSettings.NodePadding, self._titleBarHeight - QpnSettings.NodePadding),
                                      QFont(QpnSettings.NodeTitleFont, QpnSettings.NodeTitleFontSize),
                                      self._title)

        self.width = max(self.width, int(self._path_title_text.boundingRect().width() + (QpnSettings.NodePadding * 2)))
        self.baseHeight = self.height
        self._nodeContent.setGeometry(QpnSettings.NodeEdgeRoundness,
                                      int(self._titleBarHeight) + QpnSettings.NodeEdgeRoundness,
                                      int(self.width) - 2 * QpnSettings.NodeEdgeRoundness,
                                      int(self.height) - 2 * QpnSettings.NodeEdgeRoundness - int(self._titleBarHeight))

        self._nodeContentProxy = QGraphicsProxyWidget(self)
        self._nodeContentProxy.setWidget(self._nodeContent)


    def _load_ui(self):
        self.title = self._algorithm.name
        # TODO: add input/output types being QpnDataType types

        for input in self._algorithm.inputs:
            if isinstance(input.dataType, QpnSocketDataType):
                #################
                # QPN Data Type #
                #################
                if input.dataType.atLeast(QpnDataType.Color):
                    colorInputText = QLineEdit('#FFFFFF')
                    self.addInput(input.dataType, input.description, input.toolTip, colorInputText)
                elif input.dataType.atLeast(QpnDataType.Enum):
                    self.addLabel(input.description)
                    enumInputList = QComboBox()
                    # FIXME: add the actual values from the API
                    if input.options is None:
                        enumInputList.addItem("Option A", 0)
                        enumInputList.addItem("Option B", 1)
                        enumInputList.addItem("Option C", 2)
                        enumInputList.addItem("Option D", 3)
                    else:
                        paramOptions = input.options
                        if 'enumValues' in paramOptions:
                            for value in paramOptions['enumValues']:
                                enumInputList.addItem(str(value[1]), str(value[0]))
                            if 'defaultValue' in paramOptions:
                                # FIXME: actually find the index for the default value
                                enumInputList.setCurrentIndex(0)
                    self.addInput(input.dataType, input.description, input.toolTip, enumInputList)
                elif input.dataType.atLeast(QpnDataType.String):
                    self.addLabel(input.description)
                    stringInputText = QLineEdit()
                    self.addInput(input.dataType, input.description, input.toolTip, stringInputText)
                elif input.dataType.atLeast(QpnDataType.Boolean):
                    booleanInputWidget = QCheckBox(input.description)
                    booleanInputWidget.setChecked(False)
                    self.addInput(input.dataType, input.description, input.toolTip, booleanInputWidget)
                elif input.dataType.atLeast(QpnDataType.Numeric):
                    self.addLabel(input.description)
                    numberInputText = QDoubleSpinBox()

                    numberInputText.setValue(0.0)
                    if input.options is not None:
                        if 'minValue' in input.options:
                            numberInputText.setMinimum(float(input.options['minValue']))
                        if 'maxValue' in input.options:
                            numberInputText.setMaximum(float(input.options['maxValue']))
                        if 'defaultValue' in input.options:
                            numberInputText.setValue(input.options['defaultValue'])

                    self.addInput(input.dataType, input.description, input.toolTip, numberInputText)
                else:
                    # Regular socket, no input widget
                    self.addInput(input.dataType, input.description, input.toolTip)

            else:
                ############################
                # QGIS internal data types #
                ############################

                # FIXME: unimplemented data type
                if input.dataType == 'aggregates':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name), 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType), 'QpnAlgorithm._initAlg()')

                elif input.dataType == 'alignrasterlayers':
                    self.addInput(QpnDataType.MultiRasterLayers, input.description, input.toolTip)

                elif input.dataType == 'area':
                    self.addLabel(input.description)
                    areaInputText = QDoubleSpinBox()
                    areaInputText.setValue(0.0)
                    self.addInput(QpnDataType.Area, input.description, input.toolTip, areaInputText)

                elif input.dataType == 'attribute':
                    self.addInput(QpnDataType.Field, input.description, input.toolTip)

                elif input.dataType == 'authcfg':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'band':
                    self.addInput(QpnDataType.RasterBand, input.description, input.toolTip)

                elif input.dataType == 'boolean':
                    booleanInputWidget = QCheckBox(input.description)
                    booleanInputWidget.setChecked(False)
                    self.addInput(QpnDataType.Boolean, input.description, input.toolTip, booleanInputWidget)

                elif input.dataType == 'color':
                    self.addLabel(input.description)
                    colorInputText = QLineEdit('#FFFFFF')
                    self.addInput(QpnDataType.Color, input.description, input.toolTip, colorInputText)

                elif input.dataType == 'coordinateoperation':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'crs':
                    self.addInput(QpnDataType.CoordinateSystem, input.description, input.toolTip)

                elif input.dataType == 'databaseschema':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'databasetable':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'distance':
                    self.addLabel(input.description)
                    distanceInputText = QDoubleSpinBox()
                    distanceInputText.setValue(0.0)
                    self.addInput(QpnDataType.Distance, input.description, input.toolTip, distanceInputText)

                elif input.dataType == 'duration':
                    self.addLabel(input.description)
                    durationInputText = QDoubleSpinBox()
                    durationInputText.setValue(0.0)
                    self.addInput(QpnDataType.Duration, input.description, input.toolTip, durationInputText)

                elif input.dataType == 'dxflayers':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'enum':
                    self.addLabel(input.description)
                    enumInputList = QComboBox()
                    # FIXME: add the actual values from the API
                    enumInputList.addItem("Option A", 0)
                    enumInputList.addItem("Option B", 1)
                    enumInputList.addItem("Option C", 2)
                    enumInputList.addItem("Option D", 3)
                    self.addInput(QpnDataType.Enum, input.description, input.toolTip, enumInputList)

                elif input.dataType == 'execute_sql':
                    self.addLabel(input.description)
                    sqlInputText = QLineEdit()
                    self.addInput(QpnDataType.String, input.description, input.toolTip, sqlInputText)

                elif input.dataType == 'expression':
                    self.addLabel(input.description)
                    expressionInputText = QLineEdit()
                    self.addInput(QpnDataType.Expression, input.description, input.toolTip, expressionInputText)

                elif input.dataType == 'extent':
                    self.addInput(QpnDataType.Extent, input.description, input.toolTip)

                elif input.dataType == 'field':
                    self.addInput(QpnDataType.Field, input.description, input.toolTip)

                elif input.dataType == 'fields_mapping':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'file':
                    self.addLabel(input.description)
                    fileInputText = QLineEdit()
                    self.addInput(QpnDataType.FileReader, input.description, input.toolTip, fileInputText)

                elif input.dataType == 'fileDestination':
                    self.addLabel(input.description)
                    fileWriterInputText = QLineEdit()
                    self.addInput(QpnDataType.FileWriter, input.description, input.toolTip, fileWriterInputText)

                elif input.dataType == 'folderDestination':
                    self.addLabel(input.description)
                    folderInputText = QLineEdit()
                    self.addInput(QpnDataType.FolderWriter, input.description, input.toolTip, folderInputText)

                elif input.dataType == 'geometry':
                    self.addInput(QpnDataType.VectorGeometry, input.description, input.toolTip)

                elif input.dataType == 'idw_interpolation_data':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                # This is a generic layer param. Takes raster or vector
                elif input.dataType == 'layer':
                    self.addInput(QpnDataType.DataLayer, input.description, input.toolTip)

                elif input.dataType == 'layout':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'layoutitem':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'maptheme':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'band':
                    self.addInput(QpnDataType.Matrix, input.description, input.toolTip)

                elif input.dataType == 'mesh':
                    self.addInput(QpnDataType.MeshLayer, input.description, input.toolTip)

                elif input.dataType == 'meshdatasetgroups':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'meshdatasettime':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                # Generic catch-all for vector and/or raster layers
                elif input.dataType == 'multilayer':
                    self.addInput(QpnDataType.MultiVectorLayers, input.description, input.toolTip)

                elif input.dataType == 'number':
                    self.addLabel(input.description)
                    numberInputText = QDoubleSpinBox()
                    numberInputText.setValue(0.0)
                    self.addInput(QpnDataType.Numeric, input.description, input.toolTip, numberInputText)

                elif input.dataType == 'point':
                    self.addInput(QpnDataType.PointGeometry, input.description, input.toolTip)

                elif input.dataType == 'pointcloud':
                    self.addInput(QpnDataType.PointCloudLayer, input.description, input.toolTip)

                elif input.dataType == 'pointCloudDestination':
                    self.addInput(QpnDataType.PointCloudLayerWriter, input.description, input.toolTip)

                elif input.dataType == 'providerconnection':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'raster':
                    self.addInput(QpnDataType.RasterLayer, input.description, input.toolTip)

                elif input.dataType == 'raster_calc_expression':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                # This is the same as a feature sink, but for rasters.
                # This input defines where the output goes
                # TODO: implement a handler for these
                elif input.dataType == 'rasterDestination':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'relief_colors':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'scale':
                    self.addLabel(input.description)
                    scaleInputText = QDoubleSpinBox()
                    scaleInputText.setValue(0.0)
                    self.addInput(QpnDataType.MapScale, input.description, input.toolTip, scaleInputText)

                # This input defines where the output goes
                # TODO: implement a handler for these
                elif input.dataType == 'sink':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'source':
                    self.addInput(QpnDataType.VectorFeature, input.description, input.toolTip)

                elif input.dataType == 'string':
                    self.addLabel(input.description)
                    stringInputText = QLineEdit()
                    self.addInput(QpnDataType.String, input.description, input.toolTip, stringInputText)

                elif input.dataType == 'tininputlayers':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                elif input.dataType == 'vector':
                    self.addInput(QpnDataType.VectorLayer, input.description, input.toolTip)

                # Same as sink
                # TODO: implement this
                elif input.dataType == 'vectorDestination':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(input.name),
                                      'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

                # Output folder
                elif input.dataType == 'vectorTileDestination':
                    self.addLabel(input.description)
                    vectorTileDestinationInputText = QLineEdit()
                    self.addInput(QpnDataType.FolderWriter, input.description, input.toolTip, vectorTileDestinationInputText)

                elif input.dataType == 'vectortilewriterlayers':
                    self.addInput(QpnDataType.MultiVectorLayers, input.description, input.toolTip)

                else:
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented input data type: {}".format(input.dataType),
                                      'QpnAlgorithm._initAlg()')

        for output in self._algorithm.outputs:
            if isinstance(output.dataType, QpnSocketDataType):
                self.addOutput(output.dataType, output.description, None)
                pass
            else:
                if output.dataType == 'outputBoolean':
                    self.addOutput(QpnDataType.Boolean, output.description, None)

                elif output.dataType == 'outputFile':
                    self.addOutput(QpnDataType.File, output.description, None)

                elif output.dataType == 'outputFolder':
                    self.addOutput(QpnDataType.Folder, output.description, None)

                elif output.dataType == 'outputHtml':
                    self.addOutput(QpnDataType.String, output.description, None)

                elif output.dataType == 'outputLayer':
                    self.addOutput(QpnDataType.VectorLayer, output.description, None)

                elif output.dataType == 'outputMultilayer':
                    self.addOutput(QpnDataType.MultiVectorLayers, output.description, None)

                elif output.dataType == 'outputNumber':
                    self.addOutput(QpnDataType.Numeric, output.description, None)

                elif output.dataType == 'outputPointCloud':
                    self.addOutput(QpnDataType.PointCloudLayer, output.description, None)

                elif output.dataType == 'outputRaster':
                    self.addOutput(QpnDataType.RasterLayer, output.description, None)

                elif output.dataType == 'outputString':
                    self.addOutput(QpnDataType.String, output.description, None)

                # TODO: implement this
                elif output.dataType == 'outputVariant':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented output data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(output.name), 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(output.dataType), 'QpnAlgorithm._initAlg()')

                elif output.dataType == 'outputVector':
                    self.addOutput(QpnDataType.VectorLayer, output.description, None)

                # TODO: implement this
                elif output.dataType == 'outputVectorTile':
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented output data type", 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Algorithm: {}".format(output.name), 'QpnAlgorithm._initAlg()')
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "    Data Type: {}".format(output.dataType), 'QpnAlgorithm._initAlg()')

                else:
                    QpnLog.LogMessage(QpnLog.MessageType.Error, "Unimplemented output data type: {}".format(output.dataType), 'QpnAlgorithm._initAlg()')

    @property
    def title(self):
        """The node's title text"""
        return self._title
    @title.setter
    def title(self, value: str):
        # TODO: add code to check the width if the widget will need to be resized
        if value.strip() != '': 
            self._title = value
            self._path_title_text.clear()
            self._path_title_text.addText(
                QPointF(QpnSettings.NodePadding, self._titleBarHeight - QpnSettings.NodePadding),
                QFont(QpnSettings.NodeTitleFont, QpnSettings.NodeTitleFontSize, QFont.Medium),
                self._title)
            self.width = max(self.width, int(self._path_title_text.boundingRect().width() + (QpnSettings.NodePadding * 2)))

    def addWidget(self, widget: QWidget) -> float:
        """
        Description: Adds a widget to the node's content.
        Parameters
        ----------
            widget : QWidget
                A QWidget that is to be added to the node's content.
        Returns
        -------
            float
                The y position of the midpoint of the added widget for positioning a socket.
        """
        self._nodeContent.layout().addWidget(widget)

        # Calculate the new width of the node content
        newWidth = int(max(self.width - 2*QpnSettings.NodeEdgeRoundness, widget.sizeHint().width()))
        # Update the node content's size
        self._nodeContent.setFixedSize(newWidth, int(self._nodeContent.height() + widget.sizeHint().height()))
        return self._nodeContent.height() - (widget.sizeHint().height()/2)


    def addLabel(self, labelText: str):
        """Add a label to the node's content with no input/output socket
        Parameters
        ----------
            labelText : str
                The text for the label
        """
        self.addWidget(QLabel(labelText))

        self.height = self.baseHeight + self._nodeContent.height()
        self.width = self._nodeContent.width() + 2 * QpnSettings.NodeEdgeRoundness


    def addInput(self, dataType: QpnSocketDataType, name: str, tooltip: str, widget = None):
        """Add an input socket to the node
        Parameters
        ----------
            dataType : QpnSocketDataType
                The data type of the input socket
            name : str
                The name of the input socket to be used as the input's label in the UI
            tooltip : str
                The tooltip text of the input socket
            widget : QWidget, optional
                The widget to be used for the input socket. If None, the input socket will be given just a label
        """
        # QpnLog.LogMessage(QpnLog.MessageType.Debug, dataType, 'QpnNode.addInput()')
        socket = QpnSocket(dataType, name, tooltip, QpnSocketSide.INPUT, self)

        # If no input widget was passed, just create a label with the input name
        if widget is None:
            widget = QLabel(name)
            widget.setFixedHeight(25)

        # TODO: Add ID-based access of the input widgets (i.e. inputWidgets['INPUT'].getValue())
        self.inputWidgets.append(None if isinstance(widget, QLabel) else widget)

        # Add the widget to the node content
        socketY = self.addWidget(widget)
        self.height = self.baseHeight + self._nodeContent.height()
        self.width = self._nodeContent.width() + 2 * QpnSettings.NodeEdgeRoundness

        _x_pos = 0.0
        _y_pos = socketY + self._titleBarHeight + QpnSettings.NodeEdgeRoundness
        index = len(self.inputs)

        socket.setPos(_x_pos, _y_pos)

        # Add the socket to the node
        self.inputs.append(socket)


    def addOutput(self, dataType: QpnSocketDataType, name: str, tooltip: str):
        """Add an output socket to the node
        Parameters
        ----------
            dataType : QpnSocketDataType
                The data type of the output socket
            name : str
                The name of the input socket to be used as the output's label in the UI
            tooltip : str
                The tooltip text of the output socket
        """
        socket = QpnSocket(dataType, name, tooltip, QpnSocketSide.OUTPUT, self)

        tempLabel = QLabel(name)
        tempLabel.setFixedHeight(25)
        tempLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Add the widget to the node content
        socketY = self.addWidget(tempLabel)
        self.height = self.baseHeight + self._nodeContent.height()
        self.width = self._nodeContent.width() + 2 * QpnSettings.NodeEdgeRoundness

        _x_pos = self.width
        index = len(self.outputs)

        _y_pos = socketY + self._titleBarHeight + QpnSettings.NodeEdgeRoundness

        socket.setPos(_x_pos, _y_pos)

        # Add the socket to the node
        self.outputs.append(socket)
        self.widthChanged()


    def Icon(self, icon):
        """Add or change the icon associated with the node's title (NOT IMPLEMENTED)"""
        pass


    def RemoveSocket(self):
        """Remove a socket from the node (NOT IMPLEMENTED)"""
        pass


    def boundingRect(self) -> QRectF:
        """Qt Callback: (REQUIRED) returns the bounding box area of the graphics item."""
        return QRectF(0, 0, 2 * QpnSettings.NodeEdgeRoundness + self.width, 2 * QpnSettings.NodeEdgeRoundness + self.height).normalized()


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget=None):
        """Qt Callback: (REQUIRED) draws the node onto the painter object."""
        # Title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self._titleBarHeight, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_title.addRect(0, self._titleBarHeight - QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_title.addRect(self.width - QpnSettings.NodeEdgeRoundness, self._titleBarHeight - QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        # Title Text
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor('#ffffff'))
        painter.drawPath(self._path_title_text)

        # Content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self._titleBarHeight, self.width, self.height - self._titleBarHeight, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_content.addRect(0, self._titleBarHeight, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        path_content.addRect(self.width - QpnSettings.NodeEdgeRoundness, self._titleBarHeight, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

        # Outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0, 0, self.width, self.height, QpnSettings.NodeEdgeRoundness, QpnSettings.NodeEdgeRoundness)
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())


    def widthChanged(self):
        """Updates the graphics elements when a node's width is changed"""
        for i in self.outputs:
            i.setPos(self.width, i.y())


    def adjustSize(self):
        """Updates the graphics elements when a node's size is changed (NOT IMPLEMENTED)"""
        pass
