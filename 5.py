import turtle

size = int(input("enter size of square : "))

length = int(input("enter length of District of square : "))

color = input("enter color of square : ")

t = turtle.Turtle()

screen = t.getscreen()

t.pencolor(color)

t.pensize(size)

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

screen.mainloop()