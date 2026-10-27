import time


class RichBIOS:
    def __init__(self, window):
        self.window = window

    def executar_post(self):
        prints = [
            ("RICHTERM TECHNOLOGIES - BIOS V0.4", 1),
            ("CHECKING PROCESSOR... RT4 OK", 1),
            ("INITIALIZING 16 NIBBLES RAM...", 1),
            ("BOOT SUCCESSFUL. LAUNCHING KERNEL...", 2),
        ]

        y_atual = 20
        for texto, cor in prints:
            self.window.limpar_tela()
            for i, (txt, c) in enumerate(prints[: prints.index((texto, cor)) + 1]):
                self.window.draw_text(txt, 20, 20 + (i * 12), color_idx=c)
            self.window.atualizar()
            time.sleep(0.3)

    def carregar_programa(self, cpu, filepath="programa.hex"):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                linhas = [l.strip() for l in f if l.strip() and not l.startswith("$")]

                for idx, linha in enumerate(linhas):
                    if idx >= 16:
                        break
                    valor = int(linha, 16) & 0x0F
                    cpu.write_ram(idx, valor)

            return True
        except FileNotFoundError:
            self.window.draw_text("BIOS ERR: BOOT DEVICE NOT FOUND", 20, 100, color_idx=3)
            self.window.atualizar()
            return False
