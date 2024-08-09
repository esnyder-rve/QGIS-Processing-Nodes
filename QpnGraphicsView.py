from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QMouseEvent, QWheelEvent
from PyQt5.QtCore import Qt, QEvent

from QpnSettings import QpnSettings

class QpnGraphicsView(QGraphicsView):
    def __init__(self, scene: QGraphicsScene, parent=None):
        super(QpnGraphicsView, self).__init__(parent)
        self.graphicsScene = scene
        self.InitUI()
        self.setScene(self.graphicsScene)

        # Set zoom variables
        self.zoomInFactor = 1.25
        self.zoomLevel = 10
        self.zoomStep = 1
        self.zoomRange = [0, 15]
    

    def InitUI(self):
        # Enable flags for better rendering quality
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        
        # Set the viewport update mode to refresh all
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # Disable the scrollbars
        if not QpnSettings.GridShowScrollbars:
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        if QpnSettings.GridZoomTranslation:
            self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        else:
            self.setTransformationAnchor(QGraphicsView.AnchorViewCenter)


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.MiddleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.LeftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.RightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)


    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.MiddleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.LeftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.RightMouseButtonRelease(event)
        else:
            super().mousePressEvent(event)


    def LeftMouseButtonPress(self, event: QMouseEvent):
        super().mousePressEvent(event)
        pass
    

    def LeftMouseButtonRelease(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
        pass


    def MiddleMouseButtonPress(self, event: QMouseEvent):
        # Fake release event:
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), Qt.LeftButton, Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)

        # Set the drag mode
        self.setDragMode(QGraphicsView.ScrollHandDrag)

        # Send another fake click event
        clickEvent = QMouseEvent(QEvent.MouseButtonPress, event.localPos(), event.screenPos(), Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(clickEvent)


    def MiddleMouseButtonRelease(self, event: QMouseEvent):
        # Fake release event:
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), Qt.LeftButton, event.buttons() & ~Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)

        # Set the drag mode
        self.setDragMode(QGraphicsView.NoDrag)


    def RightMouseButtonPress(self, event: QMouseEvent):
        super().mousePressEvent(event)
        pass


    def RightMouseButtonRelease(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
        pass


    '''
    Override function for the scroll wheel event. Used for zooming
    '''
    def wheelEvent(self, event: QWheelEvent):
        # Check if the "Shift" key is being held (for touchpad support)
        if event.modifiers() == Qt.ShiftModifier:
            # Ignore this override, and call default behavior for panning
            super().wheelEvent(event)
            return

        # Calculate the zoom out factor:
        zoomOutFactor = 1 / self.zoomInFactor

        # Initialize the zoom factor to 1 (no effect)
        zoomFactor = 1.0

        # Calculate the zoom
        if event.angleDelta().y() > 0:
            if self.zoomLevel >= self.zoomRange[1]:
                self.zoomLevel = self.zoomRange[1]
                return

            zoomFactor = self.zoomInFactor
            self.zoomLevel += self.zoomStep
        elif event.angleDelta().y() < 0:
            if self.zoomLevel <= self.zoomRange[0]:
                self.zoomLevel = self.zoomRange[0]
                return

            zoomFactor = zoomOutFactor
            self.zoomLevel -= self.zoomStep

        # Set the view scale
        self.scale(zoomFactor, zoomFactor)
