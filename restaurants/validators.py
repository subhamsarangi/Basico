from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

CATEGORIES=['American', 'Indian', 'Asian', 'Bakery', 'Asian Fusion',
'Bengali','South Indian','Chinese','Italian','French','Continental',
'North Indian', 'Mexican','Sardinian']

def validate_category(value):
    value=value.capitalize()
    if value not in CATEGORIES:
        raise ValidationError("Not valid category")
