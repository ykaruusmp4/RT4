import pygame

from bios import RichBIOS
from cpu import RichCPU
from window import RichWindow


def main():
    janela = RichWindow(largura=400, altura=300, titulo="RT4")
    bios = RichBIOS(janela)
    cpu = RichCPU()

    bios.executar_post()

    if not bios.carregar_programa(cpu, "programa.hex"):
        pygame.time.wait(3000)
        return

    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            janela.verificar_fechar(evento)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    cpu.ciclo_clock() if hasattr(cpu, "ciclo_clock") else cpu.ciclo_clock
        janela.limpar_tela()
        janela.draw_text_centered("--- RT4 CONSOLE ---", 10, color_idx=2)

        status = cpu.obter_status_str()
        janela.draw_text(status["A"], 20, 40, color_idx=1)
        janela.draw_text(status["B"], 20, 55, color_idx=1)
        janela.draw_text(status["PC"], 20, 70, color_idx=2)
        janela.draw_text(status["FLAGS"], 20, 85, color_idx=3)

        janela.draw_text("RAM MAP:", 240, 40, color_idx=2)
        for idx in range(16):
            valor_ram = cpu.ram[idx]
            x_col = 240 + (50 * (idx // 8))
            y_row = 60 + (15 * (idx % 8))

            cor_linha = 2 if cpu.pc == idx else 1
            janela.draw_text(f"[{idx:X}]: {valor_ram:X}", x_col, y_row, color_idx=cor_linha)

            janela.draw_text_centered("[ ESPACO ] PARA PULSAR O CLOCK", 270, color_idx=1)

            janela.atualizar()
            clock.tick(60)


if __name__ == "__main__":
    main()
