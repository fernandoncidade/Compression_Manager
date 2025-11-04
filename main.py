import sys
from PySide6.QtWidgets import QApplication
from source.InterfaceCore.intercore_01_InterfaceGrafica import InterfaceGrafica
from language.tr_01_gerenciadorTraducao import GerenciadorTraducao
from utils.LogManager import LogManager
# from utils.TrialManager import TrialManager

logger = LogManager.get_logger()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        gerenciador_traducao = GerenciadorTraducao()
        # TrialManager.enforce_trial()  # Descomente esta linha para forçar o uso da versão de avaliação
        # TrialManager.delete_first_run_timestamp()  # Use esta linha para testes, removendo o timestamp de primeiro uso
        window = InterfaceGrafica()
        window.show()
        exit_code = app.exec()
        logger.debug(f"Aplicação encerrada com código de saída: {exit_code}")
        sys.exit(exit_code)

    except Exception as e:
        logger.critical(f"Erro fatal ao iniciar aplicação: {e}", exc_info=True)
        sys.exit(1)
