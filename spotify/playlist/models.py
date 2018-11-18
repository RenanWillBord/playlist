from django.db import models

class PlayList(models.Model):
    titulo = models.CharField(max_length=50)
    interprete= models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    letra= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # cread for upload images
    capa = models.FileField(blank=False, null=True)

    def __str__(self):
        return self.title
