class QpnAlgorithmDB():
    def __init__(self):
        pass


    @staticmethod
    def getAlgName(algID: str):
        return 'Buffer'


    @staticmethod
    def getAlgProvider(algID: str):
        return 'QGIS'


    @staticmethod
    def getAlgInputs(algID: str):
        inputs = [
                {
                    'Name': 'Input Layer',
                    'ID': 'INPUT',
                    'Type': ('QgsVectorLayer', 'Geometry:Any'),
                    'Default': None
                    },
                {
                    'Name': 'Distance',
                    'ID': 'DISTANCE',
                    'Type': ('Integer', None),
                    'Default': 10
                    },
                {
                    'Name': 'Segments',
                    'ID': 'SEGMENTS',
                    'Type': ('Integer', 'Integer:Positive'),
                    'Default': 5
                    },
                {
                    'Name': 'End Cap Style',
                    'ID': 'ENDCAPSTYLE',
                    'Type': ('Integer', 'Integer:Range(0, 4)'),
                    'Default': 0
                    },
                {
                    'Name': 'Join Style',
                    'ID': 'JOINSTYLE',
                    'Type': ('Integer', 'Integer:Range(0, 3)'),
                    'Default': 0
                    },
                {
                    'Name': 'Miter Limit',
                    'ID': 'MITER',
                    'Type': ('Float', 'Float:Positive'),
                    'Default': 2.00
                    },
                {
                    'Name': 'Dissolve Result',
                    'ID': 'DISSOLVE',
                    'Type': ('Boolean', None),
                    'Default': False
                    },
                {
                    'Name': 'Keep Disjoint Separate',
                    'ID': 'DISJOINT',
                    'Type': ('Boolean', None),
                    'Default': False
                    }
                ]
        return inputs


    @staticmethod
    def getAlgOutputs(algID: str):
        outputs = [
                {
                    'Name': 'Buffered',
                    'ID': 'OUTPUT',
                    'Type': ('QgsVectorLayer', 'Geometry:Polygon')
                    }
                ]
        return outputs
