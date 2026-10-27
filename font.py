import pygame

font_data = {}
font_cache = {}


def load_font(filepath="P16.txt"):
    global font_data
    with open(filepath, encoding="utf-8") as archive:
        for line in archive:
            line = line.strip()
            if line:
                parts = [x.strip() for x in line.split(",") if x.strip()]
                if parts:
                    n = [int(x, 16) for x in parts]
                    font_data[n[0]] = n[1:]


def generate_font_cache(paleta):
    global font_cache
    for color_idx, rgb in enumerate(paleta):
        font_cache[color_idx] = {}
        for char_code, rows in font_data.items():
            surf = pygame.Surface((8, 8), pygame.SRCALPHA)
            for r, row in enumerate(rows):
                for c in range(8):
                    if (row >> (7 - c)) & 1:
                        surf.set_at((c, r), rgb)
            font_cache[color_idx][char_code] = surf


def put_char(surf, ch, x, y, color_idx):
    color_dict = font_cache.get(color_idx, font_cache)
    char_surf = color_dict.get(ord(ch), color_dict.get(ord("?")))
    if char_surf:
        surf.blit(char_surf, (x, y))


def put_text(surf, text, x, y, color_idx=1, espacamento=7):
    x_atual = x
    for ch in text:
        put_char(surf, ch, x_atual, y, color_idx)
        x_atual += espacamento


def put_text_centered(surf, text, y, largura_tela, color_idx=1, espacamento=7):
    largura_texto = (len(text) * espacamento) - (espacamento - 8)
    x_centralizado = largura_tela - largura_texto
    put_text(surf, text, x_centralizado, y, color_idx, espacamento)
