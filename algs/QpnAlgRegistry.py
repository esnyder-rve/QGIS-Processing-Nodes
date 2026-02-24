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
        self._algsList[QPN.QpnIteratorForEachFeature.algName] = QPN.QpnIteratorForEachFeature
        self._algsList[QPN.QpnIteratorForEachVectorLayer.algName] = QPN.QpnIteratorForEachVectorLayer
        self._algsList[QPN.QpnIteratorForEachRasterBand.algName] = QPN.QpnIteratorForEachRasterBand
        self._algsList[QPN.QpnBranchJoiner.algName] = QPN.QpnBranchJoiner
        self._algsList[QPN.QpnConditionalIf.algName] = QPN.QpnConditionalIf
        self._algsList[QPN.SagaFlowAccumulationD8.algName] = QPN.SagaFlowAccumulationD8
        self._algsList[QPN.SagaFlowAccumulationMFD.algName] = QPN.SagaFlowAccumulationMFD

    def algorithms(self) -> List[QpnAlgorithm]:
        # return list of algs
        return list(self._algsList.values())

    def algorithmById(self, algId) -> QpnAlgorithm:
        return self._algsList[algId]

