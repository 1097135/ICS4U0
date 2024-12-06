from poly import *  # Import the Point and Polygon classes from poly.py

def getNumeric(S: str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple (x, y) where x, y are either int or float
    S = S.strip("()")  # Remove parentheses
    x, y = S.split(",")  # Split by comma
    x = float(x)  # Convert x to float
    y = float(y)  # Convert y to float
    return (x, y)

# Open the data file
with open("a2.txt", "r") as fh:
    polydata = fh.readline().strip()  # Read the first line of the file and remove extra spaces

# Split the data into individual points (strings)
points = polydata.split("),")  # Split by "),"

# Create a polygon object
polygon = Polygon()

# Loop through the points array, turn them into numbers, and add them to the polygon
for point_str in points:
    point_str = point_str.strip()  # Strip any extra spaces
    if point_str:  # Ensure it's not an empty string
        # Ensure the last point string ends with ')'
        if not point_str.endswith(')'):
            point_str += ')'
        
        # Get numeric values (x, y) for the point
        x, y = getNumeric(point_str)
        polygon.add_point(x, y)  # Add point to the polygon

# Print the entire polygon linked list as a string
print(polygon)  # This should print the entire linked list of points in the required format

