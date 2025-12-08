from PySide6.QtWidgets import QVBoxLayout
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_third_quadrant(self):
    layout = QVBoxLayout()
    self.create_method_checkboxes(layout)
    return layout
