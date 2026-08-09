from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog
from source.MotoresCompressao.mtcomp_01_metodosCompressao import MenuPersistente
from source.InterfaceCore.GerenciadorInterfaceGrafica.ginter_20_exibir_sobre import exibir_sobre
from source.GerenciamentoUI.ui_07_Manual import exibir_manual
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()


def _is_layout2_active(self):
    return hasattr(self, 'segundo_layout_action') and self.segundo_layout_action.isChecked() and hasattr(self, 'gerenciador_interface_2')


def menu_browse_folder(self):
    if _is_layout2_active(self):
        self.gerenciador_interface._browse(QFileDialog.FileMode.Directory, [self.gerenciador_interface.folder_listbox, self.gerenciador_interface_2.folder_listbox])
    else:
        self.gerenciador_interface.browse_folder()


def menu_browse_file(self):
    if _is_layout2_active(self):
        self.gerenciador_interface._browse(QFileDialog.FileMode.ExistingFiles, [self.gerenciador_interface.folder_listbox, self.gerenciador_interface_2.folder_listbox])
    else:
        self.gerenciador_interface.browse_file()


def menu_testar_integridade(self):
    self.gerenciador_interface.testar_integridade()
    if _is_layout2_active(self):
        self.gerenciador_interface_2.testar_integridade()


def menu_clear_folders(self):
    self.gerenciador_interface.clear_folders()
    if _is_layout2_active(self):
        self.gerenciador_interface_2.clear_folders()


def menu_clear_output(self):
    self.gerenciador_interface.clear_output()
    if _is_layout2_active(self):
        self.gerenciador_interface_2.clear_output()


def menu_specify_output(self, method_name):
    if _is_layout2_active(self):
        lb1 = getattr(self.gerenciador_interface, f'output_listbox_{method_name}')
        lb2 = getattr(self.gerenciador_interface_2, f'output_listbox_{method_name}')
        self.gerenciador_interface._browse(QFileDialog.FileMode.Directory, [lb1, lb2])
    else:
        getattr(self.gerenciador_interface, f'output_button_output_{method_name.upper()}_clicked')()


def menu_store_as(self, method_name):
    getattr(self.gerenciador_interface, f'store_as_{method_name}')()
    if _is_layout2_active(self):
        getattr(self.gerenciador_interface_2, f'store_as_{method_name}')()


def menu_extract_files(self):
    self.gerenciador_interface.extract_files()
    if _is_layout2_active(self):
        self.gerenciador_interface_2.extract_files()


def menu_clear_output_listbox(self, method_name):
    getattr(self.gerenciador_interface, f'clear_output_listbox_{method_name}')()
    if _is_layout2_active(self):
        getattr(self.gerenciador_interface_2, f'clear_output_listbox_{method_name}')()


def init_menu(self):
    self.menu_bar = self.menuBar()

    self.arquivo_menu = self.menu_bar.addMenu(QCoreApplication.translate("InterfaceGrafica", "Arquivo"))

    self.adicionar_pastas_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":", self)
    self.adicionar_pastas_action.triggered.connect(lambda: menu_browse_folder(self))
    self.arquivo_menu.addAction(self.adicionar_pastas_action)

    self.adicionar_arquivos_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":", self)
    self.adicionar_arquivos_action.triggered.connect(lambda: menu_browse_file(self))
    self.arquivo_menu.addAction(self.adicionar_arquivos_action)

    self.testar_integridade_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":", self)
    self.testar_integridade_action.triggered.connect(lambda: menu_testar_integridade(self))
    self.arquivo_menu.addAction(self.testar_integridade_action)

    self.arquivo_menu.addSeparator()

    self.limpar_entrada_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":", self)
    self.limpar_entrada_action.triggered.connect(lambda: menu_clear_folders(self))
    self.arquivo_menu.addAction(self.limpar_entrada_action)

    self.limpar_todas_saidas_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":", self)
    self.limpar_todas_saidas_action.triggered.connect(lambda: menu_clear_output(self))
    self.arquivo_menu.addAction(self.limpar_todas_saidas_action)

    self.arquivo_menu.addSeparator()

    self.especificar_saida_menu = self.arquivo_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Especificar Saída") + ":")
    self.especificar_zip_action = QAction(".ZIP", self)
    self.especificar_zip_action.triggered.connect(lambda: menu_specify_output(self, 'zip'))
    self.especificar_saida_menu.addAction(self.especificar_zip_action)

    self.especificar_7z_action = QAction(".7Z", self)
    self.especificar_7z_action.triggered.connect(lambda: menu_specify_output(self, '7z'))
    self.especificar_saida_menu.addAction(self.especificar_7z_action)

    self.especificar_tar_action = QAction(".TAR", self)
    self.especificar_tar_action.triggered.connect(lambda: menu_specify_output(self, 'tar'))
    self.especificar_saida_menu.addAction(self.especificar_tar_action)

    self.especificar_wim_action = QAction(".WIM", self)
    self.especificar_wim_action.triggered.connect(lambda: menu_specify_output(self, 'wim'))
    self.especificar_saida_menu.addAction(self.especificar_wim_action)

    self.especificar_extracao_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Extração"), self)
    self.especificar_extracao_action.triggered.connect(lambda: menu_specify_output(self, 'extracao'))
    self.especificar_saida_menu.addAction(self.especificar_extracao_action)

    self.arquivo_menu.addSeparator()

    self.armazenar_menu = self.arquivo_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Armazenar") + ":")
    self.armazenar_zip_action = QAction(".ZIP", self)
    self.armazenar_zip_action.triggered.connect(lambda: menu_store_as(self, 'zip'))
    self.armazenar_menu.addAction(self.armazenar_zip_action)

    self.armazenar_7z_action = QAction(".7Z", self)
    self.armazenar_7z_action.triggered.connect(lambda: menu_store_as(self, '7z'))
    self.armazenar_menu.addAction(self.armazenar_7z_action)

    self.armazenar_tar_action = QAction(".TAR", self)
    self.armazenar_tar_action.triggered.connect(lambda: menu_store_as(self, 'tar'))
    self.armazenar_menu.addAction(self.armazenar_tar_action)

    self.armazenar_wim_action = QAction(".WIM", self)
    self.armazenar_wim_action.triggered.connect(lambda: menu_store_as(self, 'wim'))
    self.armazenar_menu.addAction(self.armazenar_wim_action)

    self.arquivo_menu.addSeparator()

    self.extrair_arquivos_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Extrair Arquivos") + ":", self)
    self.extrair_arquivos_action.triggered.connect(lambda: menu_extract_files(self))
    self.arquivo_menu.addAction(self.extrair_arquivos_action)

    self.arquivo_menu.addSeparator()

    self.limpar_saida_menu = self.arquivo_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Limpar Saída") + ":")
    self.limpar_saida_zip_action = QAction(".ZIP", self)
    self.limpar_saida_zip_action.triggered.connect(lambda: menu_clear_output_listbox(self, 'zip'))
    self.limpar_saida_menu.addAction(self.limpar_saida_zip_action)

    self.limpar_saida_7z_action = QAction(".7Z", self)
    self.limpar_saida_7z_action.triggered.connect(lambda: menu_clear_output_listbox(self, '7z'))
    self.limpar_saida_menu.addAction(self.limpar_saida_7z_action)

    self.limpar_saida_tar_action = QAction(".TAR", self)
    self.limpar_saida_tar_action.triggered.connect(lambda: menu_clear_output_listbox(self, 'tar'))
    self.limpar_saida_menu.addAction(self.limpar_saida_tar_action)

    self.limpar_saida_wim_action = QAction(".WIM", self)
    self.limpar_saida_wim_action.triggered.connect(lambda: menu_clear_output_listbox(self, 'wim'))
    self.limpar_saida_menu.addAction(self.limpar_saida_wim_action)

    self.limpar_saida_extracao_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Extração"), self)
    self.limpar_saida_extracao_action.triggered.connect(lambda: menu_clear_output_listbox(self, 'extracao'))
    self.limpar_saida_menu.addAction(self.limpar_saida_extracao_action)

    self.arquivo_menu.addSeparator()

    self.sair_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Sair"), self)
    self.sair_action.triggered.connect(self.close)
    self.arquivo_menu.addAction(self.sair_action)

    self.config_menu = self.menu_bar.addMenu(QCoreApplication.translate("InterfaceGrafica", "Configurações"))

    self.compression_method_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Selecionar Método de Compressão"), self)
    self.compression_method_action.triggered.connect(self.select_compression_method)
    self.config_menu.addAction(self.compression_method_action)

    self.layouts_menu = MenuPersistente(QCoreApplication.translate("InterfaceGrafica", "Layouts"), self)
    self.config_menu.addMenu(self.layouts_menu)

    self.primeiro_layout_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Primeiro Layout"), self)
    self.primeiro_layout_action.setCheckable(True)
    self.primeiro_layout_action.setChecked(True)
    self.primeiro_layout_action.setEnabled(False)
    self.layouts_menu.addAction(self.primeiro_layout_action)

    self.segundo_layout_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Segundo Layout"), self)
    self.segundo_layout_action.setCheckable(True)
    self.segundo_layout_action.setChecked(False)
    self.segundo_layout_action.triggered.connect(self.toggle_segundo_layout)
    self.layouts_menu.addAction(self.segundo_layout_action)

    self.idiomas_menu = MenuPersistente(QCoreApplication.translate("InterfaceGrafica", "Idiomas"), self)
    self.config_menu.addMenu(self.idiomas_menu)

    self.pt_br_action = QAction("Português (Brasil)", self)
    self.pt_br_action.triggered.connect(lambda: self.mudar_idioma("pt_BR"))
    self.pt_br_action.setCheckable(True)
    self.pt_br_action.setChecked(self.gerenciador_traducao.idioma_atual == "pt_BR")
    self.idiomas_menu.addAction(self.pt_br_action)

    self.en_us_action = QAction("English (United States)", self)
    self.en_us_action.triggered.connect(lambda: self.mudar_idioma("en_US"))
    self.en_us_action.setCheckable(True)
    self.en_us_action.setChecked(self.gerenciador_traducao.idioma_atual == "en_US")
    self.idiomas_menu.addAction(self.en_us_action)

    self.opcoes_menu = self.menu_bar.addMenu(QCoreApplication.translate("InterfaceGrafica", "Opções"))
    
    self.manual_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Manual"), self)
    self.manual_action.triggered.connect(lambda: exibir_manual(self))
    self.opcoes_menu.addAction(self.manual_action)

    self.sobre_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Sobre"), self)
    self.sobre_action.triggered.connect(lambda: exibir_sobre(self))
    self.opcoes_menu.addAction(self.sobre_action)

    self.config_menu.aboutToShow.connect(self.update_compression_menus)
