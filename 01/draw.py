from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if(x1 < x0):
        draw_line(screen, x1, y1, x0, y0, color)
    else:
        A = y1 - y0
        B = x0 - x1
        d = 2*A + B
        A *= 2
        B *= 2
        if(y1 - y0 > 0):
            if(y1 - y0 > x1 - x0):
                pass
            else:
                plot(screen, color, x0, y0)
                while(x0 != x1):
                    if(d > 0):
                        y0 += 1
                        d += B
                    x0 += 1
                    d += A
        else:
            if(y1 - y0 > x1 - x0):
                pass
            else:
                pass
