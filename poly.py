class Point:
    def __init__(self, x: float = None, y: float = None):
        # Initialize a point with x and y coordinates
        self.__x = x
        self.__y = y
        self.next = None  # This will be used for the linked list

    def valid(self):
        # Check if x and y are either int or float
        return isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float))

    def __str__(self):
        # Return the point as a string in the format (x, y)
        return f"({self.__x}, {self.__y})"

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Polygon:
    def __init__(self):
        self.__sides = 0
        self.__vertices = 0
        self.__head = Point()  # A null point for the head node of the linked list

    def add_point(self, x: float, y: float):
        new_point = Point(x, y)  # Create a new Point object
        if self.__vertices == 0:
            self.__head.next = new_point  # Set the first point as head.next
        else:
            current = self.__head.next
            while current.next is not None:
                current = current.next  # Traverse to the end of the list
            current.next = new_point  # Link the last point to the new point

        self.__vertices += 1  # Count the number of vertices

    def __str__(self):
        # Traverse the linked list and print all points in the required format
        points_str = []
        current = self.__head.next  # Skip the null head point
        while current is not None:
            points_str.append(str(current))  # Convert point to string and append
            current = current.next
        return " -> ".join(points_str)  # Join all points with "->"

