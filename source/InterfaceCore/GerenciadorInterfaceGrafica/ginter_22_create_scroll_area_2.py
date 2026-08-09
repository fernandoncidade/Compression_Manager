from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox
from PySide6.QtCore import QCoreApplication
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_scroll_area_2(self):
    self.methods_group_2 = QGroupBox(QCoreApplication.translate("InterfaceGrafica", "Métodos de compressão e extração"))

    group_layout = QVBoxLayout(self.methods_group_2)
    group_layout.setContentsMargins(8, 8, 8, 8)
    group_layout.setSpacing(6)

    self.scroll_area_2 = QScrollArea()
    self.scroll_area_2.setWidgetResizable(True)

    self.scroll_area_widget_2 = QWidget()
    self.scroll_area_layout_2 = QVBoxLayout(self.scroll_area_widget_2)
    self.scroll_area_2.setWidget(self.scroll_area_widget_2)

    self.scroll_area_2.setMinimumSize(280, 200)

    self.method_layouts_container_2 = QVBoxLayout()
    self.scroll_area_layout_2.addLayout(self.method_layouts_container_2)

    group_layout.addWidget(self.scroll_area_2)

    return self.methods_group_2
