import json
from typing import List, Self, Dict
from QpnAlgorithm import QpnAlgorithm, QpnAlgorithmInput, QpnAlgorithmOutput

from Singleton import Singleton

class TEMP_QgsAlgsRegistry(metaclass=Singleton):
    def __init__(self):
        self._jsonDB = None
        self._algsList : Dict[str: QpnAlgorithm] = {}
        self.refreshDB()

    def instance(self) -> Self:
        return self

    def refreshDB(self):
        # Load JSON here
        self._algsList.clear()
        file = open("qgis_algs_v4.json", "r")
        self._jsonDB = json.load(file)
        file.close()

        for algId, algDetails in self._jsonDB.items():
            newAlg = QpnAlgorithm(algId, algDetails['NAME'], '')
            newAlg.provider = algDetails['PROVIDER']
            newAlg.group = algDetails['GROUP']

            # TODO: port these over to QpnAlgorithm
            for input, inputParams in algDetails['INPUTS'].items():
                newInput = QpnAlgorithmInput(input, inputParams['TYPE'], inputParams['DESCRIPTION'], inputParams['TOOLTIP'], inputParams['IS_DESTINAION'], inputParams['IS_DYNAMIC'])
                # TODO: Add parameter options (i.e. min/max, default value, dropdown items, etc...)
                newAlg.addInput(newInput)

            for output, outputParams in algDetails['OUTPUTS'].items():
                newOutput = QpnAlgorithmOutput(output, outputParams['TYPE'], outputParams['DESCRIPTION'], '', outputParams['AUTOCREATED'])
                newAlg.addOutput(newOutput)

            self._algsList[algId] = newAlg
    
    def algorithms(self) -> List[QpnAlgorithm]:
        # return list of algs
        return list(self._algsList.values())

    def algorithmById(self, algId) -> QpnAlgorithm:
        return self._algsList[algId]

