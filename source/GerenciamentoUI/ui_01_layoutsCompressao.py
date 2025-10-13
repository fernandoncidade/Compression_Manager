from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import Qt, QCoreApplication
from utils.LogManager import LogManager

logger = LogManager.get_logger()


class LayoutsCompressao:
    def __init__(self, gerenciador_interface, create_button):
        self.gerenciador_interface = gerenciador_interface
        self.create_button = create_button
        self._max_left_width = 0
        self._left_widgets = []

    def create_compression_method_layouts(self):
        methods = ['zip', '7z', 'tar', 'wim', 'extracao']
        return {method: getattr(self, f'create_{method.replace(".", "_")}_layout') for method in methods}

    def create_layout(self, method, icon_name, store_callback, clear_callback):
        layout = QHBoxLayout()
        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()
        layout_1.insertStretch(0, 1)

        base_text = QCoreApplication.translate("InterfaceGrafica", "Especificar Saída")
        method_display = method
        if method == "extracao":
            method_display = QCoreApplication.translate("InterfaceGrafica", "Extração")

        else:
            method_display = f".{method.upper()}"

        output_label_text = f"{base_text} {method_display}:"

        output_hbox = QHBoxLayout()
        output_label = QLabel(output_label_text)
        output_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        output_callback = getattr(self.gerenciador_interface, f'output_button_output_{method.upper()}_clicked')
        output_button = self.create_button("", output_callback, icon="saida.png")
        output_hbox.addWidget(output_label)
        output_hbox.addStretch(1)
        output_hbox.addWidget(output_button)
        layout_1.addLayout(output_hbox)

        store_text = QCoreApplication.translate("InterfaceGrafica", "Armazenar")
        if method == "extracao":
            store_label_text = QCoreApplication.translate("InterfaceGrafica", "Extrair Arquivos") + ":"

        else:
            store_label_text = f"{store_text} {method_display}:"

        store_hbox = QHBoxLayout()
        store_label = QLabel(store_label_text)
        store_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        store_button = self.create_button("", store_callback, icon=icon_name)
        store_hbox.addWidget(store_label)
        store_hbox.addStretch(1)
        store_hbox.addWidget(store_button)
        layout_1.addLayout(store_hbox)

        clear_label_text = QCoreApplication.translate("InterfaceGrafica", "Limpar Saída") + ":"
        clear_hbox = QHBoxLayout()
        clear_label = QLabel(clear_label_text)
        clear_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        clear_button = self.create_button("", clear_callback, icon="clear_button2.png")
        clear_hbox.addWidget(clear_label)
        clear_hbox.addStretch(1)
        clear_hbox.addWidget(clear_button)
        layout_1.addLayout(clear_hbox)

        try:
            left_right_margins = layout_1.contentsMargins().left() + layout_1.contentsMargins().right()
            spacing_padding = 20

            hbox_widths = []
            for lbl, btn, hbox in ((output_label, output_button, output_hbox),
                                   (store_label, store_button, store_hbox),
                                   (clear_label, clear_button, clear_hbox)):
                label_w = lbl.fontMetrics().horizontalAdvance(lbl.text())
                button_w = btn.sizeHint().width()
                hbox_margins = hbox.contentsMargins().left() + hbox.contentsMargins().right()
                hbox_widths.append(label_w + button_w + left_right_margins + hbox_margins + spacing_padding)

            required_width = max(hbox_widths)

            if required_width > self._max_left_width:
                self._max_left_width = required_width

            left_widget = QWidget()
            left_widget.setLayout(layout_1)
            left_widget.setMinimumWidth(self._max_left_width)

            for w in self._left_widgets:
                try:
                    w.setMinimumWidth(self._max_left_width)

                except Exception:
                    pass

            self._left_widgets.append(left_widget)

            layout.addWidget(left_widget)
            layout.addLayout(layout_2, 1)

        except Exception as e:
            logger.exception("Erro ao calcular largura mínima do layout_1: %s", e)
            layout.addLayout(layout_1, 1)
            layout.addLayout(layout_2, 3)

        output_dir_text = QCoreApplication.translate("InterfaceGrafica", "Diretório(s) de saída")
        if method == "extracao":
            output_label_text = QCoreApplication.translate("InterfaceGrafica", "Diretório(s) de destino para extração:")

        else:
            output_label_text = f"{output_dir_text} {method_display}:"

        output_label = QLabel(output_label_text)
        layout_2.addWidget(output_label)

        listbox = getattr(self.gerenciador_interface, f'output_listbox_{method}')
        listbox.setMinimumHeight(82)
        layout_2.addWidget(listbox)

        return layout

    def create_zip_layout(self):
        return self.create_layout('zip', 'winzip4.png', self.gerenciador_interface.store_as_zip, self.gerenciador_interface.clear_output_listbox_zip)

    def create_7z_layout(self):
        return self.create_layout('7z', 'sevenzip3.png', self.gerenciador_interface.store_as_7z, self.gerenciador_interface.clear_output_listbox_7z)

    def create_tar_layout(self):
        return self.create_layout('tar', 'tar1.png', self.gerenciador_interface.store_as_tar, self.gerenciador_interface.clear_output_listbox_tar)

    def create_wim_layout(self):
        return self.create_layout('wim', 'wim.png', self.gerenciador_interface.store_as_wim, self.gerenciador_interface.clear_output_listbox_wim)

    def create_extracao_layout(self):
        return self.create_layout('extracao', 'extracao4.png', self.gerenciador_interface.extract_files, self.gerenciador_interface.clear_output_listbox_extracao)
