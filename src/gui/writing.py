from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QGraphicsScene

from src.gui.painter import Painter

class WritingScene(QGraphicsScene):
    def __init__(
        self,
        parent = None,
        size: QSize = QSize(900, 600)
    ) -> None:
        super().__init__(parent)
        self.setObjectName("WritingScene")
        self.setSceneRect(0, 0, size.width(), size.height())

        self.setupUI()
    
    def setupUI(self) -> None:
        # Painter
        self.painter = Painter("painter", QSize(400, 400))
        self.painter.setPos(100, 100)
        self.addItem(self.painter)

        # TODO: Add 'Clear' Button