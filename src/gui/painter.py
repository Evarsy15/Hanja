from PyQt6.QtCore import Qt, QSize, QObject, QPointF
from PyQt6.QtGui import \
    QPixmap, QPainter, QColor, QPen, QBrush, \
    QAction
from PyQt6.QtWidgets import \
    QGraphicsItem, QGraphicsPixmapItem

from typing import Optional

import gui_config as gui_cfg

class PenConfig(QObject):
    def __init__(
        self
    ) -> None:
        self.color : QColor = QColor("#000000")
        self.width : int    = 5
        
        self.style    : Qt.PenStyle    = Qt.PenStyle.SolidLine
        self.capStyle : Qt.PenCapStyle = Qt.PenCapStyle.RoundCap

class BrushConfig(QObject):
    def __init__(
        self
    ) -> None:
        self.color : QColor = QColor("#9900FF")
        self.style : Qt.BrushStyle = Qt.BrushStyle.SolidPattern

'''
    https://www.youtube.com/watch?v=uGu3GLoh_xA
'''
class Painter(QGraphicsPixmapItem):
    def __init__(
        self,
        name: str,
        size: QSize,
    ):
        super().__init__()
        self.name = name    # Instance name

        # Setup Canvas
        self.canvas = QPixmap(size)
        self.canvas.fill(QColor("#EEEEEE"))

        # Setup Pen
        self.pen_config = PenConfig()
        self.pen = QPen()
        self.pen.setColor(self.pen_config.color)
        self.pen.setWidth(self.pen_config.width)
        self.pen.setStyle(self.pen_config.style)
        self.pen.setCapStyle(self.pen_config.capStyle)

        # Setup Brush
        self.brush_config = BrushConfig()
        self.brush = QBrush()
        self.brush.setColor(self.brush_config.color)
        self.brush.setStyle(self.brush_config.style)

        # Setup Painter
        self.painter = QPainter(self.canvas)
        self.painter.end()

        self.prevPos : Optional[QPointF] = None

        self.setPixmap(self.canvas)

    def __del__(self) -> None:
        pass
    
    '''
        Core Signal Handlers
    '''

    def mousePressEvent(self, event) -> None:
        if event == None:
            print("Painter.mousePressEvent: event is None")
            return
        
        pos = event.pos()
        if gui_cfg.DEBUG:
            print(f"Painter.mousePressEvent: event.pos() = [{pos.x()}, {pos.y()}]")

        self.painter.begin(self.canvas)
        self.painter.setPen(self.pen)
        if self.prevPos:
            self.painter.drawLine(self.prevPos, pos)
        else:
            self.painter.drawPoint(pos)
        self.prevPos = pos
        self.setPixmap(self.canvas)

    def mouseMoveEvent(self, event) -> None:
        if event == None:
            print("Painter.mouseMoveEvent: event is None")
            return
        
        pos = event.pos()
        if gui_cfg.DEBUG:
            print(f"Painter.mouseMoveEvent: event.pos() = [{pos.x()}, {pos.y()}]")

        if self.prevPos:
            self.painter.drawLine(self.prevPos, pos)
        else:
            self.painter.drawPoint(pos)
        self.prevPos = pos
        self.setPixmap(self.canvas)
    
    def mouseReleaseEvent(self, event) -> None:
        self.prevPos = None
        self.painter.end()
