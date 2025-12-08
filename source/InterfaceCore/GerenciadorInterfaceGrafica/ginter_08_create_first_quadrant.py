from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QLabel
from PySide6.QtCore import QCoreApplication
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def create_first_quadrant(self):
    layout = QVBoxLayout()
    layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    self.add_folders_label = QLabel(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":")
    add_folders_button = self.create_button("", self.gerenciador_interface.browse_folder, "pasta.png")
    row1 = QHBoxLayout()
    row1.addWidget(self.add_folders_label)
    row1.addWidget(add_folders_button)
    self.main_buttons[self.add_folders_label] = "Adicionar Pastas" + ":"

    self.add_files_label = QLabel(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":")
    add_files_button = self.create_button("", self.gerenciador_interface.browse_file, "arquivo.png")
    row2 = QHBoxLayout()
    row2.addWidget(self.add_files_label)
    row2.addWidget(add_files_button)
    self.main_buttons[self.add_files_label] = "Adicionar Arquivos" + ":"

    self.test_label = QLabel(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":")
    test_integrity_button = self.create_button("", self.gerenciador_interface.testar_integridade, "interrogacao.png")
    row3 = QHBoxLayout()
    row3.addWidget(self.test_label)
    row3.addWidget(test_integrity_button)
    self.main_buttons[self.test_label] = "Testar Integridade" + ":"

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addLayout(row3)

    def retranslate():
        try:
            self.add_folders_label.setText(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":")
            self.add_files_label.setText(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":")
            self.test_label.setText(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":")

            self.main_buttons[self.add_folders_label] = QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":"
            self.main_buttons[self.add_files_label] = QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":"
            self.main_buttons[self.test_label] = QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":"

        except Exception as e:
            logger.error(f"Erro em retranslate (first quadrant): {e}", exc_info=True)

    trad = getattr(self, "gerenciador_traducao", None)
    if trad and hasattr(trad, "idioma_alterado"):
        try:
            trad.idioma_alterado.connect(retranslate)
            retranslate()

        except Exception as e:
            logger.error(f"Erro ao conectar retranslate (first quadrant): {e}", exc_info=True)

    return layout
