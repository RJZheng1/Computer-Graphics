from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r').read().split('\n')
    i = 0
    while i < len(f):
        if f[i] == "line":
            i += 1
            p = map(lambda x: int(x), f[i].split())
            if len(p) != 6:
                pass
            else:
                add_edge(points, p[0], p[1], p[2], p[3], p[4], p[5]) 
        elif f[i] == "display":
            pass
        elif f[i] == "ident":
            pass
        elif f[i] == "scale":
            pass
        elif f[i] == "apply":
            pass
        elif f[i] == "translate":
            pass
        elif f[i] == "xrotate":
            pass
        elif f[i] == "yrotate":
            pass
        elif f[i] == "zrotate":
            pass
        elif f[i] == "save":
            pass
        elif f[i] == "display":
            pass
        i += 1
    

