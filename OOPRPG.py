import turtle

wn = turtle.Screen()
wn.bgcolor('red')
wn.title('Turtle Python Graphics Game Using Classes')

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape('triangle')
        self.color('white')
        self.speed = 1 #not a property of turtle

    def move(self):
        self.forward(self.speed)


player = Player() #class instance

#main loop
while True:
    player.move()


