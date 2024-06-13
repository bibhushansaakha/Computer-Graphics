import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

win_width, win_height = 800, 800

original_polygon = [(100, 150), (200, 250), (300, 200), (350, 150), (250, 100)]
clip_rect = [150, 100, 300, 250]  # [xmin, ymin, xmax, ymax]

def sutherland_hodgman_clip(polygon, clip_rect):
    def clip_polygon(poly, edge):
        clipped_polygon = []
        x0, y0 = poly[-1]
        for x1, y1 in poly:
            if inside(x1, y1, edge):
                if not inside(x0, y0, edge):
                    clipped_polygon.append(intersect(x0, y0, x1, y1, edge))
                clipped_polygon.append((x1, y1))
            elif inside(x0, y0, edge):
                clipped_polygon.append(intersect(x0, y0, x1, y1, edge))
            x0, y0 = x1, y1
        return clipped_polygon

    def inside(x, y, edge):
        if edge == 'left':
            return x >= xmin
        elif edge == 'right':
            return x <= xmax
        elif edge == 'bottom':
            return y >= ymin
        elif edge == 'top':
            return y <= ymax

    def intersect(x0, y0, x1, y1, edge):
        if edge == 'left':
            x = xmin
            y = y0 + (xmin - x0) * (y1 - y0) / (x1 - x0)
        elif edge == 'right':
            x = xmax
            y = y0 + (xmax - x0) * (y1 - y0) / (x1 - x0)
        elif edge == 'bottom':
            y = ymin
            x = x0 + (ymin - y0) * (x1 - x0) / (y1 - y0)
        elif edge == 'top':
            y = ymax
            x = x0 + (ymax - y0) * (x1 - x0) / (y1 - y0)
        return (x, y)

    xmin, ymin, xmax, ymax = clip_rect
    edges = ['left', 'right', 'bottom', 'top']
    output_polygon = polygon
    for edge in edges:
        output_polygon = clip_polygon(output_polygon, edge)
    return output_polygon

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
    
    window = glfw.create_window(win_width, win_height, "Sutherland-Hodgman Polygon Clipping", None, None)
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
        clipped_polygon = sutherland_hodgman_clip(original_polygon, clip_rect)
        if clipped_polygon:
            draw_polygon(clipped_polygon)
        
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
