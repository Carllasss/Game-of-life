from collections import defaultdict
from random import random

from django.db import transaction

import config
from .models import Cells

width = config.WIDTH - 1
height = config.HEIGHT - 1


def get_neighbours(x: int, y: int):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0),
               (1, 0), (-1, 1), (0, 1), (1, 1)]
    alive = []
    possible_neighbours = {(x + x_add, y + y_add) for x_add, y_add in offsets}
    with transaction.atomic():
        for i in possible_neighbours:
            if Cells.objects.filter(x=i[0], y=i[1]):
                alive.append((i[0], i[1]))
    return possible_neighbours, alive


@transaction.atomic
def upgrade_grid():
    grid = []
    try:
        Cells.objects.get()
    except Cells.MultipleObjectsReturned:
        pass
    except Cells.DoesNotExist:
        for row in range(height):
            grid.append([])
            for column in range(width):
                grid[row].append(1 if random() < 15 / 100 else 0)
        j = 0
        for x in grid:
            i = 0
            for y in x:
                if y == 1:
                    cell = Cells(x=j, y=i)
                    cell.save()
                i += 1
            j += 1
    undead = defaultdict(int)
    for cell in Cells.objects.all():
        x, y = cell.x, cell.y
        dead_neighbours, alive_neighbourse = get_neighbours(x, y)
        if len(alive_neighbourse) not in [2, 3]:
            cell.delete()

        for pos in dead_neighbours:
            undead[pos] += 1
    for pos, _ in filter(lambda elem: elem[1] == 3, undead.items()):
        x = pos[0]
        y = pos[1]
        if x == -1:
            x = height
        if y == -1:
            y = width
        if not Cells.objects.filter(x=x, y=y):
            cell = Cells(x=x, y=y)
            cell.save()
