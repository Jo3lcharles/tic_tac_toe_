import doctest

class Rectangle:
    """ A class for rectangles"""

    def __init__(self, length: float, width:float)-> None:
        """
        The construcgtor of the rectangle class

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1._length
        4.6
        >>> rectangle_1._width
        1.2

        """
        assert isinstance(length, float) and length > 0, "length is not a positive float"
        assert isinstance(width, float) and width > 0, "width is not a positive float"

        self._length = length
        self._width = width

    def calculate_area(self) -> float:
            """"
            A class method that calculate the area of the rectangle 

            >>> rectangle_1 = Rectangle(4.6, 1.2)
            >>> rectangle_1.calculate_area()
            5.52
            """
            return self._length * self._width
        
    def calculate_perimeter(self) -> float:
            """"
            A class method that calculate the perimeter of the rectangle 

            >>> rectangle_1 = Rectangle(4.6, 1.2)
            >>> rectangle_1.calculate_perimeter()
            11.6
            """
            return 2 * (self._length + self._width)
        
    def get_length(self) -> float:

            """
            a class metgod that get the value of the length

            >>> rectangle_1 = Rectangle(4.6, 1.2)
            >>> rectangle_1.get_length()
            4.6
            """

            return self._length
        
    def set_length(self, length: float)-> float:
            """
            A class method taht set the value of the length

            >>> rectangle_1 = Rectangle(4.6, 1.2)
            >>> rectangle_1.set_length(1.3)
            >>> rectangle_1._length
            1.3
            """
            assert isinstance(length, float) and length > 0 , "length is not a positive float"

            self._length = length

    def get_width(self) -> float:

            """
            a class method that get the value of the width

            >>> rectangle_1 = Rectangle(4.6, 1.2)
            >>> rectangle_1.get_width()
            1.2
            """

            return self._width
        
    def set_width(self, width: float)-> float:
            """
            A class method taht set the value of the width

            >>> rectangle_1 = Rectangle(4.6, 1.2)
            >>> rectangle_1.set_width(1.3)
            >>> rectangle_1._width
            1.3
            """
            assert isinstance(width, float) and width > 0 , "width is not a positive float"

            self._width = width


doctest.testmod()

