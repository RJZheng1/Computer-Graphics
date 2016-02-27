from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = []

add_edge(matrix, 0, 0, 0, 100, 0, 0)
add_edge(matrix, 100, 0, 0, 100, 100, 0)
add_edge(matrix, 100, 100, 0, 0, 100, 0)
add_edge(matrix, 0, 100, 0, 0, 0, 0)
add_point(matrix, 362, 143, 0)
add_point(matrix, 73, 51, 0)

draw_lines(matrix, screen, color)

display(screen)
