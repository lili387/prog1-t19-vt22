from math import sin,cos,pi
import random

dt = 0.005
t = 0
x = []
y = []
theta = []
num_points = 100

def setup():
    global x, y, theta, num_points
    size(600,600) 
    for n in range(num_points):
        t = 2*pi/num_points*n
        theta.append(t)
        x.append(cos(t)*100+300) 
        y.append(sin(t)*100+300)
        
def draw():
    global t, dt, x, y, theta, num_points
    t += dt
    
    #background(3);
    
    stroke(0, 125, 255, 10)

    Dr = []
    for t in range(num_points):
        dr = random.random()*10-4.85
        Dr.append(dr)

    for t in range(num_points):
        dr = 0
        for k in range(-2,2+1):
            dr += Dr[(t-k)%num_points]
        dr = dr/5
        x[t] += cos(theta[t])*dr
        y[t] += sin(theta[t])*dr

    for k in range(num_points):
        line(x[k%num_points],y[k%num_points],x[(1+k)%num_points],y[(1+k)%num_points])
        
