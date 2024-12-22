# # # # # from OpenGL.GL import *
# # # # # from OpenGL.GLUT import *
# # # # # from OpenGL.GLU import *

# # # # # def draw():
# # # # #     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# # # # #     glBegin(GL_TRIANGLES)
# # # # #     glVertex2f(-0.5, -0.5)
# # # # #     glVertex2f(0.5, -0.5)
# # # # #     glVertex2f(0.0, 0.5)
# # # # #     glEnd()
# # # # #     glutSwapBuffers()

# # # # # glutInit()
# # # # # glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# # # # # glutInitWindowSize(800, 600)
# # # # # glutCreateWindow(b"Test Window")
# # # # # glutDisplayFunc(draw)
# # # # # glutMainLoop()


# # # # from OpenGL.GLUT import glutInit, glutCreateWindow, glutMainLoop

# # # # glutInit()
# # # # glutCreateWindow(b"Test Window")
# # # # glutMainLoop()

# # # from OpenGL.GLUT import glutInit, glutCreateWindow, glutMainLoop

# # # def display():
# # #     pass

# # # try:
# # #     glutInit()
# # #     glutCreateWindow(b"Test Window")
# # #     glutMainLoop()
# # # except OpenGL.error.NullFunctionError as e:
# # #     print(f"Error: {e}")
# # #     print("FreeGLUT might not be correctly installed or linked.")


# from OpenGL.GLUT import glutInit, glutCreateWindow, glutMainLoop

# glutInit()
# glutCreateWindow(b"Test Window")
# glutMainLoop()

from OpenGL.GLUT import glutInit

if not callable(glutInit):
    print("glutInit không sẵn có, cho thấy rằng FreeGLUT không được cài đặt hoặc liên kết đúng cách.")
else:
    print("glutInit sẵn sàng.")

# from OpenGL.GL import *
# from OpenGL.GLUT import *

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glBegin(GL_TRIANGLES)
#     glVertex2f(-0.5, -0.5)
#     glVertex2f(0.5, -0.5)
#     glVertex2f(0.0, 0.5)
#     glEnd()
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# glutInitWindowSize(800, 600)
# glutCreateWindow(b"Test Window")
# glutDisplayFunc(display)
# glutMainLoop()

from OpenGL.GLUT import glutInit

if not callable(glutInit):
    print("glutInit function is not properly linked.")
else:
    print("glutInit function is linked and callable.")

from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Minimal Test Window")
glutDisplayFunc(display)
glutMainLoop()


import ctypes

try:
    ctypes.CDLL("freeglut.dll")
    print("freeglut.dll loaded successfully")
except OSError as e:
    print(f"Failed to load freeglut.dll: {e}")
