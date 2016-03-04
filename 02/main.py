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
numAng = 720

for a in xrange(numAng):
    matrix = [[x],
              [y+r+r],
              [0],
              [1]]
    trans_matrix = matrix_mult(
        matrix_mult(make_translate(x,y+r,0), make_rotZ(a*2*pi/numAng)),
        make_translate(-x,-y-r,0))
    matrix = matrix_mult(trans_matrix, matrix)
    edge[0].append(matrix[0][0])
    edge[1].append(matrix[1][0])
    edge[2].append(matrix[2][0])
    edge[3].append(matrix[3][0])

numAng = 90

for a in xrange(numAng):
    trans_matrix = matrix_mult(
        matrix_mult(make_translate(x,y,0), make_rotZ(2*pi/numAng)),
        make_translate(-x,-y,0))
    edge = matrix_mult(trans_matrix, edge)
    draw_lines(edge, screen, color)

display(screen)
