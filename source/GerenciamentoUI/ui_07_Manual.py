from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QCoreApplication
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

# Textos do Manual (PT-BR e EN-US)
MANUAL_TEXT_PT_BR = """
<h2>COMPRESSION MANAGER - Manual do Usuário</h2>

<h3>1. Empacotamento</h3>
<p>Para empacotar arquivos ou pastas:</p>
<ul>
    <li>Arraste e solte os arquivos ou pastas na área principal ou utilize os botões de seleção.</li>
    <li>Selecione o formato desejado (ZIP, 7Z, TAR, WIM, etc).</li>
    <li>Configure o método de compressão, se necessário.</li>
    <li>Clique no botão para iniciar e adicionar à fila de processos.</li>
</ul>

<h3>2. Extração</h3>
<p>Para extrair arquivos:</p>
<ul>
    <li>Selecione o arquivo compactado que deseja extrair.</li>
    <li>Escolha o diretório de destino.</li>
    <li>Inicie o processo de extração.</li>
</ul>

<h3>3. Verificação de Integridade</h3>
<p>Para garantir que um arquivo não está corrompido:</p>
<ul>
    <li>Selecione o arquivo e utilize a opção de verificação de integridade.</li>
</ul>

<h3>4. Configurações e Idioma</h3>
<p>No menu superior, você pode:</p>
<ul>
    <li>Alterar o idioma (Português ou Inglês) em <b>Configurações &gt; Idiomas</b>.</li>
    <li>Alternar entre layouts.</li>
</ul>
"""

MANUAL_TEXT_EN_US = """
<h2>COMPRESSION MANAGER - User Manual</h2>

<h3>1. Packing</h3>
<p>To pack files or folders:</p>
<ul>
    <li>Drag and drop files or folders into the main area or use the selection buttons.</li>
    <li>Select the desired format (ZIP, 7Z, TAR, WIM, etc).</li>
    <li>Configure the compression method if necessary.</li>
    <li>Click the button to start and add it to the process queue.</li>
</ul>

<h3>2. Extracting</h3>
<p>To extract files:</p>
<ul>
    <li>Select the compressed file you wish to extract.</li>
    <li>Choose the destination directory.</li>
    <li>Start the extraction process.</li>
</ul>

<h3>3. Integrity Check</h3>
<p>To ensure a file is not corrupted:</p>
<ul>
    <li>Select the file and use the integrity check option.</li>
</ul>

<h3>4. Settings and Language</h3>
<p>In the top menu, you can:</p>
<ul>
    <li>Change the language (Portuguese or English) under <b>Configurações &gt; Idiomas</b>.</li>
    <li>Toggle between layouts.</li>
</ul>
"""

class ManualDialog(QDialog):
    def __init__(self, parent=None, idioma="pt_BR"):
        super().__init__(parent)
        try:
            titulo = "Manual do Usuário - COMPRESSION MANAGER" if idioma == "pt_BR" else "User Manual - COMPRESSION MANAGER"
            self.setWindowTitle(titulo)
            self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
            self.setModal(False)
            
            layout = QVBoxLayout(self)
            
            self.browser = QTextBrowser()
            self.browser.setReadOnly(True)
            self.browser.setOpenExternalLinks(True)
            self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
            # Carregar texto correto
            if idioma == "en_US":
                self.browser.setHtml(MANUAL_TEXT_EN_US)
            else:
                self.browser.setHtml(MANUAL_TEXT_PT_BR)
                
            layout.addWidget(self.browser)
            
            # Botão OK
            button_layout = QHBoxLayout()
            ok_text = "OK" if idioma == "pt_BR" else "OK"
            self.ok_button = QPushButton(ok_text)
            self.ok_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            self.ok_button.clicked.connect(self.accept)
            
            button_layout.addStretch(1)
            button_layout.addWidget(self.ok_button)
            layout.addLayout(button_layout)
            
            self.setMinimumSize(600, 400)
            self.resize(700, 500)
            
        except Exception as e:
            logger.error(f"Erro ao criar dialog do Manual: {e}", exc_info=True)

def exibir_manual(app):
    try:
        # Pega o idioma do gerenciador, se existir
        idioma = "pt_BR"
        if hasattr(app, "gerenciador_traducao"):
            idioma = app.gerenciador_traducao.obter_idioma_atual()
            
        dialog = ManualDialog(app, idioma=idioma)
        dialog.show()
    except Exception as e:
        logger.error(f"Erro ao exibir manual: {e}", exc_info=True)
