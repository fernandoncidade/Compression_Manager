from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QVBoxLayout, QWidget
from source.utils.IconUtils import get_icon_path
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def init_ui(self):
    self.setWindowTitle(QCoreApplication.translate("InterfaceGrafica", "Compression Manager"))
    self.setWindowIcon(QIcon(get_icon_path("Manager-BackUp.ico")))

    self.main_buttons = {}
    self.folder_label = None

    main_layout = QVBoxLayout()
    self.main_layout_1_widget = self.create_widget_with_layout(self.create_main_layout_1())
    self.main_layout_1_widget.setMinimumHeight(152)
    self.main_layout_1_widget.setMaximumHeight(304)
    main_layout.addWidget(self.main_layout_1_widget)
    main_layout.addWidget(self.create_widget_with_layout(self.create_main_layout_2()))
    main_layout.addWidget(self.create_scroll_area())

    central_widget = QWidget(self)
    central_widget.setLayout(main_layout)
    self.setCentralWidget(central_widget)
