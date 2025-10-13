from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction
from source.MotoresCompressao.mtcomp_01_metodosCompressao import MenuPersistente
from source.InterfaceCore.GerenciadorInterfaceGrafica.ginter_20_exibir_sobre import exibir_sobre
from utils.LogManager import LogManager

logger = LogManager.get_logger()

def init_menu(self):
    self.menu_bar = self.menuBar()

    self.arquivo_menu = self.menu_bar.addMenu(QCoreApplication.translate("InterfaceGrafica", "Arquivo"))

    self.adicionar_pastas_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Adicionar Pastas") + ":", self)
    self.adicionar_pastas_action.triggered.connect(self.gerenciador_interface.browse_folder)
    self.arquivo_menu.addAction(self.adicionar_pastas_action)

    self.adicionar_arquivos_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Adicionar Arquivos") + ":", self)
    self.adicionar_arquivos_action.triggered.connect(self.gerenciador_interface.browse_file)
    self.arquivo_menu.addAction(self.adicionar_arquivos_action)

    self.testar_integridade_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Testar Integridade") + ":", self)
    self.testar_integridade_action.triggered.connect(self.gerenciador_interface.testar_integridade)
    self.arquivo_menu.addAction(self.testar_integridade_action)

    self.arquivo_menu.addSeparator()

    self.limpar_entrada_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Limpar Entrada") + ":", self)
    self.limpar_entrada_action.triggered.connect(self.gerenciador_interface.clear_folders)
    self.arquivo_menu.addAction(self.limpar_entrada_action)

    self.limpar_todas_saidas_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Limpar Todas Saídas") + ":", self)
    self.limpar_todas_saidas_action.triggered.connect(self.gerenciador_interface.clear_output)
    self.arquivo_menu.addAction(self.limpar_todas_saidas_action)

    self.arquivo_menu.addSeparator()

    self.especificar_saida_menu = self.arquivo_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Especificar Saída") + ":")
    self.especificar_zip_action = QAction(".ZIP", self)
    self.especificar_zip_action.triggered.connect(self.gerenciador_interface.output_button_output_ZIP_clicked)
    self.especificar_saida_menu.addAction(self.especificar_zip_action)

    self.especificar_7z_action = QAction(".7Z", self)
    self.especificar_7z_action.triggered.connect(self.gerenciador_interface.output_button_output_7Z_clicked)
    self.especificar_saida_menu.addAction(self.especificar_7z_action)

    self.especificar_tar_action = QAction(".TAR", self)
    self.especificar_tar_action.triggered.connect(self.gerenciador_interface.output_button_output_TAR_clicked)
    self.especificar_saida_menu.addAction(self.especificar_tar_action)

    self.especificar_wim_action = QAction(".WIM", self)
    self.especificar_wim_action.triggered.connect(self.gerenciador_interface.output_button_output_WIM_clicked)
    self.especificar_saida_menu.addAction(self.especificar_wim_action)

    self.especificar_extracao_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Extração"), self)
    self.especificar_extracao_action.triggered.connect(self.gerenciador_interface.output_button_output_EXTRACAO_clicked)
    self.especificar_saida_menu.addAction(self.especificar_extracao_action)

    self.arquivo_menu.addSeparator()

    self.armazenar_menu = self.arquivo_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Armazenar") + ":")
    self.armazenar_zip_action = QAction(".ZIP", self)
    self.armazenar_zip_action.triggered.connect(self.gerenciador_interface.store_as_zip)
    self.armazenar_menu.addAction(self.armazenar_zip_action)

    self.armazenar_7z_action = QAction(".7Z", self)
    self.armazenar_7z_action.triggered.connect(self.gerenciador_interface.store_as_7z)
    self.armazenar_menu.addAction(self.armazenar_7z_action)

    self.armazenar_tar_action = QAction(".TAR", self)
    self.armazenar_tar_action.triggered.connect(self.gerenciador_interface.store_as_tar)
    self.armazenar_menu.addAction(self.armazenar_tar_action)

    self.armazenar_wim_action = QAction(".WIM", self)
    self.armazenar_wim_action.triggered.connect(self.gerenciador_interface.store_as_wim)
    self.armazenar_menu.addAction(self.armazenar_wim_action)

    self.arquivo_menu.addSeparator()

    self.extrair_arquivos_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Extrair Arquivos") + ":", self)
    self.extrair_arquivos_action.triggered.connect(self.gerenciador_interface.extract_files)
    self.arquivo_menu.addAction(self.extrair_arquivos_action)

    self.arquivo_menu.addSeparator()

    self.limpar_saida_menu = self.arquivo_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Limpar Saída") + ":")
    self.limpar_saida_zip_action = QAction(".ZIP", self)
    self.limpar_saida_zip_action.triggered.connect(self.gerenciador_interface.clear_output_listbox_zip)
    self.limpar_saida_menu.addAction(self.limpar_saida_zip_action)

    self.limpar_saida_7z_action = QAction(".7Z", self)
    self.limpar_saida_7z_action.triggered.connect(self.gerenciador_interface.clear_output_listbox_7z)
    self.limpar_saida_menu.addAction(self.limpar_saida_7z_action)

    self.limpar_saida_tar_action = QAction(".TAR", self)
    self.limpar_saida_tar_action.triggered.connect(self.gerenciador_interface.clear_output_listbox_tar)
    self.limpar_saida_menu.addAction(self.limpar_saida_tar_action)

    self.limpar_saida_wim_action = QAction(".WIM", self)
    self.limpar_saida_wim_action.triggered.connect(self.gerenciador_interface.clear_output_listbox_wim)
    self.limpar_saida_menu.addAction(self.limpar_saida_wim_action)

    self.limpar_saida_extracao_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Extração"), self)
    self.limpar_saida_extracao_action.triggered.connect(self.gerenciador_interface.clear_output_listbox_extracao)
    self.limpar_saida_menu.addAction(self.limpar_saida_extracao_action)

    self.arquivo_menu.addSeparator()

    self.sair_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Sair"), self)
    self.sair_action.triggered.connect(self.close)
    self.arquivo_menu.addAction(self.sair_action)

    self.config_menu = self.menu_bar.addMenu(QCoreApplication.translate("InterfaceGrafica", "Configurações"))

    self.compression_method_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Selecionar Método de Compressão"), self)
    self.compression_method_action.triggered.connect(self.select_compression_method)
    self.config_menu.addAction(self.compression_method_action)

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
    self.sobre_menu = self.opcoes_menu.addMenu(QCoreApplication.translate("InterfaceGrafica", "Sobre"))
    self.sobre_action = QAction(QCoreApplication.translate("InterfaceGrafica", "Sobre o Aplicativo"), self)
    self.sobre_action.triggered.connect(lambda: exibir_sobre(self))
    self.sobre_menu.addAction(self.sobre_action)

    self.config_menu.aboutToShow.connect(self.update_compression_menus)
