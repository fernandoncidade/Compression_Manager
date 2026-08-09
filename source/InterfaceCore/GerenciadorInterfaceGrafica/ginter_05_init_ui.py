from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy
from source.utils.IconUtils import get_icon_path
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def init_ui(self):
    self.setWindowTitle(QCoreApplication.translate("InterfaceGrafica", "Compression Manager"))
    self.setWindowIcon(QIcon(get_icon_path("Manager-BackUp.ico")))

    # Initial window dimensions
    self.resize(1200, 750)
    self.setMinimumSize(700, 500)

    self.main_buttons = {}
    self.main_buttons_2 = {}
    self.folder_label = None
    self.folder_label_2 = None

    self.primeiro_layout_column = QVBoxLayout()
    self.main_layout_1_widget = self.create_widget_with_layout(self.create_main_layout_1())
    self.main_layout_1_widget.setMinimumHeight(152)
    self.main_layout_1_widget.setMaximumHeight(304)
    self.primeiro_layout_column.addWidget(self.main_layout_1_widget)
    self.primeiro_layout_column.addWidget(self.create_widget_with_layout(self.create_main_layout_2()))
    self.primeiro_layout_column.addWidget(self.create_scroll_area())

    self.primeiro_layout_widget = QWidget()
    self.primeiro_layout_widget.setLayout(self.primeiro_layout_column)
    self.primeiro_layout_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    self.segundo_layout_widget = None

    self.columns_widget = QWidget(self)
    columns_layout = QHBoxLayout(self.columns_widget)
    columns_layout.setContentsMargins(0, 0, 0, 0)
    columns_layout.setSpacing(10)
    columns_layout.addWidget(self.primeiro_layout_widget, 1)

    main_layout = QVBoxLayout()
    main_layout.addWidget(self.columns_widget)

    central_widget = QWidget(self)
    central_widget.setLayout(main_layout)
    self.setCentralWidget(central_widget)
