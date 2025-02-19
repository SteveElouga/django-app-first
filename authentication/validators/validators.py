import re
from django.core.exceptions import ValidationError


class ContainsSpecialCharacterValidator:
    def validate(self, password, user=None):
        if bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]"), password):
            raise ValidationError('Le mot de passe doit contenir au moins au caratere special')
        
    def get_help_text(self):
        return 'Le mot de passe doit contenir au moins au caratere special. Exemple: !@#$%^&*(),.?":{}|<>'