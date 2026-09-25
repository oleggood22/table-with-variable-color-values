"""Black -> transparent gradients, 16:9 (3840x2160 PNG + SVG), in presentation/brand/gradient/.
Black is the SONU Black 419C (#232323). Linear, from full black on one edge to fully transparent on the opposite one."""
import os

import numpy as np
from PIL import Image

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "brand", "gradient"))
W, H = 3840, 2160
BLACK = (0x23, 0x23, 0x23)
# name -> (black edge, svg x1 y1 x2 y2 from black to transparent)
SIDES = {"bottom": (0, 1, 0, 0), "top": (0, 0, 0, 1), "left": (0, 0, 1, 0), "right": (1, 0, 0, 0)}


def main():
    os.makedirs(OUT, exist_ok=True)
    rng = np.random.default_rng(0)
    for side, (x1, y1, x2, y2) in SIDES.items():
        if side in ("bottom", "top"):
            t = np.linspace(0, 1, H)[:, None].repeat(W, 1)
        else:
            t = np.linspace(0, 1, W)[None, :].repeat(H, 0)
        if side in ("top", "left"):
            t = 1 - t
        alpha = t * 255 + rng.uniform(-0.5, 0.5, t.shape)  # light dither against banding
        a = np.clip(np.round(alpha), 0, 255).astype(np.uint8)
        rgba = np.dstack([np.full((H, W), c, np.uint8) for c in BLACK] + [a])
        name = f"sonu-gradient-black-{side}"
        Image.fromarray(rgba, "RGBA").save(os.path.join(OUT, name + ".png"), optimize=True)
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf8") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">'
                    f'<defs><linearGradient id="g" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
                    f'<stop offset="0" stop-color="#232323" stop-opacity="1"/>'
                    f'<stop offset="1" stop-color="#232323" stop-opacity="0"/></linearGradient></defs>'
                    f'<rect width="1920" height="1080" fill="url(#g)"/></svg>')
        print(name, round(os.path.getsize(os.path.join(OUT, name + ".png")) / 1e6, 2), "MB")


if __name__ == "__main__":
    main()
