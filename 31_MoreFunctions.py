
# ======================
# 31_MoreFunctions.py
# ======================

# ============
# Parabola
# ============

# Functions are very useful to make the same block of code to be used over and over again.
# parabola is a very interesting shape
# parabolic reflectors can be used to focus light or sound and are also used to focus satelite signals
# used for modern TV broadcast.
# If you throw a ball in the air, it follows a parabolic path as it rises and falls back to earth

# we will create a simple equation for parabola using a parabola function

def parabola(x):
    y = x * x
    return y

# Then we can test the parabola function by giving it values in range

for x in range(-100, 100):
    y = parabola(x)
    print(y)

print("="*40)

# We see the results start with a high number, then go low and then high again.



# ===================================
# Plotting parabola result to graph
# ===================================

# we can plot this in a graph using tkinter to see what it looks like

# First we import tkinter

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# This is the parabola function we created.

def parabola(x):
    y = x * x / 100  # NOTE: we use / 100 here to make our graph fit. remove / 100 and see the result
    return y

# Then we can test the parabola function by giving it values in range

for x in range(-100, 100):
    y = parabola(x)
    print(y)


# then we create the mainWindow

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# Then we create the canvas and add it to grid
# http://effbot.org/tkinterbook/canvas.htm
# The canvas is a general purpose widget, which is typically used to display and edit graphs and other drawings.
# you can also place texts and images on a canvas.
# Canvas coordinate section has 0,0 on top left, while normal graph would have 0,0 in the middle.

# Add canvas to mainWindow and give it dimensions, in this case, same dimensions as mainWindow so canvas fills mainWindow
# Then we add the canvas to grid in the mainWindow

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)


# We would also like to have X and Y axis displayed on the graph
# We can find the midpoint of the screen by dividing the width and height by two and Canvas can have its origin
# shifted by using the "scroll region" option.
# we want to shift right by half the width, bringing 0 from left side to the middle and also shift it down by half the height.
# we want to do this when we want to plot a graph on a canvas where "axis" function would be useful for that purpose

# We will now define the "draw_axes" method here

def draw_axes(canvas):  # parameter is "canvas"
    canvas.update()  # it calls the canvas.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = canvas.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = canvas.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # scrollregion is a box with one corner at -x_origin & -y_origin and the other corner at x_origin & y_origin.
    # example if you had a 10 cm paper with top left side in the middle of your desk, if you move it up 5 cm and
    # left 5 cm, it will place the center of the paper in the middle of you desk

    # To add scrolling
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis

    canvas.create_line(-x_origin, 0, x_origin, 0, fill="red")  # Draws horizontal line. use red to see line well
    canvas.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line


# Now we call the draw_axes function here to draw the vertical and horizontal lines to divide the canvas.
# We see the canvas is now divided into four quadrants on x and y axis

draw_axes(canvas)

# To draw graphs, we need to plot single points which a canvas does not provide a method for.
# But a line length of 1 will do.
# NOTE again. you cannot plot single points but you can use a line of lengh 1 to plot them

# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.

def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="black")  # creates small lines of 1 pixel length, looks like dots.

# Then we call the "plot" function

for x in range(-100, 100): # gives x range from -100 to 100
    y = parabola(x)  # this functions gives result y = x * x
    plot(canvas, x, -y)  # plot function is called and given parameter canvas, and x and y axis. it will plot the small lines

# NOTE: the resulting graph is upside down. To flip it up, pass -y to plot function i.e plot(canvas, x, -y)


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()


print("="*40)

# ========================================
# Variable "Scope" in functions
# ========================================

# NOTE: if you want more comments for below program, see above.

# MAIN THING TO NOTE ABOUT SCOPE
# A function can use a variable from the main program but the main program cannot see variables that are local to the function

# First we import tkinter

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# This is the parabola function we created.

# The parabola() function below is not doing all it could because the main program needs to
# loop through the range on this line (for x in range(-100, 100):) and go through all the values it returns
# in order to print the parabola.
# it would be more useful if the function plotted the points and all we had to do is tell it how big the parabola
# should be and then give it a canvas to draw on

# ============================
# Shadow error messages
# ============================

# NOTE: These errors messages help you find the location of error if you have made mistakes in global/local variables

# but first lets look at the shadow name error
# Shadow name error showing under these lines
# def parabola(x):
# def draw_axes(canvas)
# def plot(canvas, x, y):

# This "shadow name" error is coming about because one of our variables in our function "shadows" a variable
# with the same name in the main program

# DEFINITION: variable shadowing occurs when a variable declared within a certain scope (decision block, method, or inner class)
# has the same name as a variable declared in an outer scope.

# Error message when you highlight to the right side:

# Shadow name 'x' from outer scope (Ctrl+F1)
# This inspection detects shadowing names defined in outer scope

# When they say "outer scope", they mean the main program where we created a variable called "canvas"
# This is the line with variable canvas => canvas = tkinter.Canvas(mainWindow, width=640, height=480)

# Example: one of the errors say that "canvas" name is defined here as a parameter to function "def draw_axes(canvas)"
# When we gave function "def draw_axes(canvas)" parameter named "canvas", the function lost the ability to see the "canvas" variable
# in the main program because they have same name => canvas = tkinter.Canvas(mainWindow, width=640, height=480)

# So all references to "canvas" within function "def draw_axes(canvas)" will refer to the parameter that was passed in and not the "canvas" variable from => canvas = tkinter.Canvas(mainWindow, width=640, height=480)

# This is where we need to understand the "scope" because functions introduce new scope in python.
# To explain the difference between the "canvas" that is local to function "def draw_axes(canvas)" and one that is global,
# we will create another Canvas and resize both so they can each occupy half the window
# we go to this line ==> canvas = tkinter.Canvas(mainWindow, width=640, height=480)

def parabola(x):
    y = x * x / 100  # NOTE: we use / 100 here to make our graph fit. remove / 100 and see the result
    return y

# Then we can test the parabola function by giving it values in range

for x in range(-100, 100):
    y = parabola(x)
    print(y)


# then we create the mainWindow

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# Global Variables (canvas and canvas2)
# we will create another Canvas and resize both so they can each occupy half the window
# our original canvas had width of 640. we will make that half (320) so it occupys half the window

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

# now we will add a second variable called canvas2
# Then we add it to next column 1 of grid

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")  # Add backgroud of blue
canvas2.grid(row=0, column=1)

# Since we have defined draw_axes function below, we will go down to call the new draw_axes(canvas2)

# We will now define the "draw_axes" method here
# you can replace this local variable (parameter) called "canvas" with another name and it will work for the function it is defined in.
# but it will not be visible to the main program


def draw_axes(canvas):  # parameter is "canvas"
    canvas.update()  # it calls the canvas.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = canvas.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = canvas.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis

    canvas.create_line(-x_origin, 0, x_origin, 0, fill="red")  # Draws horizontal line. use red to see line well
    canvas.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line

    # Local variables
    # NOTE: Read this after reading section above ==> print(repr(canvas), repr(canvas2))
    # we can also print local variables using locals() function to print all the local variables for a method.
    # We use command below to print all the variables that have been defined for this function.
    # When we run it, we get this results where "canvas" is the parameter defined in this object and .!canvas & .!canvas
    # are the global parameters defined below.
    # {'y_origin': 242.0, 'x_origin': 162.0, 'canvas': <tkinter.Canvas object .!canvas>}
    # {'y_origin': 242.0, 'x_origin': 162.0, 'canvas': <tkinter.Canvas object .!canvas2>}
    # both "locals" and "repr" functions are important when debugging and trying to find which are local variables and which are global

    print(locals())

# Call function draw_axes
# Now we call the draw_axes function here to draw the vertical and horizontal lines to divide the canvas.
# We see the canvas is now divided into four quadrants on x and y axis

# When you run this, you see it draws to sections in the window. one on left and one on right
# How this works:
# First line calls draw_axes function and passes argument named "canvas" defined here ==> canvas = tkinter.Canvas(mainWindow, width=320, height=480)
# Then function draw_axes takes argument named "canvas" and names it "canvas" as defined in its definition above ==> (def draw_axes(canvas):

# Second line calls draw_axes function and passes argument named "canvas2"
# Then function draw_axes takes argument "canvas2" and renames it "canvas" as defined in its definition above ==> (def draw_axes(canvas):

draw_axes(canvas)  # call canvas
draw_axes(canvas2)  # call canvas2

# We can see this better by printing the details of the canvas/canvas2 objects
# we use command "repr" which shows the representation of the object.
# This should print out the memory address of the objects, but in my case, it prints  this
# <tkinter.Canvas object .!canvas> <tkinter.Canvas object .!canvas2>
# In trainers video, it prints numbers instead of .!canvas and .!canvas2
# But we can see that canvas and canvas2 are separate objects

print(repr(canvas), repr(canvas2))



# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.

def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="black")  # creates small lines of 1 pixel length, looks like dots.

# Then we call the "plot" function

for x in range(-100, 100): # gives x range from -100 to 100
    y = parabola(x)  # this functions gives result y = x * x
    plot(canvas, x, -y)  # plot function is called and given parameter canvas, and x and y axis. it will plot the small lines

# NOTE: the resulting graph is upside down. To flip it up, pass -y to plot function i.e plot(canvas, x, -y)


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()

print("="*40)



# ===============================================
# Get back to original program
# ===============================================

# We will clean up above code and put it back to how it was before, with only one canvas or section
# we will delete canvas2 object
# In function "def draw_axes(canvas)", we will rename parameter "canvas" into "page" so it is
# not confused with the global variable "canvas" defined by ==> canvas = tkinter.Canvas(mainWindow, width=320, height=480)
# Now if you run this code, we have the original program


try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

def parabola(x):
    y = x * x / 100  # NOTE: we use / 100 here to make our graph fit. remove / 100 and see the result
    return y

# Then we can test the parabola function by giving it values in range

for x in range(-100, 100):
    y = parabola(x)
    print(y)


# then we create the mainWindow

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# We return width back to 640 to so that canvas can occupy whole screen (mainWindow)
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# We will rename parameter to be "page" instead of "canvas"
# NOTE that everything under function "def draw_axes(page)" will take parameter "page".

def draw_axes(page):  # parameter is "page"
    page.update()  # it calls the canvas.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = page.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = page.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis

    page.create_line(-x_origin, 0, x_origin, 0, fill="red")  # Draws horizontal line. use red to see line well
    page.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line

    print(locals())


draw_axes(canvas)  # call canvas



# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.

def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="black")  # creates small lines of 1 pixel length, looks like dots.

# Then we call the "plot" function

for x in range(-100, 100): # gives x range from -100 to 100
    y = parabola(x)  # this functions gives result y = x * x
    plot(canvas, x, -y)  # plot function is called and given parameter canvas, and x and y axis. it will plot the small lines

# NOTE: the resulting graph is upside down. To flip it up, pass -y to plot function i.e plot(canvas, x, -y)


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()

print("="*40)




# ======================================================
# Making Parabola function plot to different sizes
# ======================================================

# The parabola function would be more useful if it did the plotting and all we have to do is call it
# with a canvas and size we want to use.
# so instead of creating a range like "for x in range(-100, 100)" , we should be able to call the parabola
# function and pass it the size and have it do the work for us.

# We do this by making a change to the parabola method "def parabola():"

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# Method 1 for defining parabola function
# Make sure to comment out one parabola function while running the other

# will pass the canvas (named "page") and "size" to the parabola
# Then we add a for loop to get values from -size to + size.
# The for loop here replaces the original for loop "for x in range(-100, 100)" which we will delete
# We then call the "plot" function which plots the graph
# We will delete the "return y" because we don't need to return anything. Hence will return None


# def parabola(page, size):
#     for x in range(-size, size):  # calculates range from negative to positive
#         y = x * x / size  # we divide by "size" to reduce screen length. This is because x*x is a high number
#         plot(page, x, y)  # plot function takes three parameters. see plot function config below


# Method 2 for defining parabola function
# we only use positive size to calculate y
# then use - and + numbers to display it on the canvas

def parabola(page, size):
    for x in range(size):
        y = x * x / size  # Calculates y once using size instead of twice using -size and size
        plot(page, x, y)  # plots graph on the top right side.
        plot(page, -x, y)  # plots graph on the top left side
        plot(page, x, -y)  # plots graph on the bottom right side
        plot(page, -x, -y)  # plots graph on the bottom left side

# then we create the mainWindow

mainWindow = tkinter.Tk()


mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# We return width back to 640 to so that canvas can occupy whole screen (mainWindow)

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# We will rename parameter to be "page" instead of "canvas"
# NOTE that everything under function "def draw_axes(page)" will take parameter "page".

def draw_axes(page):  # parameter is "page"
    page.update()  # it calls the canvas.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = page.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = page.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis
    page.create_line(-x_origin, 0, x_origin, 0, fill="red")  # Draws horizontal line. use red to see line well
    page.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line
    print(locals())

# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.
# NOTE: put -y and -y + 1 to make the graph look upwards. If you only put -y + 1, it creates a cool effect. play with it and see

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="black")  # creates small lines of 1 pixel length, looks like dots.

# We call the "draw_axes" function and pass it "canvas"  to draw axes for us

draw_axes(canvas)

# Now we call function "parabola" and pass it to parameters: "canvas" function and size 100 (and 200) to plot two graphs
# NOTE that function "parabola" takes two parameters
# NOTE: the resulting graph is upside down. We correct this in the "plot" function above


parabola(canvas, 100)
parabola(canvas, 200)



# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()

print("="*40)








# ======================================================
# Function to draw Circle
# ======================================================


# Now we will add a function to draw a circle


try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# We will import math because we will be using math functions

import math

# Method 1 for defining parabola function

# def parabola(page, size):
#     for x in range(-size, size):  # calculates range from negative to positive
#         y = x * x / size  # we divide by "size" to reduce screen length. This is because x*x is a high number
#         plot(page, x, y)  # plot function takes three parameters. see plot function config below


# Method 2 for defining parabola function

def parabola(page, size):
    for x in range(size):
        y = x * x / size  # Calculates y once using size instead of twice using -size and size
        plot(page, x, y)  # plots graph on the top right side.
        plot(page, -x, y)  # plots graph on the top left side
        plot(page, x, -y)  # plots graph on the bottom right side
        plot(page, -x, -y)  # plots graph on the bottom left side


# Calculating Circle
# Circle is symmetric around both axes, so we only need to calculate a quarter of the points of the circumference
# This line "y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))" gives the positive or negative value for y
# So instead of calculating the sqrt twice, we can calculate it once and then negate -y for the negative
# Because -y will also take off h, we have 2 * h back on lines "plot(page, x, 2 * h - y)" and "plot(page, 2 * g - x, 2 * h - y)"
# And the same for x when we calculate the value for other quadrants.

# this function will draw circles with any radius centered around the canvas.
# Hence we can call it a few times to create a pattern.
# See "Call circle function" below

# Say for example we call "circle(canvas, 100, 100, 100)" giving it these parameters.
# where page=canvas, radius=100, g=100, h=100.
# We will use "for x in range(g, g + radius" to loop through the range when we call circle function (say from 100 to 200)
# Now that you have x and y values, we call function "plot", give it parameters (page, x and y) and it will plot the circle


def circle(page, radius, g, h):
    for x in range(g, g + radius):  # We loop through the range say 100 to 200 (from g = 100 and radius = 100)
        y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))  # Then we calculate y using values called and range.
        plot(page, x, y)  # x and y plots the top right side of the circle
        plot(page, x, 2 * h - y)  # This plots the bottom right side of the circle
        plot(page, 2 * g - x, y)  # Plots the top left side of the circle
        plot(page, 2 * g - x, 2 * h - y)  # Plots the bottom left side of the circle



# then we create the mainWindow

mainWindow = tkinter.Tk()


mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# We return width back to 640 to so that canvas can occupy whole screen (mainWindow)

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# We will rename parameter to be "page" instead of "canvas"
# NOTE that everything under function "def draw_axes(page)" will take parameter "page".

def draw_axes(page):  # parameter is "page"

    page.update()  # it calls the page.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = page.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = page.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling.
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis
    page.create_line(-x_origin, 0, x_origin, 0, fill="green")  # Draws horizontal line. use green to see line well
    page.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line. use red
    print(locals())

# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.
# NOTE: put -y and -y + 1 to make the graph look upwards. If you only put -y + 1, it creates a cool effect. play with it and see

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")  # creates small lines of 1 pixel length, looks like dots.

# We call the "draw_axes" function and pass it "canvas"  to draw axes for us

draw_axes(canvas)

# Now we call function "parabola" and pass it to parameters: "canvas" function and size 100 (and 200) to plot two graphs
# NOTE that function "parabola" takes two parameters
# NOTE: the resulting graph is upside down. We correct this in the "plot" function above

parabola(canvas, 100)
parabola(canvas, 200)

# Call circle function
# We call the circle function several with various parameters to create a pattern of circles
# NOTE: circle function takes 4 arguments ==> def circle(page, radius, g, h):

# NOTE: that it plots circles with vague lines on the edges.
# This is because its only plotting integer values of x on the ranges given hence we don't get many points plotted
# This will be corrected in the next code below

circle(canvas, 100, 100, 100)  # page=canvas, radius=100, g=100, h=100 (Draws circle with radius 100 on top, right side of canvas)
circle(canvas, 100, 100, -100)  # page=canvas, radius=100, g=100, h=-100 (Draws circle with radius 100 on bottom, right side of canvas)
circle(canvas, 100, -100, 100)  # page=canvas, radius=100, g=-100, h=100 (Draws circle with radius 100 on top, left side of canvas)
circle(canvas, 100, -100, -100)  # page=canvas, radius=100, g=-100, h=-100 (Draws circle with radius 100 on bottom, left side of canvas)
circle(canvas, 10, 30, 30)  # page=canvas, radius=10, g=30, h=30 (Draws circle with radius 30 on top, right side of canvas)
circle(canvas, 10, 30, -30)  # page=canvas, radius=10, g=30, h=-30 (Draws circle with radius 30 on bottom, right side of canvas)
circle(canvas, 10, -30, 30)  # page=canvas, radius=10, g=-30, h=30 (Draws circle with radius 30 on top, left side of canvas)
circle(canvas, 10, -30, -30)  # page=canvas, radius=10, g=-30, h=-30 (Draws circle with radius 30 on bottom, left side of canvas)
circle(canvas, 30, 0, 0)  # page=canvas, radius=00, g=00, h=0 (Draws circle with radius 30 in the middle of canvas)


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()


print("="*40)








# ======================================================
# How to fix circle to be drawn more clearly
# ======================================================


# In above code, we saw that the circle was drawn with faint edges
# This is because we are only using integer values of x on the circle function
# we can fix this by multiplying x by 100 to increase the range of points plotted
# and then scale back x back to normal by dividing by 100

# Now we will add a function to draw a circle


try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# We will import math because we will be using math functions

import math

# Method 1 for defining parabola function

# def parabola(page, size):
#     for x in range(-size, size):  # calculates range from negative to positive
#         y = x * x / size  # we divide by "size" to reduce screen length. This is because x*x is a high number
#         plot(page, x, y)  # plot function takes three parameters. see plot function config below


# Method 2 for defining parabola function

def parabola(page, size):
    for x in range(size):
        y = x * x / size  # Calculates y once using size instead of twice using -size and size
        plot(page, x, y)  # plots graph on the top right side.
        plot(page, -x, y)  # plots graph on the top left side
        plot(page, x, -y)  # plots graph on the bottom right side
        plot(page, -x, -y)  # plots graph on the bottom left side


# Calculating Circle
# Circle is symmetric around both axes, so we only need to calculate a quarter of the points of the circumference
# This line "y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))" gives the positive or negative value for y
# So instead of calculating the sqrt twice, we can calculate it once and then negate -y for the negative
# Because -y will also take off h, we have 2 * h back on lines "plot(page, x, 2 * h - y)" and "plot(page, 2 * g - x, 2 * h - y)"
# And the same for x when we calculate the value for other quadrants.

# this function will draw circles with any radius centered around the canvas.
# Hence we can call it a few times to create a pattern.
# See "Call circle function" below

# Say for example we call "circle(canvas, 100, 100, 100)" giving it these parameters.
# where page=canvas, radius=100, g=100, h=100.
# We will use "for x in range(g, g + radius" to loop through the range when we call circle function (say from 100 to 200)
# Now that you have x and y values, we call function "plot", give it parameters (page, x and y) and it will plot the circle

# Solution to faint circle lines
# in the "for x in range" loop, we multiply by 100 to make more points to be plotted
# NOTE: This may take a longer time to run because it is plotting 100 times more points
# The performance has suffered due to more points.
# The canvas widget has a "create_oval" method that can be used to to draw circles and is much faster than the method we used here

# ADVANTAGE: e see that having the circle drawing code in a function, the change of one function changes all circles



def circle(page, radius, g, h):
    for x in range(g * 100, (g + radius) * 100):  # We loop through range but multiply it by 100 to increase number of points plotted
        x /= 100  # Bring back x to original integers by saying x = x / 100
        print(x)  # You can add this print here to show the number of x points that are being plotted
        y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))  # Then we calculate y using values called and range.
        plot(page, x, y)  # x and y plots the top right side of the circle
        plot(page, x, 2 * h - y)  # This plots the bottom right side of the circle
        plot(page, 2 * g - x, y)  # Plots the top left side of the circle
        plot(page, 2 * g - x, 2 * h - y)  # Plots the bottom left side of the circle



# then we create the mainWindow

mainWindow = tkinter.Tk()


mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# We return width back to 640 to so that canvas can occupy whole screen (mainWindow)

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# We will rename parameter to be "page" instead of "canvas"
# NOTE that everything under function "def draw_axes(page)" will take parameter "page".

def draw_axes(page):  # parameter is "page"

    page.update()  # it calls the page.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = page.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = page.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling.
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis
    page.create_line(-x_origin, 0, x_origin, 0, fill="green")  # Draws horizontal line. use green to see line well
    page.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line. use red
    print(locals())

# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.
# NOTE: put -y and -y + 1 to make the graph look upwards. If you only put -y + 1, it creates a cool effect. play with it and see

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")  # creates small lines of 1 pixel length, looks like dots.

# We call the "draw_axes" function and pass it "canvas"  to draw axes for us

draw_axes(canvas)

# Now we call function "parabola" and pass it to parameters: "canvas" function and size 100 (and 200) to plot two graphs
# NOTE that function "parabola" takes two parameters
# NOTE: the resulting graph is upside down. We correct this in the "plot" function above

parabola(canvas, 100)
parabola(canvas, 200)

# Call circle function
# We call the circle function several with various parameters to create a pattern of circles
# NOTE: circle function takes 4 arguments ==> def circle(page, radius, g, h):

# NOTE: that it plots circles with vague lines on the edges.
# This is because its only plotting integer values of x on the ranges given hence we don't get many points plotted
# This will be corrected in the next code below

circle(canvas, 100, 100, 100)  # page=canvas, radius=100, g=100, h=100 (Draws circle with radius 100 on top, right side of canvas)
circle(canvas, 100, 100, -100)  # page=canvas, radius=100, g=100, h=-100 (Draws circle with radius 100 on bottom, right side of canvas)
circle(canvas, 100, -100, 100)  # page=canvas, radius=100, g=-100, h=100 (Draws circle with radius 100 on top, left side of canvas)
circle(canvas, 100, -100, -100)  # page=canvas, radius=100, g=-100, h=-100 (Draws circle with radius 100 on bottom, left side of canvas)
circle(canvas, 10, 30, 30)  # page=canvas, radius=10, g=30, h=30 (Draws circle with radius 30 on top, right side of canvas)
circle(canvas, 10, 30, -30)  # page=canvas, radius=10, g=30, h=-30 (Draws circle with radius 30 on bottom, right side of canvas)
circle(canvas, 10, -30, 30)  # page=canvas, radius=10, g=-30, h=30 (Draws circle with radius 30 on top, left side of canvas)
circle(canvas, 10, -30, -30)  # page=canvas, radius=10, g=-30, h=-30 (Draws circle with radius 30 on bottom, left side of canvas)
circle(canvas, 30, 0, 0)  # page=canvas, radius=00, g=00, h=0 (Draws circle with radius 30 in the middle of canvas)


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()


print("="*40)




# ======================================================
# Using "create_oval" method to draw a circle
# ======================================================


# in above code, we drew circle but there were some performance issues because it was very slow
# We can use "create_oval" method of the "canvas" widget to draw circles much faster

# "create_oval" method needs the coordinates of the top left and bottom right of a bounding rectangle
# but we are working with the radius and coordinates of the center.
# We will still use our circle method, but will change to calculate the coordinates that "create_oval" method needs.


# Now we will add a function to draw a circle

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# We will import math because we will be using math functions

import math

# Method 1 for defining parabola function

# def parabola(page, size):
#     for x in range(-size, size):  # calculates range from negative to positive
#         y = x * x / size  # we divide by "size" to reduce screen length. This is because x*x is a high number
#         plot(page, x, y)  # plot function takes three parameters. see plot function config below


# Method 2 for defining parabola function

def parabola(page, size):
    for x in range(size):
        y = x * x / size  # Calculates y once using size instead of twice using -size and size
        plot(page, x, y)  # plots graph on the top right side.
        plot(page, -x, y)  # plots graph on the top left side
        plot(page, x, -y)  # plots graph on the bottom right side
        plot(page, -x, -y)  # plots graph on the bottom left side


# Calculating Circle
# Circle is symmetric around both axes, so we only need to calculate a quarter of the points of the circumference
# This line "y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))" gives the positive or negative value for y
# So instead of calculating the sqrt twice, we can calculate it once and then negate -y for the negative
# Because -y will also take off h, we have 2 * h back on lines "plot(page, x, 2 * h - y)" and "plot(page, 2 * g - x, 2 * h - y)"
# And the same for x when we calculate the value for other quadrants.

# this function will draw circles with any radius centered around the canvas.
# Hence we can call it a few times to create a pattern.
# See "Call circle function" below

# Say for example we call "circle(canvas, 100, 100, 100)" giving it these parameters.
# where page=canvas, radius=100, g=100, h=100.
# We will use "for x in range(g, g + radius" to loop through the range when we call circle function (say from 100 to 200)
# Now that you have x and y values, we call function "plot", give it parameters (page, x and y) and it will plot the circle

# Solution to faint circle lines
# in the "for x in range" loop, we multiply by 100 to make more points to be plotted
# NOTE: This may take a longer time to run because it is plotting 100 times more points
# The performance has suffered due to more points.
# The canvas widget has a "create_oval" method that can be used to to draw circles and is much faster than the method we used here

# ADVANTAGE: e see that having the circle drawing code in a function, the change of one function changes all circles

# Using "create_oval" method
# ===========================

# "create_oval" method needs the coordinates of the top left and bottom right of a bounding rectangle
# but we are working with the radius and coordinates of the center.
# We will still use our circle method, but will change to calculate the coordinates that "create_oval" method needs.

# The "page.create_oval" line calculates the coordinates that create_oval needs i.e. top left and bottom left of the bounding rectangle
# and then we will draw an oval within those parameters.
# outline="green" gives the color of the outline or line
# width=3 gives the width of the line
#
# NOTE that this method runs much faster.
# The advantage of this is we are using optimized code that is built in as part of python.
# it is always a good idea where possible to use premade code instead of reinventing the wheel

# NOTE: we refer to "create_oval" as a "method" and not a "function"
# This is because "canvas" is a class and class functions are called "Methods"
# We will explain more on this in our object oriented programming


def circle(page, radius, g, h):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline="green", width=3)

    # We will comment this original code out.
    #
    # for x in range(g * 100, (g + radius) * 100):  # We loop through range but multiply it by 100 to increase number of points plotted
    #     x /= 100  # Bring back x to original integers by saying x = x / 100
    #     print(x)  # You can add this print here to show the number of x points that are being plotted
    #     y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))  # Then we calculate y using values called and range.
    #     plot(page, x, y)  # x and y plots the top right side of the circle
    #     plot(page, x, 2 * h - y)  # This plots the bottom right side of the circle
    #     plot(page, 2 * g - x, y)  # Plots the top left side of the circle
    #     plot(page, 2 * g - x, 2 * h - y)  # Plots the bottom left side of the circle



# then we create the mainWindow

mainWindow = tkinter.Tk()


mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# We return width back to 640 to so that canvas can occupy whole screen (mainWindow)

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# We will rename parameter to be "page" instead of "canvas"
# NOTE that everything under function "def draw_axes(page)" will take parameter "page".

def draw_axes(page):  # parameter is "page"

    page.update()  # it calls the page.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = page.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = page.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling.
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis
    page.create_line(-x_origin, 0, x_origin, 0, fill="green")  # Draws horizontal line. use green to see line well
    page.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line. use red
    print(locals())

# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.
# NOTE: put -y and -y + 1 to make the graph look upwards. If you only put -y + 1, it creates a cool effect. play with it and see

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")  # creates small lines of 1 pixel length, looks like dots.

# We call the "draw_axes" function and pass it "canvas"  to draw axes for us

draw_axes(canvas)

# Now we call function "parabola" and pass it to parameters: "canvas" function and size 100 (and 200) to plot two graphs
# NOTE that function "parabola" takes two parameters
# NOTE: the resulting graph is upside down. We correct this in the "plot" function above

parabola(canvas, 100)
parabola(canvas, 200)

# Call circle function
# We call the circle function several with various parameters to create a pattern of circles
# NOTE: circle function takes 4 arguments ==> def circle(page, radius, g, h):

# NOTE: that it plots circles with vague lines on the edges.
# This is because its only plotting integer values of x on the ranges given hence we don't get many points plotted
# This will be corrected in the next code below

circle(canvas, 100, 100, 100)  # page=canvas, radius=100, g=100, h=100 (Draws circle with radius 100 on top, right side of canvas)
circle(canvas, 100, 100, -100)  # page=canvas, radius=100, g=100, h=-100 (Draws circle with radius 100 on bottom, right side of canvas)
circle(canvas, 100, -100, 100)  # page=canvas, radius=100, g=-100, h=100 (Draws circle with radius 100 on top, left side of canvas)
circle(canvas, 100, -100, -100)  # page=canvas, radius=100, g=-100, h=-100 (Draws circle with radius 100 on bottom, left side of canvas)
circle(canvas, 10, 30, 30)  # page=canvas, radius=10, g=30, h=30 (Draws circle with radius 30 on top, right side of canvas)
circle(canvas, 10, 30, -30)  # page=canvas, radius=10, g=30, h=-30 (Draws circle with radius 30 on bottom, right side of canvas)
circle(canvas, 10, -30, 30)  # page=canvas, radius=10, g=-30, h=30 (Draws circle with radius 30 on top, left side of canvas)
circle(canvas, 10, -30, -30)  # page=canvas, radius=10, g=-30, h=-30 (Draws circle with radius 30 on bottom, left side of canvas)
circle(canvas, 30, 0, 0)  # page=canvas, radius=00, g=00, h=0 (Draws circle with radius 30 in the middle of canvas)


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()

print("="*40)


# ======================================================
# Circle challenge
# ======================================================

# Challenge:
# Modify the circle function so that it allows the color of the circle to be specified
# and defaults to red if a color is not given.
# Can Review previous lectures on named and default values for solution



# in above code, we drew circle but there were some performance issues because it was very slow
# We can use "create_oval" method of the "canvas" widget to draw circles much faster

# "create_oval" method needs the coordinates of the top left and bottom right of a bounding rectangle
# but we are working with the radius and coordinates of the center.
# We will still use our circle method, but will change to calculate the coordinates that "create_oval" method needs.


# Now we will add a function to draw a circle

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# We will import math because we will be using math functions

import math

# Method 1 for defining parabola function

def parabola(page, size):
    for x in range(-size, size):  # calculates range from negative to positive
        y = x * x / size  # we divide by "size" to reduce screen length. This is because x*x is a high number
        plot(page, x, y)  # plot function takes three parameters. see plot function config below

print("="*40)

# Method 2 for defining parabola function

def parabola(page, size):
    for x in range(size):
        y = x * x / size  # Calculates y once using size instead of twice using -size and size
        plot(page, x, y)  # plots graph on the top right side.
        plot(page, -x, y)  # plots graph on the top left side
        plot(page, x, -y)  # plots graph on the bottom right side
        plot(page, -x, -y)  # plots graph on the bottom left side

print("="*40)

# Calculating Circle
# Circle is symmetric around both axes, so we only need to calculate a quarter of the points of the circumference
# This line "y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))" gives the positive or negative value for y
# So instead of calculating the sqrt twice, we can calculate it once and then negate -y for the negative
# Because -y will also take off h, we have 2 * h back on lines "plot(page, x, 2 * h - y)" and "plot(page, 2 * g - x, 2 * h - y)"
# And the same for x when we calculate the value for other quadrants.

# this function will draw circles with any radius centered around the canvas.
# Hence we can call it a few times to create a pattern.
# See "Call circle function" below

# Say for example we call "circle(canvas, 100, 100, 100)" giving it these parameters.
# where page=canvas, radius=100, g=100, h=100.
# We will use "for x in range(g, g + radius" to loop through the range when we call circle function (say from 100 to 200)
# Now that you have x and y values, we call function "plot", give it parameters (page, x and y) and it will plot the circle

# Solution to faint circle lines
# in the "for x in range" loop, we multiply by 100 to make more points to be plotted
# NOTE: This may take a longer time to run because it is plotting 100 times more points
# The performance has suffered due to more points.
# The canvas widget has a "create_oval" method that can be used to to draw circles and is much faster than the method we used here

# ADVANTAGE: e see that having the circle drawing code in a function, the change of one function changes all circles

# Using "create_oval" method
# ===========================

# "create_oval" method needs the coordinates of the top left and bottom right of a bounding rectangle
# but we are working with the radius and coordinates of the center.
# We will still use our circle method, but will change to calculate the coordinates that "create_oval" method needs.

# The "page.create_oval" line calculates the coordinates that create_oval needs i.e. top left and bottom left of the bounding rectangle
# and then we will draw an oval within those parameters.
# outline="green" gives the color of the outline or line
# width=3 gives the width of the line
#
# NOTE that this method runs much faster.
# The advantage of this is we are using optimized code that is built in as part of python.
# it is always a good idea where possible to use premade code instead of reinventing the wheel

# NOTE: we refer to "create_oval" as a "method" and not a "function"
# This is because "canvas" is a class and class functions are called "Methods"
# We will explain more on this in our object oriented programming



# ============
# Challenge:
# ============

# Modify the circle function so that it allows the color of the circle to be specified
# and defaults to red if a color is not given.
# Can Review previous lectures on named and default values for solution

# Solution to this is to give "circle" function an extra parameter named "color" and setting it to "red"
# Then on the seconds line, replace color name (e.g. green) with parameter color i.e. outline=color
# Now when you call the "circle" function, you can specify additional parameter (color)
# but if you don't specify color when calling "circle", it defaults to red

def circle(page, radius, g, h, color="red"):   # Add parameter "color" and default it to red
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=3)  # Make outline to be "color" parameter

    # We will comment this original code out.
    #
    # for x in range(g * 100, (g + radius) * 100):  # We loop through range but multiply it by 100 to increase number of points plotted
    #     x /= 100  # Bring back x to original integers by saying x = x / 100
    #     print(x)  # You can add this print here to show the number of x points that are being plotted
    #     y = h + (math.sqrt(radius ** 2 - ((x-g)) ** 2))  # Then we calculate y using values called and range.
    #     plot(page, x, y)  # x and y plots the top right side of the circle
    #     plot(page, x, 2 * h - y)  # This plots the bottom right side of the circle
    #     plot(page, 2 * g - x, y)  # Plots the top left side of the circle
    #     plot(page, 2 * g - x, 2 * h - y)  # Plots the bottom left side of the circle



# then we create the mainWindow

mainWindow = tkinter.Tk()


mainWindow.title("Parabola")  # title of the window
mainWindow.geometry("640x480")  # you can modify this to suit your screen

# We return width back to 640 to so that canvas can occupy whole screen (mainWindow)

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# We will rename parameter to be "page" instead of "canvas"
# NOTE that everything under function "def draw_axes(page)" will take parameter "page".

def draw_axes(page):  # parameter is "page"

    page.update()  # it calls the page.update method to ensure we can access winfo_width and winfo_height methods
    x_origin = page.winfo_width() / 2  # divide width by 2 to get value of x_origin (i.e. middle of canvas)
    y_origin = page.winfo_height() / 2  # divide height by 2 to get value of y_origin (i.e. middle of canvas)

    # To add scrolling.
    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # The function create_line draws a horizontal line on x axis and vertical line on y axis
    page.create_line(-x_origin, 0, x_origin, 0, fill="green")  # Draws horizontal line. use green to see line well
    page.create_line(0, y_origin, 0, -y_origin, fill="red")  # Draws vertical line. use red
    print(locals())

# we will create a function called "plot",
# The function will take a "canvas" as its first parameter, followed by the x and y coordinates of the point to be plotted.
# NOTE: put -y and -y + 1 to make the graph look upwards. If you only put -y + 1, it creates a cool effect. play with it and see

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")  # creates small lines of 1 pixel length, looks like dots.

# We call the "draw_axes" function and pass it "canvas"  to draw axes for us

draw_axes(canvas)

# Now we call function "parabola" and pass it to parameters: "canvas" function and size 100 (and 200) to plot two graphs
# NOTE that function "parabola" takes two parameters
# NOTE: the resulting graph is upside down. We correct this in the "plot" function above

parabola(canvas, 100)
parabola(canvas, 200)

# Call circle function
# We call the circle function several with various parameters to create a pattern of circles
# NOTE: circle function takes 4 arguments ==> def circle(page, radius, g, h):

# NOTE: that it plots circles with vague lines on the edges.
# This is because its only plotting integer values of x on the ranges given hence we don't get many points plotted
# This will be corrected in the next code below

# we call "circle" function and specify color in first three lines
# The other lines will use default color red since we did not specify the color.
# Note if there was no default color specified in the defainition of "circle" ==> def circle(page, radius, g, h, color="red")
# Then we would have an error if we called without passing an argument for color

circle(canvas, 100, 100, 100, "green")  # specify parameter color as green
circle(canvas, 100, 100, -100, "yellow")  # specify paraameter color as yellow
circle(canvas, 100, -100, 100, "brown")  # specify parameter color as brown
circle(canvas, 100, -100, -100)  # Don't specify any color. it will default to red
circle(canvas, 10, 30, 30)  # Don't specify any color. it will default to red
circle(canvas, 10, 30, -30)  # Don't specify any color. it will default to red
circle(canvas, 10, -30, 30)  # Don't specify any color. it will default to red
circle(canvas, 10, -30, -30)  # Don't specify any color. it will default to red
circle(canvas, 30, 0, 0)  # Don't specify any color. it will default to red


# Need to add mainloop to give control to tkinter to create the graph/drawing

mainWindow.mainloop()


