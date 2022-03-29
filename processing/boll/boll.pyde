from math import sin,cos,pi
import random

dt = 0.1
t = 0

x = 300
y = 300
vx = 20 
vy = 0

theta = []
num_points = 100

def setup():
    global x, y, theta, num_points
    size(600,600) 
        
def draw():
    global t, dt, x, y, vx, vy 
    t += dt
    
    x += vx*dt
    y += vy*dt
    
    vy += 9.82*dt
    
    if x<100:
        vx = abs(vx)*0.95
    elif x>500:
        vx = -abs(vx)*0.95
    
    if y>500:
        vy = -abs(vy)*0.95
    #background(3);
    
    stroke(0, 125, 255, 50)
    fill(0, 125, 255, 20)
    circle(x,y,10)
        
