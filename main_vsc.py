import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(width=400, height=600)
screen.title("Space Escape Game")
screen.bgpic("background.gif")  # Use GIF for background

# Register custom GIF shapes
spaceship_img = "spaceship.gif"
asteroid_img = "asteroid.gif"
blast_img = "blast.gif"

screen.register_shape(spaceship_img)
screen.register_shape(asteroid_img)
screen.register_shape(blast_img)

# Create spaceship turtle
spaceship = turtle.Turtle()
spaceship.shape(spaceship_img)
spaceship.penup()
spaceship.goto(0, -250)

# Create asteroid turtle
asteroid = turtle.Turtle()
asteroid.shape(asteroid_img)
asteroid.penup()
asteroid.goto(0, 250)
asteroid.speed(0)

# Movement functions
def move_right():
    x = spaceship.xcor()
    if x < 180:
        spaceship.setx(x + 20)

def move_left():
    x = spaceship.xcor()
    if x > -180:
        spaceship.setx(x - 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Reset asteroid if it crosses the bottom
def reset_asteroid():
    if asteroid.ycor() < -300:
        x = random.randint(-170, 170)
        asteroid.hideturtle()
        asteroid.goto(x, 300)
        asteroid.showturtle()

# Game loop function
def update():
    if spaceship.shape() != blast_img:
        asteroid.sety(asteroid.ycor() - 5)

        # Collision detection
        if spaceship.distance(asteroid) < 50:
            spaceship.shape(blast_img)
            asteroid.hideturtle()
        else:
            reset_asteroid()
            screen.ontimer(update, 50)  # Update every 50ms

# Start the game loop
update()

# Keep the window open
screen.mainloop()
