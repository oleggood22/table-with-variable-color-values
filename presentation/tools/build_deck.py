"""SONU SS27 — Director's Note.

Builds presentation/SONU_SS27_DirNote.pptx and presentation/SONU_SS27_DirNote.html
from the slide descriptions below. Run prepare_assets.py first.
"""
import os

from engine import W, H, Slide, build_html, build_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.abspath(os.path.join(HERE, ".."))
ASSETS = os.path.join(PRES, "assets")

# palette
INK = "#0D0F11"      # dark
PAPER = "#EAE7E1"    # light
SOFT_D = "#A4A9AB"   # secondary text on dark
SOFT_L = "#52575A"   # secondary text on light
CLAY_D = "#D46A3F"   # accent on dark
CLAY_L = "#A2421C"   # accent on light

M = 128  # margin

# type scale
MEGA = dict(font="light", size=220, lh=0.9, ls=-6)
DISPLAY = dict(font="light", size=88, lh=1.06, ls=-2)
TITLE = dict(font="light", size=56, lh=1.14, ls=-1)
SUB = dict(font="light", size=40, lh=1.2, ls=-0.5)
BODY = dict(font="regular", size=30, lh=1.42)
LABEL = dict(font="mono", size=24, lh=1.3, ls=3, upper=True)

BRAND = "SONU"

slides = []


def new(sid, bg, title):
    s = Slide(sid, bg, title)
    slides.append(s)
    return s


def label(s, x, y, w, t, color):
    s.text(x, y, w, 40, t, color=color, **LABEL)


def bottom_scrim(s, top=420, strength=0.82):
    s.grad(0, top, W, H - top, 180, [(0, INK, 0), (0.55, INK, strength * 0.6), (1, INK, strength)])


def opener(s, index, name, subtitle, dark_text=False, title_lines=1):
    """Film / chapter opener: label, mega title bottom-left, subtitle bottom-right."""
    fg = INK if dark_text else PAPER
    th = int(220 * 0.9 * title_lines) + 20
    ty = 952 - th + 24
    label(s, M, ty - 52, 900, index, fg)
    if subtitle:
        s.text(992, ty - 76, 800, 56, subtitle, color=fg, align="r", valign="b", **SUB)
    s.text(M, ty, 1664, th, name, color=fg, valign="b", **MEGA)


# ---------------------------------------------------------------------------
# 01 cover
s = new("cover", INK, "Обложка")
s.img("cover-laugh.jpg", 0, 0, W, H, fx=0.5, fy=0.5, alt="Герой смеётся, бетонная стена")
bottom_scrim(s, top=460, strength=0.85)
label(s, M, 700, 900, f"{BRAND} · Director's note", PAPER)
s.text(M, 740, 1100, 212, "SS27", color=PAPER, valign="b", **MEGA)
s.text(1052, 900, 740, 52, "Running · Padel · Sportswear · Fitness", color=PAPER, align="r", valign="b",
       font="light", size=36, lh=1.2)

# 02 task
s = new("task", PAPER, "Задача")
label(s, M, M, 600, "Задача", CLAY_L)
s.text(M, 176, 1300, 140, "Концепция четырёх роликов для социальных сетей", color=INK, **TITLE)
cols = [("4", "ролика"), ("30″", "секунд каждый"), ("2", "съёмочные смены")]
for i, (n, cap) in enumerate(cols):
    x = M + i * 560
    s.text(x, 356, 520, 210, n, color=INK, font="light", size=210, lh=0.95, ls=-6)
    s.text(x, 576, 520, 50, cap, color=SOFT_L, **BODY)
s.rect(M, 716, 1664, 2, INK, 0.25)
label(s, M, 748, 900, "Версии для экранов", CLAY_L)
s.text(M, 796, 780, 70, "Running + Fitness", color=INK, **TITLE)
s.text(992, 796, 800, 70, "Padel + Sportswear", color=INK, **TITLE)
s.text(M, 884, 1664, 50, "На основе четырёх основных роликов в монтаже собираются версии для экранов и разных форматов.",
       color=SOFT_L, **BODY)

# 03 intro statement
s = new("intro", INK, "Интро")
label(s, M, M, 600, "Интро", CLAY_D)
s.text(M, 470, 1500, 200, "Спорт не всегда начинается с цели.", color=PAPER, **DISPLAY)
s.text(M, 740, 820, 180,
       "Иногда — с желания двигаться и быть частью этой культуры. Для бренда спорт существует не как "
       "испытание на предел, а как ощущение свободы.", color=SOFT_D, **BODY)
s.text(1032, 740, 760, 180,
       f"{BRAND} — проводник в этом пути: технология, комфорт и эстетика, слившись вместе, помогают "
       "получать удовольствие от движения.", color=SOFT_D, **BODY)

# 04 accent statement on dunes
s = new("pleasure", "#5A2A12", "Удовольствие от движения")
s.img("lib-dunes.jpg", 0, 0, W, H, fx=0.5, fy=0.5, alt="Песчаные дюны, тёплый свет")
s.rect(0, 0, W, H, "#1A0C05", 0.28)
s.text(M, 236, 1560, 240, "Мы не снимаем спорт\nкак испытание.", color="#E2BFA8",
       font="light", size=108, lh=1.04, ls=-3)
s.text(M, 500, 1560, 240, "Мы снимаем удовольствие\nот движения.", color=PAPER,
       font="light", size=108, lh=1.04, ls=-3)
s.text(M, 836, 900, 120,
       "…когда находишь свой ритм, а технология просто помогает тебе не отвлекаться от этого.",
       color=PAPER, **BODY)

# 05 what a person feels
s = new("feel", INK, "Что чувствует человек")
s.img("intro-tennis-city.gif", 0, 0, 1060, H, fx=0.5, fy=0.5, alt="Рапид: теннисист в городе")
s.text(1188, M, 604, 100, "В SS27 мы хотим показать не сам спорт, а то, что человек чувствует:",
       color=SOFT_D, **BODY)
s.text(1188, 300, 604, 470,
       ["Импульс", "Концентрация", "Лёгкость", "Энергия", "Контакт с собственным телом"],
       color=PAPER, font="light", size=60, lh=1.12, ls=-1, pgap=6)
s.text(1188, 816, 604, 136,
       "Момент, когда ты находишь свой ритм и просто получаешь удовольствие от того, что делаешь.",
       color=SOFT_D, **BODY)

# 06 approach
s = new("approach", PAPER, "Approach")
s.img("approach-look-up.jpg", 1060, 0, 860, H, fx=0.5, fy=0.5, alt="Герой в разминке смотрит в камеру")
label(s, M, M, 600, "Approach", CLAY_L)
s.text(M, 176, 830, 250,
       "Каждый ролик — небольшая история о движении, человеке и эстетике отдельного вида спорта.",
       color=INK, font="light", size=52, lh=1.14, ls=-1)
principles = [
    "Герои не выглядят профессиональными атлетами из спортивной рекламы. Нет акцента на поте, превозмогании и боли.",
    "Одежда и тело становятся единым целым: движение раскрывает посадку, силуэт и детали вещей.",
    "Визуальный язык обращается к fashion: пластика, «позирование», характер и живость героя.",
]
for i, t in enumerate(principles):
    y = 488 + i * 156
    s.rect(M, y - 20, 830, 1, INK, 0.2)
    s.text(M, y, 70, 40, f"0{i + 1}", color=CLAY_L, **LABEL)
    s.text(208, y, 750, 130, t, color=INK, **BODY)

# 07 vision & tone opener
s = new("vision", INK, "Vision & Tone")
s.img("vision-gymnast.gif", 0, 0, W, H, fx=0.5, fy=0.5, alt="Гимнастка в зале, синий свет")
bottom_scrim(s, top=380, strength=0.8)
opener(s, "Визуальный язык", "VISION\n& TONE", "", title_lines=2)

# 08 camera
s = new("camera", INK, "Камера")
s.img("vision-motion-gym.gif", 0, 0, W, 420, fx=0.5, fy=0.5, alt="Движение камеры в зале, размытие")
label(s, M, 484, 700, "Камера", CLAY_D)
s.text(M, 528, 760, 220, "Камера большую часть времени остаётся наблюдателем.", color=PAPER, **TITLE)
rows = [
    ("Основной инструмент", "Длиннофокусная оптика."),
    ("Отдельные моменты", "Ручная камера и широкоугольные объективы — только в отдельных моментах."),
    ("Системы движения", "Стедикам, кран и роборука дают каждому направлению свой характер движения."),
]
for i, (k, v) in enumerate(rows):
    y = 484 + i * 160
    if i:
        s.rect(1008, y - 22, 784, 1, PAPER, 0.18)
    s.text(1008, y, 784, 40, k, color=CLAY_D, **LABEL)
    s.text(1008, y + 40, 784, 90, v, color=SOFT_D, **BODY)

# 09 rapid & flash
s = new("rapid", INK, "Рапид и вспышки")
s.img("vision-flash-car.gif", 0, 0, W, 700, fx=0.5, fy=0.5, alt="Вспышки света в машине")
label(s, M, 772, 760, "Высокая частота съёмки", CLAY_D)
s.text(M, 816, 760, 136,
       "Рапиды позволяют задержаться на коротких моментах: движение ткани, эмоция, отдельная фаза движения.",
       color=SOFT_D, **BODY)
label(s, 1032, 772, 760, "Вспышки света", CLAY_D)
s.text(1032, 816, 760, 136,
       "Фиксируют отдельные доли секунды и добавляют изображению ощущение фотографии.",
       color=SOFT_D, **BODY)

# 10 tone
s = new("tone", PAPER, "Тон")
s.img("run-track-standing.jpg", 1128, 0, 792, H, fx=0.5, fy=0.4, alt="Бегун стоит на синей дорожке")
label(s, M, M, 600, "Тон", CLAY_L)
s.text(M, 176, 900, 140, "Референс — fashion middle+ сегмента.", color=INK, **TITLE)
s.text(M, 356, 840, 260,
       "Мы позволяем себе низкий ключ и грубые текстуры, но оставляем акцент на героях и одежде. "
       "Тёмную и тяжёлую спортивную эстетику не строим — изображение должно рассказывать ровно противоположное.",
       color=SOFT_L, **BODY)
label(s, M, 676, 400, "Баланс", CLAY_L)
s.text(M, 720, 900, 64, "Натуральность", color=INK, **TITLE)
s.rect(M, 808, 860, 1, INK, 0.3)
s.text(M, 824, 900, 64, "Кинематографичность", color=INK, **TITLE)

# 11 synopsis
s = new("synopsis", PAPER, "Synopsis")
label(s, M, M, 600, "Synopsis", CLAY_L)
s.text(M, 300, 1664, 300, "Sportswear выходит\nза рамки тренировки.", color=INK,
       font="light", size=128, lh=1.02, ls=-4)
s.rect(M, 700, 1664, 1, INK, 0.25)
s.text(M, 740, 760, 180,
       "Спорт становится частью повседневной жизни. В центре остаётся человек — его движение показывает характер одежды.",
       color=SOFT_L, **BODY)
s.text(1032, 740, 760, 180,
       "Sportswear соединяет функциональность, технологичность и fashion. Одежда работает вместе с человеком и остаётся частью его образа.",
       color=SOFT_L, **BODY)

# 12 fabric
s = new("fabric", INK, "Ткань")
s.img("run-details.gif", 0, 0, W, H, fx=0.5, fy=0.5, alt="Детали одежды в движении")
s.grad(0, 0, 1300, H, 90, [(0, INK, 0.88), (0.6, INK, 0.55), (1, INK, 0)])
label(s, M, M, 700, "Ткань и технологичность", PAPER)
s.text(M, 380, 900, 200, "Ткань повторяет движение тела.", color=PAPER, **DISPLAY)
s.text(M, 620, 760, 240,
       "Она растягивается, возвращается в форму и сохраняет силуэт. Свойства ткани не объясняем напрямую — "
       "показываем через движение, свет и контакт с телом.", color=PAPER, **BODY)

# 13 moments
s = new("moments", INK, "Момент")
s.img("lib-track-overhead.jpg", 0, 0, W, H, fx=0.5, fy=0.35, alt="Беговая дорожка сверху, ч/б")
s.rect(0, 0, W, H, INK, 0.62)
label(s, M, M, 700, "Structure", CLAY_D)
s.text(M, 176, 1200, 140, "Камера наблюдает за тем, что происходит в течение одного момента.", color=PAPER, **TITLE)
beats = ["Разминка", "Движение", "Короткий отдых", "Концентрация", "Эмоции"]
colw = 1664 / 5
s.rect(M, 560, 1664, 2, PAPER, 0.5)
for i, b in enumerate(beats):
    x = int(M + i * colw)
    s.rect(x, 548, 2, 26, PAPER, 0.9)
    s.text(x, 500, 200, 40, f"0{i + 1}", color=CLAY_D, **LABEL)
    s.text(x, 600, int(colw) - 24, 110, b, color=PAPER, font="light", size=44, lh=1.1, ls=-0.5)
s.text(M, 808, 960, 136,
       "Не строим сложную сюжетную линию и не ведём героя к результату. Детали создают ощущение документальности происходящего.",
       color=SOFT_D, **BODY)

# 14 running opener
s = new("running", INK, "Running")
s.img("run-aerial.jpg", 0, 0, W, H, alt="Бегуны на улице, вид сверху")
bottom_scrim(s, top=420, strength=0.8)
opener(s, "01 / 04 · 30″", "RUNNING", "Движение и технологичность")

# 15 lidar
s = new("lidar", "#060708", "LIDAR")
s.img("run-lidar.gif", 0, 400, W, 544, fx=0.5, fy=0.5, alt="Облако точек, LIDAR-референс")
label(s, M, M, 600, "LIDAR", CLAY_D)
s.text(M, 176, 880, 210, "В беге человек становится частью большой технологичной среды.", color=PAPER, **TITLE)
s.text(1128, 176, 664, 190,
       "LIDAR переводит реальное пространство в облако точек. Переход происходит прямо внутри движения "
       "и становится частью визуального языка ролика.", color=SOFT_D, **BODY)

# 16 scale & light
s = new("light", INK, "Локация и свет")
s.img("lib-light-track.jpg", 0, 0, W, H, fx=0.5, fy=0.6, alt="Световые пятна на дорожке, фигура бегуна")
s.grad(0, 0, W, 640, 180, [(0, INK, 0.75), (1, INK, 0)])
label(s, M, M, 700, "Локация и свет", PAPER)
s.text(M, 176, 1000, 140, "Масштаб локации подчёркивает движение героя в пространстве.", color=PAPER, **TITLE)
s.text(M, 348, 780, 140,
       "Локация — часть идентичности бега, а не только фон. Движение света создаёт дополнительную динамику и развитие.",
       color=PAPER, **BODY)

# 17 running details
s = new("run-details", INK, "Детали бега")
s.img("run-topdown.jpg", 0, 0, W, H, fx=0.5, fy=0.35, alt="Бегун на красной дорожке, вид сверху")
s.grad(0, 0, W, H, 90, [(0, INK, 0.7), (0.45, INK, 0.25), (0.7, INK, 0)])
label(s, M, M, 600, "Running", PAPER)
s.text(M, 176, 760, 260, "Помимо бега — разминка, отдых, эмоции и детали одежды.", color=PAPER, **TITLE)
s.text(M, 740, 640, 212,
       "Камера чаще наблюдает за героем со стороны. Эти моменты постепенно раскрывают характер героя.",
       color=PAPER, valign="b", **BODY)

# 18 padel opener
s = new("padel", INK, "Padel")
s.img("padel-lines.jpg", 0, 0, W, H, fx=0.5, fy=0.5, alt="Линии корта, макро")
bottom_scrim(s, top=360, strength=0.78)
opener(s, "02 / 04 · 30″", "PADEL", "Герой и геометрия")

# 19 geometry
s = new("geometry", PAPER, "Геометрия корта")
s.img("padel-clay-serve.jpg", M, M, 1040, 585, alt="Подача на корте, вид сверху, длинная тень")
s.img("padel-court-top.jpg", 1296, 560, 624, 351, alt="Корт сверху, игрок у корзины с мячами")
label(s, 1296, M, 500, "Геометрия", CLAY_L)
s.text(1296, 176, 496, 330,
       "Линии и разметка формируют композицию кадра. Съёмка через стекло позволяет смотреть на игру с необычных точек.",
       color=SOFT_L, **BODY)
s.text(M, 761, 1040, 150, "Герой постоянно взаимодействует с геометрией пространства.", color=INK, **SUB)

# 20 macro
s = new("macro", INK, "Макро")
s.img("padel-macro.gif", 0, 0, 1180, H, fx=0.5, fy=0.5, alt="Макро: ноги у линии, лицо игрока")
label(s, 1308, M, 484, "Макрооптика", CLAY_D)
s.text(1308, 176, 484, 330, "Камера приближается к самому движению.", color=PAPER, **TITLE)
s.text(1308, 716, 484, 236, "Она проходит вдоль рук, ракетки и ног — прямо перед ударом.", color=SOFT_D, **BODY)

# 21 sportswear opener
s = new("sportswear", INK, "Sportswear")
s.img("sw-storm.gif", 0, 0, W, H, fx=0.5, fy=0.3, alt="Силуэт бегуна под грозовым небом")
bottom_scrim(s, top=520, strength=0.6)
opener(s, "03 / 04 · 30″", "SPORTSWEAR", "Свобода и жизнь")

# 22 fashion
s = new("fashion", INK, "Fashion")
s.img("sw-rock-water.jpg", 1368, 310, 424, 642, alt="Модель на камне в воде, синий свет")
label(s, M, M, 600, "Sportswear", CLAY_D)
s.text(M, 176, 1000, 300, "Здесь визуальный язык становится ближе к fashion.", color=PAPER, **DISPLAY)
s.text(M, 620, 860, 140,
       "В центре — модели, их движение и позирование. Одежда раскрывается через силуэт, пластику и характер человека.",
       color=SOFT_D, **BODY)
s.text(M, 812, 860, 140,
       "Спорт не задаёт жёсткую структуру действия, а становится естественной частью образа.",
       color=SOFT_D, **BODY)

# 23 water
s = new("water", INK, "Вода")
s.img("sw-water-macro.gif", 740, 0, 1180, H, fx=0.5, fy=0.5, alt="Вода, капли, лицо в очках")
label(s, M, M, 560, "Студия · практические эффекты", CLAY_D)
fx_rows = [
    ("Вода", "Камера проходит сквозь воду на высокой скорости. Рапид фиксирует движение воды и одежды."),
    ("Отражения", "Вода на полу создаёт отражения. В некоторых сценах она исчезает, открывая CG-пространство."),
    ("Свет", "Динамический свет связывает разные состояния внутри одного ролика."),
]
for i, (k, v) in enumerate(fx_rows):
    y = 236 + i * 240
    s.text(M, y, 520, 40, k, color=PAPER, **LABEL)
    s.text(M, y + 44, 520, 180, v, color=SOFT_D, **BODY)

# 24 fitness opener
s = new("fitness", PAPER, "Fitness")
s.img("fit-studio.gif", 0, 0, W, H, fx=0.5, fy=0.5, alt="Фитнес в белой студии, синий костюм")
s.grad(0, 480, W, H - 480, 180, [(0, PAPER, 0), (0.55, PAPER, 0.72), (1, PAPER, 0.92)])
opener(s, "04 / 04 · 30″", "FITNESS", "Движение и эстетика", dark_text=True)

# 25 fitness space
s = new("space", PAPER, "Пространство")
s.img("fit-room-cg.jpg", 0, 0, 1160, H, fx=0.5, fy=0.5, alt="Белая комната со световой платформой")
s.img("fit-platform-top.gif", 1288, M, 504, 336, alt="Платформа сверху, двое героев")
label(s, 1288, 760, 504, "Пространство", CLAY_L)
s.text(1288, 804, 504, 148, "Световая платформа и потолок — пространство для героев.", color=INK, valign="b", **SUB)

# 26 robo arm + match cut
s = new("matchcut", INK, "Роборука и match cut")
s.img("fit-roboarm.gif", M, M, 960, 640, alt="Роборука на площадке, детали обуви")
s.img("fit-details.gif", 1216, 392, 576, 384, alt="Фитнес-детали: руки, ткань, бег")
label(s, 1216, 336, 576, "Match cut →", CLAY_D)
s.text(M, 816, 960, 136,
       "Ролик снимается на роборуку. Камера проходит длинные фазы движения, внутри которых несколько действий соединяются через match cut.",
       color=SOFT_D, **BODY)
s.text(1216, 816, 576, 136, "Одно движение переходит в другое.", color=PAPER, **SUB)

# 27 location opener
s = new("location", "#050607", "Location")
s.img("loc-floodlights.gif", 0, 0, W, H, fx=0.5, fy=0.5, alt="Прожекторы стадиона включаются")
opener(s, "Локации", "LOCATION", "")

# 28 locations
s = new("locations", INK, "Локации")
s.img("loc-cska.jpg", 0, 0, W, 560, fx=0.5, fy=0.72, alt="Легкоатлетический манеж ЦСКА")
places = [("Running", "Стадион ЦСКА"), ("Padel", "Крытый корт или имитация корта"),
          ("Fitness", "Студия, застройка"), ("Sportswear", "Дарк рум с водой + CG фона")]
cw = (1664 - 3 * 40) / 4
for i, (k, v) in enumerate(places):
    x = int(M + i * (cw + 40))
    s.text(x, 632, int(cw), 40, k, color=CLAY_D, **LABEL)
    s.text(x, 680, int(cw), 200, v, color=PAPER, **SUB)

# 29 cast & styling
s = new("cast", PAPER, "Cast & Styling")
s.img("lib-athlete-bw.jpg", 0, 0, 640, H, fx=0.5, fy=0.5, alt="Атлет в прыжке, ч/б")
s.img("padel-racket-portrait.gif", 1320, 600, 600, 480, alt="Героиня с ракеткой")
label(s, 768, M, 600, "Cast & Styling", CLAY_L)
s.text(768, 176, 1000, 200, "Живые и настоящие люди в кадре.", color=INK, **DISPLAY)
s.text(768, 400, 960, 180,
       "Не хочется нагнетать слишком много игры. Важно сохранить ощущение реального спорта и дать героям "
       f"достаточно индивидуальности, чтобы они воспринимались как носители образа {BRAND}.",
       color=SOFT_L, **BODY)
s.text(768, 660, 480, 260,
       "Каждый герой — запоминающийся образ, соответствующий уровню одежды и характеру бренда.",
       color=INK, **BODY)

# 30 sound & edit
s = new("sound", INK, "Sound & Edit")
s.img("lib-metronomes.jpg", 1100, 0, 820, H, fx=0.5, fy=0.42, alt="Метрономы, ч/б")
label(s, M, M, 600, "Sound & Edit", CLAY_D)
s.text(M, 176, 900, 200, "Ритм меняется вместе с действием.", color=PAPER, **DISPLAY)
label(s, M, 424, 400, "Монтаж", PAPER)
s.text(M, 468, 860, 140,
       "Быстрые фрагменты чередуются с паузами и наблюдением. Рапиды задерживают на моменте: движение ткани, жест, взгляд, эмоция.",
       color=SOFT_D, **BODY)
label(s, M, 652, 400, "Звук", PAPER)
s.text(M, 696, 860, 260,
       "Пространство, эхо, гул. Шаги, дыхание, движение одежды и среда. Хороший современный сэмпл и саунд-дизайн — "
       "без банальных акцентов на движениях и барабанов.", color=SOFT_D, **BODY)

# 31 conclusion
s = new("conclusion", INK, "Conclusion")
s.img("lib-runners-shadows.jpg", 0, 0, W, H, fx=0.5, fy=0.55, alt="Бегуны с длинными тенями, ч/б")
s.grad(0, 0, W, H, 90, [(0, INK, 0.85), (0.55, INK, 0.5), (1, INK, 0.1)])
label(s, M, M, 600, "Conclusion", PAPER)
s.text(M, 360, 1300, 300, "В центре спорта остаются человек, движение и ощущение себя.", color=PAPER, **DISPLAY)
s.text(M, 716, 900, 236,
       "Мы видим большой потенциал в том, чтобы через простые и живые моменты показать характер бренда. "
       "Не объяснять его напрямую, а дать почувствовать через героя, движение, одежду и пространство.",
       color=PAPER, **BODY)

# 32 thanks
s = new("thanks", INK, "Спасибо")
s.img("lib-jump-sky.jpg", 0, 0, W, H, fx=0.5, fy=0.4, alt="Прыжок на фоне неба")
s.grad(0, 360, W, H - 360, 180, [(0, INK, 0), (0.45, INK, 0.7), (1, INK, 0.94)])
s.text(M, 620, 900, 140,
       "Мне было интересно работать с идеей, миссией и позиционированием бренда — и соединить их "
       "с моей визуальной стилистикой и собственным видением.", color=PAPER, **BODY)
s.text(M, 790, 1500, 162, "Спасибо за возможность стать его частью!", color=PAPER, valign="b", **TITLE)


if __name__ == "__main__":
    out_pptx = os.path.join(PRES, "SONU_SS27_DirNote.pptx")
    out_html = os.path.join(PRES, "SONU_SS27_DirNote.html")
    build_pptx(slides, ASSETS, out_pptx)
    build_html(slides, os.path.join(HERE, "template.html"), out_html, "assets/", "fonts/")
    print(len(slides), "slides")
    print(out_pptx, os.path.getsize(out_pptx) // 1_000_000, "MB")
    print(out_html)
