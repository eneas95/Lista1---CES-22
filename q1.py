import turtle
def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Questão 1")
quad = turtle.Turtle()
size = 20
for i in range(4):
    draw_square(quad,size)
    size = size + 20
    quad.penup()
    quad.goto(quad.position() + (-10,-10))
    quad.pendown()
wn.mainloop()
