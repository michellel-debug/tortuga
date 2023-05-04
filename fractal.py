import turtle

tu = turtle.Turtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color("green")

tu.left(90)
tu.backward(100)
tu.speed(200)
tu.shape("turtle")

def tree(i):
    if i<10:
        return
    
    else:
        tu.forward(i)
        tu.color("orange")
        tu.circle(2)
        tu.color("brown")
        




turtle(100)
turtle.done()