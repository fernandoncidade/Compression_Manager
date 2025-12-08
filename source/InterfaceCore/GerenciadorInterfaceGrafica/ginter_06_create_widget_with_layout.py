from PySide6.QtWidgets import QWidget
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_widget_with_layout(self, layout):
    widget = QWidget()
    widget.setLayout(layout)
    return widget
