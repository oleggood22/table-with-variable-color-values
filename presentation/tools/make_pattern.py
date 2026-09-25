"""SONU brand pattern (identity guide, pattern 3.2): tilted rows of the wordmark
with the sign between them. Marks at 10 % opacity.

Output: presentation/brand/pattern/  (SVG + PNG, dark / light / transparent overlays)
"""
import math
import os
import re

import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.abspath(os.path.join(HERE, "..", "brand"))
OUT = os.path.join(BRAND, "pattern")

OPACITY = 0.10
TILT = -19          # degrees, each mark
WORD_W = 290        # wordmark width at 1920 px wide canvas
STEP_A = (270, 34)  # next wordmark along a row
STEP_B = (-10, 270) # next row
BLACK, WHITE = "#232323", "#FFFFFF"


def glyph(path):
    """Inner <g> of a potrace SVG plus its viewBox size (content has 80-unit padding)."""
    svg = open(path, encoding="utf8").read()
    vw, vh = map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
    g = re.search(r"(<g transform=.*?</g>)", svg, re.S).group(1)
    g = re.sub(r'fill="#[0-9A-Fa-f]{6}"', "", g)
    return g, vw, vh


def pattern_svg(w, h, mark_color, bg=None):
    word, ww, wh = glyph(os.path.join(BRAND, "sonu-wordmark-white.svg"))
    sign, sw, sh = glyph(os.path.join(BRAND, "sonu-sign-white.svg"))
    k = w / 1920
    s = WORD_W * k / (ww - 160)          # both marks share one scale, as in the guide
    ax, ay = STEP_A[0] * k, STEP_A[1] * k
    bx, by = STEP_B[0] * k, STEP_B[1] * k
    uses = []
    n = int(max(w, h) / min(ax, by)) + 4
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            for ref, off, vw_, vh_ in (("w", 0.0, ww, wh), ("s", 0.5, sw, sh)):
                cx = i * ax + (j + off) * bx
                cy = i * ay + (j + off) * by
                if -300 * k < cx < w + 300 * k and -300 * k < cy < h + 300 * k:
                    uses.append(
                        f'<use href="#{ref}" xlink:href="#{ref}" transform="translate({cx:.1f} {cy:.1f}) '
                        f'rotate({TILT}) scale({s:.5f}) translate({-vw_ / 2:.1f} {-vh_ / 2:.1f})"/>')
    bg_rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs><g id="w">{word}</g><g id="s">{sign}</g></defs>{bg_rect}'
            f'<g fill="{mark_color}" fill-opacity="{OPACITY}">{"".join(uses)}</g></svg>')


def main():
    os.makedirs(OUT, exist_ok=True)
    variants = {
        "sonu-pattern-dark": (WHITE, BLACK),          # white marks on Black 419C
        "sonu-pattern-light": (BLACK, WHITE),         # black marks on white
        "sonu-pattern-white-overlay": (WHITE, None),  # transparent, to lay over photos / colour
        "sonu-pattern-black-overlay": (BLACK, None),
    }
    for name, (mark, bg) in variants.items():
        svg = pattern_svg(1920, 1080, mark, bg)
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf8") as f:
            f.write(svg)
        cairosvg.svg2png(bytestring=pattern_svg(3840, 2160, mark, bg).encode(),
                         write_to=os.path.join(OUT, name + ".png"))
        print(name)


if __name__ == "__main__":
    main()
