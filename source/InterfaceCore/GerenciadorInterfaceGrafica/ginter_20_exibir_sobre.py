from PySide6.QtCore import QCoreApplication
from source.GerenciamentoUI.ui_06_SobreDialog import SobreDialog
from source.GerenciamentoUI.ui_05_OpcoesSobre import (
    SITE_LICENSES,
    LICENSE_TEXT_PT_BR, LICENSE_TEXT_EN_US,
    NOTICE_TEXT_PT_BR, NOTICE_TEXT_EN_US,
    ABOUT_TEXT_PT_BR, ABOUT_TEXT_EN_US,
    Privacy_Policy_pt_BR, Privacy_Policy_en_US,
    History_APP_pt_BR, History_APP_en_US,
    RELEASE_NOTES_pt_BR, RELEASE_NOTES_en_US,
    LICENSE_OWNER
)
from PySide6.QtWidgets import QMessageBox
from utils.LogManager import LogManager
logger = LogManager.get_logger()

def get_text(text):
    return QCoreApplication.translate("InterfaceGrafica", text)

def exibir_sobre(app):
    try:
        idioma = app.gerenciador_traducao.obter_idioma_atual()
        textos_sobre = { "pt_BR": ABOUT_TEXT_PT_BR, "en_US": ABOUT_TEXT_EN_US }
        textos_licenca = { "pt_BR": LICENSE_TEXT_PT_BR, "en_US": LICENSE_TEXT_EN_US }
        textos_aviso = { "pt_BR": NOTICE_TEXT_PT_BR, "en_US": NOTICE_TEXT_EN_US }
        textos_privacidade = { "pt_BR": Privacy_Policy_pt_BR, "en_US": Privacy_Policy_en_US }
        history_texts = { "pt_BR": History_APP_pt_BR, "en_US": History_APP_en_US }
        release_notes_texts = { "pt_BR": RELEASE_NOTES_pt_BR, "en_US": RELEASE_NOTES_en_US }

        descricao_texts = {
            "pt_BR": (
                "COMPRESSION MANAGER é um utilitário gráfico leve para Windows projetado para "
                "empacotamento, extração e verificação de integridade de arquivos e pastas. "
                "Oferece suporte a múltiplos formatos (ZIP, 7Z, TAR, WIM e outros reconhecidos "
                "pelo 7‑Zip), seleção de vários diretórios de saída, métodos de compressão "
                "configuráveis, fila de processos e operação via arrastar-e-soltar. A interface "
                "é multilíngue (pt_BR / en_US) e preparada para empacotamento como executável "
                "(distribuição sem necessidade de instalação manual de dependências Python)."
            ),
            "en_US": (
                "COMPRESSION MANAGER is a lightweight graphical utility for Windows designed "
                "for packing, extracting and integrity checking of files and folders. It "
                "supports multiple formats (ZIP, 7Z, TAR, WIM and others recognized by 7‑Zip), "
                "selection of multiple output directories, configurable compression methods, "
                "process queuing and drag-and-drop operation. The interface is multilingual "
                "(pt_BR / en_US) and prepared for packaging as an executable (distribution "
                "without requiring manual installation of Python dependencies)."
            )
        }

        texto_sobre = textos_sobre.get(idioma, textos_sobre["en_US"])
        texto_licenca = textos_licenca.get(idioma, textos_licenca["en_US"])
        texto_aviso = textos_aviso.get(idioma, textos_aviso["en_US"])
        texto_privacidade = textos_privacidade.get(idioma, textos_privacidade["en_US"])
        texto_history = history_texts.get(idioma, history_texts["en_US"])
        texto_release_notes = release_notes_texts.get(idioma, release_notes_texts["en_US"])
        texto_descricao = descricao_texts.get(idioma, descricao_texts["en_US"])

        try:
            license_file_text = LICENSE_OWNER or ""

        except NameError:
            license_file_text = ""

        if license_file_text:
            texto_licenca = f"{texto_licenca}\n\n{license_file_text}"

        cabecalho_fixo = (
            "<h3>COMPRESSION MANAGER</h3>"
            f"<p><b>{get_text('Versão')}:</b> 0.0.3.0</p>"
            f"<p><b>{get_text('Autores')}:</b> Fernando Nillsson Cidade</p>"
            f"<p><b>{get_text('Descrição')}:</b> {texto_descricao}</p>"
        )

        dialog = SobreDialog(
            app,
            titulo=f"{get_text('Sobre')} - COMPRESSION MANAGER",
            texto_fixo=cabecalho_fixo,
            texto_history=texto_history,
            detalhes=texto_sobre,
            licencas=texto_licenca,
            sites_licencas=SITE_LICENSES,
            show_history_text=get_text("Histórico"),
            hide_history_text=get_text("Ocultar histórico"),
            show_details_text=get_text("Detalhes"),
            hide_details_text=get_text("Ocultar detalhes"),
            show_licenses_text=get_text("Licenças"),
            hide_licenses_text=get_text("Ocultar licenças"),
            ok_text=QCoreApplication.translate("Dialog", "OK"),
            site_oficial_text=get_text("Site oficial"),
            avisos=texto_aviso,
            show_notices_text=get_text("Avisos"),
            hide_notices_text=get_text("Ocultar avisos"),
            Privacy_Policy=texto_privacidade,
            show_privacy_policy_text=get_text("Política de Privacidade"),
            hide_privacy_policy_text=get_text("Ocultar política de privacidade"),
            info_not_available_text=get_text("Informação não disponível"),
            release_notes=texto_release_notes,
            show_release_notes_text=get_text("Notas de Versão"),
            hide_release_notes_text=get_text("Ocultar notas de versão")
        )
        dialog.resize(900, 500)
        dialog.show()

    except Exception as e:
        logger.error(f"Erro ao exibir diálogo Sobre: {e}", exc_info=True)
        QMessageBox.critical(app, get_text("Erro"), f"{get_text('Erro')}: {e}")
