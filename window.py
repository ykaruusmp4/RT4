import sys

import pygame

import font

PALETA = [(10, 16, 12), (57, 255, 20), (0, 229, 255), (255, 46, 99)]


class RichWindow:
    def __init__(self, largura=640, altura=480, titulo="RT4 - 4-Bit Processor"):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(titulo)

        font.load_font("P16.txt")
        font.generate_font_cache(PALETA)

    def limpar_tela(self):
        self.tela.fill(PALETA[0])

    def draw_text(self, texto, x, y, color_idx=1, espacamento=7):
        font.put_text(self.tela, texto, x, y, color_idx, espacamento)

    def draw_text_centered(self, texto, y, color_idx=1, espacamento=7):
        font.put_text_centered(self.tela, texto, y, self.largura, color_idx, espacamento)

    def atualizar(self):
        pygame.display.flip()

    def verificar_fechar(self, evento):
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
