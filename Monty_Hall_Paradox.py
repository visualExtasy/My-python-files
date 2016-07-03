# The description of this paradox is on Wikipedia page
# https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%B4%D0%BE%D0%BA%D1%81_%D0%9C%D0%BE%D0%BD%D1%82%D0%B8_%D0%A5%D0%BE%D0%BB%D0%BB%D0%B0
# https://en.wikipedia.org/wiki/Monty_Hall_problem
import random

car = 0
for i in range(1000):
    doors = [1, 2, 3]
    win = random.choice(doors)
    if win == 1:
        doors.pop(random.choice([1,2]))
    elif win == 2:
        doors.pop(2)
    elif win == 3:
        doors.pop(1)
    if doors[1] == win:
        car += 1
print car/1000.0
