from django.db import models
from django.utils.translation import gettext
from django.templatetags.static import static
from django.contrib.auth.models import User


class Hemis_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()


class Moodle_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()


class KeroControl_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_self_visible = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = gettext('Profile')
        verbose_name_plural = gettext('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('img/team/default-profile-picture.png')


class Position(models.Model):  # Lavozimlar va talabalar
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Bolim(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class System(models.Model):  # hemis, moodle va kero control
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Hemisid(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Moodle(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Kerocontrol(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Username(models.Model):  # foydalanuvchi
    full_name = models.CharField(max_length=150, null=True, blank=True)
    # admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_ariza')  # Bu yerda "Admin" ning ma'lumotlarini saqlaydigan modelni ko'rsatishingiz kerak
    pasport = models.FileField(upload_to='file/user_pasport', null=True)
    image = models.ImageField(upload_to='img/user_img', null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=13, null=True)
    text = models.TextField()
    javob = models.TextField(blank=True, null=True)
    creatad = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Ariza {self.id} - {self.foydalanuvchi}'
