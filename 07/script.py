import mdl
from display import *
from matrix import *
from draw import *
from copy import deepcopy

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
    
    for command in commands:
        if command[0] == 'push':
            stack.append(deepcopy(stack[-1]))
            
        elif command[0] == 'pop':
            stack.pop()
            
        elif command[0] == 'move':
                t = make_translate( command[1], command[2], command[3] )
                matrix_mult( stack[-1], t )
                stack[-1] = t

        elif command[0] == 'rotate':
            angle = command[2] * ( math.pi / 180 )
            if command[1] == 'x':
                r = make_rotX( angle )
            elif command[1] == 'y':
                r = make_rotY( angle )
            else:
                r = make_rotZ( angle )
            matrix_mult( stack[-1], r )
            stack[-1] = r

        elif command[0] == 'scale':
                s = make_scale( command[1], command[2], command[3] )
                matrix_mult( stack[-1], s )
                stack[-1] = s
                
        elif command[0] == 'box':
            pass
            
        elif command[0] == 'sphere':
            pass

        elif command[0] == 'torus':
            pass

        elif command[0] == 'line':
            pass

        elif command[0] == 'circle':
            pass

        elif command[0] == 'bezier':
            pass

        elif command[0] == 'hermite':
            pass
        
        elif command[0] == 'save':
            save_extension(screen, commands[1])

        elif command[0] == 'display':
            display(screen)
            screen = new_screen()

        elif command[0] == 'quit':
            return

        else:
            print command
