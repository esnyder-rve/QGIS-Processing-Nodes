from typing import List, Dict, Callable
from QpnSocketDataType import QpnDataType, QpnSocketDataType
import QpnLog

# Notes:
#   Additional functions may need to be made from QgsProcessingAlgorithm, but as-needed
#   The QpnNode functionality needs to be stripped and moved to the QpnNode class. The node
#     will hold the algorithm as a member variable and populate itself from it. This suggestion
#     came from the OLC Discord

class QpnAlgorithmInput():
    def __init__(self, name: str, dataType: str | QpnDataType, description: str, toolTip: str, isDestination: bool, isDynamic: bool, options: Dict = None):
        self._name = name
        self._dataType = dataType
        self._description = description
        self._toolTip = toolTip
        self._isDestination = isDestination
        self._isDynamic = isDynamic
        self._options : Dict | None = options
        self._hasCustomUI : bool = False

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def dataType(self) -> str | QpnSocketDataType:
        return self._dataType
    @dataType.setter
    def dataType(self, dataType: str | QpnSocketDataType):
        self._dataType = dataType

    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def toolTip(self) -> str:
        return self._toolTip
    @toolTip.setter
    def toolTip(self, toolTip: str):
        self._toolTip = toolTip

    @property
    def isDestination(self) -> bool:
        return self._isDestination
    @isDestination.setter
    def isDestination(self, isDestination: bool):
        self._isDestination = isDestination

    @property
    def isDynamic(self) -> bool:
        return self._isDynamic
    @isDynamic.setter
    def isDynamic(self, isDynamic: bool):
        self._isDynamic = isDynamic

    @property
    def options(self) -> Dict:
        return self._options
    @options.setter
    def options(self, options: Dict):
        self._options = options

    @property
    def hasCustomUI(self) -> bool:
        return self._hasCustomUI
    @hasCustomUI.setter
    def hasCustomUI(self, hasCustomUI: bool):
        self._hasCustomUI = hasCustomUI


class QpnAlgorithmOutput():
    def __init__(self, name: str, dataType: str | QpnDataType, description: str, toolTip: str, autocreated: bool):
        self._name = name
        self._dataType = dataType
        self._description = description
        self._toolTip = toolTip
        self._autocreated = autocreated

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def dataType(self) -> str | QpnSocketDataType:
        return self._dataType
    @dataType.setter
    def dataType(self, dataType: str | QpnSocketDataType):
        self._dataType = dataType

    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def toolTip(self) -> str:
        return self._toolTip
    @toolTip.setter
    def toolTip(self, toolTip: str):
        self._toolTip = toolTip

    @property
    def autocreated(self) -> bool:
        return self._autocreated
    @autocreated.setter
    def autocreated(self, autocreated: bool):
        self._autocreated = autocreated


class QpnAlgorithm():
    """The holder class of a QGIS Processing Nodes algorithm.

    Description:
        This class holds all the information regarding a processing node.
        This is a small re-implementation of the QGIS processing algorithm class,
        but is intended to be light-weight for the QPN processing algs vs the
        entire processing framework.

    Properties:
        algID: The QGIS/QPN algorithm ID that is used to id the type of
            algorithm this node is executing. This cannot be edited by
            the user, and is set at creation.
        name: The visual name/title of the node. This can be user changed.
            Changing this will change the visual title on the node in the
            header.
        description: The long description of the node. This can be user
            changed. Changing this will change the description in the
            properties panel. Can be used to describe the purpose of the
            node in relation to the model. The default value will be the
            algorithm's description.
    """

    def __init__(self, algID: str = None, name: str = None, description: str = None):
        """Initializes the node using default, auto-generated contents.

        Parameters:
            algID: The QGIS algorithm ID for this processing node.
        """

        # Algorithm ID in QGIS notation (ex. 'qpn:modelinput')
        self._algID: str | None = algID

        # The display name of the algorithm/node that will show up as the title bar text
        # This value can be user modified
        self._name: str | None = name

        # The long description of the algorithm/node
        self._description: str | None = description

        # The help text for the algorithm/node that will be shown in the properties panel
        self._help: str | None = None

        # The provider name (defaults to QPN, as that's the main usage for this class)
        self._provider: str | None = 'QPN'

        # The group that the algorithm resides in, within it's provider
        self._group: str | None = None

        # The algorithm's tooltip when hovered over (can differ from description)
        self._tooltip: str | None = None

        self._inputs: List[QpnAlgorithmInput] = []

        self._outputs: List[QpnAlgorithmOutput] = []

        self._customExecFunc : Callable | None = None


    def addInput(self, input: QpnAlgorithmInput):
        """
        Description: Adds an input to the algorithm.

        Parameters
        ----------
            input : QpnAlgorithmInput
                The input to add.
        """
        self._inputs.append(input)

    def addOutput(self, output: QpnAlgorithmOutput):
        """
        Description: Adds an output to the algorithm.

        Parameters
        ----------
            output : QpnAlgorithmOutput
                The output to add.
        """
        self._outputs.append(output)

    ###################
    #    Property     #
    # Getters/Setters #
    ###################

    @property
    def algID(self):
        """The QGIS algorithm ID."""
        return self._algID
    @algID.setter
    def algID(self, value: str):
        """Set the QGIS algorithm ID. Cannot be changed if set."""
        if self._algID is None:
            self._algID = value
        else:
            QpnLog.LogMessage(QpnLog.MessageType.Error,
                              "Attempted to change algorithm ID for node, this should not be done. If you meant to do this, you're doing something wrong.",
                              "QpnAlgorithm.algID(str)")

    @property
    def algName(self):
        """The algorithm name."""
        return self._name
    @algName.setter
    def algName(self, value: str | None):
        """Set the algorithm name."""
        self._name = value

    @property
    def description(self):
        """The algorithm description."""
        return self._description
    @description.setter
    def description(self, value: str | None):
        """Set the algorithm description."""
        self._description = value

    @property
    def tooltip(self):
        """The algorithm tooltip."""
        return self._tooltip
    @tooltip.setter
    def tooltip(self, value: str | None):
        """Set the algorithm tooltip."""
        self._tooltip = value

    @property
    def group(self):
        """The group name for the algorithm."""
        return self._group
    @group.setter
    def group(self, value: str):
        """Set the group name for the algorithm."""
        self._group = value

    @property
    def provider(self):
        """The provider name for the algorithm."""
        return self._provider
    @provider.setter
    def provider(self, value: str):
        """Set the provider name for the algorithm."""
        self._provider = value

    @property
    def help(self):
        """The help text for the algorithm."""
        return self._help
    @help.setter
    def help(self, value: str):
        """Set the help text for the algorithm."""
        self._help = value

    @property
    def inputs(self) -> List[QpnAlgorithmInput]:
        """The inputs for the algorithm."""
        return self._inputs

    @property
    def outputs(self) -> List[QpnAlgorithmOutput]:
        """The outputs for the algorithm."""
        return self._outputs

    @property
    def executionFunction(self) -> Callable | None:
        return self._customExecFunc
    @executionFunction.setter
    def executionFunction(self, functionPointer: Callable):
        self._customExecFunc = functionPointer

    def execute(self, input):
        """Execute this node with the input"""
        if self._customExecFunc is None:
            print('Executing {}'.format(self.algName))
        else:
            output = self._customExecFunc(input)
            return output