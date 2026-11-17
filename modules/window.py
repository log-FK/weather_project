from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QMainWindow,
    QScrollArea,
)

from .app import app  # QApplication має бути створений до вікна

WIDTH_WINDOW = 800
HEIGHT_WINDOW = 600
SQUARE_SIZE = 30


SIDEBAR_COLOR = "#000000"
CONTENT_COLOR = "#33ff00"
BLOCK_COLOR = "#212529"


main_window = QMainWindow()
main_window.setWindowTitle("Weather app")
main_window.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW) 
 
scroll_area = QScrollArea(parent=main_window)
scroll_area.setGeometry(0, 0, 245, HEIGHT_WINDOW)
scroll_area.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)
scroll_area.setWidgetResizable(True)
scroll_area.setStyleSheet(f"background-color: grey;")

scroll_content = QFrame(parent=scroll_area)
scroll_content.setFixedWidth(390)

scroll_area.setWidget(scroll_content)
scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)


content_frame = QFrame(parent=main_window)
content_frame.setGeometry(245, 0, 555, HEIGHT_WINDOW)
content_frame.setStyleSheet(f"background-color: {CONTENT_COLOR};")


search_frame = QFrame(parent=main_window)
search_frame.setGeometry(255, 18, 535, 27)
search_frame.setStyleSheet(f"background-color: {BLOCK_COLOR};")

block_frame = QFrame(parent= main_window)
block_frame.setGeometry(255, 63, 535, 227)
block_frame.setStyleSheet(f"background-color: {BLOCK_COLOR};")

block_frame2 = QFrame(parent= main_window)
block_frame2.setGeometry(255, 308, 535, 273)
block_frame2.setStyleSheet(f"background-color: {BLOCK_COLOR};")
