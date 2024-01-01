# models.py
from django.db import models

class Data(models.Model):
    Nama_Lengkap = models.CharField(max_length=100)
    Panggilan = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Panggilan}, {self.Nama_Lengkap}"
