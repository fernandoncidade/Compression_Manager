from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QLabel
from PySide6.QtCore import QCoreApplication
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_first_quadrant_2(self):
    layout = QVBoxLayout()
    layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    self.add_folders_label_2 = QLabel(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":")
    add_folders_button_2 = self.create_button("", self.gerenciador_interface_2.browse_folder, "pasta.png")
    row1 = QHBoxLayout()
    row1.addWidget(self.add_folders_label_2)
    row1.addWidget(add_folders_button_2)
    self.main_buttons_2[self.add_folders_label_2] = "Adicionar Pastas" + ":"

    self.add_files_label_2 = QLabel(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":")
    add_files_button_2 = self.create_button("", self.gerenciador_interface_2.browse_file, "arquivo.png")
    row2 = QHBoxLayout()
    row2.addWidget(self.add_files_label_2)
    row2.addWidget(add_files_button_2)
    self.main_buttons_2[self.add_files_label_2] = "Adicionar Arquivos" + ":"

    self.test_label_2 = QLabel(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":")
    test_integrity_button_2 = self.create_button("", self.gerenciador_interface_2.testar_integridade, "interrogacao.png")
    row3 = QHBoxLayout()
    row3.addWidget(self.test_label_2)
    row3.addWidget(test_integrity_button_2)
    self.main_buttons_2[self.test_label_2] = "Testar Integridade" + ":"

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addLayout(row3)

    def retranslate():
        try:
            self.add_folders_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":")
            self.add_files_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":")
            self.test_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":")

            self.main_buttons_2[self.add_folders_label_2] = QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":"
            self.main_buttons_2[self.add_files_label_2] = QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":"
            self.main_buttons_2[self.test_label_2] = QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":"

        except Exception as e:
            logger.error(f"Erro em retranslate (first quadrant 2): {e}", exc_info=True)

    trad = getattr(self, "gerenciador_traducao", None)
    if trad and hasattr(trad, "idioma_alterado"):
        try:
            trad.idioma_alterado.connect(retranslate)
            retranslate()

        except Exception as e:
            logger.error(f"Erro ao conectar retranslate (first quadrant 2): {e}", exc_info=True)

    return layout
