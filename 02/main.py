from display import *
from draw import *
from math import pi

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = [[],
          [],
          [],
          []]

add_edge(matrix, 0, 0, 0, 100, 0, 0)
add_edge(matrix, 100, 0, 0, 100, 100, 0)
add_edge(matrix, 100, 100, 0, 0, 100, 0)
add_edge(matrix, 0, 100, 0, 0, 0, 0)

matrix = matrix_mult(make_translate(200, 200, 0), matrix)

matrix = matrix_mult(make_rotZ(pi/12), matrix)

print_matrix(ident(matrix))

draw_lines(matrix, screen, color)

display(screen)
