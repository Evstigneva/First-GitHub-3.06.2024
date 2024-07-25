from dataclasses import dataclass, field
from random import choice


def choice_color():
    print('Start choice')
    colors = ['black', 'white', 'red', 'green']
    return choice(colors)


@dataclass
class InventoryItem:
    name: str
    quantity: int = field(default=1)
    price: float = field(default=9.99)
    color: str = field(default_factory=choice_color)


desk = InventoryItem('Computer desk')
monitor = InventoryItem('Monitor', 300)
monitor_blue = InventoryItem('Monitor', 300, color='blue')
print(desk)
print(monitor)
print(monitor_blue)