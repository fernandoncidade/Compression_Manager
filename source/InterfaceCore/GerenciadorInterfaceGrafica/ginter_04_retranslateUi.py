from PySide6.QtCore import QCoreApplication
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def retranslateUi(self):
    self.setWindowTitle(QCoreApplication.translate("InterfaceGrafica", "Compression Manager"))

    if hasattr(self, "arquivo_menu"):
        self.arquivo_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Arquivo"))

    if hasattr(self, "adicionar_pastas_action"):
        self.adicionar_pastas_action.setText(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":")

    if hasattr(self, "adicionar_arquivos_action"):
        self.adicionar_arquivos_action.setText(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":")

    if hasattr(self, "testar_integridade_action"):
        self.testar_integridade_action.setText(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":")

    if hasattr(self, "limpar_entrada_action"):
        self.limpar_entrada_action.setText(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":")

    if hasattr(self, "limpar_todas_saidas_action"):
        self.limpar_todas_saidas_action.setText(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":")

    if hasattr(self, "especificar_saida_menu"):
        self.especificar_saida_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Especificar Saída") + ":")

    if hasattr(self, "especificar_extracao_action"):
        self.especificar_extracao_action.setText(QCoreApplication.translate("InterfaceGrafica", "Extração"))

    if hasattr(self, "especificar_zip_action"):
        self.especificar_zip_action.setText(QCoreApplication.translate("InterfaceGrafica", ".ZIP"))

    if hasattr(self, "especificar_7z_action"):
        self.especificar_7z_action.setText(QCoreApplication.translate("InterfaceGrafica", ".7Z"))

    if hasattr(self, "especificar_tar_action"):
        self.especificar_tar_action.setText(QCoreApplication.translate("InterfaceGrafica", ".TAR"))

    if hasattr(self, "especificar_wim_action"):
        self.especificar_wim_action.setText(QCoreApplication.translate("InterfaceGrafica", ".WIM"))

    if hasattr(self, "armazenar_menu"):
        self.armazenar_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Armazenar") + ":")

    if hasattr(self, "armazenar_zip_action"):
        self.armazenar_zip_action.setText(QCoreApplication.translate("InterfaceGrafica", ".ZIP"))

    if hasattr(self, "armazenar_7z_action"):
        self.armazenar_7z_action.setText(QCoreApplication.translate("InterfaceGrafica", ".7Z"))

    if hasattr(self, "armazenar_tar_action"):
        self.armazenar_tar_action.setText(QCoreApplication.translate("InterfaceGrafica", ".TAR"))

    if hasattr(self, "armazenar_wim_action"):
        self.armazenar_wim_action.setText(QCoreApplication.translate("InterfaceGrafica", ".WIM"))

    if hasattr(self, "extrair_arquivos_action"):
        self.extrair_arquivos_action.setText(QCoreApplication.translate("InterfaceGrafica", "Extrair Arquivos") + ":")

    if hasattr(self, "limpar_saida_menu"):
        self.limpar_saida_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Limpar Saída") + ":")

    if hasattr(self, "limpar_saida_zip_action"):
        self.limpar_saida_zip_action.setText(QCoreApplication.translate("InterfaceGrafica", ".ZIP"))

    if hasattr(self, "limpar_saida_7z_action"):
        self.limpar_saida_7z_action.setText(QCoreApplication.translate("InterfaceGrafica", ".7Z"))

    if hasattr(self, "limpar_saida_tar_action"):
        self.limpar_saida_tar_action.setText(QCoreApplication.translate("InterfaceGrafica", ".TAR"))

    if hasattr(self, "limpar_saida_wim_action"):
        self.limpar_saida_wim_action.setText(QCoreApplication.translate("InterfaceGrafica", ".WIM"))

    if hasattr(self, "limpar_saida_extracao_action"):
        self.limpar_saida_extracao_action.setText(QCoreApplication.translate("InterfaceGrafica", "Extração"))

    if hasattr(self, "sair_action"):
        self.sair_action.setText(QCoreApplication.translate("InterfaceGrafica", "Sair"))

    self.config_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Configurações"))
    self.idiomas_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Idiomas"))
    self.compression_method_action.setText(QCoreApplication.translate("InterfaceGrafica", "Selecionar Método de Compressão"))
    self.opcoes_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Opções"))
    
    if hasattr(self, "manual_action"):
        self.manual_action.setText(QCoreApplication.translate("InterfaceGrafica", "Manual"))
        
    if hasattr(self, "sobre_action"):
        self.sobre_action.setText(QCoreApplication.translate("InterfaceGrafica", "Sobre"))

    if hasattr(self, "layouts_menu"):
        self.layouts_menu.setTitle(QCoreApplication.translate("InterfaceGrafica", "Layouts"))

    if hasattr(self, "primeiro_layout_action"):
        self.primeiro_layout_action.setText(QCoreApplication.translate("InterfaceGrafica", "Primeiro Layout"))

    if hasattr(self, "segundo_layout_action"):
        self.segundo_layout_action.setText(QCoreApplication.translate("InterfaceGrafica", "Segundo Layout"))

    if hasattr(self, "methods_group_2") and self.methods_group_2 is not None:
        self.methods_group_2.setTitle(QCoreApplication.translate("InterfaceGrafica", "Métodos de compressão e extração"))

    for button, text in self.main_buttons.items():
        button.setText(QCoreApplication.translate("InterfaceGrafica", text))

    self.folder_label.setText(QCoreApplication.translate("InterfaceGrafica", "Diretório(s) Pastas e Arquivos:"))

    for method, checkbox in self.checkboxes.items():
        if method == 'extracao':
            checkbox.setText(QCoreApplication.translate("InterfaceGrafica", "EXTRAÇÃO"))
        else:
            checkbox.setText(method.upper())

    if hasattr(self, "methods_group"):
        self.methods_group.setTitle(QCoreApplication.translate("InterfaceGrafica", "Métodos de compressão e extração"))

    if hasattr(self, 'main_buttons_2') and self.main_buttons_2:
        for button, text in self.main_buttons_2.items():
            button.setText(QCoreApplication.translate("InterfaceGrafica", text))

    if hasattr(self, 'folder_label_2') and self.folder_label_2 is not None:
        self.folder_label_2.setText(QCoreApplication.translate("InterfaceGrafica", "Diretório(s) Pastas e Arquivos:"))

    if hasattr(self, 'checkboxes_2') and self.checkboxes_2:
        for method, checkbox in self.checkboxes_2.items():
            if method == 'extracao':
                checkbox.setText(QCoreApplication.translate("InterfaceGrafica", "EXTRAÇÃO"))
            else:
                checkbox.setText(method.upper())

    self.rebuild_method_layouts()
    self.gerenciador_interface.atualizar_traducoes_dialogos()

    if hasattr(self, 'gerenciador_interface_2') and hasattr(self, 'segundo_layout_action') and self.segundo_layout_action.isChecked():
        self.gerenciador_interface_2.atualizar_traducoes_dialogos()

    self.update_compression_menus()

