from django.db import models

# Create your models here.
class news(models.Model):
    title=models.TextField()
    def __unicode__(self):
        return self.title
class content(models.Model):
    content=models.TextField()
    title = models.TextField()
    def __unicode__(self):
        return (self.content,self.title)
