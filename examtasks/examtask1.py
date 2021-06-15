from cmath import sin
import pywavefront
from pyglet.gl import *
from pywavefront import visualization, Wavefront
from tkinter import *

window = pyglet.window.Window(width=800, height=600, resizable=False)
rotation = 0.0
mymodel = pywavefront.Wavefront('model2.obj')


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()

    draw_model(mymodel, 0.0, 0.0)


@window.event
def on_resize(width, height):
    viewport_width, viewport_height = window.get_framebuffer_size()
    glViewport(0, 0, viewport_width, viewport_height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45., float(width) / height, 1., 100.)
    glMatrixMode(GL_MODELVIEW)
    return True


def draw_model(mymodel, x, y):
    glLoadIdentity()
    glTranslated(x, y, -40.0)
    glRotatef(rotation, 0.0, 1.0, 0.0)
    glRotatef(-25.0, 1.0, 0.0, 0.0)
    glRotatef(45.0, 0.0, 0.0, 1.0)

    visualization.draw(mymodel)


def update(dt):
    global rotation
    rotation -= 1.35#90.0 * dt

    if rotation > 360.0:
        rotation = 0.0


pyglet.clock.schedule(update)
pyglet.app.run()

# consts
A = 50
e1, e2, e3, e4, e5 = 0.1, 0.1, 0.05, 0.02, 0.05
c1, c2, c3, c4, c5 = 900, 900, 520, 1930, 520
l12, l23, l34, l45 = 240, 130, 118, 10.5
QR1 = QR2 = QR3 = QR4 = 0


def QR5(t):
    return A * (20 + 3 * sin(t / 4))
