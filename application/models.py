from django.db import models
from django.contrib.auth.models import AbstractUser

class Position(models.Model):  # Lavozimlar va talabalar
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Bolim(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class System(models.Model):  # hemis, moodle va kero control
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Hemisid(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Moodle(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Kerocontrol(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Username(models.Model):  # foydalanuvchi
    full_name = models.CharField(max_length=150, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    hemisid = models.CharField(max_length=12, null=True)
    group = models.CharField(max_length=10, null=True)
    pasport = models.FileField(upload_to='file/user_pasport', null=True)
    phone = models.CharField(max_length=13, null=True)
    image = models.ImageField(upload_to='img/user_img', null=True)
    text = models.TextField()
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True)
    creatad = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name
