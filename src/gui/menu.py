from typing import Any, Optional
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QGraphicsScene

class TopMenu(QGraphicsScene):
    def __init__(
        self,
        parent : Optional[QObject] = None
    ) -> None:
        super().__init__(parent)

    