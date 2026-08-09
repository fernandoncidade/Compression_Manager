import os
import subprocess

def _encontrar_lrelease():
    try:
        import PySide6
        pyside6_dir = os.path.dirname(PySide6.__file__)
        lrelease_path = os.path.join(pyside6_dir, "lrelease.exe")
        if os.path.isfile(lrelease_path):
            return lrelease_path

    except ImportError:
        pass

    return "pyside6-lrelease"

def compilar_traducoes():
    diretorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    diretorio_traducoes = os.path.join(diretorio_base, "language", "translations")
    lrelease = _encontrar_lrelease()

    for arquivo in os.listdir(diretorio_traducoes):
        if arquivo.endswith('.ts'):
            arquivo_ts = os.path.join(diretorio_traducoes, arquivo)
            arquivo_qm = os.path.join(diretorio_traducoes, arquivo.replace('.ts', '.qm'))

            print(f"Compilando: {arquivo}")
            try:
                resultado = subprocess.run(
                    [lrelease, arquivo_ts, "-qm", arquivo_qm],
                    check=True, 
                    capture_output=True, 
                    text=True
                )
                print(f"Sucesso: {resultado.stdout}")

            except subprocess.CalledProcessError as e:
                print(f"Erro ao compilar {arquivo}: {e}")
                print(f"Saída: {e.output}")

if __name__ == "__main__":
    compilar_traducoes()

