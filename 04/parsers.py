from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r').read().split('\n')
    i = 0
    while i < len(f):
        if f[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif f[i] == "save":
            i += 1
            save_extension(screen, f[i])
        elif f[i] == "apply":
            matrix_mult(transform, points)
        elif f[i] == "line":
            i += 1
            try:
                p = map(lambda x: float(x), f[i].split())
                if len(p) != 6:
                    print "There should only be 6 coordinates to an edge"
                else:
                    add_edge(points, p[0], p[1], p[2], p[3], p[4], p[5]) 
            except ValueError:
                "The coordinates should be numbers"
        elif f[i] == "ident":
            ident(transform)
        elif f[i] == "scale":
            i += 1
            try:
                p = map(lambda x: float(x), f[i].split())
                if len(p) != 3:
                    print "There should only be 3 dimensions to scale"
                else:
                    matrix_mult(make_scale(p[0], p[1], p[2]), transform)
            except ValueError:
                print "You should be scaling by numbers"
        elif f[i] == "translate":
            i += 1
            try:
                p = map(lambda x: float(x), f[i].split())
                if len(p) != 3:
                    print "There should only be 3 dimensions to translate"
                else:
                    matrix_mult(make_translate(p[0], p[1], p[2]), transform)     
            except ValueError:
                print "You should be translating by numbers"
        elif f[i] == "xrotate":
            i += 1
            try:
                p = int(f[i])
                matrix_mult(make_rotX(p), transform)
            except ValueError:
                print "There should only be one angle to rotate by"
        elif f[i] == "yrotate":
            i += 1
            try:
                p = int(f[i])
                matrix_mult(make_rotY(p), transform)
            except ValueError:
                print "There should only be one angle to rotate by"
        elif f[i] == "zrotate":
            i += 1
            try:
                p = int(f[i])
                matrix_mult(make_rotZ(p), transform)
            except ValueError:
                print "There should only be one angle to rotate by"
        elif f[i] == "circle":
            i += 1
            try:
                p = map(lambda x: float(x), f[i].split())
                if len(p) != 3:
                    print "There should only be 3 numbers: cx, cy, and r"
                else:
                    add_circle(points, p[0], p[1], 0, p[2], 100)
            except ValueError:
                print "The values should be numbers"
        elif f[i] == "hermite":
            i += 1
            try:
                p = map(lambda x: float(x), f[i].split())
                if len(p) != 8:
                    print "There should only be 8 numbers"
                else:
                    add_curve(points, p[0], p[1], p[4], p[5], p[2]-p[0], p[3]-p[1], p[6]-p[4], p[7]-p[5], 100, 0)
            except ValueError:
                print "The values should be numbers"
        elif f[i] == "bezier":
            i += 1
            try:
                p = map(lambda x: float(x), f[i].split())
                if len(p) != 8:
                    print "There should only be 8 numbers"
                else:
                    add_curve(points, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], 100, 1)
            except ValueError:
                print "The values should be numbers"
        elif f[i] == "exit":
            break
        i += 1
