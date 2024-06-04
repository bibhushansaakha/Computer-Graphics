import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

win_width, win_height = 800, 800

def liang_barsky_clip(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    dx = x1 - x0
    dy = y1 - y0
    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Parallel and outside
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > u2:
                    return None  # No intersection
                u1 = max(u1, t)
            else:
                if t < u1:
                    return None  # No intersection
                u2 = min(u2, t)

    if u1 > u2:
        return None  # No intersection
    
    x_clip_start = x0 + u1 * dx
    y_clip_start = y0 + u1 * dy
    x_clip_end = x0 + u2 * dx
    y_clip_end = y0 + u2 * dy
    
    return (x_clip_start, y_clip_start, x_clip_end, y_clip_end)

def draw_line(x0, y0, x1, y1):
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()

def draw_shape(points):
    glBegin(GL_LINE_LOOP)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window(win_width, win_height, "Liang-Barsky Line Clipping", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, win_width, 0, win_height)
    
    # Example line and clipping window
    x0, y0 = 50, 50
    x1, y1 = 300, 300
    xmin, ymin = 100, 100
    xmax, ymax = 200, 200
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Draw clipping window
        draw_shape([(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)])
        
        # Draw original line
        draw_line(x0, y0, x1, y1)
        
        # Draw clipped line using Liang-Barsky
        clipped_line = liang_barsky_clip(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
        if clipped_line:
            glColor3f(1.0, 0.0, 0.0)  # Red color for clipped line
            draw_line(clipped_line[0], clipped_line[1], clipped_line[2], clipped_line[3])
            glColor3f(1.0, 1.0, 1.0)  # Reset to white
        
        # Swap front and back buffers
        glfw.swap_buffers(window)
        
        # Poll for and process events
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
