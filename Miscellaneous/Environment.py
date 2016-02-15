'''
    In Order to import OpenGL go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl

    If you have 32bit pyhton version 2.7 download PyOpenGL-3.1.1b1-cp27-none-win32.whl

    If you have 64bit pyhton version 2.7 download PyOpenGL-3.1.1b1-cp27-none-win_amd64.whl

    Start cmd .exe cd to the directory where the "PyOpenGL-3.1.1b1.........whl" file is

    in cmd type the command python -m pip install PyOpenGL-3.1.1b1.........whl
                                                  ^(the name of your specific file)
'''
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import sys


def display():
    glut.glutSwapBuffers()

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == '\033':
        sys.exit( )

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
glut.glutCreateWindow('Hello world!')
glut.glutReshapeWindow(512,512)
glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()