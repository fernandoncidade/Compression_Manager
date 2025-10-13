from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon, QFont
from utils.IconUtils import get_icon_path
from utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_button(self, text, callback=None, icon=None):
    button = QPushButton(text)
    button.setMinimumWidth(3 * button.fontMetrics().horizontalAdvance('m'))
    button.setMaximumWidth(3 * button.fontMetrics().horizontalAdvance('m'))
    button.setMinimumHeight(1.5 * button.fontMetrics().height())
    button.setMaximumHeight(1.5 * button.fontMetrics().height())
    button.setFont(QFont('Arial', 9))
    if icon:
        button.setIcon(QIcon(get_icon_path(icon)))

    if callback:
        button.clicked.connect(callback)

    return button
