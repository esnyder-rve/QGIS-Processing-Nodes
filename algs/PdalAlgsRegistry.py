from typing import List, Self, Dict
import algs.PDAL as PDAL
from QpnAlgorithm import QpnAlgorithm

from Singleton import Singleton


class PdalAlgRegistry(metaclass=Singleton):
    def __init__(self):
        self._algsList : Dict[str: QpnAlgorithm] = {}
        self.refreshDB()

    def instance(self) -> Self:
        return self

    def refreshDB(self):
        self._algsList.clear()
        self._algsList[PDAL.PdalAlgPipeline.algName] = PDAL.PdalAlgPipeline
        self._algsList[PDAL.PdalPipelineReaderArrow.algName] = PDAL.PdalPipelineReaderArrow
        self._algsList[PDAL.PdalPipelineReaderBpf.algName] = PDAL.PdalPipelineReaderBpf
        self._algsList[PDAL.PdalPipelineReaderCopc.algName] = PDAL.PdalPipelineReaderCopc
        self._algsList[PDAL.PdalPipelineWriterArrow.algName] = PDAL.PdalPipelineWriterArrow
        self._algsList[PDAL.PdalPipelineFilterCsf.algName] = PDAL.PdalPipelineFilterCsf
        self._algsList[PDAL.PdalPipelineFilterPmf.algName] = PDAL.PdalPipelineFilterPmf
        self._algsList[PDAL.PdalPipelineFilterSkewnessBalancing.algName] = PDAL.PdalPipelineFilterSkewnessBalancing
        self._algsList[PDAL.PdalPipelineFilterSmrf.algName] = PDAL.PdalPipelineFilterSmrf
        self._algsList[PDAL.PdalPipelineFilterSparseSurface.algName] = PDAL.PdalPipelineFilterSparseSurface
        self._algsList[PDAL.PdalPipelineFilterTrajectory.algName] = PDAL.PdalPipelineFilterTrajectory

    def algorithms(self) -> List[QpnAlgorithm]:
        # return list of algs
        return list(self._algsList.values())

    def algorithmById(self, algId) -> QpnAlgorithm:
        return self._algsList[algId]

