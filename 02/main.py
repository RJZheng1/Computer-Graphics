from display import *
from draw import *
from math import pi

screen = new_screen()
color = [ 0, 255, 0 ]

edge = [[],
     [],
     [],
     []]

x = XRES/2
y = YRES/2
r = 100

for a in xrange(720):
    matrix = [[],
              [],
              [],
              []]
    add_edge(matrix, x, y+r+r, 0, x, y+r+r, 0)
    theta = a*pi/360
    trans_matrix = matrix_mult(
        matrix_mult(make_translate(x,y+r,0), make_rotZ(theta)),
        make_translate(-x,-y-r,0))
    matrix = matrix_mult(trans_matrix, matrix)
    edge[0].extend(matrix[0])
    edge[1].extend(matrix[1])
    edge[2].extend(matrix[2])
    edge[3].extend(matrix[3])
    
for a in xrange(6):
    trans_matrix = matrix_mult(
        matrix_mult(make_translate(x,y,0), make_rotZ(pi/3)),
        make_translate(-x,-y,0))
    edge = matrix_mult(trans_matrix, edge)
    draw_lines(edge, screen, color)

display(screen)

print_matrix(edge)
