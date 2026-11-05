"""Render an original pixel-art coding loop. Requires Pillow; no network or fonts."""
from pathlib import Path
import random
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 480, 192
FONT = ImageFont.load_default()
BG, PANEL, EDGE = "#100e1b", "#19152b", "#45325f"
MINT, PURPLE, WHITE = "#5eead4", "#b89aff", "#e5def7"
GLYPHS = {
    "L": ["10000"]*6 + ["11111"],
    "U": ["10001"]*6 + ["01110"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "N": ["10001", "11001", "11001", "10101", "10011", "10011", "10001"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01110"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
}


def title(draw, text, x, y, color, size=3):
    for char in text:
        for row, bits in enumerate(GLYPHS.get(char, [])):
            for col, bit in enumerate(bits):
                if bit == "1":
                    draw.rectangle((x+col*size, y+row*size,
                                    x+(col+1)*size-1, y+(row+1)*size-1), fill=color)
        x += 6*size if char != " " else 3*size


def frame(t):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    rng = random.Random(23)
    # Reproducible skyline and stars behind the workstation.
    for _ in range(45):
        x, y = rng.randrange(260, 473), rng.randrange(9, 110)
        d.point((x, y), fill=PURPLE if (x+t//6) % 5 else MINT)
    d.rectangle((413, 17, 431, 35), fill=PURPLE)
    d.rectangle((408, 13, 424, 29), fill=BG)
    for x in range(264, 480, 19):
        top = rng.randrange(50, 110)
        d.rectangle((x, top, x+15, 143), fill="#211b36")
        for wy in range(top+7, 139, 10):
            for wx in (x+4, x+10):
                d.rectangle((wx, wy, wx+2, wy+3), fill="#55416d")
    d.line((256, 0, 256, 143), fill=EDGE)
    d.rectangle((14, 14, 89, 17), fill=MINT)
    d.text((14, 24), "PLAYER 01 / BACKEND DEV", font=FONT, fill=MINT)
    title(d, "LUAN", 16, 45, "#49355f")
    title(d, "LUAN", 14, 43, WHITE)
    title(d, "NGUYEN", 16, 74, "#49355f")
    title(d, "NGUYEN", 14, 72, PURPLE)
    d.text((14, 103), "BUILD. DEBUG. LEVEL UP.", font=FONT, fill="#a69bbd")
    # Window frame, monitor and chunky pixel desk.
    d.rectangle((270, 6, 473, 141), outline=EDGE, width=2)
    d.line((370, 6, 370, 90), fill=EDGE, width=2)
    d.rectangle((302, 58, 382, 113), fill="#392b50")
    d.rectangle((305, 61, 379, 108), fill="#090f1c")
    for row in range(7):
        yy = 67 + row*5
        indent = (row % 3)*4
        length = min(48, max(0, (t*3-row*9) % 76))
        d.rectangle((311+indent, yy, 312+indent+length, yy+1),
                    fill=[MINT, PURPLE, "#f4b57a"][row % 3])
    d.rectangle((335, 114, 348, 122), fill="#665184")
    d.rectangle((326, 121, 356, 124), fill="#665184")
    d.rectangle((280, 127, 460, 134), fill="#8660a4")
    d.rectangle((280, 135, 460, 140), fill="#3a284f")
    d.rectangle((287, 141, 295, 179), fill="#49315f")
    d.rectangle((447, 141, 455, 179), fill="#49315f")
    # Coffee, steam, and keyboard.
    d.rectangle((285, 114, 294, 125), fill=MINT)
    d.rectangle((295, 116, 298, 122), outline=MINT)
    d.line((289, 110, 290+(t//4 % 2), 105), fill="#8b7da1")
    d.rectangle((320, 125, 358, 127), fill="#c4b5dd")
    # Developer seen from the side, with alternating typing hand position.
    d.rectangle((389, 92, 410, 115), fill="#f2b99f")
    d.rectangle((386, 86, 410, 100), fill="#2c223d")
    d.rectangle((382, 93, 390, 110), fill=PURPLE)
    d.rectangle((389, 93, 393, 105), fill=MINT)
    d.rectangle((389, 114, 418, 145), fill="#7653a9")
    d.rectangle((379, 120, 394, 128), fill="#9870cf")
    d.rectangle((365, 124-(t % 4 < 2), 380, 127), fill="#f2b99f")
    d.rectangle((411, 113, 424, 151), fill="#302343")
    d.rectangle((387, 146, 421, 155), fill="#302343")
    d.rectangle((396, 156, 401, 178), fill="#6a537d")
    d.line((384, 179, 417, 179), fill="#6a537d", width=3)
    # Foreground terminal: an illustrative compile loop, not live metrics.
    d.rectangle((14, 127, 250, 177), fill="#0b1320", outline=EDGE)
    d.text((21, 132), "$ pnpm build", font=FONT, fill=MINT)
    code = "compiling backend modules..."
    visible = min(len(code), t)
    d.text((21, 146), code[:visible], font=FONT, fill=WHITE)
    if t < 32:
        if t % 8 < 4:
            d.rectangle((22+int(d.textlength(code[:visible], font=FONT)), 147,
                         26+int(d.textlength(code[:visible], font=FONT)), 155), fill=MINT)
    else:
        d.text((21, 161), "> BUILD COMPLETE. NEXT QUEST?", font=FONT, fill=MINT)
    d.line((0, 185, W, 185), fill=EDGE)
    for x in range(264, 470, 8):
        d.rectangle((x, 187, x+3, 189), fill=MINT if x < 264+t*4 else EDGE)
    return im.resize((960, 384), Image.Resampling.NEAREST)


if __name__ == "__main__":
    frames = [frame(t) for t in range(48)]
    frames[0].save(OUT / "pixel-code.gif", save_all=True,
                   append_images=frames[1:], duration=120, loop=0, optimize=False)
    print(f"Saved {OUT / 'pixel-code.gif'} ({len(frames)} frames)")
