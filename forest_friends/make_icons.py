"""Generates the app icons (icon-180/192/512.png) with only the standard library.

The PNGs are gitignored (media stays out of git); run this to recreate them:
    python make_icons.py
"""
import math
import struct
import zlib

SKY = (127, 211, 255)
GRASS = (92, 198, 64)
GOLD = (255, 207, 51)
GOLD_DARK = (201, 138, 0)
PINK = (255, 111, 168)
SS = 3  # supersampling per axis for smooth edges


def key_at(u, v):
    """Golden key, tilted. Returns a color or None."""
    # rotate into key space
    cx, cy, a = 0.5, 0.47, -0.6
    x, y = u - cx, v - cy
    kx = x * math.cos(a) - y * math.sin(a)
    ky = x * math.sin(a) + y * math.cos(a)
    d = math.hypot(kx + 0.17, ky)
    if d < 0.055:
        return PINK
    if d < 0.15:
        return GOLD if d < 0.13 else GOLD_DARK
    if -0.04 < kx < 0.30 and abs(ky) < 0.04:
        return GOLD
    if (0.16 < kx < 0.21 or 0.25 < kx < 0.29) and 0.0 < ky < 0.11:
        return GOLD
    return None


def color_at(u, v):
    k = key_at(u, v)
    if k:
        return k
    if v > 0.80 + 0.03 * math.sin(u * 18):
        return GRASS
    return SKY


def make(size, path):
    rows = []
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            acc = [0, 0, 0]
            for sy in range(SS):
                for sx in range(SS):
                    c = color_at((x + (sx + 0.5) / SS) / size, (y + (sy + 0.5) / SS) / size)
                    for i in range(3):
                        acc[i] += c[i]
            row += bytes(a // (SS * SS) for a in acc)
        rows.append(bytes(row))
    raw = zlib.compress(b''.join(rows), 9)

    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', raw) + chunk(b'IEND', b'')
    with open(path, 'wb') as f:
        f.write(png)


if __name__ == '__main__':
    for s in (180, 192, 512):
        make(s, f'icon-{s}.png')
        print(f'wrote icon-{s}.png')
