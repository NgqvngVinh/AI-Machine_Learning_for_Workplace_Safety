# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# window = 0
# width, height = 500, 400

# def draw():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
# glutInitWindowSize(width, height)
# glutInitWindowPosition(0, 0)
# window = glutCreateWindow("Test")
# glutDisplayFunc(draw)
# glutIdleFunc(draw)
# glutMainLoop()
from OpenGL.GL import *
from OpenGL.GLUT import *

def print_opengl_info():
    glutInit()  # Khởi tạo môi trường OpenGL
    print("OpenGL Version:", glGetString(GL_VERSION))
    print("OpenGL Vendor:", glGetString(GL_VENDOR))
    print("OpenGL Renderer:", glGetString(GL_RENDERER))

print_opengl_info()

