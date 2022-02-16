"""
Калькулятор площадей геометрических фигур.
Консольная версия.
"""

import math


class Shape:
    title = 'Фигура'

    def area(self):
        pass

    def volume(self):
        pass


class Pyramid(Shape):
    title = 'Пирамида'

    def __init__(self, base, side, height):
        self.a = base
        self.n = side
        self.h = height

    def area(self):
        return (self.n * self.a / 2) * ((self.a / (2 * math.tan(180 / self.n))) + (
                self.h ** 2 + (self.a / (2 * math.tan(180 / self.n))) ** 2) ** 0.5)


class Trapezoid(Shape):
    title = 'Трапеция'

    def __init__(self, upper, bottom, height):
        self.upper = upper
        self.bottom = bottom
        self.height = height

    def area(self):
        return (self.upper + self.bottom) * self.height * 0.5


class Cone(Shape):
    title = 'Конус'

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return (self.radius + self.height) * self.radius * math.pi


class Cylinder(Cone):
    title = 'Цилиндр'

    def area(self):
        return super().area() * 2


class Rectangle(Shape):
    title = 'Прямоугольник'

    def __init__(self, width, length):
        self.width = width
        self.length = length

    @staticmethod
    def _area_rectangle(a, b):
        return a * b

    def area(self):
        return self._area_rectangle(self.width, self.length)


class Triangle(Rectangle):
    title = 'Треугольник'

    def __init__(self, base, height):
        super().__init__(width=base, length=height)

    def area(self):
        return (self._area_rectangle(self.width, self.length)) * 0.5


class Rhombus(Rectangle):
    title = 'Ромб'

    def __init__(self, base, height):
        super().__init__(width=base, length=height)


class Parallelepiped(Rectangle):
    """Полиморфизм"""

    title = 'Параллелепипед'

    def __init__(self, width, length, height):
        super().__init__(width=width, length=length)
        self.height = height

    def area(self):
        return (self._area_rectangle(self.width, self.length) + self._area_rectangle(self.length, self.height) +
                self._area_rectangle(self.height, self.width)) * 2


class Square(Rectangle):
    """Наследование"""

    title = 'Квадрат'

    def __init__(self, width):
        super().__init__(width=width, length=width)


class Cube(Square):
    title = 'Куб'

    def area(self):
        return super().area() * 6


class Circle(Square):
    title = 'Круг'

    def __init__(self, radius):
        super().__init__(width=radius)

    def area(self):
        return super().area() * math.pi


class Sphere(Circle):
    title = 'Сфера'

    def area(self):
        return super().area() * 4


class BaseClass:
    shape = None
    params = {}

    shapes = {
        'cube': Cube,
        'parallelepiped': Parallelepiped,
        'square': Square,
        'rectangle': Rectangle,
        'triangle': Triangle,
        'rhombus': Rhombus,
        'circle': Circle,
        'sphere': Sphere,
        'cone': Cone,
        'cylinder': Cylinder,
        'trapezoid': Trapezoid,
        'pyramid': Pyramid,
    }

    shapes_params = {
        'cube': {'width': None},
        'parallelepiped': {'width': None, 'length': None, 'height': None},
        'square': {'width': None},
        'rectangle': {'width': None, 'length': None},
        'triangle': {'base': None, 'height': None},
        'rhombus': {'base': None, 'height': None},
        'circle': {'radius': None},
        'sphere': {'radius': None},
        'cone': {'radius': None, 'height': None},
        'cylinder': {'radius': None, 'height': None},
        'trapezoid': {'upper': None, 'bottom': None, 'height': None},
        'pyramid': {'base': None, 'side': None, 'height': None},
    }

    def get_shape(self):
        self.shape = input(f'Введите одну из фигур: {", ".join(list(self.shapes.keys()))}\n:')

    def get_shape_params(self):
        return self.shapes_params[self.shape]

    def get_params(self, shape_params):
        for param in shape_params.keys():
            p = int(input(f'Введите параметр {param}\n:'))
            self.params[param] = p

    def get_area(self):
        shape_class = self.shapes[self.shape]
        area = shape_class(**self.params).area()
        print(f'Площадь фигуры:\n{area}')

    def start(self):
        self.get_shape()
        shape_params = self.get_shape_params()
        self.get_params(shape_params)
        self.get_area()


shape = BaseClass()
shape.start()
