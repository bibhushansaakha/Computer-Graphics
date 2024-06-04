import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

win_width, win_height = 800, 800

def sutherland_hodgman_clip(subject_polygon, clip_polygon):
    def inside(p, edge_start, edge_end):
        return (edge_end[0] - edge_start[0]) * (p[1] - edge_start[1]) > (edge_end[1] - edge_start[1]) * (p[0] - edge_start[0])

    def compute_intersection(p1, p2, edge_start, edge_end):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = edge_start
        x4, y4 = edge_end

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

    def clip(subject_polygon, edge_start, edge_end):
        clipped_polygon = []
        for i in range(len(subject_polygon)):
            current_vertex = subject_polygon[i]
            prev_vertex = subject_polygon[i - 1]
            inside_current = inside(current_vertex, edge_start, edge_end)
            inside_prev = inside(prev_vertex, edge_start, edge_end)
            if inside_current:
                if not inside_prev:
                    intersection = compute_intersection(prev_vertex, current_vertex, edge_start, edge_end)
                    clipped_polygon.append(intersection)
                clipped_polygon.append(current_vertex)
            elif inside_prev:
                intersection = compute_intersection(prev_vertex, current_vertex, edge_start, edge_end)
                clipped_polygon.append(intersection)
        return clipped_polygon

    clipped_polygon = subject_polygon[:]
    for i in range(len(clip_polygon)):
        edge_start = clip_polygon[i]
        edge_end = clip_polygon[(i + 1) % len(clip_polygon)]
        clipped_polygon = clip(clipped_polygon, edge_start, edge_end)
    
    return clipped_polygon

def draw_shape(points):
    glBegin(GL_LINE_LOOP)
    for x, y in points:
        glVertex2f(x, y)
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
    
    # Example polygon and clipping window
    subject_polygon = [(150, 150), (250, 150), (250, 250), (150, 250)]
    clip_polygon = [(100, 100), (200, 100), (200, 200), (100, 200)]
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Draw clipping window
        glColor3f(0.0, 1.0, 0.0)  # Green color for clipping window
        draw_shape(clip_polygon)
        
        # Draw original polygon
        glColor3f(1.0, 1.0, 1.0)  # White color for original polygon
        draw_shape(subject_polygon)
        
        # Draw clipped polygon using Sutherland-Hodgman
        clipped_polygon = sutherland_hodgman_clip(subject_polygon, clip_polygon)
        if clipped_polygon:
            glColor3f(1.0, 0.0, 0.0)  # Red color for clipped polygon
            draw_shape(clipped_polygon)
            glColor3f(1.0, 1.0, 1.0)  # Reset to white
        
        # Swap front and back buffers
        glfw.swap_buffers(window)
        
        # Poll for and process events
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
