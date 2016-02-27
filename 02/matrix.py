import math

def make_translate( x, y, z ):
    pass

def make_scale( x, y, z ):
    pass
    
def make_rotX( theta ):   
    pass

def make_rotY( theta ):
    pass

def make_rotZ( theta ):
    pass

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
    pass

def scalar_mult( matrix, x ):
    pass

def matrix_mult(m1, m2):
    m = new_matrix(len(m2[0]), len(m1))
    for x in xrange(len(m1)):
        for y in xrange(len(m2[0])):
            sum = 0
            for i in xrange(len(m2)):
                sum += m1[x][i] * m2[i][y]
            m[x][y] = sum
    return m
