from figure import Figure
import math

class Circle(Figure):
    def __init__(self, R):
        if R <= 0:
            raise ValueError("Радиус круга должен быть положительным числом")

        self.R = R

    @property
    def get_area(self):
        return math.pi * self.R ** 2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.R

