import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

win_width, win_height = 800, 800

original_polygon = [(100, 150), (200, 250), (300, 200), (350, 150), (250, 100)]
clip_rect = [150, 100, 300, 250]  # [xmin, ymin, xmax, ymax]

def liang_barsky_clip(x0, y0, x1, y1, clip_rect):
    xmin, ymin, xmax, ymax = clip_rect
    dx = x1 - x0
    dy = y1 - y0

    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > u1:
                    u1 = t
            else:
                if t < u2:
                    u2 = t

    if u1 > u2:
        return None

    clipped_x0 = x0 + u1 * dx
    clipped_y0 = y0 + u1 * dy
    clipped_x1 = x0 + u2 * dx
    clipped_y1 = y0 + u2 * dy

    return (clipped_x0, clipped_y0, clipped_x1, clipped_y1)

def clip_polygon_with_liang_barsky(polygon, clip_rect):
    clipped_polygon = []
    for i in range(len(polygon)):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % len(polygon)]
        clipped_line = liang_barsky_clip(x0, y0, x1, y1, clip_rect)
        if clipped_line:
            clipped_polygon.append((clipped_line[0], clipped_line[1]))
            clipped_polygon.append((clipped_line[2], clipped_line[3]))
    return clipped_polygon

def draw_polygon(polygon):
    glBegin(GL_POLYGON)
    for x, y in polygon:
        glVertex2f(x, y)
    glEnd()

def draw_clipping_region():
    xmin, ymin, xmax, ymax = clip_rect
    glColor3f(0, 1, 0)  # Green color
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window(win_width, win_height, "Liang-Barsky Polygon Clipping", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, win_width, 0, win_height)
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        draw_clipping_region()
        
        glColor3f(1, 0, 0)  # Red color
        draw_polygon(original_polygon)
        
        glColor3f(0, 0, 1)  # Blue color
        clipped_polygon = clip_polygon_with_liang_barsky(original_polygon, clip_rect)
        if clipped_polygon:
            draw_polygon(clipped_polygon)
        
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
