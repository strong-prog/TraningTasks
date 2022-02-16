"""
Калькулятор площадей геометрических фигур.
Интерфейс версия. Черновик.
"""

import math
from tkinter import *


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


class BaseWindow:
    shape_key = None
    shape_class = None
    shape_params = None
    txt = None
    shape_txt = None
    shape_title = None

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

    def __init__(self):
        self.window = Tk()
        self.window.title('Калькулятор площадей фигур')
        self.window.geometry('297x250')

    def set_shape(self):
        self.shape_title = self.shape_txt
        print(f'self.shape_title {self.shape_title}')
        temp_dict = {shape_class.title: key for key, shape_class in self.shapes.items()}
        self.shape_key = temp_dict[self.shape_title]
        print(f'self.shape_key {self.shape_key}')
        self.shape_class = self.shapes[self.shape_key]
        print(f'self.shape_class {self.shape_class}')
        self.shape_params = self.shapes_params[self.shape_key]
        print(f'self.shape_params {self.shape_params}')

        self.input_shape_params()

    def input_shape(self):
        label = Label(self.window, text='Выберите фигуру')
        label.grid(column=0, row=0, columnspan=2)

        button = []

        for txt in self.shapes.values():
            self.shape_txt = txt.title
            button.append(Button(self.window, text=txt.title, command=self.set_shape, width=15, height=1))

        print(button)
        count = 1
        for pos in range(len(self.shapes)):
            if pos % 2 == 0:
                button[pos].grid(column=0, row=count)
            else:
                button[pos].grid(column=1, row=count - 1)
            count += 1
        self.window.mainloop()

    def click(self):
        print(f'f{self.txt.get()}')

    def click_back(self):
        self.window.destroy()
        self.__init__()
        self.input_shape()

    def input_shape_params(self):

        self.window.destroy()
        self.__init__()

        label = Label(self.window, text=f'Введите параметры фигуры {self.shape_title}')
        label.grid(column=0, row=1, columnspan=2)

        count = 2
        for key, value in self.shape_params.items():
            print(key, value)
            label_value = Label(self.window, text=key)
            label_value.grid(column=0, row=count)
            self.txt = Entry(self.window, width=10)
            self.txt.grid(column=1, row=count)
            count += 1

        btn = Button(self.window, text='Вычислить', command=self.click, width=8, height=1)
        btn.grid(column=1, row=count)

        btn_back = Button(self.window, text='Назад', command=self.click_back, width=8, height=1)
        btn_back.grid(column=0, row=count)

        self.window.mainloop()


window = BaseWindow()
window.input_shape()
