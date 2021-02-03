import time

def main():
    didgit = turtle.textinput('PRESS TOKEN', 'WRITE YOUR IDANTIFICATION ID')
    TURTLE_SIZE = 20

    screen = Screen()

    yertle = Turtle(shape="turtle", visible=False)
    yertle.ht()
    circle = turtle.Turtle()
    circle.ht()
    yertle.penup()
    yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
    yertle.pendown()
    yertle.showturtle()
    turtle.write('''
    PENTAGON HACKING
    ''')

    screen = turtle.Screen()

    image = r"F:\10им\original.gif"

    screen.addshape(image)
    turtle.shape(image)
    

    yertle.left(270)
    yertle.forward(300)
    yertle.right(270)
    yertle.forward(350)


    turtle.title("Turtle Drawing")
    circle.shape("turtle")
    circle.pensize(5)
    circle.pencolor("cyan")

    circle.dot(20)
    circle.penup()
    circle.goto(0, -100)
    circle.pendown()
    circle.circle(100)
    screen = turtle.Screen()
    image2 = r"F:\10им\s120.gif"
    
    screen.addshape(image2)
    
    turtle.shape(image2)
    x = turtle.color('red')
    s = '''
        INJECT SUCCESS
        PRESS ANY KEY
    '''
    turtle.write(s, align = 'center', font = (x, 30, 'bold'))
    
    turtle.exitonclick()
    initialization()

a = 'я люблю Полину'
for i in range(1000):
    print(a)
