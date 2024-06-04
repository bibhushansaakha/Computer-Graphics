import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

win_width, win_height = 800, 800

def MidPointCircle(x_center, y_center, r):
    points = []
    x = 0
    y = r
    P = 1 - r
    
    while x <= y:
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))
        points.append((x_center + y, y_center + x))
        points.append((x_center - y, y_center + x))
        points.append((x_center + y, y_center - x))
        points.append((x_center - y, y_center - x))
        
        if P < 0:
            P = P + 2 * (x + 1) + 1
        else:
            P = P + 2 * (x + 1) + 1 - 2 * (y - 1)
            y -= 1
        
        x += 1
    
    return points

def draw_circle(x_center, y_center, radius):
    points = MidPointCircle(x_center, y_center, radius)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

def main():
    # Initialize glfw
    if not glfw.init():
        return
    
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(win_width, win_height, "Mid-Point Circle Drawing", None, None)
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
        #glClear(GL_COLOR_BUFFER_BIT)
        draw_circle(100, 100, 50)
        
        # Swap front and back buffers
        glfw.swap_buffers(window)
        
        # Poll for and process events
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
