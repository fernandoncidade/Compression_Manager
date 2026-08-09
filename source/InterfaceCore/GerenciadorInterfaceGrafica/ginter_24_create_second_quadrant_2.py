from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import QCoreApplication
from source.GerenciamentoUI.ui_03_dragDrop import DragDropListWidget
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_second_quadrant_2(self):
    layout = QVBoxLayout()
    button_layout = QHBoxLayout()

    self.folder_label_2 = QLabel(QCoreApplication.translate("InterfaceGrafica", "Diretório(s) Pastas e Arquivos:"))
    button_layout.addWidget(self.folder_label_2)

    button_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

    self.clear_input_label_2 = QLabel(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":")
    clear_input_button_2 = self.create_button("", self.gerenciador_interface_2.clear_folders, "clear_button3.png")
    self.main_buttons_2[self.clear_input_label_2] = "Limpar Entrada" + ":"

    self.clear_outputs_label_2 = QLabel(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":")
    clear_outputs_button_2 = self.create_button("", self.gerenciador_interface_2.clear_output, "clear_button2.png")
    self.main_buttons_2[self.clear_outputs_label_2] = "Limpar Todas Saídas" + ":"

    button_layout.addWidget(self.clear_input_label_2)
    button_layout.addWidget(clear_input_button_2)
    button_layout.addWidget(self.clear_outputs_label_2)
    button_layout.addWidget(clear_outputs_button_2)

    layout.addLayout(button_layout)
    self.gerenciador_interface_2.folder_listbox = DragDropListWidget()
    layout.addWidget(self.gerenciador_interface_2.folder_listbox)

    def retranslate():
        try:
            self.folder_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Diretório(s) Pastas e Arquivos:"))
            self.clear_input_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":")
            self.clear_outputs_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":")

            self.main_buttons_2[self.clear_input_label_2] = QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":"
            self.main_buttons_2[self.clear_outputs_label_2] = QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":"

        except Exception as e:
            logger.error(f"Erro em retranslate (second quadrant 2): {e}", exc_info=True)

    trad = getattr(self, "gerenciador_traducao", None)
    if trad and hasattr(trad, "idioma_alterado"):
        try:
            trad.idioma_alterado.connect(retranslate)
            retranslate()

        except Exception as e:
            logger.error(f"Erro ao conectar retranslate (second quadrant 2): {e}", exc_info=True)

    return layout
