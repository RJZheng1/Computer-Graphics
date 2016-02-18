from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

for x in xrange(0, XRES, 10):
    for y in xrange(0, YRES, 10):
        draw_line(screen, XRES/2, YRES/2, x, y, color)

display(screen)
