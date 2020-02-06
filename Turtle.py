import pygame
import queue
from math import sin, cos, radians


class Turtle:
	
	# Turtle is a Turtle-Graphics Implementation in python on the pygame platform.
	# In Initializaton, it takes a pygame surface as its input and an initial location for where to
	# start writing/drawing from.
	# It has optional Arguments too:
	# 1- strk (means stroke) is the color of the stroke, default is full green.
	# 2- stroke_w means stroke_width, its the width of the line drawn.

	# Methods:
	# 	translate:

	# 	You can change the location of Turtle (The pen thats drawing the line) directly from
	# 	one (x, y) to another using this function.

	# 	push/pop:

	# 	The moment at which you the function pop, the current location of the turtle are stored
	# 	with pop you can get them back. you can call push and pop in nested form. Its storage
	# 	mechanism is a LIFO-Queue.

	# 	draw_forward/draw_backward:

	# 	These two functions are the ones drawing stuff, they work exactly as the names suggests
	# 	the parammeter of the function mag means Magnitude (in pixels).

	# 	rotate:

	# 	Use this function to rotate the head of the turtle around in degrees.

	# 	stroke/stroke_width:

	# 	Use these to functions to change the color and the width of the line being drawn respectively.


    def __init__(self, surface, x, y, strk=(0, 255, 0), stroke_w=2):
        self.x = x
        self.y = y
        self.surface = surface
        self.angle = radians(-90)
        self.strk = strk  #  Stroke
        self.state = queue.LifoQueue(-1)  # The LIFO queue to store turtle location
        self.stroke_w = stroke_w  #  Stroke width

    def translate(self, loc: tuple):
        self.x = loc[0]
        self.y = loc[1]

    def rotate(self, byAngle: float):
        self.angle += radians(byAngle)

    def push(self):
        self.state.put((self.x, self.y, self.angle, self.stroke_w))

    def pop(self):
        self.x, self.y, self.angle, self.stroke_w = self.state.get()

    def draw_forward(self, mag: float):
        end = (self.x + mag*cos(self.angle), self.y + mag*sin(self.angle))
        pygame.draw.line(self.surface, self.strk, (self.x, self.y), end, self.stroke_w)
        self.x = end[0]
        self.y = end[1]

    def draw_backward(self, mag: float):
        end = (self.x - mag*cos(self.angle), self.y - mag*sin(self.angle))
        pygame.draw.line(self.surface, self.strk, (self.x, self.y), end, self.stroke_w)
        self.x = end[0]
        self.y = end[1]

    def stroke_width(self, val: float):
    	self.stroke_w = val

    def stroke(self, val: int):
    	self.strk = val

