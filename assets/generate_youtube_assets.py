"""
Generate YouTube banner and logo for Victorjia trading channel.
"""

from PIL import Image, ImageDraw, ImageFont
import math
import random

random.seed(42)

# ============================================================
# HELPER: Try to load a nice font, fallback to default
# ============================================================
def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def get_bold_font(size):
    bold_paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in bold_paths:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return get_font(size, bold=True)


# ============================================================
# 1. YOUTUBE BANNER (2048 x 1152)
# ============================================================
def create_banner():
    W, H = 2048, 1152
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)

    # --- Dark gradient background ---
    for y in range(H):
        t = y / H
        r = int(10 + t * 15)
        g = int(14 + t * 20)
        b = int(30 + t * 35)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # --- Subtle grid lines ---
    grid_color = (30, 38, 55)
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=grid_color, width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=grid_color, width=1)

    # --- Draw candlestick chart on the RIGHT side ---
    candle_data = []
    price = 100.0
    for i in range(28):
        open_p = price
        change = random.uniform(-3, 3.5)
        close_p = open_p + change
        high_p = max(open_p, close_p) + random.uniform(0.5, 2.5)
        low_p = min(open_p, close_p) - random.uniform(0.5, 2.5)
        candle_data.append((open_p, high_p, low_p, close_p))
        price = close_p + random.uniform(-0.5, 0.5)

    all_prices = [p for c in candle_data for p in c]
    min_price = min(all_prices)
    max_price = max(all_prices)
    price_range = max_price - min_price

    chart_left = 1050
    chart_right = 1950
    chart_top = 180
    chart_bottom = 950
    chart_h = chart_bottom - chart_top
    candle_w = (chart_right - chart_left) / len(candle_data)

    def price_to_y(p):
        return chart_bottom - ((p - min_price) / price_range) * chart_h

    # --- Horizontal price level lines ---
    for y_level in [chart_top + 50, chart_top + 250, chart_top + 450, chart_top + 650]:
        draw.line([(chart_left - 30, y_level), (chart_right + 20, y_level)],
                  fill=(35, 45, 65), width=1)
        price_val = min_price + (chart_bottom - y_level) / chart_h * price_range
        label = f"{price_val:.1f}"
        draw.text((chart_right + 25, y_level - 10), label, fill=(60, 75, 100), font=get_font(18))

    # Moving average line
    ma_points = []
    window = 5
    for i in range(len(candle_data)):
        start = max(0, i - window + 1)
        avg = sum(c[3] for c in candle_data[start:i+1]) / (i - start + 1)
        cx = chart_left + i * candle_w + candle_w / 2
        cy = price_to_y(avg)
        ma_points.append((cx, cy))

    if len(ma_points) > 1:
        for i in range(len(ma_points) - 1):
            draw.line([ma_points[i], ma_points[i+1]], fill=(60, 100, 180), width=2)

    # Draw candles
    green = (0, 200, 120)
    red = (220, 50, 50)
    green_body = (0, 180, 100)
    red_body = (200, 40, 40)

    for i, (o, h, l, c) in enumerate(candle_data):
        x_center = chart_left + i * candle_w + candle_w / 2
        body_w = candle_w * 0.55

        y_high = price_to_y(h)
        y_low = price_to_y(l)
        y_open = price_to_y(o)
        y_close = price_to_y(c)

        is_bull = c >= o
        color = green if is_bull else red
        bc = green_body if is_bull else red_body

        # Wick
        draw.line([(x_center, y_high), (x_center, y_low)], fill=color, width=2)

        # Body
        y_top = min(y_open, y_close)
        y_bot = max(y_open, y_close)
        if y_bot - y_top < 2:
            y_bot = y_top + 2

        draw.rectangle(
            [x_center - body_w/2, y_top, x_center + body_w/2, y_bot],
            fill=bc, outline=color, width=1,
        )

    # --- Glow effect behind text area ---
    glow_cx, glow_cy = 450, H // 2
    for radius in range(400, 0, -2):
        alpha = int(8 * (1 - radius / 400))
        glow_color = (15 + alpha * 2, 30 + alpha * 3, 70 + alpha * 4)
        draw.ellipse(
            [glow_cx - radius, glow_cy - radius, glow_cx + radius, glow_cy + radius],
            fill=glow_color,
        )

    # --- Main text: "Victorjia" ---
    font_main = get_bold_font(130)
    font_sub = get_font(42)
    font_tag = get_font(32)

    text_main = "Victorjia"
    bbox = draw.textbbox((0, 0), text_main, font=font_main)
    tw = bbox[2] - bbox[0]

    text_x = 120
    text_y = H // 2 - 120

    # Text shadow
    for ox, oy in [(3, 3), (2, 2), (1, 1)]:
        draw.text((text_x + ox, text_y + oy), text_main, fill=(0, 0, 0), font=font_main)

    # Main text
    draw.text((text_x, text_y), text_main, fill=(255, 255, 255), font=font_main)

    # --- Accent line under main text ---
    accent_color = (220, 175, 50)
    line_y = text_y + 145
    draw.rectangle([text_x, line_y, text_x + tw, line_y + 4], fill=accent_color)

    # --- Subtitle ---
    subtitle = "Al Brooks Price Action | Trading Education"
    sub_y = line_y + 30
    draw.text((text_x + 2, sub_y + 2), subtitle, fill=(0, 0, 0), font=font_sub)
    draw.text((text_x, sub_y), subtitle, fill=(180, 195, 220), font=font_sub)

    # --- Tagline ---
    tagline = "Learn to Read Price Charts Like a Pro"
    tag_y = sub_y + 65
    draw.text((text_x, tag_y), tagline, fill=(100, 120, 150), font=font_tag)

    # --- Bottom border accent ---
    draw.rectangle([0, H - 4, W, H], fill=accent_color)

    img.save("/Users/zhiqiangjia/Claude-Global/公众号国际化/assets/youtube_banner.png", "PNG")
    print("Banner saved: youtube_banner.png (2048x1152)")


# ============================================================
# 2. YOUTUBE LOGO (800 x 800)
# ============================================================
def create_logo():
    W, H = 800, 800
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = W // 2, H // 2
    radius = 370

    # --- Dark circular background with gradient ---
    for r in range(radius, 0, -1):
        t = r / radius
        cr = int(12 + (1 - t) * 15)
        cg = int(16 + (1 - t) * 22)
        cb = int(35 + (1 - t) * 40)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(cr, cg, cb, 255))

    # --- Subtle ring border ---
    accent_color = (220, 175, 50)
    ring_w = 6
    for i in range(ring_w):
        r = radius - i
        alpha = int(255 * (1 - i / ring_w) * 0.8)
        color = (accent_color[0], accent_color[1], accent_color[2], alpha)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=1)

    # --- Draw the "V" letter using polygons ---
    v_top_y = 180
    v_bottom_y = 560
    v_left_x = 195
    v_right_x = 605
    v_center_x = cx
    stroke_w = 50

    # Left stroke of V
    left_stroke = [
        (v_left_x, v_top_y),
        (v_left_x + stroke_w + 15, v_top_y),
        (v_center_x + stroke_w // 2, v_bottom_y),
        (v_center_x - stroke_w // 2, v_bottom_y),
    ]

    # Right stroke of V
    right_stroke = [
        (v_right_x - stroke_w - 15, v_top_y),
        (v_right_x, v_top_y),
        (v_center_x + stroke_w // 2, v_bottom_y),
        (v_center_x - stroke_w // 2, v_bottom_y),
    ]

    draw.polygon(left_stroke, fill=(255, 255, 255, 245))
    draw.polygon(right_stroke, fill=(255, 255, 255, 245))

    # --- Small upward chart line integrated into right arm of V ---
    chart_start_x = v_center_x + 30
    chart_start_y = v_bottom_y - 180

    chart_points = [
        (chart_start_x, chart_start_y),
        (chart_start_x + 40, chart_start_y - 15),
        (chart_start_x + 70, chart_start_y - 5),
        (chart_start_x + 110, chart_start_y - 45),
        (chart_start_x + 145, chart_start_y - 35),
        (chart_start_x + 180, chart_start_y - 85),
        (chart_start_x + 205, chart_start_y - 110),
    ]

    # Glow effect around chart line
    for glow in range(6, 0, -1):
        for i in range(len(chart_points) - 1):
            draw.line([chart_points[i], chart_points[i + 1]],
                      fill=(0, 200, 120, 60), width=glow * 2)

    # Main chart line
    for i in range(len(chart_points) - 1):
        draw.line([chart_points[i], chart_points[i + 1]],
                  fill=(0, 220, 130, 255), width=4)

    # Dot at the end
    end_x, end_y = chart_points[-1]
    draw.ellipse([end_x - 5, end_y - 5, end_x + 5, end_y + 5],
                 fill=(0, 255, 140, 255))

    # --- Mini candlesticks along chart ---
    mini_candles = [
        (chart_start_x + 40, chart_start_y - 15, True),
        (chart_start_x + 110, chart_start_y - 45, False),
        (chart_start_x + 145, chart_start_y - 35, True),
        (chart_start_x + 180, chart_start_y - 85, True),
    ]

    for mcx, mcy, is_bull in mini_candles:
        c = (0, 200, 120, 200) if is_bull else (220, 60, 60, 200)
        body_h = random.randint(10, 20)
        wick_h = random.randint(5, 12)
        if is_bull:
            draw.line([(mcx, mcy - wick_h - body_h), (mcx, mcy + wick_h)], fill=c, width=2)
            draw.rectangle([mcx - 4, mcy - body_h, mcx + 4, mcy], fill=c)
        else:
            draw.line([(mcx, mcy - wick_h), (mcx, mcy + body_h + wick_h)], fill=c, width=2)
            draw.rectangle([mcx - 4, mcy, mcx + 4, mcy + body_h], fill=c)

    # --- Accent dot at V bottom ---
    draw.ellipse([v_center_x - 8, v_bottom_y - 5, v_center_x + 8, v_bottom_y + 11],
                 fill=accent_color)

    # Flatten alpha onto dark background
    bg = Image.new("RGB", (W, H), (0, 0, 0))
    bg.paste(img, (0, 0), img)
    bg.save("/Users/zhiqiangjia/Claude-Global/公众号国际化/assets/youtube_logo.png", "PNG")
    print("Logo saved: youtube_logo.png (800x800)")


if __name__ == "__main__":
    create_banner()
    create_logo()
    print("Done! Both images generated.")
