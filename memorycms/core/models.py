from django.contrib.contenttypes.models import ContentType
from django.db import models

class App(models.Model):
    title = models.CharField(max_length = 255,default='')
    top_entity = models.ForeignKey('EntityBase', null=True)

class EntityBase(models.Model):
    entity_types = models.ManyToManyField('EntityTypeBase')
    @property
    def is_group(self):
        return self.entity_types.filter(is_group=True).exists()


class EntityTypeBase(models.Model):
    is_group = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, editable=False, null=True)

    def save(self, *args, **kwargs):
        if(not self.content_type):
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        super(EntityTypeBase, self).save(*args, **kwargs)

    def get_top_class(self):
        content_type = self.content_type
        model = content_type.model_class()
        if(model == EntityTypeBase):
            return self
        return model.objects.get(id=self.id)

class EntityTypeString(EntityTypeBase):
    content = models.CharField(max_length = 255,default='')
    def __unicode__(self):
        return '%d: %s' % (self.pk, self.content)


class EntityTypeText(EntityTypeBase):
    content = models.TextField(default='')
    def __unicode__(self):
        return '%d: %s' % (self.pk, self.content)

class EntityTypeEntityGroup(EntityTypeBase):
    #TODO how to get the name from the group
    content = models.ManyToManyField('EntityBase')
    def __init__(self, *args, **kwargs):
        super(EntityTypeEntityGroup, self).__init__(*args, **kwargs)
        self.is_group = True
