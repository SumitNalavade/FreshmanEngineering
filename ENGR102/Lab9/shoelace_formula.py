# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Surya Jasper, Sumit Nalavade, Srikar Velavarthipati, Ronit Dhawan
# Section:      524
# Assignment:   Lab 9 Shoelace Formula
# Date:         31 10 2022

# first, we create a function to parse our raw input string into a list of points
def getpoints(raw_str):
  points = [
    # here, we're converting the raw string into a list of strings, each formatted as "p1,p2"
    # and then converting each of those strings into a list of integers [p1, p2]
    list(map( int, raw_pt.split(',') )) 
      for raw_pt in raw_str.split()
  ]
  # lastly, we return our list of points
  return points

# next, we create a function that returns the determinant of the matrix formed by the 2 points
def cross(p1, p2):
  return p1[0] * p2[1] - p1[1] * p2[0]

# here, we're defining a function that uses the shoelace formula to calculate the area of any
# convex or concave polygon defined by a list of points
def shoelace(points):
  # first, we set the area to 0
  area = 0

  for i in range(len(points)):
    # then, for every consecutive pairing of points, we add the cross product between those 
    # two points to our area. however, we need this to loop back to the start for the last point
    # in the list, so we can simply use an if-else block to handle that case
    if i < len(points)-1:
      area += cross(points[i], points[i+1])
    else:
      area += cross(points[i], points[0])
  
  # since the shoelace formula gives us 2*area, we need to divide by 2 before returning it
  area /= 2
  return area

# lastly, we define our main function
def main():
  # first, we get user input for the vertices as a string
  raw_point_str = input('Please enter the vertices: ')
  
  # next, we use our getpoints function to convert that raw inputted string to a list of points
  points = getpoints(raw_point_str)

  # lastly, we call the shoelace function to calculate the area of the polygon defined by those points and return it
  area = shoelace(points)
  print(f'The area of the polygon is {area:.1f}')

if __name__ == '__main__':
  main()