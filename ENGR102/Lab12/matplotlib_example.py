# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Surya Jasper, Sumit Nalavade, Ronit Dhawan, Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 12 Matplotlib Example
# Date:         17 November 2022

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

# import our libraries
import numpy as np
from matplotlib import pyplot as plt
from math import pi

def part1():
  # here, we initialize or x and y values in the domain [-2, 2] with the correct focal lengths
  domain = np.linspace(-2, 2, 100)
  y_vals1 = 1/(4*2) * domain**2
  y_vals2 = 1/(4*6) * domain**2

  plt.figure('Part 1')

  # we use the plot function to plot both of these parabolas with the appropriate labels and line widths
  plt.plot(domain, y_vals1, 'r', linewidth=2, label='f=2')
  plt.plot(domain, y_vals2, 'b', linewidth=6, label='f=6')

  # lastly, we set our title, x and y labels, and our legend
  plt.title('Parabola plots with varying focal length')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend(loc="lower left")

def part2():
  # in part 2, we want our x values to be in the domain [-4, 4] and calculate our y values from the polynomial equation we're given
  x = np.linspace(-4, 4, 25)
  y = 2*x**3 + 3*x**2 - 11*x - 6

  plt.figure('Part 2')

  # we use the same plot function but use 'y*' for the stroke decoration to graph yellow stars for each point
  plt.plot(x, y, 'y*')

  # lastly, we set our title and x/y labels accordingly
  plt.title('Plot of cubic polynomial')
  plt.xlabel('x values')
  plt.ylabel('y values')

def part3():
  # in part 3, we want x values in the range [-2pi, 2pi] and to graph a cosine / sine function
  x = np.linspace(-2*pi, 2*pi, 100)
  cos = np.cos(x)
  sin = np.sin(x)
  
  # we can use the subplots function to create 2 vertically stacked graphs
  fig, axs = plt.subplots(2)

  # here, we give the plot a title
  fig.suptitle('Plot of cos(x) and sin(x)')

  # for each subplot, we want to plot the appropriate function and set the x/y labels properly
  # we can do this using the second item returned by the subplots function which gives us a list
  # of the 2 matplotlib plots we initialized with the subplots function
  axs[0].plot(x, cos, 'r', label='cos(x)')
  axs[0].set_ylabel('y=cos(x)')
  axs[0].legend(loc='lower right')

  axs[1].plot(x, sin, 'gray', label='sin(x)')
  axs[1].set_xlabel('x')
  axs[1].set_ylabel('y=sin(x)')
  axs[1].legend(loc='lower right')

# lastly, we set up all the graphs by calling the 3 functions and use plt.show() to display all of them
part1()
part2()
part3()
plt.show()
