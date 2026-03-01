#!/usr/bin/env python3
"""生成 YouTube 视频封面模板 (1280x720)"""

from PIL import Image, ImageDraw, ImageFont
import os, math, random

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1280, 720

# Colors
DARK_BG = (26, 26, 46)
DARK_BG2 = (15, 15, 35)
GOLD = (212, 168, 67)
WHITE = (255, 255, 255)
RED_CANDLE = (220, 60, 60)
GREEN_CANDLE = (60, 180, 80)
ORANGE = (255, 120, 40)
TEAL = (40, 180, 180)
BLUE_ACCENT = (60, 120, 220)

def get_font(size, bold=True):
    paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size, index=1 if bold and p.endswith('.ttc') else 0)
            except:
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def get_cn_font(size):
    paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size, index=0)
            except:
                pass
    return get_font(size)

def draw_gradient(draw, y0, y1, c1, c2, w=W):
    for y in range(y0, y1):
        t = (y - y0) / max(1, y1 - y0)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def draw_candles(draw, x_start, y_base, count, height_range, candle_w=12, gap=6):
    """Draw candlestick chart pattern"""
    x = x_start
    price = y_base
    for i in range(count):
        change = random.randint(-height_range, height_range)
        o = price
        c = price + change
        h = min(o, c) - random.randint(5, 25)
        l = max(o, c) + random.randint(5, 25)
        color = GREEN_CANDLE if c < o else RED_CANDLE  # inverted Y axis
        # Wick
        cx = x + candle_w // 2
        draw.line([(cx, h), (cx, l)], fill=color, width=1)
        # Body
        top = min(o, c)
        bot = max(o, c)
        if bot - top < 2:
            bot = top + 2
        draw.rectangle([(x, top), (x + candle_w, bot)], fill=color)
        price = c
        x += candle_w + gap

def draw_grid(draw, alpha_factor=0.3):
    """Draw subtle grid lines"""
    grid_color = (40, 40, 70)
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=grid_color, width=1)
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=grid_color, width=1)

def add_watermark(draw, text="Victorjia"):
    font = get_font(24)
    draw.text((W - 160, H - 40), text, fill=(*GOLD, 180), font=font)

def add_series_badge(draw, text, color=GOLD):
    font = get_font(18)
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.rounded_rectangle([(30, 25), (60 + tw, 55)], radius=5, fill=(*color, 200))
    draw.text((45, 28), text, fill=DARK_BG, font=font)

# ── Template 1: Course (系统课程) ──
def make_cover_course():
    img = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw_gradient(draw, 0, H, (20, 30, 60), DARK_BG2)
    draw_grid(draw)

    random.seed(42)
    draw_candles(draw, 50, 400, 55, 40, candle_w=14, gap=8)

    # Moving average line
    points = []
    y = 380
    for x in range(50, W - 50, 15):
        y += random.randint(-8, 8)
        y = max(280, min(480, y))
        points.append((x, y))
    if len(points) > 1:
        draw.line(points, fill=(*GOLD, 200), width=2)

    # Dark overlay for text area
    for y in range(200, 520):
        alpha = 0.7
        draw.line([(300, y), (W - 80, y)], fill=(20, 20, 40))

    # EP number
    ep_font = get_font(140, bold=True)
    draw.text((340, 210), "EP01", fill=GOLD, font=ep_font)

    # Title
    cn_font = get_cn_font(42)
    draw.text((340, 380), "如何识别强趋势", fill=WHITE, font=cn_font)
    cn_font_sm = get_cn_font(28)
    draw.text((340, 435), "的3个关键信号", fill=(*WHITE[:3],), font=cn_font_sm)

    add_series_badge(draw, "TREND TRADING", GOLD)
    add_watermark(draw)

    img.save(os.path.join(OUT, "cover_course.png"), quality=95)
    print("✅ cover_course.png")

# ── Template 2: Concept (概念讲解) ──
def make_cover_concept():
    img = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw_gradient(draw, 0, H, (25, 25, 50), (10, 10, 30))
    draw_grid(draw)

    # Draw a wedge/triangle pattern
    points_upper = [(200, 350), (500, 300), (800, 280)]
    points_lower = [(200, 400), (500, 420), (800, 430)]
    draw.line(points_upper, fill=(*GOLD, 200), width=3)
    draw.line(points_lower, fill=(*GOLD, 200), width=3)

    # Breakout arrow
    draw.line([(800, 280), (950, 180)], fill=GREEN_CANDLE, width=4)
    draw.polygon([(940, 195), (970, 170), (945, 175)], fill=GREEN_CANDLE)

    # Question mark
    q_font = get_font(200, bold=True)
    draw.text((950, 300), "?", fill=(*ORANGE, 150), font=q_font)

    # Title
    cn_font = get_cn_font(52)
    draw.text((80, 500), "假突破怎么识别？", fill=WHITE, font=cn_font)
    cn_font_sm = get_cn_font(30)
    draw.text((80, 570), "3个特征帮你避坑", fill=GOLD, font=cn_font_sm)

    add_series_badge(draw, "BREAKOUT", BLUE_ACCENT)
    add_watermark(draw)

    img.save(os.path.join(OUT, "cover_concept.png"), quality=95)
    print("✅ cover_concept.png")

# ── Template 3: Shorts (短视频) ──
def make_cover_shorts():
    img = Image.new('RGB', (W, H))
    draw = ImageDraw.Draw(img)
    # Vibrant gradient: deep red to orange
    draw_gradient(draw, 0, H, (180, 30, 30), (220, 100, 20))

    # Large bold text
    cn_font = get_cn_font(72)
    draw.text((80, 180), "90%的交易者", fill=WHITE, font=cn_font)
    draw.text((80, 270), "不知道这个", fill=WHITE, font=cn_font)

    cn_font_gold = get_cn_font(80)
    draw.text((80, 380), "止损技巧", fill=(255, 255, 100), font=cn_font_gold)

    # Exclamation mark
    bang_font = get_font(180, bold=True)
    draw.text((1050, 150), "!", fill=(255, 255, 100), font=bang_font)

    # Bottom bar
    draw.rectangle([(0, H-60), (W, H)], fill=(0, 0, 0))
    bar_font = get_cn_font(28)
    draw.text((40, H-48), "#PriceAction  #交易技巧  #AlBrooks", fill=GOLD, font=bar_font)

    add_watermark(draw)

    img.save(os.path.join(OUT, "cover_shorts.png"), quality=95)
    print("✅ cover_shorts.png")

# ── Template 4: Podcast (播客/书评) ──
def make_cover_podcast():
    img = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw_gradient(draw, 0, H, (20, 20, 45), (10, 10, 25))

    # Book icon (simplified)
    bx, by = 160, 180
    # Book spine
    draw.rectangle([(bx, by), (bx+180, by+280)], fill=(60, 50, 40), outline=GOLD, width=2)
    draw.line([(bx+15, by+10), (bx+15, by+270)], fill=GOLD, width=2)
    # Book title lines
    for i in range(5):
        y = by + 40 + i * 30
        draw.line([(bx+35, y), (bx+160, y)], fill=(150, 140, 120), width=2)

    # Headphone icon (circle + arc)
    cx, cy = 160 + 90, by + 320
    draw.arc([(cx-40, cy-30), (cx+40, cy+10)], 180, 0, fill=GOLD, width=3)
    draw.ellipse([(cx-50, cy-5), (cx-30, cy+25)], fill=GOLD)
    draw.ellipse([(cx+30, cy-5), (cx+50, cy+25)], fill=GOLD)

    # Episode info
    ep_font = get_font(28)
    draw.text((450, 150), "TRADING BOOK CLUB", fill=GOLD, font=ep_font)

    num_font = get_font(100, bold=True)
    draw.text((450, 200), "EP 05", fill=WHITE, font=num_font)

    cn_font = get_cn_font(44)
    draw.text((450, 340), "《交易心理分析》", fill=WHITE, font=cn_font)

    cn_font_sm = get_cn_font(28)
    draw.text((450, 400), "接受不确定性才能长期盈利", fill=GOLD, font=cn_font_sm)

    # Separator line
    draw.line([(450, 460), (1100, 460)], fill=GOLD, width=1)

    cn_font_xs = get_cn_font(22)
    draw.text((450, 480), "Mark Douglas 的核心观点：单笔结果随机，", fill=(180, 180, 180), font=cn_font_xs)
    draw.text((450, 510), "样本结果可确定。不需知道下一刻会发生什么", fill=(180, 180, 180), font=cn_font_xs)
    draw.text((450, 540), "也能长期赚钱。", fill=(180, 180, 180), font=cn_font_xs)

    add_watermark(draw)

    img.save(os.path.join(OUT, "cover_podcast.png"), quality=95)
    print("✅ cover_podcast.png")

# ── Template 5: Beginner (入门引导) ──
def make_cover_beginner():
    img = Image.new('RGB', (W, H))
    draw = ImageDraw.Draw(img)
    # Gradient: dark teal to dark blue
    draw_gradient(draw, 0, H, (15, 60, 80), (15, 25, 60))

    # Staircase / growth path
    steps = [(100, 580), (250, 520), (400, 450), (550, 370), (700, 280), (850, 180)]
    for i, (x, y) in enumerate(steps):
        # Step block
        color = tuple(int(c + (TEAL[j] - DARK_BG[j]) * i / len(steps)) for j, c in enumerate(DARK_BG))
        draw.rectangle([(x, y), (x+120, y+40)], fill=color, outline=TEAL, width=2)
        if i < len(steps) - 1:
            nx, ny = steps[i+1]
            draw.line([(x+120, y+20), (nx, ny+20)], fill=TEAL, width=2)

    # Star at top
    sx, sy = 920, 140
    for angle in range(0, 360, 72):
        rad = math.radians(angle)
        ex = sx + int(30 * math.sin(rad))
        ey = sy - int(30 * math.cos(rad))
        draw.line([(sx, sy), (ex, ey)], fill=GOLD, width=2)
    draw.ellipse([(sx-8, sy-8), (sx+8, sy+8)], fill=GOLD)

    # Title
    cn_font = get_cn_font(56)
    draw.text((80, 50), "交易新手第一步", fill=WHITE, font=cn_font)

    cn_font_sub = get_cn_font(36)
    draw.text((80, 120), "你该从哪里开始？", fill=TEAL, font=cn_font_sub)

    # Labels on steps
    labels = ["认知", "学习", "模拟", "实盘", "复盘", "盈利"]
    label_font = get_cn_font(20)
    for i, (x, y) in enumerate(steps):
        draw.text((x+20, y+8), labels[i], fill=WHITE, font=label_font)

    add_series_badge(draw, "BEGINNER", TEAL)
    add_watermark(draw)

    img.save(os.path.join(OUT, "cover_beginner.png"), quality=95)
    print("✅ cover_beginner.png")

if __name__ == "__main__":
    random.seed(42)
    make_cover_course()
    make_cover_concept()
    make_cover_shorts()
    make_cover_podcast()
    make_cover_beginner()
    print(f"\n🎨 All 5 templates saved to {OUT}/")
