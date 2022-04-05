import random
circles = [{"radius":0.05, "pos_x":0.5, "pos_y":0.5}]
size_x = 600
size_y = 600

def draw_circle(circ):
    pixel_x = 600.0*circ["pos_x"]
    pixel_y = 600.0*circ["pos_y"]
    pixel_diameter = 600*circ["radius"]*2
    circle(pixel_x, pixel_y, pixel_diameter)

def split_circle(circ):
    new_circle1 = {"radius":circ["radius"]*(random.random()+2)/3, "pos_x":circ["pos_x"] + (random.random()-0.5)/5, "pos_y":circ["pos_y"] + (random.random()-0.5)/5}
    new_circle2 = {"radius":circ["radius"]*(random.random()+2)/3, "pos_x":circ["pos_x"] + (random.random()-0.5)/5, "pos_y":circ["pos_y"] + (random.random()-0.5)/5}
    return [new_circle1, new_circle2]

def find_clicked_circles(click_x, click_y):
    clicked_circles = []
    for circ in circles:
        if (click_x - circ["pos_x"])**2 + (click_y - circ["pos_y"])**2 < circ["radius"]**2:
            clicked_circles.append(circ)
    return clicked_circles

def handle_mouse_click(pos_x, pos_y):
    global circles
    for clicked_circle in find_clicked_circles(pos_x, pos_y):
        circles.remove(clicked_circle)
        for circle_to_add in split_circle(clicked_circle):
            circles.append(circle_to_add)

def setup():
    global size_x, size_y
    size(600,600)
    
def draw():
    background(90,90,90)
    stroke(255, 255, 255, 80)
    fill(255, 255, 255,80)
    for circle in circles:
        draw_circle(circle)


def mouseClicked(): 
    pos_x = mouseX/600.0
    pos_y = mouseY/600.0
    handle_mouse_click(pos_x, pos_y)
