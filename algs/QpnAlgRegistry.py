from typing import List, Self, Dict
import algs.QPN as QPN
from QpnAlgorithm import QpnAlgorithm

from Singleton import Singleton


class QpnAlgRegistry(metaclass=Singleton):
    def __init__(self):
        self._algsList : Dict[str: QpnAlgorithm] = {}
        self.refreshDB()

    def instance(self) -> Self:
        return self

    def refreshDB(self):
        self._algsList.clear()
        self._algsList[QPN.QpnAlgModelInput.algName] = QPN.QpnAlgModelInput
        self._algsList[QPN.QpnAlgModelOutput.algName] = QPN.QpnAlgModelOutput
        self._algsList[QPN.QpnAlgTestNode.algName] = QPN.QpnAlgTestNode
        self._algsList[QPN.QpnRasterBandSelector.algName] = QPN.QpnRasterBandSelector

    def algorithms(self) -> List[QpnAlgorithm]:
        # return list of algs
        return list(self._algsList.values())

    def algorithmById(self, algId) -> QpnAlgorithm:
        return self._algsList[algId]

