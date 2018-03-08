from .models import Person

class UserAuthentificacionBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = Person.objects.get(username=username)
            # en este punto, debes verificar la contraseña, yo lo hare como lo hace el modelo de usuario de django, siguiendo los metodos que trae este
            if user.check_password(password):
                return user
        except Person.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Person.objects.get(id=user_id)
        except:
            return None