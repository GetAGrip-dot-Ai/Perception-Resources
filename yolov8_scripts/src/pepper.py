from yolov8_scripts.src.pepper_peduncle import PepperPeduncle
from yolov8_scripts.src.pepper_fruit import PepperFruit
class Pepper:
    def __init__(self, number:int, pf_number: int, pp_number: int):
        self._number = number

        self._pepper_fruit: PepperFruit = PepperFruit(pf_number)
        self._pepper_peduncle: PepperPeduncle = PepperPeduncle(pp_number)

    @property
    def number(self):
        return self._number
    @property
    def pepper_fruit(self):
        return self._pepper_fruit
    @pepper_fruit.setter
    def pepper_fruit(self, value):
        self._pepper_fruit = value
    @property
    def pepper_peduncle(self):
        return self._pepper_peduncle
    @pepper_peduncle.setter
    def pepper_peduncle(self, value):
        self._pepper_peduncle = value
    def __str__(self):
        return f"Pepper #{self.number}"

