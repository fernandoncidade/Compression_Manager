import sys
from queue import Queue
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QTreeView, QMessageBox)
from source.MotoresCompressao.mtcomp_02_motoresCompressao import (buscar_sevenzip_executavel, CompressaoZIP, Compressao7Z, CompressaoTAR, CompressaoWIM, TesteIntegridade, Extracao)
from .ui_03_dragDrop import DragDropListWidget
from .ui_04_dialogTraducao import FileDialogTraduzivel, MessageBoxTraduzivel
from utils.LogManager import LogManager

logger = LogManager.get_logger()


class GerenciadorInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.compress_queue = Queue()
        self.compress_threads = []
        self.dialogos_ativos = []
        self.compression_method_zip = None
        self.compression_method_7z = None
        self.compression_method_tar = None
        self.compression_method_wim = None
        self.update_existing = None
        self.last_directory = None

        self.sevenzip_executavel = buscar_sevenzip_executavel()

        if not self.sevenzip_executavel:
            print("7-Zip não encontrado. Por favor, instale o 7-Zip e tente novamente.")
            exit(1)

        self.output_listbox_zip = DragDropListWidget(accept_folders_only=True)
        self.output_listbox_7z = DragDropListWidget(accept_folders_only=True)
        self.output_listbox_tar = DragDropListWidget(accept_folders_only=True)
        self.output_listbox_wim = DragDropListWidget(accept_folders_only=True)
        self.output_listbox = DragDropListWidget(accept_folders_only=True)
        self.folder_listbox = DragDropListWidget()
        self.output_listbox_extracao = DragDropListWidget(accept_folders_only=True)
        self.compressed_files = []

        self.init_threads()

    def init_threads(self):
        self.compress_thread_zip = CompressaoZIP(self.sevenzip_executavel, self.update_existing, self.output_listbox, self.folder_listbox)
        self.compress_thread_zip.finished.connect(self.on_compress_finished)

        self.compress_thread_7z = Compressao7Z(self.sevenzip_executavel, self.update_existing, self.output_listbox, self.folder_listbox)
        self.compress_thread_7z.finished.connect(self.on_compress_finished)

        self.compress_thread_tar = CompressaoTAR(self.sevenzip_executavel, self.update_existing, self.output_listbox, self.folder_listbox)
        self.compress_thread_tar.finished.connect(self.on_compress_finished)

        self.compress_thread_wim = CompressaoWIM(self.sevenzip_executavel, self.update_existing, self.output_listbox, self.folder_listbox)
        self.compress_thread_wim.finished.connect(self.on_compress_finished)

        self.teste_integridade_thread = TesteIntegridade(self.sevenzip_executavel, self.compressed_files)
        self.teste_integridade_thread.finished.connect(self.on_teste_integridade_finished)

        self.extract_thread = Extracao(self.sevenzip_executavel, self.output_listbox, self.folder_listbox)
        self.extract_thread.finished.connect(self.on_extract_finished)

    def browse_folder(self):
        self._browse(QFileDialog.FileMode.Directory, self.folder_listbox)

    def browse_file(self):
        self._browse(QFileDialog.FileMode.ExistingFiles, self.folder_listbox)

    def browse_output(self):
        self._browse(QFileDialog.FileMode.Directory, self.output_listbox)
        self._browse(QFileDialog.FileMode.Directory, self.output_listbox_zip)
        self._browse(QFileDialog.FileMode.Directory, self.output_listbox_7z)
        self._browse(QFileDialog.FileMode.Directory, self.output_listbox_tar)
        self._browse(QFileDialog.FileMode.Directory, self.output_listbox_wim)
        self._browse(QFileDialog.FileMode.Directory, self.output_listbox_extracao)

    def _browse(self, file_mode, listbox):
        import os

        if sys.platform == "win32" and file_mode == QFileDialog.FileMode.Directory:
            dialog = FileDialogTraduzivel()
            dialog.setFileMode(file_mode)
            dialog.setOption(QFileDialog.Option.DontUseNativeDialog, False)
            dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
            dialog.traduzir_botoes()

            if self.last_directory and os.path.exists(self.last_directory):
                dialog.setDirectory(self.last_directory)

            continue_selecting = True
            first_selection = True

            while continue_selecting:
                dialog_title = QCoreApplication.translate("InterfaceGrafica", "Selecione um diretório") if first_selection else QCoreApplication.translate("InterfaceGrafica", "Selecione outro diretório")
                dialog.setWindowTitle(dialog_title)

                if dialog.exec() == QFileDialog.DialogCode.Accepted:
                    selected_dirs = dialog.selectedFiles()
                    if selected_dirs:
                        for dir_path in selected_dirs:
                            exists = False
                            for i in range(listbox.count()):
                                if listbox.item(i).text() == dir_path:
                                    exists = True
                                    break

                            if not exists:
                                listbox.addItem(dir_path)

                        self.last_directory = os.path.dirname(selected_dirs[0])

                    msg_box = MessageBoxTraduzivel(
                        QMessageBox.Icon.Question,
                        QCoreApplication.translate("InterfaceGrafica", "Seleção Múltipla"),
                        QCoreApplication.translate("InterfaceGrafica", "Deseja adicionar mais diretórios?"),
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )

                    self.dialogos_ativos.append(msg_box)
                    msg_box.finished.connect(lambda: self.dialogos_ativos.remove(msg_box) if msg_box in self.dialogos_ativos else None)

                    reply = msg_box.exec()
                    continue_selecting = (reply == QMessageBox.StandardButton.Yes)
                    first_selection = False

                    if continue_selecting and self.last_directory:
                        dialog.setDirectory(self.last_directory)

                else:
                    continue_selecting = False

            return

        dialog = FileDialogTraduzivel()
        dialog.setFileMode(file_mode)
        dialog.traduzir_botoes()

        if file_mode == QFileDialog.FileMode.ExistingFiles:
            dialog.setWindowTitle(QCoreApplication.translate("InterfaceGrafica", "Selecionar Arquivos"))

        else:
            dialog.setWindowTitle(QCoreApplication.translate("InterfaceGrafica", "Selecionar"))

        if self.last_directory and os.path.exists(self.last_directory):
            dialog.setDirectory(self.last_directory)

        if file_mode == QFileDialog.FileMode.Directory:
            dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)

        tree_view = dialog.findChild(QTreeView)
        if tree_view:
            tree_view.setSelectionMode(QTreeView.SelectionMode.ExtendedSelection)

        if dialog.exec() == QFileDialog.DialogCode.Accepted:
            selected_items = dialog.selectedFiles()
            if selected_items:
                listbox.addItems(selected_items)
                self.last_directory = os.path.dirname(selected_items[0])

    def select_output_path(self, output_listbox):
        self._browse(QFileDialog.FileMode.Directory, output_listbox)

    def output_button_output_ZIP_clicked(self):
        self.select_output_path(self.output_listbox_zip)

    def output_button_output_7Z_clicked(self):
        self.select_output_path(self.output_listbox_7z)

    def output_button_output_TAR_clicked(self):
        self.select_output_path(self.output_listbox_tar)
    
    def output_button_output_WIM_clicked(self):
        self.select_output_path(self.output_listbox_wim)

    def output_button_output_EXTRACAO_clicked(self):
        self.select_output_path(self.output_listbox_extracao)

    def clear_folders(self):
        self.folder_listbox.clear()

    def clear_output(self):
        self.output_listbox.clear()
        self.output_listbox_zip.clear()
        self.output_listbox_7z.clear()
        self.output_listbox_tar.clear()
        self.output_listbox_wim.clear()
        self.output_listbox_extracao.clear()

    def clear_output_listbox_zip(self):
        self.output_listbox_zip.clear()

    def clear_output_listbox_7z(self):
        self.output_listbox_7z.clear()

    def clear_output_listbox_tar(self):
        self.output_listbox_tar.clear()

    def clear_output_listbox_wim(self):
        self.output_listbox_wim.clear()

    def clear_output_listbox_extracao(self):
        self.output_listbox_extracao.clear()

    def store_as_zip(self):
        self._store_as(self.compress_thread_zip, self.output_listbox_zip, self.compression_method_zip)

    def store_as_7z(self):
        self._store_as(self.compress_thread_7z, self.output_listbox_7z, self.compression_method_7z)

    def store_as_tar(self):
        self._store_as(self.compress_thread_tar, self.output_listbox_tar, self.compression_method_tar)

    def store_as_wim(self):
        self._store_as(self.compress_thread_wim, self.output_listbox_wim, self.compression_method_wim)

    def _store_as(self, thread, output_listbox, compression_method):
        if self.folder_listbox.count() == 0:
            self.show_selection_compression_warning()

        elif output_listbox.count() == 0:
            self.show_selection_destination_warning()

        elif compression_method is not None:
            new_thread = thread.__class__(thread.executable, self.update_existing, output_listbox, self.folder_listbox, compress_as=True, compression_method=compression_method)
            new_thread.finished.connect(self.on_compress_finished)
            self.start_compression_thread(new_thread)

        else:
            self.show_method_warning()

    def testar_integridade(self):
        selected_files = [self.folder_listbox.item(idx).text() for idx in range(self.folder_listbox.count())]
        SUPPORTED_EXTS = ('.rar', '.zip', '.7z', '.bz2', '.tar', '.wim', '.tar.xz', '.zipx', '.tgz', '.tar.gz', '.lzh', '.iso')
        compressed_files = [file for file in selected_files if file.lower().endswith(SUPPORTED_EXTS)]

        if not compressed_files:
            self.show_extension_warning()
            return

        if self.sevenzip_executavel:
            self.teste_integridade_thread = TesteIntegridade(self.sevenzip_executavel, compressed_files)
            self.teste_integridade_thread.finished.connect(self.on_teste_integridade_finished)
            self.teste_integridade_thread.start()

        else:
            self.show_extract_warning()

    def extract_files(self):
        if self.folder_listbox.count() == 0:
            self.show_selection_descompression_warning()

        elif self.output_listbox_extracao.count() == 0:
            self.show_selection_destination_warning()

        else:
            self._start_extraction_thread()

    def _start_extraction_thread(self):
        if not self.sevenzip_executavel:
            self.show_extract_warning()
            return

        self.extract_thread = Extracao(self.sevenzip_executavel, self.output_listbox_extracao, self.folder_listbox)
        self.extract_thread.finished.connect(self.on_extract_finished)
        self.extract_thread.start()

    def start_compression_thread(self, new_thread):
        new_format = new_thread.format

        if any(thread.isRunning() and thread.format == new_format for thread in self.compress_threads):
            self.compress_queue.put(new_thread)
            self.show_queue_warning()

        else:
            new_thread.start()
            self.compress_threads.append(new_thread)

    def on_compress_finished(self):
        finished_thread = self.sender()
        self.compress_threads.remove(finished_thread)

        if not self.compress_queue.empty():
            next_thread = self.compress_queue.get()
            self.start_compression_thread(next_thread)

        elif not self.compress_threads:
            self.show_info_message(
                QCoreApplication.translate("InterfaceGrafica", "Empacotamento Concluído"),
                QCoreApplication.translate("InterfaceGrafica", "O Empacotamento dos arquivos foi concluído com sucesso!")
            )

    def on_teste_integridade_finished(self):
        self.show_info_message(
            QCoreApplication.translate("InterfaceGrafica", "Teste de Integridade Concluído"),
            QCoreApplication.translate("InterfaceGrafica", "O teste de integridade dos arquivos foi concluído com sucesso!")
        )

    def on_extract_finished(self):
        self.show_info_message(
            QCoreApplication.translate("InterfaceGrafica", "Extração Concluída"),
            QCoreApplication.translate("InterfaceGrafica", "A Extração dos arquivos foi concluída com sucesso!")
        )

    def show_queue_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "O processo solicitado foi colocado em fila, aguardando o anterior encerrar.")
        )

    def show_method_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "Por favor, selecione um método de compressão antes de prosseguir.")
        )

    def show_integridade_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "Por favor, selecione um arquivo para testar a integridade.")
        )

    def show_extension_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "Por favor, selecione um arquivo COMPACTADO para prosseguir.")
        )

    def show_extract_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "7-Zip não encontrado. Por favor, instale o 7-Zip e tente novamente.")
        )

    def show_selection_compression_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "Por favor, selecione uma pasta antes de prosseguir.")
        )

    def show_selection_descompression_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "Por favor, selecione um arquivo antes de prosseguir.")
        )

    def show_selection_destination_warning(self):
        self.show_warning(
            QCoreApplication.translate("InterfaceGrafica", "Aviso"),
            QCoreApplication.translate("InterfaceGrafica", "Por favor, selecione um diretório de saída antes de prosseguir.")
        )

    def show_warning(self, title, message):
        self.show_message(QMessageBox.Icon.Warning, title, message)

    def show_info_message(self, title, message):
        self.show_message(QMessageBox.Icon.Information, title, message)

    def atualizar_traducoes_dialogos(self):
        for dialogo in self.dialogos_ativos:
            if hasattr(dialogo, "atualizar_traducao"):
                dialogo.atualizar_traducao()

    def show_message(self, icon, title, message):
        msg_box = MessageBoxTraduzivel(icon, title, message)

        self.dialogos_ativos.append(msg_box)
        msg_box.finished.connect(lambda: self.dialogos_ativos.remove(msg_box) if msg_box in self.dialogos_ativos else None)

        msg_box.exec()
