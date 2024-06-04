import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

win_width, win_height = 800, 800

def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    return apply_transformation(points, translation_matrix)

def rotate(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad), 0],
                                [np.sin(rad), np.cos(rad), 0],
                                [0, 0, 1]])
    return apply_transformation(points, rotation_matrix)

def scale(points, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    return apply_transformation(points, scaling_matrix)

def shear(points, shx, shy):
    shearing_matrix = np.array([[1, shx, 0],
                                [shy, 1, 0],
                                [0, 0, 1]])
    return apply_transformation(points, shearing_matrix)

def apply_transformation(points, matrix):
    transformed_points = []
    for x, y in points:
        vec = np.array([x, y, 1])
        result = matrix @ vec
        transformed_points.append((result[0], result[1]))
    return transformed_points

def draw_shape(points):
    glBegin(GL_LINE_LOOP)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window(win_width, win_height, "2D Transformations", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, win_width, 0, win_height)
    
    points = [(100, 100), (200, 100), (200, 200), (100, 200)]  # Example shape: square
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Original shape
        draw_shape(points)
        
        composite_transformation = translate(rotate(translate(points, -100, -100), 30), 100, 100)
        
        draw_shape(composite_transformation)
        
        scaled_points = scale(points, 2, 2)
        draw_shape(scaled_points)

        translated_points = translate(points, 400, 200)
        draw_shape(translated_points)

        sheared_points = shear(points, 0.5, 0)  
        draw_shape(sheared_points)
        
        sheared_points = shear(points, 0, 0.5)  
        draw_shape(sheared_points)

        # Swap front and back buffers
        glfw.swap_buffers(window)
        
        # Poll for and process events
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
