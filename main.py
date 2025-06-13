import turtle
import random

screen = turtle.Screen()
screen.setup(400, 600)
screen.bgpic("background.png")

# Spaceship image
spaceship_img = "spaceship.png"
screen.register_shape(spaceship_img)

# Asteroid image
asteroid_img = "asteroid.png"
screen.register_shape(asteroid_img)

# Asteroid turtle
asteroid = turtle.Turtle()
asteroid.penup()
asteroid.speed(0)
asteroid.goto(0, 250)
asteroid.shape(asteroid_img)

# Spaceship turtle
spaceship = turtle.Turtle()
spaceship.penup()
spaceship.goto(0, -250)
spaceship.shape(spaceship_img)

# Blast image
blast_img = "blast.png"
screen.register_shape(blast_img)

# Movement functions
def move_right():
    spaceship_x = spaceship.xcor()
    spaceship_y = spaceship.ycor()
    spaceship.goto(spaceship_x + 10, spaceship_y)
    
def move_left():
    spaceship_x = spaceship.xcor()
    spaceship_y = spaceship.ycor()
    spaceship.goto(spaceship_x - 10, spaceship_y)
    
# Create keyboard bindings
screen.listen()
screen.onkey("Left", move_left)
screen.onkey("Right", move_right)

# Check collision between the asteroid and boundary
def reset_asteroid():
    if asteroid.ycor() < -300: #Bottom Wall
        asteroid_x = random.randint(-170, 170)
        asteroid_y = 300
        asteroid.hideturtle()
        asteroid.speed(0)
        asteroid.goto(asteroid_x, asteroid_y)
        asteroid.showturtle()
        
# Infinite loop to move the asteroid
while True:
    asteroid_x = asteroid.xcor()
    asteroid_y = asteroid.ycor()
    asteroid.goto(asteroid_x,asteroid_y - 5)
    # Check the collision between spaceship and steroid
    distance = spaceship.distance(asteroid)
    # Break the loop
    if(distance <= 67):
        spaceship.shape(blast_img)
        # Hide the asteroid on blast
        
        break     
    reset_asteroid()