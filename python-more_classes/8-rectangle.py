#!/usr/bin/python3
""" Class that defines a rectangle """


class Rectangle:
    """ A class used to represent a Rectangle

    Attribute:
        number_of_instances(int): The number of Rectangle instances.
        print_symbol(any type): The symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __init__ method

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.

        Attributes:
            __width(int): The width of the rectangle.
            __height(int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Get the width of the rectangle

            return:
                the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle

        Args:
            value(int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle

            return:
                the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle

        Args:
            value(int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ method that returns the rectangle area

        Return:
            rectangle area
        """

        return self.__width * self.__height

    def perimeter(self):
        """ method that returns the rectangle perimeter

        Return:
            rectangle perimeter
        """

        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle string with the character # """

        rectangle = ""
        if self.width == 0 or self.height == 0:
            pass
        else:
            for index in range(self.height):
                rectangle += (str(self.print_symbol) * self.width)
                if index != self.height - 1:
                    rectangle += "\n"

        return rectangle

    def __repr__(self):
        """ return a string representation of the rectangle """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """ print the message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method: return the biggest rectangle based on the area

        Args:
            rect_1: The instance of Rectangle.
            rect_2: The instance of Rectangle.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.

        Return:
            The biggest rectangle based on the area.  
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
