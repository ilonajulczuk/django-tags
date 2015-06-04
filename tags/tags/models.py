from django.db import models


class Tag(models.Model):
    """Tag for data. Every tag has unique text.
    """
    text = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return 'Tag[id: {id}, text: {text}]'.format(
            id=self.id, text=self.text)


class Library(models.Model):
    """Library represents a piece of software. It has its website url,
    name, description and as many tags as you like.
    """

    # django has a nice field that validates URLs
    url = models.URLField()

    # name should be in a slug form
    name = models.SlugField(max_length=80)
    description = models.CharField(max_length=256, blank=True)
    tags = models.ManyToManyField(Tag, related_name='libraries')

    def __str__(self):
        return 'Library[id: {id}, name: {name}]'.format(
            id=self.id, name=self.name)
