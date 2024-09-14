# import turtle

# # Setup the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Create a turtle object
# my_turtle = turtle.Turtle()
# my_turtle.speed(1)

# # Functions to control the turtle
# def move_forward():
#     my_turtle.forward(10)

# def turn_left():
#     my_turtle.left(10)

# def turn_right():
#     my_turtle.right(10)

# def clear_drawing():
#     my_turtle.clear()

# # Keyboard bindings
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_drawing, "c")

# # Hide the turtle and keep the window open
# my_turtle.hideturtle()
# turtle.done()


# import turtle

# # Setup the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("black")

# # Create a turtle object
# my_turtle = turtle.Turtle()
# my_turtle.speed(0)

# # Draw a spiral with a gradient effect
# def draw_gradient_spiral():
#     colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#     for i in range(360):
#         my_turtle.pencolor(colors[i % len(colors)])
#         my_turtle.forward(i)
#         my_turtle.right(59)

# # Draw the spiral
# draw_gradient_spiral()

# # Hide the turtle and keep the window open
# my_turtle.hideturtle()
# turtle.done()


# import turtle

# # Setup the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("black")

# # Create a turtle object
# my_turtle = turtle.Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# my_turtle.speed(0)

# # Function to move the turtle to the clicked position
# def move_to(x, y):
#     my_turtle.penup()
#     my_turtle.goto(x, y)
#     my_turtle.pendown()

# # Bind the click event to the move_to function
# screen.onclick(move_to)

# # Keep the window open
# turtle.done()

# import turtle

# # Setup the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Create a turtle object
# my_turtle = turtle.Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# my_turtle.speed(0)


# # Function to update turtle position to the cursor
# def follow_cursor(x, y):
#     my_turtle.penup()
#     my_turtle.goto(x, y)
#     my_turtle.pendown()


# # Bind the cursor movement event to the follow_cursor function
# screen.tracer(0)  # Turn off automatic screen updates for smoother following


# # Function to continuously update turtle position
# def update_position():
#     x, y = turtle.window_width(), turtle.window_height()
#     screen.ontimer(lambda: follow_cursor(my_turtle.xcor(), my_turtle.ycor()), 10)
#     screen.update()
#     screen.ontimer(update_position, 10)


# # Start the continuous update
# update_position()

# # Keep the window open
# turtle.done()
