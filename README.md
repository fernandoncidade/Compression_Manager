
<p align="center">
  <b>Selecione o idioma / Select language:</b><br>
  <a href="#ptbr">🇧🇷 Português (BR)</a> |
  <a href="#enus">🇺🇸 English (US)</a>
</p>

---

## <a id="ptbr"></a>🇧🇷 Português (BR)

> **Observação:** Este repositório refere-se à versão **v0.0.2.0** do Projeto COMPRESSION MANAGER. Apoie o projeto e adquira a versão paga através do link: [Instalar via Microsoft Store](https://apps.microsoft.com/detail/9PJMT90R953K)

<details>
<summary>Clique para expandir o README em português</summary>

# COMPRESSION MANAGER

Versão: v0.0.2.0  
Autor: Fernando Nillsson Cidade

COMPRESSION MANAGER é um utilitário gráfico leve para Windows projetado para empacotamento, extração e verificação de integridade de arquivos e pastas. Oferece suporte a múltiplos formatos (ZIP, 7Z, TAR, WIM e outros reconhecidos pelo 7‑Zip), seleção de vários diretórios de saída, métodos de compressão configuráveis, fila de processos e operação via arrastar-e-soltar. A interface é multilíngue (pt_BR / en_US) e preparada para empacotamento como executável (distribuição sem necessidade de instalação manual de dependências Python).

## Funcionalidades principais:
- Compressão de pastas e arquivos nos formatos .zip, .7z, .tar e .wim.
- Extração de arquivos compactados em diversos formatos suportados pelo 7‑Zip (.rar, .zip, .7z, .tar, .wim, .bz2, .tar.xz, .tgz, .tar.gz, .zipx, .lzh, .iso etc.).
- Seleção e manutenção de múltiplos diretórios de saída por formato.
- Arrastar e soltar (drag & drop) para adicionar arquivos e pastas às listas de entrada e saída.
- Métodos de compressão configuráveis por formato (níveis 0–9 onde aplicável) e persistência das preferências.
- Modo "Armazenar como" para criar pacotes com ajustes específicos sem alterar as configurações padrões.
- Atualização de arquivos existentes (opção de atualizar arquivos compactados em vez de recriá‑los).
- Teste de integridade de arquivos compactados (comando "t" do 7‑Zip) para validar pacotes.
- Fila de compressão: novos pedidos podem aguardar enquanto outra tarefa do mesmo formato é executada.
- Mensagens e diálogos traduzíveis; troca de idioma em tempo de execução.
- Janela "Sobre" que exibe texto de descrição, histórico, licenças, avisos e política de privacidade carregados a partir dos recursos incluídos.
- Operação offline: todos os dados são locais (arquivos de configuração e preferências armazenados no diretório persistente do usuário).

## Arquitetura e integração:
- Base GUI: PySide6 (Qt) com widgets personalizados para facilitar seleção múltipla e arrastar-e-soltar.
- Motor de compressão/extração: 7‑Zip (7zG.exe). O aplicativo procura por um executável 7‑Zip incluído junto ao aplicativo (diretório "7-Zip") ou nos caminhos padrão do sistema (Program Files). Se o 7‑Zip não for encontrado, operações de compressão/extracção não funcionarão e o usuário será avisado.
- Threads: operações de compressão, extração e verificação são executadas em threads para manter a interface responsiva.
- Persistência: preferências de compressão e idioma são salvas em arquivos JSON no diretório persistente do usuário (obter_caminho_persistente).

## Instalação e distribuição:
- Projetado para ser empacotado como executável para Windows, incluindo recursos e traduções.
- Quando distribuído como instalador/executável, o usuário final não precisa instalar dependências Python.
- Diálogos de Abrir/Salvar usam as interfaces nativas do sistema quando possível.

## Privacidade e armazenamento de dados:
- Configurações e preferências (por exemplo, config.json, language.json) são salvos localmente no caminho persistente do usuário (por exemplo, AppData).
- Nenhum dado é enviado automaticamente para servidores externos pelo aplicativo.
- Arquivos exportados (compactos, relatórios, etc.) são gravados no local escolhido pelo usuário.

## Como usar (resumo rápido):
1. Adicione pastas/arquivos arrastando-os para a lista de entrada ou usando "Adicionar Pastas" / "Adicionar Arquivos".
2. Especifique diretórios de saída para cada formato (botões "Especificar Saída" para .ZIP, .7Z, .TAR, .WIM e Extração).
3. Selecione o método de compressão em Configurações → Selecionar Método de Compressão.
4. Use "Armazenar" para iniciar a compressão no formato desejado.
5. Marque múltiplas opções de formatos para exibir/ocultar layouts relacionados.
6. Para testar integridade de arquivos compactados, selecione-os e execute "Testar Integridade".
7. Para extrair, selecione arquivos compactados na lista de entrada e escolha um diretório de destino.

## Soluções de problemas comuns:
- 7‑Zip não encontrado: verifique se o 7zG.exe está instalado no sistema ou disponível dentro da pasta "7-Zip" do aplicativo. Mensagens de erro instrutivas serão exibidas.
- Erro ao gravar configurações: confirme permissões de escrita na pasta de usuário (AppData).
- Arquivos não extraem corretamente: verifique se o formato é suportado e se o 7‑Zip está funcional.
- Alto uso da CPU durante compressão: compressão em níveis altos (8–9) é intensiva; reduza o nível ou execute em momento apropriado.

## Limitações conhecidas:
- Suporte de formatos e comportamento dependem do executável 7‑Zip presente no sistema.
- Integração com PDFs/XLSX para importação/exportação (caso presente) requer conformidade de formato — use arquivos gerados por este aplicativo ou compatíveis.

## Licença:
- Componentes de terceiros seguem suas respectivas licenças; informações completas sobre licenças e avisos inclusos estão disponíveis na janela "Sobre" e nos arquivos de licença distribuídos com o instalador.

## Contato e suporte:
- Autor: Fernando Nillsson Cidade
- Para sugestões, relatos de bugs e contribuições, consulte os canais indicados no instalador ou documentação anexa.

## Notas finais:
Este documento descreve o conteúdo do diálogo "Sobre" e o comportamento do aplicativo quando distribuído como executável para Windows. Usuários avançados interessados em integração, automação ou local de armazenamento dos arquivos de configuração devem consultar a documentação técnica incluída no pacote ou o código-fonte para detalhes adicionais.

---

### INFORMAÇÕES ADICIONAIS SOBRE LICENÇAS:

  7-Zip
  ~~~~~
  License for use and distribution
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  7-Zip Copyright (C) 1999-2025 Igor Pavlov.

  The licenses for files are:

    - 7z.dll:
         - The "GNU LGPL" as main license for most of the code
         - The "GNU LGPL" with "unRAR license restriction" for some code
         - The "BSD 3-clause License" for some code
         - The "BSD 2-clause License" for some code
    - All other files: the "GNU LGPL".

  Redistributions in binary form must reproduce related license information from this file.

  Note:
    You can use 7-Zip on any computer, including a computer in a commercial
    organization. You don't need to register or pay for 7-Zip.


GNU LGPL information
--------------------

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You can receive a copy of the GNU Lesser General Public License from
    http://www.gnu.org/




BSD 3-clause License in 7-Zip code
----------------------------------

  The "BSD 3-clause License" is used for the following code in 7z.dll
    1) LZFSE data decompression.
       That code was derived from the code in the "LZFSE compression library" developed by Apple Inc,
       that also uses the "BSD 3-clause License".
    2) ZSTD data decompression.
       that code was developed using original zstd decoder code as reference code.
       The original zstd decoder code was developed by Facebook Inc,
       that also uses the "BSD 3-clause License".

  Copyright (c) 2015-2016, Apple Inc. All rights reserved.
  Copyright (c) Facebook, Inc. All rights reserved.
  Copyright (c) 2023-2025 Igor Pavlov.

Text of the "BSD 3-clause License"
----------------------------------

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may
   be used to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---




BSD 2-clause License in 7-Zip code
----------------------------------

  The "BSD 2-clause License" is used for the XXH64 code in 7-Zip.

  XXH64 code in 7-Zip was derived from the original XXH64 code developed by Yann Collet.

  Copyright (c) 2012-2021 Yann Collet.
  Copyright (c) 2023-2025 Igor Pavlov.

Text of the "BSD 2-clause License"
----------------------------------

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---




unRAR license restriction
-------------------------

The decompression engine for RAR archives was developed using source
code of unRAR program.
All copyrights to original unRAR code are owned by Alexander Roshal.

The license for original unRAR code has the following restriction:

  The unRAR sources cannot be used to re-create the RAR compression algorithm,
  which is proprietary. Distribution of modified unRAR sources in separate form
  or as a part of other software is permitted, provided that it is clearly
  stated in the documentation and source comments that the code may
  not be used to develop a RAR (WinRAR) compatible archiver.

---

</details>

## <a id="enus"></a>🇺🇸 English (US)

> **Note:** This repository refers to the **v0.0.2.0** version of the COMPRESSION MANAGER Project. Support the project and purchase the paid version through the link: [Instalar via Microsoft Store](https://apps.microsoft.com/detail/9PJMT90R953K)

<details>
<summary>Click to expand the README in English</summary>

# COMPRESSION MANAGER

Version: v0.0.2.0  
Author: Fernando Nillsson Cidade

Compression Manager is a lightweight graphical utility for Windows designed for packing, extracting and integrity testing of files and folders. It supports multiple formats (ZIP, 7Z, TAR, WIM and other formats recognized by 7‑Zip), multiple output directories per format, configurable compression methods, a job queue and drag-and-drop operation. The interface is multilingual (pt_BR / en_US) and prepared for packaging as an executable (no manual Python dependency installation required for end users).

## Main features:
- Compress folders and files into .zip, .7z, .tar and .wim formats.
- Extract archives in many formats supported by 7‑Zip (.rar, .zip, .7z, .tar, .wim, .bz2, .tar.xz, .tgz, .tar.gz, .zipx, .lzh, .iso etc.).
- Maintain multiple output directories per format.
- Drag & drop to add files and folders to input/output lists.
- Configurable compression methods per format (levels 0–9 where applicable) and persistence of preferences.
- "Save as" mode to create packages with specific settings without changing global preferences.
- Update existing archives (option to update instead of recreating).
- Archive integrity test (7‑Zip "t" command) to validate packages.
- Job queue: new requests can wait while another task of the same format is running.
- Translatable messages and dialogs; runtime language switching.
- "About" window that loads description, history, licenses, notices and privacy policy from bundled resources.
- Offline operation: all data is local (config and preferences files stored in the user's persistent directory).

## Architecture and integration:
- GUI base: PySide6 (Qt) with custom widgets for multi-selection and drag-and-drop.
- Compression/extraction engine: 7‑Zip (7zG.exe). The app looks for a bundled 7‑Zip executable ("7-Zip" folder) or system locations (Program Files). If 7‑Zip isn't found, compression/extraction operations won't work and the user will be notified.
- Threads: compress, extract and test operations run in threads to keep the UI responsive.
- Persistence: compression methods and language preferences are saved in JSON files in the user's persistent directory (obter_caminho_persistente).

## Installation and distribution:
- Designed to be packaged as a Windows executable including resources and translations.
- When distributed as an installer/executable the end user does NOT need to install Python.
- Open/Save dialogs use native system dialogs when possible.

## Privacy and storage:
- Settings and preferences (e.g. config.json, language.json) are saved locally in the user's persistent path (e.g. %APPDATA% on Windows).
- No user data is sent automatically to external servers by the app.
- Exported files (archives, reports, etc.) are written to the location chosen by the user.

## How to use (quick summary):
1. Add folders/files by dragging them into the input list or using "Add Folders" / "Add Files".
2. Specify output directories per format ("Specify Output" buttons for .ZIP, .7Z, .TAR, .WIM and Extraction).
3. Choose compression method in Settings → Select Compression Method.
4. Use "Store" to start compression in the desired format.
5. Check multiple format options to show/hide related layouts.
6. To test archive integrity, select them and run "Test Integrity".
7. To extract, select archive files in the input list and choose a destination directory.

## Common troubleshooting:
- 7‑Zip not found: verify 7zG.exe is installed or available inside the app's "7-Zip" folder. User-friendly error messages will be shown.
- Error writing settings: ensure write permissions for the user's folder (AppData).
- Archives not extracting correctly: verify the format is supported and 7‑Zip works.
- High CPU during compression: high compression levels (8–9) are CPU intensive; lower the level or run at a convenient time.

## Known limitations:
- Supported formats and behaviour depend on the 7‑Zip executable present on the system.
- Integration with PDFs/XLSX for import/export (if present) requires format compliance — use files produced by this app or compatible ones.

## License:
- Third-party components follow their respective licenses; full license and notices are available in the About window and license files bundled with the installer.

## Contact and support:
- Author: Fernando Nillsson Cidade
- For suggestions, bug reports and contributions, check the channels indicated in the installer or attached documentation.

## Final notes:
This document describes the About dialog content and the app behaviour when distributed as a Windows executable. Advanced users interested in integration, automation or configuration storage locations should consult the included technical documentation or the source code for details.

---

### Additional information about licenses:

  7-Zip
  ~~~~~
  License for use and distribution
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  7-Zip Copyright (C) 1999-2025 Igor Pavlov.

  The licenses for files are:

    - 7z.dll:
         - The "GNU LGPL" as main license for most of the code
         - The "GNU LGPL" with "unRAR license restriction" for some code
         - The "BSD 3-clause License" for some code
         - The "BSD 2-clause License" for some code
    - All other files: the "GNU LGPL".

  Redistributions in binary form must reproduce related license information from this file.

  Note:
    You can use 7-Zip on any computer, including a computer in a commercial
    organization. You don't need to register or pay for 7-Zip.


GNU LGPL information
--------------------

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You can receive a copy of the GNU Lesser General Public License from
    http://www.gnu.org/




BSD 3-clause License in 7-Zip code
----------------------------------

  The "BSD 3-clause License" is used for the following code in 7z.dll
    1) LZFSE data decompression.
       That code was derived from the code in the "LZFSE compression library" developed by Apple Inc,
       that also uses the "BSD 3-clause License".
    2) ZSTD data decompression.
       that code was developed using original zstd decoder code as reference code.
       The original zstd decoder code was developed by Facebook Inc,
       that also uses the "BSD 3-clause License".

  Copyright (c) 2015-2016, Apple Inc. All rights reserved.
  Copyright (c) Facebook, Inc. All rights reserved.
  Copyright (c) 2023-2025 Igor Pavlov.

Text of the "BSD 3-clause License"
----------------------------------

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may
   be used to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---




BSD 2-clause License in 7-Zip code
----------------------------------

  The "BSD 2-clause License" is used for the XXH64 code in 7-Zip.

  XXH64 code in 7-Zip was derived from the original XXH64 code developed by Yann Collet.

  Copyright (c) 2012-2021 Yann Collet.
  Copyright (c) 2023-2025 Igor Pavlov.

Text of the "BSD 2-clause License"
----------------------------------

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---




unRAR license restriction
-------------------------

The decompression engine for RAR archives was developed using source
code of unRAR program.
All copyrights to original unRAR code are owned by Alexander Roshal.

The license for original unRAR code has the following restriction:

  The unRAR sources cannot be used to re-create the RAR compression algorithm,
  which is proprietary. Distribution of modified unRAR sources in separate form
  or as a part of other software is permitted, provided that it is clearly
  stated in the documentation and source comments that the code may
  not be used to develop a RAR (WinRAR) compatible archiver.

---

</details>
