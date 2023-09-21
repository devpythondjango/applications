from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Hemis_admin, Moodle_admin, KeroControl_admin

@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_admin:
            if instance.admin_type == 'hemis':
                Hemis_admin.objects.create(user=instance.user)
            elif instance.admin_type == 'moodle':
                Moodle_admin.objects.create(user=instance.user)
            elif instance.admin_type == 'kerocontrol':
                KeroControl_admin.objects.create(user=instance.user)
