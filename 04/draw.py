from display import *
from matrix import *
import math

def add_box( points, x, y, z, width, height, depth ):
    add_edge(points, x, y, z, x, y+height, z)
    add_edge(points, x, y, z, x+width, y, z)
    add_edge(points, x+width, y, z, x+width, y+height, z)
    add_edge(points, x, y+height, z, x+width, y+height, z)
    add_edge(points, x, y, z, x, y, z-depth)
    add_edge(points, x+width, y, z, x+width, y, z-depth)
    add_edge(points, x, y+height, z, x, y+height, z-depth)
    add_edge(points, x+width, y+height, z, x+width, y+height, z-depth)
    add_edge(points, x, y, z-depth, x, y+height, z-depth)
    add_edge(points, x, y, z-depth, x+width, y, z-depth)
    add_edge(points, x+width, y, z-depth, x+width, y+height, z-depth)
    add_edge(points, x, y+height, z-depth, x+width, y+height, z-depth)
    
def add_sphere( points, cx, cy, cz, r, step ):
    sphere = []
    generate_sphere(sphere, cx, cy, cz, r, step)
    for p in sphere:
        add_edge(points, p[0], p[1], p[2], p[0], p[1], p[2])

def generate_sphere( points, cx, cy, cz, r, step ):
    theta = 0
    phi = 0
    while phi < 1:
        while theta < 1:
            x = r*math.cos(2*math.pi * theta) + cx
            y = r*math.sin(2*math.pi * theta) * math.cos(math.pi * phi) + cy
            z = r*math.sin(2*math.pi * theta) * math.sin(math.pi * phi) + cz
            add_point(points, x, y, z)
            theta += step
        theta = 0
        phi += step

def add_torus( points, cx, cy, cz, r0, r1, step ):
    torus = []
    generate_torus(torus, cx, cy, cz, r0, r1, step)
    for p in torus:
        add_edge(points, p[0], p[1], p[2], p[0], p[1], p[2])

def generate_torus( points, cx, cy, cz, r0, r1, step ):
    theta = 0
    phi = 0
    while phi < 1:
        while theta < 1:
            x = r0 * math.cos(2*math.pi * theta) + cx
            y = math.cos(2*math.pi * phi) * (r0 * math.sin(2*math.pi * theta) + r1) + cy
            z = math.sin(2*math.pi * phi) * (r0 * math.sin(2*math.pi * theta) + r1) + cz
            add_point(points, x, y, z)
            theta += step
        theta = 0
        phi += step

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy

    t = step
    while t<= 1:
        
        x = r * math.cos( 2 * math.pi * t ) + cx
        y = r * math.sin( 2 * math.pi * t ) + cy

        add_edge( points, x0, y0, cz, x, y, cz )
        x0 = x
        y0 = y
        t+= step
    add_edge( points, x0, y0, cz, cx + r, cy, cz )

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xcoefs = generate_curve_coefs( x0, x1, x2, x3, curve_type )
    ycoefs = generate_curve_coefs( y0, y1, y2, y3, curve_type )
        
    t =  step
    while t <= 1:
        
        x = xcoefs[0][0] * t * t * t + xcoefs[0][1] * t * t + xcoefs[0][2] * t + xcoefs[0][3]
        y = ycoefs[0][0] * t * t * t + ycoefs[0][1] * t * t + ycoefs[0][2] * t + ycoefs[0][3]

        add_edge( points, x0, y0, 0, x, y, 0 )
        x0 = x
        y0 = y
        t+= step

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

