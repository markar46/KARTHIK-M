## Written by Scott Pflaumer ##

from __future__ import division
from vpython import *


m = 5           ## see the effect of making the box more/less massive
vi = 9         ##magnitude of initial velocity

g = -9.8         #gravitational frield strength

theta = 45       ## try changing this angle (degrees) to make a new ramp
L = 10            ##ramp length
W = 10            ##ramp width
H = .5            ##ramp thickness
l = 1             ## box length
w = 1             ## box width
h = 1             ## box height

vscale=.6

scene.range = 2*L

##change the code in this section at your own risk - this is the ramp code
xaxis = cylinder(pos=vec(0,0,0), axis=vec(2*L,0,0), radius=.1)
yaxis = cylinder(pos=vec(0,0,0), axis=vec(0,2*L,0), radius=.1)
zaxis = cylinder(pos=vec(0,0,0), axis=vec(0,0,2*L), radius=.1)

ramp = box(pos= vec(0, sin(theta*2*pi/360)*L/2, 0), length = L, width = W, height = H, axis= vec(cos(theta*2*pi/360), sin(theta*2*pi/360), 0), color=color.white)
rampbase = box(pos= vec(0, 0, 0), length = L*cos(theta*2*pi/360), width = W, height = H, color=color.white)
rampside = box(pos= vec((L*cos(theta*2*pi/360)/2), sin(theta*2*pi/360)*L/2-.00*L, 0), length = H/5, width = W, height = sin(theta*2*pi/360)*L, color=color.white)

box = box(pos= vec(0, (L*sin(theta*2*pi/360)*L*cos(theta*2*pi/360)*.5/(L*cos(theta*2*pi/360))+ h/2 + H/2), 0), length = l, width =w, height = h, axis = ramp.axis, color=color.blue)   #creates the box and it's physical attributes
##end of no edit zone


box.velocity = vector (vi*cos(theta*2*pi/360), vi*sin(theta*2*pi/360), 3) #calculates the initial box velocity in 3D with a vector in the form (x, y, z)

a = vector(sin(theta*2*pi/360)*cos(theta*2*pi/360)*g, sin(theta*2*pi/360)*sin(theta*2*pi/360)*g, 0)#calculates the initial box acceleration


varrow = arrow(pos=box.pos, axis=vscale*box.velocity, color=color.green)
farrow = arrow(pos=box.pos, axis=vscale*a, color=color.red)

box.trail = curve(color=box.color)


t = 0
dt = .001



while (box.pos.x < (L*cos(theta*2*pi/360))/2) and (abs(box.pos.y) < W/2):      #this loop determines the box positionk, velocity, and acceleration on the ramp
    rate(200)            #slows the computer down to 200 calculations per second

    box.velocity = box.velocity + a*dt               #updates velocity
    box.pos = box.pos + box.velocity*dt              #updates position

    varrow.pos = box.pos                             #updates velocity arrow position
    farrow.pos = box.pos                             #updates force or accelerion arrow position

    varrow.axis = vscale*box.velocity                #updates velocity arrow size and direction
    farrow.axis = vscale*a                           #updates force/acceleration arrow size and direction

    box.trail.append(pos=box.pos)
        
    t = t + dt




while True:           #this loop calculats the box position, velocity, and acceleration once it becomes a projectile
    rate(200)

    box.velocity = box.velocity + vector(0, g, 0)*dt        #updates velocity
    box.pos = box.pos + box.velocity*dt                     #updates position

    varrow.pos = box.pos                                    #updates velocity arrow position
    farrow.pos = box.pos                                    #updates force or accelerion arrow position

    varrow.axis = box.velocity                              #updates velocity arrow size and direction
    farrow.axis = vscale*vector(0, g, 0)                    #updates force/acceleration arrow size and direction

    box.trail.append(pos=box.pos)