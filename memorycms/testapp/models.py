from django.contrib.contenttypes.models import ContentType
from django.db import models

class ParentClass(models.Model):
    superclass = models.CharField(max_length = 255, blank = True)

    def save(self, *args, **kwargs):
        if not self.superclass:
            self.superclass = ContentType.objects.get_for_model(self.__class__)

        super(ParentClass, self).save(*args, **kwargs)

    def get_child(self):
        s = getattr(self, self.superclass)
        if hasattr(s, 'pk'):
            return s
        else:
            return None

class Child1(ParentClass):
    child1field = models.CharField(max_length=30, blank=True)


class Child2(ParentClass):
    child2field = models.CharField(max_length=30, blank=True)