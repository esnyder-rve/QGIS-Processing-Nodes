from typing import Self

class QpnSocketDataType():

    def __init__(self, dataType: str, description: str, subType: Self = None):
        self._dataType = dataType
        self._description = description
        self._subType = subType


    @classmethod
    def copy(cls, other: Self):
        return cls(other._dataType, other._description, other._subType)


    def __eq__(self, other):
        return self.dataType == other.dataType and self.subType == other.subType


    def __str__(self):
        return self._dataType + ('' if self._subType is None else '.' + self._subType.__str__())


    # VectorLayer.Point.atLeast(VectorLayer)
    def atLeast(self, other):
        if self._dataType == other._dataType:
            if other._subType and self._subType:
                return self._subType.atLeast(other._subType)
            elif other._subType is None:
                return True
            elif self._subType is None and other.subType is not None:
                return False
            else:
                return True
        return False


    @property
    def dataType(self):
        """The dataType property."""
        return self._dataType
    @dataType.setter
    def dataType(self, value):
        self._dataType = value


    @property
    def description(self):
        """The description property."""
        return self._description
    @description.setter
    def description(self, value):
        self._description = value


    @property
    def subType(self):
        """The subType property."""
        return self._subType
    @subType.setter
    def subType(self, value):
        self._subType = value


    def setSubType(self, subType: Self):
        self._subType = subType
        return self


    def addSubType(self, subType: Self):
        if self._subType is None:
            self._subType = subType
        else:
            self._subType.addSubType(subType)
        return self


class QpnDataSubTypes():
    """QPN Data subtypes.
    
    Description:
        This class is intended to hold sub-types for nesting, and shouldn't be used directly by
        the user. These types will include vector geometry type (point, line, poly), geometry
        attributes (z, m), underlying raster band data type, and other sub-types
    """
    # Vector related subs:
    # Nesting Order: Vector->Pt/Line/Poly->Z/M
    Z_Geom = QpnSocketDataType('Z', 'Z Geometry', None)
    M_Geom = QpnSocketDataType('M', 'M Geometry', None)
    ZM_Geom = QpnSocketDataType('ZM', 'Z & M Geometry', None)
    Any_Geom = QpnSocketDataType('Any', 'Any Geometry Type', None)
    Point_Geom = QpnSocketDataType('Point', 'Point Geometry', None)
    Multi_Point_Geom = QpnSocketDataType('MultiPoint', 'Multi-Point Geometry', None)
    Line_Geom = QpnSocketDataType('Line', 'Line Geometry', None)
    Multi_Line_Geom = QpnSocketDataType('MultiLine', 'Multi-Line Geometry', None)
    Curve_Line_Geom = QpnSocketDataType('CurveLine', 'Curve-Line Geometry', None)
    Multi_Curve_Line_Geom = QpnSocketDataType('MultiCurveLine', 'Mutli-Curve-Line Geometry', None)
    Poly_Geom = QpnSocketDataType('Poly', 'Poly Geometry', None)
    Multi_Poly_Geom = QpnSocketDataType('MultiPoly', 'Multi-Polygon Geometry', None)
    Curve_Poly_Geom = QpnSocketDataType('CurvePoly', 'Curve-Polygon Geometry', None)
    Multi_Curve_Poly_Geom = QpnSocketDataType('MultiCurvePoly', 'Mutli-Curve-Polygon Geometry', None)
    Area = QpnSocketDataType('Area', 'Area', None)
    Distance = QpnSocketDataType('Distance', 'Distance', None)
    Duration = QpnSocketDataType('Duration', 'Time duration', None)
    Enum = QpnSocketDataType('Enumeration', 'Enumeration', None)
    Expression = QpnSocketDataType('Expression', 'Expression', None)
    File = QpnSocketDataType('File', 'File Path', None)
    Folder = QpnSocketDataType('Folder', 'Folder Path', None)
    Reader = QpnSocketDataType('Reader', 'Reads Input', None)
    Writer = QpnSocketDataType('Writer', 'Writes Output', None)
    MapScale = QpnSocketDataType('MapScale', 'Map Scale', None)


class QpnDataType():
    # These are the main data types to work with
    DataLayer = QpnSocketDataType('DataLayer', 'General Data Layer (Vector or Raster)', None)
    MultiDataLayer = QpnSocketDataType('MultiDataLayer', 'General Multi Data Layer (Vector and/or Raster)', None)
    VectorLayer = QpnSocketDataType('VectorLayer', 'General Vector Layer', None)
    MultiVectorLayers = QpnSocketDataType('MultiVectorLayers', 'Multiple Vector Layers', None)
    VectorFeature = QpnSocketDataType('VectorFeature', 'General Vector Feature', None)
    VectorGeometry = QpnSocketDataType('VectorGeometry', 'General Vector Geometry', None)
    PointGeometry = QpnSocketDataType.copy(VectorGeometry).addSubType(QpnDataSubTypes.Point_Geom)
    LineGeometry = QpnSocketDataType.copy(VectorGeometry).addSubType(QpnDataSubTypes.Line_Geom)
    PolygonGeometry = QpnSocketDataType.copy(VectorGeometry).addSubType(QpnDataSubTypes.Poly_Geom)
    RasterLayer = QpnSocketDataType('RasterLayer', 'General Raster Layer', None)
    MultiRasterLayers = QpnSocketDataType('MultiRasterLayers', 'Multiple Raster Layers', None)
    RasterBand = QpnSocketDataType('RasterBand', 'Raster Band', None)
    MeshLayer = QpnSocketDataType('MeshLayer', 'Mesh Layer', None)
    PointCloudLayer = QpnSocketDataType('PointCloudLayer', 'Point Cloud Layer', None)
    PointCloudLayerWriter = QpnSocketDataType.copy(PointCloudLayer).addSubType(QpnDataSubTypes.Writer)
    Field = QpnSocketDataType('Field', 'Attribute Field', None)
    Extent = QpnSocketDataType('Extent', 'Geographic Extent', None)
    String = QpnSocketDataType('String', 'String', None)
    Color = QpnSocketDataType('Color', 'Color', None)
    CoordinateSystem = QpnSocketDataType('CoordinateSystem', 'Coordinate System', None)
    Boolean = QpnSocketDataType('Boolean', 'Boolean', None)
    AddWild = QpnSocketDataType('AddWild', 'Add new socket...', None)
    Numeric = QpnSocketDataType('Numeric', 'Number', None)
    Matrix = QpnSocketDataType('Matrix', 'Matrix or Table of any type', None)
    Distance = QpnSocketDataType.copy(Numeric).addSubType(QpnDataSubTypes.Distance)
    Area = QpnSocketDataType.copy(Numeric).addSubType(QpnDataSubTypes.Area)
    Duration = QpnSocketDataType.copy(Numeric).addSubType(QpnDataSubTypes.Duration)
    Enum = QpnSocketDataType.copy(Numeric).addSubType(QpnDataSubTypes.Enum)
    Expression = QpnSocketDataType.copy(String).addSubType(QpnDataSubTypes.Expression)
    File = QpnSocketDataType.copy(String).addSubType(QpnDataSubTypes.File)
    Folder = QpnSocketDataType.copy(String).addSubType(QpnDataSubTypes.Folder)
    FileReader = QpnSocketDataType.copy(File).addSubType(QpnDataSubTypes.Reader)
    FolderReader = QpnSocketDataType.copy(Folder).addSubType(QpnDataSubTypes.Reader)
    FileWriter = QpnSocketDataType.copy(File).addSubType(QpnDataSubTypes.Writer)
    FolderWriter = QpnSocketDataType.copy(Folder).addSubType(QpnDataSubTypes.Writer)
    MapScale = QpnSocketDataType.copy(Numeric).addSubType(QpnDataSubTypes.MapScale)
