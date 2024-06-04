import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_mountains():
    glColor3f(54/255, 60/255, 146/255)  # blue
    glBegin(GL_TRIANGLES)
    glVertex2f(680/1280*2-1, 414/720*2-1)
    glVertex2f(295/1280*2-1, 776/720*2-1)
    glVertex2f(1067/1280*2-1, 776/720*2-1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(928/1280*2-1, 564/720*2-1)
    glVertex2f(563/1280*2-1, 834/720*2-1)
    glVertex2f(1292/1280*2-1, 834/720*2-1)
    glEnd()

def draw_snow():
    glColor3f(1, 1, 1)  # white
    glBegin(GL_TRIANGLES)
    glVertex2f(680/1280*2-1, 432/720*2-1)
    glVertex2f(590/1280*2-1, 522/720*2-1)
    glVertex2f(770/1280*2-1, 522/720*2-1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(928/1280*2-1, 599/720*2-1)
    glVertex2f(630/1280*2-1, 843/720*2-1)
    glVertex2f(1226/1280*2-1, 843/720*2-1)
    glEnd()

def draw_stupa():
    glColor3f(54/255, 60/255, 146/255)  # blue
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(418/1280*2-1, 1024/720*2-1)
    for i in range(360):
        angle = i * 3.14159265 / 180
        glVertex2f(418/1280*2-1 + cos(angle) * 437/1280*2, 1024/720*2-1 + sin(angle) * 437/720*2)
    glEnd()

def draw_face():
    glColor3f(54/255, 60/255, 146/255)  # blue
    glBegin(GL_QUADS)
    glVertex2f(291/1280*2-1, 439/720*2-1)
    glVertex2f(291/1280*2-1, 611/720*2-1)
    glVertex2f(494/1280*2-1, 611/720*2-1)
    glVertex2f(494/1280*2-1, 439/720*2-1)
    glEnd()

def draw_shrine():
    glColor3f(54/255, 60/255, 146/255)  # blue
    glBegin(GL_TRIANGLES)
    glVertex2f(393/1280*2-1, -17/720*2-1)
    glVertex2f(296/1280*2-1, 441/720*2-1)
    glVertex2f(489/1280*2-1, 441/720*2-1)
    glEnd()

def draw_head_top():
    glColor3f(221/255, 0, 39/255)  # red
    glBegin(GL_TRIANGLES)
    glVertex2f(393/1280*2-1, 370/720*2-1)
    glVertex2f(337/1280*2-1, 441/720*2-1)
    glVertex2f(449/1280*2-1, 441/720*2-1)
    glEnd()

def draw_head_hat():
    glColor3f(221/255, 0, 39/255)  # red
    glBegin(GL_QUADS)
    glVertex2f(281/1280*2-1, 439/720*2-1)
    glVertex2f(281/1280*2-1, 466/720*2-1)
    glVertex2f(504/1280*2-1, 466/720*2-1)
    glVertex2f(504/1280*2-1, 439/720*2-1)
    glEnd()

def draw_text():
    glColor3f(1, 1, 1)  # white
    glBegin(GL_QUADS)
    glVertex2f(19/1280*2-1, 834/720*2-1)
    glVertex2f(19/1280*2-1, 984/720*2-1)
    glVertex2f(64/1280*2-1, 984/720*2-1)
    glVertex2f(64/1280*2-1, 834/720*2-1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(167/1280*2-1, 834/720*2-1)
    glVertex2f(167/1280*2-1, 984/720*2-1)
    glVertex2f(212/1280*2-1, 984/720*2-1)
    glVertex2f(212/1280*2-1, 834/720*2-1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(370/1280*2-1, 834/720*2-1)
    glVertex2f(370/1280*2-1, 984/720*2-1)
    glVertex2f(419/1280*2-1, 984/720*2-1)
    glVertex2f(419/1280*2-1, 834/720*2-1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(300/1280*2-1, 834/720*2-1)
    glVertex2f(300/1280*2-1, 871/720*2-1)
    glVertex2f(489/1280*2-1, 871/720*2-1)
    glVertex2f(489/1280*2-1, 834/720*2-1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(579/1280*2-1, 834/720*2-1)
    glVertex2f(579/1280*2-1, 984/720*2-1)
    glVertex2f(627/1280*2-1, 984/720*2-1)
    glVertex2f(627/1280*2-1, 834/720*2-1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(709/1280*2-1, 834/720*2-1)
    glVertex2f(709/1280*2-1, 984/720*2-1)
    glVertex2f(755/1280*2-1, 984/720*2-1)
    glVertex2f(755/1280*2-1, 834/720*2-1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(62.5/1280*2-1, 835.5/720*2-1)
    glVertex2f(170.5/1280*2-1, 923.5/720*2-1)
    glVertex2f(173.5/1280*2-1, 982.5/720*2-1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(62.5/1280*2-1, 835.5/720*2-1)
    glVertex2f(62.5/1280*2-1, 900.5/720*2-1)
    glVertex2f(173.5/1280*2-1, 982.5/720*2-1)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_mountains()
    draw_snow()
    draw_stupa()
    draw_face()
    draw_shrine()
    draw_head_top()
    draw_head_hat()
    draw_text()
    pygame.display.flip()

def main():
    pygame.init()
    display = (1080, 1080)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()

if __name__ == "__main__":
    main()

