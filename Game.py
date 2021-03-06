import turtle

wn = turtle.Screen()
wn.title('My Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball = turtle.Turtle()
ball.speed()
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# main game loop
while True:
    wn.update()



