from math import sqrt

"""
Given a point P (p) on a cartesian plane, take a given amount of steps along the x-axis and y-axis for each iteration and get as close to p as possible. 
After every 3rd iteration, take a given amount of steps backwards in the x and y directions. 
Arrive at a point (x, y) whose distance is closest to p (using the distance formula). Start at the origin (0,0).
"""

# Point class (Given)
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


# Main program

# All of the vars I tested against

# point_x, point_y, x_steps_in, y_steps_in, back_steps = 6, 6, 1, 1, 1
# point_x, point_y, x_steps_in, y_steps_in, back_steps = 4, 5, 2, 3, 1
# point_x, point_y, x_steps_in, y_steps_in, back_steps = 12, 9, 4, 3, 2
point_x, point_y, x_steps_in, y_steps_in, back_steps = 5,8,2,3,1

# Read in x and y for Point P
p = Point()
p.x = int(point_x)
p.y = int(point_y)

# Read in num of steps to be taken in X and Y directions
x_steps = int(x_steps_in)
y_steps = int(y_steps_in)

# Read in num of steps to be taken (backwards) every 3 steps
b_steps = int(back_steps)

# Write dynamic programming algorithm
c = Point()
c.x = 0
c.y = 0

num = (p.x - c.x)**2 + (p.y - c.y)**2
min_dist = sqrt(num)
i, d = 1, 0

while d <= min_dist:
  c.x += x_steps
  c.y += y_steps

  d = sqrt((p.x - c.x)**2 + (p.y - c.y)**2)

  # End loop
  if d >= min_dist:
    c.x -= x_steps
    c.y -= y_steps
    i -= 1
    break
  # Every third
  elif i % 3 == 0 and i != 0:
    c.x -= b_steps
    c.y -= b_steps
    d = sqrt((p.x - c.x)**2 + (p.y - c.y)**2)
  else:
    min_dist = d

  print(str(i) + " Location: " + str((c.x, c.y)) + "Distance :" + str(d))
  i += 1



num = (p.x - c.x)**2 + (p.y - c.y)**2
d = sqrt(num)
print("Point p: (" + str(p.x) + "," + str(p.y) + ")")
print("Arrival Point: (" + str(c.x) + "," + str(c.y) + ")")
print(f"Distance between P and arrival: " + "%.6f" % d)
print("Number of Iterations: ", i)
