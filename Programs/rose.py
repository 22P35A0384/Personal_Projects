import turtle

def halfcircle(parts=360, line=1, direction=1):
    for x in range(parts//2):
        turtle.forward(line)
        turtle.left(360/parts * direction)

turtle.tracer(False)

for x in range(2):
    halfcircle(20, 360/30, 1)
    halfcircle(20, 360/30, -1)

turtle.update() 
