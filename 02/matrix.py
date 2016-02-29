from math import sin, cos

def make_translate( x, y, z ):
    return [[1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]]

def make_scale( x, y, z ):
    return [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]
    
def make_rotX( theta ):
    return [[1, 0, 0, 0],
            [0, cos(theta), -sin(theta), 0],
            [0, sin(theta), cos(theta), 0],
            [0, 0, 0, 1]]

def make_rotY( theta ):
    return [[cos(theta), 0, -sin(theta), 0],
            [0, 1, 0, 0],
            [sin(theta), 0, cos(theta), 0],
            [0, 0, 0, 1]]

def make_rotZ( theta ):
    return [[cos(theta), -sin(theta), 0, 0],
            [sin(theta), cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]
                
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    for x in xrange(len(matrix)):
        s = ''
        for y in xrange(len(matrix[x])):
            s += str(matrix[x][y]) + '\t'
        print s

def ident( matrix ):
    m = new_matrix(len(matrix), len(matrix))
    for i in xrange(len(matrix)):
        m[i][i] = 1
    return m

def scalar_mult( matrix, x ):
    m = new_matrix(len(matrix[0]), len(matrix))
    for r in xrange(len(matrix)):
        for c in xrange(len(matrix[r])):
            m[r][c] = x * matrix[r][c]
    return m
            
def matrix_mult(m1, m2):
    m = new_matrix(len(m2[0]), len(m1))
    for x in xrange(len(m1)):
        for y in xrange(len(m2[0])):
            sum = 0
            for i in xrange(len(m2)):
                sum += m1[x][i] * m2[i][y]
            m[x][y] = sum
    return m
