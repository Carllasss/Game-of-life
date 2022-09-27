from django.db import models


class Cells(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return self.x, self.y
