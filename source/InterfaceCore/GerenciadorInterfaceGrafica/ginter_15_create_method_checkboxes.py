from PySide6.QtWidgets import QHBoxLayout, QCheckBox, QSpacerItem, QSizePolicy
from PySide6.QtCore import QCoreApplication
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_method_checkboxes(self, layout):
    checkbox_layout = QHBoxLayout()
    checkbox_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
    methods = ['zip', '7z', 'tar', 'wim', 'extracao']
    method_display_names = {}

    for method in methods:
        if method == 'extracao':
            method_display_names[method] = QCoreApplication.translate("InterfaceGrafica", "EXTRAÇÃO")

        else:
            method_display_names[method] = method.upper()

    self.checkboxes = {method: QCheckBox(method_display_names[method]) for method in methods}

    for method, checkbox in self.checkboxes.items():
        checkbox.method = method
        checkbox.toggled.connect(self.on_method_toggled)
        checkbox_layout.addWidget(checkbox)

    layout.addLayout(checkbox_layout)
