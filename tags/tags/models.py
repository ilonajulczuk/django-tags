from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return '[id: {id}, text: {text}]'.format(id=self.id, text=self.text)



class Library(models.Model):
    url = models.URLField()
    name = models.SlugField(max_length=80)
    description = models.CharField(max_length=256, blank=True)
    tags = models.ManyToManyField(Tag, related_name='libraries')

    def __str__(self):
        return '[id: {id}, name: {name}]'.format(id=self.id, name=self.name)
