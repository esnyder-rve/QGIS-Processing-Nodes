class QpnSettings():
    # Grid Scene Settings
    '''
    Default canvas size in pixels (default=64,000)
    '''
    GridSceneSize = 64000

    '''
    Color of the grid background (in hex RGB). Uses system default if set to None
    '''
    GridColorBackground = "#393939"

    '''
    Enable grid lines (default=True)
    '''
    GridLinesEnabled = True

    '''
    Enable minor grid lines (ignored if GridLinesEnabled=False)
    '''
    GridLinesMinorEnabled = True

    '''
    Color of the minor grid lines (in hex RGB)
    '''
    GridColorMinor = "#2f2f2f"

    '''
    Minor grid line width (in pixels)
    '''
    GridLineWidthMinor = 1

    '''
    Enable major grid lines (ignored if GridLinesEnabled=False)
    '''
    GridLinesMajorEnabled = True

    '''
    Major grid line width (in pixels)
    '''
    GridLineWidthMajor = 2

    '''
    Color of the major grid lines (in hex RGB)
    '''
    GridColorMajor = "#1c1c1c"

    '''
    Grid size in pixels
    '''
    GridSizeMinor  = 20

    '''
    Multiplier to GridSizeMinor. A major line is drawn every n lines
    '''
    GridSizeMajor  = 4

    '''
    Enable/Disable the scrollbars on the grid (default=False)
    '''
    GridShowScrollbars = False

    '''
    Zoom to/from mouse cursor position (default=True)
    '''
    GridZoomTranslation = True

    # Node Settings
    '''
    Color for the node title text in RGB Hex (default='#ffffff' aka White)
    '''
    NodeTitleTextColor = '#ffffff'

    '''
    Font for node title (default=Noto Sans)
    '''
    NodeTitleFont = 'Inter'

    '''
    Font size for node title (default=10pt)
    '''
    NodeTitleFontSize = 10

    '''
    Roundedness (in pixels) of the node box (default=?)
    '''
    NodeEdgeRoundness = 10

    '''
    Node Outline Color in ARGB hex (default='#7F000000')
    '''
    NodeOutlineColor = '#7F000000'

    '''
    Node Outline Selection color in ARGB hex (default='#FFFFA637')
    '''
    NodeOutlineSelectionColor = "#FFFFA637"

    '''
    Node outline width in pixels (default=2)
    '''
    NodeOutlineWidth = 2

    '''
    Node title bar background color in hex RGB (default='#313131')
    '''
    NodeTitleBackgroundColor = '#313131'

    '''
    Node content background color in hex RGB (default='#212121')
    '''
    NodeContentBackgroundColor = '#212121'
