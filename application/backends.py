from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminProfileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.is_active and self._is_admin_profile(user):
            if user.check_password(password):
                return user

        return None

    @staticmethod
    def _is_admin_profile(user):
        return hasattr(user, 'Hemis_admin') or hasattr(user, 'Moodle_admin') or hasattr(user, 'KeroControl_admin')
