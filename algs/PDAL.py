from QpnAlgorithm import QpnAlgorithm, QpnAlgorithmInput, QpnAlgorithmOutput
from QpnSocketDataType import QpnDataType

# PDAL Pipeline Top Level Node
PdalAlgPipeline = QpnAlgorithm('pdal:pipeline', 'PDAL Pipeline', 'Input parameters for the pipeline')
PdalAlgPipeline.help = """PDAL Pipeline
    This node is to run a PDAL pipeline on input. The sub structure of this node will house the
    components needed that will compile into a pipeline JSON script.
    Inputs: Whatever you need them to be
    Outputs: Whatever your pipeline outputs"""
PdalAlgPipeline.group = 'Pipeline'
PdalAlgPipeline.provider = 'PDAL'

PdalAlgPipeline.addInput(QpnAlgorithmInput('ADDNEW', QpnDataType.AddWild, "Add new input", 'Add new pipeline input', False, False))
PdalAlgPipeline.addOutput(QpnAlgorithmOutput('ADDNEW', QpnDataType.AddWild, "Add new output", 'Add new pipeline output', False))

######################
# Pipeline - Readers #
######################

# readers.arrow
PdalPipelineReaderArrow = QpnAlgorithm('pdal:pipelinereaderarrow', 'readers.arrow', 'PDAL GeoArrow/GeoParquet Reader')
PdalPipelineReaderArrow.help = """PDAL Pipeline - Readers - readers.arrow
    Read GeoArrow/GeoParquet formatted data"""
PdalPipelineReaderArrow.group = 'Pipeline - Readers'
PdalPipelineReaderArrow.provider = 'PDAL'

PdalPipelineReaderArrow.addInput(QpnAlgorithmInput('FILENAME', QpnDataType.File, "Input File", 'Input Arrow GeoArrow or GeoParquet file to read [Required]', False, False))
PdalPipelineReaderArrow.addInput(
    QpnAlgorithmInput(
        'FORMAT',
        QpnDataType.Enum,
        'Format',
        '`geoarrow` or `geoparquet` option to override any filename extension hinting of data type',
        False,
        False,
        {'enumValues':
             [
                 ('auto', 'auto'),
                 ('geoarrow', 'geoarrow'),
                 ('geoparquet', 'geoparquet')],
            'defaultValue': 'auto'}))
PdalPipelineReaderArrow.addInput(
    QpnAlgorithmInput(
        'COUNT',
        QpnDataType.Numeric,
        'Count',
        'Maximum number of points to read [Default: unlimited]',
        False,
        False,
        {'defaultValue': 0}
    )
)
PdalPipelineReaderArrow.addInput(
    QpnAlgorithmInput(
        'COORDINATESYSTEM',
        QpnDataType.CoordinateSystem,
        'Coordinate SystemOverride',
        'Coordinate system to either set to an unset dataset, or to override a provided one.',
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineReaderArrow.addInput(
    QpnAlgorithmInput(
        'SRSOVERRIDE',
        QpnDataType.Boolean,
        'Override SRS?',
        'Use the provided CRS to override the CRS of the input dataset.',
        False,
        False,
        {'defaultValue': False}
    )
)
PdalPipelineReaderArrow.addOutput(
    QpnAlgorithmOutput(
        'OUTPUT',
        QpnDataType.PointCloudLayer,
        'Point Cloud',
        'Output point cloud layer',
        False
    )
)

# readers.bpf
PdalPipelineReaderBpf = QpnAlgorithm('pdal:pipelinereaderbpf', 'readers.bpf', 'PDAL BPF Reader')
PdalPipelineReaderBpf.help = """PDAL Pipeline - Readers - readers.bpf
    Read BPF formatted data"""
PdalPipelineReaderBpf.group = 'Pipeline - Readers'
PdalPipelineReaderBpf.provider = 'PDAL'

PdalPipelineReaderBpf.addInput(
    QpnAlgorithmInput(
        'FILENAME',
        QpnDataType.File,
        "Input File",
        'Input BPF file to read [Required]',
        False,
        False
    )
)
PdalPipelineReaderBpf.addInput(
    QpnAlgorithmInput(
        'FIXDIMS',
        QpnDataType.Boolean,
        'Fix Dimensions',
        'BPF files may contain dimension names that aren\' allowed by PDAL. When this option is \'true\', invalid characters in dimension names are replaced by \'_\' in order to make the names valid.',
        False,
        False,
        {'defaultValue': True}
    )
)
PdalPipelineReaderBpf.addInput(
    QpnAlgorithmInput(
        'COUNT',
        QpnDataType.Numeric,
        'Count',
        'Maximum number of points to read [Default: unlimited]',
        False,
        False,
        {'defaultValue': 0}
    )
)
PdalPipelineReaderBpf.addInput(
    QpnAlgorithmInput(
        'COORDINATESYSTEM',
        QpnDataType.CoordinateSystem,
        'Coordinate SystemOverride',
        'Coordinate system to either set to an unset dataset, or to override a provided one.',
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineReaderBpf.addInput(
    QpnAlgorithmInput(
        'SRSOVERRIDE',
        QpnDataType.Boolean,
        'Override SRS?',
        'Use the provided CRS to override the CRS of the input dataset.',
        False,
        False,
        {'defaultValue': False}
    )
)
PdalPipelineReaderBpf.addOutput(
    QpnAlgorithmOutput(
        'OUTPUT',
        QpnDataType.PointCloudLayer,
        'Point Cloud',
        'Output point cloud layer',
        False
    )
)

PdalPipelineReaderCopc = QpnAlgorithm(
    'pdal:pipelinereadercopc',
    'readers.copc',
    'PDAL COPC Reader'
)
PdalPipelineReaderCopc.help = """PDAL Pipeline - Readers - readers.copc
    Read COPC formatted data"""
PdalPipelineReaderCopc.group = 'Pipeline - Readers'
PdalPipelineReaderCopc.provider = 'PDAL'

PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'FILENAME',
        QpnDataType.File,
        "Input File",
        'Input COPC file to read [Required]',
        False,
        False
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'COUNT',
        QpnDataType.Numeric,
        'Count',
        'Maximum number of points to read [Default: unlimited]',
        False,
        False,
        {'defaultValue': 0}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'COORDINATESYSTEM',
        QpnDataType.CoordinateSystem,
        'Coordinate SystemOverride',
        'Coordinate system to either set to an unset dataset, or to override a provided one.',
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'SRSOVERRIDE',
        QpnDataType.Boolean,
        'Override SRS?',
        'Use the provided CRS to override the CRS of the input dataset.',
        False,
        False,
        {'defaultValue': False}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'BOUNDS',
        QpnDataType.Extent,
        'Bounds',
        'The extent of the data to select in 2 or 3 dimensions.',
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'POLYGON',
        QpnDataType.PolygonGeometry,
        'Polygon Geometry',
        'The polygon geometry to clip the point cloud with.',
        False,
        False
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'REQUESTS',
        QpnDataType.Numeric,
        'Requests',
       'The number of worker threads processing data. The optimal number depends on your system and your network connection, but more is not necessarily better.',
        False,
        False,
        {'defaultValue': 15}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'RESOLUTION',
        QpnDataType.Numeric,
        'Resolution',
        'Limit the pyramid levels of data to fetch based on the expected resolution of the data. UNits match that of the data. Use -1 for no resolution limit',
        False,
        False,
        {'defaultValue': -1}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'HEADER',
        QpnDataType.String,
        'Header',
        'HTTP headers to forward for remote endpoints. Specify as a JSON object of key/value string pairs.',
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'VLR',
        QpnDataType.Boolean,
        'vlr',
        'Read LAS VLRs and import as metadata.',
        False,
        False,
        {'defaultValue': False}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'KEEPALIVE',
        QpnDataType.Numeric,
        'Keep alive',
        'The number of chunks to keep in active memory while reading',
        False,
        False,
        {'defaultValue': 10}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'FIXDIMS',
        QpnDataType.Boolean,
        'Fixed Dimensions',
        'Make invalid dimension names valid by converting disallowed characters to \'_\'. Only applies to names specified in an extra-bytes VLR.',
        False,
        False,
        {'defaultValue': True}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'SRSVLRORDER',
        QpnDataType.String,
        'SRS VLR Order',
        'Preference order to read SRS VLRs (list of \'wkt1\', \'wkt2\', or \'projjson\').',
        False,
        False,
        {'defaultValue': '[\'wkt1\', \'wkt2\', \'projjson\']'}
    )
)
PdalPipelineReaderCopc.addInput(
    QpnAlgorithmInput(
        'NOSRS',
        QpnDataType.Boolean,
        'No SRS',
        "Don't read the SRS VLRs. The data will not be assigned an SRS. This option is for use only in special cases where processing the SRS could cause performance issues.",
        False,
        False,
        {'defaultValue': False}
    )
)
PdalPipelineReaderCopc.addOutput(
    QpnAlgorithmOutput(
        'OUTPUT',
        QpnDataType.PointCloudLayer,
        'Point Cloud',
        'Output point cloud layer',
        False
    )
)

######################
# Pipeline - Writers #
######################

# writers.arrow
PdalPipelineWriterArrow = QpnAlgorithm(
    'pdal:pipelinewriterarrow',
    'writers.arrow',
    'The Arrow Writer'
)
PdalPipelineWriterArrow.help = """PDAL Pipeline - Writers - writers.arrow
    Write GeoArrow/GeoParquet formatted data"""
PdalPipelineWriterArrow.group = 'Pipeline - Writers'
PdalPipelineWriterArrow.provider = 'PDAL'

PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'INPUT',
        QpnDataType.PointCloudLayer,
        'Input Point Cloud',
        'Input point cloud layer',
        False,
        False
    )
)

PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'BATCHSIZE',
        QpnDataType.Numeric,
        'Batch size',
        'The number of rows to write as a batch',
        False,
        False,
        {'defaultValue': 262144}
    )
)
PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'FORMAT',
        QpnDataType.Enum,
        'Format',
        "File type to write (feather, parquet).",
        False,
        False,
        {'enumValues':
            [
                ('feather', 'feather'),
                ('parquet', 'parquet')],
            'defaultValue': 'feather'}
    )
)
PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'GEOARROWDIMMENSIONNAME',
        QpnDataType.String,
        'Dimension Name',
        "Dimension name to write GeoArrow struct",
        False,
        False,
        {'defaultValue': 'xyz'}
    )
)
PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'GEOPARQUET',
        QpnDataType.Boolean,
        'Geoparquet',
        "Write WKB column and GeoParquet metadata when writing parquet output.",
        False,
        False,
        {'defaultValue': True}
    )
)
PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'WRITEPIPELINEMETADATA',
        QpnDataType.Boolean,
        'Write Pipeline Metadata',
        "Write Pipeline metadata when writing parquet output into `PDAL:pipeline_metadata` for `Dimension Name`.",
        False,
        False,
        {'defaultValue': False}
    )
)
PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'WHERE',
        QpnDataType.String,
        'Where',
        "An expression that limits points passed to this writer.",
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineWriterArrow.addInput(
    QpnAlgorithmInput(
        'WHEREMERGE',
        QpnDataType.Enum,
        'Where Merge',
        "A strategy for merging points skipped by a `where` option when running in standard mode. If true, the skipped points are added to the first point view returned by the skipped filter or if no views are returned, placed in their own view. If false, skipped points are placed in their own point view. If auto, skipped points are merged into the returned point view provided that only one point view is returned and it has the same point count as it did when the filter was run, otherwise the skipped points are placed in their own view.",
        False,
        False,
        {'enumValues':
            [
                ('auto', 'auto'),
                ('true', 'true'),
                ('false', 'false')],
            'defaultValue': 'auto'}
    )
)
PdalPipelineWriterArrow.addOutput(
    QpnAlgorithmOutput(
        'OUTPUT',
        QpnDataType.PointCloudLayer,
        'Point Cloud',
        'Output point cloud layer',
        False
    )
)

######################
# Pipeline - Filters #
######################

PdalPipelineFilterCsf = QpnAlgorithm(
    'pdal:pipelinefilterscsf',
    'filters.csf',
    'Cloth Simulation Filter'
)
PdalPipelineFilterCsf.provider = 'PDAL'
PdalPipelineFilterCsf.group = 'Pipeline - Filters'
PdalPipelineFilterCsf.help = 'The Cloth Simulation Filter (CSF) classifies ground points based on the approach outlined in [Zhang et al., 2016].'

PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'INPUT',
        QpnDataType.PointCloudLayer,
        'Input Point Cloud',
        'Input point cloud layer',
        False,
        False
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'RESOLUTION',
        QpnDataType.Numeric,
        'Resolution',
        "Cloth resolution",
        False,
        False,
        {'defaultValue': 1.0}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'IGNORE',
        QpnDataType.String,
        'Ignore',
        "A range of values of a dimension to ignore.",
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'RETURNS',
        QpnDataType.Enum,
        'Returns',
        "Return types to include in output.",
        False,
        False,
        {'enumValues': [
            ('first', 'first'),
            ('last', 'last'),
            ('intermediate', 'intermediate'),
            ('only', 'only')
        ],
        'defaultValue': 'last'}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'THRESHOLD',
        QpnDataType.Numeric,
        'Threshold',
        "Classification threshold.",
        False,
        False,
        {'defaultValue': 0.5}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'HDIFF',
        QpnDataType.Numeric,
        'hdiff',
        "Height difference threshold.",
        False,
        False,
        {'defaultValue': 0.3}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'SMOOTH',
        QpnDataType.Boolean,
        'Smooth',
        "Perform slope post-processing?",
        False,
        False,
        {'defaultValue': True}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'STEP',
        QpnDataType.Numeric,
        'Step',
        "Time step.",
        False,
        False,
        {'defaultValue': 0.65}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'RIGIDNESS',
        QpnDataType.Numeric,
        'Rigidness',
        "Rigidness",
        False,
        False,
        {'defaultValue': 3}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'ITERATIONS',
        QpnDataType.Numeric,
        'Iterations',
        "Maximum number of iterations",
        False,
        False,
        {'defaultValue': 500}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'WHERE',
        QpnDataType.String,
        'Where',
        "An expression that limits points passed to this filter.",
        False,
        False,
        {'defaultValue': None}
    )
)
PdalPipelineFilterCsf.addInput(
    QpnAlgorithmInput(
        'WHEREMERGE',
        QpnDataType.Enum,
        'Where Merge',
        "A strategy for merging points skipped by a `where` option when running in standard mode. If true, the skipped points are added to the first point view returned by the skipped filter or if no views are returned, placed in their own view. If false, skipped points are placed in their own point view. If auto, skipped points are merged into the returned point view provided that only one point view is returned and it has the same point count as it did when the filter was run, otherwise the skipped points are placed in their own view.",
        False,
        False,
        {'enumValues':
            [
                ('auto', 'auto'),
                ('true', 'true'),
                ('false', 'false')],
            'defaultValue': 'auto'}
    )
)
PdalPipelineFilterCsf.addOutput(
    QpnAlgorithmOutput(
        'OUTPUT',
        QpnDataType.PointCloudLayer,
        'Output Point Cloud',
        'Output point cloud layer',
        True
    )
)