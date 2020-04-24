import turtle
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Questão 2")
poly = turtle.Turtle()
draw_poly(poly, 8, 50)
wn.mainloop()