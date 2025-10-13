from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox
from PySide6.QtCore import QCoreApplication
from utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_scroll_area(self):
    self.methods_group = QGroupBox(QCoreApplication.translate("InterfaceGrafica", "Métodos de compressão e extração"))

    group_layout = QVBoxLayout(self.methods_group)
    group_layout.setContentsMargins(8, 8, 8, 8)
    group_layout.setSpacing(6)

    self.scroll_area = QScrollArea()
    self.scroll_area.setWidgetResizable(True)

    self.scroll_area_widget = QWidget()
    self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
    self.scroll_area.setWidget(self.scroll_area_widget)

    self.scroll_area.setMinimumSize(600, 347)

    self.method_layouts_container = QVBoxLayout()
    self.scroll_area_layout.addLayout(self.method_layouts_container)

    group_layout.addWidget(self.scroll_area)

    return self.methods_group
