from PySide6.QtWidgets import QHBoxLayout
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_main_layout_2(self):
    layout = QHBoxLayout()
    layout.addLayout(self.create_third_quadrant())
    return layout
