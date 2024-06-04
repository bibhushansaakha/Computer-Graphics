import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

win_width, win_height = 800, 800

def MidPointEllipse(x_center, y_center, rx, ry):
    points = []
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    
    # Initial decision parameter for region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    
    # Region 1
    while tworx2 * y > twory2 * x:
        points.extend([(x_center + x, y_center + y), (x_center - x, y_center + y), 
                       (x_center + x, y_center - y), (x_center - x, y_center - y)])
        if p1 < 0:
            x += 1
            p1 += twory2 * x + ry2
        else:
            x += 1
            y -= 1
            p1 += twory2 * x - tworx2 * y + ry2
    
    # Initial decision parameter for region 2
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    
    # Region 2
    while y >= 0:
        points.extend([(x_center + x, y_center + y), (x_center - x, y_center + y), 
                       (x_center + x, y_center - y), (x_center - x, y_center - y)])
        if p2 > 0:
            y -= 1
            p2 -= tworx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += twory2 * x - tworx2 * y + rx2
    
    return points

def draw_ellipse(x_center, y_center, rx, ry):
    points = MidPointEllipse(x_center, y_center, rx, ry)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

def main():
    # Initialize glfw
    if not glfw.init():
        return
    
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(win_width, win_height, "Midpoint Ellipse", None, None)
    if not window:
        glfw.terminate()
        return
    
    # Make the window's context current
    glfw.make_context_current(window)
    
    # Set viewport and projection
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, win_width, 0, win_height)
    
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)
        draw_ellipse(400, 400, 300, 150)
        
        # Swap front and back buffers
        glfw.swap_buffers(window)
        
        # Poll for and process events
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
