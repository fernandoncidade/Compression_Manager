from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def mudar_idioma(self, codigo_idioma):
    self.pt_br_action.setChecked(codigo_idioma == "pt_BR")
    self.en_us_action.setChecked(codigo_idioma == "en_US")

    self.gerenciador_traducao.definir_idioma(codigo_idioma)
