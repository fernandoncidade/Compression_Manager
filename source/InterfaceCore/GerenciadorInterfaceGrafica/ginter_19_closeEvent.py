from utils.LogManager import LogManager

logger = LogManager.get_logger()

def closeEvent(self, event):
    if hasattr(self, 'gerenciador_traducao') and self.gerenciador_traducao.tradutor:
        self.gerenciador_traducao.app.removeTranslator(self.gerenciador_traducao.tradutor)

    super(self.__class__, self).closeEvent(event)
