from PySide6.QtWidgets import QHBoxLayout
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_main_layout_1(self):
    layout = QHBoxLayout()
    layout.addLayout(self.create_first_quadrant())
    layout.addLayout(self.create_second_quadrant())
    return layout
