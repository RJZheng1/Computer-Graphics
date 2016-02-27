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

m1 = [[1, 3, 5, 7],
      [2, 4, 6, 8]]

m2 = scalar_mult(m1, 2)

print_matrix(m2)

display(screen)
