"""Prepare deck assets from the Notion export in the repo root.

Crops letterboxes / logos out of the reference GIFs, optimises them with
gifsicle, and converts stills (jpg/png/avif) to web-sized JPEGs.
Output: presentation/assets/
"""
import os
import subprocess
import sys

import imageio_ffmpeg
from PIL import Image

try:
    import pillow_avif  # noqa: F401  (registers the AVIF decoder)
except ImportError:
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "presentation", "assets")
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

# name -> (source file, crop box (x, y, w, h) or None)
GIFS = {
    "vision-flash-car": ("Timeline_2.gif", (0, 105, 720, 270)),
    "vision-motion-gym": ("Timeline_2_00000200.gif", None),
    "vision-gymnast": ("SaveClip.App_AQMJStbn2rIhoqLurfr0Ut4RygAnsBtWms36waK8uz9EEd4VbALzh8i-TmA9fNKjtnpdhdW60LzeBIOEowBKnkphmTN_Sry70inVi0Y00000000.gif", None),
    "intro-tennis-city": ("SaveClip.App_AQPYu1zpKrJe5AKwUILHQ9mgylKLyjB3wKeqZick4ARlBhkYriVaQ8_DM6AwBOc-QIoXsmlh1TmJFY6peoe2D0sbbuVxmdXxFMRCM9Y00000032.gif", None),
    "run-details": ("SaveClip.App_AQM-FKmBwMcI7iW6B9xfZhApvsSq4bWrBqjoq7Bhj1adlcSkoXb9be4Y2C1PIifp_FLZJb2tWr2VwXX6p-emF4BAvEhuELNZmwDQFtA00000000.gif", None),
    # point-cloud reference: keep only the band above the partner logo
    "run-lidar": ("Compound_Clip_1_00000000.gif", (0, 0, 720, 204)),
    "padel-racket-portrait": ("SaveClip.App_AQPYu1zpKrJe5AKwUILHQ9mgylKLyjB3wKeqZick4ARlBhkYriVaQ8_DM6AwBOc-QIoXsmlh1TmJFY6peoe2D0sbbuVxmdXxFMRCM9Y00000178.gif", None),
    "padel-macro": ("SaveClip.App_AQPYu1zpKrJe5AKwUILHQ9mgylKLyjB3wKeqZick4ARlBhkYriVaQ8_DM6AwBOc-QIoXsmlh1TmJFY6peoe2D0sbbuVxmdXxFMRCM9Y00000761.gif", (4, 0, 716, 480)),
    "sw-storm": ("SaveClip.App_AQPJ7Je4FqQmCg6-v2UvpuwR5AMCKZw8WM1VWei4iH4nI_GQ6eSNOo3nSOiPPdBy-KIpndeX5WXwYCouFXlP2ZTm.gif", None),
    "sw-water-macro": ("SaveClip.App_AQPJ7Je4FqQmCg6-v2UvpuwR5AMCKZw8WM1VWei4iH4nI_GQ6eSNOo3nSOiPPdBy-KIpndeX5WXwYCouFXlP2ZTm00000023.gif", None),
    "fit-studio": ("SaveClip.App_AQMEgJuIye7B82qfNAcb2vBeVg0cfVKiAP_YbIUUW1AkgMhcAxYQT_t2IyBu_ZmArWtzGHqHG0vaJiH9ga_bEIIh8ZCqqK7iZvY48eI00000169.gif", None),
    "fit-roboarm": ("Timeline_2_00000220.gif", None),
    "fit-platform-top": ("Timeline_2_00000025.gif", None),
    "fit-details": ("SaveClip.App_AQMEgJuIye7B82qfNAcb2vBeVg0cfVKiAP_YbIUUW1AkgMhcAxYQT_t2IyBu_ZmArWtzGHqHG0vaJiH9ga_bEIIh8ZCqqK7iZvY48eI00000229.gif", None),
    "loc-floodlights": ("SaveClip.App_AQObklY8OU3CheiHHVF3s_qYcUJBCnZ3YkvMZ_Ybba6X67agFVtqfUEVjEMANWTG2HiFbxg__k1lD_6MZpRhzJzoMe09ESeB5IkGSfE00000000.gif", None),
}

# name -> (source file, crop box or None)
STILLS = {
    "cover-laugh": ("SaveClip.App_550064447_18368452846194945_3346294024597490047_n.jpg", None),
    "run-track-standing": ("SaveClip.App_670860325_17891182101452261_1704218474416157075_n.jpg", None),
    "run-aerial": ("image.png", None),
    "approach-look-up": ("image 1.png", None),
    "run-topdown": ("SaveClip.App_650135582_18313184578287356_3012343236521660558_n.jpg", None),
    "padel-clay-serve": ("6df31657-ed1d-4ec8-a25c-465d7be5f9f5_sm.avif", None),
    "padel-lines": ("587c6d62-806a-4414-ad43-43d167852515_sm.avif", None),
    "padel-court-top": ("3bb2def1-0357-44a1-873d-04cf032f0fe3_sm.avif", None),
    "padel-night-jump": ("25f8e9e1-5ccb-4858-9cfb-fd223ccb2435_sm.avif", None),
    "sw-rock-water": ("Still_2026-09-25_100146_1.24.1.png", (208, 0, 304, 460)),
    "fit-room-cg": ("image 2.png", None),
    "fit-platform-seated": ("SaveClip.App_708088298_18083341343426927_5695181273401033961_n.jpg", None),
    "loc-cska": ("image 3.png", None),
    "lib-legs-track": ("SaveClip.App_813804580_18630967003027399_8320781145748091962_n.jpg", None),
    "lib-runners-shadows": ("SaveClip.App_809615892_18630966910027399_6445407313194522199_n.jpg", None),
    "lib-track-overhead": ("SaveClip.App_813987101_18630967036027399_2167070489183120441_n.jpg", None),
    "lib-metronomes": ("SaveClip.App_813841800_18630966934027399_8016775618354045742_n.jpg", None),
    "lib-dunes": ("455e4759-4006-4bd2-b183-4f8e860edc9f_sm.avif", None),
    "lib-jump-sky": ("SaveClip.App_671243747_17891182128452261_226771427028069025_n.jpg", None),
    "lib-light-track": ("SaveClip.App_708102697_18578048716038202_8006964236910031512_n.jpg", (3, 0, 1263, 765)),
    "lib-athlete-bw": ("SaveClip.App_689039630_18590273671057539_988142558543941887_n.jpg", (0, 149, 2305, 3947)),
}

MAX_SIDE = 2400


def gif(name, src, crop):
    dst = os.path.join(OUT, name + ".gif")
    tmp = dst + ".tmp.gif"
    if crop:
        x, y, w, h = crop
        vf = f"crop={w}:{h}:{x}:{y},split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a"
        subprocess.run([FFMPEG, "-v", "error", "-y", "-i", os.path.join(ROOT, src), "-vf", vf, "-loop", "0", tmp], check=True)
        src_path = tmp
    else:
        src_path = os.path.join(ROOT, src)
    subprocess.run(["gifsicle", "-O3", "--lossy=35", "--no-warnings", src_path, "-o", dst], check=True)
    if os.path.exists(tmp):
        os.remove(tmp)
    return dst


def still(name, src, crop):
    dst = os.path.join(OUT, name + ".jpg")
    im = Image.open(os.path.join(ROOT, src)).convert("RGB")
    if crop:
        x, y, w, h = crop
        im = im.crop((x, y, x + w, y + h))
    if max(im.size) > MAX_SIDE:
        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    im.save(dst, quality=86, optimize=True, progressive=True)
    return dst


def main():
    os.makedirs(OUT, exist_ok=True)
    only = set(sys.argv[1:])
    for name, (src, crop) in GIFS.items():
        if not only or name in only:
            p = gif(name, src, crop)
            print(f"{os.path.getsize(p) / 1e6:6.2f} MB  {name}.gif")
    for name, (src, crop) in STILLS.items():
        if not only or name in only:
            p = still(name, src, crop)
            print(f"{os.path.getsize(p) / 1e6:6.2f} MB  {name}.jpg")


if __name__ == "__main__":
    main()
