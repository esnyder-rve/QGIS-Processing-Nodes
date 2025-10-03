# This wrapper class is responsible for all interactions between QPN and the algorithms and actual processing
# The purpose of this wrapper is to provide a single API to QGIS algorithms, and built-in QPN algorithms (whether real, or pseudo)
# This class will also be responsible for adding any additional "provider" that may come into play outside the usual 2 methods above
# This class is intended to be a pass-through class

from typing import List, Self
from PyQt5.QtGui import QIcon
from QpnAlgorithm import QpnAlgorithm, QpnAlgorithmInput, QpnAlgorithmOutput

class QpnAlgorithmWrapper():
    def __init__(self, algorithm: QpnAlgorithm | None = None):
        # Can be of the following types:
        #  * QgsProcessingAlgorithm (any algorithm provided through the QGIS processing registry)
        #  * QpnAlgorithm (QPN specific algorithms, not exposed to the QGIS processing registry)
        # TODO: add QgsProcessingAlgorithm to the list of acceptable types
        self._algorithm: QpnAlgorithm | None = algorithm

    @property
    def algId(self) -> str | None:
        """
        Description: Get the algorithm ID (provider:name)

        Returns:
        --------
            str | None
                The ID of the algorithm
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.algID

        return None

    @property
    def name(self) -> str | None:
        """
        Description: Get the name of the algorithm. Technically, the name() of an algorithm
        (according to the QGIS API) is the right-hand portion of the ID (i.e. gdal:buildvirtualraster
        would return "buildvirtualraster"). However, this isn't very useful. This function instead
        returns the useful, visual name of the algorithm.

        Returns
        -------
            str | None
                The name of the algorithm, or None if no name exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.algName

        return None


    @property
    def description(self) -> str | None:
        """
        Description: Get the description of the algorithm.

        Returns
        -------
            str | None
                The description of the algorithm, or None if none exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.description

        return None

    @property
    def group(self) -> str | None:
        """
        Description: Get the group name that contains the algorithm.

        Returns
        -------
            str | None
                The group name for the algorithm, or None if none exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.group

        return None

    @property
    def provider(self) -> str | None:
        """
        Description: Get the provider name of the algorithm.

        Returns
        -------
            str | None
                The provider name of the algorithm, or None if none exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.provider

        return None


    @property
    def algorithmIcon(self) -> QIcon | None:
        """
        Description: Get the icon of the algorithm.

        Returns
        -------
            QIcon | None
                The icon of the algorithm, or None if none exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            pass

        return None

    @property
    def inputs(self) -> List[QpnAlgorithmInput] | None:
        """
        Description: Get the list of inputs for the algorithm.

        Returns
        -------
            List | None
                The list of inputs for the algorithm, or None if none exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.inputs

        return None


    @property
    def outputs(self) -> List[QpnAlgorithmOutput] | None:
        """
        Description: Get the list of outputs for the algorithm.

        Returns
        -------
            List | None
                The list of outputs for the algorithm, or None if none exists, or this wrapper is empty
        """
        if isinstance(self._algorithm, QpnAlgorithm):
            return self._algorithm.outputs

        return None


    def exec(self):
        pass

    ###################
    # Factory Methods #
    ###################

    @classmethod
    def fromQgisAlgorithm(cls, qgisAlgorithm) -> Self:
        newAlg = cls()
        return newAlg

    @classmethod
    def fromQpnAlgorithm(cls, qpnAlgorithm) -> Self:
        newAlg = cls()
        return newAlg