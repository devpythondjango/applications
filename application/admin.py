from django.contrib import admin
from .models import (
    Position, Group, Kafedra, Bolim,
    System, Hemisid, Moodle, Kerocontrol,
    Username, Hemis_admin, KeroControl_admin,
    Moodle_admin
)
# Register your models here.
admin.site.register(Position)
admin.site.register(Group)
admin.site.register(Kafedra)
admin.site.register(Bolim)
admin.site.register(System)
admin.site.register(Hemisid)
admin.site.register(Moodle)
admin.site.register(Kerocontrol)
admin.site.register(Username)
admin.site.register(Hemis_admin)
admin.site.register(KeroControl_admin)
admin.site.register(Moodle_admin)
