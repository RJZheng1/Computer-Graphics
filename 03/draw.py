from display import *
from matrix import *
from math import cos, sin, pi

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    while t < 1.001:
        x = cx + r*cos(2*pi*t)
        y = cy + r*sin(2*pi*t)
        t += 1.0/step
        add_edge(points, x, y, cz, cx+r*cos(2*pi*t), cy+r*sin(2*pi*t), cz)

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    #curve_type 0 is a hermite curve
    #curve_type 1 is a bezier curve
    if curve_type == 0:
        m = make_hermite()
    else:
        m = make_bezier()
    c = generate_curve_coefs([x0, y0], [x1, y1], [x2, y2], [x3, y3], m)
    t = 0
    while t < 1.001:
        x = t*(t*(c[0][0]*t + c[0][1]) + c[0][2]) + c[0][3]
        y = t*(t*(c[1][0]*t + c[1][1]) + c[1][2]) + c[1][3]
        t += 1.0/step
        add_edge(points, x, y, 0, t*(t*(c[0][0]*t + c[0][1]) + c[0][2]) + c[0][3], t*(t*(c[1][0]*t + c[1][1]) + c[1][2]) + c[1][3], 0)
    
def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

