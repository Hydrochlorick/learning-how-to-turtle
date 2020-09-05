import turtle

class Flower:
  """This is an object that helps your turtle draw flowers!"""
  def __init__(self, num_petals, color, dot_color, petal_length, petal_size, x, y):
    self.num_petals = num_petals
    self.color = color
    self.dot_color = dot_color
    self.petal_length = petal_length
    self.petal_size = petal_size
    self.x = x
    self.y = y

  def get_turn_degrees(self):
    return 360/self.num_petals

  def draw(self): #, x, y, num_petals, petal_size, color, petal_length
    """This function draws the flower using turtle graphics"""
    turtle.penup()
    turtle.goto(self.x, self.y)
    turtle.pendown()
    turtle.pencolor(self.color)
    turtle.pensize(self.petal_size)

    #draw petals
    degrees = self.get_turn_degrees()
    for _ in range(self.num_petals):
      turtle.forward(self.petal_length)
      turtle.backward(self.petal_length)
      turtle.right(degrees)

    #draw center
    turtle.pencolor(self.dot_color)
    turtle.dot(self.petal_size + 1.5)


class Tree:
  """This one makes a simple tree"""
  def __init__(self, leaf_color, leaves_size, trunk_size, x, y):
    self.leaf_color = leaf_color
    self.leaves_size = leaves_size #It's just gonna be a big circle
    self.trunk_size = trunk_size
    self.x = x
    self.y = y

  def get_trunk_length(self):
    return 10*self.trunk_size

  def draw(self):
    turtle.penup()
    turtle.goto(self.x, self.y)
    turtle.setheading(90) #Make sure it's facing up to start
    turtle.pendown()

    #draw trunk
    trunk_length = self.get_trunk_length()
    turtle.pencolor("brown")
    turtle.pensize(self.trunk_size)
    turtle.forward(trunk_length)

    #draw "leaves"
    turtle.pencolor(self.leaf_color)
    turtle.dot(self.leaves_size)


#Create some flower objects
jerry = Flower(6, "pink", "orange", 30, 18, 0, -300)
sonny = Flower(15, "yellow", "brown", 40, 8, 175, -360)
samuel = Flower(20, "purple", "red", 45, 10, -220, -345)

#Create some tree objects
atticus = Tree("green", 50, 15, -200, -200)
bruce = Tree("orange", 80, 24, 300, -100)
hollis = Tree("green", 140, 35, 40, -200)

#Draw the flowers!
jerry.draw()
sonny.draw()
samuel.draw()

#Draw the trees!
atticus.draw()
bruce.draw()
hollis.draw()

turtle.done()