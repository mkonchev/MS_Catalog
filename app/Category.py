from enum import Enum


class Category(str, Enum):
    clothes = "Одежда"
    food = "Еда"
    another = "Другие"
