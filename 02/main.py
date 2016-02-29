from display import *
from draw import *
from math import pi

screen = new_screen()
color = [ 0, 255, 0 ]

x = 100
y = 100
r = 20

for a in xrange(360):
    matrix = [[],
              [],
              [],
              []]
    add_edge(matrix, x+r, y+r, 0, x+r, y+r, 0)

    theta = a*pi/180
    trans_matrix = matrix_mult(make_translate(x,y,0), make_rotZ(theta))
    trans_matrix = matrix_mult(trans_matrix, make_translate(-x,-y,0))
    matrix = matrix_mult(trans_matrix, matrix)
    draw_lines(matrix, screen, color)
    
display(screen)
