# http://docs.python.org/2/library/turtle.html
import turtle      # import turtle module


turtle.pensize(2) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-200, -50) # Coordinate (-200, -50) is center of the circle
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red") # Use red color
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

turtle.penup() # Pull the pen up
turtle.goto(-100, -50) # Coordinate (-100, -50) is center of the circle
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("orange") # Use orange color
turtle.circle(40, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape

turtle.penup() # Pull the pen up
turtle.goto(0, -50) # Coordinate (0, -50) is center of the circle
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green") # Use green color
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape

turtle.penup() # Pull the pen up
turtle.goto(100, -50) # Coordinate (100, -50) is center of the circle
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow") # Use yellow color
turtle.circle(40, steps = 6) # Draw a hexagon
turtle.end_fill() # Fill the shape

turtle.penup() # Pull the pen up
turtle.goto(200, -50) # Coordinate (200, -50) is center of the circle
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("black") # Use black color
turtle.circle(40) # Draw a circle
turtle.end_fill() # Fill the shape

turtle.clear()
