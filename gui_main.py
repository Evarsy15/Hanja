import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import \
	QApplication,	\
	QGraphicsView, QGraphicsScene

from src.gui.menu import TopMenu
from src.gui.painter import Painter
from src.gui.writing import WritingScene

class HanjaGUI(QGraphicsView):
	def __init__(self) -> None:
		super().__init__()

		self.setWindowTitle("한자 공부 프로그램")
		self.setFixedSize(900, 600)

		# Invalidate Scroll Bars
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

		self.top_menu 	   : QGraphicsScene = TopMenu()
		self.writing_scene : QGraphicsScene = WritingScene()

		# Set scene
		# self.setScene(self.top_menu)
		self.setScene(self.writing_scene)

def main() -> None:
	app = QApplication(sys.argv)
	window = HanjaGUI()
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
