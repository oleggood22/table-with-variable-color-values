"""Print the HTML copy to presentation/SONU_SS27_DirNote.pdf (one 1920x1080 page per slide).

Animated GIFs are swapped for a representative still frame so the PDF shows
a clean picture instead of whatever frame happened to be on screen.
"""
import asyncio
import os
import re
import tempfile

from PIL import Image
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.abspath(os.path.join(HERE, ".."))
HTML = os.path.join(PRES, "SONU_SS27_DirNote.html")
OUT = os.path.join(PRES, "SONU_SS27_DirNote.pdf")
CHROMIUM = "/opt/pw-browsers/chromium"

# frame position (0..1) per GIF; default is the middle of the clip
FRAME_AT = {
    "fit-details.gif": 0.95,       # skip the frame with a third-party label
    "loc-floodlights.gif": 0.97,   # floodlights fully on
    "fit-platform-top.gif": 0.6,   # after the fade-in
}


def still(gif_path, out_dir):
    name = os.path.basename(gif_path)
    im = Image.open(gif_path)
    n = getattr(im, "n_frames", 1)
    im.seek(min(n - 1, int(n * FRAME_AT.get(name, 0.5))))
    dst = os.path.join(out_dir, name.replace(".gif", ".png"))
    im.convert("RGB").save(dst)
    return dst


async def main():
    with open(HTML, encoding="utf8") as f:
        page_html = f.read()
    with tempfile.TemporaryDirectory() as tmp:
        def swap(m):
            src = m.group(1)
            return f'src="file://{still(os.path.join(PRES, src), tmp)}"'
        page_html = re.sub(r'src="(assets/[^"]+\.gif)"', swap, page_html)
        # keep every other relative path working from the temp copy
        page_html = page_html.replace('src="assets/', f'src="file://{PRES}/assets/')
        page_html = page_html.replace('url("fonts/', f'url("file://{PRES}/fonts/')
        tmp_html = os.path.join(tmp, "print.html")
        with open(tmp_html, "w", encoding="utf8") as f:
            f.write(page_html)
        async with async_playwright() as p:
            browser = await p.chromium.launch(executable_path=CHROMIUM)
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            await page.emulate_media(media="print")  # show every slide so all fonts get requested
            await page.goto("file://" + tmp_html)
            await page.evaluate("Promise.all(Array.from(document.fonts).map(f => f.load())).then(() => document.fonts.ready)")
            await page.wait_for_timeout(1000)
            await page.pdf(path=OUT, width="1920px", height="1080px", print_background=True,
                           margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            await browser.close()
    print(OUT, round(os.path.getsize(OUT) / 1e6, 1), "MB")


if __name__ == "__main__":
    asyncio.run(main())
