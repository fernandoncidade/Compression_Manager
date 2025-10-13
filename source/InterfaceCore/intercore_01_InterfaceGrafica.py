from PySide6.QtWidgets import QMainWindow
from source.GerenciamentoUI.ui_01_layoutsCompressao import LayoutsCompressao
from source.GerenciamentoUI.ui_02_gerenteGUILayouts import GerenciadorInterface
from source.MotoresCompressao.mtcomp_01_metodosCompressao import MetodoCompressao
from language.tr_01_gerenciadorTraducao import GerenciadorTraducao

from .GerenciadorInterfaceGrafica.ginter_01_init_menu import init_menu
from .GerenciadorInterfaceGrafica.ginter_02_update_compression_menus import update_compression_menus
from .GerenciadorInterfaceGrafica.ginter_03_mudar_idioma import mudar_idioma
from .GerenciadorInterfaceGrafica.ginter_04_retranslateUi import retranslateUi
from .GerenciadorInterfaceGrafica.ginter_05_init_ui import init_ui
from .GerenciadorInterfaceGrafica.ginter_06_create_widget_with_layout import create_widget_with_layout
from .GerenciadorInterfaceGrafica.ginter_07_create_main_layout_1 import create_main_layout_1
from .GerenciadorInterfaceGrafica.ginter_08_create_first_quadrant import create_first_quadrant
from .GerenciadorInterfaceGrafica.ginter_09_create_second_quadrant import create_second_quadrant
from .GerenciadorInterfaceGrafica.ginter_10_rebuild_method_layouts import rebuild_method_layouts
from .GerenciadorInterfaceGrafica.ginter_11_create_main_layout_2 import create_main_layout_2
from .GerenciadorInterfaceGrafica.ginter_12_create_third_quadrant import create_third_quadrant
from .GerenciadorInterfaceGrafica.ginter_13_create_scroll_area import create_scroll_area
from .GerenciadorInterfaceGrafica.ginter_14_create_button import create_button
from .GerenciadorInterfaceGrafica.ginter_15_create_method_checkboxes import create_method_checkboxes
from .GerenciadorInterfaceGrafica.ginter_16_on_method_toggled import on_method_toggled
from .GerenciadorInterfaceGrafica.ginter_17_adjust_scroll_area import adjust_scroll_area
from .GerenciadorInterfaceGrafica.ginter_18_remove_layout_widgets import remove_layout_widgets
from .GerenciadorInterfaceGrafica.ginter_19_closeEvent import closeEvent
from utils.LogManager import LogManager

logger = LogManager.get_logger()


class InterfaceGrafica(QMainWindow, MetodoCompressao):
    def __init__(self):
        super().__init__()
        self.gerenciador_interface = GerenciadorInterface()
        self.layouts_compressao = LayoutsCompressao(self.gerenciador_interface, self.create_button)
        self.compression_method_layouts = self.layouts_compressao.create_compression_method_layouts()
        self.current_layouts = {}

        self.gerenciador_traducao = GerenciadorTraducao()
        self.gerenciador_traducao.idioma_alterado.connect(self.retranslateUi)
        self.gerenciador_traducao.aplicar_traducao()

        self.traduzir_widgets = {}

        self.init_menu()
        self.init_ui()
        MetodoCompressao.load_compression_method(self)

    def init_menu(self):
        init_menu(self)

    def update_compression_menus(self):
        update_compression_menus(self)

    def mudar_idioma(self, codigo_idioma):
        mudar_idioma(self, codigo_idioma)

    def retranslateUi(self):
        retranslateUi(self)

    def init_ui(self):
        init_ui(self)

    def create_widget_with_layout(self, layout):
        return create_widget_with_layout(self, layout)

    def create_main_layout_1(self):
        return create_main_layout_1(self)

    def create_first_quadrant(self):
        return create_first_quadrant(self)

    def create_second_quadrant(self):
        return create_second_quadrant(self)

    def rebuild_method_layouts(self):
        rebuild_method_layouts(self)

    def create_main_layout_2(self):
        return create_main_layout_2(self)

    def create_third_quadrant(self):
        return create_third_quadrant(self)

    def create_scroll_area(self):
        return create_scroll_area(self)

    def create_button(self, text, callback=None, icon=None):
        return create_button(self, text, callback, icon)

    def create_method_checkboxes(self, layout):
        return create_method_checkboxes(self, layout)

    def on_method_toggled(self):
        on_method_toggled(self)

    def adjust_scroll_area(self):
        adjust_scroll_area(self)

    def remove_layout_widgets(self, layout):
        remove_layout_widgets(self, layout)

    def closeEvent(self, event):
        closeEvent(self, event)
