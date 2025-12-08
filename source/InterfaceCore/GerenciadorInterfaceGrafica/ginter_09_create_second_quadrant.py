from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import QCoreApplication
from source.GerenciamentoUI.ui_03_dragDrop import DragDropListWidget
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_second_quadrant(self):
    layout = QVBoxLayout()
    button_layout = QHBoxLayout()

    self.folder_label = QLabel(QCoreApplication.translate("InterfaceGrafica", "Diretório(s) Pastas e Arquivos:"))
    button_layout.addWidget(self.folder_label)

    button_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

    self.clear_input_label = QLabel(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":")
    clear_input_button = self.create_button("", self.gerenciador_interface.clear_folders, "clear_button3.png")
    self.main_buttons[self.clear_input_label] = "Limpar Entrada" + ":"

    self.clear_outputs_label = QLabel(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":")
    clear_outputs_button = self.create_button("", self.gerenciador_interface.clear_output, "clear_button2.png")
    self.main_buttons[self.clear_outputs_label] = "Limpar Todas Saídas" + ":"

    button_layout.addWidget(self.clear_input_label)
    button_layout.addWidget(clear_input_button)
    button_layout.addWidget(self.clear_outputs_label)
    button_layout.addWidget(clear_outputs_button)

    layout.addLayout(button_layout)
    self.gerenciador_interface.folder_listbox = DragDropListWidget()
    layout.addWidget(self.gerenciador_interface.folder_listbox)

    def retranslate():
        try:
            self.folder_label.setText(QCoreApplication.translate("InterfaceGrafica", "Diretório(s) Pastas e Arquivos:"))
            self.clear_input_label.setText(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":")
            self.clear_outputs_label.setText(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":")

            self.main_buttons[self.clear_input_label] = QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":"
            self.main_buttons[self.clear_outputs_label] = QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":"

        except Exception as e:
            logger.error(f"Erro em retranslate (second quadrant): {e}", exc_info=True)

    trad = getattr(self, "gerenciador_traducao", None)
    if trad and hasattr(trad, "idioma_alterado"):
        try:
            trad.idioma_alterado.connect(retranslate)
            retranslate()

        except Exception as e:
            logger.error(f"Erro ao conectar retranslate (second quadrant): {e}", exc_info=True)

    return layout
