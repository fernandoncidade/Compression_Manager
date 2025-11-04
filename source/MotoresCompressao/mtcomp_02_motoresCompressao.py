import os
import sys
import subprocess
import tempfile
from PySide6.QtCore import QThread, Signal
from utils.LogManager import LogManager
from utils.ApplicationPathUtils import get_app_base_path

logger = LogManager.get_logger()


SEVENZIP_PATHS = [
    rf"C:\Program Files\7-Zip\7zG.exe",
    rf"C:\Program Files (x86)\7-Zip\7zG.exe",
]

def buscar_executavel(nome_pasta, nome_executavel, possiveis_caminhos):
    try:
        app_base_path = get_app_base_path()
        caminho_executavel_bundle = os.path.join(app_base_path, nome_pasta, nome_executavel)
        if os.path.exists(caminho_executavel_bundle):
            return caminho_executavel_bundle

        dir_atual = getattr(sys, '_MEIPASS', os.path.dirname(os.path.realpath(__file__)))
        caminho_executavel = os.path.join(dir_atual, nome_pasta, nome_executavel)
        if os.path.exists(caminho_executavel):
            return caminho_executavel

        for caminho in possiveis_caminhos:
            if os.path.isfile(caminho):
                return caminho

        return None

    except Exception as e:
        logger.error(f"Erro ao buscar executável '{nome_executavel}': {e}", exc_info=True)
        return None

def buscar_sevenzip_executavel():
    try:
        return buscar_executavel("7-Zip", "7zG.exe", SEVENZIP_PATHS)

    except Exception as e:
        logger.error(f"Erro ao buscar executável 7-Zip: {e}", exc_info=True)
        return None


class CompressaoBase(QThread):
    finished = Signal()

    def __init__(self, executable, update_existing, output_listbox, folder_listbox, compress_as=False, compression_method=None):
        try:
            super().__init__()
            self.executable = executable
            self.update_existing = update_existing
            self.output_listbox = output_listbox
            self.folder_listbox = folder_listbox
            self.compress_as = compress_as
            self.compression_method = compression_method
            self.format = None

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def run(self):
        try:
            output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
            if not output_paths:
                return

            for idx in range(self.folder_listbox.count()):
                folder_path = self.folder_listbox.item(idx).text()
                folder_name = os.path.basename(folder_path)

                for output_path in output_paths:
                    self.comprimir(output_path, folder_path, folder_name)

        except Exception as e:
            logger.error(f"Erro no método run de {self.__class__.__name__}: {e}", exc_info=True)


class CompressaoZIP(CompressaoBase):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
            self.format = 'zip'

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def comprimir(self, output_path, folder_path, folder_name):
        try:
            compressed_file = os.path.join(output_path, f"{folder_name}.zip")
            command = f'"{self.executable}" a -r -tzip -mx={self.compression_method} "{compressed_file}" "{folder_path}"'

            if self.update_existing:
                command = f'"{self.executable}" u -r -tzip -mx={self.compression_method} "{compressed_file}" "{folder_path}"'

            subprocess.run(command, shell=True)

        except Exception as e:
            logger.error(f"Erro ao comprimir (ZIP) pasta '{folder_path}' em '{output_path}': {e}", exc_info=True)


class Compressao7Z(CompressaoBase):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
            self.format = '7z'

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def comprimir(self, output_path, folder_path, folder_name):
        try:
            compressed_file = os.path.join(output_path, f"{folder_name}.7z")
            command = f'"{self.executable}" a -r -t7z -mx={self.compression_method} "{compressed_file}" "{folder_path}"'

            if self.update_existing:
                command = f'"{self.executable}" u -r -t7z -mx={self.compression_method} "{compressed_file}" "{folder_path}"'

            subprocess.run(command, shell=True)

        except Exception as e:
            logger.error(f"Erro ao comprimir (7Z) pasta '{folder_path}' em '{output_path}': {e}", exc_info=True)


class CompressaoTAR(CompressaoBase):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
            self.format = 'tar'

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def comprimir(self, output_path, folder_path, folder_name):
        try:
            compressed_file = os.path.join(output_path, f"{folder_name}.tar")
            command = f'"{self.executable}" a -r -ttar "{compressed_file}" "{folder_path}"'

            if self.update_existing:
                command = f'"{self.executable}" u -r -ttar "{compressed_file}" "{folder_path}"'

            subprocess.run(command, shell=True)

        except Exception as e:
            logger.error(f"Erro ao comprimir (TAR) pasta '{folder_path}' em '{output_path}': {e}", exc_info=True)


class CompressaoWIM(CompressaoBase):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
            self.format = 'wim'

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def comprimir(self, output_path, folder_path, folder_name):
        try:
            compressed_file = os.path.join(output_path, f"{folder_name}.wim")
            command = f'"{self.executable}" a -r -twim "{compressed_file}" "{folder_path}"'

            if self.update_existing:
                command = f'"{self.executable}" u -r -twim "{compressed_file}" "{folder_path}"'

            subprocess.run(command, shell=True)

        except Exception as e:
            logger.error(f"Erro ao comprimir (WIM) pasta '{folder_path}' em '{output_path}': {e}", exc_info=True)


class TesteIntegridade(QThread):
    finished = Signal()

    def __init__(self, sevenzip_executable, compressed_files):
        try:
            super(TesteIntegridade, self).__init__()
            self.sevenzip_executable = sevenzip_executable
            self.compressed_files = compressed_files

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def run(self):
        try:
            SUPPORTED_EXTS = ('.rar', '.zip', '.7z', '.bz2', '.tar', '.wim', '.tar.xz', '.zipx', '.tgz', '.tar.gz', '.lzh', '.iso')
            for compressed_file in self.compressed_files:
                cf_lower = compressed_file.lower()
                if cf_lower.endswith(SUPPORTED_EXTS):
                    command = f'"{self.sevenzip_executable}" t "{compressed_file}"'
                    result = subprocess.run(command, shell=True, check=True)
                    if result.returncode != 0:
                        raise Exception("A verificação da integridade do arquivo falhou")

        except Exception as e:
            logger.error(f"Erro no método run de {self.__class__.__name__}: {e}", exc_info=True)


class Extracao(QThread):
    finished = Signal()

    def __init__(self, sevenzip_executable, output_listbox, folder_listbox):
        try:
            super().__init__()
            self.sevenzip_executable = sevenzip_executable
            self.output_listbox = output_listbox
            self.folder_listbox = folder_listbox

        except Exception as e:
            logger.error(f"Erro ao inicializar {self.__class__.__name__}: {e}", exc_info=True)

    def run(self):
        try:
            output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
            if not output_paths:
                return

            for idx in range(self.folder_listbox.count()):
                archive_path = self.folder_listbox.item(idx).text()
                for output_path in output_paths:
                    self.extrair(archive_path, output_path)

        except Exception as e:
            logger.error(f"Erro no método run de {self.__class__.__name__}: {e}", exc_info=True)

    def extrair(self, archive_path, output_path):
        try:
            if archive_path.endswith((".rar", ".zip", ".7z", ".tar", ".wim")):
                command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{output_path}"'
                subprocess.run(command, shell=True)

            elif archive_path.endswith(".bz2"):
                with tempfile.TemporaryDirectory() as temp_dir:

                    temp_tar_path = os.path.join(temp_dir, os.path.basename(archive_path).replace('.bz2', ''))
                    command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{temp_dir}"'
                    subprocess.run(command, shell=True)

                    command = f'"{self.sevenzip_executable}" x -y "{temp_tar_path}" -o"{output_path}"'
                    subprocess.run(command, shell=True)

            elif archive_path.endswith(".tar.xz") or archive_path.endswith(".tgz") or archive_path.endswith(".tar.gz"):
                with tempfile.TemporaryDirectory() as temp_dir:

                    temp_tar_path = os.path.join(temp_dir, os.path.basename(archive_path).replace('.xz', '').replace('.tgz', '.tar').replace('.gz', ''))
                    command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{temp_dir}"'
                    subprocess.run(command, shell=True)

                    command = f'"{self.sevenzip_executable}" x -y "{temp_tar_path}" -o"{output_path}"'
                    subprocess.run(command, shell=True)

            elif archive_path.endswith(".zipx") or archive_path.endswith(".lzh") or archive_path.endswith(".iso"):
                command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{output_path}"'
                subprocess.run(command, shell=True)

        except Exception as e:
            logger.error(f"Erro no método extrair de {self.__class__.__name__}: {e}", exc_info=True)
