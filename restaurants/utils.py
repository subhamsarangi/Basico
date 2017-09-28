import random
import string
from django.utils.text import slugify

DONT_USE = ['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    slug = slugify(instance.title)
    new_slug =  "{slug}-{randstr}".format(
                slug=slug,
                randstr=random_string_generator(size=5)
            )
    return new_slug
