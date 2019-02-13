# The MIT License (MIT)
#
# Copyright (c) 2019 Jonah Yolles-Murphy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import displayio
from adafruit_bitmap_font import bitmap_font

def color(r,g,b):
    return (r<< 16) + (g<< 8) + (b)

def rect(x, y, width, height, color):
    global _bad_practice

    plt = displayio.Palette(2)
    plt.make_transparent(0)
    plt[1] = color

    return displayio.TileGrid(displayio.Shape(width, height), pixel_shader = plt, position = (x,y))


def roundrect(x, y, width, height, radius, color):
    global _bad_practice

    plt = displayio.Palette(2)
    plt.make_transparent(0)
    plt[1] = color

    shp = displayio.Shape(width, height)

    for y_pos in range(radius):
        #not turned to int here due to rounding errors post subtractions below
        clip_off = radius - ((radius**2)-(y_pos-radius)**2)**.5 #r-((r**2)-(y-r)**2)**.5 = x
        shp.set_boundary(y_pos , int(clip_off), int(width- clip_off))
        shp.set_boundary(height -1 -y_pos, int(clip_off) , int(width- clip_off))

    return displayio.TileGrid(shp, pixel_shader = plt, position = (x,y))


def hline(x, y, length, thickness, color):
    return rect(x, y, length, thickness, color)

def vline(x, y, length, thickness, color):
    return rect(x, y, thickness, length, color)

def circle(x, y, radius, color):
    return roundrect(x - radius, y - radius, radius*2, radius*2, radius, color)