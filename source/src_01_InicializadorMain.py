import sys
from PySide6.QtWidgets import QApplication
from source.InterfaceCore.intercore_01_InterfaceGrafica import InterfaceGrafica
from source.language.tr_01_gerenciadorTraducao import GerenciadorTraducao
from source.utils.LogManager import LogManager
# from source.utils.TrialManager import TrialManager

logger = LogManager.get_logger()

def iniciar_aplicacao() -> int:
    try:
        app = QApplication(sys.argv)
        gerenciador_traducao = GerenciadorTraducao()
        # TrialManager.enforce_trial()  # Descomente esta linha para forçar o uso da versão de avaliação
        # TrialManager.delete_first_run_timestamp()  # Use esta linha para testes, removendo o timestamp de primeiro uso
        window = InterfaceGrafica()
        window.show()
        exit_code = app.exec()
        logger.debug(f"Aplicação encerrada com código de saída: {exit_code}")
        return int(exit_code)

    except Exception as e:
        logger.critical(f"Erro fatal ao iniciar aplicação: {e}", exc_info=True)
        return 1
