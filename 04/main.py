from display import *
from draw import *
from parsers import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

if(len(sys.argv) != 2):
    print "Please give only one script file"
else:
    parse_file( sys.argv[1], edges, transform, screen, color )
