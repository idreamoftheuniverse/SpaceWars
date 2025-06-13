import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=400, height=600)
screen.bgpic("background.png")
screen.title("Space Escape")

# Register shapes
spaceship_img = "spaceship.png"
asteroid_img = "asteroid.png"
blast_img = "blast.png"

screen.register_shape(spaceship_img)
screen.register_shape(asteroid_img)
screen.register_shape(blast_img)

# Create spaceship
spaceship = turtle.Turtle()
spaceship.shape(spaceship_img)
spaceship.penup()
spaceship.goto(0, -250)

# Create asteroid
asteroid = turtle.Turtle()
asteroid.shape(asteroid_img)
asteroid.penup()
asteroid.speed(0)
asteroid.goto(0, 250)

# Movement functions
def move_right():
    x = spaceship.xcor()
    spaceship.setx(min(x + 20, 190))  # Keep within screen

def move_left():
    x = spaceship.xcor()
    spaceship.setx(max(x - 20, -190))  # Keep within screen

# Key bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Reset asteroid if it goes off screen
def reset_asteroid():
    if asteroid.ycor() < -300:
        new_x = random.randint(-170, 170)
        asteroid.hideturtle()
        asteroid.goto(new_x, 300)
        asteroid.showturtle()

# Game update loop
def update():
    if spaceship.shape() != blast_img:
        asteroid.sety(asteroid.ycor() - 5)

        # Collision check
        if spaceship.distance(asteroid) < 50:
            spaceship.shape(blast_img)
            asteroid.hideturtle()
        else:
            reset_asteroid()
            screen.ontimer(update, 50)  # Repeat after 50ms

# Start game loop
update()

# Keep the window open
screen.mainloop()
